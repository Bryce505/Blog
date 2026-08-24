# 技术博客自动发布流水线 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 Obsidian-base 里的原创笔记按标签自动成组、经 DeepSeek 结构重组为技术文章、通过机械校验后发布到 Astro + GitHub Pages 站点，并保留手动投稿通道。

**Architecture:** 单仓库，两条通道。自动通道 `select → images → compose → verify → 落盘`，每晚 21:00 由 GitHub Actions 触发发一篇；手动通道 `drafts/*.md → images → 落盘`，push 即发。Python 流水线只产出 markdown，Astro 负责全部渲染。校验器是整套系统的安全阀：拦不住 AI 篡改数据，这条流水线就不该上线。

**Tech Stack:** Python 3.11（uv venv）、PyYAML、Pillow、google-api-python-client、DeepSeek API（OpenAI 兼容）、Astro、GitHub Actions

**Spec:** `TechnicalBlog/docs/superpowers/specs/2026-08-24-tech-blog-pipeline-design.md`

## Global Constraints

- 开发目录 `TechnicalBlog/`，其内容即未来 `Bryce505/blog` 的仓库根（用 `git subtree split` 拆出）
- Python 虚拟环境建在 `TechnicalBlog/` 下，用 `uv venv`；不与仓库其他子项目共用
- **不引入测试框架**：`pipeline/test_pipeline.py` 用 assert，文件底部自带 10 行 runner，`python pipeline/test_pipeline.py` 直接跑
- 单元测试一律跑 `pipeline/fixtures/` 里的样本笔记，不依赖真实 vault，保证 CI 可跑
- commit message 用中文；全部推到 `claude/tech-blog-sync-architecture-8bcvq2`
- 排除目录：`Clippings` `Backup` `tmp` `script` `Inbox-待处理` `Excalidraw` `docs` `.claude` `Obsidian`
- 可发布 type 白名单：`note` `sci-note` `book-note` `综述` `lit-review` `reference` `regulatory-strategy` `项目报告` `实验` `reference-table`
- 分组阈值：三级标签，3 ≤ 组内笔记数 ≤ 30
- 图片：限宽 1200px，WebP quality 82
- Drive 文件夹 id：`1jwf_lkCo-Rq42VwWToyTeu2ciJTRg4zT`

---

### Task 1: 项目骨架与笔记解析

**Files:**
- Create: `TechnicalBlog/pipeline/config.py`
- Create: `TechnicalBlog/pipeline/vault.py`
- Create: `TechnicalBlog/pipeline/requirements.txt`
- Create: `TechnicalBlog/pipeline/fixtures/sci-note-dsc.md`
- Create: `TechnicalBlog/pipeline/fixtures/note-sec.md`
- Create: `TechnicalBlog/pipeline/fixtures/clipping-excluded.md`
- Test: `TechnicalBlog/pipeline/test_pipeline.py`

**Interfaces:**
- Consumes: 无（首个任务）
- Produces: `Note` dataclass（字段 `path title tags type description book paper link body images wikilinks`）、`parse_note(path: Path, vault_root: Path) -> Note | None`、`load_vault(vault_root: Path) -> list[Note]`、`config` 中的常量 `EXCLUDE_DIRS` `PUBLISHABLE_TYPES` `MIN_GROUP` `MAX_GROUP` `DRIVE_FOLDER_ID` `IMAGE_MAX_WIDTH` `WEBP_QUALITY`

- [ ] **Step 1: 建目录与虚拟环境**

```bash
cd TechnicalBlog
mkdir -p pipeline/fixtures drafts public/images src/content/posts _review
touch _review/.gitkeep
uv venv && . .venv/bin/activate
cat > pipeline/requirements.txt <<'EOF'
PyYAML>=6.0
Pillow>=10.0
google-api-python-client>=2.100
google-auth>=2.23
requests>=2.31
EOF
uv pip install -r pipeline/requirements.txt
```

- [ ] **Step 2: 写三个 fixture 笔记**

`pipeline/fixtures/sci-note-dsc.md`：
```markdown
---
tags:
  - 02分子表征/Biophysical-Techniques/DSC
  - 04抗体设计与筛选/stability
book: Biophysical characterization of proteins
description: DSC 测热容差的极简摘录
type: sci-note
---
折叠态与去折叠态存在较大热容差 δCp，扫描速率设为 60 °C/h。
详见[[热容和热容差]]。
![](../image&attachment/image-laptop/DSC-curve.png)
```

`pipeline/fixtures/note-sec.md`：
```markdown
---
tags:
  - 02分子表征/Size-variant/SEC
type: note
title: SEC 方法开发要点
link: https://example.org/sec
---
柱温 25 °C，流速 0.5 mL/min，参考 ICH Q6B。
![[../image&attachment/image-laptop/SEC-peak.png|600]]
```

`pipeline/fixtures/clipping-excluded.md`：
```markdown
---
tags:
  - "clippings"
type: clipping
author:
  - "[[某作者]]"
link: https://mp.weixin.qq.com/s/xxxx
---
这是转载的他人文章正文，不应进入可发布集合。
```

- [ ] **Step 3: 写 config.py**

```python
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
```

- [ ] **Step 4: 写失败的测试**

在 `pipeline/test_pipeline.py`：
```python
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import vault

FIX = Path(__file__).parent / 'fixtures'

def test_parse_sci_note():
    n = vault.parse_note(FIX / 'sci-note-dsc.md', FIX)
    assert n is not None
    assert n.type == 'sci-note'
    assert '02分子表征/Biophysical-Techniques/DSC' in n.tags
    assert n.book == 'Biophysical characterization of proteins'
    assert n.images == ['DSC-curve.png']
    assert n.wikilinks == ['热容和热容差']

def test_parse_wiki_image_with_size():
    n = vault.parse_note(FIX / 'note-sec.md', FIX)
    assert n.images == ['SEC-peak.png'], n.images
    assert n.title == 'SEC 方法开发要点'
    assert n.wikilinks == []

def test_load_vault_filters_nothing_by_itself():
    notes = vault.load_vault(FIX)
    assert len(notes) == 3
```

文件底部加 runner（本任务写一次，后续任务只追加测试函数）：
```python
if __name__ == '__main__':
    fns = [(k, v) for k, v in sorted(globals().items()) if k.startswith('test_')]
    bad = 0
    for name, fn in fns:
        try:
            fn(); print(f'  PASS  {name}')
        except Exception as e:
            bad += 1; print(f'  FAIL  {name}: {type(e).__name__}: {e}')
    print(f'\n{len(fns) - bad}/{len(fns)} passed')
    sys.exit(1 if bad else 0)
```

- [ ] **Step 5: 跑测试确认失败**

Run: `python pipeline/test_pipeline.py`
Expected: FAIL，`ModuleNotFoundError: No module named 'vault'`

- [ ] **Step 6: 写 vault.py**

```python
import re
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path

import yaml

import config

FM_RE = re.compile(r'^---\n(.*?)\n---\n?', re.S)
IMG_MD = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
IMG_WIKI = re.compile(r'!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]')
WIKILINK = re.compile(r'(?<!!)\[\[([^\]|]+)(?:\|([^\]]*))?\]\]')


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


def _flat(v):
    """frontmatter 字段可能是 None / 字符串 / 列表，统一成字符串。"""
    if v is None:
        return ''
    if isinstance(v, list):
        return ', '.join(str(x) for x in v if x)
    return str(v)


def parse_note(path: Path, vault_root: Path):
    """解析单个 md。frontmatter 缺失或 YAML 损坏返回 None，不抛异常。"""
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
            p = urllib.parse.unquote(raw.split('|')[0].strip())
            if not p.startswith('http'):
                images.append(Path(p).name)

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
    """遍历 vault，跳过黑名单目录。不做 type 过滤——那是 select 的职责。"""
    notes = []
    for p in sorted(vault_root.rglob('*.md')):
        rel = p.relative_to(vault_root)
        if any(part in config.EXCLUDE_DIRS for part in rel.parts):
            continue
        n = parse_note(p, vault_root)
        if n:
            notes.append(n)
    return notes
```

- [ ] **Step 7: 跑测试确认通过**

Run: `python pipeline/test_pipeline.py`
Expected: `3/3 passed`

- [ ] **Step 8: 对真实 vault 冒烟**

Run: `python -c "import sys; sys.path.insert(0,'pipeline'); import vault; from pathlib import Path; ns=vault.load_vault(Path('/home/user/obsidian-base')); print(len(ns),'篇解析成功')"`
Expected: **516 篇**，无异常抛出。

实测基准（黑名单外共 971 篇 md）：454 篇无 frontmatter、1 篇 YAML 损坏（`Python/AI/llm-wiki-ClaudeCodeCLI...md`，双引号未闭合）、516 篇正常解析。无 frontmatter 的笔记没有标签和 type，本来就不会被选中发布，跳过不造成损失。数字大幅低于 516 说明解析逻辑退化。

- [ ] **Step 9: 提交**

```bash
git add TechnicalBlog/pipeline TechnicalBlog/.gitignore
git commit -m "TechnicalBlog: 笔记解析模块与测试骨架"
```

---

### Task 2: 分组选题

**Files:**
- Create: `TechnicalBlog/pipeline/select.py`
- Modify: `TechnicalBlog/pipeline/test_pipeline.py`（追加测试）

**Interfaces:**
- Consumes: `vault.Note`、`vault.load_vault`、`config.PUBLISHABLE_TYPES/MIN_GROUP/MAX_GROUP`
- Produces: `Group` dataclass（字段 `tag notes source_hash slug`）、`publishable(notes) -> list[Note]`、`build_groups(notes) -> list[Group]`、`pick_next(groups, published: dict) -> Group | None`

- [ ] **Step 1: 写失败的测试**

追加到 `test_pipeline.py`：
```python
import select_ as sel   # 见 Step 3 说明：模块名避开标准库 select

def _fake(path, tags, type_='note'):
    return vault.Note(path=path, title=path, tags=tags, type=type_, body='正文 ' + path)

def test_publishable_excludes_clipping_type():
    notes = vault.load_vault(FIX)
    pub = sel.publishable(notes)
    assert len(pub) == 2
    assert all(n.type != 'clipping' for n in pub)

def test_group_by_third_level_tag():
    ns = [_fake(f'n{i}.md', ['02分子表征/PTM/糖基化']) for i in range(5)]
    gs = sel.build_groups(ns)
    assert len(gs) == 1
    assert gs[0].tag == '02分子表征/PTM/糖基化'
    assert len(gs[0].notes) == 5

def test_note_belongs_to_first_third_level_tag_only():
    ns = [_fake(f'n{i}.md', ['00基础/文献', '02分子表征/PTM/糖基化', '03质量控制/SEC/柱效'])
          for i in range(4)]
    gs = sel.build_groups(ns)
    assert len(gs) == 1, [g.tag for g in gs]
    assert gs[0].tag == '02分子表征/PTM/糖基化'

def test_small_group_dropped():
    ns = [_fake('a.md', ['02分子表征/PTM/糖基化']), _fake('b.md', ['02分子表征/PTM/糖基化'])]
    assert sel.build_groups(ns) == []

def test_oversized_group_truncated_to_max():
    ns = [_fake(f'n{i}.md', ['02分子表征/PTM/糖基化']) for i in range(40)]
    gs = sel.build_groups(ns)
    assert len(gs[0].notes) == 30

def test_pick_next_skips_published_unchanged():
    ns = [_fake(f'n{i}.md', ['02分子表征/PTM/糖基化']) for i in range(5)]
    g = sel.build_groups(ns)[0]
    published = {g.tag: {'source_hash': g.source_hash, 'slug': g.slug}}
    assert sel.pick_next([g], published) is None
    assert sel.pick_next([g], {}) is g

def test_pick_next_returns_changed_group():
    ns = [_fake(f'n{i}.md', ['02分子表征/PTM/糖基化']) for i in range(5)]
    g = sel.build_groups(ns)[0]
    published = {g.tag: {'source_hash': 'sha256:stale', 'slug': g.slug}}
    assert sel.pick_next([g], published) is g
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python pipeline/test_pipeline.py`
Expected: FAIL，`ModuleNotFoundError: No module named 'select_'`

- [ ] **Step 3: 写 select.py，并以 `select_` 为导入名**

文件名 `select.py` 与 Python 标准库 `select` 同名。因为 `sys.path` 插入了 `pipeline/` 且位于最前，本地模块会优先命中，但这依赖导入顺序，太脆。**直接把文件命名为 `select_.py`**，消除歧义：

```bash
# 文件实际路径：TechnicalBlog/pipeline/select_.py
```

```python
import hashlib
import re
from dataclasses import dataclass

import config


@dataclass
class Group:
    tag: str
    notes: list
    source_hash: str
    slug: str


def publishable(notes):
    return [n for n in notes if n.type in config.PUBLISHABLE_TYPES and n.tags]


def _primary_tag(note):
    """归属规则：tags 中出现顺序最靠前、层级 >=3 的标签；退而求其次取二级。"""
    for t in note.tags:
        if t.count('/') >= 2:
            return t
    for t in note.tags:
        if t.count('/') >= 1:
            return t
    return None


def _slugify(tag):
    """三级标签转 URL slug。中文原样保留（Astro 支持 Unicode 路由），去掉空白与特殊字符。"""
    s = tag.replace('/', '-')
    s = re.sub(r'[^\w一-鿿-]+', '-', s)
    return re.sub(r'-{2,}', '-', s).strip('-').lower()


def _hash(notes):
    h = hashlib.sha256()
    for n in sorted(notes, key=lambda x: x.path):
        h.update(n.path.encode())
        h.update(n.body.encode())
    return 'sha256:' + h.hexdigest()


def build_groups(notes):
    """按主标签建组。一篇笔记只进一组，避免同一内容出现在多篇文章里。"""
    buckets = {}
    for n in publishable(notes):
        t = _primary_tag(n)
        if t:
            buckets.setdefault(t, []).append(n)

    groups = []
    for tag, ns in buckets.items():
        if len(ns) < config.MIN_GROUP:
            continue
        ns = sorted(ns, key=lambda x: x.path)[:config.MAX_GROUP]
        groups.append(Group(tag=tag, notes=ns, source_hash=_hash(ns), slug=_slugify(tag)))
    return sorted(groups, key=lambda g: (-len(g.notes), g.tag))


def pick_next(groups, published):
    """取第一个未发布、或源笔记已变更的组。"""
    for g in groups:
        rec = published.get(g.tag)
        if rec is None or rec.get('source_hash') != g.source_hash:
            return g
    return None
```

同步修改 Task 2 Step 1 的导入为 `import select_ as sel`（已按此写）。

- [ ] **Step 4: 跑测试确认通过**

Run: `python pipeline/test_pipeline.py`
Expected: `10/10 passed`

- [ ] **Step 5: 对真实 vault 验证回归基准**

Run:
```bash
python -c "
import sys; sys.path.insert(0,'pipeline')
import vault, select_ as sel
from pathlib import Path
ns = vault.load_vault(Path('/home/user/obsidian-base'))
pub = sel.publishable(ns); gs = sel.build_groups(ns)
print(f'可发布 {len(pub)} 篇，合格组 {len(gs)} 个')
for g in gs[:5]: print(f'  {len(g.notes):3d}  {g.tag}')
"
```
Expected: **可发布 224 篇 → 合格组 33 个，覆盖 198 篇（88%）**。另需断言：无一级标签组、slug 唯一、同一笔记不出现在多组。数字大幅偏离说明过滤或回退逻辑漂移，先查原因再继续。

- [ ] **Step 6: 提交**

```bash
git add TechnicalBlog/pipeline
git commit -m "TechnicalBlog: 按三级标签分组选题与去重"
```

---

### Task 3: 机械校验器（本项目最关键代码）

**Files:**
- Create: `TechnicalBlog/pipeline/verify.py`
- Modify: `TechnicalBlog/pipeline/test_pipeline.py`

**Interfaces:**
- Consumes: `config.MIN_LENGTH_RATIO`
- Produces: `VerifyResult` dataclass（`ok: bool`、`failures: list[str]`）、`data_numbers(text) -> set[str]`、`citations(text) -> set[str]`、`verify(src, out, images, min_ratio=None) -> VerifyResult`

本任务的负向用例比实现更重要：校验器拦不住错误，等于没有校验器。以下代码已在真实数据上验证通过 8 项断言。

- [ ] **Step 1: 写失败的测试（正向 + 负向）**

追加到 `test_pipeline.py`：
```python
import verify as vf

SRC = ("SEC 柱温设为 25 °C，流速 0.5 mL/min，进样量 20 μL，"
       "参考 ICH Q6B 和 21 CFR 211.194。\n"
       "分子量约 148000 Da，回收率 95%。本文分为 3 个部分讨论。\n"
       "![](../image&attachment/image-laptop/XTEN-1.png)\n") * 4
IMGS = ['XTEN-1.png']

def test_verify_passes_identical():
    assert vf.verify(SRC, SRC, IMGS).ok

def test_verify_catches_changed_flowrate():
    r = vf.verify(SRC, SRC.replace('0.5 mL/min', '0.8 mL/min', 1), IMGS)
    assert not r.ok and any('数据' in f for f in r.failures)

def test_verify_catches_dropped_image():
    out = SRC.replace('![](../image&attachment/image-laptop/XTEN-1.png)', '')
    r = vf.verify(SRC, out, IMGS)
    assert not r.ok and any('丢图' in f for f in r.failures)

def test_verify_catches_lost_regulation():
    r = vf.verify(SRC, SRC.replace('ICH Q6B', '相关指导原则'), IMGS)
    assert not r.ok and any('引用' in f for f in r.failures)

def test_verify_catches_truncation():
    r = vf.verify(SRC, SRC[:len(SRC) // 5], IMGS)
    assert not r.ok and any('过短' in f for f in r.failures)

def test_verify_catches_changed_molecular_weight():
    r = vf.verify(SRC, SRC.replace('148000', '148500'), IMGS)
    assert not r.ok and any('数据' in f for f in r.failures)

def test_verify_catches_changed_recovery():
    r = vf.verify(SRC, SRC.replace('95%', '98%'), IMGS)
    assert not r.ok and any('数据' in f for f in r.failures)

def test_verify_allows_ai_framing_integers():
    """AI 写导读必然产生新的小整数，不能因此误报——否则校验器天天误杀。"""
    out = SRC + '\n本文将从 5 个角度展开，共 2 类方法。\n'
    assert vf.verify(SRC, out, IMGS).ok

def test_verify_allows_dropping_redundant_numbers():
    """重组时删掉重复论述是正常的，数字变少不该报错。"""
    out = SRC.replace('回收率 95%。', '', 2)
    assert vf.verify(SRC, out, IMGS).ok

def test_data_numbers_ignores_bare_small_int():
    assert vf.data_numbers('分为 3 类') == set()
    assert '25°c' in vf.data_numbers('柱温 25 °C')
    assert '0.5' in vf.data_numbers('流速 0.5 mL/min')
    assert '148000' in vf.data_numbers('分子量 148000 Da')
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python pipeline/test_pipeline.py`
Expected: FAIL，`ModuleNotFoundError: No module named 'verify'`

- [ ] **Step 3: 写 verify.py**

```python
import re
from dataclasses import dataclass, field

import config

# 只抓「承载数据」的数字：带单位、含小数点、或三位以上整数。
# 裸露的一两位整数（"分为 3 类"）不纳入——AI 写导读必然产生这类数字，
# 纳入检查等于让校验器天天误报。
DATA_NUM = re.compile(r"""
    \d+\.\d+
  | \d{3,}
  | \d+(?:\.\d+)?\s*(?:%|‰|°C|℃|[a-zA-ZμµÅΩ]{1,6})
""", re.X)

CITATION = re.compile(
    r'10\.\d{4,9}/\S+'                       # DOI
    r'|ICH\s*[QSEM]\d[A-Z]?(?:\(R\d\))?'     # ICH Q6B / Q2(R2)
    r'|21\s*CFR\s*\d+(?:\.\d+)?'             # 21 CFR 211.194
    r'|USP\s*<\d+>'                          # USP <1058>
    r'|Ph\.\s*Eur\.\s*\d[\d.]*',             # Ph. Eur. 2.2.29
    re.I)


def _norm(t):
    return re.sub(r'\s+', '', t).lower()


def data_numbers(text):
    return {_norm(m.group()) for m in DATA_NUM.finditer(text)}


def citations(text):
    return {_norm(m.group()) for m in CITATION.finditer(text)}


@dataclass
class VerifyResult:
    ok: bool
    failures: list = field(default_factory=list)


def verify(src, out, images, min_ratio=None):
    """对 LLM 输出做四项确定性检查。任一不过则不发布。"""
    if min_ratio is None:
        min_ratio = config.MIN_LENGTH_RATIO
    failures = []

    missing = [i for i in images if i not in out]
    if missing:
        failures.append(f'丢图: {missing}')

    # 只查「新增」，不查「减少」：重组时删掉重复论述是正常的。
    new_nums = data_numbers(out) - data_numbers(src)
    if new_nums:
        failures.append(f'出现源文没有的数据: {sorted(new_nums)[:10]}')

    lost = citations(src) - citations(out)
    if lost:
        failures.append(f'丢失引用/条款: {sorted(lost)[:10]}')

    src_len = len(re.sub(r'\s', '', src))
    out_len = len(re.sub(r'\s', '', out))
    if src_len and out_len < src_len * min_ratio:
        failures.append(f'正文过短: {out_len}/{src_len}={out_len / src_len:.0%} < {min_ratio:.0%}')

    return VerifyResult(ok=not failures, failures=failures)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `python pipeline/test_pipeline.py`
Expected: `20/20 passed`，其中 10 个 verify 相关用例全过

- [ ] **Step 5: 提交**

```bash
git add TechnicalBlog/pipeline
git commit -m "TechnicalBlog: 机械校验器，拦截 AI 篡改数据与丢图"
```

---

### Task 4: 双链解析、图片重写与图注

**Files:**
- Create: `TechnicalBlog/pipeline/render.py`
- Modify: `TechnicalBlog/pipeline/test_pipeline.py`

**Interfaces:**
- Consumes: `vault.Note`
- Produces: `resolve_wikilinks(text, title_to_slug: dict) -> str`、`rewrite_images(text, image_map: dict, missing: list, caption_of: dict) -> str`、`caption_for(note) -> str`

- [ ] **Step 1: 写失败的测试**

```python
import render as rd

def test_wikilink_published_becomes_link():
    out = rd.resolve_wikilinks('详见[[热容和热容差]]。', {'热容和热容差': 'dsc-basics'})
    assert out == '详见[热容和热容差](/posts/dsc-basics)。'

def test_wikilink_with_alias():
    out = rd.resolve_wikilinks('见[[热容和热容差|热容]]。', {'热容和热容差': 'dsc-basics'})
    assert out == '见[热容](/posts/dsc-basics)。'

def test_wikilink_unpublished_degrades_to_plain_text():
    """不留死链：未发布的目标退化成纯文字，保留可读性。"""
    assert rd.resolve_wikilinks('详见[[某笔记]]。', {}) == '详见某笔记。'

def test_image_rewritten_to_webp_path():
    out = rd.rewrite_images(
        '![](../image&attachment/image-laptop/SEC-peak.png)',
        {'SEC-peak.png': '/images/sec/SEC-peak.webp'}, [], {})
    assert '/images/sec/SEC-peak.webp' in out
    assert 'image&attachment' not in out

def test_missing_image_becomes_note_not_broken_img():
    out = rd.rewrite_images('![](../x/GONE.png)', {}, ['GONE.png'], {})
    assert out.strip() == '*[图缺失：GONE.png]*'
    assert '![' not in out

def test_image_caption_appended_from_book():
    out = rd.rewrite_images(
        '![](../x/DSC-curve.png)',
        {'DSC-curve.png': '/images/a/DSC-curve.webp'}, [],
        {'DSC-curve.png': '图源：《Biophysical characterization of proteins》'})
    assert '图源：《Biophysical characterization of proteins》' in out

def test_caption_for_prefers_book_then_paper_then_link():
    assert rd.caption_for(vault.Note('p', 't', [], 'note', book='B书')) == '图源：《B书》'
    assert rd.caption_for(vault.Note('p', 't', [], 'note', paper='P论文')) == '图源：P论文'
    assert rd.caption_for(vault.Note('p', 't', [], 'note', link='http://x')) == '图源：http://x'
    assert rd.caption_for(vault.Note('p', 't', [], 'note')) == ''
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python pipeline/test_pipeline.py`
Expected: FAIL，`ModuleNotFoundError: No module named 'render'`

- [ ] **Step 3: 写 render.py**

```python
import re
import urllib.parse
from pathlib import Path

WIKILINK = re.compile(r'(?<!!)\[\[([^\]|]+)(?:\|([^\]]*))?\]\]')
IMG_MD = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
IMG_WIKI = re.compile(r'!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]')


def resolve_wikilinks(text, title_to_slug):
    """已发布转文章级站内链接；未发布退化成纯文本，不留死链。

    不做章节级锚点：采用结构重组后，源笔记不再对应输出文章里的独立章节。
    """
    def sub(m):
        target, alias = m.group(1).strip(), m.group(2)
        label = (alias or target).strip()
        slug = title_to_slug.get(target)
        return f'[{label}](/posts/{slug})' if slug else label
    return WIKILINK.sub(sub, text)


def caption_for(note):
    for val, tpl in ((note.book, '图源：《{}》'), (note.paper, '图源：{}'), (note.link, '图源：{}')):
        if val:
            return tpl.format(val)
    return ''


def _render_one(name, alt, image_map, missing, caption_of):
    if name in missing or name not in image_map:
        return f'*[图缺失：{name}]*'
    md = f'![{alt}]({image_map[name]})'
    cap = caption_of.get(name, '')
    return f'{md}\n*{cap}*' if cap else md


def rewrite_images(text, image_map, missing, caption_of):
    """把 Obsidian 的两种图片写法统一重写成站点内 WebP 路径，并追加图注。"""
    def sub_md(m):
        alt, raw = m.group(1), m.group(2)
        if raw.startswith('http'):
            return m.group(0)
        name = Path(urllib.parse.unquote(raw.split('|')[0].strip())).name
        return _render_one(name, alt, image_map, missing, caption_of)

    def sub_wiki(m):
        raw = m.group(1)
        name = Path(urllib.parse.unquote(raw.strip())).name
        return _render_one(name, '', image_map, missing, caption_of)

    return IMG_WIKI.sub(sub_wiki, IMG_MD.sub(sub_md, text))
```

- [ ] **Step 4: 跑测试确认通过**

Run: `python pipeline/test_pipeline.py`
Expected: `27/27 passed`

- [ ] **Step 5: 提交**

```bash
git add TechnicalBlog/pipeline
git commit -m "TechnicalBlog: 双链解析、图片路径重写与图注生成"
```

---

### Task 5: Google Drive 取图

**Files:**
- Create: `TechnicalBlog/pipeline/images.py`
- Modify: `TechnicalBlog/pipeline/test_pipeline.py`

**Interfaces:**
- Consumes: `config.DRIVE_FOLDER_ID/IMAGE_MAX_WIDTH/WEBP_QUALITY`
- Produces: `drive_service(sa_json_str) -> service`、`build_drive_index(service, folder_id) -> dict[str, str]`、`load_index(cache_path, factory, max_age_days=7) -> dict`、`to_webp(src_bytes, dest: Path) -> None`、`fetch_images(names, index, service, out_dir, url_prefix) -> tuple[dict, list]`

Drive 与网络部分不写单元测试（需要凭据、不可在 CI 跑）；可测的是 WebP 转换和索引缓存过期逻辑，这两项写测试。

- [ ] **Step 1: 写失败的测试**

```python
import io as _io
import json as _json
import time as _time
import images as im
from PIL import Image as _Image

def test_to_webp_downscales_and_converts(tmp_path=Path('/tmp/pipe-test')):
    tmp_path.mkdir(exist_ok=True)
    buf = _io.BytesIO()
    _Image.new('RGB', (2400, 1200), 'white').save(buf, format='PNG')
    dest = tmp_path / 'out.webp'
    im.to_webp(buf.getvalue(), dest)
    assert dest.exists()
    w, h = _Image.open(dest).size
    assert w == 1200 and h == 600, (w, h)
    assert _Image.open(dest).format == 'WEBP'

def test_to_webp_does_not_upscale_small_image(tmp_path=Path('/tmp/pipe-test')):
    tmp_path.mkdir(exist_ok=True)
    buf = _io.BytesIO()
    _Image.new('RGB', (300, 200), 'white').save(buf, format='PNG')
    dest = tmp_path / 'small.webp'
    im.to_webp(buf.getvalue(), dest)
    assert _Image.open(dest).size == (300, 200)

def test_index_cache_expires(tmp_path=Path('/tmp/pipe-test')):
    tmp_path.mkdir(exist_ok=True)
    cache = tmp_path / 'idx.json'
    cache.write_text(_json.dumps({'built_at': 0, 'index': {'a.png': 'id1'}}))
    calls = []
    def factory():
        calls.append(1)
        return {'b.png': 'id2'}
    idx = im.load_index(cache, factory, max_age_days=7)
    assert calls == [1] and idx == {'b.png': 'id2'}

def test_index_cache_reused_when_fresh(tmp_path=Path('/tmp/pipe-test')):
    tmp_path.mkdir(exist_ok=True)
    cache = tmp_path / 'idx2.json'
    cache.write_text(_json.dumps({'built_at': _time.time(), 'index': {'a.png': 'id1'}}))
    def factory():
        raise AssertionError('缓存未过期时不应重建索引')
    assert im.load_index(cache, factory, max_age_days=7) == {'a.png': 'id1'}
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python pipeline/test_pipeline.py`
Expected: FAIL，`ModuleNotFoundError: No module named 'images'`

- [ ] **Step 3: 写 images.py**

```python
import io
import json
import time
from pathlib import Path

from PIL import Image

import config


def drive_service(sa_json_str):
    """用服务账号 JSON 建 Drive 只读客户端。"""
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    info = json.loads(sa_json_str)
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=['https://www.googleapis.com/auth/drive.readonly'])
    return build('drive', 'v3', credentials=creds, cache_discovery=False)


def build_drive_index(service, folder_id):
    """递归遍历文件夹，建 文件名 -> fileId 映射。同名文件后出现者覆盖前者。"""
    index, stack = {}, [folder_id]
    while stack:
        fid = stack.pop()
        token = None
        while True:
            resp = service.files().list(
                q=f"'{fid}' in parents and trashed = false",
                fields='nextPageToken, files(id, name, mimeType)',
                pageSize=1000, pageToken=token).execute()
            for f in resp.get('files', []):
                if f['mimeType'] == 'application/vnd.google-apps.folder':
                    stack.append(f['id'])
                else:
                    index[f['name']] = f['id']
            token = resp.get('nextPageToken')
            if not token:
                break
    return index


def load_index(cache_path, factory, max_age_days=7):
    """索引缓存提交进仓库，避免每晚重新遍历整个 Drive 文件夹。"""
    cache_path = Path(cache_path)
    if cache_path.exists():
        try:
            data = json.loads(cache_path.read_text(encoding='utf-8'))
            if time.time() - data.get('built_at', 0) < max_age_days * 86400:
                return data['index']
        except (json.JSONDecodeError, KeyError):
            pass
    index = factory()
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps({'built_at': time.time(), 'index': index},
                                     ensure_ascii=False), encoding='utf-8')
    return index


def to_webp(src_bytes, dest: Path):
    """限宽 1200px（等比，不放大），转 WebP。"""
    img = Image.open(io.BytesIO(src_bytes))
    if img.mode in ('P', 'RGBA', 'LA'):
        img = img.convert('RGBA' if 'A' in img.mode else 'RGB')
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    if img.width > config.IMAGE_MAX_WIDTH:
        h = round(img.height * config.IMAGE_MAX_WIDTH / img.width)
        img = img.resize((config.IMAGE_MAX_WIDTH, h), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, 'WEBP', quality=config.WEBP_QUALITY)


def fetch_images(names, index, service, out_dir: Path, url_prefix):
    """返回 (name -> 站点内路径, 找不到的文件名列表)。已存在的跳过，重跑幂等。"""
    from googleapiclient.http import MediaIoBaseDownload
    mapping, missing = {}, []
    out_dir = Path(out_dir)
    for name in names:
        dest = out_dir / (Path(name).stem + '.webp')
        if dest.exists():
            mapping[name] = f'{url_prefix}/{dest.name}'
            continue
        fid = index.get(name)
        if not fid:
            missing.append(name)
            continue
        buf = io.BytesIO()
        dl = MediaIoBaseDownload(buf, service.files().get_media(fileId=fid))
        done = False
        while not done:
            _, done = dl.next_chunk()
        try:
            to_webp(buf.getvalue(), dest)
        except Exception:
            missing.append(name)
            continue
        mapping[name] = f'{url_prefix}/{dest.name}'
    return mapping, missing
```

- [ ] **Step 4: 跑测试确认通过**

Run: `python pipeline/test_pipeline.py`
Expected: `31/31 passed`

- [ ] **Step 5: 提交**

```bash
git add TechnicalBlog/pipeline
git commit -m "TechnicalBlog: Drive 取图与 WebP 转换"
```

---

### Task 6: DeepSeek 结构重组

**Files:**
- Create: `TechnicalBlog/pipeline/compose.py`
- Create: `TechnicalBlog/pipeline/prompt.md`
- Modify: `TechnicalBlog/pipeline/test_pipeline.py`

**Interfaces:**
- Consumes: `select_.Group`
- Produces: `SYSTEM_PROMPT`（从 `prompt.md` 读入）、`build_user_message(group) -> str`、`compose(group, api_key, model='deepseek-chat', _post=None) -> str`

`_post` 参数用于注入假 HTTP 调用，让 `compose` 在无 API key 时可测。

- [ ] **Step 1: 写系统提示 `prompt.md`**

```markdown
你在为一个中文专业技术博客整理文章，读者是生物医药 CMC 与分析方法领域的从业者。

## 你要做什么

我会给你若干篇主题相关的笔记。把它们**打散重组**成一篇结构完整的文章 —— 不是按笔记顺序拼接，而是重新梳理出一条属于这篇文章自己的脉络（例如：原理 → 方法 → 关键参数 → 常见问题）。允许调整段落顺序、合并重复论述、补写过渡句和开头导读。

## 绝对不能做的

1. **凡是包含数字、单位、法规条款号、文献引用、图片引用 `![...](...)` 的句子，必须逐字原样保留。** 不改写、不合并、不换算单位、不调整有效数字。
2. **不得引入源文中不存在的事实、数据或结论。** 你可以重新组织已有内容，不能补充你自己知道的知识。
3. **不得删除任何图片引用。** 图片可以换位置，但必须全部出现在输出里。
4. **不要输出 frontmatter。** 只输出正文 markdown，从一级标题开始。

## 语气与风格

- 中文书写，专业术语保留英文原词（如 SEC、CE-SDS、Orbitrap），不强行翻译
- 克制、准确，不用营销腔，不用"惊人的""革命性的"这类形容词
- 面向同行，不需要解释基础概念，但需要交代方法的适用边界
- 标题层级从 `##` 开始，不要出现 `#` 一级标题（标题由系统另行拼装）
```

- [ ] **Step 2: 写失败的测试**

```python
import compose as cp

def test_build_user_message_includes_all_notes_and_meta():
    ns = [vault.Note('a.md', 'A笔记', ['t/x/y'], 'note', body='正文A', book='书A'),
          vault.Note('b.md', 'B笔记', ['t/x/y'], 'note', body='正文B', paper='论文B')]
    g = sel.Group(tag='t/x/y', notes=ns, source_hash='h', slug='s')
    msg = cp.build_user_message(g)
    assert '正文A' in msg and '正文B' in msg
    assert 'A笔记' in msg and 'B笔记' in msg
    assert '书A' in msg and '论文B' in msg

def test_system_prompt_carries_hard_constraints():
    assert '逐字原样保留' in cp.SYSTEM_PROMPT
    assert '不得引入源文中不存在' in cp.SYSTEM_PROMPT
    assert '不要输出 frontmatter' in cp.SYSTEM_PROMPT

def test_compose_sends_system_prompt_first_and_returns_content():
    captured = {}
    def fake_post(url, headers, payload):
        captured['payload'] = payload
        return {'choices': [{'message': {'content': '## 重组后的文章\n正文'}}]}
    ns = [vault.Note('a.md', 'A', ['t/x/y'], 'note', body='正文A')]
    g = sel.Group(tag='t/x/y', notes=ns, source_hash='h', slug='s')
    out = cp.compose(g, api_key='k', _post=fake_post)
    assert out == '## 重组后的文章\n正文'
    msgs = captured['payload']['messages']
    assert msgs[0]['role'] == 'system' and '逐字原样保留' in msgs[0]['content']
    assert captured['payload']['model'] == 'deepseek-chat'
```

- [ ] **Step 3: 跑测试确认失败**

Run: `python pipeline/test_pipeline.py`
Expected: FAIL，`ModuleNotFoundError: No module named 'compose'`

- [ ] **Step 4: 写 compose.py**

```python
from pathlib import Path

import requests

SYSTEM_PROMPT = (Path(__file__).parent / 'prompt.md').read_text(encoding='utf-8')
API_URL = 'https://api.deepseek.com/chat/completions'


def build_user_message(group):
    parts = [f'以下是 {len(group.notes)} 篇关于「{group.tag}」的笔记，请重组成一篇文章。\n']
    for i, n in enumerate(group.notes, 1):
        meta = ' | '.join(x for x in (
            f'出处：《{n.book}》' if n.book else '',
            f'论文：{n.paper}' if n.paper else '',
            f'摘要：{n.description}' if n.description else '',
        ) if x)
        parts.append(f'\n### 笔记 {i}：{n.title}\n{meta}\n\n{n.body.strip()}\n')
    return ''.join(parts)


def _post(url, headers, payload):
    r = requests.post(url, headers=headers, json=payload, timeout=300)
    r.raise_for_status()
    return r.json()


def compose(group, api_key, model='deepseek-chat', _post=None):
    """调 DeepSeek 做结构重组。系统提示固定放最前面，便于 prompt caching。"""
    post = _post or globals()['_post']
    payload = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': build_user_message(group)},
        ],
        'temperature': 0.3,
        'max_tokens': 8000,
    }
    resp = post(API_URL, {'Authorization': f'Bearer {api_key}',
                          'Content-Type': 'application/json'}, payload)
    return resp['choices'][0]['message']['content'].strip()
```

- [ ] **Step 5: 跑测试确认通过**

Run: `python pipeline/test_pipeline.py`
Expected: `34/34 passed`

- [ ] **Step 6: 提交**

```bash
git add TechnicalBlog/pipeline
git commit -m "TechnicalBlog: DeepSeek 结构重组与硬约束提示词"
```

---

### Task 7: 自动通道串联

**Files:**
- Create: `TechnicalBlog/pipeline/main.py`
- Modify: `TechnicalBlog/pipeline/test_pipeline.py`

**Interfaces:**
- Consumes: 全部前置模块
- Produces: `assemble_frontmatter(group, title) -> str`、`run_auto(vault_root, blog_root, api_key, sa_json, count=1) -> list[dict]`（每项含 `slug status failures`）

- [ ] **Step 1: 写失败的测试**

```python
import main as mn

def test_assemble_frontmatter_has_required_fields():
    ns = [vault.Note('a.md', 'A', ['02分子表征/PTM/糖基化'], 'note', book='书A'),
          vault.Note('b.md', 'B', ['02分子表征/PTM/糖基化'], 'note', link='http://x')]
    g = sel.Group(tag='02分子表征/PTM/糖基化', notes=ns, source_hash='h',
                  slug='02分子表征-ptm-糖基化')
    fm = mn.assemble_frontmatter(g, '蛋白糖基化表征')
    assert fm.startswith('---\n') and fm.rstrip().endswith('---')
    assert 'title: "蛋白糖基化表征"' in fm
    assert 'category: "02分子表征"' in fm
    assert '02分子表征/PTM/糖基化' in fm
    assert '书A' in fm and 'http://x' in fm

def test_assemble_frontmatter_escapes_quotes_in_title():
    g = sel.Group(tag='a/b/c', notes=[vault.Note('a.md', 'A', ['a/b/c'], 'note')],
                  source_hash='h', slug='s')
    assert '\\"' in mn.assemble_frontmatter(g, '含"引号"的标题')
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python pipeline/test_pipeline.py`
Expected: FAIL，`ModuleNotFoundError: No module named 'main'`

- [ ] **Step 3: 写 main.py**

```python
import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import compose
import config
import images
import render
import select_ as sel
import vault
import verify


def _q(s):
    return str(s).replace('\\', '\\\\').replace('"', '\\"')


def assemble_frontmatter(group, title):
    """frontmatter 由流水线拼装，不让 LLM 生成，避免它编造日期和标签。"""
    refs = []
    for n in group.notes:
        for v in (n.book, n.paper, n.link):
            if v and v not in refs:
                refs.append(v)
    lines = ['---', f'title: "{_q(title)}"',
             f'date: {dt.date.today().isoformat()}',
             f'category: "{_q(group.tag.split("/")[0])}"',
             f'primaryTag: "{_q(group.tag)}"', 'tags:']
    seen = set()
    for n in group.notes:
        for t in n.tags:
            if t not in seen:
                seen.add(t)
                lines.append(f'  - "{_q(t)}"')
    lines.append('references:')
    for r in refs:
        lines.append(f'  - "{_q(r)}"')
    lines += ['sourceNotes:'] + [f'  - "{_q(n.path)}"' for n in group.notes]
    lines.append('---')
    return '\n'.join(lines) + '\n\n'


def _title_of(article_md, group):
    m = re.search(r'^##\s+(.+)$', article_md, re.M)
    return m.group(1).strip() if m else group.tag.split('/')[-1]


def _load_published(p):
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}


def run_auto(vault_root, blog_root, api_key, sa_json, count=1):
    vault_root, blog_root = Path(vault_root), Path(blog_root)
    pub_path = blog_root / 'published.json'
    published = _load_published(pub_path)

    notes = vault.load_vault(vault_root)
    groups = sel.build_groups(notes)
    title_to_slug = {n_title: rec['slug'] for rec in published.values()
                     for n_title in rec.get('noteTitles', [])}

    svc = images.drive_service(sa_json)
    index = images.load_index(
        Path(__file__).parent / 'drive_index.json',
        lambda: images.build_drive_index(svc, config.DRIVE_FOLDER_ID))

    results = []
    for _ in range(count):
        g = sel.pick_next(groups, published)
        if not g:
            break

        src_text = '\n\n'.join(n.body for n in g.notes)
        src_images = list(dict.fromkeys(i for n in g.notes for i in n.images))

        img_map, missing = images.fetch_images(
            src_images, index, svc,
            blog_root / 'public' / 'images' / g.slug, f'/images/{g.slug}')

        article = compose.compose(g, api_key)
        res = verify.verify(src_text, article, [i for i in src_images if i not in missing])

        caption_of = {i: render.caption_for(n) for n in g.notes for i in n.images}
        body = render.rewrite_images(article, img_map, missing, caption_of)
        body = render.resolve_wikilinks(body, title_to_slug)
        doc = assemble_frontmatter(g, _title_of(article, g)) + body

        if res.ok:
            out = blog_root / 'src' / 'content' / 'posts' / f'{g.slug}.md'
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(doc, encoding='utf-8')
            published[g.tag] = {
                'slug': g.slug, 'published_at': dt.date.today().isoformat(),
                'source_hash': g.source_hash,
                'notes': [n.path for n in g.notes],
                'noteTitles': [n.title for n in g.notes],
            }
            pub_path.write_text(json.dumps(published, ensure_ascii=False, indent=2),
                                encoding='utf-8')
        else:
            out = blog_root / '_review' / f'{g.slug}.md'
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text('<!-- 校验未通过：\n' + '\n'.join(res.failures) + '\n-->\n' + doc,
                           encoding='utf-8')

        results.append({'slug': g.slug, 'tag': g.tag,
                        'status': 'published' if res.ok else 'review',
                        'failures': res.failures, 'missingImages': missing})
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vault', required=True)
    ap.add_argument('--blog', default=str(Path(__file__).parent.parent))
    ap.add_argument('--count', type=int, default=1)
    ap.add_argument('--drafts', action='store_true', help='只处理 drafts/，跳过 AI 通道')
    a = ap.parse_args()

    if a.drafts:
        import drafts
        rs = drafts.run_drafts(a.blog, os.environ['GDRIVE_SA_JSON'])
    else:
        rs = run_auto(a.vault, a.blog, os.environ['DEEPSEEK_API_KEY'],
                      os.environ['GDRIVE_SA_JSON'], a.count)
    print(json.dumps(rs, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

- [ ] **Step 4: 跑测试确认通过**

Run: `python pipeline/test_pipeline.py`
Expected: `36/36 passed`

- [ ] **Step 5: 提交**

```bash
git add TechnicalBlog/pipeline
git commit -m "TechnicalBlog: 自动通道串联与 frontmatter 拼装"
```

---

### Task 8: drafts 手动发布通道

**Files:**
- Create: `TechnicalBlog/pipeline/drafts.py`
- Create: `TechnicalBlog/drafts/README.md`
- Modify: `TechnicalBlog/pipeline/test_pipeline.py`

**Interfaces:**
- Consumes: `images`、`render`、`vault.parse_note`
- Produces: `slugify_cn(text) -> str`、`fill_defaults(fm: dict, path: Path, body: str) -> dict`、`run_drafts(blog_root, sa_json) -> list[dict]`

- [ ] **Step 1: 写失败的测试**

```python
import drafts as df

def test_fill_defaults_requires_title_only():
    fm = df.fill_defaults({'title': '我的文章'}, Path('drafts/my-post.md'), '正文内容很长' * 30)
    assert fm['title'] == '我的文章'
    assert fm['slug'] == 'my-post'
    assert fm['category'] == '杂记'
    assert fm['tags'] == []
    assert len(fm['description']) <= 120 and fm['description']
    assert re.match(r'\d{4}-\d{2}-\d{2}', str(fm['date']))

def test_fill_defaults_derives_category_from_tags():
    fm = df.fill_defaults({'title': 'T', 'tags': ['03质量控制/SEC']}, Path('a.md'), '正文')
    assert fm['category'] == '03质量控制'

def test_fill_defaults_missing_title_returns_none():
    assert df.fill_defaults({}, Path('a.md'), '正文') is None

def test_slugify_cn_keeps_ascii_and_strips_symbols():
    assert df.slugify_cn('My Post! (v2)') == 'my-post-v2'
    assert df.slugify_cn('SEC 方法开发') == 'sec-方法开发'
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python pipeline/test_pipeline.py`
Expected: FAIL，`ModuleNotFoundError: No module named 'drafts'`

- [ ] **Step 3: 写 drafts.py**

```python
import datetime as dt
import json
import re
import subprocess
from pathlib import Path

import yaml

import config
import images
import render
import vault


def slugify_cn(text):
    s = re.sub(r'[^\w一-鿿]+', '-', str(text).strip().lower())
    return re.sub(r'-{2,}', '-', s).strip('-')


def _git_first_commit_date(path):
    try:
        out = subprocess.run(
            ['git', 'log', '--diff-filter=A', '--format=%ad', '--date=short', '--', str(path)],
            capture_output=True, text=True, timeout=10).stdout.strip().splitlines()
        return out[-1] if out else None
    except (OSError, subprocess.SubprocessError):
        return None


def fill_defaults(fm, path, body):
    """手写稿只需要 title 一个必填字段，其余全部有默认值。"""
    title = fm.get('title')
    if not title:
        return None
    tags = fm.get('tags') or []
    if isinstance(tags, str):
        tags = [tags]
    plain = re.sub(r'[#*>`\[\]!()]|\!\[[^\]]*\]\([^)]*\)', '', body).strip()
    return {
        'title': str(title),
        'slug': fm.get('slug') or slugify_cn(path.stem),
        'date': fm.get('date') or _git_first_commit_date(path) or dt.date.today().isoformat(),
        'tags': [str(t) for t in tags],
        'category': fm.get('category') or (tags[0].split('/')[0] if tags else '杂记'),
        'description': fm.get('description') or plain[:120],
        'references': fm.get('references') or [],
    }


def _dump(fm):
    return '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n'


def run_drafts(blog_root, sa_json):
    """drafts/*.md → 取图 + 双链解析 + 补默认值 → src/content/posts/，删除原件。"""
    blog_root = Path(blog_root)
    draft_dir = blog_root / 'drafts'
    posts_dir = blog_root / 'src' / 'content' / 'posts'
    pub_path = blog_root / 'published.json'
    published = json.loads(pub_path.read_text(encoding='utf-8')) if pub_path.exists() else {}
    title_to_slug = {t: r['slug'] for r in published.values() for t in r.get('noteTitles', [])}

    files = [p for p in sorted(draft_dir.glob('*.md')) if p.name != 'README.md']
    if not files:
        return []

    svc = images.drive_service(sa_json)
    index = images.load_index(
        Path(__file__).parent / 'drive_index.json',
        lambda: images.build_drive_index(svc, config.DRIVE_FOLDER_ID))

    results = []
    for p in files:
        note = vault.parse_note(p, draft_dir)
        if note is None:
            results.append({'file': p.name, 'status': 'error',
                            'reason': 'frontmatter 缺失或 YAML 损坏'})
            continue
        raw = yaml.safe_load(vault.FM_RE.match(p.read_text(encoding='utf-8')).group(1)) or {}
        fm = fill_defaults(raw, p, note.body)
        if fm is None:
            results.append({'file': p.name, 'status': 'error', 'reason': '缺少 title 字段'})
            continue

        out = posts_dir / f"{fm['slug']}.md"
        if out.exists():
            results.append({'file': p.name, 'status': 'error',
                            'reason': f"slug 冲突：{fm['slug']} 已存在，未覆盖"})
            continue

        img_map, missing = images.fetch_images(
            note.images, index, svc,
            blog_root / 'public' / 'images' / fm['slug'], f"/images/{fm['slug']}")
        body = render.rewrite_images(note.body, img_map, missing, {})
        body = render.resolve_wikilinks(body, title_to_slug)

        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(_dump(fm) + body, encoding='utf-8')
        p.unlink()
        results.append({'file': p.name, 'status': 'published',
                        'slug': fm['slug'], 'missingImages': missing})
    return results
```

- [ ] **Step 4: 写 `drafts/README.md`**

```markdown
# 手动发布投递口

把写好的 md 扔进这个目录，push 上去就会发布。

## 最少只要一个字段

```yaml
---
title: 文章标题
---
```

其余字段可选，缺省行为：`slug` 由文件名生成、`date` 取该文件首次提交时间、
`tags` 为空、`category` 从 tags 一级标签推导（无标签则归入「杂记」）、
`description` 取正文前 120 字。

## 这个通道替你做的事

- 从 Google Drive 拉取 `![](../image&attachment/xxx.png)` 引用的图并转 WebP
- 把 `[[双链]]` 转成站内链接（目标未发布则退化成纯文字，不留死链）

**不经过 DeepSeek，不经过机械校验** —— 自己写的内容不需要防篡改。

## 注意

- 发布成功后本目录里的原文件会被删除（已转存到 `src/content/posts/`）
- slug 与已有文章冲突时报错跳过，不会静默覆盖
```

- [ ] **Step 5: 跑测试确认通过**

Run: `python pipeline/test_pipeline.py`
Expected: `40/40 passed`

- [ ] **Step 6: 提交**

```bash
git add TechnicalBlog/pipeline TechnicalBlog/drafts
git commit -m "TechnicalBlog: drafts 手动发布通道"
```

---

### Task 9: Astro 骨架与 Obsidian callout 渲染

**Files:**
- Create: `TechnicalBlog/package.json`、`TechnicalBlog/astro.config.mjs`、`TechnicalBlog/tsconfig.json`
- Create: `TechnicalBlog/src/content.config.ts`
- Create: `TechnicalBlog/src/plugins/remark-callout.mjs`
- Create: `TechnicalBlog/src/content/posts/_sample.md`（本地验证用，Task 11 结束后删除）

**Interfaces:**
- Consumes: `main.assemble_frontmatter` 产出的字段（`title date category primaryTag tags references sourceNotes`）与 `drafts.fill_defaults` 产出的字段（`title slug date tags category description references`）
- Produces: Astro content collection `posts`，schema 兼容两条通道的 frontmatter

- [ ] **Step 1: 初始化 Astro**

```bash
cd TechnicalBlog
npm create astro@latest . -- --template minimal --no-install --no-git --skip-houston
npm install
npm install -D @astrojs/sitemap @astrojs/rss
```

- [ ] **Step 2: 写 content collection schema**

`src/content.config.ts`：
```typescript
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    category: z.string().default('杂记'),
    primaryTag: z.string().optional(),
    tags: z.array(z.string()).default([]),
    description: z.string().default(''),
    references: z.array(z.string()).default([]),
    sourceNotes: z.array(z.string()).default([]),
  }),
});

export const collections = { posts };
```

- [ ] **Step 3: 写 remark 插件处理 545 处 callout**

`src/plugins/remark-callout.mjs`：
```javascript
import { visit } from 'unist-util-visit';

const RE = /^\[!(\w+)\]([+-])?\s*(.*)$/;

/** Obsidian callout：>[!abstract] 标题 → <aside class="callout callout-abstract"> */
export default function remarkCallout() {
  return (tree) => {
    visit(tree, 'blockquote', (node) => {
      const first = node.children?.[0];
      if (first?.type !== 'paragraph') return;
      const text = first.children?.[0];
      if (text?.type !== 'text') return;
      const m = RE.exec(text.value.split('\n')[0]);
      if (!m) return;

      const [, kind, , label] = m;
      const rest = text.value.split('\n').slice(1).join('\n');
      text.value = rest;
      if (!rest) first.children.shift();
      if (!first.children.length) node.children.shift();

      node.data = {
        hName: 'aside',
        hProperties: { className: ['callout', `callout-${kind.toLowerCase()}`] },
      };
      node.children.unshift({
        type: 'paragraph',
        data: { hName: 'div', hProperties: { className: ['callout-title'] } },
        children: [{ type: 'text', value: label || kind }],
      });
    });
  };
}
```

- [ ] **Step 4: 接入 astro.config.mjs**

```javascript
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import remarkCallout from './src/plugins/remark-callout.mjs';

export default defineConfig({
  site: 'https://bryce505.github.io',
  base: '/blog',
  integrations: [sitemap()],
  markdown: {
    remarkPlugins: [remarkCallout],
    shikiConfig: { themes: { light: 'github-light', dark: 'github-dark' } },
  },
});
```

- [ ] **Step 5: 写样本文章验证 schema 与 callout**

`src/content/posts/_sample.md`：
```markdown
---
title: "样本文章"
date: 2026-08-24
category: "02分子表征"
primaryTag: "02分子表征/PTM/糖基化"
tags:
  - "02分子表征/PTM/糖基化"
references:
  - "Biophysical characterization of proteins"
sourceNotes:
  - "a.md"
---

## 一级小节

> [!abstract] 摘要
> 这是一个 callout，应渲染成带样式的 aside。

正文，流速 0.5 mL/min。
```

- [ ] **Step 6: 构建并确认 callout 渲染正确**

Run: `npm run build && grep -c 'class="callout callout-abstract"' dist/**/*.html`
Expected: 构建成功，grep 结果 ≥ 1

- [ ] **Step 7: 提交**

```bash
git add TechnicalBlog/package.json TechnicalBlog/package-lock.json TechnicalBlog/astro.config.mjs TechnicalBlog/tsconfig.json TechnicalBlog/src
git commit -m "TechnicalBlog: Astro 骨架、内容 schema 与 callout 渲染插件"
```

---

### Task 10: 视觉设计与文章页

**Files:**
- Create: `TechnicalBlog/src/styles/global.css`
- Create: `TechnicalBlog/src/layouts/Base.astro`、`TechnicalBlog/src/layouts/Post.astro`
- Create: `TechnicalBlog/src/components/Header.astro`、`Footer.astro`、`Toc.astro`、`PostCard.astro`
- Create: `TechnicalBlog/src/pages/index.astro`、`TechnicalBlog/src/pages/posts/[...slug].astro`

**Interfaces:**
- Consumes: Task 9 的 `posts` collection 与 callout class 名（`callout` / `callout-<kind>`）
- Produces: `Base.astro`（props: `title`, `description`）、`Post.astro`（props: `entry`）、CSS 变量令牌（`--bg --fg --muted --accent --border --code-bg`）

- [ ] **Step 1: 用 design 技能产出视觉稿**

调用 `design` 技能，输入：中文专业技术博客，面向生物医药 CMC/分析同行；需要首页、文章页两块画板；风格冷静克制、阅读优先；深浅色双主题。产出 `.dc.html` 画板后，从中提取配色令牌、字号阶梯、间距节奏，落到 `global.css` 的 CSS 变量。

- [ ] **Step 2: 写 global.css 的主题令牌**

三段式定义，保证深浅色都正确（浅色定义在裸 `:root`，深色在媒体查询与 `[data-theme]` 各定义一次）：
```css
:root {
  --bg: #ffffff; --fg: #1a1d21; --muted: #5b6470;
  --accent: #1f5f8b; --border: #e3e6ea; --code-bg: #f6f7f9;
  --measure: 42rem;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #14171a; --fg: #e6e9ec; --muted: #9aa4b0;
    --accent: #6fb3d9; --border: #2a2f35; --code-bg: #1c2024;
  }
}
:root[data-theme="dark"] {
  --bg: #14171a; --fg: #e6e9ec; --muted: #9aa4b0;
  --accent: #6fb3d9; --border: #2a2f35; --code-bg: #1c2024;
}
body { background: var(--bg); color: var(--fg); }
```

中文排版必须包含：`line-height: 1.85`、正文 `max-width: var(--measure)`、
`text-wrap: pretty`、中西文混排间距（`p { word-break: normal; overflow-wrap: break-word; }`）。

表格与代码块必须可横向滚动，页面本身不得横向滚动：
```css
.prose :is(table, pre) { display: block; max-width: 100%; overflow-x: auto; }
.prose img { max-width: 100%; height: auto; }
```

callout 样式对应插件产出的 class：
```css
.callout { border-left: 3px solid var(--accent); background: var(--code-bg);
           padding: .75rem 1rem; margin: 1.25rem 0; border-radius: 0 4px 4px 0; }
.callout-title { font-weight: 600; color: var(--accent); margin-bottom: .35rem; }
.callout-warning { --accent: #b8860b; }
.callout-summary, .callout-abstract { --accent: #1f5f8b; }
```

图注样式（`render.rewrite_images` 产出的是图片后紧跟一行斜体）：
```css
.prose img + em { display: block; text-align: center; font-size: .875rem;
                  color: var(--muted); font-style: normal; margin-top: .5rem; }
```

- [ ] **Step 3: 写 Base.astro 与 Post.astro**

`Base.astro` 承担 `<head>`、跳过导航链接、Header/Footer；`Post.astro` 渲染文章正文 + 目录 + 三个末尾区块（参考文献 / 延伸阅读 / 相关文章）。

`src/pages/posts/[...slug].astro`：
```astro
---
import { getCollection, render } from 'astro:content';
import Post from '../../layouts/Post.astro';

export async function getStaticPaths() {
  const posts = await getCollection('posts');
  return posts.map((entry) => ({ params: { slug: entry.id }, props: { entry } }));
}
const { entry } = Astro.props;
const { Content, headings } = await render(entry);
const all = await getCollection('posts');
const related = all
  .filter((p) => p.id !== entry.id &&
    p.data.tags.some((t) => entry.data.tags.some(
      (e) => t.split('/').slice(0, 2).join('/') === e.split('/').slice(0, 2).join('/'))))
  .slice(0, 5);
---
<Post entry={entry} headings={headings} related={related}>
  <Content />
</Post>
```

- [ ] **Step 4: 本地预览，逐项核对**

Run: `npm run build && npm run preview`
核对清单（逐条确认，任一不过则修）：
- [ ] 浅色主题正常
- [ ] 深色主题正常（浏览器切到 dark，且手动 `data-theme` 切换也生效）
- [ ] callout 有左边框和标题样式
- [ ] 图注为居中小字灰色
- [ ] 长表格横向滚动，页面本身不横向滚动
- [ ] 400px 窄屏下正文可读、不溢出

- [ ] **Step 5: 提交**

```bash
git add TechnicalBlog/src
git commit -m "TechnicalBlog: 站点视觉设计与文章页布局"
```

---

### Task 11: 分类、标签、归档、工具栏目

**Files:**
- Create: `TechnicalBlog/src/pages/category/[category].astro`
- Create: `TechnicalBlog/src/pages/tags/[tag].astro`
- Create: `TechnicalBlog/src/pages/archive.astro`
- Create: `TechnicalBlog/src/pages/tools.astro`
- Create: `TechnicalBlog/src/pages/about.astro`
- Create: `TechnicalBlog/src/pages/rss.xml.js`
- Delete: `TechnicalBlog/src/content/posts/_sample.md`

**Interfaces:**
- Consumes: Task 9 的 `posts` collection、Task 10 的 `Base.astro`、`PostCard.astro`
- Produces: 全部路由；`tools.astro` 读取 `category === '工具与效率'` 的文章

- [ ] **Step 1: 写分类页**

```astro
---
import { getCollection } from 'astro:content';
import Base from '../../layouts/Base.astro';
import PostCard from '../../components/PostCard.astro';

export async function getStaticPaths() {
  const posts = await getCollection('posts');
  const cats = [...new Set(posts.map((p) => p.data.category))];
  return cats.map((category) => ({
    params: { category },
    props: { posts: posts.filter((p) => p.data.category === category)
      .sort((a, b) => b.data.date - a.data.date) },
  }));
}
const { category } = Astro.params;
const { posts } = Astro.props;
// 按二级标签分区，复用笔记原有的分类树
const sections = new Map();
for (const p of posts) {
  const key = (p.data.primaryTag || '').split('/').slice(0, 2).join('/') || '其他';
  if (!sections.has(key)) sections.set(key, []);
  sections.get(key).push(p);
}
---
<Base title={category} description={`${category} 分类下的全部文章`}>
  <h1>{category}</h1>
  {[...sections].map(([name, items]) => (
    <section><h2>{name}</h2>{items.map((p) => <PostCard post={p} />)}</section>
  ))}
</Base>
```

- [ ] **Step 2: 写标签页、归档页、工具栏目、关于页、RSS**

标签页 `getStaticPaths` 展开 `posts.flatMap(p => p.data.tags)` 去重；归档页按年份分组；
`tools.astro` 过滤 `category === '工具与效率'`；`rss.xml.js` 用 `@astrojs/rss` 输出全部文章。

- [ ] **Step 3: 首页接上分类入口**

`index.astro` 列出最新 10 篇 + 全部一级分类入口（从 `posts` 的 `category` 去重得出，不硬编码分类名）。

- [ ] **Step 4: 删除样本文章并构建**

```bash
rm TechnicalBlog/src/content/posts/_sample.md
npm run build
```
Expected: 构建成功，无 404 链接。若因无文章导致空集合报错，先跑一次 Task 12 Step 4 的离线演练产出真实文章再构建。

- [ ] **Step 5: 提交**

```bash
git add -A TechnicalBlog/src
git commit -m "TechnicalBlog: 分类、标签、归档、工具栏目与 RSS"
```

---

### Task 12: GitHub Actions、离线演练与交付

**Files:**
- Create: `TechnicalBlog/.github/workflows/publish.yml`
- Create: `TechnicalBlog/.github/workflows/deploy.yml`
- Create: `TechnicalBlog/README.md`

**Interfaces:**
- Consumes: `pipeline/main.py` 的 CLI（`--vault --blog --count --drafts`）
- Produces: 两个 workflow；Secrets 契约 `DEEPSEEK_API_KEY` / `VAULT_TOKEN` / `GDRIVE_SA_JSON`

- [ ] **Step 1: 写 publish.yml**

```yaml
name: publish
on:
  schedule:
    - cron: '0 13 * * *'      # UTC 13:00 = 北京时间 21:00
  push:
    paths: ['drafts/**']
  workflow_dispatch:
    inputs:
      count:
        description: 本次发布篇数
        default: '1'

permissions:
  contents: write

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/checkout@v4
        with:
          repository: Bryce505/Obsidian-base
          token: ${{ secrets.VAULT_TOKEN }}
          path: .vault
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install -r pipeline/requirements.txt

      - name: 处理 drafts（两种触发都先跑）
        env:
          GDRIVE_SA_JSON: ${{ secrets.GDRIVE_SA_JSON }}
        run: python pipeline/main.py --drafts --blog . | tee -a report.json

      - name: 自动通道发文（仅定时与手动触发）
        if: github.event_name != 'push'
        env:
          DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
          GDRIVE_SA_JSON: ${{ secrets.GDRIVE_SA_JSON }}
        run: python pipeline/main.py --vault .vault --blog . --count ${{ github.event.inputs.count || 1 }} | tee -a report.json

      - name: 提交产出
        run: |
          rm -rf .vault
          git config user.name  'blog-bot'
          git config user.email 'makejun505@gmail.com'
          git add src/content/posts public/images published.json pipeline/drive_index.json _review 2>/dev/null || true
          git diff --staged --quiet || git commit -m "自动发布：$(date -u +%Y-%m-%d)"
          git push

      - uses: actions/upload-artifact@v4
        if: always()
        with: { name: run-report, path: report.json }
```

- [ ] **Step 2: 写 deploy.yml**

```yaml
name: deploy
on:
  push:
    branches: [master]
    paths-ignore: ['drafts/**', 'pipeline/**', 'docs/**']
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write
concurrency: { group: pages, cancel-in-progress: true }

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: npm }
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with: { path: dist }
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: { name: github-pages, url: '${{ steps.d.outputs.page_url }}' }
    steps:
      - id: d
        uses: actions/deploy-pages@v4
```

- [ ] **Step 3: 写 README.md**

必须写清四件事：三个 Secrets 怎么配（含**把 Drive 的 `image&attachment` 文件夹共享给服务账号邮箱**这一步，漏了就是取图全失败）；手动发布怎么用；`_review/` 里的文章怎么人工放行；怎么手动补发一篇。

- [ ] **Step 4: 离线全流程演练（接 Actions 前必须做）**

在本地用真实 vault 与真实 API key 跑三个组：
```bash
cd TechnicalBlog
export DEEPSEEK_API_KEY=... GDRIVE_SA_JSON="$(cat sa.json)"
python pipeline/main.py --vault /home/user/obsidian-base --blog . --count 3
```
逐项确认：
- [ ] 三篇文章落到 `src/content/posts/`，或落到 `_review/` 且失败原因合理
- [ ] `public/images/<slug>/` 下有 WebP，尺寸 ≤1200px
- [ ] **人工通读三篇**：结构确实做了重组而非拼接；数字、法规条款号、图片一个不少
- [ ] `published.json` 记录正确，重跑一次不会重复发布同一组

- [ ] **Step 5: 建仓库并首次推送**

```bash
cd /home/user/CodeSpace
git subtree split --prefix=TechnicalBlog -b technicalblog-extracted
git push https://github.com/Bryce505/blog.git technicalblog-extracted:master
```
然后在 GitHub 仓库设置里：Settings → Pages → Source 选 **GitHub Actions**；Settings → Secrets 加三个 Secret。

- [ ] **Step 6: 手动触发验证**

在 Actions 页面手动跑一次 `publish`，确认凭据全部有效、站点可访问。
再往 `drafts/` 扔一篇含 Drive 图片和双链的真实 md，push 后确认图片显示、双链解析、文章上线。

- [ ] **Step 7: 提交**

```bash
git add TechnicalBlog/.github TechnicalBlog/README.md
git commit -m "TechnicalBlog: GitHub Actions 工作流与使用说明"
```

---

## 交付验收

全部满足才算完成：

1. `python pipeline/test_pipeline.py` 全绿，其中 verify 的 5 个负向用例必须真的拦得住（改数字、删图、丢条款、截断、AI 导读句不误报）
2. 离线演练 3 篇，人工通读确认结构重组质量与事实保真
3. `npm run build` 通过；深浅色主题、中文排版、callout、图注、窄屏均正确
4. `Bryce505/blog` 建好，两个 workflow 就位，三个 Secrets 配齐
5. 手动触发 `publish` 跑通，站点可访问
6. `drafts/` 投递一篇真实 md，图片与双链正确
7. `README.md` 写明配凭据、手动发布、`_review/` 放行、手动补发
