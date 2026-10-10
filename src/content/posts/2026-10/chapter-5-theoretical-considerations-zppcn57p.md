---
draft: true
reviewNotes:
  - "正文过短: 3929/13045=30% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,887 字符（原文 16,405，比例 24%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-10-10
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这一章讨论 ELISA 反应体系背后的几个基本概念：抗原的分子大小与表位如何决定可结合位点数的上限，抗体一侧亲和力（affinity）与亲合力（avidity）的定义与区别，以及免疫方式、血清稀释如何改变抗体的组成与反应行为。内容偏定义与前提条件，是理解后续方法学设计（抗体用量估"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这一章讨论 ELISA 反应体系背后的几个基本概念：抗原的分子大小与表位如何决定可结合位点数的上限，抗体一侧亲和力（affinity）与亲合力（avidity）的定义与区别，以及免疫方式、血清稀释如何改变抗体的组成与反应行为。内容偏定义与前提条件，是理解后续方法学设计（抗体用量估算、稀释系列解释、疫苗免疫原性评价指标选择）的出发点。

## 抗原侧：分子大小决定可结合位点数的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20 nm²，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

需要注意的是这种算法所依赖的前提：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009, p. 127)

即：这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。两个前提在真实抗原上很少同时成立。

**应用**：可以据此计算饱和任意一种试剂所需的抗体量，或测定抗体结合水平随可及表面变化的函数（Crowther, 2009, p. 127）。

## 表位、表位型与 paratope：定义与区分

- **epitope**：antigenic site（抗原位点）。
- **Epitype（表位型）**：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009, p. 128)

即：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一位点与抗体群体两个层次

### 亲和力（affinity / binding affinity）

1. 单个 epitope 与 paratope 之间的能量；
2. binding affinity 是抗原的 epitope 与抗体的 paratope 之间**在单一位点上**的相互作用强度；
3. affinity 由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009, p. 136)

即：抗体分子与抗原决定簇之间的结合能称为亲和力。

### 亲合力（avidity / 功能性亲和力）

1. 与抗原的总结合能：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009, p. 130)

2. 抗体在每个结合位点上总结合强度的度量称为 avidity，也称为功能性亲和力（functional affinity）；
3. 三个影响因素：1）the binding affinity，2）valency，3）the structural arrangement of the antibody and antigen in question。

在血清水平上，亲合力还有一层含义：

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009, p. 137)

即：亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

## 抗体应答与免疫方式

应对抗原刺激产生抗体，得到的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

（Crowther, 2009）

- **passive immunization**：直接打中和抗体；
- **active immunization**：服用抗原，产生保护性抗体。

**疫苗注射方式**：sc（皮下注射）或 im（肌内注射）。这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑究竟使用总抗体检测、isotype-specific assay，还是检测抗原清除的 assay 来评估疫苗接种效果。

**口服/吸入免疫**则引出同位素型特异检测的问题：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)

即：免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 血清稀释会改变亲合力与抗原区分能力

亲合力并非血清的固定属性，稀释本身就会改变它：

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009, p. 137)

一个具体的例子：血清中可能同时含有**少量高亲和力抗体**和**大量低亲和力抗体**。在血清**未被大幅稀释**的免疫分析条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度会下降，直至只剩下低亲和力抗体。操作者用免疫分析**比较不同抗血清对抗原的差异活性**时，这类问题很重要；**任何血清的稀释都可能影响其区分抗原的能力**，原因在于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力）（Crowther, 2009, p. 137）。

## 这些概念的边界与用法

把上述内容收拢起来，可以归纳为三条使用上的边界：

- **抗原侧**：以球形表面积除以 20 nm² 得到的 Fab 结合位点数，建立在「整个表面都有抗原性」和「分子最大结合」两个前提之上，而这两个前提很少成立，因此它给出的是估算的上限，用于反推饱和所需抗体量时需要保留这一保留条件（Crowther, 2009, p. 127）。
- **抗体侧**：affinity 描述单个 epitope–paratope 位点，avidity 描述抗体整体乃至血清中异质性抗体群体的总结合强度，受 binding affinity、valency 和抗体–抗原结构排布三者影响；两者不可混用。
- **操作侧**：血清的 avidity 会随稀释改变，不同稀释度下留下来的抗体群体不同，这会直接影响免疫分析对抗原的区分能力；因此在用免疫分析比较抗血清或评估免疫效果时，稀释方案本身就是一个需要交代的变量。

未在本章内解决的问题也很明确：上述内容给出的是概念和前提，并未给出在具体体系中如何选定稀释度、如何选择总抗体与 isotype-specific 检测的判据，这些需要在具体的检测目的下另行确定。

原始笔记中的「相关笔记」链接为知识库内部链接，此处不再保留。