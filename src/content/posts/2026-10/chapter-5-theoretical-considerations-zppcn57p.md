---
draft: true
reviewNotes:
  - "正文过短: 4076/13045=31% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗原刺激后的抗体产生']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,123 字符（原文 16,405，比例 25%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原位点、抗体亲和力与亲合力"
date: 2026-10-01
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记梳理 ELISA 检测背后的几个理论支点：抗原的尺寸如何决定可结合位点的上限，epitope、epitype 与 paratope 的界定，亲和力（affinity）与亲合力（avidity）的区别与联系，以及多克隆抗体的产生、血清稀释对表观亲合力的影响和免疫途径对检测策"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记梳理 ELISA 检测背后的几个理论支点：抗原的尺寸如何决定可结合位点的上限，epitope、epitype 与 paratope 的界定，亲和力（affinity）与亲合力（avidity）的区别与联系，以及多克隆抗体的产生、血清稀释对表观亲合力的影响和免疫途径对检测策略的要求。按概念定义、抗体来源、检测策略的顺序组织。

## 从分子尺寸估算 Fab 结合位点数

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个估算有两个前提：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009)

也就是说，它假定整个表面都具有抗原性、并且分子按最大数量结合，而这两点都很少成立。它的价值不在于给出精确的位点计数，而在于：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009)

即用于估算饱和某一抗原所需的抗体量，或测定抗体结合量随可用表面的变化。

## epitope、epitype 与 paratope

三个容易混淆的术语：

- **epitope**：antigenic site，抗原位点。
- **epitype**：抗原上的一个区域，由一组识别非常相似化学结构的密切相关的抗体（例如定义重叠或相互关联表位的 mAbs）所识别，可视为识别与同一抗原位点反应的、特异性略有差异的抗体的区域。

  > "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009)

- **paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单一位点与整体结合

### affinity

亲和力指抗体分子与抗原决定簇之间的结合能：

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009)

具体可以从三个层面描述：

1. the energy between a single epitope and paratope；
2. binding affinity 是**单个结合位点**上抗原 epitope 与抗体 paratope 之间相互作用的强度；
3. 它由**非共价相互作用**介导，包括氢键、静电键、范德华力与疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

### avidity

avidity 又称 functional affinity：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009)

- 与抗原的整体结合能；
- 抗体在每个结合位点上总结合强度的量度，即 functional affinity；
- 三个影响因素：**binding affinity、valency，以及抗体与抗原的结构排布**。

## 抗原刺激后的抗体产生

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 血清稀释会改变表观亲合力

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009)

原因是血清中的抗体是异质的，不同分子的相对浓度与亲和力并不一致：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)." (Crowther, 2009)

## 免疫途径与随之而来的检测策略选择

被动免疫（passive immunization）是直接给予中和抗体；主动免疫（active immunization）是给予抗原，由机体产生保护性抗体。

疫苗的注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：究竟是用总抗体检测、isotype-specific assay，还是用检测抗原清除的 assay 来评估疫苗接种效果。口服或吸入免疫路径下这一问题尤其突出：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009)

即免疫分析工作者需要判断，检测 isotype-specific 抗体（特别是 IgA）是否比检测总抗体更能揭示疫苗接种带来的收益。

## 小结

这一章给出的是一组约束条件，而不是一套操作规程：抗原表面积只能给出 Fab 结合位点数的上限，实际抗原性表面与结合饱和程度都低于假设值；affinity 描述单个 epitope–paratope 的相互作用，avidity 描述抗体与抗原的整体结合，二者受 binding affinity、valency 和分子排布共同影响。落到检测上，多克隆血清的异质性意味着稀释本身会改变表观亲合力、进而改变血清区分不同抗原的能力，免疫途径决定的 isotype 分布则直接关系到报告基因该选总抗体还是 isotype-specific 抗体（如 IgA）。这些都属于设计阶段就需要定下来的前提，笔记本身未进一步展开具体实验方案。