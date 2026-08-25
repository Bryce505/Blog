"""机械校验器：LLM 输出的确定性安全阀。

这是整套流水线里最关键的代码。内容是生物医药 CMC / 分析方法，AI 把
某个流速、某条法规编号改错了，是专业性错误而不是排版问题。校验拦不住
篡改，这条流水线就不该上线。

四项检查任一不过，文章进 _review/ 等人工复核，不发布。
"""
import re
import urllib.parse
from dataclasses import dataclass, field

import config

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
