---
draft: true
reviewNotes:
  - "正文过短: 5000/13045=38% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗体应答的产物是多克隆抗体，且不限于 IgG']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 5,187 字符（原文 16,405，比例 32%）超出 9,023～15,585 字符的区间"
title: "ELISA 理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-09-20
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本篇整理自 ELISA 理论章节，按三条线索展开：抗原本身的特性如何决定一个分子上可结合的抗体数量，如何用 affinity 与 avidity 描述抗体—抗原结合的强弱，以及抗体应答的产生方式（多克隆、免疫途径、isotype）对检测设计意味着什么。内容偏概念与前提条件，目的是"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本篇整理自 ELISA 理论章节，按三条线索展开：抗原本身的特性如何决定一个分子上可结合的抗体数量，如何用 affinity 与 avidity 描述抗体—抗原结合的强弱，以及抗体应答的产生方式（多克隆、免疫途径、isotype）对检测设计意味着什么。内容偏概念与前提条件，目的是为具体的试验设计和结果解释提供依据。

## 抗原分子大小如何决定可结合的抗体数量

分子越大，其复杂性也就越高。

### 从 Fab 结合面积反推位点数量

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009)

也就是说，这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

### 这个估算的用途与边界

这类估算的用途有两方面：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009)

即估算饱和任意一种试剂所需的抗体量，或测量抗体结合水平随可用表面而变化的关系。需要注意，它给出的是上限而非实际值。

## 表位相关术语：epitope、epitype 与 paratope

### epitope 与 epitype

epitope：antigenic site。

Epitype：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009)

表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应、但特异性略有不同的抗体的区域。

### paratope

paratope：抗体上结合抗原表位的部分。

## affinity 与 avidity：单一位点结合能与总体结合强度

### affinity 的定义与物理基础

- the energy between a single epitope and paratope；
- the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
- Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K_D)；

概括地说，affinity 是单个结合位点上抗原表位与抗体 paratope 之间相互作用的强度，由氢键、静电键、范德华力和疏水相互作用等非共价作用介导，以平衡解离常数（K_D）定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009)

抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity 的定义与三个影响因素

- overall binding energy with an antigen；
- The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity；
- 三个影响因素：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question.

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009)

## 抗体应答的产物是多克隆抗体，且不限于 IgG

应对抗原刺激产生抗体，为多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\
(Crowther, 2009)

## 血清稀释为什么会改变表观 avidity

avidity 描述的是整个抗体群体的行为，而不是单一分子的性质：

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009)

亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

正因为如此：

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009)

重要的是要认识到，血清的 avidity 在稀释时可能会发生变化，因为操作者可能会把某些抗体群体稀释掉。

### 高低亲和力抗体混合的一个例子

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)." (Crowther, 2009)

举例来说，血清中可能含有少量对某一复杂抗原呈高亲和力的抗体，同时含有大量低亲和力抗体。在血清未被大幅稀释的免疫测定条件下，高、低亲和力抗体会竞争抗原位点，高亲和力抗体优先反应；而一旦稀释，高亲和力抗体的浓度会被降低，直至只剩下低亲和力抗体。当操作者试图用免疫测定、以不同抗血清对抗原的差异活性来比较抗原时，这类问题很重要。由于异质性抗体群体的动态变化（各抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力。

## 免疫途径与检测策略的选择

passive immunization：直接打中和抗体；active immunization：服用抗原，产生保护性抗体。

疫苗注射方式为 sc—皮下注射或 im—肌内注射；这种方式可以诱导产生多种抗体类型—isotype；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

对于口服/吸入免疫：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)

免疫分析工作者必须决定，同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的获益。

## 小结

这一章的理论考量可以归为三层。抗原层面，Fab 结合面积与球形表面积的换算只给出结合位点数量的上限，其成立依赖「整个表面都具有抗原性」和「分子最大结合」两个很少同时满足的前提。结合层面，affinity 是单一位点、可以用 K_D 描述的强度，avidity 则是抗体群体在多个抗原位点上结合能的平均，受结合亲和力、价数和抗体—抗原结构排布三者共同影响。样本层面，血清的 avidity 会随稀释而改变，因此用不同稀释度比较不同抗血清对抗原的区分能力时需要格外谨慎。检测设计层面，免疫途径决定了所诱导的抗体类型，也就决定了应当选择总抗体检测还是 isotype-specific 检测来评价免疫效果。