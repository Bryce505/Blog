---
draft: true
reviewNotes:
  - "正文过短: 4458/13045=34% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,528 字符（原文 16,405，比例 28%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：从抗原表位到抗体 affinity 与 avidity"
date: 2026-10-11
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本篇整理 ELISA 理论部分的几个基础命题：抗原分子的大小如何约束可结合位点数的上限，epitope、epitype、paratope 与 affinity、avidity 这几个术语各自的准确所指，以及抗体是主动还是被动获得、经何种途径获得，会怎样影响检测方案的选择。内容按抗"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本篇整理 ELISA 理论部分的几个基础命题：抗原分子的大小如何约束可结合位点数的上限，epitope、epitype、paratope 与 affinity、avidity 这几个术语各自的准确所指，以及抗体是主动还是被动获得、经何种途径获得，会怎样影响检测方案的选择。内容按抗原特性、抗体特性、免疫方式三条线组织，最后归拢这些估算与判断的适用边界。

## 抗原分子越大，可结合位点数的上限越高

分子越大，其复杂性也就越高。

Fab 的结合面积大约是 20nm^2，这也就是 epitope 的表面积。据此可以估算结合位点数的最大值：先计算分子的球形表面积，再把表面积除以 20。

这一算法的成立条件必须写明：

> Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally

> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

因此它给出的是上限，而非实际可结合位点数。这一估算的实际用途在于：计算使任一试剂饱和所需的抗体量，或测定抗体结合水平随可用表面的变化。

## 表位、表位型与 paratope：三个必须区分的术语

**epitope**：即 antigenic site，抗原上的表位。

**Epitype**：

> An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site

> 表位型是抗原上的一个区域，由一组识别非常相似化学结构的、彼此密切相关的抗体（例如定义重叠或相互关联表位的 mAb）识别。表位型可视为识别与同一抗原位点反应的、特异性略有不同的抗体的区域。

**paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity 不是同义词

### affinity：单一位点上的结合能

> The binding energy between an antibody molecule and an antigen determinant is termed affinity.

> 抗体分子与抗原决定簇之间的结合能称为亲和力。

其准确所指可以拆成三条：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗原 epitope 与抗体 paratope 在单一结合位点上的相互作用强度；
3. 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数 (K_D) 定义。

### avidity：整体结合强度，即 functional affinity

> The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites

> Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)

> 亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和。

抗体在每个结合位点上的总结合强度称为 avidity，也称 functional affinity。

### avidity 由三个因素决定

1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question —— 即亲和力、价数，以及抗体与抗原的结构排布。

## 血清稀释会改变 avidity，也改变抗体区分抗原的能力

> It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies

> 重要的是要认识到，血清的 avidity 在稀释时可能发生变化，因为操作者可能把某些抗体群体稀释掉了。

原文给了一个具体情形：

> As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).

一份血清中可以同时存在少量高亲和力抗体和大量低亲和力抗体。在稀释倍数不高的免疫分析条件下，两者竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度下降，最终只剩低亲和力抗体。当操作者用免疫分析、以不同抗血清的差异活性来比较抗原时，这一点尤其重要——由于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力。

## 抗体从何而来，决定用哪一类检测去评价

抗体的获得方式分两类：

- **passive immunization**：直接注射中和抗体；
- **active immunization**：给予抗原，产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）。这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：评估疫苗接种效果时，究竟使用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。

口服/吸入免疫则引出另一个判断：

> The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody

> 免疫分析人员必须决定，同型抗体——特别是 IgA——的检测是否比总抗体的检测更能深入反映疫苗接种的收益。

应对抗原刺激产生的是多克隆抗体，且抗体类型并不限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 结论与适用边界

- 表面积除以 20 的位点数估算只在「整个表面都有抗原性」与「分子达到最大结合」两个前提下成立，而前者很少为真。它是上限，不是预期值，正当用途是估算饱和所需抗体量、以及考察结合水平随可用表面的变化。
- affinity 描述单一位点，avidity 描述整体；avidity 是抗体群对不同抗原位点各亲和力的总和（平均结合能），并受 binding affinity、valency、抗体与抗原结构排布三者影响，因此也称 functional affinity。
- avidity 不是血清的固有常数。稀释会改变异质性抗体群体的组成，从而改变 avidity，也改变血清区分不同抗原的能力；用不同抗血清的差异活性来比较抗原时，这一效应必须被控制。
- 免疫途径不同，诱导出的 isotype 谱不同（sc/im 可诱导多种 isotype，口服/吸入则需判断是否检测 IgA 这类 isotype-specific 抗体）。在总抗体、isotype-specific assay 与抗原清除检测之间先做选择，是评价疫苗效果的第一步。
- 本文范围止于抗原与抗体两端的理论考量；酶反应动力学与浓度-反应关系属于同一章但未在此展开。