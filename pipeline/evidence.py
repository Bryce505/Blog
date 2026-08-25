"""解析并核验文章里的「依据与出处」标注。

引子通道允许模型补内容，风险是它顺手编一个出处。「有没有幻觉」本身
没法用正则判定，所以把问题换个形式：**强制模型为每处扩展写出可核验的
来源**，再由机器逐条回原文核对。编造的出处会在三个地方露馅 ——
路径在知识库里不存在、引用要点在那篇笔记里找不到、DOI 没在输入里出现过。

引用要点用二元组重合度核对而不是全句匹配：模型转述是正常的，逐字比对
会把所有正常转述都判成幻觉。中文没有空格分词，字符二元组是不引入分词
依赖的最省事代理。
"""
import re

MARKER = re.compile(r'\[依据\s*(\d+)\]')
SECTION = re.compile(r'^##\s*依据与出处\s*$', re.M)
NOTE_ENTRY = re.compile(
    r'^\s*(\d+)[.、]\s*笔记：\s*`([^`]+)`\s*[—\-–]+\s*引用要点：\s*(.+?)\s*$', re.M)
DOI_ENTRY = re.compile(
    r'^\s*(\d+)[.、]\s*文献：\s*DOI:\s*(\S+?)\s*[—\-–]+\s*引用要点：\s*(.+?)\s*$', re.M)
DOI_SHAPE = re.compile(r'^10\.\d{4,9}/\S+$')

# 二元组重合度低于此判定为「原文找不到这个说法」。定在 0.5 是刻意宽松的：
# 宁可放过一条转述得面目全非的真依据，也不要把正常转述判成幻觉 —— 这个
# 检查的目标是拦住整条编造，不是做文本相似度评分。
MIN_OVERLAP = 0.5

CJK = re.compile(r'[一-鿿]+')
WORD = re.compile(r'[A-Za-z][A-Za-z0-9\-]{2,}')


def _tokens(text):
    """中文取字符二元组，英文取词。都归一化到小写。"""
    toks = {w.lower() for w in WORD.findall(text)}
    for run in CJK.findall(text):
        toks |= {run[i:i + 2] for i in range(len(run) - 1)}
    return toks


def supported(claim, source_text):
    """引用要点的词元有多大比例能在来源里找到。"""
    toks = _tokens(claim)
    if not toks:
        return 0.0
    hit = sum(1 for t in toks if t in source_text.lower())
    return hit / len(toks)


def parse(article):
    """返回 (正文里出现的编号集合, {编号: 条目})。"""
    m = SECTION.search(article)
    body, tail = (article[:m.start()], article[m.start():]) if m else (article, '')
    used = {int(x) for x in MARKER.findall(body)}
    entries = {}
    for num, path, claim in NOTE_ENTRY.findall(tail):
        entries[int(num)] = {'kind': 'note', 'ref': path.strip(), 'claim': claim.strip()}
    for num, doi, claim in DOI_ENTRY.findall(tail):
        entries[int(num)] = {'kind': 'doi', 'ref': doi.strip().rstrip('.'), 'claim': claim.strip()}
    return used, entries


def check(article, note_bodies, source_text):
    """核验标注。note_bodies 是 {笔记路径: 正文}，source_text 是喂给模型的全部输入。

    返回 (失败信息列表, 条目数)。
    """
    used, entries = parse(article)
    fails = []

    orphan = sorted(used - set(entries))
    if orphan:
        fails.append(f'正文引用了不存在的依据编号: {orphan}')
    unused = sorted(set(entries) - used)
    if unused:
        fails.append(f'依据列表里有正文没引用的条目: {unused}')

    for num in sorted(entries):
        e = entries[num]
        if e['kind'] == 'note':
            body = note_bodies.get(e['ref'])
            if body is None:
                fails.append(f'依据 {num} 的笔记路径在知识库里不存在: {e["ref"]}')
                continue
            ratio = supported(e['claim'], body)
            if ratio < MIN_OVERLAP:
                fails.append(f'依据 {num} 的引用要点在该笔记里找不到依据'
                             f'（重合度 {ratio:.0%}）: {e["claim"][:40]}')
        else:
            if not DOI_SHAPE.match(e['ref']):
                fails.append(f'依据 {num} 的 DOI 格式不合法: {e["ref"]}')
            elif e['ref'].lower() not in source_text.lower():
                fails.append(f'依据 {num} 的 DOI 没在输入材料里出现过，疑似编造: {e["ref"]}')
    return fails, len(entries)


def crossref_alive(doi, timeout=8, _get=None):
    """联网确认 DOI 真实存在。取不到网络时返回 None（未知），不判失败。"""
    import requests
    get = _get or requests.get
    try:
        r = get(f'https://api.crossref.org/works/{doi}', timeout=timeout,
                headers={'User-Agent': 'technicalblog/1.0 (mailto:makejun505@gmail.com)'})
    except Exception:
        return None
    if r.status_code == 404:
        return False
    if r.status_code != 200:
        return None
    return True
