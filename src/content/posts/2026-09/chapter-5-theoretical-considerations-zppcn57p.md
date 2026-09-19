---
draft: true
reviewNotes:
  - "正文过短: 4335/13045=33% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,381 字符（原文 16,405，比例 27%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与亲合力"
date: 2026-09-19
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量表现最终受制于抗原—抗体相互作用本身的物理化学属性：抗原表面有多少可被识别的区域、单个结合位点的结合能有多大、血清中异质抗体群的整体结合强度如何随稀释变化。本文围绕 Crowther《The ELISA Guidebook》第 5 章的理论部分，依次整理抗原性考"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量表现最终受制于抗原—抗体相互作用本身的物理化学属性：抗原表面有多少可被识别的区域、单个结合位点的结合能有多大、血清中异质抗体群的整体结合强度如何随稀释变化。本文围绕 Crowther《The ELISA Guidebook》第 5 章的理论部分，依次整理抗原性考虑、表位相关术语的界定、affinity 与 avidity 的区分，以及抗体应答的异质性对检测策略的影响。

## 抗原分子大小与可结合位点数量的估算

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）
>
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

也就是说，由球形表面积折算出的位点数是一个上限，而不是实测的结合容量。该估算的用途在于 "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009, p. 127）——即估算饱和某一试剂所需的抗体量，或把抗体结合水平表示为可用表面的函数。

## 表位、表位型与 paratope：结合界面的术语

**epitope**：antigenic site。

**Epitype**：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009, p. 128）
>
> 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

**paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单一位点结合能与总体结合强度

**affinity**（binding affinity）有三层含义：

1. the energy between a single epitope and paratope；
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
3. Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K_D)。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009, p. 136）
>
> 抗体分子与抗原决定簇之间的结合能称为亲和力。

**avidity**（functional affinity）：

1. overall binding energy with an antigen；
2. The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity；
3. 三个影响因素：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009, p. 130）

当讨论对象从单个抗体分子换成血清时，avidity 的含义相应扩展：

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009, p. 137）
>
> 亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

## 血清稀释如何改变 avidity 与抗原区分能力

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009, p. 137）
>
> 重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释某些群体的抗体。

其机制在于异质抗体群的相对浓度与各自亲和力的分布。设想一份血清中同时含有**少量高亲和力抗体**与**大量低亲和力抗体**：在血清**未经大幅稀释**的免疫分析条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度被削减，最终只剩下低亲和力抗体在起作用。

这一现象在操作者用免疫分析、以不同抗血清的差异活性来**比较抗原**时尤为要紧：**任何血清的稀释都可能影响其区分抗原的能力**，取决于异质性抗体群的动力学，即各个抗体分子的相对浓度与亲和力（Crowther, 2009, p. 137）。

## 抗体应答的异质性与检测策略的选择

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

免疫方式决定抗体谱：

- **passive immunization**：直接打中和抗体；
- **active immunization**：服用抗原，产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫则另有取舍：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）
>
> 免疫分析人员必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 适用边界与未展开的部分

把上述内容归拢起来，这一章提供的是一组约束条件而非操作步骤：

位点数量估算给出的是上限，因为它建立在"整个表面具有抗原性"和"分子最大结合"两个很少成立的前提上；affinity 描述的是单一 epitope 与 paratope 之间的结合能，由氢键、静电作用、范德华力与疏水相互作用等非共价作用介导，以平衡解离常数 K_D 表征；avidity 则是总体结合强度，受结合亲和力、价数（valency）、以及抗体与抗原的结构排布三者共同影响，在血清层面表现为异质抗体群各亲和力的总和。

由此推出的两条实操边界值得记住：其一，血清的 avidity 会随稀释改变，用不同抗血清的差异活性比较抗原时，稀释方案本身就是变量；其二，免疫途径（sc/im 与口服/吸入）决定产生的 isotype 谱，检测策略需要在总抗体、isotype-specific 抗体与抗原清除之间作出选择。

需要说明的是，本篇笔记覆盖的是抗原与抗体一侧的理论；摘要中提到的酶反应动力学与浓度—反应关系不属于本篇笔记的范围。