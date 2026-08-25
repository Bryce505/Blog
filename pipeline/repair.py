"""把已发布文章里的「图片暂缺」占位重新取一次图。

图缺的原因基本只有一个：Drive 上没有那个文件名（实测 30 个待发布组
共 351 张引用图，17 张属于这种情况 —— 有的存在笔记同级的 res/、
attachments/ 里从没上传过 Drive，有的是早期 17 位时间戳命名，Drive 上
已经改名）。补传之后文章却修不好：published.json 里已经记了账，自动
通道不会重跑那篇，占位就永远留在页面上。

这条通道专治这个。占位标记里藏着文件名和图注（见 render.MISSING_TPL），
凭它重取一次即可，不用回头翻源笔记，也不用再烧一次 LLM。

索引默认仍走 7 天缓存：占位大多是永远补不回来的（源文件根本没上传过
Drive），每晚重建整个索引只是白跑一趟 API，还会让 drive_index.json
天天产生无意义的提交。刚补传完图想立刻生效，用 --refresh-index 强制
重建。没有占位要修就一次 Drive 都不碰。
"""
import json
from pathlib import Path

import config
import images
import render
import select_ as sel
import vault

INDEX_PATH = Path(__file__).parent / 'drive_index.json'


def run(blog_root, sa_json, refresh_index=False, _index=None, _download=None):
    """返回每篇文章补回了哪些图、还差哪些。"""
    posts_dir = Path(blog_root) / 'src' / 'content' / 'posts'
    pending = {}
    for p in sorted(posts_dir.glob('*.md')):
        marks = render.missing_marks(p.read_text(encoding='utf-8'))
        if marks:
            pending[p] = dict(marks)      # 同名图在一篇里可能出现多次
    if not pending:
        return []

    svc = None if _index is not None else images.drive_service(sa_json)
    index = _index if _index is not None else images.load_index(
        INDEX_PATH,
        lambda: images.build_drive_index(svc, config.DRIVE_FOLDER_ID),
        max_age_days=0 if refresh_index else 7)

    results = []
    for p, marks in pending.items():
        slug = p.stem
        img_map, missing = images.fetch_images(
            list(marks), index, svc,
            Path(blog_root) / 'public' / 'images' / slug, f'/images/{slug}',
            _download=_download)
        if img_map:
            p.write_text(render.restore_missing(
                p.read_text(encoding='utf-8'), img_map), encoding='utf-8')
        results.append({'slug': slug, 'status': 'repaired' if img_map else 'nothing',
                        'repaired': sorted(img_map), 'stillMissing': sorted(missing)})
    return results


def audit(vault_root, _index=None):
    """列出待发布笔记里 Drive 上没有的图，按源笔记分组。

    发文之前就想知道要往 Drive 补传哪些图 —— 否则只能等文章发出来、
    页面上出现「图片暂缺」才发现。只读索引缓存，一次 Drive 都不碰。

    实测 30 个待发布组共 351 张引用图，17 张查不到：大头是笔记同级的
    res/、attachments/ 这类从没上传过 Drive 的目录。
    """
    index = _index if _index is not None else json.loads(
        INDEX_PATH.read_text(encoding='utf-8'))['index']
    out = []
    for g in sel.build_groups(vault.load_vault(Path(vault_root))):
        for n in g.notes:
            gone = [i for i in n.images if not images.resolve(i, index)]
            if gone:
                out.append({'slug': g.slug, 'note': n.path, 'missing': gone})
    return out
