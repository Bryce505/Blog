"""机械校验器：LLM 输出的确定性安全阀。

这是整套流水线里最关键的代码。内容是生物医药 CMC / 分析方法，AI 把
某个流速、某条法规编号改错了，是专业性错误而不是排版问题。校验拦不住
篡改，这条流水线就不该上线。

两组检查：

- `verify()`：数据保真。源文的数值、法规条款号、文献引用、图片引用有没有
  被改动或丢失。自动通道与引子通道都跑这一组。
- `review()`：可发表性。结构、格式、选材重复、关联文章链接、扩展内容的
  来源核验（转交 evidence.py）。引子通道跑这一组。

任一项不过，文章照样落 posts/ 但带 `draft: true`（站点构建跳过），
并记日志、发通知，等人工放行。
"""
import re
import unicodedata
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
# 单位分支排在最前面：同一个量不能因为空格与否得到两个 token。
# 实测踩坑 —— 源笔记写「分析物＜4000Da」（粘连）提取成 4000da，而
# 「分子量 148000 Da」（带空格）走小数/整数分支提取成裸 148000，同类量两种
# 口径。结果模型把 4000Da 复述成「4000 道尔顿」就被判成编造数据（HPLC 那篇
# 实测复现）。绑定优先反而更严：以前「0.5 mL/min → 0.5 L/min」两边都提取成
# 裸 0.5，单位调包完全看不见，现在拦得住。
DATA_NUM = re.compile(
    r'(?<![0-9A-Za-z_.])(?:'
    r'\d+(?:\.\d+)?\s*(?:' + '|'.join(re.escape(u) for u in _UNITS) + r')(?![A-Za-z])'
    r'|\d+\.\d+'                                    # 小数
    r'|\d{3,}(?![0-9A-Za-z_])'                       # 三位以上整数
    r')')

# 这些载体里的数字不是实验数据，而且各自有更严的专属检查（图片走「丢图」、
# DOI 走丢失阈值）。重复计入只会制造误报：实测 209 篇笔记里，515 个不同
# token 来自链接 URL 与 DOI 串，其中大量是 202208091746201.png 这种截图
# 时间戳 —— 它们在源文和成稿里的写法必然不同（.png → .webp）。
# 替换成等长空格而不是删除，保证后面按位置取上下文时偏移不变。
IMG_EMBED = re.compile(r'!\[[^\]]*\]\([^)]*\)|!\[\[[^\]]*\]\]')
LINK_URL = re.compile(r'(?<=\])\([^)]*\)|<https?://[^>]*>|https?://\S+')

# 裸年份不是测量值。这条规则原意是拦「编造的流速、限度、回收率」，而实测
# 语料里 63 个不同裸年份 token 绝大多数来自参考文献串（Nature Protocols,
# 2007, 1, 2650–2660）；模型写「截至 2026 年」这类过渡句也必然产生年份，
# 把它当编造等于让校验器天天误杀。
BARE_YEAR = re.compile(r'^(?:19|20)\d\d$')
# 唯一例外：版本年份。《中国药典》2020年版 / ChP 2025年版 是规范性依据，
# 改错了是合规主张变了，必须继续拦。实测语料里 10 处全部带「年版」或「版」。
VERSION_YEAR = re.compile(r'\s*(?:年版|版|Edition|edition)')

# 纯数值（不带单位）
BARE_NUM = re.compile(r'^\d+(?:\.\d+)?$')


def _value(tok):
    """token 的数值部分，'4000da' → '4000'。"""
    m = re.match(r'\d+(?:\.\d+)?', tok)
    return m.group() if m else tok

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
    # 先做 NFKC：µ(U+00B5) 与 μ(U+03BC)、℃(U+2103) 与 °C 在语料里并存
    # （实测 127 vs 588、168 vs 198），那是字符编码差异不是数据差异，
    # 不归一化的话「37℃ → 37 °C」这种纯转写会被判成编造数据。
    # 只对提取出来的 token 做，不对全文做 —— 全文 NFKC 会把上标 10⁶ 压成
    # 106，凭空造出一个三位整数。
    t = unicodedata.normalize('NFKC', t)
    # DOI 常以句点结尾，归一化时去掉，避免 'x.' 与 'x' 被当成两个引用
    return re.sub(r'\s+', '', t).lower().rstrip('.')


def _blank(m):
    """替换成等长空格，保住后续按位置取上下文的偏移。"""
    return re.sub(r'\S', ' ', m.group())


def data_numbers(text):
    text = DOI.sub(_blank, LINK_URL.sub(_blank, IMG_EMBED.sub(_blank, text)))
    out = set()
    for m in DATA_NUM.finditer(text):
        tok = _norm(m.group())
        if BARE_YEAR.match(tok) and not VERSION_YEAR.match(text[m.end():m.end() + 8]):
            continue
        out.add(tok)
    return out


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


def verify(src, out, images, min_ratio=None, extra_src=''):
    """四项确定性检查。任一不过则不发布。

    extra_src 是「同样合法的素材」：引子通道会把相关笔记片段一起喂给模型
    并要求优先从中取材，那些片段里的数字当然不算编造。但它只参与「有没有
    凭空多出数据」的比对，不参与篇幅比例 —— 篇幅永远以引子笔记为准，
    否则喂进去几篇片段就能把「正文过短」这条稀释掉。
    实测漏掉这一层的后果：模型老老实实引用片段里的 50 pmol，被判成幻觉。

    先整体 URL 解码再比对：Obsidian 粘贴的图片名带空格，正文里是
    「Pasted%20image%2020240528.png」。不解码有两处会出错 ——
    图片 basename 对不上（误判丢图），且 %2020240528 会被数字校验
    读成 2020240528，凭空多出一个源文没有的「数据」。
    """
    if min_ratio is None:
        min_ratio = config.MIN_LENGTH_RATIO
    src = urllib.parse.unquote(src)
    out = urllib.parse.unquote(out)
    pool = src + '\n' + urllib.parse.unquote(extra_src)
    failures = []

    missing = [i for i in images if i not in out]
    if missing:
        failures.append(f'丢图: {missing}')

    # 只查「新增」不查「减少」：重组时删掉重复论述是正常的，
    # 凭空冒出源文没有的数据才是危险信号。
    #
    # 单位的写法差异不是编造，值本身对不上才是。三种情形分开判：
    #
    #   数值源文根本没有            → 拦。这是这条规则的本职
    #   输出裸写                    → 值对上就放行。源文「4000Da」模型写成
    #                                「4000 道尔顿」是复述（HPLC 那篇实测）
    #   输出带单位，源文裸写过该值   → 放行。源文「precursor mass is 574.3」
    #                                模型补成「574.3 Da」也是复述
    #                                （master 手动触发 publish 抓到的回归）
    #   输出带单位，源文只带别的单位 → 拦。源文「50 mM」改成「50 pmol」是
    #                                单位调包，实测真出现过（label-free 那篇）
    pool_nums = data_numbers(pool)
    out_nums = data_numbers(out)
    # 源文里裸写过的数值。裸写意味着源文自己就没把单位绑死，此时输出补个
    # 单位算复述；只带单位出现过的数值，则必须连单位一起对上。
    pool_bare = {t for t in pool_nums if BARE_NUM.match(t)}
    pool_values = {_value(t) for t in pool_nums}
    new_nums = set()
    for tok in out_nums - pool_nums:
        val = _value(tok)
        if val not in pool_values:
            new_nums.add(tok)            # 值本身源文没有 —— 编造
        elif not BARE_NUM.match(tok) and val not in pool_bare:
            new_nums.add(tok)            # 值有，但两边单位不同 —— 调包
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
