---
draft: true
reviewNotes:
  - "正文过短: 3941/13096=30% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗原免疫后的抗体应答：多克隆与同种型']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,885 字符（原文 16,470，比例 24%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答"
date: 2026-10-24
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理 ELISA 设计背后的几个理论前提：抗原分子大小如何决定可结合表位的数量上限、表位相关术语与 affinity/avidity 的界定，以及免疫途径和血清稀释如何改变抗体的实际表现。内容按抗原—抗体—免疫应答的顺序组织，并在每一处标出该结论成立所需的前提。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理 ELISA 设计背后的几个理论前提：抗原分子大小如何决定可结合表位的数量上限、表位相关术语与 affinity/avidity 的界定，以及免疫途径和血清稀释如何改变抗体的实际表现。内容按抗原—抗体—免疫应答的顺序组织，并在每一处标出该结论成立所需的前提。

## 抗原性首先是一个分子大小与复杂度的问题

分子越大，其复杂性也就越高。

### Fab 结合面积与表位数量上限

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积。由此可以做一个粗略的上限估算：通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> [!warning] 这个估算的两个前提
> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally” (Crowther, 2009, p. 127)。
> 即：该计算假设整个表面都具有抗原性（这很少是真实的），并且分子处于最大结合状态。实际可及表位数通常低于此上限。

**应用**：这一估算的用途是 “calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface” (Crowther, 2009, p. 127)，即估算饱和某一试剂所需的抗体量，或测定抗体结合水平随可用表面的变化。

## 表位、表位型与互补位：结合界面的术语

几个容易混用的名词需要先分清：

- **epitope**：antigenic site，即抗原上被抗体识别的位点。
- **Epitype**（表位型）：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site” (Crowther, 2009, p. 128)。简单说，表位型是抗原上被一组化学结构高度相近的抗体（例如识别重叠或相互关联表位的 mAb）所识别的区域，可视为同一抗原位点上抗体特异性略有差异的那片区域。
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单点强度与整体强度

### affinity（结合亲和力）

笔记里给了三条彼此等价的表述：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗原表位与抗体互补位之间**在单一结合位点**上的相互作用强度；
3. 由**非共价相互作用**介导，包括氢键、静电作用、范德华力和疏水相互作用，并由**平衡解离常数（K_D）**定义。

> [!quote]
> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.” (Crowther, 2009, p. 136)

### avidity（亲合力，functional affinity）

- 与抗原的整体结合能。
- “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites” (Crowther, 2009, p. 130)，即一群抗体结合不同抗原位点时，各亲和力之和所给出的平均结合能。
- 另一个定义：抗体在每一个结合位点上总结合强度的度量称为 avidity，也称 functional affinity。
- 在血清层面可表述为：“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)” (Crowther, 2009, p. 137)。
- **三个影响因素**：1）binding affinity；2）valency；3）抗体与抗原的结构排布。

## 血清稀释会改变亲合力，也会改变抗原鉴别的结果

avidity 不是血清的固定属性。“It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies” (Crowther, 2009, p. 137)。

一个具体情形：血清中同时存在**少量高亲和力抗体**（针对某个复杂抗原）和**大量低亲和力抗体**。在血清**未经大幅稀释**的免疫测定条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；而在稀释后，高亲和力抗体的浓度持续下降，直至体系中只剩下低亲和力抗体。当操作者用免疫测定、以不同抗血清的差异活性来**比较抗原**时，这类问题很重要；由于异质性抗体群的动力学（各个抗体分子的相对浓度与亲和力），**任何血清的稀释都可能影响其区分抗原的能力**。

## 抗原免疫后的抗体应答：多克隆与同种型

抗原刺激后产生的是多克隆抗体，且抗体类型并不仅限于 IgG；各抗体类型的产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 免疫途径与检测策略的选择

不同免疫方式决定了应答的性质，也决定了后续该用什么样的检测去评估它。

### 被动免疫与主动免疫

- **passive immunization**：直接给予中和抗体。
- **active immunization**：给予抗原，由机体产生保护性抗体。

### 注射途径与同种型

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）。这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑：是用总抗体检测、isotype-specific assay，还是检测抗原清除的检测来评估疫苗接种效果。

### 口服/吸入免疫

黏膜途径的免疫应答有其特殊性。此时需要判断的是：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody” (Crowther, 2009, p. 140)，即同种型特异性抗体（尤其是 IgA）的检测，是否比总抗体检测更能反映疫苗接种带来的获益。

## 小结

这套理论框架的实际含义可以归结为几点。第一，由球形表面积除以 20nm^2 得到的表位数只是一个上限，它同时假设了“整个表面都有抗原性”和“分子最大结合”，两个假设在真实抗原上通常都不成立，因此只能用于估算饱和抗体用量或表面结合曲线，不能当作实测值。第二，affinity 描述的是单一表位—互补位界面的强度并以 K_D 定义，avidity 描述的是整体结合强度，受 binding affinity、valency 与结构排布三者共同影响，两者不可互换使用。第三，血清是一个异质性抗体群，稀释会改变其组成，进而改变 avidity 和区分不同抗原的能力；凡是用免疫测定做抗原比较或以抗血清活性判断疫苗效果，稀释条件都必须固定并交代。第四，检测策略要跟着免疫途径走——注射途径诱导多种 isotype，黏膜途径则需专门评估是否用 IgA 等 isotype-specific 检测替代总抗体检测。最后一点是这章本身没有展开的边界：以上讨论停留在结合热力学与血清学层面，并未涉及具体的固相包被、酶反应动力学与信号放大部分，那属于后续章节的内容。