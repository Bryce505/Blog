---
draft: true
reviewNotes:
  - "正文过短: 4904/13096=37% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 5,036 字符（原文 16,470，比例 31%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与免疫应答"
date: 2026-10-16
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量表现不只取决于板、酶和底物，还取决于抗原表面有多少可用表位、抗体以多大强度结合上去，以及免疫应答本身由哪些抗体群体构成。这篇笔记按「抗原—抗体—免疫应答」的次序整理这几组理论考量：抗原分子大小与可结合 Fab 位点数的关系、epitope／epitype／par"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量表现不只取决于板、酶和底物，还取决于抗原表面有多少可用表位、抗体以多大强度结合上去，以及免疫应答本身由哪些抗体群体构成。这篇笔记按「抗原—抗体—免疫应答」的次序整理这几组理论考量：抗原分子大小与可结合 Fab 位点数的关系、epitope／epitype／paratope 的定义边界、affinity 与 avidity 的区分及其在稀释条件下的变化，最后落到疫苗接种后该选择哪一类抗体检测来评价效果。

## 抗原分子的大小决定可结合的 Fab 位点上限

分子越大，其复杂性也就越高。

Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

这一算法有明确的前提：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”(Crowther, 2009, p. 127)——即整个表面具有抗原性(很少是真实的)和分子最大结合的事实。换言之，球形表面积除以 20 得到的是位点数的上限而非实测值。

它的实际用途在于“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”(Crowther, 2009, p. 127)，也就是估算饱和某一试剂所需的抗体量，或测定抗体结合量随可用表面的变化。

## 表位、表位型与互补位：三个容易混用的定义

**epitope**：antigenic site，抗原上被抗体识别的位点。

**Epitype**：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”(Crowther, 2009, p. 128)。表位型是抗原上的一个区域，由一组化学结构非常相似的抗体(例如 mAbs，它们定义重叠或相互关联的表位)识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

**paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单价结合能与功能性亲和力

### affinity 描述单一结合位点上的结合能

1. the energy between a single epitope and paratope；
2. the binding affinity is the strength of the interaction between the antigen’s epitope and the antibody’s paratope at a singular binding site；
3. Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K<sub>D</sub>)。

用一句话概括：“The binding energy between an antibody molecule and an antigen determinant is termed affinity.”(Crowther, 2009, p. 136)

### avidity 是群体层面的功能性亲和力

1. overall binding energy with an antigen；
2. 抗体在每一个结合位点上总结合强度的量度称为 avidity，也称 functional affinity；
3. 三个影响因素：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question。

两种表述指向同一件事：“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”(Crowther, 2009, p. 130)；而“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”(Crowther, 2009, p. 137)。亲和力可以看作是血清中包含的异质性抗体与各种抗原位点(抗原表位)之间所有不同亲和力的总和。

## 稀释会改变血清的表观 avidity 与抗原区分能力

“It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”(Crowther, 2009, p. 137)。这一点在异质性抗体群体中尤其明显：

> “As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).”(Crowther, 2009, p. 137)

换句话说，血清的 avidity 在稀释时可能发生变化，因为操作者可能把某些群体的抗体稀释掉。当需要用免疫分析比较抗原与不同抗血清的差异活性时，这一效应直接决定了稀释度不可随意选取。

## 免疫与疫苗接种后的抗体应答：该检测哪一类抗体

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型的产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 主动免疫与被动免疫的区别

passive immunization：直接打中和抗体；active immunization：服用抗原，产生保护性抗体。

### 免疫途径决定检测策略

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型——isotype；因此必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。口服/吸入免疫则另有考量：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”(Crowther, 2009, p. 140)——即同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地反映疫苗接种的获益。

## 这些理论前提在方法设计中的位置

把上述内容收拢起来，有几条边界需要在设计 assay 时记住。

第一，由球形表面积推算 Fab 结合位点数的做法给出的是上限，它默认整个表面都有抗原性并且分子达到最大结合，而这两个前提都很少成立，因此该数值只能用于估算饱和所需抗体量这类用途。

第二，affinity 与 avidity 不可互换：affinity 描述单一 epitope–paratope 的相互作用并以 K<sub>D</sub> 定义，avidity 则是抗体群体的功能性亲和力，由 binding affinity、valency 以及抗体与抗原的结构排布共同决定；用单价参数去预测多克隆血清的行为会失真。

第三，血清的 avidity 会随稀释而改变，稀释可能把高亲和力抗体群体优先稀释掉，因此在用不同抗血清比较抗原差异活性时，稀释度本身就是变量。

第四，疫苗接种效果的评价不存在默认选项：sc/im 免疫会诱导多种 isotype，究竟用总抗体检测、isotype-specific assay 还是抗原清除检测，需要结合免疫途径（包括口服/吸入）来判断；口服/吸入免疫下是否改用 IgA 特异的检测，仍是需要由方法学人员自行判断的问题。