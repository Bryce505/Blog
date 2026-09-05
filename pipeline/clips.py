"""把 Bryce505/Notes 的月度剪藏索引解析成站点用的 JSON。

用法: python pipeline/clips.py --notes <Notes 仓库路径> --out src/data/clips.json

上游格式的唯一真相是 Notes 仓库的 `src/clipper/md_writer.py::render_entry` ——
那是机器生成的固定格式，所以这里用严格正则匹配而不是宽松扫描：匹配不上意味着
上游改了格式，那时候要的是 workflow 红一条，不是站上悄悄少几条内容。

本模块与 main.py 的五步流程完全无关，也不经过 verify.py —— 剪藏不是 AI 改写
本仓库笔记的产物，没有「把某个流速改错」那个风险面，校验器的两组检查在这里
不适用。
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
from pathlib import Path

# 快照留在 Notes 仓库，本站只链过去：公众号正文是别人的版权内容，转载到公网
# 站点有风险；且上游 archive/ 一个月就几百 KB，镜像进来会持续撑大本仓库。
#
# 指 raw 而不是 github.com/<repo>/blob/：blob 路由吃不下路径里的 %25。实测一篇
# 标题带百分号的文章（《…Token消耗降60%、提速50%》），文件名里那个字面的 %
# 编码出来就是 %25，blob 一律返回 400 —— 连 GitHub 自己 contents API 给出的
# html_url 都 400，不是编码编错了，是那条路由的限制，绕不过去。raw 对同一批
# 68 条全部 200。代价是纯文本不渲染 markdown，但一个打得开的链接胜过一个更好
# 看却会 400 的链接。
SNAPSHOT_BASE = 'https://raw.githubusercontent.com/Bryce505/Notes/master/'

# 上游 ai.py 已经把优先级兜底成这三个值之一（`if priority not in (...)` → 中），
# 所以出现第四种值只可能意味着格式变了
PRIORITIES = ('高', '中', '低')

_HEADING = re.compile(r'(?m)^## (.+)$')
_CLIPPED = re.compile(r'^- \*\*剪藏\*\*：(.+?) ｜ \*\*发布\*\*：(.+)$')
_PRIORITY = re.compile(r'^- \*\*优先级\*\*：(.+?) ｜ \*\*状态\*\*：(.+)$')
_KEYWORDS = re.compile(r'^- \*\*关键词\*\*：(.+)$')
_SUMMARY = re.compile(r'^- \*\*摘要\*\*：(.+)$')
_VERDICT = re.compile(r'^- \*\*是否值得读\*\*：(.+)$')
_LINK = re.compile(r'^- \*\*链接\*\*：\[原文\]\((\S+?)\)(?: ｜ \[全文快照\]\((\S+?)\))?$')
_INSIGHT = re.compile(r'^  - (.+)$')


def parse_month(text: str, source: str, month: str, notes_path: str) -> list[dict]:
    """把一份月度索引解析成条目列表。

    `notes_path` 是这份索引在 Notes 仓库里的相对路径（如 `notes/x/2026-08.md`），
    既用来还原快照的相对链接，也用来让报错指得出是哪份文件。
    """
    parts = _HEADING.split(text)
    # split 的结果是 [标题前的内容, 标题1, 正文1, 标题2, 正文2, ...]
    entries = [_parse_entry(title, body, source, month, notes_path)
               for title, body in zip(parts[1::2], parts[2::2])]
    if not entries:
        raise ValueError(
            f'{notes_path} 一条剪藏都没解析出来 —— 上游多半改了条目标题的层级。'
            '别把这里改成静默返回空列表：逐条检查一条都不会触发，'
            '站上会变成一个没人会发现的空栏目。')
    return entries


def collect(notes_dir: Path) -> list[dict]:
    """扫上游的 notes/ 与 notes/x/，合并后按剪藏时间倒序。"""
    clips: list[dict] = []
    for source, sub in (('weixin', ''), ('x', 'x')):
        directory = notes_dir / 'notes' / sub
        for path in sorted(directory.glob('*.md')):
            clips += parse_month(path.read_text(encoding='utf-8'), source,
                                 path.stem, posixpath.join('notes', sub, path.name))
    if not clips:
        raise ValueError(
            f'{notes_dir} 下的 notes/ 一个月度索引都没找到 —— 上游挪了目录。'
            '宁可红一条，也不要产出一个空 JSON 把整栏抹掉。')
    # 'YYYY-MM-DD HH:MM' 定宽，字典序就是时间序，不必解析成 datetime
    clips.sort(key=lambda c: c['clippedAt'], reverse=True)
    return clips


def _parse_entry(title: str, body: str, source: str, month: str,
                 notes_path: str) -> dict:
    entry = {
        'source': source, 'month': month, 'title': title.strip(),
        'clippedAt': '', 'publishedAt': '', 'priority': '', 'keywords': [],
        'summary': '', 'insights': [], 'verdict': '', 'url': '', 'snapshot': '',
    }
    lines = body.split('\n')
    for i, line in enumerate(lines):
        if m := _CLIPPED.match(line):
            entry['clippedAt'] = m.group(1).strip()
            published = m.group(2).strip()
            # 上游抓不到发布时间时写「未知」，落到站上就是不显示这一项
            entry['publishedAt'] = '' if published == '未知' else published
        elif m := _PRIORITY.match(line):
            entry['priority'] = m.group(1).strip()
        elif m := _KEYWORDS.match(line):
            entry['keywords'] = _split_keywords(m.group(1).strip())
        elif m := _SUMMARY.match(line):
            entry['summary'] = m.group(1).strip()
        elif m := _VERDICT.match(line):
            entry['verdict'] = m.group(1).strip()
        elif m := _LINK.match(line):
            entry['url'] = m.group(1)
            if m.group(2):
                entry['snapshot'] = _snapshot_url(m.group(2), notes_path)
        elif line.startswith('- **洞见**'):
            entry['insights'] = _take_insights(lines[i + 1:])
    _require(entry, notes_path)
    return entry


def _split_keywords(raw: str) -> list[str]:
    """按 ' / ' 切，不按 '/' 切。

    真实语料里有 `LC-MS/MS`、`敲除/敲低` 这类自带斜杠的词，按裸斜杠切会把一个
    词劈成两个假关键词。上游 md_writer 用的正是 ' / '.join()。
    """
    if raw == '无':          # 上游对「没有关键词」的写法
        return []
    return [k.strip() for k in raw.split(' / ') if k.strip()]


def _take_insights(rest: list[str]) -> list[str]:
    """「- **洞见**：」之后连续的缩进列表项，遇到第一个不匹配的行就停。"""
    out = []
    for line in rest:
        m = _INSIGHT.match(line)
        if not m:
            break
        out.append(m.group(1).strip())
    return out


def _snapshot_url(relative: str, notes_path: str) -> str:
    """相对索引文件的路径 → Notes 仓库的快照 URL。

    上游写的是相对路径（公众号 `../archive/…`；X 的索引在 notes/x/ 下，要多退
    一层 `../../archive/x/…`），且中文已经 percent-encode 过。这里只做路径拼接，
    绝不再编码一次 —— 二次编码会把 %E4%B8%87 变成 %25E4%25B8%2587，链接直接
    打不开。
    """
    path = posixpath.normpath(
        posixpath.join(posixpath.dirname(notes_path), relative))
    return SNAPSHOT_BASE + path


def _require(entry: dict, notes_path: str) -> None:
    """必填字段的界线是「缺了这一条，这张卡片还成不成立」。"""
    name = entry['title'] or '无标题'
    for field in ('title', 'clippedAt', 'url'):
        # 标题与链接缺了是一张点不开的无名卡片；剪藏时间缺了排不进时间流
        if not entry[field]:
            raise ValueError(f'{notes_path} 的《{name}》缺 {field}，上游格式变了')
    # 档外的优先级会让这条卡片被页面上每一个筛选条件都藏起来，等于内容凭空消失
    if entry['priority'] not in PRIORITIES:
        raise ValueError(
            f'{notes_path} 的《{name}》优先级是 {entry["priority"]!r}，'
            f'不在 {PRIORITIES} 里 —— 上游格式变了')


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description='把 Notes 的月度剪藏索引解析成站点 JSON')
    ap.add_argument('--notes', required=True, help='Notes 仓库的 checkout 路径')
    ap.add_argument('--out', required=True, help='输出 JSON 路径')
    args = ap.parse_args(argv)

    clips = collect(Path(args.notes))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    # ensure_ascii=False：中文不转义，diff 才看得出上游改了什么
    out.write_text(json.dumps(clips, ensure_ascii=False, indent=2) + '\n',
                   encoding='utf-8')
    print(f'{len(clips)} 条剪藏 → {out}')


if __name__ == '__main__':
    main()
