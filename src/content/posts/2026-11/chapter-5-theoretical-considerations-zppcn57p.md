---
draft: true
reviewNotes:
  - "正文过短: 3510/13045=27% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,382 字符（原文 16,405，比例 21%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力/亲合力与免疫应答"
date: 2026-11-15
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理 Crowther《The ELISA Guidebook》第 5 章的理论要点，先讲抗原一侧——分子大小如何决定可结合位点数的上限，以及 epitope、epitype、paratope 这几个常被混用的术语；再讲抗体一侧——affinity 与 avidity 的区分"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理 Crowther《The ELISA Guidebook》第 5 章的理论要点，先讲抗原一侧——分子大小如何决定可结合位点数的上限，以及 epitope、epitype、paratope 这几个常被混用的术语；再讲抗体一侧——affinity 与 avidity 的区分，以及免疫应答产生的多克隆、多同型抗体；最后落到一个实操中容易忽略的问题：血清稀释会改变亲合力，从而改变抗体区分抗原的能力。

## 抗原的大小决定可结合位点数的上限

分子越大，其复杂性也就越高。

Fab 与抗原结合的面积大概是 20nm^2，也就是 epitope 的表面积；据此可以通过计算分子的球形表面积，再把表面积除以 20，获得 Fab 结合位点的最大数量。

这个估算建立在两个假设之上：“整个表面都具有抗原性（很少是真实的）和分子最大结合”（Crowther, 2009）。两个假设都偏向高估，所以算出来的数字是理论上限，不是实际结合数。

它的用途在于两个方向：“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”（Crowther, 2009）——即估算饱和某一试剂所需的抗体量，或测定抗体结合量随可用表面变化的函数关系。

## 表位与结合位点：几个不能混用的术语

- **epitope**：antigenic site，即抗原表位。
- **epitype**：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009）。也就是说，表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别；可视为识别与同一抗原位点反应的、特异性略有不同的抗体所对应的区域。
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一位点对比整体结合

### affinity（结合亲和力）

指单个 epitope 与 paratope 之间的能量；也即在**单一位点**上，抗原表位与抗体 paratope 之间相互作用的强度。亲和力由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

### avidity（功能性亲和力）

指与抗原的总结合能。原文的表述是：“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009）。抗体的总结合强度在每一个结合位点上的量度即称为 avidity，又称 functional affinity（功能性亲和力）。

其影响因素有三个：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 免疫应答产生的抗体：多克隆、多同型

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

被动免疫（passive immunization）是直接给予中和抗体；主动免疫（active immunization）则是给予抗原，使机体产生保护性抗体。

疫苗以 sc（皮下注射）或 im（肌内注射）方式接种时，可以诱导产生多种抗体类型（isotype）。因此评估疫苗接种效果时，必须考虑是采用总抗体检测、isotype-specific assay，还是检测抗原清除。

口服/吸入途径免疫时，同样需要做出这一判断：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”（Crowther, 2009, p. 140）。

## 血清稀释会改变亲合力，从而改变抗原区分能力

血清的亲合力可视为血清中异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和。问题在于：“the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”（Crowther, 2009）。

一个具体情形是：血清中可能含有**少量**对某复杂抗原呈高亲和力的抗体，同时含有**大量**低亲和力抗体。在血清**未经大幅稀释**的免疫分析条件下，高、低亲和力抗体会竞争抗原位点，**高亲和力抗体优先反应**；而一旦稀释，高亲和力抗体的浓度被降低，最终只剩下低亲和力抗体。

原文对此的判断是：“Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).”（Crowther, 2009）

## 小结

这一章的落点可以归为两条。抗原侧，用表面积除以 20nm^2 得到的 Fab 结合位点数只是上限，因为它默认整个表面都有抗原性且结合达到最大；抗体侧，affinity 描述单一位点的结合强度并以 K_D 定义，avidity 描述整体结合强度并受亲和力、价数、以及抗体与抗原的结构排布三者共同影响。

需要留意的是 avidity 的非守恒性：血清是多克隆、多同型的异质混合物，其亲合力本身就是各群抗体的加权结果，稀释会改变这个组成，进而改变检测结果。因此当用免疫分析比较不同抗血清对不同抗原的差异活性时，稀释倍数不是可以随意设定的参数。至于在具体疫苗评价中究竟选择总抗体检测、isotype-specific 检测还是抗原清除检测，原书把这个问题留给实验设计者判断，未给出统一规则。