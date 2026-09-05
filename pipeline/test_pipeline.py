"""流水线自检。不用测试框架：assert + 文件底部的 runner，CI 里零依赖可跑。

用法: python pipeline/test_pipeline.py
"""
import io
import json
import re
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import clips as cl
import compose as cp
import drafts as df
import main as mn
import config
import images as im
import render as rd
import evidence as ev
import manual as mnl
import notify as nt
import seed as sd
import select_ as sel
import vault
import verify as vf

FIX = Path(__file__).parent / 'fixtures'


# ---------- vault ----------

def test_parse_sci_note():
    n = vault.parse_note(FIX / 'sci-note-dsc.md', FIX)
    assert n is not None
    assert n.type == 'sci-note'
    assert '02分子表征/Biophysical-Techniques/DSC' in n.tags
    assert n.book == 'Biophysical characterization of proteins'
    assert n.images == ['DSC-curve.png'], n.images
    assert n.wikilinks == ['热容和热容差'], n.wikilinks


def test_parse_wiki_image_with_size():
    n = vault.parse_note(FIX / 'note-sec.md', FIX)
    assert n.images == ['SEC-peak.png'], n.images
    assert n.title == 'SEC 方法开发要点'
    assert n.wikilinks == [], n.wikilinks


def test_html_img_tag_normalised_to_markdown():
    """Typora 时代的 <img src="D:\...">：不归一化就既取不到图，正文里还留死链。"""
    out = vault.html_img_to_md(
        '  <img src="D:\\Knowlege\\image/202201302203668.png" alt="x" style="zoom: 50%;" />')
    assert out == '  ![](D:\\Knowlege\\image/202201302203668.png)', repr(out)
    assert vault.image_ref_name('D:\\Knowlege\\image/202201302203668.png') \
        == '202201302203668.png'


def test_zotero_escaped_img_in_alt_left_alone():
    """Zotero 导出的 alt 里塞着整段 <img>，外层已是 markdown 图片，不能套娃。"""
    src = '![\\<img src="attachments/T.png" ztype="zimage">](attachments/T.png)'
    assert vault.html_img_to_md(src) == src
    # alt 里的 HTML 不该原样输出到站上
    out = rd.rewrite_images(src, {'T.png': '/images/s/T.webp'}, [], {})
    assert out == '![](/images/s/T.webp)', out


def test_obsidian_size_suffix_stripped_from_alt():
    """`![|330](x)` 的管道符会把 GFM 表格行劈成两个单元格。"""
    assert rd.rewrite_images('![|330](../a/x.png)', {'x.png': '/images/s/x.webp'}, [], {}) \
        == '![](/images/s/x.webp)'
    assert rd.rewrite_images('![谱图|330](../a/x.png)', {'x.png': '/images/s/x.webp'}, [], {}) \
        == '![谱图](/images/s/x.webp)'


def test_parse_note_keeps_only_real_images():
    """笔记嵌入、附件、外链都不是要去 Drive 取的图。"""
    body = ('![[真图.png]]\n![[某笔记#小节]]\n![[画板.excalidraw]]\n'
            '![](https://x.com/远程.png)\n![](res\\本地图.PNG)\n')
    p = FIX / '_tmp_refs.md'
    p.write_text('---\ntitle: t\ntype: note\n---\n' + body, encoding='utf-8')
    try:
        n = vault.parse_note(p, FIX)
        # 顺序按解析顺序：先 markdown 写法后 wiki 写法
        assert n.images == ['本地图.PNG', '真图.png'], n.images
    finally:
        p.unlink()


def test_load_vault_filters_nothing_by_itself():
    notes = vault.load_vault(FIX)
    assert len(notes) == 3, len(notes)


# ---------- select_ ----------

def _fake(path, tags, type_='note'):
    return vault.Note(path=path, title=path, tags=tags, type=type_, body='正文 ' + path)


def test_publishable_excludes_clipping_type():
    pub = sel.publishable(vault.load_vault(FIX))
    assert len(pub) == 2, [n.path for n in pub]
    assert all(n.type != 'clipping' for n in pub)


def test_oversized_note_excluded():
    """单篇 158 万字符的「笔记」其实是整本书导入，一篇就撑爆上下文。"""
    big = vault.Note('book.md', 'B', ['a/b/c'], 'note',
                     body='x' * (config.MAX_NOTE_CHARS + 1))
    assert big not in sel.publishable([big])


def test_exempt_note_bypasses_size_limit():
    """作者自己写的长文不该被当成书籍转录剔除。"""
    path = next(iter(config.SIZE_EXEMPT_NOTES))
    n = vault.Note(path, 'N', ['a/b/c'], 'note',
                   body='x' * (config.MAX_NOTE_CHARS + 1))
    assert n in sel.publishable([n])


def test_exempt_list_paths_all_exist_in_vault():
    """名单里的路径写错了会静默失效 —— 那篇长文就被悄悄剔除了。"""
    root = Path('/home/user/obsidian-base')
    if not root.exists():
        return  # CI 无 vault 时跳过
    for rel in config.SIZE_EXEMPT_NOTES:
        assert (root / rel).exists(), '豁免名单路径不存在: ' + rel


def test_group_truncated_by_char_budget_not_just_count():
    """按篇数限制是错的指标：9 篇也可能加起来 170 万字符。"""
    # 20 篇 x 8 千 = 16 万，超预算 5 万；应截断而非整组丢弃
    ns = [vault.Note(f'n{i:02d}.md', f'N{i}', ['a/b/c'], 'note',
                     body='x' * 8_000) for i in range(20)]
    g = sel.build_groups(ns)[0]
    total = sum(len(n.body) for n in g.notes)
    assert total <= config.MAX_GROUP_CHARS, total
    assert config.MIN_GROUP <= len(g.notes) < 20, len(g.notes)


def test_group_dropped_when_budget_cannot_fit_min_notes():
    """预算装不下 3 篇就整组放弃，不发半截文章。

    用豁免名单里的路径构造：它们绕过单篇上限，因此能撑到组预算装不下。
    """
    paths = sorted(config.SIZE_EXEMPT_NOTES)[:3]
    ns = [vault.Note(p, 'N', ['a/b/c'], 'note', body='x' * 200_000) for p in paths]
    assert sel.build_groups(ns) == []


def test_group_by_third_level_tag():
    ns = [_fake(f'n{i}.md', ['02分子表征/PTM/糖基化']) for i in range(5)]
    gs = sel.build_groups(ns)
    assert len(gs) == 1
    assert gs[0].tag == '02分子表征/PTM/糖基化'
    assert len(gs[0].notes) == 5


def test_note_belongs_to_first_third_level_tag_only():
    """一篇笔记只进一组，否则同一内容会出现在多篇文章里。"""
    ns = [_fake(f'n{i}.md', ['00基础/文献', '02分子表征/PTM/糖基化', '03质量控制/SEC/柱效'])
          for i in range(4)]
    gs = sel.build_groups(ns)
    assert len(gs) == 1, [g.tag for g in gs]
    assert gs[0].tag == '02分子表征/PTM/糖基化'


def test_two_level_tag_used_when_no_third_level():
    ns = [_fake(f'n{i}.md', ['06工艺/纯化']) for i in range(3)]
    gs = sel.build_groups(ns)
    assert len(gs) == 1 and gs[0].tag == '06工艺/纯化'


def test_sibling_subtopics_stay_separate_articles():
    """不同子题不能焊成一篇：这是「一篇文章什么都讲」的根源。

    实测归并版把 12 篇横跨定量/测序/碎裂/数据分析/离子源的笔记塞进
    「05仪器与分析技术/质谱」一篇里，出来只能是大杂烩。
    """
    ns = ([_fake(f'a{i}.md', ['02分子表征/PTM/糖基化']) for i in range(2)] +
          [_fake(f'b{i}.md', ['02分子表征/PTM/二硫键']) for i in range(2)])
    gs = sel.build_groups(ns)
    assert {g.tag: len(g.notes) for g in gs} == {
        '02分子表征/PTM/糖基化': 2, '02分子表征/PTM/二硫键': 2}, \
        {g.tag: len(g.notes) for g in gs}


def test_group_below_minimum_dropped():
    ns = [_fake('a.md', ['02分子表征/PTM/糖基化']), _fake('b.md', ['03质量控制/SEC/柱效'])]
    assert sel.build_groups(ns) == []


def test_two_level_only_notes_still_group():
    """只打了二级标签的笔记本来就没有更细的粒度，不能永久排除。"""
    ns = [_fake(f'a{i}.md', ['00基础/生物制品']) for i in range(3)]
    assert [(g.tag, len(g.notes)) for g in sel.build_groups(ns)] == [('00基础/生物制品', 3)]


def test_deeper_than_three_levels_folds_to_three():
    """四级标签折到三级：再细下去每组只剩一篇。"""
    ns = ([_fake(f'a{i}.md', ['02分子表征/PTM/糖基化/N-糖']) for i in range(2)] +
          [_fake(f'b{i}.md', ['02分子表征/PTM/糖基化/O-糖']) for i in range(2)])
    gs = sel.build_groups(ns)
    assert [(g.tag, len(g.notes)) for g in gs] == [('02分子表征/PTM/糖基化', 4)]
    assert len(set(g.slug for g in gs)) == len(gs), 'slug 撞车会让后写的文章静默覆盖先写的'


def test_oversized_group_truncated_to_max():
    ns = [_fake(f'n{i:03d}.md', ['02分子表征/PTM/糖基化']) for i in range(40)]
    assert len(sel.build_groups(ns)[0].notes) == 30


def test_pick_next_skips_published_unchanged():
    ns = [_fake(f'n{i}.md', ['02分子表征/PTM/糖基化']) for i in range(5)]
    g = sel.build_groups(ns)[0]
    assert sel.pick_next(
        [g], {g.slug: {'tag': g.tag, 'source_hash': g.source_hash, 'slug': g.slug}}) is None
    assert sel.pick_next([g], {}) is g


def test_pick_next_honours_skip_set():
    """校验失败的组不跳过就会永久霸占队首，后面的文章一篇也发不出去。"""
    ns = [_fake(f'n{i}.md', ['02分子表征/PTM/糖基化']) for i in range(5)]
    ns += [_fake(f'm{i}.md', ['03质量控制/SEC/柱效']) for i in range(4)]
    gs = sel.build_groups(ns)
    first = sel.pick_next(gs, {})
    second = sel.pick_next(gs, {}, skip={first.tag})
    assert second is not None and second.tag != first.tag


def test_verify_image_check_survives_url_encoding():
    """Obsidian 粘贴的图片名带空格，正文里是 %20 编码，basename 是解码的。"""
    src = '![](../x/Pasted image 20240528.png)'
    out = '![](../x/Pasted%20image%2020240528.png)'
    assert vf.verify(src, out * 3, ['Pasted image 20240528.png']).ok


def test_pick_next_returns_changed_group():
    """笔记更新导致哈希变化时该组可重发。"""
    ns = [_fake(f'n{i}.md', ['02分子表征/PTM/糖基化']) for i in range(5)]
    g = sel.build_groups(ns)[0]
    assert sel.pick_next(
        [g], {g.slug: {'tag': g.tag, 'source_hash': 'sha256:stale', 'slug': g.slug}}) is g


# ---------- verify（本项目最关键的模块）----------

SRC = ("SEC 柱温设为 25 °C，流速 0.5 mL/min，进样量 20 μL，"
       "参考 ICH Q6B 和 21 CFR 211.194。\n"
       "分子量约 148000 Da，回收率 95%。本文分为 3 个部分讨论。\n"
       "![](../image&attachment/image-laptop/XTEN-1.png)\n") * 4
IMGS = ['XTEN-1.png']


def test_verify_passes_identical():
    assert vf.verify(SRC, SRC, IMGS).ok


def test_numbers_adjacent_to_chinese_are_seen():
    """紧挨汉字的数字必须提取得到 —— Python 的 \\w 把汉字算词字符，
    用它当边界会让中文正文里的多数数据对校验器不可见。"""
    nums = vf.data_numbers('准确度在1.5倍至1.8倍范围内，流速0.05 mL/min，回收率95%。')
    # 带单位的一律连单位一起提取（0.05 mL 而不是裸 0.05）：同一个量不能因为
    # 空格与否得到两个 token，详见 test_unit_binds_regardless_of_spacing
    assert {'1.5', '1.8', '0.05ml', '95%'} <= nums, nums
    # 反过来不能把长数字切开：18.5 里不该冒出 8.5
    assert '8.5' not in vf.data_numbers('取 IAM 18.5 mg 溶解')


def test_reformatting_alone_is_not_a_new_number():
    """模型给数字前后加空格是排版行为，不该被当成编造数据。"""
    src = '准确度在真实值的1.5倍至1.8倍范围内'
    out = '准确度在真实值的 1.5 倍至 1.8 倍范围内'
    assert vf.verify(src, out, [], min_ratio=0.1).ok


def test_numbers_from_supplied_fragments_are_not_fabrication():
    """加法模式喂进去的相关片段里的数字，模型引用了不算编造。"""
    src = '本文讨论 HCP 定量。'
    out = '本文讨论 HCP 定量。掺入量取 50 pmol。'
    assert not vf.verify(src, out, [], min_ratio=0.1).ok
    assert vf.verify(src, out, [], min_ratio=0.1,
                     extra_src='相关片段：标准品掺入量 50 pmol').ok
    # 但篇幅比例仍以引子为准，喂片段不能把「正文过短」稀释掉
    assert not vf.verify('x' * 1000, 'y' * 10, [], extra_src='z' * 100000).ok


def test_verify_catches_changed_flowrate():
    r = vf.verify(SRC, SRC.replace('0.5 mL/min', '0.8 mL/min', 1), IMGS)
    assert not r.ok and any('数据' in f for f in r.failures), r.failures


def test_verify_catches_dropped_image():
    out = SRC.replace('![](../image&attachment/image-laptop/XTEN-1.png)', '')
    r = vf.verify(SRC, out, IMGS)
    assert not r.ok and any('丢图' in f for f in r.failures), r.failures


def test_verify_catches_lost_regulation():
    """法规条款号零容忍：丢一个就是合规依据变了。"""
    r = vf.verify(SRC, SRC.replace('ICH Q6B', '相关指导原则'), IMGS)
    assert not r.ok and any('法规条款' in f for f in r.failures), r.failures


def test_verify_tolerates_small_doi_loss():
    """结构重组合并重复论述时折叠掉个别文献引用是正常的。"""
    src = SRC + ''.join(f'\n见 10.1016/j.test.{i}。' for i in range(10))
    out = src.replace('10.1016/j.test.0。', '')
    assert vf.verify(src, out, IMGS).ok


def test_doi_threshold_has_absolute_floor():
    """小分母失真：只有 3 条 DOI 时丢 1 条是 33%，但这在重组里完全正常。"""
    src = SRC + '\n见 10.1016/a.1、10.1016/a.2、10.1016/a.3。'
    out = src.replace('10.1016/a.1、', '')
    assert vf.verify(src, out, IMGS).ok, vf.verify(src, out, IMGS).failures


def test_verify_catches_bulk_doi_loss():
    """但整批文献引用消失说明 AI 把参考内容整段丢了。"""
    src = SRC + ''.join(f'\n见 10.1016/j.test.{i}。' for i in range(10))
    out = SRC
    r = vf.verify(src, out, IMGS)
    assert not r.ok and any('文献引用过多' in f for f in r.failures), r.failures


def test_ampere_not_matched_as_unit():
    """HPLC 的「流动相 A」不能被当成安培数值。"""
    assert vf.data_numbers('梯度 36A 到 88A') == set()


def test_verify_catches_truncation():
    r = vf.verify(SRC, SRC[:len(SRC) // 5], IMGS)
    assert not r.ok and any('过短' in f for f in r.failures), r.failures


def test_verify_catches_changed_molecular_weight():
    r = vf.verify(SRC, SRC.replace('148000', '148500'), IMGS)
    assert not r.ok and any('数据' in f for f in r.failures), r.failures


def test_verify_catches_changed_recovery():
    r = vf.verify(SRC, SRC.replace('95%', '98%'), IMGS)
    assert not r.ok and any('数据' in f for f in r.failures), r.failures


def test_verify_allows_ai_framing_integers():
    """AI 写导读必然产生新的小整数。这里误报的话校验器天天误杀，等于废掉。"""
    assert vf.verify(SRC, SRC + '\n本文将从 5 个角度展开，共 2 类方法。\n', IMGS).ok


def test_verify_allows_dropping_redundant_numbers():
    """重组时删掉重复论述是正常的，数字变少不该报错。"""
    assert vf.verify(SRC, SRC.replace('回收率 95%。', '', 2), IMGS).ok


def test_data_numbers_ignores_bare_small_int():
    assert vf.data_numbers('分为 3 类') == set()
    assert '25°c' in vf.data_numbers('柱温 25 °C')
    # 单位跟着数值走，不再因为中间有没有空格而分成两种 token
    assert '0.5ml' in vf.data_numbers('流速 0.5 mL/min')
    assert '148000da' in vf.data_numbers('分子量 148000 Da')


def test_citations_recognises_common_formats():
    t = '见 ICH Q2(R2)、21 CFR 211.194、USP <1058> 与 doi:10.1016/j.chroma.2020.461234'
    assert len(vf.regulations(t)) == 3, vf.regulations(t)
    assert len(vf.dois(t)) == 1, vf.dois(t)


def test_doi_regex_stops_at_markdown_syntax():
    """\\S+ 会把 markdown 链接语法一起吞掉，同一 DOI 因上下文不同提取出不同串。"""
    a = vf.dois('[10.1021/pr4010019](https://doi.org/10.1021/pr4010019)')
    b = vf.dois('参考 10.1021/pr4010019。')
    assert a == b == {'10.1021/pr4010019'}, (a, b)


# ---------- verify：误报治理（每条都有语料实测支撑）----------
#
# 语料实测（209 篇可发布笔记，1,503,893 字符）：提取器抓到的 13,624 个
# 「数据」token 里约 44% 根本不是测量值 —— 1,677 个裸年份、972 个图片文件名
# 时间戳、643 个 DOI 前缀，其余大量是参考文献的卷号页码。下面每条都是拿这份
# 实测数据定的，且都只动「什么算数据」，不动「拦不拦」的判定。

def test_unit_binds_regardless_of_spacing():
    """同一个量不能因为空格与否得到两个 token。

    实测踩坑：源笔记写「分析物＜4000Da」（粘连）提取成 4000da，而
    「分子量 148000 Da」（带空格）提取成裸 148000 —— 同类量两种口径。
    结果模型把 4000Da 复述成「4000 道尔顿」就被判成编造数据（HPLC 那篇
    实测复现）。改成单位分支优先绑定，两种写法都带单位。
    """
    assert vf.data_numbers('分析物＜4000Da') == vf.data_numbers('分析物 < 4000 Da')
    assert '4000da' in vf.data_numbers('分析物＜4000Da')
    assert '148000da' in vf.data_numbers('分子量 148000 Da')


def test_unit_swap_still_caught_after_binding():
    """单位绑定优先反而更严：小数换单位以前看不见，现在拦得住。"""
    assert not vf.verify('流速 0.5 mL/min', '流速 0.5 L/min', [], min_ratio=0.1).ok


def test_dropped_unit_is_not_fabrication():
    """模型把单位省掉或改用中文写，是复述不是编造 —— 数值本身源文有。"""
    assert vf.verify('分析物＜4000Da', '分析物小于 4000 道尔顿', [], min_ratio=0.1).ok
    # 反过来不成立：源文 50 mM，输出 50 pmol 是单位调包，必须拦。
    # 实测真出现过（label-free 那篇），所以裸数字匹配只能是单向的。
    assert not vf.verify('加入 50 mM IAA', '掺入 50 pmol 标准品', [], min_ratio=0.1).ok


def test_attaching_a_unit_to_a_bare_source_value_is_not_fabrication():
    """源文裸写的数值，模型补上上下文里明确的单位，是复述不是编造。

    实测踩坑（master 上手动触发 publish 抓到的回归）：源笔记写
    「precursor mass is 574.3」，旁边就是「573.3Da（574.3-1）」，模型写
    小标题时补成「案例一：574.3 Da 单电荷前体」—— 被判成编造数据。
    旧版校验器在这篇上一个都没拦，是这次改动引入的新误报。

    判定改成：数值本身源文没有 → 拦；数值有、且源文就是裸写的 → 放行
    （补单位或去单位都算复述）；数值有、但源文只带着别的单位 → 拦（调包）。
    """
    assert vf.verify('precursor mass is 574.3，完整多肽离子质量为 573.3Da',
                     '案例一：574.3 Da 单电荷前体', [], min_ratio=0.1).ok


def test_unit_swap_still_caught_when_source_never_wrote_it_bare():
    """源文只以「50 mM」出现过，输出改成「50 pmol」仍然是调包，必须拦。

    这条和上一条是一体两面：放行的前提是源文本身裸写过这个值。
    """
    assert not vf.verify('加入 50 mM IAA', '掺入 50 pmol 标准品', [], min_ratio=0.1).ok
    assert not vf.verify('流速 0.5 mL/min', '流速 0.5 L/min', [], min_ratio=0.1).ok


def test_micro_and_celsius_variants_are_the_same_number():
    """µ(U+00B5) 与 μ(U+03BC)、℃(U+2103) 与 °C 在语料里并存
    （实测 127 vs 588、168 vs 198），是字符编码差异不是数据差异。"""
    assert vf.data_numbers('取 1µg') == vf.data_numbers('取 1μg')
    assert vf.data_numbers('孵育 25℃') == vf.data_numbers('孵育 25 °C')
    assert vf.verify('37℃ 水浴，加 20µL', '37 °C 水浴，加 20 μL', [], min_ratio=0.1).ok


def test_link_and_doi_digits_are_not_data():
    """图片文件名与 DOI 里的数字不是实验数据，且各有更严的专属检查
    （丢图、DOI 丢失阈值）。重复计入只会制造误报。

    实测：语料里 515 个不同 token 来自链接 URL 与 DOI 串，其中大量是
    202208091746201.png 这种截图时间戳。
    """
    assert vf.data_numbers('![](../img/202208091746201.png)') == set()
    assert vf.data_numbers('见 doi:10.1016/j.chroma.2020.461234') == set()
    assert vf.data_numbers('[链接](https://x.com/a/12345/b)') == set()
    # 正文里的数据照抓不误
    assert '25°c' in vf.data_numbers('![](../img/202208091746201.png) 柱温 25 °C')
    # 但 DOI 自己的检查不受影响
    assert vf.dois('见 doi:10.1016/j.chroma.2020.461234') == {'10.1016/j.chroma.2020.461234'}


def test_bare_year_is_not_data():
    """裸年份不是测量值。规则原意是拦「编造的流速、限度、回收率」。

    实测：语料里 63 个不同裸年份 token，绝大多数来自参考文献串
    （Nature Protocols, 2007, 1, 2650–2660）；label-free 那篇被拦的
    10 个数里 4 个是年份，其中 2026 就是当天年份 —— 模型写「截至 2026 年」
    这种过渡句必然产生，把它当编造等于让校验器天天误杀。
    """
    assert vf.data_numbers('2012 年的一项研究') == set()
    assert vf.verify('本文讨论 HCP 定量。', '2017 年以来，截至 2026 年，HCP 定量……',
                     [], min_ratio=0.1).ok
    # 非年份的四位整数仍然是数据
    assert '4500' in vf.data_numbers('转速 4500')


def test_pharmacopoeia_edition_year_is_still_data():
    """药典版本年份是规范性依据，改错了是合规主张变了 —— 必须继续拦。

    这是裸年份豁免的唯一例外。语料里 10 处《中国药典》2020年版 /
    ChP 2025年版 / 2020年版起，全部带「年版」或「版」。
    """
    assert '2020' in vf.data_numbers('《中国药典》2020年版通则3407')
    assert '2025' in vf.data_numbers('参照 ChP 2025年版三部')
    r = vf.verify('依据《中国药典》2020年版', '依据《中国药典》2025年版', [], min_ratio=0.1)
    assert not r.ok and any('数据' in f for f in r.failures), r.failures


# ---------- render ----------

def test_wikilink_published_becomes_link():
    assert rd.resolve_wikilinks('详见[[热容和热容差]]。', {'热容和热容差': 'dsc-basics'}) \
        == '详见[热容和热容差](/posts/dsc-basics)。'


def test_wikilink_with_alias():
    assert rd.resolve_wikilinks('见[[热容和热容差|热容]]。', {'热容和热容差': 'dsc-basics'}) \
        == '见[热容](/posts/dsc-basics)。'


def test_wikilink_unpublished_degrades_to_plain_text():
    """不留死链：未发布的目标退化成纯文字，保留可读性。"""
    assert rd.resolve_wikilinks('详见[[某笔记]]。', {}) == '详见某笔记。'


def test_wikilink_does_not_touch_image_embeds():
    """![[...]] 是图片嵌入，不是双链，不能被当成链接处理。"""
    t = '![[../x/a.png]] 和 [[某笔记]]'
    assert rd.resolve_wikilinks(t, {}) == '![[../x/a.png]] 和 某笔记'


def test_wikilink_skips_fenced_code_block():
    """Python 嵌套列表 [['a','b']] 会被双链正则匹配，改写后代码就坏了。"""
    t = "文字[[某笔记]]\\n```python\\nx = [['及格', '不及格']]\\n```"
    out = rd.resolve_wikilinks(t, {})
    assert "[['及格', '不及格']]" in out, out
    assert '文字某笔记' in out


def test_wikilink_skips_inline_code():
    t = '见 `[[literal]]` 与 [[某笔记]]'
    out = rd.resolve_wikilinks(t, {})
    assert '`[[literal]]`' in out and '与 某笔记' in out, out


def test_image_rewrite_skips_code_block():
    t = '```\\n![](../x/a.png)\\n```'
    assert rd.rewrite_images(t, {'a.png': '/images/a.webp'}, [], {}) == t


def test_image_rewritten_to_webp_path():
    out = rd.rewrite_images('![](../image&attachment/image-laptop/SEC-peak.png)',
                            {'SEC-peak.png': '/images/sec/SEC-peak.webp'}, [], {})
    assert '/images/sec/SEC-peak.webp' in out and 'image&attachment' not in out


def test_image_wiki_embed_rewritten():
    out = rd.rewrite_images('![[../x/SEC-peak.png|600]]',
                            {'SEC-peak.png': '/images/sec/SEC-peak.webp'}, [], {})
    assert out == '![](/images/sec/SEC-peak.webp)', out


def test_url_encoded_image_name_resolved():
    """Obsidian 粘贴的图片名常含 URL 编码空格。"""
    out = rd.rewrite_images('![](../x/Pasted%20image%2020240528.png)',
                            {'Pasted image 20240528.png': '/images/a/x.webp'}, [], {})
    assert '/images/a/x.webp' in out


def test_external_image_left_untouched():
    t = '![](https://raw.githubusercontent.com/a/b/c.png)'
    assert rd.rewrite_images(t, {}, [], {}) == t


def test_missing_image_becomes_note_not_broken_img():
    out = rd.rewrite_images('![](../x/GONE.png)', {}, ['GONE.png'], {})
    assert '图片暂缺' in out and '![' not in out
    # 文件名只留在 HTML 注释里：读者看不见，补图通道认得出
    assert rd.missing_marks(out) == [('GONE.png', '')], out


def test_missing_mark_carries_caption_for_later_repair():
    out = rd.rewrite_images('![](../x/GONE.png)', {}, ['GONE.png'],
                            {'GONE.png': '图源：《某书》'})
    assert rd.missing_marks(out) == [('GONE.png', '图源：《某书》')]
    back = rd.restore_missing(out, {'GONE.png': '/images/a/GONE.webp'})
    assert back.strip() == '![](/images/a/GONE.webp)\n*图源：《某书》*', back
    assert rd.missing_marks(back) == []


def test_restore_leaves_still_missing_marks_alone():
    out = rd.rewrite_images('![](../x/GONE.png)', {}, ['GONE.png'], {})
    assert rd.restore_missing(out, {}) == out


def test_windows_separator_in_image_ref():
    """vault 里有 Windows 时期留下的 `image\\xxx.png`，反斜杠不当分隔符就丢图。"""
    assert vault.image_ref_name('../a/image\\202112141122601.png') == '202112141122601.png'
    out = rd.rewrite_images('![](../a/image\\x.png)', {'x.png': '/images/a/x.webp'}, [], {})
    assert '/images/a/x.webp' in out, out


def test_note_embed_is_not_treated_as_image():
    """![[笔记#小节]] 与图片同语法，混进来会变成假的「图片暂缺」。"""
    assert vault.image_ref_name('某笔记#某小节') is None
    out = rd.rewrite_images('![[某笔记#某小节]]', {}, [], {})
    assert out == '[[某笔记]]' and '暂缺' not in out, out
    # 退化成双链后交给 resolve_wikilinks：已发布就链过去，没发布转纯文本
    assert rd.resolve_wikilinks(out, {'某笔记': 'slug-x'}) == '[某笔记](/posts/slug-x)'


def test_non_image_attachment_embed_dropped():
    out = rd.rewrite_images('![[../Excalidraw/图.excalidraw]]', {}, [], {})
    assert out == '' and '暂缺' not in out, out


def test_image_caption_appended():
    out = rd.rewrite_images('![](../x/DSC-curve.png)',
                            {'DSC-curve.png': '/images/a/DSC-curve.webp'}, [],
                            {'DSC-curve.png': '图源：《Biophysical characterization》'})
    assert '图源：《Biophysical characterization》' in out


def test_caption_for_prefers_book_then_paper_then_link():
    N = vault.Note
    assert rd.caption_for(N('p', 't', [], 'note', book='B书')) == '图源：《B书》'
    assert rd.caption_for(N('p', 't', [], 'note', paper='P论文')) == '图源：P论文'
    assert rd.caption_for(N('p', 't', [], 'note', link='http://x')) == '图源：http://x'
    assert rd.caption_for(N('p', 't', [], 'note')) == ''


# ---------- images ----------

TMP = Path('/tmp/pipe-test')


def _png(w, h):
    from PIL import Image
    buf = io.BytesIO()
    Image.new('RGB', (w, h), 'white').save(buf, format='PNG')
    return buf.getvalue()


def test_to_webp_downscales_and_converts():
    from PIL import Image
    TMP.mkdir(parents=True, exist_ok=True)
    dest = TMP / 'out.webp'
    im.to_webp(_png(2400, 1200), dest)
    assert dest.exists()
    img = Image.open(dest)
    assert img.size == (1200, 600), img.size
    assert img.format == 'WEBP'


def test_to_webp_does_not_upscale_small_image():
    from PIL import Image
    TMP.mkdir(parents=True, exist_ok=True)
    dest = TMP / 'small.webp'
    im.to_webp(_png(300, 200), dest)
    assert Image.open(dest).size == (300, 200)


def test_to_webp_handles_palette_and_alpha():
    """Obsidian 截图常是带透明通道的 PNG，直接存 WebP 会炸。"""
    from PIL import Image
    TMP.mkdir(parents=True, exist_ok=True)
    buf = io.BytesIO()
    Image.new('RGBA', (100, 50), (255, 0, 0, 128)).save(buf, format='PNG')
    dest = TMP / 'alpha.webp'
    im.to_webp(buf.getvalue(), dest)
    assert Image.open(dest).size == (100, 50)


def test_index_cache_expires():
    TMP.mkdir(parents=True, exist_ok=True)
    cache = TMP / 'idx.json'
    cache.write_text(json.dumps({'built_at': 0, 'index': {'a.png': 'id1'}}))
    calls = []

    def factory():
        calls.append(1)
        return {'b.png': 'id2'}

    assert im.load_index(cache, factory, max_age_days=7) == {'b.png': 'id2'}
    assert calls == [1]


def test_index_cache_reused_when_fresh():
    TMP.mkdir(parents=True, exist_ok=True)
    cache = TMP / 'idx2.json'
    cache.write_text(json.dumps({'built_at': time.time(), 'index': {'a.png': 'id1'}}))

    def factory():
        raise AssertionError('缓存未过期时不应重建索引')

    assert im.load_index(cache, factory, max_age_days=7) == {'a.png': 'id1'}


def test_index_cache_rebuilds_on_corrupt_file():
    TMP.mkdir(parents=True, exist_ok=True)
    cache = TMP / 'idx3.json'
    cache.write_text('{ 这不是合法 json')
    assert im.load_index(cache, lambda: {'ok': '1'}, max_age_days=7) == {'ok': '1'}


def test_fetch_images_reports_missing_and_is_idempotent():
    """找不到的图要报出来，不能静默；已存在的图不重复下载。"""
    TMP.mkdir(parents=True, exist_ok=True)
    out = TMP / 'fetch'
    out.mkdir(exist_ok=True)
    (out / 'have.webp').write_bytes(_png(10, 10))
    downloads = []

    def fake_download(service, fid):
        downloads.append(fid)
        return _png(50, 25)

    mapping, missing = im.fetch_images(
        ['have.png', 'gone.png'], {'have.png': 'id1'}, None, out, '/images/x',
        _download=fake_download)
    assert mapping == {'have.png': '/images/x/have.webp'}, mapping
    assert missing == ['gone.png'], missing
    assert downloads == [], '已存在的图不该重新下载'


def test_image_url_escapes_spaces_and_parens():
    """图片名带空格时，裸 URL 会让整条 markdown 语法印在页面上。"""
    assert im.url_safe('Pasted image 2026.webp') == 'Pasted%20image%202026.webp'
    assert im.url_safe('a(1).webp') == 'a%281%29.webp'
    assert im.url_safe('质谱-图.webp') == '质谱-图.webp', '中文不该转义，md 源文要能读'

    TMP.mkdir(parents=True, exist_ok=True)
    out = TMP / 'urlsafe'
    out.mkdir(exist_ok=True)
    mapping, missing = im.fetch_images(
        ['Pasted image 20240528.png'], {'Pasted image 20240528.png': 'id1'}, None,
        out, '/images/x', _download=lambda service, fid: _png(20, 10))
    assert missing == []
    assert mapping == {'Pasted image 20240528.png':
                       '/images/x/Pasted%20image%2020240528.webp'}, mapping
    # 落盘文件名保持原样，只有 URL 转义
    assert (out / 'Pasted image 20240528.webp').exists()
    body = rd.rewrite_images('![[Pasted image 20240528.png]]', mapping, [], {})
    assert body == '![](/images/x/Pasted%20image%2020240528.webp)', body


def test_alias_resolves_renamed_drive_file():
    """Drive 上改了名、笔记没跟着改：别名表兜住，落盘仍用引用名。"""
    TMP.mkdir(parents=True, exist_ok=True)
    out = TMP / 'alias'
    out.mkdir(exist_ok=True)
    old, actual = '20220120182528049.png', '202201201825137.png'
    assert config.IMAGE_ALIASES[old] == actual, '别名表被改动，测试要同步'
    assert im.resolve(old, {actual: 'id9'}) == 'id9'
    assert im.resolve(old, {}) is None
    # 真有同名文件时直接命中优先，别名不抢
    assert im.resolve(old, {old: 'id-real', actual: 'id9'}) == 'id-real'

    mapping, missing = im.fetch_images(
        [old], {actual: 'id9'}, None, out, '/images/x',
        _download=lambda service, fid: _png(30, 20))
    assert missing == [] and mapping == {old: '/images/x/20220120182528049.webp'}, mapping
    assert (out / '20220120182528049.webp').exists(), '落盘用引用名，不用 Drive 上的名'


# ---------- compose ----------

def _grp(notes, tag='t/x/y'):
    return sel.Group(tag=tag, notes=notes, source_hash='h', slug='s')


def test_build_user_message_includes_all_notes_and_meta():
    ns = [vault.Note('a.md', 'A笔记', ['t/x/y'], 'note', body='正文A', book='书A'),
          vault.Note('b.md', 'B笔记', ['t/x/y'], 'note', body='正文B', paper='论文B')]
    msg = cp.build_user_message(_grp(ns))
    for token in ('正文A', '正文B', 'A笔记', 'B笔记', '书A', '论文B', 't/x/y'):
        assert token in msg, token


def test_system_prompt_carries_hard_constraints():
    for token in ('逐字原样保留', '不得引入源文中不存在', '不要输出 frontmatter',
                  '打散重组', '一个都不能少'):
        assert token in cp.SYSTEM_PROMPT, token


def test_compose_sends_system_prompt_first_and_returns_content():
    captured = {}

    def fake_post(url, headers, payload):
        captured.update(url=url, headers=headers, payload=payload)
        return {'choices': [{'message': {'content': '  ## 重组后的文章\n正文  '}}]}

    out = cp.compose(_grp([vault.Note('a.md', 'A', ['t/x/y'], 'note', body='正文A')]),
                     api_key='k', _post=fake_post)
    assert out == '## 重组后的文章\n正文'
    msgs = captured['payload']['messages']
    assert msgs[0]['role'] == 'system' and '逐字原样保留' in msgs[0]['content']
    assert msgs[1]['role'] == 'user'
    assert captured['payload']['model'] == config.DEEPSEEK_MODEL
    assert captured['headers']['Authorization'] == 'Bearer k'


def test_compose_uses_current_v4_model_not_retired_alias():
    """deepseek-chat / deepseek-reasoner 已不在 GET /models 清单里。"""
    assert config.DEEPSEEK_MODEL.startswith('deepseek-v4-'), config.DEEPSEEK_MODEL


def test_compose_max_tokens_generous_enough_for_long_article():
    """输出被截断会触发「正文过短」校验，白烧一次 token 还得重跑。"""
    assert config.DEEPSEEK_MAX_TOKENS >= 32000, config.DEEPSEEK_MAX_TOKENS


def test_compose_raises_on_malformed_response():
    def bad_post(url, headers, payload):
        return {'error': {'message': 'insufficient balance'}}
    try:
        cp.compose(_grp([vault.Note('a.md', 'A', ['t/x/y'], 'note', body='x')]),
                   api_key='k', _post=bad_post)
    except cp.ComposeError as e:
        assert 'insufficient balance' in str(e), str(e)
    else:
        raise AssertionError('响应缺少 choices 时应抛 ComposeError，不能静默返回空文章')


# ---------- main（自动通道）----------

def test_assemble_frontmatter_has_required_fields():
    ns = [vault.Note('a.md', 'A', ['02分子表征/PTM/糖基化'], 'note', book='书A'),
          vault.Note('b.md', 'B', ['02分子表征/PTM/糖基化'], 'note', link='http://x')]
    g = sel.Group(tag='02分子表征/PTM/糖基化', notes=ns, source_hash='h',
                  slug='02分子表征-ptm-糖基化')
    fm = mn.assemble_frontmatter(g, '蛋白糖基化表征', '一段导读')
    assert fm.startswith('---\n') and '\n---\n' in fm
    assert 'title: "蛋白糖基化表征"' in fm
    assert 'category: "02分子表征"' in fm
    assert '02分子表征/PTM/糖基化' in fm
    assert '书A' in fm and 'http://x' in fm
    assert 'sourceNotes:' in fm


def test_group_tags_keeps_only_shared_tags():
    """收全部标签一篇文章能挂 62 个，标签导航直接作废。"""
    ns = [vault.Note('a.md', 'A', ['共有/标签', '甲的私有'], 'note'),
          vault.Note('b.md', 'B', ['共有/标签', '乙的私有'], 'note'),
          vault.Note('c.md', 'C', ['共有/标签', '丙的私有'], 'note')]
    g = sel.Group(tag='共有/标签', notes=ns, source_hash='h', slug='s')
    assert mn._group_tags(g) == ['共有/标签']


def test_group_tags_always_includes_primary_tag():
    """主标签只在一篇里出现也要留 —— 它是这篇文章的身份。"""
    ns = [vault.Note('a.md', 'A', ['主/标/签'], 'note'),
          vault.Note('b.md', 'B', ['别的/标签'], 'note'),
          vault.Note('c.md', 'C', ['别的/标签'], 'note')]
    g = sel.Group(tag='主/标/签', notes=ns, source_hash='h', slug='s')
    tags = mn._group_tags(g)
    assert '主/标/签' in tags and '别的/标签' in tags


def test_frontmatter_actually_uses_trimmed_tags():
    """函数写了却没接进 frontmatter 是真出过的事：只测函数抓不到。"""
    import yaml as _yaml
    ns = [vault.Note(f'{i}.md', 'N', ['共有/标签', f'私有{i}'], 'note') for i in range(4)]
    g = sel.Group(tag='共有/标签', notes=ns, source_hash='h', slug='s')
    fm = _yaml.safe_load(mn.assemble_frontmatter(g, 'T').strip().strip('-'))
    assert fm['tags'] == ['共有/标签'], fm['tags']


def test_assemble_frontmatter_escapes_quotes_in_title():
    g = sel.Group(tag='a/b/c', notes=[vault.Note('a.md', 'A', ['a/b/c'], 'note')],
                  source_hash='h', slug='s')
    assert '\\"' in mn.assemble_frontmatter(g, '含"引号"的标题')


def test_assemble_frontmatter_dedupes_references():
    ns = [vault.Note(f'{i}.md', 'A', ['a/b/c'], 'note', book='同一本书')
          for i in range(3)]
    g = sel.Group(tag='a/b/c', notes=ns, source_hash='h', slug='s')
    assert mn.assemble_frontmatter(g, 'T').count('同一本书') == 1


def test_title_taken_from_h1_and_stripped_from_body():
    """H1 是文章标题，版式单独渲染，不能留在正文里重复出现一次。"""
    g = sel.Group(tag='a/b/糖基化', notes=[], source_hash='h', slug='s')
    title, body = mn.split_title('# 蛋白糖基化表征方法\n\n导读段落。\n\n## 原理\n正文', g)
    assert title == '蛋白糖基化表征方法'
    assert not body.lstrip().startswith('#'), body[:40]
    assert '## 原理' in body


def test_title_falls_back_to_h2_then_tag_leaf():
    """取 H2 只是兜底：那是第一个章节标题，会得到「HCP」这种没信息量的标题。"""
    g = sel.Group(tag='a/b/糖基化', notes=[], source_hash='h', slug='s')
    assert mn.split_title('## 只有二级标题\n正文', g)[0] == '只有二级标题'
    assert mn.split_title('没有任何标题的正文', g)[0] == '糖基化'


def test_first_paragraph_skips_headings_and_callouts():
    md = ('# 标题\n\n> [!abstract] 摘要\n> 这是 callout\n\n'
          '![](a.png)\n\n这是真正的导读段落，交代这篇文章讲什么。\n')
    d = mn.first_paragraph(md)
    assert d.startswith('这是真正的导读段落'), repr(d)
    assert 'callout' not in d


def test_first_paragraph_strips_markdown_marks():
    d = mn.first_paragraph('**加粗**的导读段落，含 [链接](http://x) 与 `代码` 标记。')
    assert '**' not in d and '](' not in d and '`' not in d, repr(d)
    assert '加粗的导读段落' in d, repr(d)


def test_empty_references_key_omitted_not_null():
    """`references:` 空着会被 YAML 解析成 null，Astro schema 直接报错。"""
    import yaml as _yaml
    g = sel.Group(tag='a/b/c', notes=[vault.Note('a.md', 'A', ['a/b/c'], 'note')],
                  source_hash='h', slug='s')
    fm = _yaml.safe_load(mn.assemble_frontmatter(g, 'T').strip().strip('-'))
    assert 'references' not in fm or fm['references'], fm.get('references')


def test_frontmatter_is_valid_yaml():
    """拼错一个引号，Astro 构建就整站失败。"""
    import yaml as _yaml
    ns = [vault.Note('a: b.md', '标题里有: 冒号', ['a/b/c'], 'note',
                     book='书名含"引号"', link='http://x?a=1&b=2')]
    g = sel.Group(tag='a/b/c', notes=ns, source_hash='h', slug='s')
    fm = mn.assemble_frontmatter(g, '标题: 带冒号和"引号"')
    parsed = _yaml.safe_load(fm.strip().strip('-'))
    assert parsed['title'] == '标题: 带冒号和"引号"', parsed['title']
    assert parsed['category'] == 'a'


def test_run_auto_end_to_end_offline():
    """端到端：真实 vault + 假 Drive + 假 LLM，跑完整条链。

    单元测试测零件，串起来才是真正会出问题的地方。
    """
    import shutil
    root = Path('/home/user/obsidian-base')
    if not root.exists():
        return  # CI 无 vault 时跳过

    blog = TMP / 'blog-e2e'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)

    # LLM 换成「原样返回源文 + 一句导读」——这是合法重组的下限，必须过校验
    def fake_compose(group, api_key, model=None, _post=None):
        body = '\n\n'.join(n.body for n in group.notes)
        return f'## {group.tag.split("/")[-1]}\n\n本文分为 3 个部分。\n\n{body}'

    def fake_fetch(names, index, service, out_dir, url_prefix, _download=None):
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        m = {}
        for n in names:
            dest = out_dir / (Path(n).stem + '.webp')
            dest.write_bytes(b'fake')
            m[n] = f'{url_prefix}/{dest.name}'
        return m, []

    orig = (mn.compose.compose, mn.images.drive_service,
            mn.images.load_index, mn.images.fetch_images)
    mn.compose.compose = fake_compose
    mn.images.drive_service = lambda _: None
    mn.images.load_index = lambda *a, **k: {}
    mn.images.fetch_images = fake_fetch
    try:
        rs = mn.run_auto(root, blog, 'fake-key', '{}', count=2)
    finally:
        (mn.compose.compose, mn.images.drive_service,
         mn.images.load_index, mn.images.fetch_images) = orig

    assert len(rs) == 2, rs
    assert all(r['status'] == 'published' for r in rs), \
        [(r['slug'], r['failures']) for r in rs]

    # 产出物必须真的落盘，且 frontmatter 是合法 YAML
    import yaml as _yaml
    import datetime as _dt
    for r in rs:
        f = (blog / 'src' / 'content' / 'posts'
            / _dt.date.today().strftime('%Y-%m') / f"{r['slug']}.md")
        assert f.exists(), f
        text = f.read_text(encoding='utf-8')
        fm = _yaml.safe_load(text.split('---')[1])
        assert fm['title'] and fm['category'] and fm['sourceNotes']
        assert 'image&attachment' not in text, '图片路径未重写'

    # published.json 记录正确，重跑不重复发布
    pub = json.loads((blog / 'published.json').read_text(encoding='utf-8'))
    assert len(pub) == 2, pub
    mn.compose.compose = fake_compose
    mn.images.drive_service = lambda _: None
    mn.images.load_index = lambda *a, **k: {}
    mn.images.fetch_images = fake_fetch
    try:
        again = mn.run_auto(root, blog, 'fake-key', '{}', count=2)
    finally:
        (mn.compose.compose, mn.images.drive_service,
         mn.images.load_index, mn.images.fetch_images) = orig
    assert {r['slug'] for r in again}.isdisjoint({r['slug'] for r in rs}), \
        '重跑发布了同一组'


def test_run_auto_marks_failed_verification_as_draft():
    """校验不过的文章照样落 posts/，但必须带 draft 标，站点构建跳过它。"""
    import shutil
    root = Path('/home/user/obsidian-base')
    if not root.exists():
        return

    blog = TMP / 'blog-review'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)

    def tampering_compose(group, api_key, model=None, _post=None):
        body = '\n\n'.join(n.body for n in group.notes)
        return f'## X\n\n流速改为 987.654 mL/min。\n\n{body}'

    orig = (mn.compose.compose, mn.images.drive_service,
            mn.images.load_index, mn.images.fetch_images)
    mn.compose.compose = tampering_compose
    mn.images.drive_service = lambda _: None
    mn.images.load_index = lambda *a, **k: {}
    mn.images.fetch_images = lambda *a, **k: ({}, list(a[0]))
    try:
        rs = mn.run_auto(root, blog, 'k', '{}', count=1)
    finally:
        (mn.compose.compose, mn.images.drive_service,
         mn.images.load_index, mn.images.fetch_images) = orig

    assert rs[0]['status'] == 'draft', rs
    assert not (blog / '_review').exists(), '_review/ 已经取消'
    import datetime as _dt
    month = _dt.date.today().strftime('%Y-%m')
    text = (blog / 'src' / 'content' / 'posts' / month
           / f"{rs[0]['slug']}.md").read_text(encoding='utf-8')
    assert re.search(r'^draft: true$', text, re.M), text[:300]
    # 草稿也记账，否则下次运行又挑中同一组
    pub = json.loads((blog / 'published.json').read_text(encoding='utf-8'))
    assert pub[rs[0]['slug']]['draft'] is True, pub


def test_run_auto_moves_article_to_new_month_removes_old_copy():
    """pick_next() 会在源笔记改动（source_hash 对不上）时重新选中已发布的组，
    run_auto() 跟 seed.process() 一样要在换月份重发时清理旧月份的孤本——
    不清理的话同一 slug 在两个月份文件夹各留一份，_all_posts() 只认得到
    其中一份，退稿删文件删不干净另一份。"""
    TMP.mkdir(parents=True, exist_ok=True)
    v = TMP / 'v-auto-remove'
    shutil.rmtree(v, ignore_errors=True)
    v.mkdir(parents=True)
    tag = '03质量控制/残留/HCP'
    for i in range(2):
        (v / f'n{i}.md').write_text(
            f'---\ntags:\n  - {tag}\ntype: note\n---\n正文{i}' + '正' * 3000,
            encoding='utf-8')

    blog = TMP / 'blog-auto-remove'
    shutil.rmtree(blog, ignore_errors=True)
    slug = '03质量控制-残留-hcp'
    old_path = blog / 'src' / 'content' / 'posts' / '2020-01' / f'{slug}.md'
    old_path.parent.mkdir(parents=True)
    old_path.write_text('---\ntitle: "旧版本"\n---\n\n旧正文', encoding='utf-8')
    (blog / 'published.json').write_text(
        json.dumps({slug: {'slug': slug, 'tag': tag, 'source_hash': 'sha256:old'}}),
        encoding='utf-8')

    def fake_compose(group, api_key, model=None, _post=None):
        body = '\n\n'.join(n.body for n in group.notes)
        return f'## {group.tag.split("/")[-1]}\n\n本文分为 3 个部分。\n\n{body}'

    def fake_fetch(names, index, service, out_dir, url_prefix, _download=None):
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        m = {}
        for n in names:
            dest = out_dir / (Path(n).stem + '.webp')
            dest.write_bytes(b'fake')
            m[n] = f'{url_prefix}/{dest.name}'
        return m, []

    orig = (mn.compose.compose, mn.images.drive_service,
            mn.images.load_index, mn.images.fetch_images)
    mn.compose.compose = fake_compose
    mn.images.drive_service = lambda _: None
    mn.images.load_index = lambda *a, **k: {}
    mn.images.fetch_images = fake_fetch
    try:
        rs = mn.run_auto(v, blog, 'fake-key', '{}', count=1)
    finally:
        (mn.compose.compose, mn.images.drive_service,
         mn.images.load_index, mn.images.fetch_images) = orig

    assert rs and rs[0]['slug'] == slug, rs
    assert not old_path.exists(), '旧月份文件夹的孤本应该被清掉'
    import datetime as _dt
    month = _dt.date.today().strftime('%Y-%m')
    assert (blog / 'src' / 'content' / 'posts' / month / f'{slug}.md').exists()


# ---------- drafts（手动通道）----------

def test_fill_defaults_requires_title_only():
    fm = df.fill_defaults({'title': '我的文章'}, Path('drafts/my-post.md'), '正文内容很长' * 30)
    assert fm['title'] == '我的文章'
    assert fm['slug'] == 'my-post'
    assert fm['category'] == '杂记'
    assert fm['tags'] == []
    assert 0 < len(fm['description']) <= 120
    assert re.match(r'\d{4}-\d{2}-\d{2}', str(fm['date']))


def test_fill_defaults_derives_category_from_tags():
    fm = df.fill_defaults({'title': 'T', 'tags': ['03质量控制/SEC']}, Path('a.md'), '正文')
    assert fm['category'] == '03质量控制'


def test_fill_defaults_missing_title_returns_none():
    assert df.fill_defaults({}, Path('a.md'), '正文') is None
    assert df.fill_defaults({'title': ''}, Path('a.md'), '正文') is None


def test_fill_defaults_respects_explicit_values():
    fm = df.fill_defaults({'title': 'T', 'slug': 'custom', 'date': '2020-01-02',
                           'description': '自定义摘要'}, Path('a.md'), '正文')
    assert fm['slug'] == 'custom' and str(fm['date']) == '2020-01-02'
    assert fm['description'] == '自定义摘要'


def test_slugify_cn_keeps_ascii_and_strips_symbols():
    assert df.slugify_cn('My Post! (v2)') == 'my-post-v2'
    assert df.slugify_cn('SEC 方法开发') == 'sec-方法开发'


def test_description_strips_markdown_noise():
    """摘要取正文前 120 字，不该混进图片语法和标题井号。"""
    body = '# 标题\n\n![](../x/a.png)\n\n这是**正文**的第一句话。'
    d = df.fill_defaults({'title': 'T'}, Path('a.md'), body)['description']
    assert '![' not in d and '#' not in d and '**' not in d, repr(d)
    assert '这是正文的第一句话' in d, repr(d)


def test_run_drafts_end_to_end():
    """扔一篇含 Drive 图片和双链的稿子，确认取图、双链、落盘、删原件都对。"""
    import shutil
    blog = TMP / 'blog-drafts'
    shutil.rmtree(blog, ignore_errors=True)
    (blog / 'drafts').mkdir(parents=True)
    (blog / 'src' / 'content' / 'posts').mkdir(parents=True)

    (blog / 'drafts' / 'sec-note.md').write_text(
        '---\ntitle: SEC 方法开发\ntags:\n  - 03质量控制/SEC\n---\n'
        '柱温 25 °C。详见[[某未发布笔记]]。\n'
        '![](../image&attachment/image-laptop/SEC-peak.png)\n', encoding='utf-8')
    (blog / 'drafts' / 'README.md').write_text('说明文件，不该被当成稿子', encoding='utf-8')
    (blog / 'drafts' / 'no-title.md').write_text('---\ntags: []\n---\n正文', encoding='utf-8')

    def fake_fetch(names, index, service, out_dir, url_prefix, _download=None):
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        m = {}
        for n in names:
            dest = out_dir / (Path(n).stem + '.webp')
            dest.write_bytes(b'fake')
            m[n] = f'{url_prefix}/{dest.name}'
        return m, []

    orig = (df.images.drive_service, df.images.load_index, df.images.fetch_images)
    df.images.drive_service = lambda _: None
    df.images.load_index = lambda *a, **k: {}
    df.images.fetch_images = fake_fetch
    try:
        rs = df.run_drafts(blog, '{}')
    finally:
        (df.images.drive_service, df.images.load_index, df.images.fetch_images) = orig

    by = {r['file']: r for r in rs}
    assert 'README.md' not in by, 'README.md 不该被当成稿子处理'
    assert by['no-title.md']['status'] == 'error', by['no-title.md']
    ok = by['sec-note.md']
    assert ok['status'] == 'published', ok

    import datetime as _dt
    month = _dt.date.today().strftime('%Y-%m')
    out = (blog / 'src' / 'content' / 'posts' / month
          / f"{ok['slug']}.md").read_text(encoding='utf-8')
    assert '/images/' in out and 'image&attachment' not in out, '图片未重写'
    assert '[[' not in out and '详见某未发布笔记' in out, '双链未解析'
    assert not (blog / 'drafts' / 'sec-note.md').exists(), '发布后原件应删除'
    assert (blog / 'drafts' / 'README.md').exists(), 'README 不该被删'


def test_run_drafts_refuses_slug_collision():
    """slug 撞车必须报错跳过，不能静默覆盖已有文章。"""
    import shutil
    blog = TMP / 'blog-collide'
    shutil.rmtree(blog, ignore_errors=True)
    (blog / 'drafts').mkdir(parents=True)
    posts = blog / 'src' / 'content' / 'posts'
    posts.mkdir(parents=True)
    (posts / 'dup.md').write_text('已有文章', encoding='utf-8')
    (blog / 'drafts' / 'dup.md').write_text(
        '---\ntitle: 新稿\n---\n正文', encoding='utf-8')

    orig = (df.images.drive_service, df.images.load_index, df.images.fetch_images)
    df.images.drive_service = lambda _: None
    df.images.load_index = lambda *a, **k: {}
    df.images.fetch_images = lambda *a, **k: ({}, [])
    try:
        rs = df.run_drafts(blog, '{}')
    finally:
        (df.images.drive_service, df.images.load_index, df.images.fetch_images) = orig

    assert rs[0]['status'] == 'error' and 'slug' in rs[0]['reason'], rs
    assert (posts / 'dup.md').read_text(encoding='utf-8') == '已有文章', '已有文章被覆盖了'
    assert (blog / 'drafts' / 'dup.md').exists(), '出错时不该删原件'


def test_run_drafts_refuses_slug_collision_across_month_folders():
    """已有文章在别的月份文件夹里，也要能查出 slug 冲突——原来只查「本次
    要写的那个月份路径」存不存在，分了月份后这一步会漏判。"""
    import shutil
    blog = TMP / 'blog-collide-nested'
    shutil.rmtree(blog, ignore_errors=True)
    (blog / 'drafts').mkdir(parents=True)
    (blog / 'src' / 'content' / 'posts' / '2020-01').mkdir(parents=True)
    (blog / 'src' / 'content' / 'posts' / '2020-01' / 'dup.md').write_text(
        '已有文章', encoding='utf-8')
    (blog / 'drafts' / 'dup.md').write_text(
        '---\ntitle: 新稿\n---\n正文', encoding='utf-8')

    orig = (df.images.drive_service, df.images.load_index, df.images.fetch_images)
    df.images.drive_service = lambda _: None
    df.images.load_index = lambda *a, **k: {}
    df.images.fetch_images = lambda *a, **k: ({}, [])
    try:
        rs = df.run_drafts(blog, '{}')
    finally:
        (df.images.drive_service, df.images.load_index, df.images.fetch_images) = orig

    assert rs[0]['status'] == 'error' and 'slug' in rs[0]['reason'], rs
    assert (blog / 'src' / 'content' / 'posts' / '2020-01' / 'dup.md'
           ).read_text(encoding='utf-8') == '已有文章', '已有文章被覆盖了'


# ---------- routinerun（工具与效率栏目）----------

def test_routinerun_skips_config_dirs_and_stub_readmes():
    """RoutineRun 285 个 md 里 269 个是技能配置，还有几个几十字符的占位 README。"""
    import routinerun as rr
    import shutil
    repo = TMP / 'rr'
    shutil.rmtree(repo, ignore_errors=True)
    (repo / '.claude' / 'skills' / 'x').mkdir(parents=True)
    (repo / '.claude' / 'skills' / 'x' / 'SKILL.md').write_text('# 技能\n' + 'x' * 2000, encoding='utf-8')
    (repo / 'docs').mkdir(parents=True)
    (repo / 'docs' / 'real.md').write_text('# 真笔记\n\n' + '正文' * 400, encoding='utf-8')
    (repo / 'stub').mkdir()
    (repo / 'stub' / 'README.md').write_text('# 占位\n\n子项目目录。', encoding='utf-8')
    (repo / 'CLAUDE.md').write_text('# 给 AI 看的\n' + 'x' * 2000, encoding='utf-8')

    got = {rel for rel, _, _ in rr.collect(repo)}
    assert got == {'docs/real.md'}, got


def test_routinerun_writes_tools_category_and_strips_h1():
    import routinerun as rr
    import shutil
    import yaml as _yaml
    repo = TMP / 'rr2'
    blog = TMP / 'rr2-blog'
    shutil.rmtree(repo, ignore_errors=True)
    shutil.rmtree(blog, ignore_errors=True)
    (repo / 'git&github').mkdir(parents=True)
    (repo / 'git&github' / '笔记.md').write_text(
        '# Git & GitHub 学习笔记\n\n按时间顺序追加记录每次相关对话的要点。\n\n' + '正文' * 400,
        encoding='utf-8')

    rs = rr.run(repo, blog)
    assert rs[0]['status'] == 'published', rs
    import datetime as _dt
    month = _dt.date.today().strftime('%Y-%m')
    f = blog / 'src' / 'content' / 'posts' / month / f"{rs[0]['slug']}.md"
    text = f.read_text(encoding='utf-8')
    fm = _yaml.safe_load(text.split('---')[1])
    assert fm['category'] == '工具与效率'
    assert fm['title'] == 'Git & GitHub 学习笔记'
    assert fm['description']
    body = text.split('---', 2)[2]
    assert not body.lstrip().startswith('# '), '标题应从正文摘掉'

    # 重跑不覆盖，避免抹掉人工修改
    assert rr.run(repo, blog)[0]['status'] == 'skipped'


def test_routinerun_skips_when_slug_exists_in_different_month_folder():
    """同一篇工具笔记已经在别的月份文件夹发过，重跑不该在新月份再写一份
    重复的——原来的「已存在则跳过」只查当前月份路径，分月后会漏判。"""
    import routinerun as rr
    import shutil
    repo = TMP / 'rr3'
    blog = TMP / 'rr3-blog'
    shutil.rmtree(repo, ignore_errors=True)
    shutil.rmtree(blog, ignore_errors=True)
    (repo / 'git&github').mkdir(parents=True)
    (repo / 'git&github' / '笔记.md').write_text(
        '# Git & GitHub 学习笔记\n\n按时间顺序追加记录每次相关对话的要点。\n\n' + '正文' * 400,
        encoding='utf-8')
    old = blog / 'src' / 'content' / 'posts' / '2020-01'
    old.mkdir(parents=True)
    # slug 算法：'tools-' + slugify_cn(Path('笔记.md').stem)，'笔记' 全是
    # \w 范围内的 CJK 字符，slugify_cn 不改动它，结果就是 'tools-笔记'
    # （跟仓库里已发布的 src/content/posts/2026-08/tools-笔记.md 同名不是
    # 巧合——那篇就是这条通道产出的）
    (old / 'tools-笔记.md').write_text('已发布的旧版本', encoding='utf-8')

    rs = rr.run(repo, blog)
    assert rs[0]['status'] == 'skipped', rs
    assert (old / 'tools-笔记.md').read_text(encoding='utf-8') == '已发布的旧版本'


# ---------- seed（引子通道）----------

LEAD = '本文围绕某个主题展开，先交代脉络，再讨论边界条件，最后归拢结论与尚未解决的问题。'


def _article(sections=3, extra='', evidence_block=''):
    parts = [LEAD]
    for i in range(sections):
        parts.append(f'\n\n## 第 {"一二三四五六"[i]} 节：讲清楚一个问题\n\n' + '正文内容。' * 40)
    return ''.join(parts) + extra + evidence_block


def _mkvault(tmp, name, body, tag='03质量控制/残留/HCP'):
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)
    (tmp / name).write_text(f'---\ntags:\n  - {tag}\ntype: note\n---\n{body}',
                            encoding='utf-8')
    return tmp


def test_grow_cap_has_an_absolute_floor():
    """短稿的比例上限要有绝对下限：201 字符 × 3 倍只有 600 字，成不了文章。"""
    assert vf.proportion('grow', 201, 3314) == []          # 3,314 < 4,000 的绝对下限
    assert vf.proportion('grow', 201, 9000)                 # 真跑飞了还是要拦
    # 正常体量的引子仍按 3 倍卡
    assert vf.proportion('grow', 4000, 11000) == []
    assert vf.proportion('grow', 4000, 13000)


def test_mode_is_decided_by_note_size():
    """长笔记做减法，短笔记做加法。"""
    assert sd.decide_mode(vault.Note('a', 't', [], 'note', body='x' * 20000)) == 'shrink'
    assert sd.decide_mode(vault.Note('a', 't', [], 'note', body='x' * 3000)) == 'grow'


def test_auto_select_skips_notes_already_drafted():
    """定时任务不传 --seed，靠自动选材；候选按体量降序排。一篇被拒的引子
    已经带 draft 标记了账，不排除的话体量没变、排序不变，下次自动选材还是
    原样排回队首——同样的失败重演一遍，还得再烧一次 DeepSeek 调用，真正的
    新材料反而排不上。
    """
    TMP.mkdir(parents=True, exist_ok=True)
    v = TMP / 'v-pending'
    shutil.rmtree(v, ignore_errors=True)
    v.mkdir(parents=True)
    (v / 'long.md').write_text(
        '---\ntags:\n  - 03质量控制/残留/HCP\ntype: note\n---\n' + '正' * 9000,
        encoding='utf-8')
    (v / 'short.md').write_text(
        '---\ntags:\n  - 03质量控制/残留/HCP\ntype: note\n---\n' + '正' * 3000,
        encoding='utf-8')

    blog = TMP / 'seed-pending'
    shutil.rmtree(blog, ignore_errors=True)
    # long.md 已经产出过一篇没过校验的草稿，还在 posts/ 里等人放行
    _post(blog, df.slugify_cn('long'), title='待复核', primaryTag='03质量控制/残留/HCP',
          sourceNotes=['long.md'], draft=True)

    rs = sd.run(v, blog, 'k', None, publish=True, _index={},
                _chat=lambda m, k: '# 标题\n\n' + _article() + '正' * 2000)
    assert rs[0]['seed'] == 'short.md', rs[0]


def test_shrink_mode_publishes_when_clean():
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-shrink'
    shutil.rmtree(blog, ignore_errors=True)
    (blog / 'src' / 'content' / 'posts').mkdir(parents=True)
    v = _mkvault(TMP / 'v-shrink', 'n.md', '回收率 85.3%。' + '正' * 20000)

    def fake(msg, key):
        assert '【减法模式】' in msg, '模式没交代给模型'
        return '# 标题\n\n' + _article() + '\n\n回收率 85.3%。' + '正' * 12000

    rs = sd.run(v, blog, 'k', None, publish=True, _index={}, _chat=fake)
    assert rs[0]['ok'] and rs[0]['status'] == 'published', rs[0]['failures']
    import datetime as _dt
    month = _dt.date.today().strftime('%Y-%m')
    assert (blog / 'src' / 'content' / 'posts' / month / f"{rs[0]['slug']}.md").exists()
    # 记账里存了引子路径，下次选材才能去重
    import json as _json
    rec = _json.loads((blog / 'published.json').read_text(encoding='utf-8'))
    assert list(rec.values())[0]['seed'] == 'n.md'


def test_shrink_that_deletes_too_much_is_blocked():
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-cut'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)
    v = _mkvault(TMP / 'v-cut', 'n.md', '正' * 20000)
    rs = sd.run(v, blog, 'k', None, publish=True, _index={},
                _chat=lambda m, k: '# 标题\n\n' + _article())
    assert not rs[0]['ok']
    assert any('减法模式下篇幅' in f for f in rs[0]['failures']), rs[0]['failures']
    assert rs[0]['status'] == 'draft'


def test_grow_mode_requires_evidence_section():
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-noev'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)
    v = _mkvault(TMP / 'v-noev', 'n.md', '正' * 3000)
    rs = sd.run(v, blog, 'k', None, publish=True, _index={},
                _chat=lambda m, k: '# 标题\n\n' + _article(4) + '正' * 2000)
    assert not rs[0]['ok']
    assert any('依据与出处' in f for f in rs[0]['failures']), rs[0]['failures']


def test_grow_mode_fabricated_source_is_blocked():
    """编一个知识库里不存在的路径当出处，必须当场拦下。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-fake'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)
    v = _mkvault(TMP / 'v-fake', 'n.md', '正' * 3000)
    ev_block = ('\n\n## 依据与出处\n\n'
                '1. 笔记：`不存在的/路径.md` —— 引用要点：某个说法\n')
    rs = sd.run(v, blog, 'k', None, publish=True, _index={},
                _chat=lambda m, k: '# 标题\n\n' + _article(4) + '结论[依据 1]。' + '正' * 2000 + ev_block)
    assert not rs[0]['ok']
    assert any('不存在' in f for f in rs[0]['failures']), rs[0]['failures']


def test_related_published_articles_get_links():
    """同二级标签的已发布文章要自动带上链接，链接由流水线生成不让模型编。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-rel'
    shutil.rmtree(blog, ignore_errors=True)
    posts = blog / 'src' / 'content' / 'posts'
    posts.mkdir(parents=True)
    (posts / 'old-one.md').write_text('---\ntitle: "旧文"\n---\n正文', encoding='utf-8')
    (blog / 'published.json').write_text(
        '{"03质量控制/残留/HCP": {"slug": "old-one", "source_hash": "h"}}', encoding='utf-8')
    v = _mkvault(TMP / 'v-rel', 'n.md', '正' * 20000)
    rs = sd.run(v, blog, 'k', None, publish=True, _index={},
                _chat=lambda m, k: '# 标题\n\n' + _article() + '正' * 12000)
    assert rs[0]['related'] == ['old-one'], rs[0]
    import datetime as _dt
    month = _dt.date.today().strftime('%Y-%m')
    text = (posts / month / f"{rs[0]['slug']}.md").read_text(encoding='utf-8')
    assert '## 相关阅读' in text and '](/posts/old-one)' in text


def test_related_published_finds_articles_across_month_folders():
    """已发布文章挪到月份子目录后，「相关阅读」的标题查找不能跟着失效
    （原来直接拼平铺路径读标题，找不到就静默退化成显示 slug）。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-rel-nested'
    shutil.rmtree(blog, ignore_errors=True)
    _post(blog, 'old-one', month='2026-07', title='旧文')
    (blog / 'published.json').write_text(
        '{"03质量控制/残留/HCP": {"slug": "old-one", "source_hash": "h"}}',
        encoding='utf-8')
    v = _mkvault(TMP / 'v-rel-nested', 'n.md', '正' * 20000)
    rs = sd.run(v, blog, 'k', None, publish=True, _index={},
                _chat=lambda m, k: '# 标题\n\n' + _article() + '正' * 12000)
    assert rs[0]['related'] == ['old-one'], rs[0]
    # process() 的返回值只留 slug，标题在这一步就丢了——真正能看出标题查找
    # 有没有跨月份生效的地方是渲染出来的正文：查不到标题会退化成显示 slug
    # 本身，链接文字变成 [old-one](...) 而不是 [旧文](...)
    import datetime as _dt
    month = _dt.date.today().strftime('%Y-%m')
    text = (blog / 'src' / 'content' / 'posts' / month
           / f"{rs[0]['slug']}.md").read_text(encoding='utf-8')
    assert '[旧文](/posts/old-one)' in text, text


# ---------- 草稿位（draft）与 published.json 自愈 ----------

def _post(blog, slug, month=None, **fm):
    """在 posts/ 造一篇文章，frontmatter 只写给定字段。month 给定时把文章落在对应
    月份子目录，用来测「文章在月份文件夹里」的场景；不给就还是平铺（兼容
    既有调用，也覆盖「迁移前遗留平铺文件」这个场景）。"""
    d = Path(blog) / 'src' / 'content' / 'posts'
    if month:
        d = d / month
    d.mkdir(parents=True, exist_ok=True)
    lines = ['---']
    for k, v in fm.items():
        if isinstance(v, list):
            lines.append(f'{k}:')
            lines += [f'  - "{x}"' for x in v]
        elif isinstance(v, bool):
            lines.append(f'{k}: {"true" if v else "false"}')
        else:
            lines.append(f'{k}: "{v}"')
    lines += ['---', '', '正文']
    (d / f'{slug}.md').write_text('\n'.join(lines), encoding='utf-8')


def test_all_posts_finds_nested_and_flat_files():
    """分月份子目录后，_all_posts 既要找到子目录里的文章，也不能漏掉迁移
    前可能残留的平铺文件——两种布局在迁移过渡期会同时存在。"""
    blog = TMP / 'all-posts'
    shutil.rmtree(blog, ignore_errors=True)
    posts = blog / 'src' / 'content' / 'posts'
    (posts / '2026-07').mkdir(parents=True)
    (posts / '2026-08').mkdir(parents=True)
    (posts / '2026-07' / 'old-post.md').write_text('正文', encoding='utf-8')
    (posts / '2026-08' / 'new-post.md').write_text('正文', encoding='utf-8')
    (posts / 'flat-post.md').write_text('正文', encoding='utf-8')

    found = mn._all_posts(posts)
    assert set(found) == {'old-post', 'new-post', 'flat-post'}, found
    assert found['old-post'] == posts / '2026-07' / 'old-post.md', found

    assert mn._all_posts(TMP / 'does-not-exist') == {}


def test_post_path_builds_month_subfolder_path():
    posts = Path('/blog/src/content/posts')
    assert mn.post_path(posts, 'my-slug', '2026-08') == posts / '2026-08' / 'my-slug.md'


def test_reconcile_finds_posts_in_month_subfolders():
    """分月份子目录后 reconcile 必须还能找到文章——找不到就会把账本里的记录
    全部当「文件没了」销掉（master 上出过同类事故，同一份代码的另一个漏账
    方向见 test_reconcile_backfills_manually_moved_article）。"""
    blog = TMP / 'rec-nested'
    shutil.rmtree(blog, ignore_errors=True)
    _post(blog, '在月份文件夹里', month='2026-08', title='已归档',
         primaryTag='03质量控制/残留/HCP', sourceNotes=['a.md'])
    pub = mn.reconcile(blog, {'在月份文件夹里':
                              {'slug': '在月份文件夹里', 'seed': 'a.md'}})
    assert '在月份文件夹里' in pub, pub


def test_reconcile_backfills_manually_moved_article():
    """人工把文章搬进 posts/ 却没记账 —— 账本自己补上。

    master 上真出过这事：HCP鉴定与定量 手工搬过去并上线，published.json
    里没有对应记录，引子通道按 seed 字段去重于是仍算「没用过」，下一次
    定时任务会重新挑中同一篇笔记、再烧一次 DeepSeek、覆盖已发布的文章。
    """
    blog = TMP / 'rec-backfill'
    shutil.rmtree(blog, ignore_errors=True)
    _post(blog, '搬过来的', title='手工搬的', primaryTag='03质量控制/残留/HCP',
          sourceNotes=['A/HCP鉴定与定量.md'])
    pub = mn.reconcile(blog, {})
    assert '搬过来的' in pub, pub
    assert pub['搬过来的']['seed'] == 'A/HCP鉴定与定量.md', pub
    assert pub['搬过来的']['tag'] == '03质量控制/残留/HCP', pub


def test_reconcile_drops_record_when_file_deleted():
    """删文件 = 退稿。账本跟着销，那篇笔记重新入列。"""
    blog = TMP / 'rec-drop'
    shutil.rmtree(blog, ignore_errors=True)
    (blog / 'src' / 'content' / 'posts').mkdir(parents=True)
    pub = mn.reconcile(blog, {'没了的': {'slug': '没了的', 'seed': 'x.md'}})
    assert pub == {}, pub


def test_reconcile_rekeys_legacy_tag_keyed_records():
    """旧账本按 tag 做 key，迁移时改成按 slug，且不丢 source_hash。"""
    blog = TMP / 'rec-rekey'
    shutil.rmtree(blog, ignore_errors=True)
    _post(blog, 'old-slug', title='旧文')
    pub = mn.reconcile(blog, {'00基础/生物制品/单抗':
                              {'slug': 'old-slug', 'source_hash': 'sha256:h'}})
    assert list(pub) == ['old-slug'], pub
    assert pub['old-slug']['source_hash'] == 'sha256:h', pub
    assert pub['old-slug']['tag'] == '00基础/生物制品/单抗', pub


def test_same_tag_articles_do_not_overwrite_each_other():
    """两篇文章的 primaryTag 可以完全相同（实测 ELISA 与 HCP鉴定与定量
    都是 03质量控制/残留/HCP）。按 tag 做 key 时后写的会静默覆盖先写的，
    被覆盖那篇于是变回「没发过」，下次定时任务重新生成一遍。"""
    blog = TMP / 'rec-collide'
    shutil.rmtree(blog, ignore_errors=True)
    tag = '03质量控制/残留/HCP'
    for s, n in (('a', 'A.md'), ('b', 'B.md')):
        _post(blog, s, title=s, primaryTag=tag, sourceNotes=[n])
    pub = mn.reconcile(blog, {})
    assert set(pub) == {'a', 'b'}, pub
    assert {r['seed'] for r in pub.values()} == {'A.md', 'B.md'}, pub


def test_seed_rerun_moves_article_to_new_month_removes_old_copy():
    """人工改完源笔记重跑同一篇引子：assemble_frontmatter 把 date 刷成
    当天，归档月份跟着变——旧月份文件夹里不能留一份没人管的孤本。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-rerun-move'
    shutil.rmtree(blog, ignore_errors=True)
    old_path = blog / 'src' / 'content' / 'posts' / '2020-01' / 'n.md'
    old_path.parent.mkdir(parents=True)
    old_path.write_text('---\ntitle: "旧版本"\n---\n\n旧正文', encoding='utf-8')
    v = _mkvault(TMP / 'v-rerun-move', 'n.md', '回收率 85.3%。' + '正' * 20000)
    chat = lambda m, k: '# 标题\n\n' + _article() + '\n\n回收率 85.3%。' + '正' * 12000

    rs = sd.run(v, blog, 'k', None, ['n.md'], publish=True, _index={}, _chat=chat)
    assert rs[0]['ok'], rs[0]['failures']
    assert not old_path.exists(), '旧月份文件夹的孤本应该被清掉'
    import datetime as _dt
    month = _dt.date.today().strftime('%Y-%m')
    assert (blog / 'src' / 'content' / 'posts' / month
           / f"{rs[0]['slug']}.md").exists()


def test_backfilled_record_is_not_republished():
    """回填记录没有 source_hash（拿不到 vault 算不出）。当作已发布，
    不重发 —— 人工放行过的文章不该因为源笔记改了个错别字就被悄悄重写。"""
    g = sel.Group(tag='02分子表征/A/B', notes=[], source_hash='sha256:new', slug='x')
    assert sel.pick_next([g], {'x': {'slug': 'x', 'tag': g.tag}}) is None
    # 有哈希且对不上才重发
    assert sel.pick_next([g], {'x': {'slug': 'x', 'tag': g.tag,
                                     'source_hash': 'sha256:old'}}) is g


def test_save_published_orders_newest_first():
    """落盘前重排：日期新的在前，同一天内后写入的排更前——手机/网页直接
    打开 published.json 确认发表状态，不用再拉到文件末尾找最新一条。"""
    blog = TMP / 'save-order'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)
    pub = {
        '旧': {'slug': '旧', 'published_at': '2026-08-25'},
        '中-先': {'slug': '中-先', 'published_at': '2026-08-26'},
        '中-后': {'slug': '中-后', 'published_at': '2026-08-26'},
        '新': {'slug': '新', 'published_at': '2026-08-27'},
        '没日期': {'slug': '没日期'},   # reconcile 补建时 frontmatter 缺 date 会出现
    }
    mn.save_published(blog, pub)
    on_disk = json.loads((blog / 'published.json').read_text(encoding='utf-8'))
    assert list(on_disk) == ['新', '中-后', '中-先', '旧', '没日期'], on_disk


def test_resolve_seed_url_extracts_path_from_github_blob_link():
    """手动指定引子更顺手的方式：直接在 Obsidian-base 里翻到笔记、复制它的
    GitHub 链接——中文和斜杠会被转成 %E6%8A%97 这类 percent-encoding。"""
    url = ('https://github.com/Bryce505/Obsidian-base/blob/master/'
           'Antibody-Engineering%2F%E6%8A%97%E4%BD%93%E7%BB%93%E6%9E%84'
           '%E4%B8%8E%E5%8A%9F%E8%83%BD.md')
    assert mn.resolve_seed_url(url) == 'Antibody-Engineering/抗体结构与功能.md'


def test_resolve_seed_url_strips_query_string():
    """GitHub「查看纯文本」视图的链接带 ?plain=1，不属于路径。"""
    url = 'https://github.com/Bryce505/Obsidian-base/blob/master/A/B.md?plain=1'
    assert mn.resolve_seed_url(url) == 'A/B.md'


def test_resolve_seed_url_accepts_raw_and_blame_views():
    """手滑复制成 raw/blame 视图的链接（而不是 blob）也认得。"""
    assert mn.resolve_seed_url('https://github.com/o/r/raw/main/A/B.md') == 'A/B.md'
    assert mn.resolve_seed_url('https://github.com/o/r/blame/main/A/B.md') == 'A/B.md'


def test_resolve_seed_url_passes_through_bare_path():
    """已经是裸路径（没有 http 前缀）就原样返回，不强求一定得是链接。"""
    assert mn.resolve_seed_url('A/B.md') == 'A/B.md'


def test_resolve_seed_url_unparseable_link_falls_through_to_existing_error():
    """解析不出路径的怪链接原样返回，不在这里报错——交给 seed.run() 已有的
    「找不到引子笔记」校验兜底，不重复一套错误处理。"""
    weird = 'https://example.com/not-a-github-link'
    assert mn.resolve_seed_url(weird) == weird


def test_failed_verification_lands_in_posts_as_draft():
    """校验没过不再进 _review/：同一个 posts/ 文件，多一行 draft: true。

    放行 = 删掉那一行。不用改名、不用移文件、不用手写 published.json。
    """
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-draft'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)
    v = _mkvault(TMP / 'v-draft', 'n.md', '正' * 20000)
    rs = sd.run(v, blog, 'k', None, publish=True, _index={},
                _chat=lambda m, k: '# 标题\n\n' + _article())
    assert not rs[0]['ok'] and rs[0]['status'] == 'draft', rs[0]
    assert not (blog / '_review').exists(), '_review/ 已经取消'
    import datetime as _dt
    month = _dt.date.today().strftime('%Y-%m')
    f = blog / 'src' / 'content' / 'posts' / month / f"{rs[0]['slug']}.md"
    assert f.exists(), '草稿也要落在 posts/ 里'
    text = f.read_text(encoding='utf-8')
    assert text.startswith('---\n'), 'frontmatter 必须在文件最开头'
    assert re.search(r'^draft: true$', text, re.M), text[:300]
    # 问题清单用 YAML 而不是 HTML 注释：GitHub 预览会把 <!-- --> 整段吃掉，
    # 人打开文件根本看不见没过哪几项
    assert '<!--' not in text.split('---')[1], '不许再用 HTML 注释'
    assert re.search(r'^reviewNotes:$', text, re.M), text[:300]
    assert any('减法模式下篇幅' in ln for ln in text.splitlines()), text[:400]


def test_draft_is_recorded_so_it_is_not_regenerated():
    """草稿也要记账，否则下次自动选材又挑中同一篇、再烧一次 DeepSeek。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-draftrec'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)
    v = _mkvault(TMP / 'v-draftrec', 'n.md', '正' * 20000)
    sd.run(v, blog, 'k', None, publish=True, _index={},
           _chat=lambda m, k: '# 标题\n\n' + _article())
    pub = json.loads((blog / 'published.json').read_text(encoding='utf-8'))
    rec = list(pub.values())[0]
    assert rec['draft'] is True and rec['seed'] == 'n.md', rec
    # 再跑一次自动选材，不该重复挑中
    rs = sd.run(v, blog, 'k', None, publish=True, _index={},
                _chat=lambda m, k: '# 标题\n\n' + _article())
    assert rs[0]['status'] == 'error', rs[0]


def test_related_reading_skips_drafts():
    """草稿不参与构建，链过去就是死链 —— 相关阅读只认已放行的文章。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-reldraft'
    shutil.rmtree(blog, ignore_errors=True)
    _post(blog, 'live-one', title='已发布', primaryTag='03质量控制/残留/HCP')
    _post(blog, 'draft-one', title='草稿', primaryTag='03质量控制/残留/HCP', draft=True)
    v = _mkvault(TMP / 'v-reldraft', 'n.md', '正' * 20000)
    rs = sd.run(v, blog, 'k', None, publish=True, _index={},
                _chat=lambda m, k: '# 标题\n\n' + _article() + '正' * 12000)
    assert rs[0]['related'] == ['live-one'], rs[0]['related']


def test_explicit_rerun_of_own_draft_is_not_selection_duplicate():
    """人工改完笔记想重跑同一篇，不该被「选材重复」挡住 —— 那条规则拦的是
    「另一篇文章已经占用了这个引子」，不是自己覆盖自己。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-rerun'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)
    v = _mkvault(TMP / 'v-rerun', 'n.md', '回收率 85.3%。' + '正' * 20000)
    chat = lambda m, k: '# 标题\n\n' + _article() + '\n\n回收率 85.3%。' + '正' * 12000
    first = sd.run(v, blog, 'k', None, publish=True, _index={}, _chat=chat)
    assert first[0]['ok'], first[0]['failures']
    again = sd.run(v, blog, 'k', None, ['n.md'], publish=True, _index={}, _chat=chat)
    assert not any('选材重复' in f for f in again[0]['failures']), again[0]['failures']


def test_site_never_reads_posts_collection_directly():
    """草稿与正式文章同住 posts/，全站列表必须走 listPosts() 这一个过滤入口。

    9 处 getCollection('posts') 逐处加过滤迟早漏一处，而漏一处就是未审
    文章直接上线 —— 这是安全阀，拿自检守住。
    """
    src = Path(__file__).parent.parent / 'src'
    bad = []
    for p in sorted(src.rglob('*')):
        if p.suffix not in ('.astro', '.ts', '.js') or p.name == 'posts.ts':
            continue
        for i, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            if re.search(r"""getCollection\(\s*['"]posts['"]""", line):
                bad.append(f'{p.relative_to(src)}:{i}')
    assert not bad, f'这些地方绕过了 listPosts()，草稿会漏上线：{bad}'


# ---------- manual（人工投稿通道）----------

def test_manual_draft_uses_local_images_then_publishes():
    """随稿上传的图就地转 WebP，稿子走同一套加减法与校验。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'manual-blog'
    shutil.rmtree(blog, ignore_errors=True)
    (blog / 'src' / 'content' / 'posts').mkdir(parents=True)
    d = blog / 'drafts'
    (d / 'images' / '我的稿子').mkdir(parents=True)
    (d / 'images' / '我的稿子' / '图一.png').write_bytes(_png(60, 40))
    (d / '我的稿子.md').write_text(
        '---\ntitle: 手写稿\ntags:\n  - 03质量控制/残留/HCP\n---\n'
        '![](图一.png)\n' + '正' * 20000, encoding='utf-8')

    def fake(msg, key):
        return '# 手写稿标题\n\n' + _article() + '\n\n![](图一.png)\n' + '正' * 12000

    rs = mnl.run(None, blog, 'k', None, publish=True, _index={}, _chat=fake)
    assert rs[0]['ok'], rs[0]['failures']
    assert rs[0]['images'] == 1 and rs[0]['missingImages'] == []
    assert (blog / 'public' / 'images' / rs[0]['slug'] / '图一.webp').exists()
    assert not (d / '我的稿子.md').exists(), '处理完的原稿要撤走，否则下次重复处理'


def test_manual_note_parsing_without_frontmatter():
    TMP.mkdir(parents=True, exist_ok=True)
    d = TMP / 'manual-parse'
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    f = d / '稿子.md'
    f.write_text('# 正文标题\n\n内容 ![](a.png)', encoding='utf-8')
    n = mnl.as_note(f, d)
    assert n.title == '正文标题' and n.images == ['a.png']
    assert '# 正文标题' not in n.body, 'H1 应被摘掉，标题由 frontmatter 承载'


# ---------- evidence / notify ----------

def test_evidence_paraphrase_passes_fabrication_fails():
    art = ('结论[依据 1]。\n\n## 依据与出处\n\n'
           '1. 笔记：`a/b.md` —— 引用要点：亲和富集会同时富集与抗体结合的 HCP\n')
    real = {'a/b.md': '做抗体亲和富集时，会同时富集那些与抗体结合的 HCP 分子。'}
    assert ev.check(art, real, '')[0] == []
    assert ev.check(art, {'a/b.md': '本节讨论柱效与塔板数的计算'}, '')[0]


def test_evidence_doi_must_come_from_input():
    art = ('结论[依据 1]。\n\n## 依据与出处\n\n'
           '1. 文献：DOI:10.1016/j.ab.2004.08.008 —— 引用要点：NTCB 断裂位点\n')
    assert ev.check(art, {}, '……DOI:10.1016/j.ab.2004.08.008……')[0] == []
    assert any('疑似编造' in f for f in ev.check(art, {}, '毫无关系的输入')[0])


def test_notify_writes_log_and_skips_when_unconfigured():
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'notify-blog'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)
    rs = [{'slug': 'a', 'title': '甲', 'ok': False, 'mode': 'grow',
           'seedChars': 100, 'articleChars': 300, 'file': 'src/content/posts/a.md',
           'failures': ['空壳章节']}]
    out = nt.notify(blog, rs)
    log = Path(out['log']).read_text(encoding='utf-8')
    assert '甲' in log and '空壳章节' in log
    # 没配 token / SMTP 时静默跳过，不能抛异常把已落盘的产出带垮
    assert out['issue'] is None and out['mail'] is None


# ---------- repair（给已发布文章补图）----------

def test_repair_fills_marks_and_reports_still_missing():
    """图补传到 Drive 后，已发布的文章要能自己修好，不用重跑 LLM。"""
    import repair
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'repair-blog'
    posts = blog / 'src' / 'content' / 'posts'
    posts.mkdir(parents=True, exist_ok=True)
    art = posts / 'a-post.md'
    art.write_text(
        '---\ntitle: t\ndate: 2026-01-01\n---\n\n正文一\n\n'
        + rd.MISSING_TPL.format(name='back.png', caption='图源：《某书》') + '\n\n'
        + rd.MISSING_TPL.format(name='still-gone.png', caption='') + '\n',
        encoding='utf-8')

    def fake_download(service, fid):
        return _png(40, 20)

    rs = repair.run(blog, None, _index={'back.png': 'id1'},
                    _download=fake_download)

    assert rs == [{'slug': 'a-post', 'status': 'repaired',
                   'repaired': ['back.png'], 'stillMissing': ['still-gone.png']}], rs
    text = art.read_text(encoding='utf-8')
    assert '![](/images/a-post/back.webp)\n*图源：《某书》*' in text, text
    assert (blog / 'public' / 'images' / 'a-post' / 'back.webp').exists()
    # 补不回来的原样留着，下次补传后还能再修
    assert rd.missing_marks(text) == [('still-gone.png', '')]


def test_repair_finds_marks_in_month_subfolder():
    """待补图的文章挪到月份子目录后，repair 的扫描不能跟着漏掉——原来是
    平铺 glob，只扫 posts/ 根下一层。"""
    import repair
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'repair-nested'
    shutil.rmtree(blog, ignore_errors=True)
    posts = blog / 'src' / 'content' / 'posts' / '2026-08'
    posts.mkdir(parents=True, exist_ok=True)
    art = posts / 'a-post.md'
    art.write_text(
        '---\ntitle: t\ndate: 2026-08-01\n---\n\n正文\n\n'
        + rd.MISSING_TPL.format(name='back.png', caption='') + '\n',
        encoding='utf-8')

    def fake_download(service, fid):
        return _png(40, 20)

    rs = repair.run(blog, None, _index={'back.png': 'id1'}, _download=fake_download)
    assert rs == [{'slug': 'a-post', 'status': 'repaired',
                   'repaired': ['back.png'], 'stillMissing': []}], rs
    assert '![](/images/a-post/back.webp)' in art.read_text(encoding='utf-8')


def test_repair_without_marks_never_touches_drive():
    """没占位就一次 Drive 都不碰 —— 每晚白跑一趟索引重建不可接受。"""
    import repair
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'repair-clean'
    posts = blog / 'src' / 'content' / 'posts'
    posts.mkdir(parents=True, exist_ok=True)
    (posts / 'b-post.md').write_text('---\ntitle: t\n---\n\n没有占位\n', encoding='utf-8')
    assert repair.run(blog, 'SA-JSON-会炸') == []


def test_audit_lists_images_drive_does_not_have():
    """发文前就能拿到「要往 Drive 补传哪些图」的清单。"""
    import repair
    TMP.mkdir(parents=True, exist_ok=True)
    v = TMP / 'audit-vault'
    shutil.rmtree(v, ignore_errors=True)      # 上次跑剩的笔记会混进分组
    v.mkdir(parents=True)
    for i in range(config.MIN_GROUP):
        (v / f'n{i}.md').write_text(
            '---\ntags:\n  - 02分子表征/A/B\ntype: note\n---\n'
            f'正文 {i}\n![](../img/have{i}.png)\n![](../img/gone{i}.png)\n',
            encoding='utf-8')
    index = {f'have{i}.png': f'id{i}' for i in range(config.MIN_GROUP)}
    rs = repair.audit(v, _index=index)
    assert len(rs) == config.MIN_GROUP, rs
    assert [r['missing'] for r in rs] == [[f'gone{i}.png'] for i in range(config.MIN_GROUP)], rs
    assert repair.audit(v, _index={**index, **{f'gone{i}.png': 'x'
                                               for i in range(config.MIN_GROUP)}}) == []



# ---------- clips（剪藏栏目）----------

def _weixin():
    return cl.parse_month((FIX / 'clips-weixin.md').read_text(encoding='utf-8'),
                          'weixin', '2026-08', 'notes/2026-08.md')


def _x():
    return cl.parse_month((FIX / 'clips-x.md').read_text(encoding='utf-8'),
                          'x', '2026-08', 'notes/x/2026-08.md')


def test_clips_parses_every_field():
    """一条完整记录的十二个字段都要落到位。"""
    c = _weixin()[0]
    assert c['source'] == 'weixin' and c['month'] == '2026-08'
    assert c['title'] == '最新版白皮书：抗体偶联药物（ADC）的生物分析（上）'
    assert c['clippedAt'] == '2026-08-29 07:25'
    assert c['publishedAt'] == '2026-07-22'
    assert c['priority'] == '高'
    assert c['summary'].startswith('系统介绍了 ADC'), c['summary']
    assert len(c['insights']) == 2, c['insights']
    assert c['insights'][0].startswith('杂交免疫捕获'), c['insights']
    assert c['verdict'].startswith('内容系统详尽'), c['verdict']
    assert c['url'] == 'https://mp.weixin.qq.com/s/BywLHNiFo_eIdlck8lckPg'


def test_clips_keyword_with_slash_stays_one_keyword():
    """关键词按 ' / ' 切，不按 '/' 切。

    真实语料里有 `LC-MS/MS`、`敲除/敲低` 这类自带斜杠的词，按裸斜杠切会把
    一个词劈成两个假关键词。
    """
    assert _weixin()[0]['keywords'] == ['抗体偶联药物', '生物分析', 'LC-MS/MS', '游离载荷']


def test_clips_optional_fields_may_be_absent():
    """洞见、发布时间、关键词缺失是上游的正常产出，不是错误。

    实测 68 条真实记录里 2 条没有洞见（AI 判定该帖没有实质观点）。
    """
    entries = _weixin()
    assert entries[1]['publishedAt'] == '', entries[1]     # 上游写「未知」
    assert entries[1]['keywords'] == [], entries[1]        # 上游写「无」
    assert entries[2]['insights'] == [], entries[2]        # 整行缺席


def test_clips_snapshot_relative_path_becomes_repo_url():
    """公众号退一层、X 退两层，都要还原成 Notes 仓库的 blob 链接。"""
    assert _weixin()[0]['snapshot'] == (
        'https://raw.githubusercontent.com/Bryce505/Notes/master/'
        'archive/2026-08/%E6%9C%80%E6%96%B0%E7%89%88-BywLHN.md'), _weixin()[0]['snapshot']
    assert _x()[0]['snapshot'] == (
        'https://raw.githubusercontent.com/Bryce505/Notes/master/'
        'archive/x/2026-08/Agent-651665.md'), _x()[0]['snapshot']


def test_clips_snapshot_path_is_passed_through_verbatim():
    """上游已经 percent-encode 过，这里一个字符都不许再动。

    两个方向都会出事：再编码一次会把 %E4%B8%87 变成 %25E4%25B8%2587；反过来
    「顺手解一次码」也会出事 —— 实测真有一篇标题带百分号（《…Token消耗降60%、
    提速50%》），它的快照文件名里就是个字面的 %，编码出来正是 %25，解掉就成了
    裸 % 同样打不开。所以这里既不编也不解。

    这条 %25 也正是 SNAPSHOT_BASE 必须指 raw 而不是 blob 的原因，见那里的注释。
    """
    weixin = _weixin()
    assert '%25' not in weixin[0]['snapshot'], weixin[0]['snapshot']
    assert weixin[3]['snapshot'].endswith(
        'archive/2026-08/247k_Star-%E9%99%8D60%25-o4pgoT.md'), weixin[3]['snapshot']


def test_clips_missing_required_field_raises():
    """标题 / 剪藏时间 / 原文链接缺任一条，这张卡片就不成立 —— 抛错。"""
    full = (FIX / 'clips-x.md').read_text(encoding='utf-8')
    drops = [
        '- **剪藏**：2026-08-28 18:16 ｜ **发布**：2026-08-28\n',
        '- **链接**：[原文](https://x.com/shao__meng/status/2093228362965651665)'
        ' ｜ [全文快照](../../archive/x/2026-08/Agent-651665.md)\n',
    ]
    for drop in drops:
        assert drop in full, f'fixture 里没有这行，测试本身失效了：{drop!r}'
        try:
            cl.parse_month(full.replace(drop, ''), 'x', '2026-08', 'notes/x/2026-08.md')
        except ValueError:
            continue
        assert False, f'缺了这行竟然没抛错：{drop!r}'


def test_clips_priority_outside_three_buckets_raises():
    """档外的优先级会让这条被页面上每一个筛选条件都藏起来，等于内容消失。"""
    bad = (FIX / 'clips-x.md').read_text(encoding='utf-8').replace(
        '- **优先级**：高 ｜', '- **优先级**：紧急 ｜')
    try:
        cl.parse_month(bad, 'x', '2026-08', 'notes/x/2026-08.md')
    except ValueError as e:
        assert '紧急' in str(e), e
    else:
        assert False, '档外优先级没抛错'


def test_clips_zero_entries_raises():
    """上游把 ## 改成 ###，逐条检查一条都不会触发 —— 靠这条兜底。

    不拦的话站上会静默变成一个空栏目，没有任何人会收到通知。
    """
    try:
        cl.parse_month('# 2026年08月\n\n### 标题层级变了\n- **摘要**：x\n',
                       'x', '2026-08', 'notes/x/2026-08.md')
    except ValueError as e:
        assert '一条' in str(e), e
    else:
        assert False, '零条目没抛错'


def test_clips_collect_merges_both_sources_newest_first():
    """两个来源合成一条流，按剪藏时间倒序。"""
    TMP.mkdir(parents=True, exist_ok=True)
    up = TMP / 'clips-upstream'
    shutil.rmtree(up, ignore_errors=True)
    (up / 'notes' / 'x').mkdir(parents=True)
    (up / 'notes' / '2026-08.md').write_text(
        (FIX / 'clips-weixin.md').read_text(encoding='utf-8'), encoding='utf-8')
    (up / 'notes' / 'x' / '2026-08.md').write_text(
        (FIX / 'clips-x.md').read_text(encoding='utf-8'), encoding='utf-8')

    got = cl.collect(up)
    assert len(got) == 5, got
    assert [c['clippedAt'] for c in got] == [
        '2026-08-29 07:25', '2026-08-28 18:16', '2026-08-28 09:00',
        '2026-08-27 12:35', '2026-08-26 20:10'], [c['clippedAt'] for c in got]
    # X 那条夹在两条公众号中间，证明是合并排序而不是先公众号后 X
    assert got[1]['source'] == 'x', got[1]
    assert got[1]['snapshot'].startswith(
        'https://raw.githubusercontent.com/Bryce505/Notes/master/archive/x/'), got[1]


def test_clips_collect_without_any_month_file_raises():
    """上游把 notes/ 挪走时要红一条，不能产出一个空 JSON 静默上线。"""
    TMP.mkdir(parents=True, exist_ok=True)
    empty = TMP / 'clips-empty'
    shutil.rmtree(empty, ignore_errors=True)
    empty.mkdir(parents=True)
    try:
        cl.collect(empty)
    except ValueError as e:
        assert 'notes' in str(e), e
    else:
        assert False, '上游一个月度文件都没有，竟然没抛错'


if __name__ == '__main__':
    fns = [(k, v) for k, v in sorted(globals().items()) if k.startswith('test_')]
    bad = 0
    for name, fn in fns:
        try:
            fn()
            print(f'  PASS  {name}')
        except Exception as e:
            bad += 1
            print(f'  FAIL  {name}: {type(e).__name__}: {e}')
    print(f'\n{len(fns) - bad}/{len(fns)} passed')
    sys.exit(1 if bad else 0)
