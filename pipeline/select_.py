"""按标签分组选题。

文件名带下划线是为了避开标准库的 select 模块——同名靠 sys.path 顺序
取胜太脆，直接改名消除歧义。
"""
import hashlib
import re
from dataclasses import dataclass

import config


@dataclass
class Group:
    tag: str
    notes: list
    source_hash: str
    slug: str


def publishable(notes):
    """type 在白名单内、有标签、且体量正常的才可发布。

    体量上限不是性能优化，是内容判定：实测超过 20 万字符的「笔记」全是
    整本书或整套课程导入（如整本《Capillary Electrophoresis Methods for
    Pharmaceutical Analysis》，142 万字符），一篇就撑爆 1M 上下文，而且
    整书重组发布还有版权问题。
    """
    return [n for n in notes
            if n.type in config.PUBLISHABLE_TYPES
            and n.tags
            and len(n.body) <= config.MAX_NOTE_CHARS]


def _primary_tag(note):
    """归属规则：tags 中出现顺序最靠前、层级 >=3 的标签；没有则退到二级。

    一篇笔记只归一个组，否则同一内容会被写进多篇文章。
    """
    for t in note.tags:
        if t.count('/') >= 2:
            return t
    for t in note.tags:
        if t.count('/') >= 1:
            return t
    return None


def _slugify(tag):
    """三级标签转 URL slug。中文保留（Astro 支持 Unicode 路由），去掉空白与符号。"""
    s = tag.replace('/', '-')
    s = re.sub(r'[^\w一-鿿-]+', '-', s)
    return re.sub(r'-{2,}', '-', s).strip('-').lower()


def _hash(notes):
    """组内笔记正文的联合哈希。笔记内容一变，该组就进入可重发队列。"""
    h = hashlib.sha256()
    for n in sorted(notes, key=lambda x: x.path):
        h.update(n.path.encode())
        h.update(n.body.encode())
    return 'sha256:' + h.hexdigest()


def _fit_budget(ns):
    """按体量预算截取。小的优先入选，同预算下能多容纳几篇，文章视角更全。"""
    picked, used = [], 0
    for n in sorted(ns, key=lambda x: (len(x.body), x.path)):
        if len(picked) >= config.MAX_GROUP:
            break
        if used + len(n.body) > config.MAX_GROUP_CHARS:
            continue
        picked.append(n)
        used += len(n.body)
    return sorted(picked, key=lambda x: x.path)


def _make(tag, ns):
    """预算装不下 MIN_GROUP 篇就返回 None —— 不发半截文章。"""
    ns = _fit_budget(ns)
    if len(ns) < config.MIN_GROUP:
        return None
    return Group(tag=tag, notes=ns, source_hash=_hash(ns), slug=_slugify(tag))


def build_groups(notes):
    """先按三级标签分组；不足 MIN_GROUP 的碎组按二级标签重新归并。

    没有回退的话，实测 224 篇可发布笔记里有 91 篇（41%）会卡在
    只有一两篇的三级标签里，永远发不出去。
    """
    buckets = {}
    for n in publishable(notes):
        t = _primary_tag(n)
        if t:
            buckets.setdefault(t, []).append(n)

    # 三级及以上的碎组降到「恰好二级」重新归并。二级碎组直接丢弃——
    # 再降就成了「02分子表征」这种把整个领域当一篇文章的荒唐结果。
    # 用同一个 dict 归并，回退目标撞上已存在的组时自动合并而非产生重名组。
    merged = {}
    for tag, ns in buckets.items():
        parts = tag.split('/')
        if len(ns) < config.MIN_GROUP and len(parts) >= 3:
            tag = '/'.join(parts[:2])
        merged.setdefault(tag, []).extend(ns)

    made = (_make(t, ns) for t, ns in merged.items() if len(ns) >= config.MIN_GROUP)
    return sorted((g for g in made if g), key=lambda g: (-len(g.notes), g.tag))


def pick_next(groups, published):
    """取第一个未发布、或源笔记已变更的组。"""
    for g in groups:
        rec = published.get(g.tag)
        if rec is None or rec.get('source_hash') != g.source_hash:
            return g
    return None
