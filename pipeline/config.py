"""流水线全局常量。改这里就能调整过滤范围和分组粒度，不用翻各模块。"""

EXCLUDE_DIRS = {'Clippings', 'Backup', 'tmp', 'script', 'Inbox-待处理',
                'Excalidraw', 'docs', '.claude', '.git', 'Obsidian'}

PUBLISHABLE_TYPES = {'note', 'sci-note', 'book-note', '综述', 'lit-review',
                     'reference', 'regulatory-strategy', '项目报告', '实验',
                     'reference-table'}

MIN_GROUP, MAX_GROUP = 3, 30

DRIVE_FOLDER_ID = '1jwf_lkCo-Rq42VwWToyTeu2ciJTRg4zT'
IMAGE_MAX_WIDTH = 1200
WEBP_QUALITY = 82

MIN_LENGTH_RATIO = 0.4
