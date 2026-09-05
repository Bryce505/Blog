---
title: 画布工作文件
date: '2026-09-05'
category: 工具与效率
tags:
- 工具与效率/乌司他丁
description: 乌司他丁技术文档.html（上级目录）与在线画布均由这些文件生成，不要直接改生成物。 | 文件 | 作用 | |---|---| | gen.py
  | 从 ../乌司他丁.docx 解析结构，输出 body.frag.html / toc.
---

`乌司他丁技术文档.html`（上级目录）与在线画布均由这些文件生成，**不要直接改生成物**。

| 文件 | 作用 |
|---|---|
| `gen.py` | 从 `../乌司他丁.docx` 解析结构，输出 `body.frag.html` / `toc.frag.html` |
| `Main.dc.html` | 画布画板：设计系统 CSS + 版面 + 正文 |
| `canvas.json` | 画布布局（单幅流式画板，A4 794px 栏宽，print: flow） |
| `img/` | 9 张原图重采样版（约 1.4 倍显示密度） |

重新生成在线画布：

```bash
node <design skill>/seed-canvas.mjs \
  --template <design skill>/payload.template.html \
  --out ulinastatin-structure-activity.html \
  --title "乌司他丁技术文档" \
  --artboard Main.dc.html --canvas canvas.json \
  $(for f in img/*.jpg; do printf -- "--image %s " "$f"; done)
```

在线画布：https://claude.ai/code/artifact/239afd33-d4d3-4de7-bd92-137de24f6444
