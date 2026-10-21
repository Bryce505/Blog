---
draft: true
reviewNotes:
  - "正文过短: 3069/13096=23% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,838 字符（原文 16,470，比例 17%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-10-21
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "导读：本文梳理 ELISA 这类免疫检测在方法设计前必须交代清楚的几个理论前提——抗原尺寸与可结合位点数、表位相关术语的界定、亲和力与亲合力的区别，以及抗血清固有的异质性如何影响检测结果。内容按\"抗原—抗体—免疫应答—对检测的约束\"这一顺序组织。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

导读：本文梳理 ELISA 这类免疫检测在方法设计前必须交代清楚的几个理论前提——抗原尺寸与可结合位点数、表位相关术语的界定、亲和力与亲合力的区别，以及抗血清固有的异质性如何影响检测结果。内容按"抗原—抗体—免疫应答—对检测的约束"这一顺序组织。

## 分子尺寸如何决定可结合的 Fab 位点数

分子越大，其复杂性也就越高。Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

这个估算有两处前提：一是假定整个分子表面都具有抗原性，二是假定分子达到最大结合。Crowther 明确指出前者"rarely true"——"Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）。因此该数值只能视为上限而非实际表位数。

其用途在于反推实验条件：据此可以计算饱和某一试剂所需的抗体量，或把抗体结合量作为可用表面积的函数来测定（Crowther, 2009）。

## 表位、表位型与互补位：三个需要分清的术语

- **epitope**：即 antigenic site，抗原上被抗体识别的位点。
- **epitype（表位型）**：抗原上的一个区域，由一组化学结构非常相似的抗体（例如定义重叠或相互关联表位的 mAb）所识别；可视为识别同一抗原位点、但特异性略有差异的抗体所对应的区域（Crowther, 2009）。
- **paratope**：抗体上结合抗原表位的部分。

epitope 与 epitype 的差别在于观察角度：前者是抗原侧的位点，后者是在一组密切相关抗体之间划出的、彼此重叠的识别区域。

## 亲和力与亲合力：单点结合强度与整体结合强度

**affinity（binding affinity）** 指单一的 epitope 与 paratope 之间的结合能，即抗原表位与抗体互补位在单个结合位点上的相互作用强度（Crowther, 2009）。它由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡解离常数（K<sub>D</sub>）来定义。

**avidity（functional affinity，亲合力）** 指与抗原的整体结合能。它是抗体在每一个结合位点上总结合强度的度量，又称 functional affinity。Crowther 对它的界定是："The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"；就血清而言，"Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009）。

avidity 受三个因素影响：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 稀释会改变血清的表观亲合力

由于血清中的抗体是异质的，avidity 并不是一个固定属性——它在稀释过程中可能发生变化，因为操作者可能把某些抗体群体稀释掉了（Crowther, 2009）。

一个典型情形是：血清中同时存在少量对某复杂抗原高亲和力的抗体和大量低亲和力抗体。在血清未被大幅稀释的免疫检测条件下，高亲和力与低亲和力抗体会竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度下降到一定程度后，体系中只剩下低亲和力抗体。当操作者用免疫检测、以不同抗血清的差异活性来比较抗原时，这一问题尤为关键——任何血清的稀释都可能影响其区分抗原的能力，原因就在于异质抗体群体的动力学，即各抗体分子的相对浓度与亲和力（Crowther, 2009）。

## 免疫方式决定该测总抗体还是特定 isotype

被动免疫（passive immunization）是直接注射中和抗体；主动免疫（active immunization）则是给予抗原、由机体产生保护性抗体。

疫苗经 sc（皮下）或 im（肌内）途径注射，可诱导产生多种抗体类型（isotype）。因此在评估疫苗接种效果时，必须先决定采用总抗体检测、isotype-specific assay，还是检测抗原清除。

口服或吸入免疫则引出另一个选择：免疫检测的设计者必须判断，针对特定 isotype（尤其是 IgA）的检测是否比总抗体检测更能反映疫苗接种的收益——"The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）。

机体受抗原刺激后产生的抗体类型随时间变化的顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 这些理论前提对方法设计的约束

把上述概念归拢起来，可以落到三条对检测设计的约束上：

其一，由分子表面积推算出的 Fab 结合位点数只是理论上限，因为它同时依赖"整个表面均具抗原性"和"结合达到饱和"两个假设，实际设计包被量与抗体浓度时不能直接照搬该数值。

其二，avidity 是异质抗体群体的加权结果，会随稀释而改变。凡是用不同抗血清比较抗原、或依赖单一稀释度下结论的实验，都需要先确认该稀释度下占主导的是哪一部分抗体群体。

其三，免疫途径与抗原给予方式决定了抗体 isotype 的构成，进而决定了检测应该测总抗体还是测特定 isotype。这一选择在疫苗评价类检测中先于方法学优化，属于必须在实验设计阶段确定的前提。