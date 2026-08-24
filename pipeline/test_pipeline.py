"""流水线自检。不用测试框架：assert + 文件底部的 runner，CI 里零依赖可跑。

用法: python pipeline/test_pipeline.py
"""
import io
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import compose as cp
import config
import images as im
import render as rd
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


def test_oversized_note_excluded():
    """单篇 158 万字符的「笔记」其实是整本书导入，一篇就撑爆上下文。"""
    big = vault.Note('book.md', 'B', ['a/b/c'], 'note',
                     body='x' * (config.MAX_NOTE_CHARS + 1))
    assert big not in sel.publishable([big])


def test_group_truncated_by_char_budget_not_just_count():
    """按篇数限制是错的指标：9 篇也可能加起来 170 万字符。"""
    # 5 篇 x 9 万 = 45 万，超预算 40 万；应截到 4 篇（36 万）而非整组丢弃
    ns = [vault.Note(f'n{i}.md', f'N{i}', ['a/b/c'], 'note',
                     body='x' * 90_000) for i in range(5)]
    g = sel.build_groups(ns)[0]
    total = sum(len(n.body) for n in g.notes)
    assert total <= config.MAX_GROUP_CHARS, total
    assert len(g.notes) == 4, len(g.notes)


def test_group_dropped_when_budget_cannot_fit_min_notes():
    """预算装不下 3 篇就整组放弃，不发半截文章。"""
    ns = [vault.Note(f'n{i}.md', f'N{i}', ['a/b/c'], 'note',
                     body='x' * 199_000) for i in range(5)]
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
    assert out.strip() == '*[图缺失：GONE.png]*' and '![' not in out


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
