"""Obsidian 笔记解析。只负责把 md 变成结构化对象，不做任何业务判断。

哪些笔记该发布是 select_ 的职责，这里一视同仁全解析出来。
"""
import re
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

import yaml

import config

FM_RE = re.compile(r'^---\n(.*?)\n---\n?', re.S)
IMG_MD = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
IMG_WIKI = re.compile(r'!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]')
WIKILINK = re.compile(r'(?<!!)\[\[([^\]|]+)(?:\|([^\]]*))?\]\]')

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp',
              '.svg', '.tif', '.tiff'}
# ![[...]] 里出现、但发不成图片的附件后缀。列出来是为了跟「笔记嵌入」
# 区分开：前者删掉，后者退化成双链。
ATTACH_EXTS = {'.excalidraw', '.canvas', '.pdf', '.docx', '.xlsx', '.pptx',
               '.mp3', '.mp4', '.mov', '.wav', '.zip'}


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


def image_ref_name(raw):
    """图片引用 → 文件名；不是图片（或是外链）返回 None。

    解析、正文改写、本地拷贝三处都要同一套规则，所以收在一个函数里。
    两个坑各修一次就够：

    反斜杠必须显式换成斜杠。vault 里有 Windows 时期留下的
    `../../image&attachment/image\202112141122601.png`，POSIX 的 Path
    不把 \ 当分隔符，basename 会带着目录名一起取出来，Drive 上永远查
    不到 —— 实测因此把一张真实存在的图判成了缺失。

    没有图片后缀的一律返回 None。![[笔记#小节]] 是笔记嵌入，跟图片嵌入
    同语法，不排掉就会被当成「找不到的图」写进正文（实测 PTM.md 里有
    一处），还会连累校验器误报丢图。
    """
    p = urllib.parse.unquote(raw.split('|')[0].strip())
    if p.startswith('http'):
        return None
    name = PurePosixPath(p.replace('\\', '/')).name
    return name if PurePosixPath(name).suffix.lower() in IMAGE_EXTS else None


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
            name = image_ref_name(raw)
            if name:
                images.append(name)

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
