"""Obsidian 语法 → 站点 markdown 的转换。

只处理需要流水线状态才能做的两件事（双链要知道哪些已发布、图片要知道
实际落盘路径）。callout 转换不在这里 —— 那是纯格式变换，交给 Astro
的 remark 插件一次性处理全站，不必逐篇跑。
"""
import re
import urllib.parse
from pathlib import Path

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


def _one(name, alt, image_map, missing, caption_of):
    if name in missing or name not in image_map:
        # 不留破图：换成一行说明，读者知道这里本该有图
        return f'*[图缺失：{name}]*'
    md = f'![{alt}]({image_map[name]})'
    cap = caption_of.get(name, '')
    return f'{md}\n*{cap}*' if cap else md


def _basename(raw):
    return Path(urllib.parse.unquote(raw.split('|')[0].strip())).name


def rewrite_images(text, image_map, missing, caption_of):
    """两种 Obsidian 图片写法统一重写成站内 WebP 路径，并追加图注。"""
    def sub_md(m):
        alt, raw = m.group(1), m.group(2)
        if raw.startswith('http'):
            return m.group(0)
        return _one(_basename(raw), alt, image_map, missing, caption_of)

    def sub_wiki(m):
        return _one(_basename(m.group(1)), '', image_map, missing, caption_of)

    return _outside_code(text, lambda seg: IMG_WIKI.sub(sub_wiki, IMG_MD.sub(sub_md, seg)))
