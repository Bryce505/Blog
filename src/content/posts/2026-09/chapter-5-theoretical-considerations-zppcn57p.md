---
draft: true
reviewNotes:
  - "正文过短: 4896/13045=38% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 5,093 字符（原文 16,405，比例 31%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-09-24
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本文整理自 Crowther《The ELISA Guidebook》第 5 章 \"Theoretical Considerations\" 的阅读笔记。内容沿三条线展开：抗原一侧的分子大小与表位界定，抗体一侧的亲和力（affinity）与亲合力（avidity）之区分，以及免疫方"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本文整理自 Crowther《The ELISA Guidebook》第 5 章 "Theoretical Considerations" 的阅读笔记。内容沿三条线展开：抗原一侧的分子大小与表位界定，抗体一侧的亲和力（affinity）与亲合力（avidity）之区分，以及免疫方式如何决定血清中抗体的类型构成并影响检测策略的选择。

## 分子大小决定的只是可结合位点数的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积。通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

但这个估算有两个前提，笔记中明确标注：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

该估算的应用方向是推算饱和某种试剂所需的抗体量，或测定抗体结合水平随可用表面积变化的函数关系：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009, p. 127）

## epitope、epitype 与 paratope：三个容易混淆的术语

- **epitope**：antigenic site，即抗原表位。
- **paratope**：抗体上结合抗原表位的部分。
- **epitype**：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009, p. 128）
> 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

## affinity 与 avidity：单一结合位点与整体结合强度

### affinity 描述的是单一 epitope–paratope 之间的结合能

笔记中对 binding affinity 给出三层界定：

- the energy between a single epitope and paratope；
- the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
- Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K_D)。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009, p. 136）
> 抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity 是异质抗体群与多个抗原位点之间的总体结合强度

- overall binding energy with an antigen；
- The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity；
- 三个影响因素：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question。

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009, p. 130）
> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009, p. 137）
> 亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

### 稀释会改变血清的亲合力

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009, p. 137）

原文举了一个具体的例子说明其后果：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)."（Crowther, 2009, p. 137）

## 免疫方式决定了血清中会出现哪些抗体类型

### 抗原刺激产生的是多克隆抗体

应对抗原刺激产生抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 被动免疫与主动免疫

- passive immunization：直接打中和抗体；
- active immunization：服用抗原，产生保护性抗体。

### 接种途径决定了该测什么

疫苗注射方式为 sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型 - isotype；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫则引出另一层判断：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）
> 免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 小结

三条线索各自的边界可以归拢如下。

**抗原侧**：球形表面积除以 20nm^2 给出的是 Fab 结合位点数的最大数量，而非实际表位数。这一计算假定整个表面具有抗原性且抗体结合达到最大，而这两个条件都很少成立，因此结果只能当作上限使用。

**抗体侧**：affinity 描述单一 epitope 与 paratope 之间的结合能，由氢键、静电作用、范德华力和疏水相互作用等非共价作用介导，以平衡解离常数 K_D 表征；avidity 则是异质抗体群与不同抗原位点之间所有亲和力的总和，受 binding affinity、valency 以及抗体与抗原的结构排布三者共同影响。两者处于不同层次，不能互换使用。

**定量解释的边界**：血清的 avidity 会随稀释而改变，因为稀释可能去除某些抗体群体。当用免疫assay按不同抗血清的差异活性来比较抗原时，稀释本身就会影响血清区分抗原的能力，其根源在于异质抗体群的动力学，即各抗体分子的相对浓度与亲和力。

**检测设计**：免疫方式（被动或主动、注射或口服/吸入）决定血清中出现的 isotype 谱，也决定评估疫苗效果时应选择总抗体检测、isotype-specific assay 还是抗原清除检测。