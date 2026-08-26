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

    体量上限不是性能优化，是内容判定：实测超过 3 万字符的笔记绝大多数是
    整书/整章转录（如整本《Capillary Electrophoresis Methods for
    Pharmaceutical Analysis》，142 万字符），既撑上下文又有版权问题。
    作者自己写的长文走 SIZE_EXEMPT_NOTES 名单放行。
    """
    return [n for n in notes
            if n.type in config.PUBLISHABLE_TYPES
            and n.tags
            and (len(n.body) <= config.MAX_NOTE_CHARS
                 or n.path in config.SIZE_EXEMPT_NOTES)]


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
    """按每篇笔记自身最深的标签层级分组（最多三级），碎组不向上归并。

    向上归并是「一篇文章什么都讲」的根源：实测把三级碎组降到二级后，
    「05仪器与分析技术/质谱」一个组吃进 12 篇笔记，横跨定量、测序、
    碎裂、数据分析、离子源五个互不相干的子题，出来的文章只能是大杂烩。

    改成不归并 + 最小 2 篇之后（实测 209 篇可发布笔记）：
      归并版   30 组，覆盖 164 篇，最大组 12 篇，含上面那个大杂烩
      不归并版 38 组，覆盖 162 篇，最大组 14 篇，全部是同一子题
    覆盖面几乎没损失，组数反而多了 —— 归并并没有救回多少笔记，只是把
    本该分开的几篇焊死在一起。

    取「最深≤三级」而不是「必须三级」：只打了二级标签的笔记（如
    「00基础/生物制品」）本来就没有更细的粒度，强求三级等于把它们
    永久排除；而它们凑成的组是同级并列，不是几个子题硬拼。
    """
    buckets = {}
    for n in publishable(notes):
        t = _primary_tag(n)
        if not t:
            continue
        parts = t.split('/')
        buckets.setdefault('/'.join(parts[:3]), []).append(n)

    made = (_make(t, ns) for t, ns in buckets.items() if len(ns) >= config.MIN_GROUP)
    return sorted((g for g in made if g), key=lambda g: (-len(g.notes), g.tag))


def pick_next(groups, published, skip=()):
    """取第一个未发布、或源笔记已变更的组。

    published 按 slug 做 key，这里要按 tag 找，所以先翻一张 tag → 记录的表。

    没有 source_hash 的是回填记录（人工搬进 posts/ 的文章，拿不到 vault
    算不出哈希）—— 当作已发布，不重发。人工放行过的文章不该因为源笔记改了
    个错别字就被悄悄重写一遍。
    """
    by_tag = {r['tag']: r for r in published.values() if r.get('tag')}
    for g in groups:
        if g.tag in skip:
            continue
        rec = by_tag.get(g.tag)
        if rec is None or (rec.get('source_hash')
                           and rec['source_hash'] != g.source_hash):
            return g
    return None
