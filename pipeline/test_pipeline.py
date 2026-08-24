"""流水线自检。不用测试框架：assert + 文件底部的 runner，CI 里零依赖可跑。

用法: python pipeline/test_pipeline.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

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
