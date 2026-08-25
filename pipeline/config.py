"""流水线全局常量。改这里就能调整过滤范围和分组粒度，不用翻各模块。"""

EXCLUDE_DIRS = {'Clippings', 'Backup', 'tmp', 'script', 'Inbox-待处理',
                'Excalidraw', 'docs', '.claude', '.git', 'Obsidian'}

PUBLISHABLE_TYPES = {'note', 'sci-note', 'book-note', '综述', 'lit-review',
                     'reference', 'regulatory-strategy', '项目报告', '实验',
                     'reference-table'}

MIN_GROUP, MAX_GROUP = 3, 30

# 体量上限。按篇数限制是错的指标：实测有单篇 158 万字符的笔记（整本书
# 导入），一篇就撑爆 1M 上下文；也有 9 篇加起来 170 万字符的组。
#
# 阈值定在 3 万字符：超过这个量的笔记实测绝大多数是整书/整章转录
# （《Capillary Electrophoresis Methods》《ELISA Guidebook》《Mass
# Spectrometry A Textbook》等），公开重组发布有版权问题。真正的读书
# 笔记都在几千字符量级，不受影响。
MAX_NOTE_CHARS = 30_000

# 体量豁免名单：作者自己写的长文，绕过上面的阈值。
#
# 为什么用名单而不是自动判别：实测数据里没有可靠信号 —— book 字段只填了
# 4/22，文件名模式要凑 Chapter/作者_年份/Guidebook/course/Practitioners
# 一串关键词才盖得全，新增一本书就漏。只有二十来篇要分类，写分类器不如
# 列名单：默认排除（对版权问题这是安全方向），原创的显式放行。
#
# 新写了超过 3 万字符的原创长文，往这里加一行路径即可。
SIZE_EXEMPT_NOTES = {
    'Bio-analysis/酶活性/重组尿酸氧化酶活性分析方法开发.md',
    'Antibody-Characterization/QC检测流程梳理.md',
    'Antibody-Characterization/HCP/吐温降解酶(高风险HCP)及其检测方法系统综述.md',
    'Antibody-Characterization/protein sequencing与离子类型.md',
    'Quality_and_Regulation/注册申报分析工作的模块化和模板化/分项策略-结构表征研究策略-20260702.md',
    'Quality_and_Regulation/注册申报分析工作的模块化和模板化/分项策略-功能学研究策略-20260703.md',
    'Analytical technology/Capillary electrophoresis methods for pharmaceutical analysis/峰面积不稳定/CE_Electrokinetic_Injection_EOF_Report.md',
}
# 组的总预算。实测教训：上限 40 万时有个组攒到 17 万字符（14 篇），
# DeepSeek 直接退化成摘要，输出只有源文的 10%，86 条文献引用全丢。
# 要求模型把 15 万字符忠实重组成一篇文章，这个要求本身不现实。
# 调到 5 万后组数只从 32 掉到 30，中位组体量几乎不变（27.9K → 25.4K），
# 砍掉的只是几个撑爆的离群组。
MAX_GROUP_CHARS = 50_000

DRIVE_FOLDER_ID = '1jwf_lkCo-Rq42VwWToyTeu2ciJTRg4zT'

# 笔记引用名 → Drive 上的实际文件名。
#
# 早期 Typora 按「截图时刻」命名（17 位 yyyyMMddHHmmssSSS），上传工具按
# 「上传时刻」重命名成 15 位（yyyyMMddHHmm + 3 位），笔记里的引用没跟着
# 改。实测全库只有 5 处，全在 Chapter1 An Overview.md：Drive 上 17 位命名
# 的文件一个都没有，而每张缺图的同一分钟里正好躺着一张任何笔记都没引用
# 过的 15 位文件 —— 逐张人工确认过是同一张图。
#
# 刻意不做自动的时间戳近似匹配：同一分钟撞车就会把错图发出去，对技术
# 文章来说比留个「图片暂缺」更糟。要认就明确列出来。
IMAGE_ALIASES = {
    '20220120182528049.png': '202201201825137.png',
    '20220120183022375.png': '202201201830449.png',
    '20220120213824398.png': '202201202138496.png',
    # 这两张同在 22:43 上传，按 3 位尾号的先后对应正文里两张连排的顺序。
    # 万一认反了，把这两行的值对调即可（都是电子倍增器一节的检测器图）。
    '20220224224140560.png': '202202242243506.png',
    '20220224224304366.png': '202202242243742.png',
}
IMAGE_MAX_WIDTH = 1200
WEBP_QUALITY = 82

MIN_LENGTH_RATIO = 0.4

# DeepSeek。模型 ID 以 GET https://api.deepseek.com/models 返回的为准 ——
# 早期的 deepseek-chat / deepseek-reasoner 已不在清单里。
# v4-pro 与 v4-flash 都是 1M 上下文、384K 最大输出。
# 技术内容改写对保真度要求高，默认用 pro；想省钱换 flash 即可，
# 反正机械校验器会兜底。
DEEPSEEK_API_URL = 'https://api.deepseek.com/chat/completions'
DEEPSEEK_MODEL = 'deepseek-v4-pro'
# 给足输出余量：截断会触发「正文过短」校验，白烧一次 token 还得重跑
DEEPSEEK_MAX_TOKENS = 65536
DEEPSEEK_TEMPERATURE = 0.3
