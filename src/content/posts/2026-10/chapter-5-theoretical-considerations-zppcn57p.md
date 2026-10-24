---
draft: true
reviewNotes:
  - "正文过短: 3286/13045=25% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,141 字符（原文 16,405，比例 19%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答的检测含义"
date: 2026-10-24
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记梳理 ELISA 反应体系背后的几组基础概念：抗原分子的尺寸如何限制可结合位点的数量、表位与互补位的定义边界、亲和力（affinity）与亲合力（avidity）的区别，以及免疫应答方式和免疫途径如何反过来决定检测策略的选择。内容按「抗原—抗体—免疫应答—检测设计」的顺序"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记梳理 ELISA 反应体系背后的几组基础概念：抗原分子的尺寸如何限制可结合位点的数量、表位与互补位的定义边界、亲和力（affinity）与亲合力（avidity）的区别，以及免疫应答方式和免疫途径如何反过来决定检测策略的选择。内容按「抗原—抗体—免疫应答—检测设计」的顺序展开，最后的落点是把这些理论概念对应到方法开发中需要留意的边界条件。

## 抗原分子的尺寸决定了可结合位点数量的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量；

**但这个数字只是理论上限。** 原文的限定是：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"

也就是说，该计算基于两个前提：整个分子表面都具有抗原性（这一点很少成立），以及分子达到最大结合。

**应用**：这类计算可用于估算饱和任意一种试剂所需的抗体量，或测定抗体结合水平随可用表面的变化。

## 表位、表位型与互补位：三个容易混淆的定义

- **epitope**：antigenic site，即抗原表位。
- **Epitype**（表位型）：抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

  > "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"

- **paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单点结合能与总体结合强度

这两个词在日常表述中常被混用，但它们描述的是不同层次的事情。

### affinity（亲和力）

指单一结合位点层面的结合能，原文给出三条相互补充的界定：

1. the energy between a single epitope and paratope;
2. 单一结合位点上，抗原表位与抗体互补位之间相互作用的强度；
3. affinity 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

### avidity（亲合力，functional affinity）

1. 与抗原的总结合能；

   > "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"

2. 抗体在每个结合位点上总结合强度的度量称为 avidity，也称 functional affinity；
3. **三个影响因素**：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question.

## 血清稀释会改变表观亲合力

既然 avidity 可以看作血清中异质性抗体与各种抗原位点（epitope）之间所有不同亲和力的总和，那么它就不是一个固定值——稀释本身就会改变它。

原文举的例子很具体：一份血清中可能同时含有**少量**对某复合抗原高亲和力的抗体和**大量**低亲和力抗体。在血清**不被大幅稀释**的免疫检测条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度会持续下降，直到体系中只剩低亲和力抗体。

因此，任何血清的稀释都可能影响其区分不同抗原的能力，这取决于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力）。当操作者用免疫检测、借助不同抗血清的差异活性来比较抗原时，这个问题尤其需要注意。

## 免疫应答产生的抗体类型与检测策略

动物受抗原刺激后产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图：

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 被动免疫与主动免疫

- passive immunization：直接注射中和抗体；
- active immunization：服用抗原，产生保护性抗体。

### 免疫途径影响抗体类型谱，进而影响检测格式

sc（皮下注射）或 im（肌内注射）可以诱导产生多种抗体类型（isotype）。因此必须考虑：究竟是用总抗体检测、isotype-specific assay，还是检测抗原清除，来评估疫苗接种效果。

口服/吸入免疫则牵出另一层选择：免疫检测的设计者必须决定，同型特异性抗体（尤其是 IgA）的检测是否比总抗体检测更能深入反映疫苗接种的获益。

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"

## 小结：这几组概念的适用边界

- **表位数量估算是上限，不是实测值。** 它建立在「整个表面都具有抗原性」和「分子达到最大结合」两个很少同时成立的前提上，因此只能用于量级估算与饱和条件设计。
- **affinity 与 avidity 不可互换。** affinity 描述单一 epitope–paratope 位点的结合强度，由 K<sub>D</sub> 定义；avidity 是抗体（或抗体群体）在多个位点上结合强度的总和，还受 valency 与抗体—抗原结构排布影响。
- **稀释倍数是方法学变量。** 对多克隆血清而言，稀释会改变抗体群体的组成，从而改变表观 avidity 和区分不同抗原的能力，而不只是改变信号强弱。
- **检测格式必须与免疫方式匹配。** 免疫途径决定了产生哪些 isotype，总抗体检测、isotype-specific 检测与抗原清除检测回答的是不同的问题。

以上内容整理自 Crowther（2009）相关章节。