"""手动发布通道：drafts/*.md → 取图 + 双链解析 → src/content/posts/。

不经过 DeepSeek，不经过机械校验 —— 自己写的内容不需要防篡改，跑一遍
纯属浪费时间和 token。

存在的意义是替你办两件事：从 Obsidian 导出的稿子里，图片写的是
`![](../image&attachment/xxx.png)`、双链写的是 `[[目标笔记]]`，直接
发出去是一堆破图和方括号。
"""
import datetime as dt
import json
import re
import subprocess
from pathlib import Path

import yaml

import config
import images
import main as mn
import render
import vault

MD_NOISE = re.compile(r'!\[[^\]]*\]\([^)]*\)|\[\[|\]\]|[#*>`\[\]!]|\(https?://[^)]*\)')


def slugify_cn(text):
    s = re.sub(r'[^\w一-鿿]+', '-', str(text).strip().lower())
    return re.sub(r'-{2,}', '-', s).strip('-')


def _git_first_commit_date(path):
    """稿子首次提交的日期就是它的写作日期，比当天更准。"""
    try:
        out = subprocess.run(
            ['git', 'log', '--diff-filter=A', '--format=%ad', '--date=short',
             '--', str(path)],
            capture_output=True, text=True, timeout=10,
            cwd=str(Path(path).parent)).stdout.strip().splitlines()
        return out[-1] if out else None
    except (OSError, subprocess.SubprocessError):
        return None


def fill_defaults(fm, path, body):
    """手写稿只需要 title 一个必填字段，其余全部有默认值。"""
    title = str(fm.get('title') or '').strip()
    if not title:
        return None
    tags = fm.get('tags') or []
    if isinstance(tags, str):
        tags = [tags]
    tags = [str(t) for t in tags if t]
    plain = re.sub(r'\s+', ' ', MD_NOISE.sub('', body)).strip()
    return {
        'title': title,
        'slug': fm.get('slug') or slugify_cn(path.stem),
        'date': fm.get('date') or _git_first_commit_date(path) or dt.date.today().isoformat(),
        'tags': tags,
        'category': fm.get('category') or (tags[0].split('/')[0] if tags else '杂记'),
        'description': fm.get('description') or plain[:120],
        'references': fm.get('references') or [],
    }


def _dump(fm):
    return '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n'


def run_drafts(blog_root, sa_json):
    blog_root = Path(blog_root)
    draft_dir = blog_root / 'drafts'
    posts_dir = blog_root / 'src' / 'content' / 'posts'
    month = dt.date.today().strftime('%Y-%m')

    pub_path = blog_root / 'published.json'
    published = json.loads(pub_path.read_text(encoding='utf-8')) if pub_path.exists() else {}
    title_to_slug = {t: r['slug'] for r in published.values()
                     for t in r.get('noteTitles', [])}

    files = [p for p in sorted(draft_dir.glob('*.md'))
             if p.name.lower() != 'readme.md'] if draft_dir.exists() else []
    if not files:
        return []

    svc = images.drive_service(sa_json)
    index = images.load_index(
        Path(__file__).parent / 'drive_index.json',
        lambda: images.build_drive_index(svc, config.DRIVE_FOLDER_ID))

    results = []
    for p in files:
        note = vault.parse_note(p, draft_dir)
        if note is None:
            results.append({'file': p.name, 'status': 'error',
                            'reason': 'frontmatter 缺失或 YAML 损坏'})
            continue
        raw = yaml.safe_load(vault.FM_RE.match(
            p.read_text(encoding='utf-8')).group(1)) or {}
        fm = fill_defaults(raw, p, note.body)
        if fm is None:
            results.append({'file': p.name, 'status': 'error',
                            'reason': '缺少 title 字段'})
            continue

        if fm['slug'] in mn._all_posts(posts_dir):
            # 静默覆盖会让人莫名其妙丢文章，报错跳过并保留原件
            results.append({'file': p.name, 'status': 'error',
                            'reason': f"slug 冲突：{fm['slug']} 已存在，未覆盖"})
            continue

        img_map, missing = images.fetch_images(
            note.images, index, svc,
            blog_root / 'public' / 'images' / fm['slug'], f"/images/{fm['slug']}")
        body = render.rewrite_images(note.body, img_map, missing, {})
        body = render.resolve_wikilinks(body, title_to_slug)

        out = mn.post_path(posts_dir, fm['slug'], month)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(_dump(fm) + body, encoding='utf-8')
        p.unlink()   # 已转存，留着会被重复处理
        results.append({'file': p.name, 'status': 'published',
                        'slug': fm['slug'], 'missingImages': missing})
    return results
