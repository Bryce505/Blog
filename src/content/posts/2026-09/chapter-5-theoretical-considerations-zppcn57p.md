---
draft: true
reviewNotes:
  - "正文过短: 4276/13096=33% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,920 字符（原文 16,470，比例 30%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与免疫应答"
date: 2026-09-30
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量能力建立在抗原-抗体相互作用的基本性质之上：抗原表面能提供多少可及表位、抗体的结合强度如何定义与测量、免疫方式又决定了血清中抗体群体的组成。这篇整理自 Crowther《The ELISA Guidebook》第 5 章的理论部分，按抗原、抗体、免疫应答三条线索"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量能力建立在抗原-抗体相互作用的基本性质之上：抗原表面能提供多少可及表位、抗体的结合强度如何定义与测量、免疫方式又决定了血清中抗体群体的组成。这篇整理自 Crowther《The ELISA Guidebook》第 5 章的理论部分，按抗原、抗体、免疫应答三条线索归纳这些前提条件，并说明它们各自在什么条件下会失效。

## 抗原的分子大小决定了可及表位数量的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）
>
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

也就是说，这个数字给出的是上限，而不是实际上可用的表位数。它的价值在于反向推算：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009, p. 127）

即估算饱和某种抗原所需的抗体量，或测定抗体结合量随可用表面的变化。

## 表位、表位型与 paratope：三个容易被混用的术语

- **epitope**：antigenic site。
- **paratope**：抗体上结合抗原表位的部分。
- **Epitype**：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009, p. 128）
>
> 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

## affinity 与 avidity：单一结合位点与整体结合强度

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009, p. 136）
>
> 抗体分子与抗原决定簇之间的结合能称为亲和力。

### affinity

1. the energy between a single epitope and paratope；
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope **at a singular binding site**；
3. Affinity is mediated by **non-covalent interactions** that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium **dissociation constant (K_D)**。

### avidity（functional affinity）

1. overall binding energy with an antigen；

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009, p. 130）

2. The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity；
3. 三个影响因素：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question。

### 血清的 avidity 会随稀释而改变

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009, p. 137）
>
> 亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009, p. 137）
>
> 重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释某些群体的抗体。

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)."（Crowther, 2009, p. 137）

## 抗体的产生方式决定了检测要怎么设计

### 应对抗原刺激产生抗体

多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生时间顺序见下图

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 主动免疫与被动免疫

passive immunization：直接打中和抗体；

active immunization：服用抗原，产生保护性抗体；

疫苗注射方式：sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型-isotype；必须考虑是否使用总抗体检测，isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果；

口服/吸入免疫：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）
>
> 免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 这些理论前提在什么情况下会失效

抗原侧的核心结论是：由分子大小和 Fab 接触面积推算出的结合位点数目只是理论上限，其成立依赖于"整个表面都具有抗原性"和"分子最大结合"两个很少同时成立的假设。

抗体侧的核心结论是：affinity 描述单一结合位点的相互作用，由非共价作用决定并以解离常数 K_D 表征；avidity 是全局量，受 binding affinity、valency 以及抗体与抗原的结构排布三者共同影响。当抗体群体是异质的（如血清），avidity 是所有个体亲和力的总和或平均值，因而它不是一个固定属性——稀释会改变群体组成，进而改变血清区分不同抗原的能力，也会改变比较不同抗血清时的结果。

免疫应答侧的核心结论是：免疫途径（sc/im 与口服/吸入）与免疫方式（主动/被动）决定产生哪些 isotype，检测方案需要在总抗体检测与 isotype-specific assay 之间做出选择。