---
title: Git & GitHub 学习笔记
date: '2026-08-24'
category: 工具与效率
tags:
- 工具与效率/git&github
description: 按时间顺序追加记录每次相关对话的要点，方便回顾（记录规则见 CLAUDE.md(./CLAUDE.md)）。 <-- 记录格式： YYYY-MM-DD
  问题/主题简要描述 - 要点1 - 要点2 （同一天多个话题就在同一个日期标题下累加多个
---

按时间顺序追加记录每次相关对话的要点，方便回顾（记录规则见 [`CLAUDE.md`](./CLAUDE.md)）。

<!--
记录格式：
## YYYY-MM-DD
### 问题/主题简要描述
- 要点1
- 要点2
（同一天多个话题就在同一个日期标题下累加多个 ### 子标题，别新开日期标题；新增内容要同步补进下面的目录）
-->

## 目录

- [2026-08-23](#user-content-2026-08-23)
  - [Git 基本概念与软件开发关键节点用法](#user-content-git-基本概念与软件开发关键节点用法)
  - [本地项目推送到 GitHub 的操作步骤](#user-content-本地项目推送到-github-的操作步骤)
  - [本地分支重命名为 main 的原理](#user-content-本地分支重命名为-main-的原理)
  - [SSH 密钥配对原理](#user-content-ssh-密钥配对原理)
  - [SSH 密钥生成命令参数详解](#user-content-ssh-密钥生成命令参数详解)
  - [PR 合并 master 与已合并分支的处理方法](#user-content-pr-合并-master-与已合并分支的处理方法)
  - [两张 Git 协作原理图讲解](#user-content-两张-git-协作原理图讲解)
- [2026-08-24](#user-content-2026-08-24)
  - [GitHub 目录锚点链接为什么点不动](#user-content-github-目录锚点链接为什么点不动)

## 2026-08-23

### Git 基本概念与软件开发关键节点用法

**基本概念**
- Git 是分布式版本控制系统(DVCS)：本地就有完整历史，不依赖中央服务器
- 三个区域：工作区 → `git add` → 暂存区(index) → `git commit` → 本地仓库(.git)
- Commit：一次快照，含改动、作者、时间、父提交哈希，是历史的最小单元
- Branch：指向某个 commit 的可移动指针，创建成本极低，用于并行开发
- HEAD：当前所在分支/commit 的指针
- Remote：远程仓库，默认名 `origin`，用于协作和备份
- Tag：固定标记(不随新提交移动)，常用于版本号如 `v1.0.0`
- Merge vs Rebase：merge 保留分支历史+产生合并提交；rebase 把提交重放成线性历史
- Conflict：同一处代码被不同提交改动，需人工解决
- Stash：临时收纳未提交改动，方便切分支处理紧急任务
- `.gitignore`：声明不纳入版本管理的文件

**软件开发关键节点 → Git 用法 → 作用**
| 阶段 | 命令/机制 | 作用 |
|---|---|---|
| 项目启动 | `git init`/`git clone` | 建立/获取仓库，协作起点 |
| 功能开发 | `git checkout -b feature/xxx` | 分支隔离开发，不影响主干 |
| 日常编码 | `git add`+`git commit` | 保存可追溯、可回滚的进度 |
| 同步进度 | `git fetch`/`git pull` | 拉取远程最新代码，尽早发现冲突 |
| 备份协作 | `git push` | 同步到远程，触发 CI |
| 代码评审 | GitHub Pull Request | 合并前的质量把关 |
| 持续集成 | CI 监听 push/PR | 自动测试构建，提前拦截问题 |
| 集成主干 | `git merge`/`git rebase` | 功能分支合入主干 |
| 预发布 | 拉 `release` 分支 | 冻结范围，只修 bug |
| 正式发布 | `git tag vX.Y.Z` | 标记上线版本，方便回滚 |
| 生产修复 | 拉 `hotfix` 分支 | 紧急修复不受在研功能干扰 |
| 出问题回滚 | `git revert`(安全)/`git reset`(慎用，勿用于已推送的公共分支) | 撤销问题提交 |
| 问题追溯 | `git log`/`git blame`/`git bisect` | 查历史/定位改动人/二分定位引入 bug 的提交 |

**分支策略**：Git Flow(main+develop+feature+release+hotfix，适合有发布节奏的项目) / GitHub Flow(main+短命feature+PR，合并即部署) / Trunk-Based(大家都提交主干，配合 feature flag)

### 本地项目推送到 GitHub 的操作步骤

**情况一：本地还不是 git 仓库**
```bash
git init
git add .
git commit -m "初始提交"
```
去 GitHub 建**空仓库**（不勾选自动生成 README/.gitignore/LICENSE，否则远程会有本地没有的提交，push 时冲突），然后：
```bash
git remote add origin <仓库地址>
git branch -M main
git push -u origin main    # -u 记住关联，以后直接 git push
```

**情况二：本地已有 git 历史，只是没关联远程**
```bash
git remote -v                       # 先看有没有已关联的远程
git remote add origin <仓库地址>
git push -u origin <本地分支名>
```
之后日常改动：`git add . && git commit -m "..." && git push`

**身份验证**（GitHub 不支持账号密码直接 push）
- HTTPS + Personal Access Token：远程地址 `https://github.com/用户名/仓库.git`，push 时密码处填 token（GitHub Settings → Developer settings → Personal access tokens 生成）
- SSH（推荐，配一次免密）：`ssh-keygen -t ed25519 -C "邮箱"` 生成密钥 → 把 `~/.ssh/id_ed25519.pub` 内容加到 GitHub Settings → SSH and GPG keys → 远程地址改用 `git@github.com:用户名/仓库.git`

**顺手一条**：装了 `gh` CLI 的话，情况一可以一条命令搞定：`gh repo create 仓库名 --private --source=. --push`

### 本地分支重命名为 main 的原理

- 不是"创建"，是**重命名当前分支**为 `main`（命令：`git branch -M main`）
- `-M` = `-m`(rename) 的强制版本：目标名已存在时，`-m` 会报错，`-M` 会强制覆盖
- 用途：`git init` 默认分支名因 Git 版本/`init.defaultBranch` 配置而异(老版本默认 `master`)，而 GitHub 新建仓库默认用 `main`；push 前统一改名，避免本地/远程分支名不一致
- 已经叫 `main` 可跳过这一步；也可以一劳永逸配置：`git config --global init.defaultBranch main`
- 只改名字，不影响提交历史和内容

### SSH 密钥配对原理

- `ssh-keygen` 生成的是**一对**密钥：私钥 `~/.ssh/id_ed25519`（留本机，绝不外传/上传）+ 公钥 `~/.ssh/id_ed25519.pub`（可公开，粘贴到 GitHub）
- GitHub 只保存你的公钥，不是"两把钥匙对上"，而是非对称加密的挑战-应答机制：GitHub 用公钥出题 → 本机用私钥作答 → 公钥验证应答 → 通过认证；私钥全程不传输
- 配完用 `ssh -T git@github.com` 测试，看到 `Hi 用户名! You've successfully authenticated...` 说明配置成功

### SSH 密钥生成命令参数详解

命令：`ssh-keygen -t ed25519 -C "邮箱"`

- `-t ed25519`：指定密钥算法，ed25519 是现代椭圆曲线算法，比 RSA 更短更快更安全，GitHub 推荐首选；旧系统不支持可退回 `-t rsa -b 4096`
- `-C "邮箱"`：comment，给密钥加备注标签，不参与加密，纯为识别"这把钥匙是谁的"，填什么都行
- 执行时会问三个问题：① 保存路径(回车用默认 `~/.ssh/id_ed25519`) ② passphrase(私钥文件的密码，回车=不加，免密但私钥泄露即可被冒用；设置后更安全，配合 ssh-agent 可只输一次) ③ 确认 passphrase
- `cat ~/.ssh/id_ed25519.pub`：`.pub` 是 ssh-keygen 自动生成的公钥文件名(私钥同名无后缀)，`cat` 打印出来的整行文本就是要粘贴到 GitHub 的内容

### PR 合并 master 与已合并分支的处理方法

- 用户直接指示"PR 合并到 master"：先 `list_pull_requests` 确认该分支没有开放 PR
- 发现该分支之前已有 PR #2 合并过一部分历史(到某条提交为止)，后续在同一分支上追加的提交没有对应 PR —— **已合并的 PR 不能复用**，需要基于最新 master 重新处理未合并的提交
- 处理方法：`git fetch origin master` → `git rebase --onto origin/master <旧的已合并提交> <分支名>`，把未合并的提交变基到最新 master 上，而不是丢弃 → `git push --force-with-lease` → 开新 PR → `merge_pull_request` 合并
- 合并后本地要 `git checkout master && git pull` 同步，再切回工作分支 `git merge --ff-only origin/master`，并 **push 回远程工作分支**——GitHub 合并 PR 只更新 base 分支(master)，不会自动更新 head 分支，本地 fast-forward 之后必须手动 push，否则 stop hook 会提示"有未推送的提交"

### 两张 Git 协作原理图讲解

![Git 四大区域工作原理](/images/tools-笔记/git四大区域工作原理.webp)

![协作标准姿势：远程 master + 本地 feature](/images/tools-笔记/协作标准姿势-远程master本地feature.webp)

**图一：Git 四大区域 + 命令**：工作目录 → (`add`) → 暂存区 → (`commit`) → 本地仓库 → (`push`/`fetch`) → 远程仓库。`pull` = `fetch`+`merge` 的组合命令。`clone`/`init` 是建仓库的起点，`branch`/`checkout` 管分支，`diff`/`status`/`log` 是只读查看命令。

**图二：协作标准姿势(远程 master + 本地 feature)**：`origin/master` 是团队唯一真相来源，每个人在自己的 feature 分支开发。四步流程：① 每天开工先 `checkout master`→`pull`→`checkout feature/xxx`→`merge master` 同步 ② 开发中 `add`+`commit` ③ 完成后 `push` 到远程 feature 分支 + 提 PR 等审查 ④ 审查通过后合并进 master。三条铁律：永远不直接 push 到 master / 永远先 pull 再开发 / 永远通过 PR 合并代码。

## 2026-08-24

### GitHub 目录锚点链接为什么点不动

现象：在 GitHub 手机 App 里点笔记开头目录中日期下面的子标题链接（比如"两张 Git 协作原理图讲解"），没有跳转。

排查过程：
- 用 `github-slugger`（GitHub 官方开源、markdown 渲染实际用的锚点生成库）本地跑了一遍，确认目录里写的锚点文字本身和标题对得上，不是拼写/编码算错的问题
- 用 GitHub Contents API 拿渲染后的真实 HTML 一看：标题自己的 `id` 是 `id="user-content-两张-git-协作原理图讲解"`，带了 `user-content-` 前缀；而我写的目录链接是 `href="#两张-git-协作原理图讲解"`，没带前缀——**两者对不上**
- GitHub 网页版能点通，是因为额外加载了一段前端脚本，把不带前缀的 `#slug` 悄悄重定向到 `#user-content-slug`；GitHub 手机 App 大概率没跑这段脚本，所以点了没反应

结论/修法：**目录里所有锚点链接都要写成 `#user-content-<slug>`**，直接对应标题真实的 DOM id，不依赖网页版才有的重定向脚本，网页版和 App 都能跳转。已经把 `笔记.md` 目录和 `CLAUDE.md` 规则同步改过来了。
