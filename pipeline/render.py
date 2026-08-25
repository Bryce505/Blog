"""Obsidian 语法 → 站点 markdown 的转换。

只处理需要流水线状态才能做的两件事（双链要知道哪些已发布、图片要知道
实际落盘路径）。callout 转换不在这里 —— 那是纯格式变换，交给 Astro
的 remark 插件一次性处理全站，不必逐篇跑。
"""
import re
from pathlib import PurePosixPath

import vault

# 前面的 (?<!!) 很关键：![[...]] 是图片嵌入，不是双链
WIKILINK = re.compile(r'(?<!!)\[\[([^\]|]+)(?:\|([^\]]*))?\]\]')
IMG_MD = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
IMG_WIKI = re.compile(r'!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]')

# 代码块（含围栏与行内）必须整段跳过：Python 的嵌套列表 [['a','b']] 会被
# 双链正则匹配上，改写后代码就坏了（实测全库 10 处）。Obsidian 自己在
# 代码块里也不渲染双链，跳过才是正确语义。
CODE_SEG = re.compile(r'(```.*?```|~~~.*?~~~|`[^`\n]+`)', re.S)


def _outside_code(text, fn):
    """只对代码块之外的片段应用 fn。re.split 保留分组，奇数下标即代码段。"""
    parts = CODE_SEG.split(text)
    return ''.join(p if i % 2 else fn(p) for i, p in enumerate(parts))


def resolve_wikilinks(text, title_to_slug):
    """已发布转文章级站内链接；未发布退化成纯文本，不留死链。

    不做章节级锚点：采用结构重组后，源笔记不再对应输出文章里的独立
    章节，锚点无从推导。
    """
    def sub(m):
        target, alias = m.group(1).strip(), m.group(2)
        label = (alias or target).strip()
        slug = title_to_slug.get(target)
        return f'[{label}](/posts/{slug})' if slug else label
    return _outside_code(text, lambda seg: WIKILINK.sub(sub, seg))


def caption_for(note):
    """图注按 book → paper → link 优先级取，全空则不加图注。"""
    for val, tpl in ((note.book, '图源：《{}》'),
                     (note.paper, '图源：{}'),
                     (note.link, '图源：{}')):
        if val:
            return tpl.format(val)
    return ''


# 取不到的图留一行占位，文件名藏在 HTML 注释里：读者看不到一串
# 时间戳文件名，repair 通道又能凭它把图补回来（图注一并带着，补图时
# 不必回头翻源笔记）。
MISSING_TPL = '*[图片暂缺]*<!--missing-image: {name}|{caption}-->'
MISSING_RE = re.compile(r'\*\[图片暂缺\]\*<!--missing-image:\s*(.+?)\|(.*?)-->')


def _alt(raw):
    """清理 alt。

    Obsidian 用 `![alt|330](x)` 表示显示宽度，管道符必须去掉 —— 它会把
    GFM 表格行劈成两个单元格，实测肽图那篇的 `![|330]` 就是这么把一张图
    变成两格乱码的。Zotero 导出的 alt 里塞着整段 <img> HTML，同样丢掉。
    """
    alt = raw.split('|')[0]
    return '' if '<' in alt else alt.strip()


def _one(name, alt, image_map, missing, caption_of):
    if name in missing or name not in image_map:
        # 不留破图：换成一行说明，读者知道这里本该有图
        return MISSING_TPL.format(name=name, caption=caption_of.get(name, ''))
    md = f'![{_alt(alt)}]({image_map[name]})'
    cap = caption_of.get(name, '')
    return f'{md}\n*{cap}*' if cap else md


def rewrite_images(text, image_map, missing, caption_of):
    """两种 Obsidian 图片写法统一重写成站内 WebP 路径，并追加图注。"""
    def sub_md(m):
        alt, raw = m.group(1), m.group(2)
        if raw.startswith('http'):
            return m.group(0)
        name = vault.image_ref_name(raw)
        # 图片语法里塞的不是图片（vault 里有 .pdf、Zotero 导出的附件），
        # 站上放不出来，删掉比留个死链好
        return _one(name, alt, image_map, missing, caption_of) if name else ''

    def sub_wiki(m):
        target = m.group(1)
        name = vault.image_ref_name(target)
        if name:
            return _one(name, '', image_map, missing, caption_of)
        # ![[笔记#小节]] 是笔记嵌入不是图片，退化成双链，由 resolve_wikilinks
        # 决定链过去还是转纯文本；附件（.excalidraw 等）发不出去，删掉。
        stem = target.split('#')[0].strip()
        return '' if PurePosixPath(stem).suffix.lower() in vault.ATTACH_EXTS \
            else f'[[{stem}]]'

    return _outside_code(text, lambda seg: IMG_WIKI.sub(sub_wiki, IMG_MD.sub(sub_md, seg)))


def missing_marks(text):
    """文章里所有占位标记 → [(文件名, 图注)]。"""
    return [(m.group(1).strip(), m.group(2).strip())
            for m in MISSING_RE.finditer(text)]


def restore_missing(text, image_map):
    """占位标记换回图片。image_map 里没有的原样留着，下次再补。

    alt 在占位时就丢了（正文里几乎全是空 alt），补回来的图不带 alt。
    """
    def sub(m):
        name, cap = m.group(1).strip(), m.group(2).strip()
        if name not in image_map:
            return m.group(0)
        md = f'![]({image_map[name]})'
        return f'{md}\n*{cap}*' if cap else md
    return MISSING_RE.sub(sub, text)
