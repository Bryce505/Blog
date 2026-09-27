---
draft: true
reviewNotes:
  - "正文过短: 3205/13045=25% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,062 字符（原文 16,405，比例 19%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与亲合力"
date: 2026-09-27
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "免疫检测的读数最终受制于抗原与抗体相互作用的物理化学性质。这篇文章整理 Crowther《The ELISA Guidebook》第 5 章的理论部分，依次说明抗原尺寸对可结合位点数的限制、表位相关术语的界定、affinity 与 avidity 的区别，以及免疫方式如何决定抗体"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

免疫检测的读数最终受制于抗原与抗体相互作用的物理化学性质。这篇文章整理 Crowther《The ELISA Guidebook》第 5 章的理论部分，依次说明抗原尺寸对可结合位点数的限制、表位相关术语的界定、affinity 与 avidity 的区别，以及免疫方式如何决定抗体类型与检测策略的选择。

## 抗原尺寸决定可结合 Fab 位点数的上限

分子越大，其复杂性也就越高。Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有明确的前提限制：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）

也就是说，这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

在应用层面，该估算可用于计算饱和某一试剂所需的抗体量，或测定抗体结合水平随可用表面的变化（"calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"）。

## epitope、epitype 与 paratope 的界定

- **epitope**：antigenic site，即抗原表位。
- **epitype**：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。
- **paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity 是两个层次的结合强度

### affinity：单个结合位点的结合能

笔记中给出了 affinity 的几种等价表述：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗原的 epitope 与抗体的 paratope 在单个结合位点（singular binding site）上的相互作用强度；
3. 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." —— 抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity：功能性亲和力

1. 与抗原的总结合能。亲合力代表一个抗体群体与不同抗原位点结合时各个亲和力的总和所给出的平均结合能（"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"）；
2. 抗体在每个结合位点上总结合强度的量度称为 avidity，也称为 functional affinity；
3. 亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和；
4. 三个影响因素：1) 结合亲和力，2) 价数（valency），3) 抗体与抗原的结构排布。

## 稀释会改变血清的表观亲合力

血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释掉某些群体的抗体（"It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"）。

举例来说，血清中可能含有少量对某一复杂抗原高亲和力的抗体和大量低亲和力抗体。在血清未被大幅稀释的免疫检测条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；稀释后，高亲和力抗体的浓度不断下降，直到只剩下低亲和力抗体。当操作者用免疫检测比较不同抗血清对抗原的差异活性时，这类问题很重要；由于异质性抗体群体的动力学（各个抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力。

## 免疫方式决定抗体类型与检测读数的选择

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### passive 与 active immunization

- passive immunization：直接打中和抗体；
- active immunization：服用抗原，产生保护性抗体。

### 接种途径与检测策略

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫则带来另一层判断：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）—— 免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 小结

上述几个概念各自划定了免疫检测读数的一个边界：

- 用球形表面积除以 20 得到的只是 Fab 结合位点数的上限，因为"整个表面均具抗原性"和"分子最大结合"这两个前提很少同时成立；
- affinity 描述单个 epitope–paratope 对的结合能，由氢键、静电键、范德华力、疏水作用等非共价相互作用介导，并由 K_D 定义；avidity 描述抗体群体对多个抗原位点的总体结合能，受结合亲和力、价数与抗体–抗原结构排布三者影响；
- avidity 依赖异质抗体群体的组成，因此血清稀释本身就会改变表观亲合力，进而影响用不同抗血清区分抗原的能力；
- 免疫途径（sc/im 与口服/吸入）决定了所产生的 isotype 谱，因而在评估疫苗接种效果之前，就要在总抗体检测、isotype-specific assay 与抗原清除检测之间作出选择。