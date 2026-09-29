---
draft: true
reviewNotes:
  - "正文过短: 4179/13045=32% < 40%"
  - "空壳章节（正文不足 120 字）: ['免疫应答中的抗体产生：多克隆与同种型']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,210 字符（原文 16,405，比例 26%）超出 9,023～15,585 字符的区间"
title: "ELISA 理论基础：抗原表位规模、抗体亲和力与亲合力、免疫应答中的抗体类型"
date: 2026-09-29
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本篇把 ELISA 建立与判读所依赖的几个理论前提归拢到一起：抗原大小与可结合位点数量的关系、表位/表位型/互补位的界定、亲和力与亲合力的区分、血清稀释对抗体群体行为的影响，以及免疫应答中多克隆抗体与同种型的产生及其对检测策略的牵制。内容按「抗原 — 抗体 — 免疫应答」的顺序组"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本篇把 ELISA 建立与判读所依赖的几个理论前提归拢到一起：抗原大小与可结合位点数量的关系、表位/表位型/互补位的界定、亲和力与亲合力的区分、血清稀释对抗体群体行为的影响，以及免疫应答中多克隆抗体与同种型的产生及其对检测策略的牵制。内容按「抗原 — 抗体 — 免疫应答」的顺序组织，来源为 Crowther《The ELISA Guidebook》第 5 章的阅读笔记。

## 抗原大小如何决定可结合的 Fab 位点数量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20 nm²，这一面积大致对应一个 epitope 的表面积。通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个估算有两个前提，原文明确点出了它们：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009, p. 127)

即：这样的计算基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

该计算的两类应用是：估算饱和任一试剂所需的抗体量，或者测量抗体结合水平与可用表面的关系（Crowther, 2009, p. 127）。

## 表位、表位型与互补位

epitope 即 antigenic site（抗原表位）。

Epitype（表位型）的定义是：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009, p. 128)

表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别；表位型可视为识别与同一抗原位点反应的、特异性略有不同的抗体所作用的区域。

paratope（互补位）则是抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一位点结合能与总体结合强度

affinity（结合亲和力）指的是单个 epitope 与 paratope 之间的能量，即在单一结合位上抗原表位与抗体互补位相互作用的强度。它由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡解离常数（K<sub>D</sub>）定义。原文的概括是：

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009, p. 136)

avidity（亲合力），又称 functional affinity（功能性亲和力），指抗体在所有结合位点上的总结合强度：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009, p. 130)

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009, p. 137)

亲合力有三个影响因素：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 血清稀释为什么会改变亲合力

血清的亲合力在稀释时可能发生变化，因为操作者可能把某些群体的抗体稀释掉了（Crowther, 2009, p. 137）。原文给出的例子是：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)." (Crowther, 2009, p. 137)

也就是说，血清中可能同时存在少量针对某一复杂抗原的高亲和力抗体和大量低亲和力抗体；在血清未大幅稀释的条件下，高低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；而稀释会把高亲和力抗体的浓度压低，直到只剩下低亲和力抗体。这一点在操作者用免疫分析、以不同抗血清的差异活性比较抗原时尤其重要——任何血清的稀释都可能影响其区分抗原的能力，原因在于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力）。

## 免疫应答中的抗体产生：多克隆与同种型

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 免疫方式与检测策略的选择

passive immunization 是直接给予中和抗体；active immunization 是给予抗原，由机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑是用总抗体检测、isotype-specific assay，还是检测抗原清除的检测来评估疫苗接种效果。

口服／吸入免疫则把问题引向检测对象本身：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)

即：免疫分析人员必须决定，同种型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地反映疫苗接种的收益。

## 小结：这些理论前提在实操中的位置

把上述几点放在一起，可以归出四条边界：

- Fab 结合位点数量按「球形表面积 ÷ 20 nm²」估算，得到的只是上限，其成立依赖「整个表面具有抗原性」与「分子最大结合」这两个很少成立的前提。
- affinity 是单一位点层面的量，以 K<sub>D</sub> 定义、由非共价作用决定；avidity 是群体层面的量，由亲和力、valency 和抗体—抗原的结构排布共同决定。
- 血清的亲合力不是固定属性：稀释会改变异质性抗体群体的组成，进而影响血清区分抗原的能力，这在用不同抗血清比较抗原时需要预先考虑。
- 在评估免疫或疫苗接种效果之前，先要确定检测对象是总抗体、特定 isotype（如 IgA），还是抗原清除。