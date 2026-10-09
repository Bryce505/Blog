---
draft: true
reviewNotes:
  - "正文过短: 3619/13045=28% < 40%"
  - "空壳章节（正文不足 120 字）: ['免疫刺激产生的抗体类型与血清的异质性']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,521 字符（原文 16,405，比例 21%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：表位、亲和力与亲合力，以及稀释对判读的影响"
date: 2026-10-09
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理自 Crowther《The ELISA Guidebook》第 5 章的理论部分，讨论 ELISA 作为定量工具时，抗原与抗体两端各自带来哪些不确定因素。内容按三条线展开：抗原侧（尺寸与表位）、抗体侧（亲和力与亲合力、免疫应答产生的抗体类型）、以及两者相遇时的实验条"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理自 Crowther《The ELISA Guidebook》第 5 章的理论部分，讨论 ELISA 作为定量工具时，抗原与抗体两端各自带来哪些不确定因素。内容按三条线展开：抗原侧（尺寸与表位）、抗体侧（亲和力与亲合力、免疫应答产生的抗体类型）、以及两者相遇时的实验条件（稀释、免疫途径）。归拢这些理论前提的目的，是说明同一个样品换一套稀释方案为什么可能得到不同结论。

## 抗原尺寸决定了可结合位点数的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。但需要明确这一估算的前提——「这样的计算是基于整个表面具有抗原性(很少是真实的)和分子最大结合的事实」(Crowther, 2009)。

在这一前提下，估算结果有两个用途：calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface (Crowther, 2009)。

## 表位、表位型与 paratope：三个容易混用的概念

- **epitope**：antigenic site。
- **Epitype**（表位型）：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体(例如 mAbs，它们定义重叠或相互关联的表位)识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域 (Crowther, 2009)。
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一位点的结合能与总体结合强度

**affinity（binding affinity）** 有三层含义：

1. 单个 epitope 与 paratope 之间的能量；
2. binding affinity 是抗原的 epitope 与抗体的 paratope 在 singular binding site 上相互作用的强度；
3. affinity 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

**avidity（functional affinity）**：

1. 与抗原的总结合能。原文表述为：the avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites (Crowther, 2009)；
2. 抗体在每个结合位点上总结合强度的量度称为 avidity，也称功能性亲和力（functional affinity）；
3. 三个影响因素：1) the binding affinity, 2) valency, 3) the structural arrangement of the antibody and antigen in question。

两处原文表述可以进一步限定这两个概念：the binding energy between an antibody molecule and an antigen determinant is termed affinity (Crowther, 2009)；而在讨论血清体系时，avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes) (Crowther, 2009)。前者描述单一决定簇，后者描述异质抗体群的加和。

## 免疫刺激产生的抗体类型与血清的异质性

机体应对抗原刺激产生抗体，得到的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 稀释会改变血清的表观亲合力

It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies (Crowther, 2009)。

原文给出的例子是：血清中可能同时存在 a low quantity of antibodies showing high affinity 与 a high quantity of low-affinity antibody。在 not diluted greatly 的免疫测定条件下，高亲和力与低亲和力抗体竞争抗原位点，此时 the high-affinity antibodies would react preferentially；而一旦稀释，高亲和力抗体的浓度被降低，until we would be left only with low-affinity antibodies。这类问题在操作者用免疫测定比较不同抗血清对抗原的差异活性时尤其重要：the dilution of any serum can affect its ability to discriminate between antigens，其根源在于异质抗体群的动力学，即各抗体分子的相对浓度与亲和力 (Crowther, 2009)。

## 免疫途径决定了该选哪一种检测形式

- **passive immunization**：直接打中和抗体；
- **active immunization**：服用抗原，产生保护性抗体。

疫苗的注射方式为 sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型-isotype；因此必须考虑是使用总抗体检测、isotype-specific assay，还是检测抗原清除的检测，来评估疫苗接种效果。

对于口服/吸入免疫，原文的判断是：the immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody (Crowther, 2009, p. 140)。

## 这些前提对方法开发的边界含义

把上述内容归拢起来，可以得出几条对方法开发有约束力的结论：

**抗原侧**，基于球形表面积除以 20nm^2 得到的 Fab 结合位点数只是一个上限，其成立依赖「整个表面具有抗原性」和「分子最大结合」两个很少同时满足的条件，因此只能用于估算饱和所需抗体量这类量级判断，不能当作真实表位数。

**抗体侧**，affinity 描述单一 epitope–paratope 的结合，avidity 描述异质抗体群与多个抗原位点的总结合强度，二者在数值上不可互相替代；avidity 由 binding affinity、valency 以及抗体与抗原的结构排布共同决定。

**操作条件侧**，稀释不是中性的：它会选择性去除高亲和力抗体群体，从而改变血清的表观亲合力，进而影响用不同抗血清比较抗原时的判别能力。这意味着稀释方案一旦变动，跨批次或跨血清的比较结论就需要重新确认。

尚未被这套理论处理的问题，是上述前提在具体检测体系中的量化边界——何时可以忽略亲和力群体的再分配、何时必须改用 isotype-specific 检测来替代总抗体检测，取决于该体系自身，而不是这些一般性论述能够直接给出的。