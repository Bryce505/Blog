---
title: Claude Code on the Web / Cloud Session 使用笔记
date: '2026-08-24'
category: 工具与效率
tags:
- 工具与效率/docs
description: 本文档整理自一次关于 Claude Code 云端会话(claude.ai/code)运行机制的问答,记录了这个仓库（Bryce505/CodeSpace）目前的
  Claude Code 配置现状，以及相关的核心概念，供后续参考。 官方文档
---

> 本文档整理自一次关于 Claude Code 云端会话(claude.ai/code)运行机制的问答,记录了这个仓库（`Bryce505/CodeSpace`）目前的 Claude Code 配置现状，以及相关的核心概念，供后续参考。
>
> 官方文档：
> - [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)
> - [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments)
> - [Data usage](https://code.claude.com/docs/en/data-usage)

## 1. Cloud Session 是怎么跑起来的

在 claude.ai/code 选一个 GitHub 仓库并发起对话时：

1. 后台在 Anthropic 托管基础设施上起一台**全新隔离 VM**（Ubuntu 24.04 x86_64，与本地系统架构无关）。
2. VM 把仓库 clone 下来（GitHub 凭证走安全代理，真实 token 不进入 VM）。
3. 如果所选 **Environment** 配置了 setup script，跑一次装依赖/工具。
4. Claude Code 本体启动，执行仓库里的 SessionStart hook、读取 CLAUDE.md，随后开始对话。
5. Session 闲置一段时间后 VM 被回收；没有 `commit` + `push` 的改动会随之消失。

VM 自带常见语言运行时/工具链（Python/Node/Ruby/PHP/Java/Go/Rust/Docker/PostgreSQL/Redis/git/gh 等），资源上限约 **4 vCPU / 16GB 内存 / 30GB 磁盘**。

## 2. Environment 配置（在哪改、改什么）

在 claude.ai/code 消息框上方的云图标处打开 Environment 选择器，可以新建/编辑：

- **Name**：环境名称。
- **Network access**：`Trusted`（默认，白名单常见包管理器域名）/ `None`（断网）/ `Full`（不限）/ `Custom`。
- **Environment variables**、**Setup script**：装依赖/配置工具用。

**Setup script 缓存机制**：第一次跑完后，系统会对整台 VM 文件系统打快照，之后新 session 复用快照、跳过脚本，约 7 天过期或改了脚本/网络白名单才重建。**注意**：这个缓存只覆盖 setup script 装的东西，不包含 Claude Code 插件安装（见第 5 节）。

本仓库当前使用的是 **Default** 环境，只设置了 `Trusted` 网络访问，未配置 setup script / 环境变量。

### 2.1 Python monorepo 推荐 Setup script（待子项目建好后启用）

本仓库是多个独立 Python 小项目的 monorepo，子项目还没建时不适合在 setup script 里预装具体依赖——那部分留给 Claude 进入某个子文件夹时按 `requirements.txt` / `pyproject.toml` 自己建虚拟环境装（见根目录 `CLAUDE.md` 的「Python 开发环境」一节）。setup script 只做通用、跟具体子项目无关的准备：

```bash
#!/bin/bash
set -e

# 确认 Python 版本（VM 自带 Python，一般不用额外装）
python3 --version

# 装 pipx：优先 apt-get，失败就退回 pip --user 方式。
# 本 VM 镜像预装了 deadsnakes / ondrej 等第三方 PPA 源，Trusted 网络策略下会被 403 拒绝，
# 导致 apt-get update 整体失败——用子 shell + || 兜底，不让这一步失败提前中断整个脚本。
if ! command -v pipx >/dev/null 2>&1; then
    (apt-get update -qq && apt-get install -y -qq pipx) || \
        python3 -m pip install --user --break-system-packages pipx
fi

# 不管 pipx 是从 apt（/usr/bin）还是 pip --user（~/.local/bin）装的，
# 先把 ~/.local/bin 加进 PATH，保证下面能直接调用 pipx / uv / ruff / black
export PATH="$HOME/.local/bin:$PATH"

# --force：因为上面手动 export 过 PATH，pipx 会觉得"已经在 PATH 里了"从而只给警告、
# 不写入 rc 文件，加 --force 确保它老老实实写进 ~/.bashrc（原因见 2.3）
pipx ensurepath --force

# 这台 VM 镜像本身已经预装了 uv（实测撞见 /root/.local/bin/uv 0.8.17），已有就不重装，
# 避免和已有二进制冲突；真没有才用 pipx 装（原因见 2.3）
if ! command -v uv >/dev/null 2>&1; then
    pipx install --backend pip uv
fi

# --backend pip：pipx 默认会优先用 PATH 上已有的 uv 做自己的加速安装后端，
# 一旦那个预装的 uv 版本不够新（实测撞到 0.8.17 < pipx 要求的 0.9.17），会直接拒绝安装。
# 强制用 pip 后端彻底绕开这个版本兼容性检查（原因见 2.3）
pipx install --backend pip ruff
pipx install --backend pip black

# 校验一下确实装上了，方便在 setup 日志里确认
uv --version
ruff --version
black --version
```

要点：

- 装 pipx 优先走 `apt-get`（Debian/Ubuntu 官方推荐方式），能绕开 PEP 668 的 `externally-managed-environment` 限制；apt 失败时自动退回 `python3 -m pip install --user --break-system-packages pipx`。
- PATH 导出放在 `pipx ensurepath` **之前**：不管 pipx 是走 apt（装在 `/usr/bin`，本来就在 PATH 里）还是走 pip fallback（装在 `~/.local/bin`），后续调用 `pipx`/`uv`/`ruff`/`black` 都得先保证 `~/.local/bin` 在 PATH 里。
- `pipx install` 统一加 `--backend pip`，`uv` 存在与否也做了判断——原因见 2.3，是实测踩出来的坑，不是过度设计。
- **没有装 `pytest`**：`ruff`/`black` 是纯静态工具，不需要 import 项目代码，全局装一份即可跨子项目共用；但 `pytest` 运行测试要 import 被测代码及其运行时依赖，用 `pipx` 隔离安装的话，全局 `pytest` 环境里没有任何子项目的依赖，跑测试大概率会 `ModuleNotFoundError`。`pytest` 应该跟着每个子项目自己的虚拟环境走，由 Claude 建 venv 时按需装。

这套脚本目前**还没有实际配置到 Environment 里**（子项目尚未建立，不着急），先记录在这里，等第一个子项目建好、需要跑测试/lint 时再贴进 Environment 设置弹窗的 Setup script 输入框启用。

### 2.2 已知问题：`apt-get update` 在这台 VM 上会因为预装的第三方 PPA 而失败

实测跑 2.1 的第一版脚本（`apt-get update -qq && apt-get install -y -qq pipx`，不带 fallback）时，Setup script 报错退出码 127：

```
E: Failed to fetch https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/dists/noble/InRelease  403  Forbidden
E: Failed to fetch https://ppa.launchpadcontent.net/ondrej/php/ubuntu/dists/noble/InRelease  403  Forbidden
.../init-script-xxx.sh: line 15: pipx: command not found
```

原因：VM 镜像自带的 apt 源列表里有 `deadsnakes`（额外 Python 版本）、`ondrej/php`（额外 PHP 版本）这两个第三方 PPA，域名 `ppa.launchpadcontent.net` 不在 `Trusted` 网络白名单里，被 403 拒绝。`apt-get update` 只要有一个源失败就整体返回非 0，导致 `apt-get update -qq && apt-get install -y -qq pipx` 里的 `apt-get install` 根本没机会跑；又因为这条失败发生在 `&&` 列表的非最后一个命令上，`set -e` 不会在这里触发（bash 的规则：`&&`/`||` 列表里除最后一个命令外的失败不算数），脚本会悄悄跳过 pipx 安装继续往下跑，直到真正调用 `pipx ensurepath` 时才因为命令不存在而报错退出。

修复（已合入 2.1 的脚本）：apt 失败时显式 fallback 到 `python3 -m pip install --user --break-system-packages pipx`。

### 2.3 已知问题：VM 预装了较旧版本的 `uv`，pipx 拿它当后端会拒绝安装

修了 2.2 之后再测一次，pip fallback 生效、pipx 装上了，但下一步 `pipx install uv` 报错，退出码 1：

```
pipx needs uv>=0.9.17, but /root/.local/bin/uv reports 0.8.17. Upgrade uv (`uv
self update` or reinstall pipx[uv]), or run with `--backend pip` to bypass.
```

原因：这台 VM 镜像本身**已经预装了 `uv`**（`/root/.local/bin/uv`，版本 0.8.17），这一点此前完全没预料到。pipx 1.16.7 默认会优先用 PATH 上已有的 `uv` 作为自己的加速安装后端，但要求 `uv>=0.9.17`；已有版本不够新，pipx 直接拒绝执行并退出。这个检查不止影响"装 uv 这个包"，`pipx install ruff` / `pipx install black` 同样会先过这道检查——脚本只是因为 `set -e` 在第一条 `pipx install uv` 就中断了，没跑到后面两条。

（顺带发现一条无害的噪音：`pipx ensurepath` 输出里有一句 `⚠️ ... try again with the '--force' flag`，大概率是因为脚本手动 `export` 过 PATH，pipx 就不确定要不要再往 `~/.bashrc` 写一遍。这条不是本次失败的原因，但一起加了 `--force` 让它老实写入。）

修复（已合入 2.1 的脚本）：
- `uv` 已存在就跳过安装，避免和预装的二进制冲突；不存在才用 `pipx install --backend pip uv` 装。
- 所有 `pipx install` 都加 `--backend pip`，强制用 pip 而不是 uv 做安装后端，彻底绕开"预装 uv 版本不够新"这个检查，不管以后 VM 镜像里预装的 uv 是什么版本都不受影响。
- `pipx ensurepath` 加 `--force`，确保 PATH 写入 `~/.bashrc` 这件事不会被"看起来已经在 PATH 里了"这种误判跳过。

**修复**：2.1 里的脚本已经改成 `(apt-get update -qq && apt-get install -y -qq pipx) || python3 -m pip install --user --break-system-packages pipx`，apt 这条路失败会显式 fallback 到 pip 安装，不再依赖"失败被 `set -e` 正确捕获"这件事本身。

## 3. Harness（Skill / Plugin / MCP）三层来源

Claude Code 本体（工具定义、agent loop、权限模型）是平台自带的，与选哪个仓库无关。真正因仓库而异的是"这个 session 里有哪些 skill/agent/MCP/plugin 可用"，分三层：

| 来源 | 云端是否自动可用 | 说明 |
|---|---|---|
| claude.ai 账号里启用的 skill / plugin | ✅ 自动 | 挂在账号上，任何仓库都自动带 |
| 仓库里提交的 `.claude/skills/`、`.claude/agents/`、`.claude/commands/`、`.claude/settings.json`（hooks/plugins）、`.mcp.json` | ✅ 自动 | commit 进仓库即生效，团队共享、可版本控制 |
| 本机 `~/.claude/` 下的个人配置 | ❌ 不带 | 只存在本地笔记本上，不会同步到云端 |

## 4. Session 过期 vs 数据保留期限（两个独立的机制，容易混淆）

- **VM 因不活跃被回收**：session 显示 `expired`，但**对话历史不受影响**。重新打开会生成一台新 VM 并**恢复对话记录**。新 VM 是重新 `git clone` 出来的，只包含**已经 push 到 GitHub** 的内容——所以真正会丢的是"没提交的代码改动"，不是"对话内容本身"。
- **账号级数据保留期限**（与 VM 是否活跃无关的独立时钟）：
  - Free/Pro/Max 个人账号：开启"允许数据用于改进模型" → 保留 **5 年**；关闭 → 保留 **30 天**。二选一的固定值，非浮动区间。设置位置：[claude.ai/settings/data-privacy-controls](https://claude.ai/settings/data-privacy-controls)。
  - 手动**删除** session：立即永久生效，不受上述窗口限制。

一句话总结：VM 回收换新 VM、重新 clone 仓库，但对话记录不受影响；真正"连对话记录都没了"要等到账号级保留期到期，或手动删除 session。commit + push 是唯一能百分百自控、不依赖任何保留策略的代码持久化方式。

## 5. 云端 vs 本地开发对比

| 维度 | 云端（claude.ai/code） | 本地 CLI |
|---|---|---|
| 运行位置 | 隔离 VM，资源上限 4vCPU/16GB/30GB | 本机全部资源 |
| 接入方式 | 浏览器/手机 App，电脑不用开机 | 需要本机终端跑 `claude` |
| 持久性 | 不 push 就丢（依赖缓存约留 7 天） | 本机文件系统天然持久 |
| 命令执行 | 无 shell，命令都是 Claude 代跑 | 可与 Claude 共用同一终端 |
| 密钥/凭证 | 无专门 secrets store；GitHub 凭证走代理不进 VM | 可用本机所有已登录凭证 |
| 并行任务 | 轻松同时开多个独立 session | 受限于本机资源 |
| 手机可控 | ✅ 原生支持 | 需另开 Remote Control 桥接 |

**Token 消耗**：云端与本地共享同一账号额度池（rate limit），VM 本身不额外收费——"There is no separate compute charge for the cloud VM"。并行开多个 session 会叠加消耗，但云端本身不比本地贵。

## 6. 本仓库当前已启用的插件：ponytail + superpowers

已提交 `.claude/settings.json`：

```json
{
  "extraKnownMarketplaces": {
    "ponytail": { "source": { "source": "github", "repo": "DietrichGebert/ponytail" } }
  },
  "enabledPlugins": {
    "ponytail@ponytail": true,
    "superpowers@claude-plugins-official": true
  }
}
```

- `extraKnownMarketplaces.ponytail`：注册一个额外插件市场源，指向 `DietrichGebert/ponytail` 仓库（它没有官方市场，只能这样直接指向自己仓库）。
- `enabledPlugins`："插件名@市场名" 格式：
  - `ponytail@ponytail`：YAGNI / 极简代码风格 skill，MIT 协议，装前已 clone 仓库读过 README、SKILL.md、hook 源码及 plugin/marketplace 清单，确认是真实活跃维护的项目、内容无异常。
  - `superpowers@claude-plugins-official`：TDD / 系统化调试 / 写计划工作流 skill 库，作者 Jesse Vincent（Prime Radiant），已上架 **Anthropic 官方插件市场**（`claude-plugins-official`），是比直接指向第三方仓库更安全的安装路径。其核心 skill `using-superpowers` 措辞强势（"1% 可能适用也必须调用"），会让 Claude 更主动触发它的技能集，这是设计如此。

**重要**：这两个插件只会被下载安装到**新 session 的 VM 本地缓存**里，不会再写回本仓库——仓库里能看到的，也就到上面这段 `.claude/settings.json` 为止。安装动作发生在 Claude Code 启动之后（"at session start"），晚于 setup script 的快照缓存点，因此大概率**不会**被第 2 节提到的 7 天快照缓存覆盖，每次新 session 大概率会重新拉取一遍（不过插件本身是文本文件，体积小，重新拉取也很快）。要看到这两个插件生效，需要**新开一个 session**，当前已经在跑的 session 不会追溯生效。

## 7. 分支说明

本仓库默认分支是 **`master`**（没有 `main`）。`.claude/settings.json` 已直接提交并推送到 `master`，同时同步到了开发分支 `claude/claude-ai-code-cloud-dev-xhk5yz`。
