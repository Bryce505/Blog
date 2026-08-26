"""人工投稿通道：自己写的稿子也走一遍加减法与校验。

跟引子通道的区别只在取材：稿子来自 drafts/ 而不是知识库。整理、取图、
校验、落盘全部复用 seed.process，所以人工稿和自动稿的质量门槛完全一致。

投稿方式见 README「人工投稿」一节：
    drafts/我的稿子.md              正文
    drafts/images/我的稿子/图1.png   随稿上传的图（可选）

图片三条路依次尝试：随稿上传的本地图 → Drive 上按文件名找 → 外链原样
保留。三条都不中就在正文里留「图片暂缺」占位，并计入校验失败。
"""
import re
from pathlib import Path

import seed as seed_channel
import vault
import yaml

H1 = re.compile(r'^#\s+(.+?)\s*$', re.M)
DEFAULT_TAG = '杂记/投稿'


def as_note(path, drafts_dir):
    """把投稿文件读成一个 Note。frontmatter 可有可无。"""
    text = Path(path).read_text(encoding='utf-8')
    m = vault.FM_RE.match(text)
    fm = {}
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            fm = {}
        text = text[m.end():]
    body = vault.html_img_to_md(text)

    title = str(fm.get('title') or '').strip()
    h1 = H1.search(body)
    if not title and h1:
        title = h1.group(1).strip()
        body = (body[:h1.start()] + body[h1.end():]).lstrip('\n')
    title = title or Path(path).stem

    tags = fm.get('tags') or [DEFAULT_TAG]
    if isinstance(tags, str):
        tags = [tags]

    imgs = []
    for pat in (vault.IMG_MD, vault.IMG_WIKI):
        for raw in pat.findall(body):
            n = vault.image_ref_name(raw)
            if n and n not in imgs:
                imgs.append(n)

    return vault.Note(
        path=str(Path(path).relative_to(drafts_dir)).replace('\\', '/'),
        title=title, tags=[str(t) for t in tags if t],
        type=str(fm.get('type') or 'note'),
        description=str(fm.get('description') or ''),
        book=str(fm.get('book') or ''), paper=str(fm.get('paper') or ''),
        link=str(fm.get('link') or ''), body=body, images=imgs,
        wikilinks=[t for t, _ in vault.WIKILINK.findall(body)])


def run(vault_root, blog_root, api_key, sa_json, publish=True,
        _index=None, _download=None, _chat=None):
    """处理 drafts/ 下的所有 md。处理完的原稿删掉，避免下次重复处理。"""
    blog_root = Path(blog_root)
    drafts_dir = blog_root / 'drafts'
    files = sorted(p for p in drafts_dir.glob('*.md') if p.name != 'README.md')
    if not files:
        return []

    notes = vault.load_vault(Path(vault_root)) if vault_root else []
    import main as mn
    published = mn.load_published(blog_root)
    index, svc = seed_channel.open_index(sa_json, _index)

    results = []
    for f in files:
        note = as_note(f, drafts_dir)
        r = seed_channel.process(
            note, blog_root=blog_root, notes=notes, published=published,
            index=index, svc=svc, api_key=api_key, publish=publish,
            local_images=drafts_dir / 'images' / f.stem,
            _download=_download, _chat=_chat)
        r['source'] = f'drafts/{f.name}'
        # 已转成文章就把原稿撤走，留着会被下次运行重复处理
        f.unlink()
        results.append(r)
    return results
