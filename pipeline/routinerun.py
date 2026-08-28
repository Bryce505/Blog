"""把 RoutineRun 的工作笔记接成「工具与效率」栏目。

这个仓库 285 个 md 里 269 个是 .claude/skills 配置，真笔记只有几篇，
其中还有几个是几十字符的占位 README。所以两道过滤：跳过 .claude 等
配置目录，再按正文体量剔掉占位文件。
"""
import datetime as dt
import re
import urllib.parse
from pathlib import Path

import yaml

import drafts
import images
import main as mn
import render
import vault

CATEGORY = '工具与效率'
SKIP_DIRS = {'.claude', '.git', 'node_modules', '.venv'}
MIN_BODY_CHARS = 500   # 低于此的是占位 README，不是笔记

H1 = re.compile(r'^#\s+(.+?)\s*$', re.M)


def collect(repo_root):
    """返回 (path, title, body) 列表。"""
    repo_root = Path(repo_root)
    out = []
    for p in sorted(repo_root.rglob('*.md')):
        rel = p.relative_to(repo_root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel.name in ('CLAUDE.md', 'AGENTS.md'):
            continue          # 给 AI 看的配置，不是给人读的笔记
        text = p.read_text(encoding='utf-8', errors='ignore')
        m = vault.FM_RE.match(text)
        body = vault.html_img_to_md(text[m.end():] if m else text)
        if len(body.strip()) < MIN_BODY_CHARS:
            continue          # 占位 README
        m1 = H1.search(body)
        title = m1.group(1).strip() if m1 else rel.stem
        if m1:
            body = (body[:m1.start()] + body[m1.end():]).lstrip('\n')
        out.append((str(rel).replace('\\', '/'), title, body))
    return out


def _copy_images(repo_root, src_rel, body, blog_root, slug):
    """本地图片搬进 public/images/<slug>/ 并转 WebP。

    图源在本仓库而不是 Drive，但落地格式和 URL 前缀跟自动通道一致，
    版式那边不用区分两种来源。
    """
    repo_root, blog_root = Path(repo_root), Path(blog_root)
    note_dir = (repo_root / src_rel).parent
    out_dir = blog_root / 'public' / 'images' / slug
    mapping, missing = {}, []
    for raw in render.IMG_MD.findall(body) + render.IMG_WIKI.findall(body):
        ref = raw[1] if isinstance(raw, tuple) else raw
        name = vault.image_ref_name(ref)
        if not name:                       # 外链、笔记嵌入、非图片附件
            continue
        # 引用里的 %20 要解码回空格，否则本地文件按原样拼路径必然找不到
        src = note_dir / urllib.parse.unquote(
            ref.split('|')[0].strip().replace('\\', '/'))
        dest = out_dir / (Path(name).stem + '.webp')
        if dest.exists():
            mapping[name] = f'/images/{slug}/{images.url_safe(dest.name)}'
            continue
        if not src.exists():
            missing.append(name)
            continue
        try:
            images.to_webp(src.read_bytes(), dest)
        except Exception:
            missing.append(name)
            continue
        mapping[name] = f'/images/{slug}/{images.url_safe(dest.name)}'
    return mapping, missing


def run(repo_root, blog_root, today=None):
    """写入 src/content/posts/，已存在则跳过（不覆盖人工改动）。"""
    posts_dir = Path(blog_root) / 'src' / 'content' / 'posts'
    posts_dir.mkdir(parents=True, exist_ok=True)
    date = (today or dt.date.today()).isoformat()
    month = date[:7]

    results = []
    for rel, title, body in collect(repo_root):
        slug = 'tools-' + drafts.slugify_cn(Path(rel).stem)
        if slug in mn._all_posts(posts_dir):
            results.append({'file': rel, 'status': 'skipped', 'slug': slug})
            continue
        img_map, missing = _copy_images(repo_root, rel, body, blog_root, slug)
        body = render.rewrite_images(body, img_map, missing, {})
        fm = {
            'title': title,
            'date': date,
            'category': CATEGORY,
            'tags': [f'{CATEGORY}/{Path(rel).parts[0]}'],
            'description': drafts.fill_defaults(
                {'title': title}, Path(rel), body)['description'],
        }
        out = mn.post_path(posts_dir, slug, month)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
            + '---\n\n' + body, encoding='utf-8')
        results.append({'file': rel, 'status': 'published', 'slug': slug,
                        'images': len(img_map), 'missingImages': missing})
    return results
