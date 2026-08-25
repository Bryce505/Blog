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
RoutineRun    ─┤ ① 选题：按最深标签（≤三级）分组 → 查 published.json 去重
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

三个 Secret + 一次 Drive 共享 + 开启 Pages。全程免费，Drive API 只读和
GitHub Actions 在这个用量下都在免费额度内。

> 下面每一步都标了**为什么需要**和**漏了会怎样**。这套配置踩坑的地方在于
> 报错信息普遍不指向真正的原因，所以按顺序做完再手动跑一次验证。

### 1. `DEEPSEEK_API_KEY`

**做什么用**：调 DeepSeek 把笔记整理成文章。

1. 打开 https://platform.deepseek.com/ 登录
2. 左侧 **API keys** → **创建 API key**，名字随便起
3. 复制生成的字符串（**只显示这一次**）

模型在 `pipeline/config.py` 里配置，默认 `deepseek-v4-pro`。想省钱可以
改成 `deepseek-v4-flash`，机械校验器会兜底。模型 ID 以
`GET https://api.deepseek.com/models` 返回的清单为准 —— 早期的
`deepseek-chat` / `deepseek-reasoner` 已经不在清单里了。

### 2. `VAULT_TOKEN`

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

### 3. `GDRIVE_SA_JSON`

**做什么用**：笔记正文里的图片（实测 1235 张）不在 git 仓库里，只在
Google Drive 的 `image&attachment` 文件夹。流水线要用服务账号去读。

**这一项步骤最多，也最容易在中途卡住。**

#### 3.1 建项目并开启 Drive API

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

#### 3.2 建服务账号

打开 https://console.cloud.google.com/iam-admin/serviceaccounts →
**+ 创建服务账号**

| 步骤 | 怎么做 |
|---|---|
| 服务账号名称 | 如 `blog-image-reader`，ID 自动生成不用改 |
| 第 2 步「授予角色」 | **直接跳过**（点继续）—— 它不需要任何 GCP 角色，权限来自 Drive 的文件夹共享 |
| 第 3 步「用户访问权限」 | 也跳过，点完成 |

#### 3.3 生成 JSON 密钥

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

### 4. 把 Drive 文件夹共享给服务账号 ← 最容易漏的一步

**漏了会怎样**：流水线能正常跑完，但**一张图都取不到**，全部文章的图片
变成「图片暂缺」占位文字，而且报的是 404 而不是「你没共享文件夹」。

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

### 5. 把三个 Secret 填进仓库

本仓库 → **Settings** → **Secrets and variables** → **Actions** →
**New repository secret**，依次建三条：

| Name | Secret |
|---|---|
| `DEEPSEEK_API_KEY` | 第 1 步复制的 key |
| `VAULT_TOKEN` | 第 2 步复制的 `github_pat_...` |
| `GDRIVE_SA_JSON` | 第 3 步 JSON 文件的**全文** |

名字必须一字不差，workflow 里是按这三个名字取的。

### 6. 开启 Pages

**Settings** → **Pages** → Source 选 **GitHub Actions**
（不是 Deploy from a branch）。

站点地址是 `https://<用户名>.github.io/<仓库名>/`。
**GitHub Pages 的路径区分大小写** —— 仓库叫 `Blog` 站点就在 `/Blog/`，
所以 `astro.config.mjs` 里的 `base` 必须和仓库名大小写完全一致。
改仓库名的话记得同步改这一行。

### 7. 验证：先手动跑一次

**别配完就直接等定时。** Actions → **publish** → **Run workflow**，
篇数填 1。

跑完检查三处：

- **workflow 是否全绿** —— 红了看是哪一步：checkout 源仓库失败是
  `VAULT_TOKEN` 问题，取图失败是 Drive 共享或 API 没启用，
  整理那步失败看 DeepSeek 的报错（余额、模型名）
- **文章有没有图** —— 打开生成的文章，如果满屏「图片暂缺」，回去检查第 4 步
- **文章内容读一遍** —— 这是唯一没法自动验证的部分，见下

> **首次运行务必人工通读生成的文章。** 机械校验器只能保证数据没被篡改、
> 图片没丢，保证不了文章好不好读。觉得改写力度不对（太放飞或太保守），
> 调 `pipeline/prompt.md` 里的提示词即可。

## 日常使用

### 手动发一篇自己写的稿子

把 md 扔进 `drafts/`，push 即可。最少只要一个 `title` 字段，
详见 [`drafts/README.md`](drafts/README.md)。

### 手动触发一次自动发布

Actions → publish → Run workflow，可填本次发布篇数。

发布成功后 `deploy` 会自动跟着跑（靠 `workflow_run` 触发）。这里有个
GitHub 的坑：**workflow 用内置 `GITHUB_TOKEN` 推的提交不会触发其他
workflow**（防递归的安全规则），所以不能指望 publish 的 push 去触发
deploy 的 push 事件 —— 文章会一直躺在仓库里不上线。

### 校验没过的文章怎么办

流水线会把它写进 `_review/<slug>.md`，文件开头的注释里写着没过哪一项。
人工确认内容没问题后，把文件移到 `src/content/posts/` 并删掉那段注释即可。

> `_review/` 里存在的分组会被自动通道跳过，否则它会一直霸占队首、
> 后面的文章一篇也发不出去。人工处理掉文件后该组自动重新入列。

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

### 觉得文章主题太杂 / 太窄

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

## 本地开发

```bash
# Python 流水线
uv venv && uv pip install -r pipeline/requirements.txt
.venv/bin/python pipeline/test_pipeline.py      # 99 项自检

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
              / images / compose / drafts / routinerun / repair / main）
  prompt.md   DeepSeek 的系统提示词，改写力度不对就调这里
src/          Astro 站点
drafts/       手动发布投递口
public/images/ 文章图片（WebP）
published.json 已发布状态，按标签组记录
_review/      校验未通过、等人工复核的文章
design/       视觉设计源文件
```
