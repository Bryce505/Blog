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

import compose as cp
import drafts as df
import main as mn
import config
import images as im
import render as rd
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
    assert sel.pick_next([g], {g.tag: {'source_hash': g.source_hash, 'slug': g.slug}}) is None
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
    assert sel.pick_next([g], {g.tag: {'source_hash': 'sha256:stale', 'slug': g.slug}}) is g


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
    # 小数分支排在带单位分支前面，所以 0.05 提取出来不带单位——本来如此
    assert {'1.5', '1.8', '0.05', '95%'} <= nums, nums
    # 反过来不能把长数字切开：18.5 里不该冒出 8.5
    assert '8.5' not in vf.data_numbers('取 IAM 18.5 mg 溶解')


def test_reformatting_alone_is_not_a_new_number():
    """模型给数字前后加空格是排版行为，不该被当成编造数据。"""
    src = '准确度在真实值的1.5倍至1.8倍范围内'
    out = '准确度在真实值的 1.5 倍至 1.8 倍范围内'
    assert vf.verify(src, out, [], min_ratio=0.1).ok


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
    assert '0.5' in vf.data_numbers('流速 0.5 mL/min')
    assert '148000' in vf.data_numbers('分子量 148000 Da')


def test_citations_recognises_common_formats():
    t = '见 ICH Q2(R2)、21 CFR 211.194、USP <1058> 与 doi:10.1016/j.chroma.2020.461234'
    assert len(vf.regulations(t)) == 3, vf.regulations(t)
    assert len(vf.dois(t)) == 1, vf.dois(t)


def test_doi_regex_stops_at_markdown_syntax():
    """\\S+ 会把 markdown 链接语法一起吞掉，同一 DOI 因上下文不同提取出不同串。"""
    a = vf.dois('[10.1021/pr4010019](https://doi.org/10.1021/pr4010019)')
    b = vf.dois('参考 10.1021/pr4010019。')
    assert a == b == {'10.1021/pr4010019'}, (a, b)


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
    for r in rs:
        f = blog / 'src' / 'content' / 'posts' / f"{r['slug']}.md"
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


def test_run_auto_routes_failed_verification_to_review():
    """校验不过的文章必须进 _review/，不能进 posts/。"""
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

    assert rs[0]['status'] == 'review', rs
    assert (blog / '_review' / f"{rs[0]['slug']}.md").exists()
    assert not (blog / 'src' / 'content' / 'posts' / f"{rs[0]['slug']}.md").exists()
    assert not (blog / 'published.json').exists(), '校验失败不该写 published.json'


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

    out = (blog / 'src' / 'content' / 'posts' / f"{ok['slug']}.md").read_text(encoding='utf-8')
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
    f = blog / 'src' / 'content' / 'posts' / f"{rs[0]['slug']}.md"
    text = f.read_text(encoding='utf-8')
    fm = _yaml.safe_load(text.split('---')[1])
    assert fm['category'] == '工具与效率'
    assert fm['title'] == 'Git & GitHub 学习笔记'
    assert fm['description']
    body = text.split('---', 2)[2]
    assert not body.lstrip().startswith('# '), '标题应从正文摘掉'

    # 重跑不覆盖，避免抹掉人工修改
    assert rr.run(repo, blog)[0]['status'] == 'skipped'


# ---------- seed（引子通道）----------

def _seed_note(body_chars=3000, path='a/b/n.md'):
    return vault.Note(path=path, title='引子笔记', tags=['03质量控制/残留/HCP'],
                      type='note', book='某书',
                      body='HCP 残留控制。回收率 85.3%，限度 100 ng/mg。\n\n'
                           + 'x' * body_chars)


def test_seed_candidates_skip_short_and_used():
    """太短的笔记撑不起主题，扩写就成了模型自由发挥。"""
    short = _seed_note(10, 'a/short.md')
    good = _seed_note(3000, 'a/good.md')
    assert [n.path for n in sd.candidates([short, good])] == ['a/good.md']
    assert sd.candidates([good], used=['a/good.md']) == []


def test_seed_run_writes_to_review_only():
    """引子通道还在试，产出只落 _review/，不碰 posts 和 published.json。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-blog'
    shutil.rmtree(blog, ignore_errors=True)
    (blog / 'src' / 'content' / 'posts').mkdir(parents=True)
    v = TMP / 'seed-vault'
    shutil.rmtree(v, ignore_errors=True)
    v.mkdir(parents=True)
    (v / 'n.md').write_text(
        '---\ntags:\n  - 03质量控制/残留/HCP\ntype: note\nbook: 某书\n---\n'
        '回收率 85.3%，限度 100 ng/mg。\n' + 'x' * 3000, encoding='utf-8')

    def fake(note, api_key):
        # 扩写：保留源文数据，只补定性叙述
        return ('# HCP 残留控制：从检测原理到限度设定\n\n导读一段。\n\n'
                '## 原理\n\n' + note.body.split("---")[-1].strip() +
                '\n\n覆盖率不足会系统性低估残留水平。\n')

    rs = sd.run(v, blog, 'k', None, _index={}, _compose=fake)
    assert len(rs) == 1 and rs[0]['ok'], rs
    assert rs[0]['articleChars'] > rs[0]['seedChars'], '扩写应当变长'
    out = blog / '_review' / f"seed-{rs[0]['slug']}.md"
    assert out.exists() and '校验：全部通过' in out.read_text(encoding='utf-8')
    assert not list((blog / 'src' / 'content' / 'posts').glob('*.md')), '不该写进 posts'
    assert not (blog / 'published.json').exists(), '不该动 published.json'


def test_seed_run_catches_fabricated_numbers():
    """扩写编出源文没有的数值必须被校验器拦下 —— 这是这条通道的红线。"""
    TMP.mkdir(parents=True, exist_ok=True)
    blog = TMP / 'seed-blog2'
    shutil.rmtree(blog, ignore_errors=True)
    blog.mkdir(parents=True)
    v = TMP / 'seed-vault2'
    shutil.rmtree(v, ignore_errors=True)
    v.mkdir(parents=True)
    (v / 'n.md').write_text(
        '---\ntags:\n  - 03质量控制/残留/HCP\ntype: note\n---\n'
        '回收率 85.3%。\n' + 'x' * 3000, encoding='utf-8')

    def fake(note, api_key):
        return ('# 标题\n\n导读。\n\n## 一节\n\n' + note.body.strip()
                + '\n\n通常流速设为 0.5 mL/min，柱温 30 °C。\n')

    rs = sd.run(v, blog, 'k', None, _index={}, _compose=fake)
    assert not rs[0]['ok'], rs
    assert any('出现源文没有的数据' in f for f in rs[0]['failures']), rs[0]['failures']
    assert '校验未通过' in (blog / '_review' / f"seed-{rs[0]['slug']}.md").read_text(encoding='utf-8')


def test_seed_message_carries_book_and_body():
    n = _seed_note()
    msg = cp.build_seed_message(n)
    assert '引子' in msg and '出处：《某书》' in msg and '85.3%' in msg


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
