---
draft: true
reviewNotes:
  - "正文过短: 3976/13045=30% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,973 字符（原文 16,405，比例 24%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-09-11
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的表现并不只由酶和显色底物决定，抗原本身的性质、抗体的结合行为以及抗血清的组成同样在底层起作用。这篇笔记围绕 Crowther 第 5 章的理论要点展开：从抗原尺寸推算可结合位点数的上限，厘清 epitope、epitype、paratope 三个术语，区分 affi"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的表现并不只由酶和显色底物决定，抗原本身的性质、抗体的结合行为以及抗血清的组成同样在底层起作用。这篇笔记围绕 Crowther 第 5 章的理论要点展开：从抗原尺寸推算可结合位点数的上限，厘清 epitope、epitype、paratope 三个术语，区分 affinity 与 avidity，并说明血清稀释和抗体产生方式如何约束检测设计。

## 抗原尺寸与可结合位点数的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个估算只是上限，因为它的前提本身很少成立：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）
>
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

估算的用途不在于预测真实的表位数，而在于给实验设定边界条件：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009, p. 127）

## epitope、epitype 与 paratope 的界定

三个词指向三个不同的对象：

- **epitope**：抗原决定簇（antigenic site）；
- **paratope**：抗体上结合抗原表位的部分；
- **epitype**：抗原上的一个区域，由一组识别非常相似化学结构的密切相关的抗体所界定。

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009, p. 128）
>
> 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

## affinity 与 avidity：从单一位点到抗体群

### affinity

affinity 指的是单一结合位点层面的结合强度，可以从三个角度描述：

- the energy between a single epitope and paratope；
- the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
- affinity is mediated by non-covalent interactions，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009, p. 136）
>
> 抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity

avidity 又称 functional affinity，描述的是抗体整体的结合强度。

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009, p. 130）

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009, p. 137）
>
> 亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

影响 avidity 的因素有三个：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 血清稀释为什么会改变检测的判别力

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009, p. 137）
>
> 重要的是要认识到血清的亲合力在稀释时可能会发生变化，因为操作者可能会稀释掉某些群体的抗体。

具体机制是：同一份血清中可能同时存在**少量高亲和力抗体**和**大量低亲和力抗体**。在血清稀释倍数不大的免疫检测条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体会优先反应**；随着稀释进行，高亲和力抗体的浓度不断降低，最终只剩下低亲和力抗体。当操作者用免疫检测通过不同抗血清的差异活性来比较抗原时，这一问题尤其重要——由于异质性抗体群的动力学（各抗体分子的相对浓度与亲和力），**任何血清的稀释都可能影响其区分抗原的能力**（Crowther, 2009, p. 137）。

## 抗体产生方式对检测设计的约束

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

两种免疫方式的区别在于：

- **passive immunization**：直接注射中和抗体；
- **active immunization**：给予抗原，由机体产生保护性抗体。

疫苗的注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：评估疫苗接种效果时，究竟使用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。

口服或吸入免疫则引出另一个选择：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）
>
> 免疫检测人员必须决定，同型抗体（特别是 IgA）的检测是否比总抗体的检测更能深入反映疫苗接种的收益。

## 小结

这篇笔记给出的是检测设计的边界条件而非操作流程：由表面积推算的 Fab 结合位点数只是上限，因为「整个表面都具有抗原性」这个前提很少成立；affinity 描述的是单一 epitope–paratope 位点上的结合能，avidity 则是异质抗体群与多个抗原位点结合能的平均与加和，受 binding affinity、valency 和抗体–抗原的空间排布三者影响。

在方法层面，有两点需要预先考虑。其一，血清稀释会改变其表观 avidity——高亲和力抗体群被稀释掉之后，血清区分不同抗原的能力随之改变，因此在用不同抗血清比较抗原时，稀释倍数本身就是一个变量。其二，免疫途径（sc/im 与口服/吸入）决定了产生的 isotype 谱，检测端需要据此在总抗体、isotype-specific 与抗原清除三类读出之间作选择。