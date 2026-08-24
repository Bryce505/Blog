# 技术博客自动发布流水线 — 设计文档

日期：2026-08-24
状态：待评审
分支：`claude/tech-blog-sync-architecture-8bcvq2`

## 1. 背景与目标

把 Obsidian 知识库里已有的原创笔记，自动整理成结构完整的中文技术文章，定时发布到公开博客。

**核心约束**：内容是生物医药 CMC / 分析方法领域，充满具体参数、法规条款号、实验条件。AI 改写这类内容一旦出错，是专业性错误而非排版问题。因此整条流水线的第一优先级是**事实不被篡改**，第二才是文章好读。

**不是要做什么**：不做知识库同步工具，不做 CMS，不做搜索后端，不做双向同步。只做"选题 → 取图 → 整理 → 校验 → 发布"这一条单向流水线。

## 2. 决策记录

| 决策项 | 结论 | 理由 |
|---|---|---|
| 数据源 | 仅 `Bryce505/Obsidian-base`（226 篇可发布原创笔记）+ `Bryce505/RoutineRun` 的 5 篇（独立栏目） | RoutineRun 285 个 md 中 269 个是 `.claude/skills` 配置，不是笔记 |
| Clippings 处理 | 排除正文，仅在同标签文章末尾生成「延伸阅读」（标题 + 原文链接） | 359 篇是他人公众号全文，公开转载侵权 |
| 文献/书籍插图 | 发布，强制标注出处 | 用户决策；图注自动从 frontmatter 的 `book`/`paper`/`link` 拼出 |
| 分组粒度 | 三级标签为主分组单位；三级及以上的碎组回退到「恰好二级」合并，二级碎组丢弃 | 实测（实现后）：33 个合格组覆盖 224 篇可发布笔记中的 198 篇（88%） |
| AI 改写力度 | 方案 C：结构重组成一篇文章，但含数字/引文/图片引用的句子原样保留 + 机械校验兜底 | 兼顾可读性与事实安全 |
| LLM | DeepSeek `deepseek-chat` | 整理任务够用；比 `deepseek-reasoner` 快且便宜一个量级 |
| 图片来源 | Google Drive `image&attachment`（folder id `1jwf_lkCo-Rq42VwWToyTeu2ciJTRg4zT`） | 唯一网络可达的完整副本 |
| 图片托管 | 构建时抓取 → 转 WebP → 提交进博客仓库自托管 | Drive 直链有限流、会失效，不能当图床 |
| SSG | Astro | 组件接近纯 HTML/CSS，设计稿落地成本最低 |
| 部署 | GitHub Pages | 用户决策 |
| 仓库 | `Bryce505/blog` 单仓库（流水线 + 站点 + 文章 + 图片） | 拆两个仓库要多配跨仓库 token，无收益 |
| 调度 | GitHub Actions cron，每晚 21:00 北京时间（UTC `0 13 * * *`） | 用户决策 |
| 站点定位 | 中文专业技术博客，面向生物医药 CMC/分析同行 | 用户决策 |
| 手动发布 | `drafts/` 目录，扔进去 push 即发；复用取图和双链解析，跳过 AI 和校验 | 用户决策；自己写的稿子不需要防 AI 篡改 |

## 3. 数据源实测数据

以下数字由脚本实测得出，不是估算，实现时可用作回归基准。

**Obsidian-base**（私有仓库，master 分支，2535 个文件）

- md 总数 1602；**可发布原创笔记 226 篇**
- 排除目录：`Clippings` `Backup` `tmp` `script` `Inbox-待处理` `Excalidraw` `docs` `.claude` `Obsidian`
- 可发布 `type` 白名单：`note` `sci-note` `book-note` `综述` `lit-review` `reference` `regulatory-strategy` `项目报告` `实验` `reference-table`
- frontmatter 字段：`tags` `type` `description` `keywords` `dateCreated` `dateUpdated` `aliases` `status` `title` `book` `paper` `link`
- 标签体系（数字编号分类树，直接用作站点导航）：

  | 一级标签 | 笔记数 |
  |---|---|
  | `02分子表征` | 520 |
  | `05仪器与分析技术` | 446 |
  | `00基础` | 299 |
  | `03质量控制` | 249 |
  | `14编程与软件` | 218 |
  | `07注册与法规` | 169 |
  | `04抗体设计与筛选` | 74 |
  | `06工艺` | 40 |
  | `02成药性` | 26 |
  | `08安全性评价` | 14 |

- 三级标签分组（**实现后实测，取代早期探索的虚高估算**）：**33 个合格组，覆盖 198 篇（88%）**，其中三级标签组 18 个、二级回退组 15 个

  > 早期探索脚本得出的「52 组」是错的：它把一篇笔记计入其拥有的每一个标签组，组间严重重叠、容量被虚高撑大。实际规则是一篇笔记只归一组（否则同一段内容会出现在多篇文章里），因此组数少得多。
- 图片：本地引用去重 **1235 张**（平均每篇 5.5 张），外链 67 张
- Obsidian 语法：callout `>[!xxx]` **545 处**，双链 `[[...]]` **719 处**

**RoutineRun**（私有仓库）：真笔记 5 篇 —— `git&github/笔记.md`、`git&github/README.md`、`PPT制作/README.md`、`翻译/README.md`、`docs/claude-code-cloud-notes.md`

**图片体量**：1235 张原图约 494 MB；限宽 1200px 转 WebP（quality 82）后约 74 MB，且随发布进度逐步增长，git 仓库可承受。

## 4. 架构与数据流

```
Obsidian-base (私有) ─┐
RoutineRun   (私有) ─┤ ① select.py  三级标签分组 → 查 published.json 去重 → 输出 1 个待发组
                     │      ↓
Google Drive ────────┤ ② images.py  按文件名查 Drive → 下载 → WebP(≤1200px) → public/images/
image&attachment     │      ↓
                     │ ③ compose.py DeepSeek 结构重组 → 一篇 markdown
                     │      ↓
                     │ ④ verify.py  机械校验（图片完整性 + 数字未篡改 + 引文完整）
                     │      ↓ 通过                    ↓ 不通过
                     │ ⑤ 写 src/content/posts/     写 _review/ 待人工复核
                     │   更新 published.json
                     │   commit + push
                     └──────↓
                       ⑥ Astro build → GitHub Pages
```

每次运行只发一篇（`--count` 可调）。52 个合格组可稳定发约两个月。

## 5. 仓库结构

```
blog/
├─ .github/workflows/
│   ├─ publish.yml            # cron 0 13 * * *：跑流水线，提交结果
│   └─ deploy.yml             # push 触发：Astro build → Pages
├─ pipeline/                  # Python，独立 venv（uv）
│   ├─ requirements.txt
│   ├─ config.py              # 常量：排除目录、type 白名单、分组阈值
│   ├─ vault.py               # 笔记解析：frontmatter、正文、图片引用、双链
│   ├─ select.py              # 分组选题 + 去重
│   ├─ images.py              # Drive 取图 + WebP 转换
│   ├─ compose.py             # DeepSeek 调用
│   ├─ verify.py              # 机械校验
│   ├─ main.py                # 串起 ①→⑤；--drafts 走手动发布通道
│   └─ test_pipeline.py       # 自检（含故意注入错误的校验用例）
├─ src/                       # Astro
│   ├─ content/posts/         # 生成的文章（md）
│   ├─ layouts/  components/  pages/  styles/
│   └─ plugins/remark-callout.js
├─ drafts/                    # 手动发布投递口：扔 md 进来，push 即发
├─ public/images/<slug>/      # WebP 图片
├─ published.json             # 发布状态
└─ astro.config.mjs
```

## 6. 模块设计

### 6.1 `vault.py` — 笔记解析

单一职责：把一个 md 文件解析成结构化对象，不做任何业务判断。

```python
Note = namedtuple('Note', 'path title tags type description book paper link body images wikilinks')
```

- frontmatter 用 `PyYAML` 解析；解析失败的笔记记录警告并跳过，不中断整批
- `images`：正文里 `![](path)` 和 `![[path]]` 两种写法都抓，路径 URL-decode 后取 basename
- `wikilinks`：`[[目标]]` 和 `[[目标|显示名]]` 都抓

### 6.2 `select.py` — 选题

1. 遍历 vault，排除黑名单目录，按 `type` 白名单过滤 → 得到候选笔记
2. 按三级标签建组（`02分子表征/PTM/糖基化`）。一篇笔记常有多个标签，归属规则：取其 frontmatter `tags` 数组中**出现顺序最靠前的、层级数 ≥3 的**标签；若无三级标签则取最靠前的二级标签。一篇笔记只属于一组，避免同一内容在多篇文章里重复出现
3. 组内笔记数 3~30 为合格组。**不足 3 篇且标签层级 ≥3 的碎组，降到「恰好二级」重新归并**；二级碎组不再降级（降到一级会得到「02分子表征」这种把整个领域当一篇文章的结果），合并后仍不足 3 篇的挂起不发。回退目标若已存在同名组则合并进去，不产生重名组——重名会导致两篇文章抢同一 slug、后者静默覆盖前者
4. 超过 30 篇的组（当前实测为 0，防御性处理）按 `dateUpdated` 倒序取前 30 篇
5. 查 `published.json`：跳过已发布且组内笔记内容哈希未变的组
6. 输出：按组内笔记数降序，取第一个未发布组

`published.json` 结构：

```json
{
  "02分子表征/PTM/糖基化": {
    "slug": "protein-glycosylation-characterization",
    "published_at": "2026-08-25",
    "source_hash": "sha256:...",
    "notes": ["Antibody-Characterization/xxx.md", "..."]
  }
}
```

`source_hash` 是组内所有笔记正文拼接后的哈希。笔记更新导致哈希变化时，该组进入"可重发"队列（生成新版本覆盖原文章，slug 不变，URL 稳定）。

### 6.3 `images.py` — 取图

1. 收集本组所有笔记引用的本地图片文件名（去重）
2. 通过 Drive API 在 `image&attachment` 下**递归**按文件名查找（`image-laptop` 是主力子目录，但不写死，遍历所有子目录建一次 `文件名 → fileId` 索引并缓存到 `pipeline/drive_index.json`，**该文件提交进仓库**，让每次 Actions 运行复用，避免每晚重新遍历整个 Drive 文件夹；内容只是文件名到 fileId 的映射，非敏感信息）
3. 下载 → Pillow 处理：限宽 1200px（等比，不放大）、转 WebP quality 82 → 存 `public/images/<slug>/<原名>.webp`
4. 已存在的文件跳过（幂等，重跑不重复下载）
5. **找不到的图**：不留破图。正文里该图片替换为一行斜体说明 `*[图缺失：<原文件名>]*`，并计入运行报告

图注生成：每张图后自动追加 `<figcaption>`，内容按优先级从笔记 frontmatter 取 `book` → `paper` → `link`，格式 `图源：《书名》` / `图源：<论文标题>` / `图源：<链接>`。三者皆空则不加图注。

### 6.4 `compose.py` — DeepSeek 整理

- 端点 `https://api.deepseek.com`（OpenAI 兼容），model `deepseek-chat`
- 系统提示固定不变（放最前面，多篇复用 prompt cache），内容包含：
  - 站点定位与语气：中文专业技术博客，面向生物医药 CMC/分析同行，术语保留英文原词，克制不煽情
  - **硬约束**：凡含数字、单位、法规条款号、文献引用、图片引用 `![...](...)` 的句子，必须原样逐字保留，不得改写、合并、换算单位
  - **结构重组要求**：不是按笔记顺序拼接，要打散重组出一条属于这篇文章自己的脉络（如"原理 → 方法 → 关键参数 → 常见问题"），允许调整段落顺序、合并重复论述、补写过渡句和导读
  - 不得引入源文中不存在的事实、数据或结论
- 用户消息：本组所有笔记的正文 + 各自的 `description`/`book`/`paper` 元信息
- 输出：文章 markdown（不含 frontmatter，frontmatter 由流水线拼装，避免 LLM 编造日期/标签）

### 6.5 `verify.py` — 机械校验（本项目最关键的代码）

对 LLM 输出做四项确定性检查，任一不过则不发布：

| 检查 | 规则 | 失败含义 |
|---|---|---|
| 图片完整性 | 源文中每个图片引用都必须在输出中出现 | AI 丢图 |
| 数字未篡改 | 输出中抽取的数字 token 集合必须是源文数字集合的子集 | AI 编造或改动了数据 |
| 引文完整性 | 源文中的 DOI、法规条款号（如 `ICH Q6B`、`21 CFR 211.x`）必须全部保留 | AI 丢失或改错法规依据 |
| 长度合理性 | 输出正文不短于源文总字数的 40% | AI 大段丢失内容 |

数字 token 抽取规则 —— **只检查承载数据的数字**，避免误杀 AI 写的导读句：

只有满足以下任一条件的数字才纳入比对：
- 带单位或百分号（`50 mM`、`4.6 mm`、`95%`、`25 °C`）
- 含小数点（`0.45`、`7.4`）
- 三位及以上整数（`1200`、`280`）

裸露的一两位整数（"本文涉及 3 个方面"、"分为 2 类"）**不纳入检查** —— 这类数字是行文措辞，AI 重组时必然会产生新的，纳入检查等于让校验器天天误报。

比对方向：归一化空格后，输出的数字集合必须是源文数字集合的**子集**。允许**变少**（重组时删掉重复论述是正常的），不允许**出现新的**。

校验不通过的文章写入 `_review/<slug>.md` 并附一份差异报告，不进 `src/content/posts/`，不更新 `published.json`。人工看过后手动移入即可发布。

### 6.6 Obsidian 语法转换

分两处，各司其职：

- **流水线内（Python）**：双链 `[[目标]]` 解析 —— 目标笔记已发布则转**文章级**站内链接 `[显示名](/posts/<slug>)`，未发布则退化为纯文本（保留文字，去掉方括号），**不留死链**

  注意不做章节级锚点：既然采用结构重组（方案 C），源笔记打散后不再对应输出文章里的某个独立章节，锚点无从推导。链到文章即可。
- **Astro 构建时（remark 插件）**：callout `>[!abstract]` / `>[!summary]` / `>[!note]` / `>[!warning]` 等转成带样式的 `<aside class="callout callout-abstract">`。一个插件处理全站 545 处，不在流水线里逐篇转

### 6.8 手动发布通道

给自己留的口子：写好的 md 扔进仓库根的 `drafts/`，push 上去就发布。

**为什么不是直接扔进 `src/content/posts/`**：直接扔当然也能发，但从 Obsidian 导出的稿子里图片写的是 `![](../image&attachment/xxx.png)`，双链写的是 `[[目标笔记]]`，直接发出去是一堆破图和方括号。手动通道复用流水线已有的 `images.py` 和双链解析，把这两件事替你办了。

**处理流程**（`main.py --drafts`）：

1. 扫 `drafts/*.md`
2. 取图：复用 `images.py`，从 Drive 拉图转 WebP（和自动通道完全同一套代码）
3. 双链解析：`[[目标]]` 已发布转站内链接，未发布退化成纯文本
4. 补全 frontmatter 默认值（见下）
5. 写入 `src/content/posts/<slug>.md`，删除 `drafts/` 中的原件（避免重复处理）

**不经过 DeepSeek，不经过 `verify.py`** —— 你自己写的内容不需要防篡改校验，跑一遍纯属浪费时间和 token。

**frontmatter 最小要求：只需要 `title` 一个字段**，其余全部有默认值，手写时不用记一堆字段名：

| 字段 | 缺省行为 |
|---|---|
| `title` | **必填**，缺失则跳过该文件并在运行报告里报错 |
| `slug` | 由文件名生成（中文转拼音，去特殊字符） |
| `date` | 该文件的 git 首次提交时间，取不到则用当天 |
| `tags` | 空数组 |
| `category` | 从 `tags` 的一级标签推导；无标签则归入「杂记」 |
| `description` | 取正文前 120 字 |

**触发方式**：`publish.yml` 增加 `on.push.paths: ['drafts/**']`。同一个 workflow，两种触发：

- push 到 `drafts/` → 只跑 `--drafts`
- 每晚 21:00 定时 / 手动 dispatch → 先跑 `--drafts`（清理积压），再跑自动通道发一篇

**与自动通道的隔离**：`published.json` 以三级标签组为键，手动文章不写入其中，两条通道各走各的，不会互相覆盖或重复发布。若手动文章的 slug 与已有文章冲突，报错跳过，不静默覆盖。

### 6.7 站点结构

| 路由 | 内容 |
|---|---|
| `/` | 站点简介 + 最新文章 + 10 个一级分类入口 |
| `/category/[一级标签]` | 该领域下的文章列表（按二级标签分区） |
| `/posts/[slug]` | 文章页：目录侧栏、正文、图注、参考文献、延伸阅读、相关文章 |
| `/tags/[tag]` | 标签聚合页 |
| `/archive` | 按时间归档 |
| `/tools` | 工具与效率栏目（RoutineRun 的 5 篇） |
| `/about` | 关于 |

文章页三个末尾区块，来源各不相同：

- **参考文献**：组内笔记 frontmatter 的 `book` / `paper` / `link` 去重汇总
- **延伸阅读**：同二级标签下的 Clippings 笔记，仅标题 + 原文链接，不含任何原文内容
- **相关文章**：同二级标签下已发布的其他文章

视觉设计在实施阶段用 `design` 技能产出，本文档不预先约束具体配色和排版。设计原则：阅读优先、冷静克制、中文正文排版（行高、标点挤压、中西文混排间距）、代码与表格可横向滚动、深浅色主题都要正确。

## 7. GitHub Actions

**`publish.yml`** — `cron: '0 13 * * *'`（UTC 13:00 = 北京时间 21:00）

```
checkout blog → 用 PAT checkout Obsidian-base + RoutineRun 到临时目录
→ uv venv + 装依赖 → python pipeline/main.py --count 1
→ 有产出则 commit + push（push 自动触发 deploy.yml）
→ 上传运行报告为 artifact（缺图、校验失败等）
```

同时保留 `workflow_dispatch` 手动触发，便于调试。

**`deploy.yml`** — push 到 master 触发：`astro build` → `actions/deploy-pages`

## 8. 需要准备的凭据

**两个源仓库都是私有的**（已通过 GitHub API 确认），所以 Actions 必须配 token 才能读取。

| Secret 名 | 内容 | 怎么拿 |
|---|---|---|
| `DEEPSEEK_API_KEY` | DeepSeek API key | platform.deepseek.com 控制台创建 |
| `VAULT_TOKEN` | GitHub PAT，只读 `Obsidian-base` 和 `RoutineRun` | GitHub Settings → Developer settings → Fine-grained PAT，仅勾选这两个仓库的 Contents: Read |
| `GDRIVE_SA_JSON` | Google 服务账号 JSON | GCP 控制台建服务账号 → 下载 JSON key → **把 `image&attachment` 文件夹共享给该服务账号邮箱（查看者权限）** |

最后一步（共享文件夹给服务账号）最容易漏，漏了就是取图全失败。

## 9. 测试策略

**不接 Actions 之前，先在本地跑通全流程。** 顺序如下：

1. **单元自检** `test_pipeline.py`（assert 驱动，不引入测试框架）：
   - `vault.py` 能正确解析真实笔记的 frontmatter、图片引用、双链
   - `select.py` 在实测数据上产出 52 个合格组（回归基准，数字变了说明逻辑漂移）
   - **`verify.py` 的负向用例**：拿一篇真实文章，程序化地把某个数字改错、删掉一张图、去掉一个法规条款号，断言校验**必须失败**。这是整套代码里最重要的测试 —— 校验器拦不住错误就等于没有校验器
2. **离线全流程演练**：选 3 个真实标签组跑 ①→④，人工通读三篇输出，确认结构重组质量和事实保真度
3. **Astro 本地构建**：`astro build` 通过，本地预览检查中文排版、callout 样式、图注、深浅色主题
4. 以上全过，才接 GitHub Actions，并先用 `workflow_dispatch` 手动跑一次验证凭据

## 10. 明确不做（YAGNI）

- **不做 RAG / 向量检索选题**：三级标签是用户手工策展的关联关系，比 embedding 聚类更准，且零额外基础设施
- **不做第二条取图路径**：`Bryce505/image` 公开仓库有 371 张（30%）重合图片，但为省 20MB 增加一条分支和一种失败模式不划算。若将来仓库体积成问题再议
- **不做评论系统、搜索后端、CMS、中英双语**
- **不做 webhook 即时触发**：定时轮询够用，跨仓库 `repository_dispatch` 多一层复杂度
- **不做 Drive 双向同步**：Drive 只作为图片只读源

## 11. 已知风险与限制

| 风险 | 影响 | 应对 |
|---|---|---|
| DeepSeek 上下文超限 | 30 篇笔记的组可能超出 64K 上下文 | 组内按 `dateUpdated` 截断到 30 篇；实测当前最大组 29 篇，暂时安全 |
| 校验器误杀 | 正常重组也可能触发数字子集检查 | 失败不丢弃，进 `_review/` 人工复核 |
| Drive 索引过期 | 用户在 Drive 里改名/移动图片 | `.drive_index.json` 设 7 天过期，过期重建 |
| 文献插图版权 | 已标注出处但仍非授权使用 | 用户已知悉并决策；若收到异议，删图成本低（图片独立存放于 `public/images/<slug>/`） |
| 私有 vault 内容误发 | 笔记里可能有未公开的项目信息 | `type` 白名单 + 目录黑名单双重过滤；首批文章人工通读 |

## 12. 交付定义

以下全部满足才算完成：

1. `pipeline/` 全部模块 + `test_pipeline.py` 自检通过（含校验器负向用例）
2. 本地离线跑通 3 个标签组，人工确认输出质量
3. Astro 站点本地构建通过，深浅色主题、中文排版、callout、图注均正确
4. `Bryce505/blog` 仓库建好，两个 workflow 就位
5. `workflow_dispatch` 手动跑通一次，站点可访问
6. **手动发布通道验证**：往 `drafts/` 扔一篇含 Drive 图片和双链的真实 md，push 后确认图片正常显示、双链正确解析、文章上线
7. `README.md` 写明如何配凭据、如何手动发布、如何补发、校验失败怎么处理
