---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['135']"
  - "正文过短: 3855/13096=29% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗原免疫后产生的抗体应答与抗体类型']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,793 字符（原文 16,470，比例 23%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答"
date: 2026-11-16
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本文整理 ELISA 赖以成立的一组基础概念：抗原分子大小与可结合位点数的关系、表位与表位型的定义、affinity 与 avidity 的区分，以及抗原免疫后抗体应答的类型与相应检测策略的选择。内容按「抗原—抗体—免疫应答—检测设计」的顺序展开，落点在这些概念对免疫分析设计与结"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本文整理 ELISA 赖以成立的一组基础概念：抗原分子大小与可结合位点数的关系、表位与表位型的定义、affinity 与 avidity 的区分，以及抗原免疫后抗体应答的类型与相应检测策略的选择。内容按「抗原—抗体—免疫应答—检测设计」的顺序展开，落点在这些概念对免疫分析设计与结果解读的约束上。

## 抗原分子大小如何限制可结合位点数

分子越大，其复杂性也就越高。Fab 结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

这个计算有明确的前提，原文的表述是：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009, p. 127）。也就是说，它假定整个分子表面都具有抗原性（这很少成立），且分子达到最大结合。因此该算法给出的是上限，而非实测的表位数。

其用途也由这一前提界定：calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface（Crowther, 2009, p. 127）。即用于估计饱和某一试剂所需的抗体量，或把抗体结合量表达为可用表面积的函数。

## 表位、表位型与互补位

三个名词需要在同一层次上界定清楚：

- epitope：antigenic site，抗原上被抗体识别的位点；
- Epitype（表位型）：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009, p. 128）。即由一组化学结构识别上非常接近的抗体（例如定义重叠或相互关联表位的 mAb）所界定的抗原区域，可视为同一抗原位点上特异性略有差异的抗体所识别的区域；
- paratope：抗体上结合抗原表位的部分。

## affinity 与 avidity：单一位点与整体结合

### affinity

affinity 指单个 epitope 与 paratope 之间的能量，是单一结合位点上的相互作用强度（the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site）。这种作用由非共价相互作用介导，包括氢键、静电作用、范德华力与疏水作用，并以平衡解离常数（K_D）表征（Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant）。

### avidity

avidity 即 functional affinity，指与抗原结合的总能量。原文对其量的表述是：“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009, p. 130）。抗体在每个结合位点上结合强度的总和即 avidity（The measure of the total binding strength of an antibody at every binding site is termed avidity），亦称 functional affinity。影响因素有三个：the binding affinity、valency，以及 the structural arrangement of the antibody and antigen in question。

## 抗原免疫后产生的抗体应答与抗体类型

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\
（Crowther, 2009, p. 135）

## 血清稀释如何改变亲合力与抗原鉴别能力

“抗体分子与抗原决定簇之间的结合能称为亲和力”（Crowther, 2009, p. 136）。血清层面的量则不同：“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”（Crowther, 2009, p. 137）——即血清亲合力是其中异质性抗体与各抗原位点之间全部不同亲和力的总和。

由此可以引出一个常被忽略的操作性后果：“It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”（Crowther, 2009, p. 137）。典型情形是：血清中含有少量对某复杂抗原高亲和力的抗体，同时含有大量低亲和力抗体。在稀释程度不大的免疫分析条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；随着稀释进行，高亲和力抗体浓度下降，最终只剩低亲和力抗体。用免疫分析比较不同抗血清与抗原的差别活性时，这一问题很重要——任何血清的稀释都可能因其异质性抗体群体的动力学（各抗体的相对浓度与亲和力）而影响其区分抗原的能力。

## 免疫途径与检测策略的选择

passive immunization 是直接给予中和抗体；active immunization 是给予抗原、由机体产生保护性抗体。

疫苗经 sc（皮下注射）或 im（肌内注射）接种，可诱导产生多种抗体类型（isotype）。因此在评估疫苗接种效果时，必须先确定是采用总抗体检测、isotype-specific assay，还是检测抗原清除。

口服/吸入免疫还涉及另一层选择：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”（Crowther, 2009, p. 140）。

## 这些前提对分析设计与结果解读的意义

上面这些概念有一个共同特征：它们并不提供可直接照搬的数值，而是划定条件。由表面积推算的位点数只是上限，假定的是全表面具抗原性且结合饱和，二者在真实抗原上都很难成立；血清亲合力随稀释而变，意味着稀释度本身就是一个方法变量，比较不同抗血清或不同抗原时的结论会随之漂移；免疫途径决定了抗体类型的分布，因而总抗体检测与 isotype-specific 检测不能相互替代。这几条一旦在设计与解读中被忽略，得到的效价或比较结论就难以在不同稀释度、不同抗血清之间迁移。