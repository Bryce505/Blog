---
draft: true
reviewNotes:
  - "正文过短: 3827/13096=29% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,764 字符（原文 16,470，比例 23%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答"
date: 2026-11-05
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的可靠性不取决于操作步骤是否熟练；结果好坏，主要由抗原—抗体相互作用的理论前提决定。这篇笔记围绕抗原的分子大小与可结合表面积、epitope/epitype/paratope 的定义分工、affinity 与 avidity 的差别，以及抗体应答本身的异质性如何影响稀"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的可靠性不取决于操作步骤是否熟练；结果好坏，主要由抗原—抗体相互作用的理论前提决定。这篇笔记围绕抗原的分子大小与可结合表面积、epitope/epitype/paratope 的定义分工、affinity 与 avidity 的差别，以及抗体应答本身的异质性如何影响稀释、检测指标选择与结果判读，按“抗原—抗体—免疫应答—操作变量”的顺序整理。

## 抗原性首先是一个表面积问题

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个估算给出的是上限，并不是真实值：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009)

也就是说，该计算建立在两个假设之上：整个分子表面都具有抗原性，而这一点很少成立；分子也会达到最大结合。

它的实际用途是反推固相包被与饱和条件："calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009) —— 既可用于估算饱和给定抗原所需的抗体量，也可把抗体结合量当作可用表面积的函数来测量。

## epitope、epitype 与 paratope：三个层次的定义

**epitope** 即 antigenic site；**paratope** 是抗体上结合抗原表位的部分。

**epitype** 描述的是比 epitope 更细的一层区分：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009)

即：epitype 是抗原上由一组化学结构识别高度相似的抗体（例如定义重叠或相互关联表位的 mAb）所界定的区域，可以看作同一抗原位点上抗体特异性略有差异的那片区域。

## affinity 与 avidity：单点结合能与总体结合强度

**affinity（binding affinity）** 有三个等价表述：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗原 epitope 与抗体 paratope 在**单个结合位点**上的相互作用强度；
3. 由**非共价相互作用**介导，包括氢键、静电键、范德华力与疏水相互作用，并以**平衡解离常数 K<sub>D</sub>** 定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009)

**avidity** 又称 functional affinity，指的是与抗原结合的总体结合能：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009)

也可以是血清层面的表述："Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009)。avidity 是抗体在每一个结合位点上结合强度的总和，其大小取决于三个因素：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 抗体应答的异质性决定了检测的设计空间

抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

正因为应答是异质的，**稀释**本身就成了一个会改变测量对象的变量：血清的亲和力在稀释时可能会发生变化，因为操作者可能把某些抗体群体稀释掉了。

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009)

典型情形是：血清中同时存在**少量高亲和力抗体**与**大量低亲和力抗体**。在不作大幅稀释的免疫分析条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度被降到很低，剩下的就只有低亲和力抗体。当操作者用免疫分析、通过不同抗血清的差异反应性来比较抗原时，这类问题尤其重要——由于异质抗体群体的动力学（各抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力 (Crowther, 2009)。

## 免疫方式决定该测什么

被动免疫（passive immunization）是直接给予中和抗体；主动免疫（active immunization）是给予抗原、由机体产生保护性抗体。

给药途径同样影响抗体谱：sc（皮下注射）或 im（肌内注射）可诱导产生多种抗体类型（isotype），因此必须考虑是用总抗体检测、isotype-specific assay，还是用检测抗原清除的试验来评估疫苗接种效果。

口服或吸入免疫则会引出另一个选择题：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009)

也就是说，需要判断 isotype-specific 抗体（尤其是 IgA）的检测是否比总抗体检测更能反映疫苗接种的收益。

## 这些前提在方法设计中的位置

把上述内容收拢：抗原侧的可结合位点数只是一个基于“全表面均具抗原性、且结合饱和”的理论上限，用于估算饱和条件而非预测真实滴度；epitope/epitype/paratope 的区分决定了抗体的识别粒度；affinity 描述单点结合能、以 K<sub>D</sub> 刻画，avidity 描述总体结合强度并受亲和力、价数与结构排布三者共同影响；多克隆应答的异质性使得稀释成为一个会改变表观亲合力的操作变量，也使“测总抗体还是测特定 isotype”成为必须先在方法设计阶段回答的问题。这些前提之外的部分——具体固相格式、信号放大与数据处理——不在本篇范围内。

## 依据与出处

1. 笔记：`Chapter-5-Theoretical-Considerations-ZPPCN57P` —— 引用要点：本篇为减法模式下的整理，未新增实质内容，全部论述与引文均出自该笔记及其所引 Crowther (2009)。