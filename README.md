# 表征笔记

把 Obsidian 知识库里的原创笔记，按主题自动整理成技术文章，定时发布到
GitHub Pages。

## 目录

- [这是什么](#这是什么)
- [架构总览](#架构总览)
- [仓库目录结构](#仓库目录结构)
- [快速上手](#快速上手)
- [内容流水线](#内容流水线)
- [校验器](#校验器)
- [日常使用](#日常使用)
- [首次部署](#首次部署)
- [开发规范](#开发规范)
- [延伸阅读](#延伸阅读)

## 这是什么

**这是仓库所有者个人的内容自动化系统，不是通用博客框架。** 它把一个私有
Obsidian 知识库里的生物医药 CMC（化学、生产与控制）与分析方法笔记，通过
LLM 整理成结构完整的中文技术文章，经机械校验后定时发布到 GitHub Pages。

面向的读者是生物医药 CMC / 分析方法的同行，不是泛读者——这决定了流水线
的第一优先级：**内容是专业内容，一个流速、一条法规条款号被 AI 改错是
专业性错误，不是排版问题**。校验器（[`pipeline/verify.py`](pipeline/verify.py)）
因此是整条流水线里最关键的代码，细节见「[校验器](#校验器)」一节。

| | |
|---|---|
| **站点** | https://bryce505.github.io/Blog |
| **数据源** | `Bryce505/Obsidian-base`（生物医药 CMC 与分析方法笔记，私有）、`Bryce505/RoutineRun`（工具与效率栏目，私有） |
| **图片** | Google Drive `image&attachment` 文件夹，取下来转 WebP 自托管 |
| **整理模型** | DeepSeek（当前默认见 [`pipeline/config.py`](pipeline/config.py) 的 `DEEPSEEK_MODEL`，写这份文档时是 `deepseek-v4-flash`） |
| **发布节奏** | 每晚 21:00（北京时间）自动发一篇；`drafts/` 推送即时处理 |
| **托管与调度** | GitHub Pages + GitHub Actions（定时 / 手动 / push 触发） |

## 架构总览

```
                ┌─ Bryce505/Obsidian-base（私有，CMC/分析笔记）
       数据源 ──┤
                └─ Bryce505/RoutineRun（私有，工具与效率笔记）
                         │
                         │  GitHub Actions（publish.yml：定时 / 手动 / drafts 推送触发）
                         ▼
                  pipeline/ 五步走：选材 → 取图 → 整理 → 校验 → 落盘
                         │
                         ▼
       src/content/posts/<slug>.md —— 校验过与没过都写这里
       校验没过 → 额外带 frontmatter `draft: true` + `reviewNotes`
                （published.json 自动对账、写日志、开 issue / 发邮件）
                         │
                         ▼
              git push → GitHub Actions（deploy.yml）
                         │
                         ▼
   npm run build（Astro，`listPosts()` 排除 draft）→ GitHub Pages
                         │
                         ▼
              https://bryce505.github.io/Blog

   放行：删掉 draft: true 那一行，提交 → 下次构建即上线（见「校验器」）
```

**为什么是单仓库**：流水线只读两个私有笔记仓库、只写这一个仓库。拆成
「流水线仓库」与「站点仓库」两个，只是多配一层跨仓库 token；而流水线的
产出（文章、图片、发布状态）本来就要长期存在于这个仓库里，拆分没有收益。

### 技术栈

| 层 | 技术 | 说明 |
|---|---|---|
| 内容流水线 | Python 3.11+ | 零测试框架依赖，`assert` + `pipeline/test_pipeline.py` 自检 |
| 整理模型 | DeepSeek API | OpenAI 兼容接口，见 `pipeline/compose.py` |
| 图片处理 | Pillow | Drive 原图 → 限宽 1200px WebP |
| 数据源接入 | google-api-python-client / google-auth | 只读 Google Drive |
| 站点 | Astro 7（静态生成，无客户端框架） | |
| 数学公式 | KaTeX（`remark-math` / `rehype-katex`） | 实测待发布内容含 648 处 LaTeX |
| 图表 | Mermaid（自定义 remark 插件） | |
| 代码高亮 | Shiki（`github-light` / `github-dark` 双主题） | |
| SEO / 订阅 | `@astrojs/sitemap` + 自定义 `src/pages/rss.xml.js` | |
| CI/CD | GitHub Actions | 三个 workflow，见下表 |
| 托管 | GitHub Pages | |

### 三个 workflow

| workflow | 触发方式 | 做什么 |
|---|---|---|
| [`publish.yml`](.github/workflows/publish.yml) | 定时（每晚 UTC 13:00）/ `workflow_dispatch` / push 到 `drafts/**` | 跑内容流水线，产出通过就 commit + push |
| [`deploy.yml`](.github/workflows/deploy.yml) | push 到 `master`（忽略 `drafts/` `pipeline/` `docs/` `design/` `README.md` 等不影响构建产物的路径）/ `publish` 运行完 / `workflow_dispatch` | `npm run build` → 部署到 GitHub Pages |
| [`sample.yml`](.github/workflows/sample.yml) | 仅 `workflow_dispatch` | 引子通道试运行，产出一律带 `draft: true`，不传 `--publish`——不存在自动上线的可能，试验性质 |

> **GitHub 的坑**：workflow 用内置 `GITHUB_TOKEN` 推的提交不会触发其他
> workflow 的 `push` 事件（防递归安全规则），所以 `deploy.yml` 额外监听
> `publish` 的 `workflow_run` 事件——否则每晚发的文章会一直躺在仓库里不上线。

## 仓库目录结构

```
Blog/
├─ .github/workflows/        publish · deploy · sample 三个 workflow
├─ .claude/                  Claude Code 技能包与项目设置（brainstorming / TDD / 分支管理等）
├─ pipeline/                  Python 内容流水线
│  ├─ main.py                  入口：串起 选材→取图→整理→校验→落盘，见「内容流水线」
│  ├─ config.py                 全局常量：过滤范围、分组阈值、图片别名、模型 ID
│  ├─ vault.py                  Obsidian 笔记解析（frontmatter / 正文 / 图片引用 / 双链）
│  ├─ select_.py                自动通道：按标签分组选题
│  ├─ seed.py                   引子通道：单篇笔记按加减法整理
│  ├─ manual.py                 人工投稿通道：drafts/ 复用引子通道的加减法与校验
│  ├─ drafts.py                 手动发布通道：drafts/ → 取图 + 双链解析，不经过 AI
│  ├─ routinerun.py             工具与效率栏目：接 RoutineRun 笔记
│  ├─ repair.py                  补图通道 + `--audit-images` 图片体检
│  ├─ compose.py                调 DeepSeek 把笔记整理成文章
│  ├─ verify.py                  机械校验器——整条流水线最关键的代码
│  ├─ evidence.py               核验引子通道「依据与出处」标注是否编造
│  ├─ images.py                 Google Drive 取图 → WebP 转换
│  ├─ render.py                  Obsidian 语法 → 站点 markdown
│  ├─ notify.py                  校验未通过时写日志 / 开 issue / 发邮件
│  ├─ prompt.md / prompt_seed.md  两条通道各自的系统提示词
│  ├─ test_pipeline.py           自检：assert + 文件底部 runner，零依赖
│  ├─ fixtures/                  自检用的样本笔记，不依赖真实 vault
│  ├─ requirements.txt
│  └─ drive_index.json           Drive 文件名 → fileId 索引缓存（提交进仓库，非敏感）
├─ src/                        Astro 站点
│  ├─ content/posts/            流水线产出的文章（.md）——校验没过的也在这里，
│  │                            只靠 frontmatter 的 `draft: true` 区分
│  │                            （见「[校验器](#校验器)」）
│  ├─ content/series.json       系列栏目的归属与顺序，唯一真相来源
│  ├─ content.config.ts         posts / series 两个 collection 的 zod schema
│  ├─ layouts/                  Base（全局骨架）/ Post（文章页）
│  ├─ components/               Header / Footer / PostCard
│  ├─ pages/                    路由：index / archive / category / posts / series / tags / tools / about / rss.xml
│  ├─ lib/posts.ts              `listPosts()`——全站唯一的文章入口，草稿过滤只在这一处
│  ├─ lib/series.ts             系列解析、上下篇计算
│  ├─ plugins/                  自定义 remark 插件（callout / 高亮 / mermaid / base path 补全）
│  └─ styles/global.css
├─ public/images/<slug>/      文章配图（WebP），按文章分目录
├─ drafts/                     人工投稿投递口：放 md（+ images/ 子目录）push 即发布
├─ logs/                       按月归档的校验运行日志（`verify-YYYY-MM.md`）
├─ docs/
│  ├─ devlog/                   开发日志，每次改动必写，见「开发规范」
│  └─ superpowers/specs·plans/  设计文档与实施计划
├─ design/                     视觉设计源文件（Claude Design 画布 `.dc.html`）
├─ published.json              发布状态账本：按 slug 记录，每次运行自动跟 posts/ 对账
├─ site.config.mjs             站点地址与 base path 的唯一来源
├─ astro.config.mjs            Astro 配置：remark/rehype 插件挂载
├─ obsidian-publish-pipeline.html  最早期的架构探索稿，历史参考，非当前实现
├─ CLAUDE.md                   开发约定：分支、日志、代码规范
└─ README.md                   本文件
```

## 快速上手

### 前置要求

- Python 3.11+（推荐用 [uv](https://github.com/astral-sh/uv) 管理虚拟环境，也可以用标准 `venv` + `pip`）
- Node.js 22+

**不需要真实的 Obsidian vault、DeepSeek key 或 Google 服务账号就能跑通下面
两步**——流水线自检用的是 `pipeline/fixtures/` 里的样本数据，Astro 本地
开发/构建读的是已经发布的 `src/content/posts/`。真要接入真实数据源发布
新文章，见「[首次部署](#首次部署)」。

### 跑通流水线自检

```bash
uv venv && uv pip install -r pipeline/requirements.txt
.venv/bin/python pipeline/test_pipeline.py
```

跑完终端会打印 `通过数/总数`（写这份文档时是 128/128；这个数字会随新增
自检增长，**以终端实际输出为准**，不要以本文的数字为准）。这套自检不
引入测试框架，纯 `assert` + 文件底部的 runner，CI 里直接
`python pipeline/test_pipeline.py` 就能跑。

### 本地跑站点

```bash
npm install
npm run dev      # 本地预览，默认 http://localhost:4321
npm run build    # 构建到 dist/，验证 Astro 页面能否正确生成
```

### 改了流水线代码之后

按 [`CLAUDE.md`](CLAUDE.md) 的要求，合并前 `pipeline/test_pipeline.py` 必须
全绿、`npm run build` 通过；动了流水线**行为**的还要在分支上找一组真实
数据实跑一次（需要真实密钥，见「[首次部署](#首次部署)」）。

## 内容流水线

设计文档见 [`docs/superpowers/specs/`](docs/superpowers/specs/)，实施计划见
[`docs/superpowers/plans/`](docs/superpowers/plans/)。

```
Obsidian-base ─┐ ① 选材：挑一篇没用过的笔记当引子
drafts/       ─┤ ② 加减法：笔记够完整→浓缩归纳；不完整→补齐并标注来源
Google Drive  ─┤ ③ 取图：本地图 / Drive → WebP(≤1200px) → public/images/
               │ ④ 校验：数据保真 + 可发表性两组检查（见「校验器」）
               │      过 → 写 src/content/posts/ + 记账 + push
               │      不过 → 同样写 src/content/posts/，但带 `draft: true`
               │             （站点构建跳过），写日志、开 issue、发邮件
               └─↓
                 ⑤ Astro build → GitHub Pages
```

### 加减法原则

一篇笔记做引子，按它自身的完整度决定怎么做：

| 模式 | 触发条件 | 做什么 | 篇幅约束 |
|---|---|---|---|
| **减法** | 笔记 ≥ 12,000 字符 | 不改原意地浓缩、归纳、调整表述，**不新增实质内容** | 原文的 55%～95% |
| **加法** | 笔记 < 12,000 字符 | 补主题本身缺的环节（原理、脉络、边界、误区），紧贴主题不过度延伸 | 原文的 105%～300% |

**加法补的每一处重要内容都必须标注来源**，格式固定，机器逐条核验：

```markdown
覆盖率不足会系统性低估 HCP 残留水平[依据 1]。

## 依据与出处

1. 笔记：`Antibody-Characterization/HCP/HCP样品前处理流程.md` —— 引用要点：亲和富集会同时富集与抗体结合的 HCP
2. 文献：DOI:10.1016/j.ab.2004.08.008 —— 引用要点：NTCB 在 C 端侧断裂
```

来源优先级：**同一知识库的相关笔记**（加法模式下流水线会自动挑最多 6 篇
同主题笔记随提示词一起喂给模型）→ **引子笔记里已出现过的文献** → 没有
就不写。凡是含数字、单位、法规条款号、文献引用、图片引用的句子，一律
原样保留。

### 五条通道

| 通道 | 触发 | 做什么 |
|---|---|---|
| **引子** | 每晚 21:00 / 手动 | 从知识库挑笔记做引子，加减法整理成文章 |
| **人工投稿** | 往 `drafts/` 推稿子 / 手动 | 自己写的稿子走同一套加减法与校验 |
| **工具与效率** | 每次运行 | 把 RoutineRun 的工作笔记接成栏目 |
| **补图** | 每次运行 | 给已发布文章补取当时没取到的图 |
| **多篇重组**（旧） | 手动选 `auto` | 按标签组把多篇笔记重组成一篇。产出拼接感强，已不作为默认 |

## 校验器

`pipeline/verify.py` 是这条流水线的安全阀。内容是生物医药 CMC 与分析方法，
AI 把某个流速、某条法规编号改错了是专业性错误而不是排版问题——**校验拦
不住篡改，这条流水线就不该上线。**

> **workflow 显示成功 ≠ 文章发布了。** 这条流水线是「失败关闭」设计：
> 校验不过的文章照样写进 `src/content/posts/`，只是带 `draft: true`——
> 不会让 workflow 报错，也不会自己上线（构建时 `listPosts()` 会排除它，
> 见「[校验没过怎么办](#校验没过怎么办)」）。判断"今晚有没有真的发新
> 文章"，看新提交的文章有没有带 `draft: true`，或者 `published.json`
> 里的记录是否新增——光看 Actions 的绿勾会误判，本仓库真实踩过这个坑，
> 见 [实测记录](docs/devlog/2026-08-26-定时发布排查.md)。

### 两组检查

两组，任一项不过就不发布。

**第一组：数据保真**（`verify.verify`，所有 AI 通道都跑）

| 检查 | 拦什么 |
|---|---|
| 图片引用 | 源文的图在成稿里丢了 |
| 数据数字 | 出现源文没有的数值 —— 编造的流速、限度、回收率 |
| 法规条款号 | ICH / 21 CFR / USP / Ph. Eur. 丢失，**零容忍** |
| 文献 DOI | 大批量丢失（允许少量，合并重复论述时折叠掉是正常的） |
| 篇幅 | 正文短于源文的 40%，说明模型退化成了摘要 |

#### 「数据数字」到底把什么算数据

这条最容易误伤，因为「哪些数字承载数据」本身要判断。**语料实测**（209 篇
可发布笔记、1,503,893 字符）：早期提取器抓到的 13,624 个「数据」token 里
约 44% 根本不是测量值 —— 1,677 个裸年份、972 个图片文件名时间戳、
643 个 DOI 前缀，其余大量是参考文献的卷号页码。据此定了四条排除与归一化
规则，**都只改「什么算数据」，一条判定阈值都没放宽**：

| 规则 | 为什么 |
|---|---|
| **单位跟着数值走** | `4000Da`（粘连）与 `148000 Da`（带空格）以前提取成两种口径，同一个量两个 token。绑定后反而更严：以前 `0.5 mL/min → 0.5 L/min` 两边都是裸 `0.5`，单位调包完全看不见 |
| **单位写法差异不算编造，值对不上才算** | 分三种情形判：**值源文根本没有** → 拦（本职）；**输出裸写** → 值对上就放行（源文 `4000Da` 写成「4000 道尔顿」）；**输出带单位、源文裸写过该值** → 放行（源文 `precursor mass is 574.3` 写成 `574.3 Da`）；**输出带单位、源文只带别的单位** → 拦（`50 mM → 50 pmol` 是调包，实测真出现过） |
| **µ/μ、℃/°C 归一化** | 两种写法在语料里并存（实测 127 vs 588、168 vs 198），是字符编码差异不是数据差异。只对提取出的 token 做 NFKC，不对全文做 —— 全文归一化会把上标 `10⁶` 压成 `106`，凭空造出一个三位整数 |
| **链接 URL、图片、DOI 里的数字不计** | 它们各有更严的专属检查（丢图、DOI 丢失阈值），重复计入只制造误报 |
| **裸年份不计** | 年份不是测量值。模型写「截至 2026 年」这类过渡句必然产生年份。**唯一例外是版本年份**：`《中国药典》2020年版`、`ChP 2025年版` 是规范性依据，改错了是合规主张变了，照样拦 |

实测效果：拿改动前后两版校验器跑真实草稿 + 真实源笔记，被拦数字
11 → 7，降幅 36%，消掉的全部是 `4000`（单位粘连）和 `2003/2012/2017/2026`
（年份）；剩下 7 个逐个核对过，确实是源笔记里没有的。

> **性能不是瓶颈，别为它改代码。** 实测最大那篇 105,190 字符的笔记：
> `verify()` 19.7 ms、`review()` 1.2 ms、`evidence.check()` 1.7 ms。
> 相比同一次运行里 DeepSeek 调用和图片下载的几十秒，校验器占比可以忽略。

**第二组：可发表性**（`verify.review`，引子通道与人工投稿通道跑）

| 检查 | 拦什么 |
|---|---|
| 扩展来源 | `[依据 N]` 与来源清单对不上；笔记路径在知识库里不存在；引用要点在那篇笔记里找不到（二元组重合度 < 50%）；DOI 格式不合法或没在输入材料里出现过 |
| 加减法 | 减法删过头或根本没删，加法没长或翻了三倍以上 |
| 结构 | 二级章节不在 3～8 个；空壳章节（正文不足 120 字）；标题自带序号；正文里有一级标题；缺导读段 |
| 格式 | 指向知识库内部 md 的相对链接（站上是死链）；残留未解析的双链；有图没取到 |
| 选材重复 | 这篇引子笔记已经用过 |
| 关联文章 | 同二级标签的已发布文章没在「相关阅读」里出现 |

关联文章的链接由**流水线生成**而不是让模型写 —— 模型不知道站上发过什么，
让它写必然编 slug。

### 校验没过怎么办

**放行 = 删掉一行。** 没过校验的文章和正式文章一样落在
`src/content/posts/`，只在 frontmatter 里多两项（这套机制取代了早期的
`_review/` 目录方案，完整踩坑经过见
[`docs/devlog/2026-08-26-草稿位放行.md`](docs/devlog/2026-08-26-草稿位放行.md)）：

```markdown
---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['1.8', '12kda']"
  - "丢图: ['202201241314544.png']"
title: "宿主细胞蛋白（HCP）的质谱鉴定与绝对定量"
date: 2026-08-25
...
---
```

`draft: true` 让站点构建整篇跳过 —— 文章躺在仓库里，但不出现在首页、
分类页、标签页、归档、RSS、sitemap 里，也不会生成自己的页面。

| 要做什么 | 怎么做 |
|---|---|
| **放行** | 删掉 `draft: true` 那一行，提交 |
| **退稿** | 删掉整个文件 |
| **记账** | 不用管，流水线每次运行自动对账 |

`reviewNotes` 是没过哪几项。放行时留着不影响任何东西（frontmatter 不参与
渲染），想顺手删掉也行。

在 GitHub 网页或手机上：打开文件 → 点铅笔 → 删掉 `draft: true` 那一行 →
Commit changes。推到 master 会自动触发 deploy，文章随即上线。

> **为什么 `reviewNotes` 用 YAML 而不是 HTML 注释。** 早期版本把问题清单写在
> 文件开头的 `<!-- -->` 里，实测 GitHub 的 markdown 预览会把注释整段隐藏 ——
> 人打开文件只看得到正文，根本不知道哪里没过，得点 Code 或 Raw 才看得见。
> YAML 字段在预览里正常显示。

除了文件本身，另外两处也会记下这次失败：

1. 追加一行到 `logs/verify-YYYY-MM.md`，随产出一起提交进仓库
2. 开一个 GitHub Issue（标签 `校验未通过`），配了 SMTP 的话同时发邮件

#### 账本自己会对账，不用手动维护

`published.json` 是选材去重的账本（引子通道按 `seed` 字段判定这篇笔记
用过没有）。它**按 slug 做 key，每次运行开头自动跟 `src/content/posts/`
对一次账**：

- 有文件、没记录 → 按 frontmatter 回填
- 有记录、没文件 → 销账，那篇笔记重新入列

所以人工只需要动文件本身，不需要写一行 JSON。

> **这一条是踩过坑才有的。** 早期账本按 `primaryTag` 做 key，而同一个三级
> 标签下会有多篇文章（ELISA 与 HCP鉴定与定量 的 `primaryTag` 完全相同），
> 后写的会静默覆盖先写的，被覆盖那篇于是变回「没发过」，下次定时任务重新
> 生成一遍。另一次是手工把文章搬进 `posts/` 却忘了记账，同样导致重复生成。
> 改 slug 做 key + 自动对账之后，这两种情况都不会再发生。

> **回填记录没有 `source_hash`**（拿不到 vault 算不出），流水线把这种记录
> 一律当作已发布、不重发 —— 人工放行过的文章不该因为源笔记改了个错别字
> 就被悄悄重写一遍。

### 通知怎么配

**GitHub Issue：零配置，已经能用。** workflow 用的是 Actions 自带的
`GITHUB_TOKEN`。手机装 GitHub App 就有推送，还能直接在 issue 里记录处理
结果 —— 比邮件更适合追踪，推荐优先用这个。

**邮件：要配 Secret。** 仓库 Settings → Secrets and variables → Actions →
New repository secret：

| Secret | 填什么 |
|---|---|
| `MAIL_USER` | 发信邮箱，如 `708838228@qq.com` |
| `MAIL_PASSWORD` | **QQ 邮箱的「授权码」**，不是登录密码。QQ 邮箱 设置 → 账号 → POP3/IMAP/SMTP 服务里开启并生成 |
| `MAIL_TO` | 收信邮箱 |
| `MAIL_HOST` | 可不填，默认 `smtp.qq.com`（SSL 465） |

没配就静默跳过，只写日志和开 issue。**通知发不出去不影响文章产出** ——
文章已经落盘了，为了通知把产出丢掉是本末倒置。

## 日常使用

### 人工投稿：自己写的稿子怎么发

**一、放文件**

```
drafts/我的稿子.md                  ← 正文
drafts/images/我的稿子/图一.png      ← 随稿上传的图（可选，目录名 = 稿件文件名去掉 .md）
```

正文里按**文件名**引用图片，不要写路径：`![](图一.png)`

frontmatter 可有可无。写了就用你的，没写就从正文的一级标题取标题、其余
字段用默认值：

```markdown
---
title: 手动投稿示例
tags:
  - 03质量控制/残留/HCP
---
```

**二、按按钮**

两种触发方式，效果一样：

- **推上去就跑**：把文件 commit 推到 master，`drafts/**` 的改动自动触发 publish
- **手动按**：Actions → publish → Run workflow → `mode` 选 `manual`

**三、AI 处理并发布**

稿子会走**和自动文章完全一样**的一套：按体量判定加减法 → 整理 → 取图 →
两组校验 → 全过就直接发布，不过就带 `draft: true` 等你放行（见
「[校验没过怎么办](#校验没过怎么办)」）。处理完原稿会从 `drafts/` 撤走
（已经转成文章了，留着会被重复处理）。

> **不想让 AI 动内容、要原样发布**：本地跑 `python pipeline/main.py --drafts`。
> 这条直通道只做格式转换和取图，不调模型、不做加减法。

#### 投稿里的图片怎么处理

三条路依次尝试，**第一条命中就不往下走**：

| 顺序 | 图在哪 | 正文里怎么写 | 结果 |
|---|---|---|---|
| 1 | 随稿上传到 `drafts/images/<稿件名>/` | `![](图一.png)` | 就地转 WebP（限宽 1200px）存进 `public/images/<slug>/` |
| 2 | 已在 Google Drive 的 `image&attachment` 里 | `![](图一.png)` | 按文件名去 Drive 取，转 WebP 落仓库 |
| 3 | 外链 | `![](https://...)` | 原样保留，不落地 |

三条都不中，正文里留一行「图片暂缺」占位，**并计入校验失败**（缺图是可
发表性检查的一项），文章带 `draft: true` 落盘。补上图再放行即可。

### 怎么建一个系列

系列是「一组按指定顺序读的文章」，有自己的落地页（`/series/<id>`）与简介。
分类和标签都是无序集合，表达不了「这几篇是一条线」。

编辑 `src/content/series.json`，加一条：

```json
{
  "id": "系列的URL名",
  "title": "系列标题",
  "description": "一句话说明这个系列讲什么、按什么线索展开。",
  "entries": [
    { "post": "已发布文章的文件名（不含 .md）" },
    { "planned": "还没写的篇目标题" }
  ]
}
```

`entries` 的数组顺序**就是**阅读顺序，不用另写序号字段 —— 序号字段会和数组
顺序产生两个真相。`planned` 条目在页面上显示成灰的「待发布」，等于把发布计划
挂在站上；那篇写完后把它换成 `{ "post": "..." }` 即可。

文章的 frontmatter 不需要加任何字段，流水线两条通道也完全不用改。

**三条硬规矩，违反会让 `npm run build` 直接失败（不是静默出错）：**

| 规矩 | 为什么 |
|---|---|
| `post` 填的 id 必须真实存在 | 手写 JSON 最容易把 id 打错。若容许「找不到就当作待发布」，一个拼写错误会变成页面上一条看不出错的灰条目 |
| 一篇文章只能属于一个系列 | 文章页的系列归属提示只有一处，属于两个系列时显示哪个都是错的 |
| 每条 entry 恰好有 `post` 或 `planned` 之一 | 两者都写意味着意图不明，交给人去定 |

序号语义：文章页显示的「第 N / M 篇」中 N 与 M **都含待发布条目** —— M 表达的是
这个系列计划写多少篇。上一篇 / 下一篇则跳过待发布条目，因为它们没有页面可链。

### 手动触发一次发布

Actions → publish → Run workflow，四个开关：

| 开关 | 作用 |
|---|---|
| `mode` | `seed` 引子通道（默认）／`manual` 处理 drafts／`auto` 旧的多篇重组 |
| `count` | 本次发几篇 |
| `publish` | 勾上=校验全过就直接发布；不勾=一律带 `draft: true` 等人工放行 |
| `refresh_index` | 刚往 Drive 补传了图就勾上，强制重建索引 |

发布成功后 `deploy` 会自动跟着跑（靠 `workflow_run` 触发，见「[架构总览](#架构总览)」
里的 GitHub 递归坑说明）。

### 文章里出现「图片暂缺」怎么办

正文里那行 `[图片暂缺]` 表示这张图在 Drive 的 `image&attachment` 文件夹
里找不到。文件名藏在同一行的 HTML 注释里（读者看不到），查看文章源码
或直接跑体检即可拿到清单：

```bash
python pipeline/main.py --audit-images --vault <vault 路径>
```

它列出所有待发布笔记里 Drive 上没有的图，按源笔记分组，只读
`pipeline/drive_index.json` 缓存，不碰 Drive。

**实测大头是笔记同级的 `res/`、`attachments/` 目录** —— 这些是 Typora
和 Zotero 时代留下的本地图，从来没上传过 Drive。把它们传进
`image&attachment`（文件名保持不变）即可。

**另一类是图在 Drive 上、但名字对不上** —— 早期 Typora 按截图时刻命名
（17 位），上传工具按上传时刻重命名成 15 位，笔记里的引用没跟着改。
这种别去改笔记（已发布的文章不会重跑），往 `pipeline/config.py` 的
`IMAGE_ALIASES` 加一行「引用名 → Drive 实际文件名」即可，下次跑补图
通道就会把文章修好。刻意不做时间戳近似匹配：同分钟撞车会把错图发出去。

补传之后：Actions → publish → Run workflow，**勾上「补图前强制重建
Drive 索引」**（只加别名不必勾，索引里本来就有那个文件）。已发布的文章会被就地修好 —— `published.json` 里已经记了
账，自动通道不会重跑那篇，靠的是补图通道按占位标记重取，不用再烧一次
LLM。不勾也行，Drive 索引缓存 7 天一换，到期后自动补上。

### 旧的多篇重组通道（`mode: auto`）

分组规则在 `pipeline/select_.py` 的 `build_groups`：按每篇笔记**自身最深的
标签层级**（最多三级）分桶，碎组不向上归并。归并才是「一篇文章什么都讲」
的根源 —— 实测归并版把 12 篇横跨定量、测序、碎裂、数据分析、离子源的笔记
塞进「05仪器与分析技术/质谱」一组，出来只能是大杂烩。

想调粒度改 `pipeline/config.py` 的 `MIN_GROUP`（实测 209 篇可发布笔记）：

| MIN_GROUP | 组数 | 覆盖笔记 | 效果 |
|---|---|---|---|
| 2（当前） | 38 | 150 | 「质谱/数据分析」这种正好 2 篇的紧凑子题也能成文 |
| 3 | 20 | 126 | 文章更厚实，但近四成笔记永远排不上队 |

单组体量还受 `MAX_GROUP_CHARS`（5 万字符）约束，超了按笔记体量截断。

### 想让某篇超长的原创笔记也能发布

单篇超过 3 万字符的笔记默认不发（实测超过这个量的绝大多数是整书/整章
转录，有版权问题）。自己写的长文把路径加进 `pipeline/config.py` 的
`SIZE_EXEMPT_NOTES` 即可。

## 首次部署

**给要在自己的 fork 上跑起来的人。** 仓库所有者已经配好了下面这些
secret，日常开发或改流水线代码不需要重新走一遍这一节；只有你想让流水线
接自己的 Obsidian vault、自己的 DeepSeek key、自己的 Google Drive 时才
需要。

三个 Secret + 一次 Drive 共享 + 开启 Pages（顺序：`DEEPSEEK_API_KEY` →
`VAULT_TOKEN` → `GDRIVE_SA_JSON` → 共享 Drive 文件夹 → 填入仓库 Secret →
开启 Pages → 手动验证）。全程免费，Drive API 只读和 GitHub Actions 在
这个用量下都在免费额度内。

> 下面每一步都标了**为什么需要**和**漏了会怎样**。这套配置踩坑的地方在于
> 报错信息普遍不指向真正的原因，所以按顺序做完再手动跑一次验证。

### DEEPSEEK_API_KEY

**做什么用**：调 DeepSeek 把笔记整理成文章。

1. 打开 https://platform.deepseek.com/ 登录
2. 左侧 **API keys** → **创建 API key**，名字随便起
3. 复制生成的字符串（**只显示这一次**）

模型在 `pipeline/config.py` 里配置。想省钱可以用 `deepseek-v4-flash`，
机械校验器会兜底；对保真度要求更高时可换回 `deepseek-v4-pro`。模型 ID 以
`GET https://api.deepseek.com/models` 返回的清单为准 —— 早期的
`deepseek-chat` / `deepseek-reasoner` 已经不在清单里了。

### VAULT_TOKEN

**做什么用**：GitHub Actions 自带的令牌只能访问它自己所在的仓库（本仓库），
碰不到 `Obsidian-base` 和 `RoutineRun`。而这两个源仓库都是**私有**的，
所以要单独给一个只能读它们的令牌。

**漏了会怎样**：workflow 在 checkout 源仓库那步就失败，报 404 或
authentication failed。

1. 打开 https://github.com/settings/personal-access-tokens/new
   （手点路径：头像 → Settings → 最底部 **Developer settings** →
   **Personal access tokens** → **Fine-grained tokens** → **Generate new token**）
2. 按下表填：

   | 项 | 填什么 |
   |---|---|
   | Token name | 随便起，如 `blog-vault-read` |
   | Expiration | 建议 1 year。**到期后流水线会停**，记一下时间 |
   | Resource owner | 选你自己（Bryce505） |
   | Repository access | 选 **Only select repositories** |
   | └ Select repositories | 勾上 **Obsidian-base** 和 **RoutineRun** |
   | Permissions → Repository permissions → **Contents** | 改成 **Read-only** |

   `Metadata: Read-only` 会自动跟着勾上，那是必需项。其他权限一个都别给。

3. **Generate token** → 立刻复制那串 `github_pat_` 开头的字符串
   （**只显示这一次**，刷新就没了，只能重新生成）

> 如果 Fine-grained 那页填不出来，退路是同一个 Developer settings 里的
> **Tokens (classic)** → Generate new token → 只勾 `repo`。缺点是它能读写
> 你**所有**仓库，不如细粒度安全。

### GDRIVE_SA_JSON

**做什么用**：笔记正文里的图片（实测 1235 张）不在 git 仓库里，只在
Google Drive 的 `image&attachment` 文件夹。流水线要用服务账号去读。

**这一项步骤最多，也最容易在中途卡住。**

#### 1. 建项目并开启 Drive API

1. 打开 https://console.cloud.google.com/ ，**用拥有那个 Drive 文件夹的
   账号登录**（登错账号后面共享那步会没权限）
2. 顶部项目选择器 → **新建项目**，名字如 `obsidian-blog` → 创建
3. **确保顶部项目选择器里选中的就是这个新项目** ← 常见卡点：不选中项目的话，
   服务账号页面只会显示「要查看此页面，请选择一个项目」，根本看不到
   「创建服务账号」按钮
4. 打开 https://console.cloud.google.com/apis/library/drive.googleapis.com
   → 点 **启用**（ENABLE）

   已经启用的话这里显示「API 已启用」或 **管理**（MANAGE）。
   **没启用的话服务账号建得再对也读不了 Drive，而且报 403 不会说是 API 没开。**

#### 2. 建服务账号

打开 https://console.cloud.google.com/iam-admin/serviceaccounts →
**+ 创建服务账号**

| 步骤 | 怎么做 |
|---|---|
| 服务账号名称 | 如 `blog-image-reader`，ID 自动生成不用改 |
| 第 2 步「授予角色」 | **直接跳过**（点继续）—— 它不需要任何 GCP 角色，权限来自 Drive 的文件夹共享 |
| 第 3 步「用户访问权限」 | 也跳过，点完成 |

#### 3. 生成 JSON 密钥

在服务账号列表点刚建的那个 → 顶部 **密钥**（KEYS）标签 →
**添加密钥** → **创建新密钥** → 选 **JSON** → 创建。

浏览器自动下载一个 .json 文件，内容形如：

```json
{
  "type": "service_account",
  "project_id": "obsidian-blog-506523",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "blog-image-reader@obsidian-blog-506523.iam.gserviceaccount.com",
  ...
}
```

**把整个文件内容全选复制**（从第一个 `{` 到最后一个 `}`），一个字符都别漏。

> ⚠️ 这个文件里有私钥。**别提交进任何仓库、别发到聊天工具里。**
> 粘进 GitHub Secret 之后本地那份可以删掉，要用再重新生成一个密钥。

### 共享Drive文件夹给服务账号

**← 最容易漏的一步。漏了会怎样**：流水线能正常跑完，但**一张图都取不到**，
全部文章的图片变成「图片暂缺」占位文字，而且报的是 404 而不是「你没共享
文件夹」。

1. 从上面 JSON 里找到 **`client_email`** 的值（形如
   `blog-image-reader@xxx.iam.gserviceaccount.com`），复制引号里那一整串
2. 打开文件夹
   https://drive.google.com/drive/folders/1jwf_lkCo-Rq42VwWToyTeu2ciJTRg4zT
   ，确认登录的是文件夹所有者账号
3. 点页面**顶部中间的文件夹名** → 下拉菜单 → **共享** → **共享**
   （或在「我的云端硬盘」列表里右键该文件夹 → 共享）
4. 在「添加成员和群组」里粘贴那个邮箱
   - 可能提示「此收件人不是 Google 账号」之类的警告 —— **正常，无视**，
     服务账号本来就不是真人账号
   - 角色选 **查看者**（Viewer）
   - **把「通知用户」的勾去掉** ← 服务账号收不了邮件，勾着可能直接报错
5. 点 **共享** / **发送**

### 填入仓库Secret

本仓库 → **Settings** → **Secrets and variables** → **Actions** →
**New repository secret**，依次建三条：

| Name | Secret |
|---|---|
| `DEEPSEEK_API_KEY` | 第一步复制的 key |
| `VAULT_TOKEN` | 第二步复制的 `github_pat_...` |
| `GDRIVE_SA_JSON` | 第三步 JSON 文件的**全文** |

名字必须一字不差，workflow 里是按这三个名字取的。

### 开启Pages

**Settings** → **Pages** → Source 选 **GitHub Actions**
（不是 Deploy from a branch）。

站点地址是 `https://<用户名>.github.io/<仓库名>/`。
**GitHub Pages 的路径区分大小写** —— 仓库叫 `Blog` 站点就在 `/Blog/`，
所以 `astro.config.mjs` 里的 `base` 必须和仓库名大小写完全一致。
改仓库名的话记得同步改这一行。

### 手动验证一次

**别配完就直接等定时。** Actions → **publish** → **Run workflow**，
篇数填 1。

跑完检查三处：

- **workflow 是否全绿** —— 红了看是哪一步：checkout 源仓库失败是
  `VAULT_TOKEN` 问题，取图失败是 Drive 共享或 API 没启用，
  整理那步失败看 DeepSeek 的报错（余额、模型名）
- **文章有没有图** —— 打开生成的文章，如果满屏「图片暂缺」，回去检查
  「共享 Drive 文件夹给服务账号」那步
- **文章内容读一遍** —— 这是唯一没法自动验证的部分，见下

> **首次运行务必人工通读生成的文章。** 机械校验器只能保证数据没被篡改、
> 图片没丢，保证不了文章好不好读。觉得改写力度不对（太放飞或太保守），
> 调 `pipeline/prompt.md` / `pipeline/prompt_seed.md` 里的提示词即可。

## 开发规范

给贡献者（含 AI agent）的约定，完整规则见 [`CLAUDE.md`](CLAUDE.md)。这里
只列最容易忽略、忽略了会导致 PR 被打回的几条：

1. **开发日志硬性要求。** 每次改动都要在 [`docs/devlog/`](docs/devlog/) 下
   新增一个 `YYYY-MM-DD-<短标题>.md`，写背景（实测现象，不是「优化一下」）、
   变更、实现取舍、动了哪些文件、怎么验证的。这是本仓库唯一的连续记忆——
   模板见 [`docs/devlog/README.md`](docs/devlog/README.md)。
2. **一个分支只开发一个功能。** 分支名 `claude/<功能>-<短标识>`，从最新
   master 起；一个分支对应一篇开发日志；合并前必须
   `python pipeline/test_pipeline.py` 全绿、`npm run build` 通过，动了流水线
   行为的还要在分支上实跑一次。
3. **注释写"为什么"，不写"做了什么"。** 尤其是阈值、正则、异常分支——
   带具体数字的判断要有实测依据（这份 README 和 `pipeline/config.py` 里
   大量「实测 XX 篇里 XX 篇会怎样」式的注释就是这个约定的产物）。
4. **校验器是安全阀，不是可有可无的检查。** 放宽 `pipeline/verify.py` 的
   规则前，先想清楚这条规则当初拦的是什么；拦不住就别上线。

## 延伸阅读

- [`CLAUDE.md`](CLAUDE.md) —— 开发约定全文
- [`docs/devlog/`](docs/devlog/) —— 开发日志，按时间倒序的真实踩坑记录
- [`docs/superpowers/specs/`](docs/superpowers/specs/) —— 设计文档
- [`docs/superpowers/plans/`](docs/superpowers/plans/) —— 实施计划
- [`logs/`](logs/) —— 按月归档的校验运行日志
- 站点：https://bryce505.github.io/Blog
