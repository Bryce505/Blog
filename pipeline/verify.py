"""机械校验器：LLM 输出的确定性安全阀。

这是整套流水线里最关键的代码。内容是生物医药 CMC / 分析方法，AI 把
某个流速、某条法规编号改错了，是专业性错误而不是排版问题。校验拦不住
篡改，这条流水线就不该上线。

两组检查：

- `verify()`：数据保真。源文的数值、法规条款号、文献引用、图片引用有没有
  被改动或丢失。自动通道与引子通道都跑这一组。
- `review()`：可发表性。结构、格式、选材重复、关联文章链接、扩展内容的
  来源核验（转交 evidence.py）。引子通道跑这一组。

任一项不过，文章进 _review/ 等人工放行，并记日志、发通知。
"""
import re
import urllib.parse
from dataclasses import dataclass, field

import config
import evidence

# 只抓「承载数据」的数字：带单位、含小数点、或三位以上整数。
#
# 裸露的一两位整数（"本文分为 3 个部分"）刻意不查 —— AI 写导读和过渡句
# 必然产生这类数字，把它们纳入检查等于让校验器天天误报，最后只能被关掉。
#
# 单位必须是真实单位白名单，不能用「任意 1-6 个字母」：后者会把
# "1The"、"12Figure"、"15piston" 这种「数字紧跟单词」当成数值+单位，
# 段落一重排碎片就变，实测 33 个真实组里误报 14 组。
_UNITS = sorted([
    '%', '‰', '°C', '℃',
    'kDa', 'Da', 'mol', 'mmol', 'μmol', 'µmol', 'umol', 'nmol', 'pmol',
    'mL', 'ml', 'μL', 'µL', 'uL', 'ul', 'L', 'l',
    'mg', 'μg', 'µg', 'ug', 'ng', 'pg', 'kg', 'g',
    'mM', 'μM', 'µM', 'uM', 'nM', 'pM', 'M',
    'nm', 'μm', 'µm', 'um', 'mm', 'cm', 'm', 'Å',
    'min', 'h', 'hr', 's', 'ms', 'sec',
    'Hz', 'kHz', 'MHz', 'ppm', 'ppb', 'rpm', 'psi', 'bar', 'Pa', 'kPa', 'MPa',
    'V', 'kV', 'mV', 'mA', 'μA', 'AU', 'mAU', 'cP', 'xg', 'rcf', 'eV',
    # 刻意不收裸 'A'（安培）和裸 'l'（升）：会把 HPLC 的「流动相 A」匹配成
    # 「36A」这类假数值。这两个单位在本领域用 mA/kV、mL/μL 表达，不损失覆盖。
], key=len, reverse=True)

# 边界用 [0-9A-Za-z_.] 而不是 \w：Python 的 \w 把汉字也算词字符，于是
# 「至1.8倍」「流速0.05 mL/min」这种紧挨中文的数字一个都提取不到。中文
# 正文里这种写法占多数，后果是校验器对源文视而不见，模型重排时顺手加个
# 空格，同一个数就成了「源文没有的数据」——实测那篇 HPLC 被拦下的 10 个
# 数里 9 个原文就有，白拦一次还白烧一次 token。
DATA_NUM = re.compile(
    r'(?<![0-9A-Za-z_.])(?:'
    r'\d+\.\d+'                                    # 小数
    r'|\d{3,}(?![0-9A-Za-z_])'                       # 三位以上整数
    r'|\d+(?:\.\d+)?\s*(?:' + '|'.join(re.escape(u) for u in _UNITS) + r')(?![A-Za-z])'
    r')')

# DOI 用否定字符类而非 \S+：\S+ 会把 markdown 链接语法、右括号、中文
# 全角括号一起吞进来，同一个 DOI 因上下文不同提取出不同字符串。
# 法规条款号与文献 DOI 分开处理，严格程度不同：
#   法规条款号是规范性依据，丢一个就是合规主张变了 —— 零容忍。
#   文献 DOI 是参考性的，结构重组合并重复论述时被一并折叠掉是正常的，
#   要求 100% 保留等于禁止重组。只在大批量丢失时才判失败。
REGULATION = re.compile(
    r'ICH\s*[QSEM]\d[A-Z]?(?:\(R\d\))?'
    r'|21\s*CFR\s*\d+(?:\.\d+)?'
    r'|USP\s*<\d+>'
    r'|Ph\.\s*Eur\.\s*\d[\d.]*',
    re.I)

DOI = re.compile(r'10\.\d{4,9}/[^\s\]\)）,;、。]+')

MAX_DOI_LOSS = 0.3
# 比例阈值要配绝对下限，否则小分母失真：只有 3 个 DOI 时丢 1 个就是 33%，
# 而丢一条文献引用在结构重组里完全正常。
MIN_DOI_LOSS_ALLOWED = 1


def _norm(t):
    # DOI 常以句点结尾，归一化时去掉，避免 'x.' 与 'x' 被当成两个引用
    return re.sub(r'\s+', '', t).lower().rstrip('.')


def data_numbers(text):
    return {_norm(m.group()) for m in DATA_NUM.finditer(text)}


def regulations(text):
    return {_norm(m.group()) for m in REGULATION.finditer(text)}


def dois(text):
    return {_norm(m.group()) for m in DOI.finditer(text)}


def citations(text):
    """法规 + DOI 的并集。供报告展示用，判定走 regulations/dois 各自的规则。"""
    return regulations(text) | dois(text)


@dataclass
class VerifyResult:
    ok: bool
    failures: list = field(default_factory=list)


def verify(src, out, images, min_ratio=None):
    """四项确定性检查。任一不过则不发布。

    先整体 URL 解码再比对：Obsidian 粘贴的图片名带空格，正文里是
    「Pasted%20image%2020240528.png」。不解码有两处会出错 ——
    图片 basename 对不上（误判丢图），且 %2020240528 会被数字校验
    读成 2020240528，凭空多出一个源文没有的「数据」。
    """
    if min_ratio is None:
        min_ratio = config.MIN_LENGTH_RATIO
    src = urllib.parse.unquote(src)
    out = urllib.parse.unquote(out)
    failures = []

    missing = [i for i in images if i not in out]
    if missing:
        failures.append(f'丢图: {missing}')

    # 只查「新增」不查「减少」：重组时删掉重复论述是正常的，
    # 凭空冒出源文没有的数据才是危险信号。
    new_nums = data_numbers(out) - data_numbers(src)
    if new_nums:
        failures.append(f'出现源文没有的数据: {sorted(new_nums)[:10]}')

    lost_reg = regulations(src) - regulations(out)
    if lost_reg:
        failures.append(f'丢失法规条款: {sorted(lost_reg)[:10]}')

    src_doi = dois(src)
    lost_doi = src_doi - dois(out)
    allowed = max(MIN_DOI_LOSS_ALLOWED, int(len(src_doi) * MAX_DOI_LOSS))
    if len(lost_doi) > allowed:
        failures.append(
            f'丢失文献引用过多: {len(lost_doi)}/{len(src_doi)}，'
            f'允许至多 {allowed} 条 {sorted(lost_doi)[:5]}')

    src_len = len(re.sub(r'\s', '', src))
    out_len = len(re.sub(r'\s', '', out))
    if src_len and out_len < src_len * min_ratio:
        failures.append(f'正文过短: {out_len}/{src_len}={out_len / src_len:.0%} < {min_ratio:.0%}')

    return VerifyResult(ok=not failures, failures=failures)


# ---------- review：可发表性检查 ----------

ARTICLE_H1 = re.compile(r'^#\s+\S', re.M)
ARTICLE_H2 = re.compile(r'^##\s+(.+?)\s*$', re.M)
SELF_NUMBERED = re.compile(r'^#{2,3}\s*(?:\d+[.、]|[一二三四五六七八九十]+[、.])', re.M)
# 指向知识库内部 md 的相对链接：发到站上是死链
VAULT_MD_LINK = re.compile(r'\[[^\]]*\]\((?!https?://|/)[^)]*\.md(?:#[^)]*)?\)')
LEFTOVER_WIKILINK = re.compile(r'(?<!!)\[\[[^\]]+\]\]')
MISSING_IMAGE = re.compile(r'\*\[图片暂缺\]\*')
EVIDENCE_HEAD = re.compile(r'^##\s*依据与出处\s*$', re.M)
RELATED_HEAD = re.compile(r'^##\s*相关阅读\s*$', re.M)

MIN_SECTIONS, MAX_SECTIONS = 3, 10
MIN_SECTION_CHARS = 120      # 低于此的是空壳章节，不是章节
MIN_LEAD_CHARS = 40          # 导读段
# 减法模式的篇幅区间：缩到一半以下说明删掉了不该删的，几乎没缩说明没做减法
SHRINK_RANGE = (0.55, 0.95)
# 加法模式：一点没长说明没做加法；翻三倍以上是过度扩展。
# 但比例上限要配一个绝对下限：实测一篇 201 字符的短稿，3 倍上限只有
# 600 字符，根本成不了文章 —— 比例是用来拦「跑飞」的，不是用来惩罚
# 「引子短」的。取两者较大值。
GROW_RANGE = (1.05, 3.0)
MIN_ARTICLE_CHARS = 4_000


def _sections(article):
    """[(标题, 该节正文去空白后的字数)]，按 H2 切。"""
    heads = list(ARTICLE_H2.finditer(article))
    out = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(article)
        body = article[m.end():end]
        out.append((m.group(1).strip(), len(re.sub(r'\s', '', body))))
    return out


def structure(article):
    """结构性检查：章节数、空壳章节、自带序号、导读。"""
    fails = []
    secs = [(t, n) for t, n in _sections(article)
            if not t.startswith(('依据与出处', '相关阅读'))]
    if not MIN_SECTIONS <= len(secs) <= MAX_SECTIONS:
        fails.append(f'二级章节 {len(secs)} 个，应在 {MIN_SECTIONS}～{MAX_SECTIONS} 之间')
    thin = [t for t, n in secs if n < MIN_SECTION_CHARS]
    if thin:
        fails.append(f'空壳章节（正文不足 {MIN_SECTION_CHARS} 字）: {thin[:5]}')
    if SELF_NUMBERED.search(article):
        fails.append('章节标题自带序号，站点会再编一次号，出现「1. 1. 概述」')
    if ARTICLE_H1.search(article):
        fails.append('正文里出现一级标题，文章标题应由 frontmatter 承载')
    first = ARTICLE_H2.search(article)
    lead = article[:first.start()] if first else article
    if len(re.sub(r'\s', '', lead)) < MIN_LEAD_CHARS:
        fails.append('缺少导读段：第一个二级标题之前应有两三句话交代脉络')
    return fails


def formatting(article):
    """格式检查：死链、残留语法、缺图。"""
    fails = []
    dead = VAULT_MD_LINK.findall(article)
    if dead:
        fails.append(f'正文有指向知识库内部 md 的相对链接（站上是死链）{len(dead)} 处: {dead[:3]}')
    left = LEFTOVER_WIKILINK.findall(article)
    if left:
        fails.append(f'残留未解析的双链 {len(left)} 处: {left[:3]}')
    gone = MISSING_IMAGE.findall(article)
    if gone:
        fails.append(f'{len(gone)} 张图没取到，正文里留着「图片暂缺」占位')
    return fails


def proportion(mode, seed_chars, article_chars):
    """加减法是否按原则执行 —— 用篇幅比例做确定性判定。"""
    if not seed_chars:
        return []
    ratio = article_chars / seed_chars
    lo, hi = SHRINK_RANGE if mode == 'shrink' else GROW_RANGE
    cap = max(seed_chars * hi, MIN_ARTICLE_CHARS) if mode == 'grow' else seed_chars * hi
    if article_chars < seed_chars * lo or article_chars > cap:
        word = '减法' if mode == 'shrink' else '加法'
        return [f'{word}模式下篇幅 {article_chars:,} 字符（原文 {seed_chars:,}，'
                f'比例 {ratio:.0%}）超出 {seed_chars * lo:,.0f}～{cap:,.0f} 字符的区间']
    return []


def selection(seed_path, used_seeds):
    """选材重复：这篇引子笔记是不是已经用过。"""
    return ([f'选材重复：{seed_path} 已经用过'] if seed_path in set(used_seeds) else [])


def related(article, related_slugs):
    """有关联的已发布文章必须都在正文里有链接。"""
    missing = [s for s in related_slugs if f'/posts/{s}' not in article]
    return ([f'关联文章缺链接: {missing}'] if missing else [])


def review(article, *, mode=None, seed_chars=0, seed_path=None, used_seeds=(),
           related_slugs=(), note_bodies=None, source_text=''):
    """可发表性检查。返回 VerifyResult。"""
    fails = structure(article) + formatting(article)
    if mode:
        fails += proportion(mode, seed_chars, len(article))
    if seed_path:
        fails += selection(seed_path, used_seeds)
    fails += related(article, related_slugs)
    if mode == 'grow':
        ev_fails, n = evidence.check(article, note_bodies or {}, source_text)
        fails += ev_fails
        if n == 0:
            fails.append('加法模式却没有「依据与出处」一节：扩展内容必须标注来源')
    return VerifyResult(ok=not fails, failures=fails)
