---
draft: true
reviewNotes:
  - "正文过短: 4045/13045=31% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,086 字符（原文 16,405，比例 25%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与 avidity 的界定"
date: 2026-10-19
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本文整理 ELISA 赖以成立的理论前提：抗原的分子大小如何决定可结合位点数的上限、epitope/epitype/paratope 这组术语如何界定、亲和力（affinity）与 avidity 为何不能混用，以及抗体产生方式与免疫途径如何反过来约束检测形式的选择。整体按「抗原"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本文整理 ELISA 赖以成立的理论前提：抗原的分子大小如何决定可结合位点数的上限、epitope/epitype/paratope 这组术语如何界定、亲和力（affinity）与 avidity 为何不能混用，以及抗体产生方式与免疫途径如何反过来约束检测形式的选择。整体按「抗原—抗体—结合强度—免疫应答」的次序组织。

## 抗原性考量：分子大小决定复杂度与位点数上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有明确的成立前提：

> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”

即该计算假定整个表面均具抗原性（很少是真实的）且分子达到最大结合。因此得到的只是一个上限，而非实测的结合位点数。

在实际使用中，这类计算可用于两件事：

> “calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”

也就是推算饱和某一试剂所需的抗体量，或测定抗体结合水平随可用表面的变化。

## 术语界定：epitope、epitype 与 paratope

epitope 即抗原位点（antigenic site）；paratope 指抗体上结合抗原表位的部分。epitype 则比 epitope 更细一层：

> “An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”

译文：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如定义重叠或相互关联表位的 mAb）识别；它可以被看作识别与同一抗原位点反应的、特异性略有差别的抗体的区域。

## 亲和力与 avidity：单一位点强度与总体结合强度

### affinity

亲和力描述的是单一结合位点层面的作用强度，可从三个角度表述：

1. 单一 epitope 与 paratope 之间的能量；
2. 抗原表位与抗体 paratope 在**单一结合位点上**的相互作用强度；
3. 由**非共价相互作用**介导，包括氢键、静电作用、范德华力和疏水相互作用，并以平衡解离常数（**K<sub>D</sub>**）定义。

> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.”

即抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity

avidity 即功能亲和力（functional affinity），描述的是总体结合强度：

1. 与抗原的总结合能；
2. 抗体在每一个结合位点上总结合强度的度量；
3. 三个影响因素：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question.

> “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”

> “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”

### 稀释会改变血清的 avidity

> “It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”

原因在于血清中高亲和力与低亲和力抗体群体的相对比例会随稀释而改变：

> “As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. … The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).”

这一点在用免疫测定比较不同抗血清与抗原的差异性反应时尤为要紧：稀释本身就会改变血清区分抗原的能力。

## 抗体产生与免疫途径：检测形式选择的前提

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 被动免疫与主动免疫

被动免疫是直接给予中和抗体；主动免疫则是给予抗原，由机体自行产生保护性抗体。

### 接种途径与 isotype

以 sc（皮下注射）或 im（肌内注射）方式接种，可诱导产生多种抗体类型（isotype）。因此必须考虑：究竟是用总抗体检测、isotype-specific assay，还是检测抗原清除，来评估疫苗接种效果。

口服或吸入免疫则多一层判断：

> “The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”

即同型抗体（尤其是 IgA）的检测是否比总抗体检测更能反映疫苗接种带来的益处。

## 收束：这些前提如何约束检测设计

几个结论可以归拢到一起。表位数量与所需抗体量的估算给出的是理论上限，前提是整个表面具抗原性且结合达到饱和，实际体系很少同时满足，因此不能把估算值当作实测值使用。affinity 描述单一结合位点的强度、由 K<sub>D</sub> 定义，avidity 则是多位点、多克隆背景下的总和与平均值，两者在多价抗体与复杂抗原体系中不可互换。血清的 avidity 会随稀释而改变，涉及用不同抗血清比较抗原差异性的实验时，稀释方案本身就是变量。免疫途径决定产生的 isotype 组成，进而决定评估手段应选总抗体检测、isotype-specific assay 还是抗原清除检测。至于这些理论前提在具体定量体系中的边界，则需要在方法开发阶段逐项确认。