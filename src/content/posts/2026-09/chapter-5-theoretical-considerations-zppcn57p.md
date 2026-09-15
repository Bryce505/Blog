---
draft: true
reviewNotes:
  - "正文过短: 4568/13045=35% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,641 字符（原文 16,405，比例 28%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原特性、抗体亲和力与亲合力"
date: 2026-09-15
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的表现并不只由试剂盒决定——抗原的尺寸与表位分布、抗体与表位之间的结合能、血清中抗体群体的组成，都会直接影响检测的灵敏度与特异性。本文按 Crowther《The ELISA Guidebook》第五章的脉络整理四组概念：抗原尺寸与表位数量的推算关系及其前提、epit"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的表现并不只由试剂盒决定——抗原的尺寸与表位分布、抗体与表位之间的结合能、血清中抗体群体的组成，都会直接影响检测的灵敏度与特异性。本文按 Crowther《The ELISA Guidebook》第五章的脉络整理四组概念：抗原尺寸与表位数量的推算关系及其前提、epitope / epitype / paratope 的界定、affinity 与 avidity 的区分及 avidity 的三个影响因素，以及免疫途径对抗体类型与检测方式选择的约束。

## 抗原尺寸与可结合位点数：一个受前提约束的估算

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"
>
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。（Crowther, 2009, p. 127）

这个估算的用途是 "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009, p. 127）——即推算饱和某一试剂所需的抗体量，或把抗体结合水平表达为可利用表面的函数。

## 表位相关的术语：epitope、epitype 与 paratope

三个术语的边界需要先厘清：

- **epitope**：antigenic site。
- **epitype**："An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"——表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别；表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。（Crowther, 2009, p. 128）
- **paratope**：抗体上结合抗原表位的部分。

## affinity：单一结合位点上的结合能

笔记对 affinity 归纳了三层表述：

1. the energy between a single epitope and paratope；
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope **at a singular binding site**；
3. Affinity is mediated by **non-covalent interactions** that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium **dissociation constant (K<sub>D</sub>)**。

归结成一句："The binding energy between an antibody molecule and an antigen determinant is termed affinity."——抗体分子与抗原决定簇之间的结合能称为亲和力。（Crowther, 2009, p. 136）

## avidity：抗体整体的结合强度及其三个影响因素

avidity 又称 functional affinity（功能亲和力），其定义为 overall binding energy with an antigen；"The measure of the total binding strength of an antibody at every binding site is termed avidity."。若强调的是群体层面，"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009, p. 130）；针对血清样本则是 "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009, p. 137）。

影响 avidity 的因素有三个：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 稀释会改变血清的 avidity，从而改变抗原区分能力

"It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies."（Crowther, 2009, p. 137）

原文举的情形是：血清中可能同时含有 **a low quantity of antibodies showing high affinity** 与 **a high quantity of low-affinity antibody**。在血清 **not diluted greatly** 的免疫分析条件下，高亲和力与低亲和力抗体竞争抗原位点，**the high-affinity antibodies would react preferentially**；但一经稀释，高亲和力抗体的浓度被降低，最终只剩下低亲和力抗体。当操作者用免疫分析 **compare antigens by their differential activity with different antisera** 时，这类问题就变得重要——**The dilution of any serum can affect its ability to discriminate between antigens**，原因是异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力）。（Crowther, 2009, p. 137）

## 免疫方式决定了该选哪一类抗体检测

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

passive immunization：直接打中和抗体；active immunization：服用抗原，产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型-isotype；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫的情形下，"The immunoassayist must decide whether an assay for **isotype-specific antibodies**, notably IgA, may provide deeper insight into the benefits of vaccination than an **assay for total antibody**"——同型抗体（特别是 IgA）的检测是否能比总抗体检测更深入地反映疫苗接种的收益，是设计检测时需要先决定的问题。（Crowther, 2009, p. 140）

## 小结：这些概念约束了什么

把以上内容收拢，可以得到几条在使用 ELISA 时绕不开的边界：

- 按球形表面积除以 20nm^2 估出的 Fab 结合位点数是一个上限。它建立在"整个表面都具有抗原性"和"分子最大结合"这两个很少同时成立的前提上，实际可结合位点只会更少。
- affinity 描述的是单一结合位点上的结合能，由氢键、静电作用、范德华力与疏水作用等非共价相互作用介导，以平衡解离常数 K<sub>D</sub> 表征；avidity 描述的是抗体在各个结合位点上的总体结合强度，由 binding affinity、valency 以及抗体与抗原的结构排布共同决定。讨论多克隆血清或完整 IgG 的结合行为时，用 affinity 会失真。
- 血清的 avidity 会随稀释改变，因为稀释改变了抗体群体的组成。凡是用免疫分析比较不同抗血清对抗原的区分能力，稀释度本身就是一个变量，而不是可以随意固定的参数。
- 免疫途径（sc/im 与口服/吸入）决定了产生的抗体 isotype 分布，从而决定了后续该选总抗体检测还是 isotype-specific 检测；这一选择在方法设计阶段就要确定，不能留到数据分析时再补。

笔记中若干问题被明确留给操作者判断，例如是否采用 isotype-specific assay、以何种稀释度比较不同抗血清——这些属于方法学决策，取决于具体的抗原与检测目的。