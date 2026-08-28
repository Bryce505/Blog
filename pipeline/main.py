"""流水线入口：串起选题 → 取图 → 整理 → 校验 → 落盘。

两条通道：
  自动通道  python main.py --vault <路径> [--count N]
  手动通道  python main.py --drafts
引子通道（单篇笔记做引子，按加减法整理）：
  python main.py --seed [笔记路径...] --vault <路径> [--count N] [--publish]
人工投稿通道（处理 drafts/ 下的稿子）：
  python main.py --manual --vault <路径> [--publish]
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
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import compose            # noqa: E402
import config             # noqa: E402
import images             # noqa: E402
import render             # noqa: E402
import select_ as sel     # noqa: E402
import vault              # noqa: E402
import yaml               # noqa: E402
import verify             # noqa: E402

H1 = re.compile(r'^#\s+(.+?)\s*$', re.M)
H2 = re.compile(r'^##\s+(.+)$', re.M)


def _q(s):
    """YAML 双引号转义。拼错一个引号，Astro 构建就整站失败。"""
    return str(s).replace('\\', '\\\\').replace('"', '\\"')


def assemble_frontmatter(group, title, description='', draft_notes=None):
    """frontmatter 由流水线拼装，不让 LLM 生成 —— 否则它会编造日期和标签。

    draft_notes 不是 None 就打草稿位：文章照样落 posts/，但 `draft: true`
    让站点构建跳过它。放行 = 删掉那一行，不用改名、不用移文件、不用记账。
    reviewNotes 用 YAML 列表而不是 HTML 注释 —— GitHub 的 markdown 预览会把
    `<!-- -->` 整段吃掉，人打开文件根本看不见没过哪几项（实测踩过）。
    """
    refs, seen_ref = [], set()
    for n in group.notes:
        for v in (n.book, n.paper, n.link):
            if v and v not in seen_ref:
                seen_ref.add(v)
                refs.append(v)

    lines = ['---']
    # 草稿位放最前面：打开文件第一眼就看见「这是草稿」和为什么
    if draft_notes is not None:
        lines.append('draft: true')
        if draft_notes:
            lines.append('reviewNotes:')
            lines += [f'  - "{_q(f)}"' for f in draft_notes]
    lines += [f'title: "{_q(title)}"',
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



def record_published(blog_root, published, group, seed=None, title=None, draft=False):
    """把一篇记进 published.json 并落盘。

    key 用 slug 不用 tag：同一个三级标签下会有多篇文章（实测 ELISA 与
    HCP鉴定与定量 的 primaryTag 完全相同），用 tag 做 key 时后写的会静默
    覆盖先写的，被覆盖那篇于是变回「没发过」，下次定时任务重新生成一遍。
    slug 就是文件名，天然唯一。

    草稿也要记账：不记的话下次自动选材又挑中同一篇，再烧一次 DeepSeek。
    """
    rec = {
        'slug': group.slug,
        'tag': group.tag,
        'published_at': dt.date.today().isoformat(),
        'source_hash': group.source_hash,
        'notes': [n.path for n in group.notes],
        'noteTitles': [n.title for n in group.notes],
    }
    if title:
        rec['title'] = title
    if seed:
        rec['seed'] = seed
    if draft:
        rec['draft'] = True
    published[group.slug] = rec
    save_published(blog_root, published)
    return rec


def save_published(blog_root, published):
    """落盘前按发布日期新→旧重排，同一天内后写入的排更前。

    实测反馈：原来直接按 dict 插入顺序落盘，等于最早发布的排最前——手机
    或网页里直接打开 published.json 确认发表状态，要拉到文件末尾才能看到
    最新一条，很不方便。这里把当前顺序整体反转，再按 published_at 做稳定
    排序（reverse=True）：稳定排序保留「同一天」这些记录参与排序前的相对
    顺序，也就是反转后的顺序，等价于「同一天内写入更晚的排更前」。只改这
    一处、不改 record_published/reconcile 的写入逻辑——不管内存里那份
    dict 顺序被谁怎么增删过，落到磁盘上的顺序始终正确。
    """
    items = list(published.items())[::-1]
    ordered = dict(sorted(items, key=lambda kv: kv[1].get('published_at', ''),
                          reverse=True))
    (Path(blog_root) / 'published.json').write_text(
        json.dumps(ordered, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def load_published(blog_root):
    """读账本，并先跟 posts/ 对一次账。

    对账是这套「放行 = 删一行、退稿 = 删文件」的前提：人只动文件，
    账本自己跟上，没有第二处状态要人工同步。
    """
    p = Path(blog_root) / 'published.json'
    published = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
    return reconcile(blog_root, published)


def _post_meta(path):
    """读文章 frontmatter。坏 YAML 当空处理，不能让一篇坏文章卡死整条流水线。"""
    m = vault.FM_RE.match(Path(path).read_text(encoding='utf-8'))
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def reconcile(blog_root, published):
    """让账本跟 src/content/posts/ 对上：缺的回填，文件没了的销账。

    实测过一次漏账的后果：HCP鉴定与定量 手工搬进 posts/ 并上线，
    published.json 里没有记录，引子通道按 seed 字段去重于是仍算「没用过」,
    下一次定时任务重新挑中同一篇笔记、再烧一次 DeepSeek、覆盖已发布的文章。
    """
    posts = Path(blog_root) / 'src' / 'content' / 'posts'
    have = {p.stem: p for p in sorted(posts.glob('*.md'))} if posts.is_dir() else {}

    # 旧账本按 tag 做 key，就地改成按 slug。丢 source_hash 会让自动通道
    # 把已发布的组当成「源笔记变了」重发一遍，所以是搬记录不是重建。
    for key in [k for k, r in published.items()
                if isinstance(r, dict) and r.get('slug') and k != r['slug']]:
        rec = published.pop(key)
        rec.setdefault('tag', key)
        published[rec['slug']] = rec

    for slug in [s for s in published if s not in have]:
        del published[slug]

    for slug, path in have.items():
        fm = _post_meta(path)
        if slug in published:
            # 人删掉 draft 那一行 = 放行，账本跟着改口径
            if fm.get('draft'):
                published[slug]['draft'] = True
            else:
                published[slug].pop('draft', None)
            continue
        notes = [str(n) for n in (fm.get('sourceNotes') or [])]
        rec = {'slug': slug,
               'tag': str(fm.get('primaryTag') or fm.get('category') or ''),
               'published_at': str(fm.get('date') or ''),
               'notes': notes}
        if fm.get('title'):
            rec['title'] = str(fm['title'])
        # 引子通道产出恰好一篇源笔记，自动通道是一组 —— 据此还原 seed
        if len(notes) == 1:
            rec['seed'] = notes[0]
        if fm.get('draft'):
            rec['draft'] = True
        published[slug] = rec
    return published


def title_slug_map(published):
    """源笔记标题 → 文章 slug，供双链解析用。草稿没有页面，链过去是死链。"""
    return {t: rec['slug'] for rec in published.values() if not rec.get('draft')
            for t in rec.get('noteTitles', [])}


def run_auto(vault_root, blog_root, api_key, sa_json, count=1):
    vault_root, blog_root = Path(vault_root), Path(blog_root)
    published = load_published(blog_root)

    groups = sel.build_groups(vault.load_vault(vault_root))
    svc = images.drive_service(sa_json)
    index = images.load_index(
        Path(__file__).parent / 'drive_index.json',
        lambda: images.build_drive_index(svc, config.DRIVE_FOLDER_ID))

    # 没过校验的组也记了账（带 draft 标），pick_next 自然不会再挑中它，
    # 不用另外维护一份跳过名单。人删掉文件 = 退稿，reconcile 销账后重新入列。
    skip = set()
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
        doc = assemble_frontmatter(g, title, first_paragraph(article),
                                   draft_notes=None if res.ok else res.failures) + body

        out = blog_root / 'src' / 'content' / 'posts' / f'{g.slug}.md'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(doc, encoding='utf-8')
        record_published(blog_root, published, g, draft=not res.ok)

        results.append({'slug': g.slug, 'tag': g.tag, 'notes': len(g.notes),
                        'status': 'published' if res.ok else 'draft',
                        'ok': res.ok, 'file': str(out.relative_to(blog_root)),
                        'failures': res.failures, 'missingImages': missing})
    return results


def resolve_seed_url(s):
    """把 GitHub 链接或裸路径统一成 vault 内的相对路径。

    手动指定引子时，直接在 Obsidian-base 仓库里翻目录、复制文件的 GitHub
    链接（形如 .../blob/master/A/B.md，中文和斜杠会被转成 %E6%8A%97...
    这种 percent-encoding），比记一遍不含扩展名的短路径更顺手——本来就
    要先在私有仓库里找到这篇笔记，链接就在那顺手复制到。

    找不到对应笔记不在这里报错：解析失败原样把输入当路径返回，交给
    seed.run() 已有的「找不到引子笔记」校验兜底，不重复一套错误处理。
    """
    s = s.strip()
    if not s.startswith('http'):
        return s
    s = s.split('?', 1)[0]                        # 去掉 ?plain=1 这类查询参数
    m = re.search(r'/(?:blob|raw|blame)/[^/]+/(.+)$', s)
    return urllib.parse.unquote(m.group(1)) if m else s


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
                    help='引子通道：单篇笔记做引子，按加减法整理成文章。'
                         '可指定一或多个笔记路径，省略则自动挑')
    ap.add_argument('--seed-url', metavar='URL_OR_PATH',
                    help='引子通道：GitHub 链接（在 Obsidian-base 里翻到'
                         '笔记后复制的那种 .../blob/分支/路径.md）或裸的'
                         'vault 内相对路径，跟 --seed 二选一')
    ap.add_argument('--manual', action='store_true',
                    help='人工投稿通道：处理 drafts/ 下的稿子，同样走加减法与校验')
    ap.add_argument('--publish', action='store_true',
                    help='校验全过就直接发布；不加则一律带 draft 标等人工放行')
    a = ap.parse_args()

    if a.manual:
        import manual
        rs = manual.run(a.vault, a.blog, os.environ['DEEPSEEK_API_KEY'],
                        os.environ['GDRIVE_SA_JSON'], publish=a.publish)
    elif a.seed is not None or a.seed_url:
        import seed as seed_channel
        if not a.vault:
            ap.error('引子通道需要 --vault')
        # 两种指定方式收拢成同一个 seed_paths：--seed 是原来的裸路径
        # （可能不指定，交给自动选材），--seed-url 是手动触发时更顺手的
        # GitHub 链接，解析成路径后走同一条 run()。
        seed_paths = [resolve_seed_url(a.seed_url)] if a.seed_url else a.seed
        rs = seed_channel.run(a.vault, a.blog, os.environ['DEEPSEEK_API_KEY'],
                              os.environ['GDRIVE_SA_JSON'], seed_paths, a.count,
                              publish=a.publish)
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
    # 写日志；有未通过的就开 issue、发邮件。通知失败不影响已经落盘的产出。
    if rs and isinstance(rs, list) and any(isinstance(r, dict) and 'ok' in r for r in rs):
        import notify
        print(json.dumps({'notify': notify.notify(a.blog, rs)}, ensure_ascii=False))
    print(json.dumps(rs, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
