---
draft: true
reviewNotes:
  - "正文过短: 2403/13045=18% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,483 字符（原文 16,405，比例 15%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原特性、抗体结合强度与免疫应答"
date: 2026-10-06
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理自 Crowther《ELISA Guidebook》第 5 章的理论部分，讨论三个层面的问题：抗原本身的特性如何限制可结合位点的数量，epitope、paratope 与 affinity、avidity 这几个术语的准确含义，以及抗体免疫应答（包括免疫途径）如何决定检"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理自 Crowther《ELISA Guidebook》第 5 章的理论部分，讨论三个层面的问题：抗原本身的特性如何限制可结合位点的数量，epitope、paratope 与 affinity、avidity 这几个术语的准确含义，以及抗体免疫应答（包括免疫途径）如何决定检测策略的选择。全篇围绕「检测体系中的结合事件由什么决定」展开，不涉及具体操作步骤。

## 抗原大小如何决定可结合位点数量的估算上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

需要明确的是，这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合这两个事实（Crowther, 2009）。也就是说，这个数字给出的是理论上限，而不是实际可用的表位数。

该估算的用途有两个方向：计算饱和任一试剂所需的抗体量，或测量抗体结合水平随可用表面积的变化（Crowther, 2009）。

## epitope、epitype 与 paratope 的定义区分

三个术语常被混用，各自的指向不同：

- **epitope**：即 antigenic site，抗原位点。
- **epitype（表位型）**：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的、抗体特异性略有不同的区域（Crowther, 2009）。
- **paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单一位点强度与整体结合强度

### affinity（binding affinity）

affinity 描述的是单一结合位点上的相互作用强度：它既是单个 epitope 与 paratope 之间的能量，也是抗原表位与抗体 paratope 在 singular binding site 上的结合强度。affinity 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

### avidity（functional affinity）

avidity 指与抗原的总结合能，是抗体在每个结合位点上的总结合强度，也称 functional affinity。它代表一群结合不同抗原位点的抗体各自 affinity 之和的平均结合能（Crowther, 2009）。

avidity 受三个因素影响：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

在血清层面，avidity 也可视作血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和（Crowther, 2009）。

## 血清稀释为什么会改变 avidity 与抗原区分能力

血清的 avidity 在稀释时可能会发生变化，因为操作者可能会稀释掉某些群体的抗体（Crowther, 2009）。

一个典型情形是：血清中同时含有**少量**对某一复杂抗原**高亲和力**的抗体和**大量低亲和力**抗体。在血清**未被大幅稀释**的免疫检测条件下，高亲和力与低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；而一旦稀释，高亲和力抗体的浓度会被降低，最终只剩下低亲和力抗体。当操作者用免疫检测、通过不同抗血清对抗原的差异活性来比较抗原时，这一问题尤为重要——任何血清的稀释都可能影响其区分抗原的能力，原因在于异质性抗体群体的动力学（各个抗体分子的相对浓度与亲和力）（Crowther, 2009）。

## 抗原刺激产生的抗体类型与免疫途径

应对抗原刺激产生抗体时，产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

（Crowther, 2009）

### 被动免疫与主动免疫

- **passive immunization**：直接打中和抗体；
- **active immunization**：服用抗原，产生保护性抗体。

### 免疫途径与检测对象的选择

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑是否使用总抗体检测、isotype-specific assay，或检测抗原清除的检测来评估疫苗接种效果。

对于口服/吸入免疫，免疫检测工作者必须决定：isotype-specific 抗体（尤其是 IgA）的检测，是否可能比总抗体检测更深入地说明疫苗接种的获益（Crowther, 2009, p. 140）。

## 这些理论前提的适用边界

把上面几条归拢一下，可以看到各自成立的边界在哪里：

Fab 结合位点数量的计算只是上限值。它建立在「整个表面都具有抗原性」和「分子最大结合」这两个前提上，而这两者很少同时成立，因此该数值不能直接当作实际表位数使用。

affinity 描述单一位点，avidity 描述整体。由于 avidity 取决于抗体群体的组成，同一份血清在不同稀释度下的 avidity 可以不同；用它来比较不同抗血清对抗原的区分能力时，稀释条件本身就是变量，而不是可以忽略的操作细节。

免疫途径决定产生的 isotype 谱，进而决定检测策略应当选择总抗体、isotype-specific 抗体还是抗原清除。至于某一条途径下是否值得做 isotype-specific 检测，笔记中把它留作需要由检测开发者判断的问题，并未给出统一答案。