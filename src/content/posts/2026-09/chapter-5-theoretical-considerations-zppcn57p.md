---
draft: true
reviewNotes:
  - "正文过短: 3047/13096=23% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,410 字符（原文 16,470，比例 21%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论考量：抗原大小、affinity/avidity 与抗体应答的定量含义"
date: 2026-09-22
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理 ELISA 检测背后的几个基础理论概念——抗原分子大小如何决定 Fab 结合位点数量的上限、epitope/epitype/paratope 的定义边界、affinity 与 avidity 的区别，以及血清稀释和免疫途径如何改变这些量。内容取自 Crowther (2"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理 ELISA 检测背后的几个基础理论概念——抗原分子大小如何决定 Fab 结合位点数量的上限、epitope/epitype/paratope 的定义边界、affinity 与 avidity 的区别，以及血清稀释和免疫途径如何改变这些量。内容取自 Crowther (2009) 第 5 章的相关论述，末尾归拢这些前提对数据解读的限制。

## 抗原分子越大，可容纳的 Fab 结合位点越多——但那只是上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20 nm²，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有明确前提。Crowther (2009) 指出："Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"，即此类计算建立在「整个表面都具有抗原性」（很少成立）和「分子达到最大结合」这两个假设之上。实际可结合位点数通常低于该计算值。

在应用层面，这类计算可用于估算饱和任意一种试剂所需的抗体量，或测定抗体结合水平随可用表面的变化——"calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009)。

## epitope、epitype 与 paratope

epitope 即 antigenic site。

Epitype 指抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别；可视为识别同一抗原位点、但特异性略有差异的抗体所对应的区域。原文定义："An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009)。

paratope 指抗体上结合抗原表位的部分。

## affinity 与 avidity：单点结合能与整体结合强度

**Affinity（binding affinity）** 有三层表述：其一，单个 epitope 与 paratope 之间的能量；其二，抗原 epitope 与抗体 paratope 在**单个结合位点**上的相互作用强度；其三，由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡**解离常数 KD** 定义。

**Avidity（functional affinity）** 则是另一个量：

- 它表示与抗原的总结合能。"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009)
- 它是抗体在所有结合位点上总结合强度的度量，也称 functional affinity；
- 三个影响因素：binding affinity、valency，以及抗体与抗原的结构排布。

在血清语境下，avidity 可看作血清中包含的异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和——"Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009)。

## 血清稀释会改变 avidity，进而改变抗原区分能力

"It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009)。

一个具体的例子：血清中可能同时存在**少量高亲和力抗体**和**大量低亲和力抗体**。在血清**稀释倍数不大**的免疫分析条件下，两类抗体会竞争抗原位点，**高亲和力抗体优先反应**；而随着稀释进行，高亲和力抗体的浓度不断下降，最终只剩下低亲和力抗体。

当操作者用免疫分析、以不同抗血清的差异活性来比较抗原时，这类问题尤其重要：由于异质抗体群的动态变化（各个抗体分子的相对浓度与亲和力），**任何血清的稀释都可能影响其区分抗原的能力** (Crowther, 2009)。

## 免疫应答产生的抗体类型与检测策略

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

passive immunization 指直接注射中和抗体；active immunization 指给予抗原、由机体产生保护性抗体。

疫苗以 sc（皮下注射）或 im（肌内注射）方式接种，可诱导产生多种抗体类型（isotype）；因此必须考虑评估疫苗接种效果时究竟采用总抗体检测、isotype-specific assay，还是检测抗原清除。

对口服/吸入免疫而言，Crowther (2009) 提出："The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"——即检测 isotype 特异性抗体（尤其是 IgA）是否比检测总抗体更能反映疫苗接种的收益，需要由方法开发者自行判断。

## 这些理论前提界定了 ELISA 数据的适用范围

归拢来看，本节涉及的几个概念各自都带有前提条件：

基于球形表面积除以 20 nm² 得到的表位数量只是理论上限，它假定整个表面都有抗原性、且分子达到最大结合，这两点在真实抗原上很少同时成立。affinity 描述单个结合位点上的相互作用，avidity 描述抗体群与多个抗原位点的总和，两者不可互换使用。由于血清稀释会改变异质抗体群的组成，不同稀释度下测得的 avidity 及抗原区分能力不具备直接可比性。免疫途径与 isotype 分布则决定了评价疫苗效果时应选择总抗体检测、isotype-specific 检测还是抗原清除检测——这一选择本身仍依赖于具体疫苗与免疫途径，笔记中并未给出统一判据。