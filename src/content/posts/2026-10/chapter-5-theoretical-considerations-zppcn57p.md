---
draft: true
reviewNotes:
  - "正文过短: 4075/13045=31% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,635 字符（原文 16,405，比例 28%）超出 9,023～15,585 字符的区间"
title: "ELISA 理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-10-08
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本篇整理 ELISA 及其它免疫检测所依赖的底层理论。先从抗原一侧出发，讨论分子大小与可结合位点数的关系，随后界定表位、表位型、互补位等术语，再区分亲和力（affinity）与亲合力（avidity）这两个常被混用的概念，最后落到免疫与疫苗接种后抗体应答的检测策略选择上。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本篇整理 ELISA 及其它免疫检测所依赖的底层理论。先从抗原一侧出发，讨论分子大小与可结合位点数的关系，随后界定表位、表位型、互补位等术语，再区分亲和力（affinity）与亲合力（avidity）这两个常被混用的概念，最后落到免疫与疫苗接种后抗体应答的检测策略选择上。

## 抗原分子的大小如何决定可结合位点数量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有前提：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009）。这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

其用途在于：“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”（Crowther, 2009）。

## 表位、表位型与互补位

- **epitope**：antigenic site。
- **Epitype**：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009）。表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一位点与整体结合的区分

### affinity（结合亲和力）

1. the energy between a single epitope and paratope；
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
3. Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K<sub>D</sub>)；

“The binding energy between an antibody molecule and an antigen determinant is termed affinity.”（Crowther, 2009）——抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity（亲合力）

1. overall binding energy with an antigen；“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009）；
2. The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity；
3. 三个影响因素：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question。

“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”（Crowther, 2009）。亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

## 稀释如何改变血清的亲合力

“It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”（Crowther, 2009）。

“As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).”（Crowther, 2009）

## 免疫与疫苗接种后的抗体应答

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

被动免疫与主动免疫的区别在于：passive immunization 是直接打中和抗体；active immunization 是服用抗原，产生保护性抗体。

疫苗注射方式为 sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型（isotype）；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫则不同：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”（Crowther, 2009, p. 140）。免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 小结：概念框架的适用边界

这套理论的核心是两对区分。其一是**抗原侧**的区分：由球形表面积除以单个 Fab 接触面积估算出的结合位点数，成立的前提是“整个表面都有抗原性”且“分子最大结合”，而这两个前提在真实抗原上很少同时满足，该估算只能当作上限参考。

其二是**抗体侧**的区分：亲和力描述的是单一 epitope–paratope 之间的结合能，以 K<sub>D</sub> 表征；亲合力描述的是抗体在所有结合位点上的总结合强度，受结合亲和力、效价（valency）、抗体与抗原的结构排布三者共同影响。两者不可互换。

由此带来一个实操上的边界：血清的亲合力会随稀释而改变——高亲和力抗体群体可能先被稀释掉，剩下低亲和力抗体，血清区分不同抗原的能力因而与稀释倍数相关。当检测目的是比较抗原、或评估疫苗接种效果时，需要在总抗体检测与 isotype-specific 检测之间做出选择，这一选择取决于所要回答的问题，而笔记本身未给出统一答案。