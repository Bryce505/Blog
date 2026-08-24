# 手动发布投递口

把写好的 md 扔进这个目录，push 上去就会发布。

## 最少只要一个字段

```yaml
---
title: 文章标题
---
```

其余全部可选，缺省行为：

| 字段 | 不写会怎样 |
|---|---|
| `slug` | 由文件名生成（`my-post.md` → `my-post`，中文保留） |
| `date` | 取该文件首次提交的日期，取不到用当天 |
| `tags` | 空 |
| `category` | 从 `tags` 的一级标签推导；无标签则归入「杂记」 |
| `description` | 取正文前 120 字（自动去掉 markdown 标记） |
| `references` | 空 |

## 这个通道替你做的事

从 Obsidian 直接导出的稿子里，图片写的是 `![](../image&attachment/xxx.png)`、
双链写的是 `[[目标笔记]]`，直接发出去是一堆破图和方括号。这里会：

- 从 Google Drive 拉取引用的图片，转 WebP（限宽 1200px）存进仓库
- 把 `[[双链]]` 转成站内链接；目标未发布则退化成纯文字，不留死链

**不经过 DeepSeek，不经过机械校验** —— 自己写的内容不需要防篡改，跑一遍
纯属浪费时间和 token。

## 注意

- 发布成功后本目录里的原文件会被**删除**（已转存到 `src/content/posts/`），
  留着会被重复处理
- slug 与已有文章冲突时**报错跳过、保留原件**，不会静默覆盖
- 没写 `title` 的会报错跳过，原件保留
- 本 `README.md` 不会被当成稿子

## 手动跑一次

```bash
export GDRIVE_SA_JSON="$(cat 服务账号.json)"
python pipeline/main.py --drafts
```
