---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['135']"
  - "正文过短: 3026/13096=23% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,823 字符（原文 16,470，比例 17%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原决定簇、抗体亲和力与免疫应答"
date: 2026-11-25
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理 ELISA 理论部分的几个前置概念：抗原大小与可结合表位数量的估算方法及其前提，epitope / epitype / paratope 与 affinity / avidity 这两组容易混淆的术语，以及血清稀释和免疫途径如何改变抗体的结合行为与检测设计。顺序按「抗原"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理 ELISA 理论部分的几个前置概念：抗原大小与可结合表位数量的估算方法及其前提，epitope / epitype / paratope 与 affinity / avidity 这两组容易混淆的术语，以及血清稀释和免疫途径如何改变抗体的结合行为与检测设计。顺序按「抗原—抗体—免疫应答」展开，落点都在那些会直接影响检测结果解释的地方。

## 分子大小如何约束可结合的表位数量

分子越大，其复杂性也就越高。Fab 与抗原结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量；

这个估算有明确的前提，不能当作实测值使用：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）

即计算假设整个表面都具有抗原性（这很少成立），且分子达到最大结合。

它的实际用途是反过来的：计算饱和任一试剂需要多少抗体，或测定抗体结合量随可用表面的变化（Crowther, 2009, p. 127）。

## 表位、表位型与互补位

三个术语各指结合界面上不同层次的对象：

- **epitope**：antigenic site，即抗原上被抗体识别的位点。
- **epitype**：抗原上的一个区域，由一组化学结构非常相似的抗体识别。原文定义为"an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes)"，可视为识别与同一抗原位点反应的、特异性略有差异的抗体的区域（Crowther, 2009, p. 128）。
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力不是同一件事

### affinity：单一结合位点上的结合强度

affinity（结合亲和力）包含三层含义：其一，单个 epitope 与 paratope 之间的能量；其二，抗原表位与抗体互补位在**单一结合位点**上的相互作用强度；其三，这种相互作用由非共价作用介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡解离常数（K<sub>D</sub>）定义。

### avidity：多个位点叠加后的总体结合强度

avidity 又称 functional affinity（功能性亲和力），指与抗原的总体结合能，是抗体在所有结合位点上总结合强度的量度：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009, p. 130）

影响 avidity 的因素有三个：binding affinity、valency（效价），以及抗体与抗原的结构排布。

在血清这一层面，avidity 可以看作血清中包含的异质性抗体与各种抗原位点之间所有不同亲和力的总和（Crowther, 2009, p. 137）。

## 稀释会改变血清的表观亲合力

一个在方法设计上必须留意的效应：血清的 avidity 在稀释时可能发生变化，因为操作者可能把某些抗体群稀释掉了（Crowther, 2009, p. 137）。

典型情形是血清中同时存在**少量高亲和力抗体**与**大量低亲和力抗体**。在血清未大幅稀释的免疫分析条件下，两类抗体竞争抗原位点，高亲和力抗体优先反应；随着稀释进行，高亲和力抗体浓度下降，最终只剩低亲和力抗体在起作用。当操作者用免疫分析、以不同抗血清的差异活性来比较抗原时，这类问题尤其重要——由于异质抗体群的动态（各抗体的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力（Crowther, 2009, p. 137）。

## 免疫途径决定了要检测哪一类抗体

抗原刺激后产生的是多克隆抗体，且抗体类型并不限于 IgG；各抗体类型出现的时间顺序见下图（Crowther, 2009, p. 135）：

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

被动免疫（passive immunization）是直接注射中和抗体；主动免疫（active immunization）则是接种抗原、由机体产生保护性抗体。

疫苗通常经 sc（皮下注射）或 im（肌内注射）途径接种，这种方式可诱导产生多种抗体类型（isotype）。因此，评估疫苗接种效果时必须先决定用哪一类检测：总抗体检测、isotype-specific assay，还是检测抗原清除。

口服或吸入免疫的情形下，这个问题更突出：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）

## 概念边界与遗留问题

几个概念的适用边界可以这样归纳：表面除法得到的是 Fab 结合位点数的**上限**，成立与否取决于「整个表面都有抗原性」和「分子最大结合」两个几乎不会完全满足的假设；affinity 描述单一 paratope–epitope 对的强度，avidity 描述多位点、多克隆背景下的总体强度，两者不可互换使用；avidity 不是血清的固有常数，稀释即可改变其实测值，因此在做不同抗血清之间的抗原比较时，稀释方案本身就是变量。

由此遗留的问题是检测策略的选择：疫苗接种后究竟以总抗体、isotype-specific 抗体（尤其 IgA）还是抗原清除作为评价指标，原文并未给出通用答案，而是把它留给具体体系判断。