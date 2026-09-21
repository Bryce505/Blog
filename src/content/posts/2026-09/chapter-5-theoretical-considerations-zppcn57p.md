---
draft: true
reviewNotes:
  - "正文过短: 4360/13096=33% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,383 字符（原文 16,470，比例 27%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力，以及免疫应答中的抗体类型"
date: 2026-09-21
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理 ELISA 检测赖以成立的理论前提：抗原分子大小如何决定可结合位点的上限、表位相关术语的界定、抗体亲和力（affinity）与亲合力（avidity）的区别，以及免疫应答中产生的抗体类型与免疫途径如何影响检测方案的选择。最后集中到一个具体的操作变量——血清稀释——对"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理 ELISA 检测赖以成立的理论前提：抗原分子大小如何决定可结合位点的上限、表位相关术语的界定、抗体亲和力（affinity）与亲合力（avidity）的区别，以及免疫应答中产生的抗体类型与免疫途径如何影响检测方案的选择。最后集中到一个具体的操作变量——血清稀释——对异质抗体群行为的影响。

## 分子越大越复杂，可结合的 Fab 位点上限也越高

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20 nm²，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）

这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

这一计算的实际用途有两方面：计算饱和任何试剂所需的抗体量，或测定抗体结合水平随可用表面的变化。

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009）

## 表位、表位型与互补位

epitope 指 antigenic site，即抗原上被识别的位点；paratope 指抗体上结合抗原表位的部分。

Epitype 则是另一个层面的概念：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009）

表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

## 亲和力与亲合力：单点相互作用与总体结合能

### affinity（binding affinity）

- 单个 epitope 与 paratope 之间的能量。
- 结合亲和力是抗原表位与抗体互补位之间、在单个结合位点上的相互作用强度。
- 亲和力由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009）

抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity（functional affinity）

- 与抗原的总体结合能。
- 抗体在每个结合位点上总结合强度的量度称为 avidity，也称 functional affinity。
- 三个影响因素：结合亲和力、价数（valency），以及抗体与抗原的结构排布。

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009）

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009）

亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

## 免疫接种后的抗体产生：多克隆背景与抗体类型

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

passive immunization 是直接注射中和抗体；active immunization 则是给予抗原、由机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：评估疫苗接种效果时，是使用总抗体检测、isotype-specific assay，还是检测抗原清除。

口服/吸入免疫则涉及另一个选择：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009）

免疫分析的设计者必须决定，同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地反映疫苗接种的收益。

## 血清稀释会改变抗体群的表观行为

血清中不同抗体群的浓度与亲和力并不一致，因此稀释本身就是一个会改变检测行为的操作。

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)."（Crowther, 2009）

也就是说，一份血清中可能同时存在少量高亲和力抗体和大量低亲和力抗体。在血清不作大幅稀释的免疫分析条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度被降低，最终只剩下低亲和力抗体。当操作者用免疫分析、以不同抗血清对抗原的差异活性来比较抗原时，这类问题很重要；由于异质抗体群的动力学（各个抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力。

## 这些前提对检测设计意味着什么

把上述几层合起来看，可以看到几个边界条件：

抗原侧的位点数目上限是一个理想值，它成立的前提是「整个表面都具有抗原性」和「分子达到最大结合」，两者在实际体系中通常都不满足，因此除以 20 nm² 得到的只是可结合位点数的上限，而非实测值。

抗体侧，affinity 描述的是单个结合位点上的相互作用，由非共价作用介导、以 K_D 定义；avidity 描述的是多个位点、乃至多克隆抗体群层面的总体结合能，受亲和力、价数和抗体—抗原结构排布三者共同影响。对血清这类异质群体，avidity 是各抗体—表位亲和力的总和，因而会随稀释而改变，这也是比较不同抗血清差异活性时必须控制的变量。

检测设计侧，免疫途径（sc/im 与口服/吸入）决定了所产生的 isotype 谱，进而决定了应当选择总抗体检测、isotype-specific assay（例如 IgA）还是抗原清除检测来回答问题。

需要说明的是，本章涵盖的范围包括抗原特性、抗体亲和力、酶反应动力学及浓度—反应关系，本笔记展开的是抗原特性与抗体两部分，酶反应动力学与浓度—反应关系未在此展开。