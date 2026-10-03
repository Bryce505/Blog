---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['135']"
  - "正文过短: 3469/13096=26% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,914 字符（原文 16,470，比例 24%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、亲和力与亲合力"
date: 2026-10-03
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 及其他免疫分析的可靠性，最终取决于几个基础变量：抗原上有多少可被识别的位点、抗体与之结合的强度如何度量、以及体系条件（尤其是稀释倍数与免疫途径）如何改变这些强度。本文按「抗原—抗体—体系」的顺序整理这些概念，并在最后一节归拢各自的适用边界。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 及其他免疫分析的可靠性，最终取决于几个基础变量：抗原上有多少可被识别的位点、抗体与之结合的强度如何度量、以及体系条件（尤其是稀释倍数与免疫途径）如何改变这些强度。本文按「抗原—抗体—体系」的顺序整理这些概念，并在最后一节归拢各自的适用边界。

## 抗原尺寸如何决定可结合位点的数量

分子的尺寸越大，其复杂性也越高。Fab 的结合面积约为 20 nm²，这一面积大致对应一个 epitope 的表面积。由此可以做一步推算：先算出分子的球形表面积，再除以 20，即可得到 Fab 结合位点数的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009, p. 127)

也就是说，这一推算建立在两个前提之上——整个表面都具有抗原性（这很少是真的），以及分子达到最大结合。

**应用**：据此可以计算饱和任一试剂所需的抗体量，也可以把抗体结合水平作为可用表面（available surface）的函数来测定 (Crowther, 2009, p. 127)。

## 表位相关的基本术语

- **epitope**：即 antigenic site（抗原位点）。
- **paratope**：抗体上结合抗原表位的部分。
- **Epitype**：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009, p. 128)

即：epitype 是抗原上由一组化学结构非常相似的抗体所识别的区域（例如定义重叠或相互关联表位的 mAb）。可以把 epitype 看作「与同一抗原位点反应、但特异性略有不同的抗体」所对应的区域。

## affinity 与 avidity：单一位点的结合能与总体结合强度

### affinity（结合亲和力）

笔记给出三层描述：

1. 单个 epitope 与 paratope 之间的能量；
2. 结合亲和力是抗原 epitope 与抗体 paratope 之间在单个结合位点（a singular binding site）上的相互作用强度；
3. Affinity 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

### avidity（亲合力 / 功能性亲和力）

- avidity 是与抗原之间的总体结合能；
- "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009, p. 130)——avidity 代表一个抗体群体结合到不同抗原位点时，所有单个 affinity 之和所给出的平均结合能；
- 抗体在每一个结合位点上总体结合强度的度量称为 avidity，avidity 也称为 functional affinity；
- 三个影响因素：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 抗血清稀释会同时改变 avidity 与抗原辨别力

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009, p. 136)

抗体分子与抗原决定簇之间的结合能称为亲和力。与之相对，

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009, p. 137)

即 avidity 可以看作血清中异质性抗体与各种抗原位点（epitope）之间所有不同亲和力的总和。

由此引出一个容易被忽略的问题：

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009, p. 137)

血清的 avidity 在稀释时可能发生变化，因为操作者可能把某些抗体群体稀释掉了。

一个具体例子：某份血清中可能同时含有针对某一复杂抗原的高亲和力抗体（少量）与低亲和力抗体（大量）(Crowther, 2009, p. 137)。在血清稀释倍数不大的免疫分析条件下，高亲和力与低亲和力抗体会竞争抗原位点，高亲和力抗体优先反应；而一经稀释，高亲和力抗体的浓度不断下降，最终只剩下低亲和力抗体。当操作者用免疫分析、以不同抗血清的差异活性来比较抗原时，这一问题尤为重要——由于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力。

## 免疫方式如何决定抗体类型与检测策略

抗体是应对抗原刺激而产生的，属于多克隆抗体，且抗体类型并不限于 IgG；各抗体类型产生的时间顺序见下图 (Crowther, 2009, p. 135)。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### passive immunization 与 active immunization

- passive immunization：直接注射中和抗体；
- active immunization：给予抗原，使机体产生保护性抗体。

### 免疫途径与检测项目的选择

疫苗的注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：究竟用总抗体检测、isotype-specific assay，还是检测抗原清除的检测来评估疫苗接种效果。

对于口服/吸入免疫：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)

做免疫分析的人必须决定，isotype-specific 抗体（尤其是 IgA）的检测是否能比总抗体检测更深入地反映疫苗接种的收益。

## 适用边界与遗留问题

把上述内容归拢，需要留意的边界有四条。

其一，「球形表面积 ÷ 20 nm²」得到的只是 Fab 结合位点数的最大数量，其前提是整个表面都具有抗原性、且分子达到最大结合，这两个前提在实际抗原上很少同时成立，因此该数值是上限而非实测值。

其二，affinity 与 avidity 描述的对象不同：前者是单个 epitope 与 paratope 在单一位点上的结合能，由 K_D 定义；后者是抗体群体结合到不同抗原位点时的总体（平均）结合能，还受 valency 与抗体—抗原结构排布的影响。两者不能互换使用。

其三，血清的 avidity 会随稀释而改变，因为稀释改变了异质性抗体群体的组成（相对浓度与各自亲和力），这会直接波及「以不同抗血清的差异活性比较抗原」这一类结论的稳健性。

其四，在疫苗免疫效果的评估上，笔记并未给出统一答案——是否需要用 isotype-specific（尤其 IgA）检测替代总抗体检测，取决于免疫途径与分析目的。