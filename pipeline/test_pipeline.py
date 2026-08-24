"""流水线自检。不用测试框架：assert + 文件底部的 runner，CI 里零依赖可跑。

用法: python pipeline/test_pipeline.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import select_ as sel
import vault

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
