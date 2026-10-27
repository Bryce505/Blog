---
draft: true
reviewNotes:
  - "正文过短: 3066/13096=23% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,433 字符（原文 16,470，比例 21%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与免疫应答的检测选择"
date: 2026-10-27
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记梳理 ELISA 及其他免疫分析在方法设计前必须想清楚的几件理论事情：抗原分子的大小如何决定可结合位点的数量上限，epitope / epitype / paratope 几个术语的边界在哪里，affinity 与 avidity 为何不能互相替代，以及用免疫分析评价疫苗"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记梳理 ELISA 及其他免疫分析在方法设计前必须想清楚的几件理论事情：抗原分子的大小如何决定可结合位点的数量上限，epitope / epitype / paratope 几个术语的边界在哪里，affinity 与 avidity 为何不能互相替代，以及用免疫分析评价疫苗接种效果时，检测对象（总抗体、isotype-specific 抗体还是抗原清除）应当如何取舍。

## 抗原的分子大小决定了可结合位点的数量上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20 nm²，也就是 epitope 的表面积。通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

需要强调的是这个估算的前提：「Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally」（Crowther, 2009, p. 127）—— 整个表面都具有抗原性（很少成立），且分子达到最大结合。

它的实际用途在于：calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface（Crowther, 2009, p. 127）。

## 表位相关术语的界定

**epitope**：antigenic site，即抗原决定簇。

**epitype**：「An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site」（Crowther, 2009, p. 128）。即：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如定义重叠或相互关联表位的 mAb）所识别；它也可视为识别同一抗原位点、但特异性略有差异的抗体所对应的区域。

**paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单点强度与整体强度

**affinity（binding affinity）** 指单一结合位点上的结合强度，可以从三个层面表述：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗原表位与抗体 paratope 在**单一结合位点**上相互作用的强度；
3. 由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡**解离常数（K_D）**来定义。

**avidity（functional affinity，功能亲和力）** 则是整体层面的量度：

1. 与抗原的总结合能 ——「The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites」（Crowther, 2009, p. 130）；
2. 抗体在每个结合位点上总结合强度的量度，又称 functional affinity；
3. 三个影响因素：**the binding affinity、valency，以及抗体与抗原的结构排布**。

在多克隆血清的语境下，「Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)」（Crowther, 2009, p. 137）。

## 稀释会改变血清的表观 avidity

「It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies」（Crowther, 2009, p. 137）。

一个典型情形是：血清中**少量高亲和力抗体**与**大量低亲和力抗体**并存。在血清**未大幅稀释**的免疫分析条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度被降低，直至体系中只剩低亲和力抗体。

「Such problems are important」当操作者用免疫分析、以不同抗血清的差异活性来比较抗原时；「The dilution of any serum can affect its ability to discriminate between antigens」，其根源在于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力）。

## 抗体应答的异质性与免疫接种效果的检测选择

抗原刺激后产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

（Crowther, 2009）

**被动免疫与主动免疫**：passive immunization 是直接注射中和抗体；active immunization 是给予抗原，使机体产生保护性抗体。

**接种途径**：疫苗注射方式为 sc（皮下注射）或 im（肌内注射）。这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑是否使用总抗体检测、isotype-specific assay，或检测抗原清除的检测来评估疫苗接种效果。

**口服/吸入免疫**：此时「The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody」（Crowther, 2009, p. 140）—— 即需要判断同型抗体（特别是 IgA）的检测是否比总抗体检测更能反映疫苗接种的获益。

## 小结

这一章的理论线索可以收敛为两点：抗原侧，可结合位点数受分子表面积与「表面是否真的具有抗原性、是否真的饱和结合」两个假设的约束，20 nm² 的估算只给出上限；抗体侧，affinity 描述单个 paratope–epitope 的强度（以 K_D、非共价作用表征），avidity 描述多点结合的总和，受 affinity、valency 与结构排布三者共同影响，并且在多克隆血清中会随稀释而改变。正因如此，疫苗接种后究竟测总抗体、测 isotype-specific 抗体（尤其 IgA）还是测抗原清除，需要在方法设计阶段就依据免疫途径与应答的异质性做出判断，而不能默认通用。