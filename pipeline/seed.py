"""引子通道：单篇笔记做引子，按加减法原则整理成一篇可发表的文章。

自动通道是「多篇笔记打散重组」，产出容易有拼接感：几篇笔记各讲各的，
模型只能按顺序摆，覆盖面广但每节浅尝辄止。这条通道换个取材方式 ——
一篇笔记当引子，按它自身的完整度决定做加法还是减法：

    减法（笔记已经足够完整）：浓缩、归纳、把流水账整理成有层次的段落，
                              不新增实质内容
    加法（笔记有主题但不完整）：补主题本身缺的环节，且每处扩展都要标注
                              可核验的来源

「有没有编造」没法用正则判定，所以把问题换个形式：强制模型为扩展内容
写出 `[依据 N]` 标注与来源清单，再由 evidence.py 逐条回原文核对。扩展
素材优先从同一知识库里取（相关片段随提示词一起喂进去），这样来源天然
可核验；实在没有再退到引子笔记里已出现过的文献。
"""
import re
from pathlib import Path

import compose
import config
import drafts
import evidence
import images
import main as mn
import render
import select_ as sel
import vault
import verify

# 超过这个体量的笔记按「已经足够完整」处理，走减法。实测 12k 字符以上的
# 笔记基本都已经自成体系，再让模型加东西只会稀释密度。
SHRINK_THRESHOLD = 12_000
MAX_FRAGMENTS = 6            # 喂给模型的相关片段篇数
FRAGMENT_CHARS = 3_000       # 每篇片段截取长度


def decide_mode(note):
    return 'shrink' if len(note.body) >= SHRINK_THRESHOLD else 'grow'


def candidates(notes, used=()):
    """还没当过引子的可发布笔记，长的排前面。字数不限 —— 长的走减法，
    短的走加法，两头都有出路。"""
    used = set(used)
    return sorted((n for n in sel.publishable(notes) if n.path not in used),
                  key=lambda n: -len(n.body))


def related_fragments(note, notes, limit=MAX_FRAGMENTS):
    """同主题的其他笔记，给加法模式当扩展素材。

    先取三级标签相同的，不够再放宽到二级；正文里双链指到的优先。这些
    片段是「可核验的来源」的唯一合法出处 —— 模型只能引用这里出现过的
    路径，编一个知识库里不存在的路径会被 evidence.check 当场拦下。
    """
    tag = sel._primary_tag(note) or ''
    lvl3, lvl2 = '/'.join(tag.split('/')[:3]), '/'.join(tag.split('/')[:2])
    linked = set(note.wikilinks)

    def score(n):
        t = sel._primary_tag(n) or ''
        return (n.title in linked, t.startswith(lvl3), t.startswith(lvl2))

    pool = [n for n in sel.publishable(notes)
            if n.path != note.path and any(score(n))]
    pool.sort(key=lambda n: (score(n), len(n.body)), reverse=True)
    return pool[:limit]


def related_published(note, published, posts_dir):
    """同二级标签的已发布文章 → [(slug, 标题)]，用来生成「相关阅读」。"""
    tag = sel._primary_tag(note) or ''
    lvl2 = '/'.join(tag.split('/')[:2])
    out = []
    for rec_tag, rec in published.items():
        if not rec_tag.startswith(lvl2):
            continue
        title = _post_title(Path(posts_dir) / f"{rec['slug']}.md") or rec['slug']
        out.append((rec['slug'], title))
    return out


def _post_title(path):
    if not Path(path).exists():
        return None
    m = re.search(r'^title:\s*"?(.+?)"?\s*$',
                  Path(path).read_text(encoding='utf-8'), re.M)
    return m.group(1) if m else None


def _as_group(note):
    """套一个单篇的 Group，好让 frontmatter、取图、校验那几步原样复用。"""
    return sel.Group(tag=sel._primary_tag(note) or '杂记',
                     notes=[note],
                     source_hash=sel._hash([note]),
                     slug=drafts.slugify_cn(Path(note.path).stem))


def build_message(note, mode, fragments):
    """加减法模式与相关片段一起交代清楚。"""
    head = ('【减法模式】这篇笔记本身已经足够完整，请按减法原则浓缩归纳，不要新增实质内容。\n'
            if mode == 'shrink' else
            '【加法模式】这篇笔记有主题但内容不完整，请按加法原则补齐，'
            '每处扩展都要按格式标注可核验的来源。\n')
    parts = [head, '\n', compose.build_seed_message(note)]
    if mode == 'grow' and fragments:
        parts.append('\n\n---\n\n以下是同一知识库里与本主题相关的片段，'
                     '扩展时优先从这里取材。引用时用它们的完整路径：\n')
        for f in fragments:
            parts.append(f'\n### 相关片段：`{f.path}`\n{f.body.strip()[:FRAGMENT_CHARS]}\n')
    return ''.join(parts)


def process(note, *, blog_root, notes, published, index, svc, api_key,
            publish=False, local_images=None, _download=None, _chat=None):
    """整理一篇 → 取图 → 校验 → 落盘。引子通道与人工通道共用这一段。"""
    blog_root = Path(blog_root)
    posts_dir = blog_root / 'src' / 'content' / 'posts'
    used_seeds = [r['seed'] for r in published.values() if r.get('seed')]

    mode = decide_mode(note)
    frags = related_fragments(note, notes) if mode == 'grow' else []
    g = _as_group(note)
    out_dir = blog_root / 'public' / 'images' / g.slug

    img_map, missing = {}, []
    if local_images:
        img_map, missing = images.copy_local(note.images, local_images, out_dir,
                                             f'/images/{g.slug}')
    if missing or not local_images:
        rest = missing or [i for i in note.images if i not in img_map]
        fetched, missing = images.fetch_images(rest, index, svc, out_dir,
                                               f'/images/{g.slug}', _download=_download)
        img_map.update(fetched)

    user_msg = build_message(note, mode, frags)
    article = (_chat or compose.compose_seed_message)(user_msg, api_key)
    title, article = mn.split_title(article, g)

    rel = related_published(note, published, posts_dir)
    body = render.rewrite_images(article, img_map, missing,
                                 {i: render.caption_for(note) for i in note.images})
    body = render.append_related(body, rel)

    fidelity = verify.verify(note.body, article,
                             [i for i in note.images if i not in missing])
    pub_check = verify.review(
        body, mode=mode, seed_chars=len(note.body), seed_path=note.path,
        used_seeds=used_seeds, related_slugs=[s for s, _ in rel],
        note_bodies={n.path: n.body for n in [note] + frags},
        source_text=user_msg)
    fails = fidelity.failures + pub_check.failures
    ok = not fails

    doc = mn.assemble_frontmatter(g, title, mn.first_paragraph(article)) + body
    if ok and publish:
        out = posts_dir / f'{g.slug}.md'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(doc, encoding='utf-8')
        mn.record_published(blog_root, published, g, seed=note.path, title=title)
    else:
        out = blog_root / '_review' / f'seed-{g.slug}.md'
        out.parent.mkdir(parents=True, exist_ok=True)
        head = ('<!-- 引子通道产出。'
                + ('校验全过，人工确认后移入 src/content/posts/ 即可发布。\n'
                   if ok else '校验未通过，逐条处理后再移入 src/content/posts/。\n')
                + f'来源：{note.path}\n'
                + f'模式：{"减法" if mode == "shrink" else "加法"}　'
                + f'{len(note.body):,} 字符 → {len(article):,} 字符\n'
                + ('' if ok else '问题：\n' + '\n'.join(f'  - {f}' for f in fails) + '\n')
                + '-->\n')
        out.write_text(head + doc, encoding='utf-8')

    return {'seed': note.path, 'slug': g.slug, 'title': title, 'mode': mode,
            'seedChars': len(note.body), 'articleChars': len(article),
            'fragments': len(frags), 'ok': ok, 'failures': fails,
            'images': len(img_map), 'missingImages': missing,
            'related': [s for s, _ in rel],
            'status': 'published' if (ok and publish) else 'review',
            'file': str(out.relative_to(blog_root))}


def open_index(sa_json, _index=None):
    """取图索引与 Drive 客户端。测试注入 _index 就完全不碰网络。"""
    if _index is not None:
        return _index, None
    svc = images.drive_service(sa_json)
    return images.load_index(
        Path(__file__).parent / 'drive_index.json',
        lambda: images.build_drive_index(svc, config.DRIVE_FOLDER_ID)), svc


def run(vault_root, blog_root, api_key, sa_json, seed_paths=(), count=1,
        publish=False, _index=None, _download=None, _chat=None):
    """引子通道：从知识库里挑笔记当引子。

    publish=False（默认）产出落 _review/ 等人工过目；publish=True 时校验
    全过的直接写进 posts/ 并记账，不过的仍然落 _review/。
    """
    vault_root, blog_root = Path(vault_root), Path(blog_root)
    notes = vault.load_vault(vault_root)
    by_path = {n.path: n for n in notes}
    published = mn.load_published(blog_root)
    used_seeds = [r['seed'] for r in published.values() if r.get('seed')]

    if seed_paths:
        picked = [by_path[p] for p in seed_paths if p in by_path]
        gone = [p for p in seed_paths if p not in by_path]
        if gone:
            return [{'status': 'error', 'reason': f'找不到引子笔记: {gone}'}]
    else:
        picked = candidates(notes, used_seeds)[:count]
    if not picked:
        return [{'status': 'error', 'reason': '没有可用的引子笔记'}]

    index, svc = open_index(sa_json, _index)
    return [process(n, blog_root=blog_root, notes=notes, published=published,
                    index=index, svc=svc, api_key=api_key, publish=publish,
                    _download=_download, _chat=_chat) for n in picked]
