"""流水线自检。不用测试框架：assert + 文件底部的 runner，CI 里零依赖可跑。

用法: python pipeline/test_pipeline.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

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


def test_small_group_falls_back_to_second_level():
    """碎组不能直接丢：41% 的可发布笔记卡在不足 3 篇的三级标签里。

    把它们按二级标签重新归并，凑够 3 篇就能成文。
    """
    ns = ([_fake(f'a{i}.md', ['02分子表征/PTM/糖基化']) for i in range(2)] +
          [_fake(f'b{i}.md', ['02分子表征/PTM/二硫键']) for i in range(2)])
    gs = sel.build_groups(ns)
    assert len(gs) == 1, [(g.tag, len(g.notes)) for g in gs]
    assert gs[0].tag == '02分子表征/PTM'
    assert len(gs[0].notes) == 4


def test_still_dropped_when_even_second_level_too_small():
    ns = [_fake('a.md', ['02分子表征/PTM/糖基化']), _fake('b.md', ['03质量控制/SEC/柱效'])]
    assert sel.build_groups(ns) == []


def test_fallback_does_not_steal_from_valid_third_level_group():
    """三级标签已够 3 篇的组保持独立，不该被二级回退吸走。"""
    ns = ([_fake(f'a{i}.md', ['02分子表征/PTM/糖基化']) for i in range(4)] +
          [_fake(f'b{i}.md', ['02分子表征/PTM/二硫键']) for i in range(2)] +
          [_fake(f'c{i}.md', ['02分子表征/PTM/氧化']) for i in range(2)])
    gs = sel.build_groups(ns)
    tags = {g.tag: len(g.notes) for g in gs}
    assert tags == {'02分子表征/PTM/糖基化': 4, '02分子表征/PTM': 4}, tags


def test_oversized_group_truncated_to_max():
    ns = [_fake(f'n{i:03d}.md', ['02分子表征/PTM/糖基化']) for i in range(40)]
    assert len(sel.build_groups(ns)[0].notes) == 30


def test_fallback_never_collapses_to_top_level():
    """二级碎组不能再降级：「02分子表征」当一篇文章毫无意义。"""
    ns = [_fake(f'a{i}.md', ['02分子表征/PTM']) for i in range(2)]
    assert sel.build_groups(ns) == []


def test_fallback_merges_into_existing_group_not_duplicate():
    """四级碎组回退撞上已存在的二级组时必须合并进去，不能产生同名组。

    产生同名组会导致两篇文章抢同一个 slug，后写的静默覆盖先写的。
    """
    ns = ([_fake(f'a{i}.md', ['02分子表征/PTM']) for i in range(3)] +
          [_fake(f'b{i}.md', ['02分子表征/PTM/糖基化/N-糖']) for i in range(2)])
    gs = sel.build_groups(ns)
    assert {g.tag: len(g.notes) for g in gs} == {'02分子表征/PTM': 5}, \
        {g.tag: len(g.notes) for g in gs}
    assert len(set(g.slug for g in gs)) == len(gs)


def test_pick_next_skips_published_unchanged():
    ns = [_fake(f'n{i}.md', ['02分子表征/PTM/糖基化']) for i in range(5)]
    g = sel.build_groups(ns)[0]
    assert sel.pick_next([g], {g.tag: {'source_hash': g.source_hash, 'slug': g.slug}}) is None
    assert sel.pick_next([g], {}) is g


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
