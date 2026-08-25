"""流水线入口：串起选题 → 取图 → 整理 → 校验 → 落盘。

两条通道：
  自动通道  python main.py --vault <路径> [--count N]
  手动通道  python main.py --drafts
引子通道（试运行，产出落 _review/）：
  python main.py --seed [笔记路径...] --vault <路径> [--count N]
另有两条辅助通道：
  补图      python main.py --repair-images
  图片体检  python main.py --audit-images --vault <路径>
"""
import argparse
import collections
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import compose            # noqa: E402
import config             # noqa: E402
import images             # noqa: E402
import render             # noqa: E402
import select_ as sel     # noqa: E402
import vault              # noqa: E402
import verify             # noqa: E402

H1 = re.compile(r'^#\s+(.+?)\s*$', re.M)
H2 = re.compile(r'^##\s+(.+)$', re.M)


def _q(s):
    """YAML 双引号转义。拼错一个引号，Astro 构建就整站失败。"""
    return str(s).replace('\\', '\\\\').replace('"', '\\"')


def assemble_frontmatter(group, title, description=''):
    """frontmatter 由流水线拼装，不让 LLM 生成 —— 否则它会编造日期和标签。"""
    refs, seen_ref = [], set()
    for n in group.notes:
        for v in (n.book, n.paper, n.link):
            if v and v not in seen_ref:
                seen_ref.add(v)
                refs.append(v)

    lines = ['---',
             f'title: "{_q(title)}"',
             f'date: {dt.date.today().isoformat()}',
             f'category: "{_q(group.tag.split("/")[0])}"',
             f'primaryTag: "{_q(group.tag)}"',
             f'description: "{_q(description)}"',
             'tags:']
    lines += [f'  - "{_q(t)}"' for t in _group_tags(group)]
    # 空列表键不输出：`references:` 后面直接跟下一个键，YAML 解析成 null
    if refs:
        lines.append('references:')
        lines += [f'  - "{_q(r)}"' for r in refs]
    lines.append('sourceNotes:')
    lines += [f'  - "{_q(n.path)}"' for n in group.notes]
    lines.append('---')
    return '\n'.join(lines) + '\n\n'


def _group_tags(group):
    """只保留组内至少两篇笔记共有的标签，加上主标签兜底。

    收全部标签的话一篇文章能挂 62 个（实测中位数 14），文章会出现在
    几十个标签页上、大多不相关，标签导航直接作废。只出现一次的标签是
    某篇笔记的个人属性，不是这组内容的共性。
    """
    cnt = collections.Counter(t for n in group.notes for t in n.tags)
    shared = [t for t, c in cnt.items() if c >= 2]
    if group.tag not in shared:
        shared.append(group.tag)
    return sorted(shared)


def split_title(article_md, group):
    """抽出 H1 当文章标题，并把它从正文里摘掉（标题由版式单独渲染）。

    退而取第一个 H2、再退到标签末段。取 H2 只是兜底 —— 那是第一个章节
    标题不是文章标题，会得到「HCP」「PTM」这种没有信息量的标题。
    """
    m = H1.search(article_md)
    if m:
        body = (article_md[:m.start()] + article_md[m.end():]).lstrip('\n')
        return m.group(1).strip(), body
    m = H2.search(article_md)
    return (m.group(1).strip() if m else group.tag.split('/')[-1]), article_md


def first_paragraph(md, limit=140):
    """取导读段落当摘要：跳过标题、图片、callout、代码块。"""
    for block in re.split(r'\n\s*\n', md):
        t = block.strip()
        if not t or t.startswith(('#', '>', '|', '```', '![', '*[')):
            continue
        t = re.sub(r'!\[[^\]]*\]\([^)]*\)|\[([^\]]*)\]\([^)]*\)|[*`_#>]', r'\1', t)
        t = re.sub(r'\s+', ' ', t).strip()
        if len(t) >= 20:
            return t[:limit]
    return ''



def load_published(blog_root):
    p = Path(blog_root) / 'published.json'
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}


def title_slug_map(published):
    """源笔记标题 → 文章 slug，供双链解析用。"""
    return {t: rec['slug'] for rec in published.values()
            for t in rec.get('noteTitles', [])}


def run_auto(vault_root, blog_root, api_key, sa_json, count=1):
    vault_root, blog_root = Path(vault_root), Path(blog_root)
    pub_path = blog_root / 'published.json'
    published = load_published(blog_root)

    groups = sel.build_groups(vault.load_vault(vault_root))
    svc = images.drive_service(sa_json)
    index = images.load_index(
        Path(__file__).parent / 'drive_index.json',
        lambda: images.build_drive_index(svc, config.DRIVE_FOLDER_ID))

    # 还躺在 _review/ 里的组等着人工复核，跳过，否则它会一直霸占队首。
    # 人工把文件移走或删掉，该组自动重新入列 —— 用文件系统当状态，不另设账本。
    skip = {g.tag for g in groups
            if (blog_root / '_review' / f'{g.slug}.md').exists()}

    results = []
    for _ in range(count):
        g = sel.pick_next(groups, published, skip)
        if not g:
            break
        skip.add(g.tag)   # 本次运行内不再重复挑中

        src_text = '\n\n'.join(n.body for n in g.notes)
        src_images = list(dict.fromkeys(i for n in g.notes for i in n.images))

        img_map, missing = images.fetch_images(
            src_images, index, svc,
            blog_root / 'public' / 'images' / g.slug, f'/images/{g.slug}')

        article = compose.compose(g, api_key)
        title, article = split_title(article, g)
        # 找不到的图不参与校验：它们本来就发不出去，不该算作 AI 丢图
        res = verify.verify(src_text, article,
                            [i for i in src_images if i not in missing])

        caption_of = {i: render.caption_for(n) for n in g.notes for i in n.images}
        body = render.rewrite_images(article, img_map, missing, caption_of)
        body = render.resolve_wikilinks(body, title_slug_map(published))
        doc = assemble_frontmatter(g, title, first_paragraph(article)) + body

        if res.ok:
            out = blog_root / 'src' / 'content' / 'posts' / f'{g.slug}.md'
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(doc, encoding='utf-8')
            published[g.tag] = {
                'slug': g.slug,
                'published_at': dt.date.today().isoformat(),
                'source_hash': g.source_hash,
                'notes': [n.path for n in g.notes],
                'noteTitles': [n.title for n in g.notes],
            }
            pub_path.write_text(
                json.dumps(published, ensure_ascii=False, indent=2), encoding='utf-8')
        else:
            out = blog_root / '_review' / f'{g.slug}.md'
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(
                '<!-- 校验未通过，人工复核后移入 src/content/posts/ 即可发布：\n'
                + '\n'.join(res.failures) + '\n-->\n' + doc, encoding='utf-8')

        results.append({'slug': g.slug, 'tag': g.tag, 'notes': len(g.notes),
                        'status': 'published' if res.ok else 'review',
                        'failures': res.failures, 'missingImages': missing})
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vault', help='Obsidian 仓库路径（自动通道必填）')
    ap.add_argument('--blog', default=str(Path(__file__).parent.parent))
    ap.add_argument('--count', type=int, default=1)
    ap.add_argument('--drafts', action='store_true', help='只处理 drafts/，跳过 AI 通道')
    ap.add_argument('--routinerun', metavar='REPO', help='把 RoutineRun 笔记接成工具与效率栏目')
    ap.add_argument('--repair-images', action='store_true',
                    help='给已发布文章补取当时没取到的图（Drive 补传后跑）')
    ap.add_argument('--refresh-index', action='store_true',
                    help='强制重建 Drive 索引，不吃 7 天缓存')
    ap.add_argument('--audit-images', action='store_true',
                    help='列出待发布笔记里 Drive 上没有的图（只读索引缓存）')
    ap.add_argument('--seed', nargs='*', metavar='NOTE',
                    help='引子通道：以单篇笔记为引子扩写成文章，产出落 _review/。'
                         '可指定一或多个笔记路径，省略则按体量自动挑')
    a = ap.parse_args()

    if a.seed is not None:
        import seed as seed_channel
        if not a.vault:
            ap.error('引子通道需要 --vault')
        rs = seed_channel.run(a.vault, a.blog, os.environ['DEEPSEEK_API_KEY'],
                              os.environ['GDRIVE_SA_JSON'], a.seed, a.count)
    elif a.audit_images:
        import repair
        if not a.vault:
            ap.error('体检要读 vault，需要 --vault')
        rs = repair.audit(a.vault)
    elif a.repair_images:
        import repair
        rs = repair.run(a.blog, os.environ['GDRIVE_SA_JSON'], a.refresh_index)
    elif a.routinerun:
        import routinerun
        rs = routinerun.run(a.routinerun, a.blog)
    elif a.drafts:
        import drafts
        rs = drafts.run_drafts(a.blog, os.environ['GDRIVE_SA_JSON'])
    else:
        if not a.vault:
            ap.error('自动通道需要 --vault')
        rs = run_auto(a.vault, a.blog, os.environ['DEEPSEEK_API_KEY'],
                      os.environ['GDRIVE_SA_JSON'], a.count)
    print(json.dumps(rs, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
