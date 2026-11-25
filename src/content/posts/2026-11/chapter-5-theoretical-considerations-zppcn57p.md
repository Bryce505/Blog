---
draft: true
reviewNotes:
  - "正文过短: 4059/13096=31% < 40%"
  - "正文有指向知识库内部 md 的相对链接（站上是死链）4 处: ['[计算ELISA cut-off value](Analytical technology/ELISA Assay/计算ELISA cut-off value.md)', '[抗体滴度（antibody titer & titration）](Analytical technology/ELISA Assay/抗体滴度（antibody titer & titration）.md)', '[方法验证](Quality_and_Regulation/方法验证.md)']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,526 字符（原文 16,470，比例 27%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答"
date: 2026-11-25
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的检测性能并非只由试剂盒的配方决定，其上限首先由抗原本身的性质和所用抗体的结合特性划定。这篇笔记从抗原性出发，依次梳理表位相关术语、affinity 与 avidity 的区分，再落到抗血清稀释效应和不同免疫方式对检测设计的影响，目的是为方法的建立与结果解释提供一层理"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的检测性能并非只由试剂盒的配方决定，其上限首先由抗原本身的性质和所用抗体的结合特性划定。这篇笔记从抗原性出发，依次梳理表位相关术语、affinity 与 avidity 的区分，再落到抗血清稀释效应和不同免疫方式对检测设计的影响，目的是为方法的建立与结果解释提供一层理论参照。

## 抗原性首先取决于分子大小与可及表面积

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。这一估算有其前提：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009）——即这样的计算是基于整个表面具有抗原性(很少是真实的)和分子最大结合的事实。

在应用层面，这一思路可用于 calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface（Crowther, 2009）。换句话说，它给出的是饱和所需抗体量与表面可及性之间关系的量级估计，而非精确值。

## 表位相关的基本术语

讨论抗体结合之前，需要先厘清几个容易混用的概念。

- **epitope**：即 antigenic site，抗原上被抗体识别的位点。
- **epitype**：An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site（Crowther, 2009）。也就是说，表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别；表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。
- **paratope**：抗体上结合抗原表位的部分。

## affinity：单个结合位点上的结合能

affinity（binding affinity）有三层表述，彼此一致：一是单个 epitope 与 paratope 之间的能量；二是 the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope **at a singular binding site**；三是 affinity is mediated by **non-covalent interactions** that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium **dissociation constant (K_D)**。

要点在于“单价”——affinity 描述的始终是一个位点对位点的相互作用强度，其大小由非共价作用力构成，并以平衡解离常数 K_D 表征。

## avidity：多个位点结合能的总和

avidity 又称 functional affinity，指与抗原结合的总结合能。The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites（Crowther, 2009）。另一种表述是：the measure of the total binding strength of an antibody at every binding site is termed avidity。

影响 avidity 的因素有三个：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。因此，avidity 不能由单一的 K_D 推出，它同时取决于抗体价数和分子间的几何排布。

## 抗血清稀释会改变 avidity，也改变抗原辨别力

Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)（Crowther, 2009）。既然针对的是异质性抗体群体，就必须注意：the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies（Crowther, 2009）。

一个具体的例子可以说明这种效应的量级：血清中可能同时存在 a low quantity of antibodies showing high affinity 与 a high quantity of low-affinity antibody。在 not diluted greatly 的免疫分析条件下，高亲和力与低亲和力抗体竞争抗原位点，the high-affinity antibodies would react preferentially；而一经稀释，高亲和力抗体的浓度持续下降，直至体系中只剩下低亲和力抗体。

这一现象的实践含义是明确的：当使用免疫分析、通过不同抗血清的差异活性来比较抗原时，The dilution of any serum can affect its ability to discriminate between antigens，其根源在于异质性抗体群体的动力学（各个抗体分子的相对浓度与亲和力）。因此，工作稀释度的选择本身就是方法学决策的一部分，而不只是操作便利问题。

## 免疫方式与抗体类型对检测设计的约束

抗原刺激机体产生的通常是多克隆抗体，且抗体类型并不仅限于 IgG；各类抗体产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

免疫策略本身也决定了后续该选什么形式的检测。被动免疫（passive immunization）是直接注射中和抗体；主动免疫（active immunization）则是给予抗原、由机体产生保护性抗体。

就疫苗而言，sc（皮下注射）或 im（肌内注射）的接种方式可以诱导产生多种抗体类型（isotype）。因此在评估疫苗接种效果时，必须考虑检测形式的选择：是用总抗体检测、isotype-specific assay，还是检测抗原清除。

对于口服/吸入途径的免疫，问题更为具体：the immunoassayist must decide whether an assay for **isotype-specific antibodies**, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for **total antibody**（Crowther, 2009）。也就是说，免疫学家必须判断，同型抗体（特别是 IgA）的检测能否比总抗体检测更深入地反映疫苗接种的获益。

## 这些理论前提的适用边界

把上述内容串起来看，可以看到一条从抗原本性到检测设计的约束链：分子大小与表面积决定了可结合位点数的上限估算，但该估算建立在“全表面具抗原性”与“最大结合”两个很少同时成立的假设之上；affinity 描述单价相互作用的强度，avidity 才是多价、多表位体系的总体表现，其大小受亲和力、价数与结构排布共同影响；血清作为异质性抗体群体，其 avidity 会随稀释而改变，进而影响不同抗原之间的辨别能力。

由此，检测形式的选择——总抗体还是 isotype-specific、在何种稀释度下比较——并非纯粹的操作细节，而是受制于上述理论前提的方法学决策。需要留意的未决之处也正在这里：饱和位点数与所需抗体量的估算只能给出量级；稀释对异质性抗体群体的影响因血清而异，难以用统一参数概括。

## 相关笔记

- [计算ELISA cut-off value](Analytical technology/ELISA Assay/计算ELISA cut-off value.md)
- [夹心ELISA(sandwich ELISA)定量法](Analytical technology/ELISA Assay/夹心ELISA(sandwich ELISA)定量法.md)
- [抗体滴度（antibody titer & titration）](Analytical technology/ELISA Assay/抗体滴度（antibody titer & titration）.md)
- [方法验证](Quality_and_Regulation/方法验证.md)
- [EC50&ED50 计算](Analytical technology/ELISA Assay/EC50&ED50 计算.md)