---
draft: true
reviewNotes:
  - "正文过短: 4331/13045=33% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,384 字符（原文 16,405，比例 27%）超出 9,023～15,585 字符的区间"
title: "ELISA 理论基础：从抗原表位、抗体亲和力到免疫应答的检测选择"
date: 2026-10-13
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本文整理 ELISA 理论层面的几个核心概念，按「抗原—抗体相互作用—血清整体行为—免疫应答与检测选择」的顺序组织：先看抗原大小与可结合位点数的关系，再厘清表位、表位型与互补位的定义，进而区分 affinity 与 avidity 及稀释带来的影响，最后落到免疫途径与抗体检测策略"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本文整理 ELISA 理论层面的几个核心概念，按「抗原—抗体相互作用—血清整体行为—免疫应答与检测选择」的顺序组织：先看抗原大小与可结合位点数的关系，再厘清表位、表位型与互补位的定义，进而区分 affinity 与 avidity 及稀释带来的影响，最后落到免疫途径与抗体检测策略的匹配问题。文中保留 Crowther 原文的关键表述与出处。

## 抗原大小与可结合的 Fab 位点数量

分子越大，其复杂性也就越高。Fab 结合的面积大概是 20 nm²，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一算法的前提必须交代清楚：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"

即：这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实 (Crowther, 2009)。

其应用在于计算饱和任意抗原所需的抗体量，或测量抗体结合量随可用表面的变化 (Crowther, 2009)。

## 表位、表位型与互补位的定义

- **epitope**：antigenic site，即抗原位点。
- **Epitype**：原文定义为 "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009)。即：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别；表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一位点结合能与抗体群体的总强度

### affinity：单一位点的结合强度

affinity 有三层含义，彼此是同一件事的不同侧面：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗体分子与抗原决定簇之间的结合能称为亲和力——"The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009)；
3. 它是抗原 epitope 与抗体 paratope 在单一结合位点上的相互作用强度，由非共价相互作用介导，包括氢键、静电键、Van der Waals 力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

### avidity：异质性抗体亲和力的总和

1. 与抗原的总体结合能。"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009)；
2. 抗体在每个结合位点上的总结合强度称为 avidity，也称 functional affinity；
3. 三个影响因素：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 稀释会改变血清的表观亲合力

avidity 是对血清中异质性抗体群体行为的描述："Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009)。既然是群体求和，"It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009)——血清的亲和力在稀释时可能发生变化，因为操作者可能会稀释掉某些群体的抗体。

这在实际测定中会带来可预期但容易被忽略的后果：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)." (Crowther, 2009)

## 抗体产生方式与检测策略的选择

应对抗原刺激产生抗体时，产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

- **passive immunization**：直接打中和抗体；
- **active immunization**：服用抗原，产生保护性抗体。

疫苗注射方式：sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型-isotype；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫："The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)——免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 适用边界与尚未解决的问题

- 表面积除以 20 nm² 得到的是 Fab 结合位点数的**上限**。它的两个前提——整个表面都具有抗原性、且分子达到最大结合——在真实抗原上很少成立，因此该数值只适合做量级估算，不能当作实测容量使用。
- affinity 与 avidity 描述的是不同尺度的对象：前者是单个 epitope–paratope 的结合强度，后者是抗体群体与多个抗原位点结合的总和，两者不可互换。avidity 同时受 binding affinity、valency 和抗体—抗原结构排布影响，因此单一位点的高亲和力不等于血清水平的高亲合力。
- 血清是异质性抗体群体，稀释会改变其组成，进而改变表观 avidity 以及区分不同抗原的能力。当用不同抗血清比较抗原时，稀释条件本身就是需要控制的变量，而不只是一个操作细节。
- 免疫途径（sc/im 与口服/吸入）决定了所产生的 isotype 谱，相应的检测策略也需匹配：总抗体检测、isotype-specific assay 还是抗原清除检测，取决于评价目标。至于是否值得为 IgA 一类 isotype 单独建立检测，原文将其保留为实验者需要权衡的判断，而非已有定论的问题。