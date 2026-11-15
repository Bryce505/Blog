---
draft: true
reviewNotes:
  - "正文过短: 3596/13096=27% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,508 字符（原文 16,470，比例 21%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答"
date: 2026-11-15
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "导读：本文梳理 ELISA 所依赖的几项前置概念：抗原的分子大小如何决定可结合位点数、表位与表位型的界定、亲和力与亲合力各自的含义，以及免疫应答产生的多克隆抗体背景。这些概念的实用价值在于它们直接影响抗体用量估算、血清稀释方案与检测形式的选择。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

导读：本文梳理 ELISA 所依赖的几项前置概念：抗原的分子大小如何决定可结合位点数、表位与表位型的界定、亲和力与亲合力各自的含义，以及免疫应答产生的多克隆抗体背景。这些概念的实用价值在于它们直接影响抗体用量估算、血清稀释方案与检测形式的选择。

## 抗原性：分子大小与可饱和位点的估算

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有两个隐含前提：它基于「整个表面具有抗原性」和「分子最大结合」的事实，而前者很少成立。原文的表述是：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009, p. 127）。

在应用层面，这类计算可用于两种目的：“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”（Crowther, 2009, p. 127）。

## 表位、表位型与互补位

**epitope**：antigenic site，即抗原上被抗体识别的位点。

**Epitype**：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009, p. 128）。也就是说，表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如定义重叠或相互关联表位的 mAbs）所识别；它描述的是针对同一抗原位点、但特异性略有差异的抗体群所界定的区域。

**paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一位点与整体结合强度

### 亲和力（affinity / binding affinity）

- 单个 epitope 与 paratope 之间的能量；
- 亲和力是抗原表位与抗体互补位在单一结合位点上的相互作用强度；
- 亲和力由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

在抗体层面，同样的界定被重复给出：“The binding energy between an antibody molecule and an antigen determinant is termed affinity.”（Crowther, 2009, p. 136）

### 亲合力（avidity / functional affinity）

- 与抗原的整体结合能：“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009, p. 130）；
- 抗体在每个结合位点上总结合强度的量度称为 avidity，也称 functional affinity；
- 三个影响因素：1) 结合亲和力，2) 价数（valency），3) 抗体与抗原的结构排布。

在血清这种异质体系中，亲合力可视为各抗体亲和力的加总：“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”（Crowther, 2009, p. 137）。

## 稀释会改变血清的表观亲合力

一个容易忽略的事实是：“It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”（Crowther, 2009, p. 137）。

其机制可以用一个典型情形说明：某份血清中可能同时存在**少量**对特定复合抗原的高亲和力抗体和**大量**低亲和力抗体。在稀释倍数不大的免疫分析条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度被降到很低，体系中实际上只剩低亲和力抗体。

这一点在使用免疫分析、通过不同抗血清的差异活性来比较抗原时尤其重要：“The dilution of any serum can affect its ability to discriminate between antigens”，原因在于异质抗体群体的动力学差异，即各抗体分子的相对浓度与亲和力（Crowther, 2009, p. 137）。

## 免疫应答：多克隆来源与抗体同型

抗原刺激后产生的是多克隆抗体，且抗体类型并不限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

被动免疫（passive immunization）指直接注射中和抗体；主动免疫（active immunization）指接种抗原，由机体自行产生保护性抗体。

疫苗的常规注射方式为 sc（皮下注射）或 im（肌内注射）。这种方式可诱导产生多种抗体类型（isotype），因此必须事先确定：评估疫苗接种效果时，是采用总抗体检测、isotype-specific assay，还是检测抗原清除。

口服或吸入免疫则带来另一个问题：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”（Crowther, 2009, p. 140）。换言之，需要判断针对同型抗体（尤其是 IgA）的检测，是否比总抗体检测更能反映疫苗接种带来的获益。

## 小结

以上几组概念构成 ELISA 设计的共同底层：可结合位点数的估算提供了一个量级参考，但「整个表面均具抗原性」与「分子最大结合」这两个前提使结果只能视为上限；亲和力描述单一 epitope–paratope 的结合强度，而亲合力是多个位点、多个抗体群体的整体表现，二者的适用层次不能混用；一旦涉及血清这类异质样本，稀释本身就会改变表观亲合力，进而影响抗原区分能力；免疫途径与佐剂决定了抗体 isotype 的构成，也决定了检测应针对总抗体还是特定 isotype。

需要留意的是：不同抗体类型产生的时间顺序决定了取样时点的意义；口服或吸入免疫下选择哪一种检测形式，原文只提出了判断问题，并未给出普适答案。