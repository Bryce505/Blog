"""流水线全局常量。改这里就能调整过滤范围和分组粒度，不用翻各模块。"""

EXCLUDE_DIRS = {'Clippings', 'Backup', 'tmp', 'script', 'Inbox-待处理',
                'Excalidraw', 'docs', '.claude', '.git', 'Obsidian'}

PUBLISHABLE_TYPES = {'note', 'sci-note', 'book-note', '综述', 'lit-review',
                     'reference', 'regulatory-strategy', '项目报告', '实验',
                     'reference-table'}

MIN_GROUP, MAX_GROUP = 3, 30

# 体量上限。按篇数限制是错的指标：实测有单篇 158 万字符的笔记（整本书
# 导入），一篇就撑爆 1M 上下文；也有 9 篇加起来 170 万字符的组。
# 单篇超过 20 万字符的，实测全是整书/整课程导入，不是笔记。
MAX_NOTE_CHARS = 200_000
# 组的总预算，留足空间给系统提示和模型输出
MAX_GROUP_CHARS = 400_000

DRIVE_FOLDER_ID = '1jwf_lkCo-Rq42VwWToyTeu2ciJTRg4zT'
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
