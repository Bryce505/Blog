"""以单篇笔记为引子，让模型围绕主题扩写成一篇文章。

自动通道是「多篇笔记打散重组」，产出容易有拼接感：几篇笔记各讲各的，
模型只能按顺序摆，读起来像目录而不是文章 —— 实测那篇 8 篇笔记合成的
《治疗性单抗质量属性与表征方法》就是这个毛病，覆盖面很广但每一节都
浅尝辄止。

这条通道换个思路：一篇笔记当引子，模型补齐原理、方法学脉络与适用边界，
写成一篇讲透一个主题的文章。代价是引入了模型自己的知识 —— 约束办法见
prompt_seed.md：**扩展部分不许出现任何新的数值、法规条款号、文献引用**，
于是 verify.py 那套「不得出现源文没有的数据」的机械校验原封不动仍然
成立，卡住的正是最危险的那类编造。定性叙述不受限制，那本来就是扩写
要补的东西。

产出一律先落 _review/：这条通道还在试，是否值得发布由人看过再定。
"""
import datetime as dt
from pathlib import Path

import compose
import config
import drafts
import images
import main as mn
import render
import select_ as sel
import vault
import verify

MIN_SEED_CHARS = 2000     # 太短的笔记扩写等于让模型自由发挥，不是「以它为引子」


def candidates(notes, used=()):
    """够分量、还没当过引子的笔记，长的排前面。

    体量下限是 2000 字符：再短的笔记撑不起一个主题，模型只能自由发挥，
    那就不是「以笔记为引子」而是「让模型写篇命题作文」了。上限沿用
    config.MAX_NOTE_CHARS —— 超过的是整书转录，本来就不该发。
    """
    used = set(used)
    out = [n for n in sel.publishable(notes)
           if n.path not in used and MIN_SEED_CHARS <= len(n.body) <= config.MAX_NOTE_CHARS]
    return sorted(out, key=lambda n: -len(n.body))


def _as_group(note):
    """套一个单篇的 Group，好让 frontmatter、取图、校验那几步原样复用。"""
    return sel.Group(tag=sel._primary_tag(note) or '杂记',
                     notes=[note],
                     source_hash=sel._hash([note]),
                     slug=drafts.slugify_cn(Path(note.path).stem))


def run(vault_root, blog_root, api_key, sa_json, seed_paths=(), count=1,
        _index=None, _download=None, _compose=None):
    """返回每篇引子文章的产出与校验结果。文章写进 _review/ 等人工过目。"""
    vault_root, blog_root = Path(vault_root), Path(blog_root)
    notes = vault.load_vault(vault_root)
    by_path = {n.path: n for n in notes}

    if seed_paths:
        picked = [by_path[p] for p in seed_paths if p in by_path]
        missing = [p for p in seed_paths if p not in by_path]
    else:
        picked, missing = candidates(notes)[:count], []

    if not picked:
        return [{'status': 'error', 'reason': f'找不到引子笔记: {missing or "无候选"}'}]

    if _index is None:
        svc = images.drive_service(sa_json)
        index = images.load_index(
            Path(__file__).parent / 'drive_index.json',
            lambda: images.build_drive_index(svc, config.DRIVE_FOLDER_ID))
    else:
        svc, index = None, _index

    composer = _compose or compose.compose_seed
    results = []
    for note in picked:
        g = _as_group(note)
        img_map, gone = images.fetch_images(
            note.images, index, svc,
            blog_root / 'public' / 'images' / g.slug, f'/images/{g.slug}',
            _download=_download)

        article = composer(note, api_key)
        title, article = mn.split_title(article, g)
        res = verify.verify(note.body, article,
                            [i for i in note.images if i not in gone])

        body = render.rewrite_images(article, img_map, gone,
                                     {i: render.caption_for(note) for i in note.images})
        doc = mn.assemble_frontmatter(g, title, mn.first_paragraph(article)) + body

        out = blog_root / '_review' / f'seed-{g.slug}.md'
        out.parent.mkdir(parents=True, exist_ok=True)
        head = ('<!-- 引子通道产出，人工过目后移入 src/content/posts/ 即可发布。\n'
                f'引子笔记：{note.path}（{len(note.body):,} 字符）\n'
                f'扩写后：{len(article):,} 字符\n'
                + ('校验：全部通过\n' if res.ok else '校验未通过：\n' + '\n'.join(res.failures) + '\n')
                + '-->\n')
        out.write_text(head + doc, encoding='utf-8')

        results.append({'seed': note.path, 'slug': g.slug, 'title': title,
                        'seedChars': len(note.body), 'articleChars': len(article),
                        'ok': res.ok, 'failures': res.failures,
                        'images': len(img_map), 'missingImages': gone,
                        'file': str(out.relative_to(blog_root))})
    return results
