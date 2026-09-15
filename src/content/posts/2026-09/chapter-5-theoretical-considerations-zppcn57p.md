---
draft: true
reviewNotes:
  - "正文过短: 3943/13096=30% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,889 字符（原文 16,470，比例 24%）超出 9,058～15,646 字符的区间"
title: "ELISA 理论基础：抗原表位、抗体亲和力与免疫应答产生的抗体类型"
date: 2026-09-15
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "抗原–抗体反应是 ELISA 定量的基础，但它并不是「一个抗原决定簇对一个抗体」的简单模型。本文按抗原侧与抗体侧两条线索整理相关的理论概念：先看分子大小如何限制可能的 Fab 结合位点数量，并界定 epitope、epitype、paratope；再区分 affinity 与 a"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

抗原–抗体反应是 ELISA 定量的基础，但它并不是「一个抗原决定簇对一个抗体」的简单模型。本文按抗原侧与抗体侧两条线索整理相关的理论概念：先看分子大小如何限制可能的 Fab 结合位点数量，并界定 epitope、epitype、paratope；再区分 affinity 与 avidity，说明血清稀释为什么会改变 avidity；最后落到免疫应答产生的抗体类型，以及它对检测策略选择的影响。

## 抗原侧：分子大小如何限制可能的结合位点数量

分子越大，其复杂性也就越高。

Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

这个估算有明确的前提。原文指出：「Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally」（Crowther, 2009, p. 127）——即该计算建立在「整个表面都具有抗原性（很少是真实的）」和「分子达到最大结合」这两点之上。换言之，由表面积除以 20nm^2 得到的是结合位点数的上限，而非实际可用的表位数。

它的用途在于「calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface」（Crowther, 2009, p. 127）：估算饱和某一试剂所需的抗体量，或把抗体结合水平作为可用表面的函数来测量。

## epitope、epitype 与 paratope：术语的界定

**epitope**：即 antigenic site（抗原位点）。

**paratope**：抗体上结合抗原表位的部分。

**epitype**：「An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site」（Crowther, 2009, p. 128）。表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）所识别；表位型可视为识别与同一抗原位点反应的、特异性略有不同的抗体的区域。

## affinity 与 avidity：单一位点与总体结合强度

### affinity

「The binding energy between an antibody molecule and an antigen determinant is termed affinity.」（Crowther, 2009, p. 136）具体而言：

- 它是单个 epitope 与 paratope 之间的能量；
- 是抗原表位与抗体 paratope 在**单一位点**（at a singular binding site）上相互作用的强度；
- 由**非共价**相互作用介导，包括氢键、静电键、范德华力与疏水相互作用，并由平衡解离常数（K_D）定义。

### avidity（functional affinity）

「The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites」（Crowther, 2009, p. 130）。抗体在每个结合位点上总结合强度的量度称为 avidity，也称 functional affinity。

进一步地，「Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)」（Crowther, 2009, p. 137）。

avidity 受三个因素影响：1）the binding affinity，2）valency，3）the structural arrangement of the antibody and antigen in question。

## 稀释为什么会改变血清的 avidity

「It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies」（Crowther, 2009, p. 137）。

一个典型情形是：血清中同时存在**少量**对某一复杂抗原具有**高亲和力**的抗体和**大量**低亲和力抗体。

- 在血清**稀释不大**的免疫分析条件下，高亲和力与低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；
- 稀释之后，高亲和力抗体的浓度不断降低，直到体系中只剩下低亲和力抗体。

这类问题在操作者用免疫分析、以不同抗血清对抗原的差异活性来比较抗原时尤其重要。由于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力），**任何血清的稀释都可能影响其区分抗原的能力**。

## 免疫应答产生的抗体类型及其对检测策略的影响

应对抗原刺激产生抗体时，产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

免疫方式分两类：passive immunization 是直接注射中和抗体；active immunization 是给予抗原、由机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）。这种方式可以诱导产生多种抗体类型（isotype），因此必须考虑：是用总抗体检测、isotype-specific assay，还是检测抗原清除来评估疫苗接种效果。

口服/吸入免疫的场合下，「The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody」（Crowther, 2009, p. 140）——同型抗体（特别是 IgA）的检测是否比总抗体检测更能反映疫苗接种的收益，是检测方案设计时必须作出的判断。

## 这些概念在检测设计中的位置

把上述内容归拢一下：

- **表位数量的估算只是上限。** 用球形表面积除以 20nm^2 可以得到 Fab 结合位点的最大数量，但该计算假定整个表面都具有抗原性、且分子达到最大结合，这两个条件在真实体系中很少同时成立。
- **affinity 与 avidity 处于不同层级。** affinity 描述单一位点上的结合能，由非共价相互作用与 K_D 定义；avidity 是群体水平上各亲和力的平均/总和，受 affinity、valency 以及抗体与抗原的结构排布共同影响。
- **稀释是一个会改变体系性质的变量。** 血清稀释会改变 avidity，因为在异质性抗体群体中不同亚群被稀释的程度不同；因此用不同抗血清比较抗原差异活性时，稀释条件本身就会影响区分能力。
- **免疫途径决定 isotype 分布，进而决定检测策略。** sc/im 接种可诱导多种 isotype，而口服/吸入途径下 IgA 的地位突出，总抗体、isotype-specific assay 与抗原清除指标三者反映的信息并不等价。

适用边界在于：以上都是抗原–抗体反应层面的理论判断，具体到某一次检测，仍需结合实际抗原的性质与所用抗血清的组成来判断，而不能直接套用理想化的结合模型。