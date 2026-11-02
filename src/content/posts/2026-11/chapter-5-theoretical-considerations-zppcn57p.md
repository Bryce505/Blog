---
draft: true
reviewNotes:
  - "正文过短: 3289/13096=25% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,654 字符（原文 16,470，比例 22%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答中的抗体类型"
date: 2026-11-02
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记梳理 ELISA 设计背后几个绕不开的理论前提：抗原分子大小如何决定可结合位点的上限，epitope、epitype、paratope 与 affinity、avidity 的定义边界在哪里，以及免疫应答产生的抗体类型如何反过来约束检测方案的选择。组织顺序是「抗原—抗体—"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记梳理 ELISA 设计背后几个绕不开的理论前提：抗原分子大小如何决定可结合位点的上限，epitope、epitype、paratope 与 affinity、avidity 的定义边界在哪里，以及免疫应答产生的抗体类型如何反过来约束检测方案的选择。组织顺序是「抗原—抗体—免疫应答—结果解释」，每一处定量估算都附上它的成立条件。

## 抗原性：分子大小决定可结合位点的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> [!warning] 这个数字是上限，不是实测值
> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009, p. 127）

这个上限值仍有实际用途：可以据此估算饱和某一试剂所需的抗体量，或测定抗体结合水平随可用表面的变化——“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”（Crowther, 2009, p. 127）。

## 表位、表位型与互补位：几个容易混用的定义

- **epitope**：antigenic site。
- **epitype**：指抗原上由一组化学结构非常相似的抗体所识别的区域，例如定义重叠或相互关联表位的 mAb；可以把它看作识别同一抗原位点、但特异性略有差异的抗体所对应的区域。“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009, p. 128）
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一结合位点与总体结合强度

### affinity：单一结合位点上的结合能

亲和力是单一 epitope 与 paratope 之间的能量，也就是抗原表位与抗体互补位在**单一结合位点**上的相互作用强度。“The binding energy between an antibody molecule and an antigen determinant is termed affinity.”（Crowther, 2009, p. 136）

亲和力由**非共价相互作用**介导，包括氢键、静电作用、范德华力和疏水作用，并由平衡解离常数（K_D）定义。

### avidity：功能亲和力

亲合力是与抗原的总结合能。它衡量的是抗体在每一个结合位点上的总体结合强度，也称 functional affinity。“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009, p. 130）；“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”（Crowther, 2009, p. 137）。

亲合力受三个因素影响：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 血清稀释会改变亲合力

“It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”（Crowther, 2009, p. 137）。

一个具体的例子：血清中可能同时存在**少量**对某复杂抗原亲和力高的抗体和**大量**低亲和力抗体。在血清**未大幅稀释**的免疫assay条件下，高亲和力与低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度被降到只剩低亲和力抗体。当操作者用免疫assay、以不同抗血清的差异活性来**比较抗原**时，这个问题尤其重要。由于异质性抗体群体的动态（各抗体分子的相对浓度与亲和力），**任何血清的稀释都可能影响其区分抗原的能力**。

## 免疫应答产生的抗体类型与检测方案

应对抗原刺激产生的是多克隆抗体，且抗体类型并不限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

被动免疫是直接注射中和抗体；主动免疫则是接种抗原、由机体产生保护性抗体。

疫苗经 sc（皮下）或 im（肌内）注射，可诱导产生多种抗体类型（isotype）。此时必须考虑：用总抗体检测、isotype-specific assay，还是检测抗原清除的assay来评估疫苗接种效果。

口服或吸入免疫则引出另一个选择：“The immunoassayist must decide whether an assay for **isotype-specific antibodies**, notably IgA, may provide deeper insight into the benefits of vaccination than an **assay for total antibody**”（Crowther, 2009, p. 140）。

## 这些前提的适用边界

上述内容构成了 ELISA 结果解释的几层约束：按表面积除以 20 得到的结合位点数只是理论最大值，其前提「整个表面都具有抗原性」和「分子达到最大结合」在真实体系中很少成立；affinity 描述单一结合位点，avidity 描述整个抗体群体与多个抗原位点的总结合，两者不可互相替代；血清的亲合力会随稀释而改变，因此用不同抗血清比较抗原时需要固定并交代稀释条件；免疫途径决定了产生的 isotype 谱，检测是测总抗体还是测特定 isotype（如 IgA），取决于想回答的是疫苗的哪一方面收益。笔记本身止于这些概念的定义与例证，未涉及具体的实验参数与判定标准。

## 依据与出处

1. 笔记：`Chapter-5-Theoretical-Considerations-ZPPCN57P` —— 引用要点：全文内容，包括抗原性估算、epitope/epitype/paratope 与 affinity/avidity 定义、血清稀释对亲合力的影响、免疫途径与 isotype 检测选择
2. 文献：Crowther, 2009（笔记中标注的引用，p. 127–140）—— 引用要点：表面抗原性计算的前提假设、饱和抗体量估算的用途、epitype 定义、affinity 与 avidity 的定义及亲合力三要素、血清稀释改变亲合力的例证、isotype-specific IgA 检测与总抗体检测的取舍