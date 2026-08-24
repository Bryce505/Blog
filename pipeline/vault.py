"""Obsidian 笔记解析。只负责把 md 变成结构化对象，不做任何业务判断。

哪些笔记该发布是 select_ 的职责，这里一视同仁全解析出来。
"""
import re
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path

import yaml

import config

FM_RE = re.compile(r'^---\n(.*?)\n---\n?', re.S)
IMG_MD = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
IMG_WIKI = re.compile(r'!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]')
WIKILINK = re.compile(r'(?<!!)\[\[([^\]|]+)(?:\|([^\]]*))?\]\]')


@dataclass
class Note:
    path: str
    title: str
    tags: list
    type: str
    description: str = ''
    book: str = ''
    paper: str = ''
    link: str = ''
    body: str = ''
    images: list = field(default_factory=list)
    wikilinks: list = field(default_factory=list)


def _flat(v):
    """frontmatter 字段可能是 None / 字符串 / 列表，统一成字符串。

    直接 str(None) 会得到 'None' 字符串，所以必须显式处理 None。
    """
    if v is None:
        return ''
    if isinstance(v, list):
        return ', '.join(str(x) for x in v if x)
    return str(v)


def parse_note(path: Path, vault_root: Path):
    """解析单个 md。frontmatter 缺失或 YAML 损坏返回 None，不抛异常——

    1600 篇笔记里总有几篇 YAML 写坏的，不能因为一篇烂掉整批。
    """
    text = path.read_text(encoding='utf-8', errors='ignore')
    m = FM_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    if not isinstance(fm, dict):
        return None

    body = text[m.end():]
    images = []
    for pat in (IMG_MD, IMG_WIKI):
        for raw in pat.findall(body):
            p = urllib.parse.unquote(raw.split('|')[0].strip())
            if not p.startswith('http'):
                images.append(Path(p).name)

    tags = fm.get('tags') or []
    if isinstance(tags, str):
        tags = [tags]

    return Note(
        path=str(path.relative_to(vault_root)).replace('\\', '/'),
        title=_flat(fm.get('title')) or path.stem,
        tags=[str(t) for t in tags if t],
        type=_flat(fm.get('type')).strip(),
        description=_flat(fm.get('description')),
        book=_flat(fm.get('book')),
        paper=_flat(fm.get('paper')),
        link=_flat(fm.get('link')),
        body=body,
        images=list(dict.fromkeys(images)),
        wikilinks=[t for t, _ in WIKILINK.findall(body)],
    )


def load_vault(vault_root: Path):
    """遍历 vault，跳过黑名单目录。"""
    notes = []
    for p in sorted(vault_root.rglob('*.md')):
        rel = p.relative_to(vault_root)
        if any(part in config.EXCLUDE_DIRS for part in rel.parts):
            continue
        n = parse_note(p, vault_root)
        if n:
            notes.append(n)
    return notes
