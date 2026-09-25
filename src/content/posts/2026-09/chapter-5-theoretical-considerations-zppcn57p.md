---
draft: true
reviewNotes:
  - "正文过短: 3937/13045=30% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,909 字符（原文 16,405，比例 24%）超出 9,023～15,585 字符的区间"
title: "ELISA 理论基础：抗原性、抗体亲和力与 avidity"
date: 2026-09-25
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的结果最终由抗原与抗体之间的相互作用决定。这篇笔记整理了该相互作用的几个理论侧面：抗原分子大小如何决定可用的结合位点数量、表位与表位型如何界定、affinity 与 avidity 的区别，以及免疫应答中抗体类型的产生规律与相应的检测策略选择。按这条脉络可以看出，EL"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的结果最终由抗原与抗体之间的相互作用决定。这篇笔记整理了该相互作用的几个理论侧面：抗原分子大小如何决定可用的结合位点数量、表位与表位型如何界定、affinity 与 avidity 的区别，以及免疫应答中抗体类型的产生规律与相应的检测策略选择。按这条脉络可以看出，ELISA 实验设计中几个被视为「常规」的参数——抗体用量、血清稀释倍数、检测对象——各自都有理论依据，也都有适用边界。

## 抗原分子大小与 Fab 结合位点数量的估算

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有明确的前提——它假定整个分子表面都具有抗原性，且所有分子都达到最大结合：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）

即便前提很少成立，估算值在实际工作中仍有两个用途：计算饱和任何试剂所需的抗体量，或测定抗体结合水平随可用表面的变化：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009, p. 127）

## 表位、表位型与互补位

三个术语描述的其实是结合界面两侧的不同层次：

- **epitope**：antigenic site，即抗原位点；
- **paratope**：抗体上结合抗原表位的部分；
- **Epitype（表位型）**：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009, p. 128）

换言之，epitope 指向抗原表面的一个位点，epitype 指向覆盖该位点、但特异性略有差异的一组抗体。

## affinity 与 avidity：单一位点结合能与总体结合能

### affinity（亲和力）

抗体分子与抗原决定簇之间的结合能称为亲和力：

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009, p. 136）

其定义包含三层含义：

1. 单个 epitope 与 paratope 之间的能量；
2. 是抗原表位与抗体互补位在单一结合位点上的相互作用强度；
3. 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

### avidity（亲合力／功能亲和力）

avidity 是与抗原的总体结合能，也称 functional affinity：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009, p. 130）

对血清这类异质性抗体群，avidity 的另一个表述是：

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009, p. 137）

抗体在每个结合位点上总体结合强度的量度称为 avidity，其影响因素有三个：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 稀释会改变血清的 avidity，因而影响抗原辨别

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009, p. 137）

典型情形是：血清中可能含有少量的、对某一复杂抗原呈高亲和力的抗体，同时含有大量的低亲和力抗体。在血清未大幅稀释的免疫分析条件下，高、低亲和力抗体会竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度被逐步降低，直至体系中只剩下低亲和力抗体。当操作者用免疫分析、通过不同抗血清的差异活性来比较抗原时，这类问题尤其重要。由于异质性抗体群的动态变化（各抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力。

## 免疫应答中的抗体类型与检测策略选择

### 抗体类型不只限于 IgG

应对抗原刺激，机体产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

（Crowther, 2009）

### 主动免疫与被动免疫

- passive immunization：直接注射中和抗体；
- active immunization：接种抗原，由机体产生保护性抗体。

### 给药途径决定需要检测什么

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）。这种方式可以诱导产生多种抗体类型（isotype），因此必须考虑：是用总抗体检测、isotype-specific assay，还是检测抗原清除来评估疫苗接种效果。

口服／吸入免疫则需要另一层判断：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）

## 适用边界与遗留问题

- 以球形表面积除以 20nm^2 来推算 Fab 结合位点数量，只在上限意义上成立：它同时假定整个表面具有抗原性、且分子达到最大结合，而这一前提「很少是真实的」。因此该估算可用于推算饱和所需的抗体量或结合量随可用表面的变化趋势，但不能当作实际结合化学计量比。
- affinity 与 avidity 是两个层次的量。affinity 是单一结合位点上的强度，以非共价作用介导、由 K<sub>D</sub> 定义；avidity 是总体结合强度，受 binding affinity、valency 与抗原抗体结构排布三者影响。对血清这类异质性群体，avidity 是所有不同亲和力之和的平均值。
- 由此产生一个容易被忽略的操作后果：稀释本身就会改变血清的 avidity，也就会改变血清区分不同抗原的能力。在比较不同抗血清、或评估疫苗免疫效果时，稀释倍数与检测对象（总抗体 vs isotype-specific，尤其 IgA）都不是可以随意设定的参数。
- 笔记给出了 avidity 变化的定性描述与影响因素，但未涉及将上述估算用于定量换算的具体方法；在需要定量结论时，仍需以实验测定为准。