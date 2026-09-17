---
draft: true
reviewNotes:
  - "正文过短: 3743/13096=29% < 40%"
  - "空壳章节（正文不足 120 字）: ['免疫应答产生的是多克隆抗体']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,671 字符（原文 16,470，比例 22%）超出 9,058～15,646 字符的区间"
title: "ELISA 理论基础：抗原表位、抗体亲和力与亲合力，以及抗血清稀释带来的变数"
date: 2026-09-17
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理的是 ELISA 检测背后的理论框架：抗原的大小如何决定可结合位点的上限、epitope / epitype / paratope 这几个定义如何区分、affinity 与 avidity 各自的含义与影响因素，以及抗血清稀释和免疫方式为什么会反过来影响检测结果与检测策略"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理的是 ELISA 检测背后的理论框架：抗原的大小如何决定可结合位点的上限、epitope / epitype / paratope 这几个定义如何区分、affinity 与 avidity 各自的含义与影响因素，以及抗血清稀释和免疫方式为什么会反过来影响检测结果与检测策略的选择。

## 抗原大小决定了可结合位点数的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）

也就是说，这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

**应用**：可以据此估算饱和任意抗原所需的抗体量，或测定抗体结合水平随可用表面积的变化——"calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009）。

## 表位、表位型与互补位：三个容易混用的定义

- **epitope**：antigenic site，即抗原位点。
- **Epitype**：抗原上的一个区域，由一组识别非常相似化学结构的、密切相关的抗体识别（例如 mAbs，它们定义重叠或相互关联的表位）；可视为识别与同一抗原位点反应的、特异性略有不同的抗体的区域。

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009）

- **paratope**：抗体上结合抗原表位的部分。

## 亲和力描述单个结合位点，亲合力描述整体结合

### 亲和力（affinity）

- 是单个 epitope 与 paratope 之间的能量；
- 指在**单一结合位点**上，抗原 epitope 与抗体 paratope 之间相互作用的强度；
- 由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡**解离常数（KD）**定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009）
>
> 抗体分子与抗原决定簇之间的结合能称为亲和力。

### 亲合力（avidity，即 functional affinity）

- 是与抗原的总结合能；
- 是抗体在每个结合位点上总结合强度的量度，也称功能亲和力。

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009）

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009）
>
> 亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

### 亲合力的三个影响因素

1）the binding affinity；2）valency；3）the structural arrangement of the antibody and antigen in question。

## 稀释会改变抗血清的亲合力与辨别力

血清的亲合力在稀释时可能会发生变化，因为操作者可能把某些抗体群稀释掉了：

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009）

一个典型的场景是：血清中同时存在**少量高亲和力抗体**和**大量低亲和力抗体**。在**不进行大幅稀释**的免疫分析条件下，高亲和力与低亲和力抗体竞争抗原位点，**高亲和力抗体会优先反应**；而一旦稀释，高亲和力抗体的浓度会被降到只剩下低亲和力抗体的程度。当操作者用免疫分析通过不同抗血清的差异活性来比较抗原时，这类问题很重要；由于异质性抗体群的动态（各个抗体分子的相对浓度与亲和力），**任何血清的稀释都可能影响其区分不同抗原的能力**（Crowther, 2009）。

## 免疫应答产生的是多克隆抗体

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；不同抗体类型的产生有时间先后顺序，见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

（Crowther, 2009）

## 免疫方式决定用哪一类检测来评估效果

- **passive immunization**：直接打中和抗体。
- **active immunization**：服用抗原，产生保护性抗体。

**疫苗注射方式**：sc（皮下注射）或 im（肌内注射）。这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑是用总抗体检测、isotype-specific assay，还是检测抗原清除的检测来评估疫苗接种效果。

**口服/吸入免疫**：此时免疫分析人员必须决定，同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地反映疫苗接种的获益——"The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）。

## 小结：这些理论概念对应的实际判断

把这些概念串起来，落点其实都很具体：Fab 结合面积与球面计算给出的是**可结合位点数的上限**，它成立的前提是"整个表面都具有抗原性"和"分子最大结合"，而这两个前提很少同时成立，所以它只能用于估算饱和抗体用量或结合水平随表面积的变化；affinity 是单个结合位点上的事，avidity 则是血清中异质性抗体与各抗原位点亲和力的总和，并受结合亲和力、价数和抗体—抗原结构排布三者共同影响；也正因为 avidity 是"一群抗体的总和"，稀释会改变血清的成分比例，进而改变其区分不同抗原的能力——在需要用不同抗血清比较抗原时，这一点必须先被排除掉。检测策略上，免疫途径（sc/im 与口服/吸入）决定了应当用总抗体、isotype-specific 检测还是抗原清除来评估效果，其中 IgA 是否比总抗体提供更多信息，是需要逐案判断的问题。