---
draft: true
reviewNotes:
  - "正文过短: 3625/13045=28% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,555 字符（原文 16,405，比例 22%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力/亲合力与免疫应答"
date: 2026-11-17
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的可靠性取决于对抗原-抗体相互作用本身的理解程度。这篇笔记整理了三个层次的理论前提：抗原侧的大小与表位概念、抗体侧 affinity 与 avidity 的区分及其影响因素，以及免疫应答方式对检测策略选择的约束。最后，笔记把这些概念归结为几条可以直接用于检测设计的判断"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的可靠性取决于对抗原-抗体相互作用本身的理解程度。这篇笔记整理了三个层次的理论前提：抗原侧的大小与表位概念、抗体侧 affinity 与 avidity 的区分及其影响因素，以及免疫应答方式对检测策略选择的约束。最后，笔记把这些概念归结为几条可以直接用于检测设计的判断。

## 抗原的分子大小如何决定可结合位点数

分子越大，其复杂性也就越高。Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally” (Crowther, 2009, p. 127)
>
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

也就是说，这个估算给出的是理论上限，并非实际可及的结合容量。它的用途在于：

> “calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface” (Crowther, 2009, p. 127)

## 表位相关术语的界定：epitope、epitype、paratope

- **epitope**：antigenic site，即抗原上被抗体识别的位点。
- **paratope**：抗体上结合抗原表位的部分。
- **Epitype**：抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别。

> “An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site” (Crowther, 2009, p. 128)

## affinity：单一结合位点上的结合能

Affinity（binding affinity）指的是单个 epitope 与 paratope 之间的结合能，即抗原表位与抗体 paratope 在**单一结合位点**上相互作用的强度。它由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并由**平衡解离常数（K_D）**定义。

> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.” (Crowther, 2009, p. 136)

## avidity：多价与多表位背景下的功能亲和力

Avidity 又称功能亲和力（functional affinity），是抗体与抗原之间总的结合能，也就是抗体在每个结合位点上总结合强度的度量。

> “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites” (Crowther, 2009, p. 130)

对于血清这类异质性抗体混合物，avidity 可以看作其中包含的异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和：

> “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)” (Crowther, 2009, p. 137)

影响 avidity 的因素有三个：the binding affinity、valency，以及 the structural arrangement of the antibody and antigen in question。

### 稀释会改变 avidity

> “It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies” (Crowther, 2009, p. 137)

具体机制是：血清中可能含有少量高亲和力抗体和大量低亲和力抗体。在血清**未被大幅稀释**的免疫测定条件下，高亲和力与低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度下降到只剩低亲和力抗体为止。当操作者用免疫测定**比较不同抗血清对抗原的差异活性**时，这类问题很重要；**任何血清的稀释都可能影响其区分抗原的能力**，这取决于异质性抗体群体的动力学（各个抗体分子的相对浓度与亲和力）。

## 抗体的产生：多克隆应答与免疫方式对检测策略的约束

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

免疫方式分为两类：passive immunization 是直接注射中和抗体；active immunization 是给予抗原、由机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑是使用总抗体检测、isotype-specific assay，还是检测抗原清除，来评估疫苗接种效果。口服或吸入免疫途径下，则需要在同型抗体检测与总抗体检测之间做出取舍：

> “The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody” (Crowther, 2009, p. 140)

## 理论考量落到检测设计上的几条判断

第一，用表面积除以 20nm^2 得到的 Fab 结合位点数只是上限，其前提（整个表面均具抗原性、分子达到最大结合）很少成立，因此该计算的实际用途是估算饱和某试剂所需的抗体量，或测定抗体结合量随可用表面的变化。

第二，affinity 描述单一结合位点，avidity 描述整体；后者受亲和力、价数和分子结构排布共同影响，且会随稀释而改变。用不同抗血清比较抗原、或在不同稀释度下比较结果时，这一效应必须纳入考虑。

第三，免疫途径决定了抗体 isotype 的组成，也决定了检测应该测总抗体、特定 isotype（如 IgA）还是抗原清除，这一点在疫苗效果评价中尤其需要事先明确。

上述判断都建立在多克隆、异质性抗体群体的前提之上；至于具体检测体系中如何据此设定试剂浓度与稀释方案，笔记本身未展开，需要在滴定实验中确定。