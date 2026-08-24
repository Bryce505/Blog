# 表征笔记

把 Obsidian 知识库里的原创笔记，按主题自动整理成技术文章，定时发布到
GitHub Pages。

- **站点**：https://bryce505.github.io/Blog
- **数据源**：`Bryce505/Obsidian-base`（生物医药 CMC 与分析方法）、
  `Bryce505/RoutineRun`（工具与效率栏目）
- **图片**：Google Drive `image&attachment` 文件夹
- **整理**：DeepSeek `deepseek-v4-pro`
- **发布节奏**：每晚 21:00（北京时间）一篇

设计文档见 [`docs/superpowers/specs/`](docs/superpowers/specs/)，
实施计划见 [`docs/superpowers/plans/`](docs/superpowers/plans/)。

## 它是怎么跑的

```
Obsidian-base ─┐
RoutineRun    ─┤ ① 选题：按三级标签分组 → 查 published.json 去重
Google Drive  ─┤ ② 取图：Drive 拉图 → WebP(≤1200px) → public/images/
               │ ③ 整理：DeepSeek 结构重组
               │ ④ 校验：四项机械校验，不过则进 _review/ 等人工
               │ ⑤ 落盘：写 src/content/posts/ + 更新 published.json + push
               └─↓
                 ⑥ Astro build → GitHub Pages
```

整理只做结构重组：打散笔记、重新梳理脉络、补写导读和过渡，但凡含数字、
单位、法规条款号、文献引用和图片引用的句子一律原样保留。

## 配置（首次部署必做）

### 1. 三个 Secrets

仓库 Settings → Secrets and variables → Actions：

| 名称 | 内容 | 怎么拿 |
|---|---|---|
| `DEEPSEEK_API_KEY` | DeepSeek API key | platform.deepseek.com 控制台创建 |
| `VAULT_TOKEN` | GitHub 细粒度 PAT | Settings → Developer settings → Fine-grained tokens，仅勾选 `Obsidian-base` 和 `RoutineRun` 的 **Contents: Read** |
| `GDRIVE_SA_JSON` | Google 服务账号 JSON 全文 | GCP 控制台建服务账号 → 建密钥（JSON）→ 把整个文件内容粘进来 |

> 两个源仓库都是**私有**的，没有 `VAULT_TOKEN` 拉不到笔记。

### 2. 把 Drive 文件夹共享给服务账号

**这一步最容易漏，漏了就是取图全失败，而且报错不直观。**

打开 Drive 里的 `image&attachment` 文件夹 → 共享 → 把服务账号邮箱
（形如 `xxx@yyy.iam.gserviceaccount.com`，在 JSON 的 `client_email` 字段里）
加为**查看者**。

### 3. 开启 Pages

Settings → Pages → Source 选 **GitHub Actions**（不是 Deploy from a branch）。

## 日常使用

### 手动发一篇自己写的稿子

把 md 扔进 `drafts/`，push 即可。最少只要一个 `title` 字段，
详见 [`drafts/README.md`](drafts/README.md)。

### 手动触发一次自动发布

Actions → publish → Run workflow，可填本次发布篇数。

### 校验没过的文章怎么办

流水线会把它写进 `_review/<slug>.md`，文件开头的注释里写着没过哪一项。
人工确认内容没问题后，把文件移到 `src/content/posts/` 并删掉那段注释即可。

> `_review/` 里存在的分组会被自动通道跳过，否则它会一直霸占队首、
> 后面的文章一篇也发不出去。人工处理掉文件后该组自动重新入列。

### 想让某篇超长的原创笔记也能发布

单篇超过 3 万字符的笔记默认不发（实测超过这个量的绝大多数是整书/整章
转录，有版权问题）。自己写的长文把路径加进 `pipeline/config.py` 的
`SIZE_EXEMPT_NOTES` 即可。

## 本地开发

```bash
# Python 流水线
uv venv && uv pip install -r pipeline/requirements.txt
.venv/bin/python pipeline/test_pipeline.py      # 89 项自检

# 站点
npm install
npm run dev        # 本地预览
npm run build      # 构建到 dist/
```

流水线的自检不依赖真实 vault，跑的是 `pipeline/fixtures/` 里的样本，
CI 里可以直接跑。

## 目录

```
pipeline/     Python 流水线（config / vault / select_ / verify / render
              / images / compose / drafts / routinerun / main）
src/          Astro 站点
drafts/       手动发布投递口
public/images/ 文章图片（WebP）
published.json 已发布状态，按三级标签组记录
_review/      校验未通过、等人工复核的文章
design/       视觉设计源文件
```
