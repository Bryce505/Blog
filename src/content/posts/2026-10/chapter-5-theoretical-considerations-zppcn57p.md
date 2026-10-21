---
draft: true
reviewNotes:
  - "正文过短: 3899/13045=30% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,834 字符（原文 16,405，比例 23%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、亲和力与抗体应答如何决定检测设计"
date: 2026-10-21
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的很多设计选择——包被量、血清稀释度、检测总抗体还是某一 isotype——背后都落在几个理论概念上：抗原能被多少抗体结合、抗体与表位的结合强度如何度量、以及血清作为异质抗体群体在稀释时会怎样变化。这篇笔记按抗原性、抗体结合的度量、抗体应答与检测形式三段整理 Crow"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的很多设计选择——包被量、血清稀释度、检测总抗体还是某一 isotype——背后都落在几个理论概念上：抗原能被多少抗体结合、抗体与表位的结合强度如何度量、以及血清作为异质抗体群体在稀释时会怎样变化。这篇笔记按抗原性、抗体结合的度量、抗体应答与检测形式三段整理 Crowther 在 ELISA Guidebook 第 5 章中的论述，作为滴定与试剂配比的原理背景。

## 抗原性从哪里来：分子大小与表位数量的估算

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。这一估算给出的是上限而非实测值，Crowther 明确指出其前提：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（这样的计算是基于整个表面具有抗原性——而这很少是真实的——以及分子达到最大结合的事实）(Crowther, 2009, p. 127)。

反过来，同样的思路可用于实用目的：“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”(Crowther, 2009, p. 127)。

## 关键术语：epitope、epitype 与 paratope

**epitope** 即 antigenic site；**paratope** 是抗体上结合抗原表位的部分。

**epitype** 描述的是比单一表位更宽的一层概念：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”——表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别；可视为识别与同一抗原位点反应的抗体特异性略有不同的区域 (Crowther, 2009, p. 128)。

## 亲和力与亲合力：不能混用的两个强度指标

### affinity：单一结合位点上的强度

抗体分子与抗原决定簇之间的结合能称为亲和力——“The binding energy between an antibody molecule and an antigen determinant is termed affinity”(Crowther, 2009, p. 136)。具体而言：

- 是单个 epitope 与 paratope 之间的结合能量；
- 是抗原表位与抗体 paratope 在**单一结合位点**上相互作用的强度；
- 由**非共价作用**介导，包括氢键、静电作用、范德华力和疏水相互作用，并以平衡**解离常数（K<sub>D</sub>）**定义。

### avidity：功能上的总结合强度（functional affinity）

- 是与抗原的总结合能；
- “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”(Crowther, 2009, p. 130)；
- 抗体在每个结合位点上总结合强度的量度，也称 functional affinity；
- 对血清这类异质样本，“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”(Crowther, 2009, p. 137)；
- 影响因素有三：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 稀释为什么会改变血清的亲合力

既然 avidity 是异质抗体群体的平均量，它就不是血清的固有常数：“It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”(Crowther, 2009, p. 137)。

Crowther 给出的典型情形是：血清中可能含有**少量高亲和力抗体**和**大量低亲和力抗体**。在稀释不大的免疫检测条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度被降到不足以竞争，剩下的只有低亲和力抗体。当操作者用免疫检测、借助不同抗血清的差异活性来比较抗原时，这一问题尤其重要——任何血清的稀释都可能改变其区分抗原的能力，原因在于异质抗体群体的动力学（各抗体分子的相对浓度与亲和力）(Crowther, 2009, p. 137)。

## 抗体应答：多克隆背景与检测形式的选择

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

被动免疫（passive immunization）指直接给予中和抗体；主动免疫（active immunization）指给予抗原、由机体产生保护性抗体。

疫苗注射通常采用 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）。因此在评估接种效果时，必须先决定采用总抗体检测、isotype-specific assay，还是检测抗原清除。口服或吸入免疫时这一点更突出：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”(Crowther, 2009, p. 140)。

## 这些概念在实践中的位置

把上述内容串起来，可以看到一条从抗原到检测形式的依赖链：抗原的分子大小决定了理论上可被 Fab 占据的位点上限，而这个上限建立在“整个表面都有抗原性”和“分子达到最大结合”两个很少成立的假设之上，因此它只能用于估算饱和所需抗体量一类的目的；epitope / epitype / paratope 的区分界定了“一个结合事件”与“一组抗体识别同一区域”这两个不同层次；affinity 描述单一结合位点的强度并以 K<sub>D</sub> 定义，avidity 则是异质抗体群体在各抗原位点上亲和力的总和或平均值，随 valency 与分子排布而变。

由此可以划定几条边界：avidity 不是血清的固有常数，稀释会筛掉高亲和力抗体群体，从而改变血清区分抗原的能力；血清学比较若跨越不同稀释度，结论未必可比。抗体应答一侧，sc/im 免疫产生的是多克隆、多 isotype 的混合抗体，检测形式（总抗体、isotype-specific、抗原清除）本身就是一个需要预先判断的问题而非事后选择。笔记未展开的是各 isotype 出现的具体时相与定量判据，这部分依赖图中所示的时间顺序。

## 依据与出处

（本篇为减法模式，仅对原笔记作浓缩与归纳，未新增外部内容，故不列外部出处。）