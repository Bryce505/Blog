---
draft: true
reviewNotes:
  - "正文过短: 3007/13045=23% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,806 字符（原文 16,405，比例 17%）超出 9,023～15,585 字符的区间"
title: "ELISA 理论基础：抗原性、抗体亲和力与免疫应答中的检测选择"
date: 2026-10-30
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记梳理 ELISA 理论部分最底层的几个环节：抗原的尺寸如何影响可结合位点数量、表位相关术语如何界定、亲和力与亲合力（avidity）有何区别，以及免疫应答产生的抗体类型如何反过来决定检测策略。全文按“抗原—抗体—免疫应答”的顺序展开。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记梳理 ELISA 理论部分最底层的几个环节：抗原的尺寸如何影响可结合位点数量、表位相关术语如何界定、亲和力与亲合力（avidity）有何区别，以及免疫应答产生的抗体类型如何反过来决定检测策略。全文按“抗原—抗体—免疫应答”的顺序展开。

## 抗原尺寸决定其复杂性与可结合位点数量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）

也就是说，这一估算建立在两个前提之上：整个分子表面都具有抗原性（实际上很少成立），以及分子达到最大结合。因此，算出的数值只是理论上限，并不代表真实表位数量。它真正的用途是反推实验条件——"calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009）。

## 表位、表位型与互补位：三个容易混淆的定义

- **epitope**：即 antigenic site，抗原上被抗体识别的位点。
- **Epitype**（表位型）：指抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力不是一回事

### affinity：单一结合位点上的结合能

affinity（binding affinity）在笔记中给出三层表述：一是单个 epitope 与 paratope 之间的能量；二是**在单一结合位点上**抗原表位与抗体互补位之间相互作用的强度；三是由非共价相互作用介导，包括氢键、静电作用、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

### avidity：所有位点结合强度的总和

avidity 又称 functional affinity，指与抗原的总结合能。它是抗体在每个结合位点上总结合强度的量度。不同抗原位点上的抗体群，其各个亲和力之和构成一个平均结合能——"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009）；在血清层面，"Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009）。

avidity 受三个因素影响：**binding affinity、valency，以及抗体与抗原的结构排布**。

### 稀释会改变血清的表观亲合力

这一点在实际操作中容易被忽略。设想一份血清，其中针对某一复杂抗原的高亲和力抗体数量很少，而低亲和力抗体数量很多。在血清**未大幅稀释**的免疫分析条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体会优先结合；一旦稀释，高亲和力抗体的浓度持续下降，最终只剩低亲和力抗体在起作用。

这在使用免疫分析、以不同抗血清的差异活性来比较抗原时尤其重要——"The dilution of any serum can affect its ability to discriminate between antigens"，原因在于异质性抗体群的动力学（各抗体分子的相对浓度与亲和力）。

## 免疫应答产生的抗体类型决定检测怎么选

### 多克隆应答与 isotype 的时序

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 被动免疫与主动免疫

passive immunization 是直接注射中和抗体；active immunization 则是接种抗原、由机体自身产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）。这种方式可以诱导产生多种抗体类型（isotype），因此必须考虑：评估疫苗接种效果时，究竟采用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。

口服或吸入免疫则引出另一个判断：isotype-specific 抗体（尤其是 IgA）的检测，是否比总抗体检测更能反映疫苗接种的收益。

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）

## 小结

这篇笔记的核心线索是：抗原侧的性质（尺寸、表位数）只给出理论上限；抗体侧的性质要区分单一结合位点的 affinity 与多价、多位点叠加的 avidity，且后者会随稀释而漂移；免疫应答侧则要区分抗体 isotype，因为检测对象的选择本身就决定了能测到什么。几点边界值得记住——表面积除以 20nm^2 的估算依赖两个通常不成立的前提；以不同抗血清比较抗原时，稀释倍数会直接影响判别能力；疫苗效果评价中总抗体与 isotype-specific 检测的取舍，需要按免疫途径逐案判断，笔记并未给出统一答案。