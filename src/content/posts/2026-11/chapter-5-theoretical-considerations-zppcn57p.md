---
draft: true
reviewNotes:
  - "正文过短: 2512/13096=19% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,637 字符（原文 16,470，比例 16%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答"
date: 2026-11-21
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的很多设计选择——包被多少抗原、抗体稀释到几倍、测总抗体还是测某一 isotype——背后都对应着一组可以讲清楚的理论前提。这篇笔记按“抗原侧的限制条件、术语界定、affinity 与 avidity 的区分、稀释带来的偏差、免疫方式与检测策略”的顺序，把这些前提梳理"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的很多设计选择——包被多少抗原、抗体稀释到几倍、测总抗体还是测某一 isotype——背后都对应着一组可以讲清楚的理论前提。这篇笔记按“抗原侧的限制条件、术语界定、affinity 与 avidity 的区分、稀释带来的偏差、免疫方式与检测策略”的顺序，把这些前提梳理了一遍。

## 抗原分子的大小如何限定可及表位的数量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个算法有明确的适用边界。原文特别指出：这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实（Crowther, 2009）。因此，算出来的只是理论上限，并不是真实可及的表位数。

在应用层面，它主要用在两种情况：

> “calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface” (Crowther, 2009)

也就是说，它既能用来估算饱和一定量抗原需要多少抗体，也能用来把“抗体结合量”表达为“可用表面”的函数。

## epitope、epitype 与 paratope 的界定

三个术语容易混用，笔记里做了区分：

- **epitope**：即 antigenic site，抗原上被抗体识别的位点。
- **epitype（表位型）**：抗原上的一个区域，由一组化学结构非常相似的抗体识别。原文的表述是“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”(Crowther, 2009)。它刻画的是针对同一抗原位点、特异性略有差异的那一批抗体所共同界定的区域。
- **paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单价结合能与整体结合强度

### affinity 是单一结合位点上的能量

affinity 指的是单个 epitope 与 paratope 之间的结合能，也就是抗体表位与抗体 paratope 在**单一结合位点**上相互作用的强度。它由非共价相互作用介导，包括氢键、静电作用、范德华力和疏水相互作用，并以平衡解离常数（K<sub>D</sub>）来定义。

### avidity 是“功能性亲和力”

avidity 是在每个结合位点上对抗体总结合强度的度量，也称为 functional affinity。两层表述：

- 它代表一群体抗体与不同抗原位点结合时，各个单独 affinity 之和所给出的平均结合能（Crowther, 2009）。
- 在抗血清语境下，avidity 可以看作血清中所含异质性抗体与各种抗原位点（epitopes）之间所有不同亲和力的总和（Crowther, 2009）。

影响 avidity 的因素有三个：binding affinity、valency，以及抗体与抗原本身的结构排布。

## 稀释会改变血清的表观亲和力

这一点在多抗血清上尤其需要注意：血清的 avidity 可能在稀释过程中发生变化，因为操作者有可能把某些抗体群体稀释掉了（Crowther, 2009）。

一个典型情形是：血清中同时存在**少量高亲和力抗体**和**大量低亲和力抗体**。在稀释倍数不大的免疫测定条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；而一旦稀释，高亲和力抗体的浓度被逐步降低，最后只剩下低亲和力抗体。

这个现象在以下操作中会直接影响结论：用免疫测定比较不同抗原与不同抗血清的反应性差异时，任何血清的稀释都可能改变它区分抗原的能力，原因在于异质性抗体群体的动力学——各抗体分子的相对浓度与亲和力共同决定了这一点（Crowther, 2009）。

## 免疫方式决定该测哪一类抗体

### 被动免疫与主动免疫

- passive immunization：直接注射中和抗体。
- active immunization：接种抗原，由机体产生保护性抗体。

### 接种途径与 isotype

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：是用总抗体检测、isotype-specific assay，还是检测抗原清除来评估疫苗接种效果。

口服或吸入免疫则引出另一个问题：免疫测定工作者必须判断，检测 isotype-specific 抗体（尤其是 IgA）是否比检测总抗体更能反映疫苗接种带来的收益（Crowther, 2009, p. 140）。

各抗体类型的产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 小结

这组理论前提的共同特征，是它们给出的多为上限或理想条件下的描述：由球形表面积推算的 Fab 结合位点数，前提是“整个表面都具有抗原性”且“分子最大结合”，而这两条在真实抗原上很少同时成立。反过来，avidity 这样的整体指标又依赖抗体群体的组成，会随稀释而漂移，使得跨样品、跨抗血清的比较需要谨慎对待稀释方案。至于免疫后究竟该测总抗体还是某一 isotype，笔记没有给出通用答案，而是把它留作一个必须结合疫苗类型与免疫途径逐案判断的问题。