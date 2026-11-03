---
draft: true
reviewNotes:
  - "正文过短: 3654/13045=28% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,555 字符（原文 16,405，比例 22%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原特性、抗体亲和力与免疫应答"
date: 2026-11-03
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理 ELISA 反应体系背后的几个理论前提：抗原的分子大小如何限制可结合位点的数量，epitope、epitype、paratope 与 affinity、avidity 这两组术语如何界定，以及免疫方式与抗体类型对检测设计的约束。全篇按「抗原—抗体—免疫应答」的顺序展"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理 ELISA 反应体系背后的几个理论前提：抗原的分子大小如何限制可结合位点的数量，epitope、epitype、paratope 与 affinity、avidity 这两组术语如何界定，以及免疫方式与抗体类型对检测设计的约束。全篇按「抗原—抗体—免疫应答」的顺序展开，关注点不在于操作步骤，而在于这些概念成立的前提，以及前提不成立时结论会如何偏移。

## 抗原分子的大小如何限制可结合位点的数量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有明确的前提：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）

即该计算假设整个表面都具有抗原性（这一假设很少成立），且分子达到最大结合。因此得到的只是上限值，而非实际可及的表位数。

它的实际用途在反方向：可以据此计算饱和某一试剂所需的抗体量，或测定抗体结合量随可用表面的变化（Crowther, 2009, p. 127）。

## epitope、epitype 与 paratope：界面上的三个术语

epitope 即 antigenic site。

epitype（表位型）的界定是：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"

也就是说，表位型是抗原上由一组所识别的化学结构非常接近的抗体（例如识别重叠或相互关联表位的 mAb）所界定的区域；它可以被看作这样一个区域：识别同一抗原位点、特异性略有差异的抗体都归于此。

paratope 则是抗体上结合抗原表位的部分。

## affinity 与 avidity：从单一结合位点到总体结合强度

### affinity：单一结合位点的强度

原文给出三条彼此补充的界定：

1. 单个 epitope 与 paratope 之间的能量；
2. 在**单一结合位点**上，抗原表位与抗体 paratope 之间相互作用的强度；
3. 由**非共价相互作用**介导，包括氢键、静电键、范德华力与疏水作用，并由平衡解离常数（K<sub>D</sub>）定义。

换一种表述："The binding energy between an antibody molecule and an antigen determinant is termed affinity."——抗体分子与抗原决定簇之间的结合能即亲和力。

### avidity：总体结合强度（functional affinity）

avidity 是与抗原的总结合能，在血清层面可以这样理解：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"

抗体在每一个结合位点上的总结合强度的量度称为 avidity，也称 functional affinity。它受三个因素影响：1）the binding affinity，2）valency，3）抗体与抗原的结构排布。

在异质性抗体的语境下，这一点更明确："Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"——亲和力可以看作血清中异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

## 稀释为何会改变血清的 avidity

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"

一个典型情形是：血清中同时含有**少量对某复杂抗原高亲和力**的抗体和**大量低亲和力**抗体。在血清**未大幅稀释**的免疫分析条件下，高亲和力与低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度会被稀释到很低，最后只剩低亲和力抗体。

这类问题在用免疫分析比较抗原与不同抗血清的差异活性时尤其重要：由于异质性抗体群体的动态（各抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力。

## 免疫方式与抗体类型对检测设计的约束

抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

两条路径需要区分：passive immunization 是直接注射中和抗体；active immunization 是接种抗原，由机体产生保护性抗体。

疫苗的 sc（皮下）或 im（肌内）注射方式可以诱导产生多种抗体类型（isotype）；因此必须考虑：评估疫苗接种效果时，究竟采用总抗体检测、isotype-specific assay，还是检测抗原清除。

口服／吸入免疫路径下，问题更集中于 isotype 层面：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"

即同型抗体（尤其是 IgA）的检测是否比总抗体的检测更能深入反映疫苗接种的获益，需要由免疫分析的设计者自行判断。

## 这些前提在方法设计中的位置

把上述内容归拢起来，可以看到几条互相牵连的边界条件。

按分子表面积除以 20nm^2 估算 Fab 结合位点数，得到的是上限，因为计算默认整个表面都具有抗原性、且分子达到最大结合，这两个条件在真实抗原上很少同时满足。affinity 描述的是单一 epitope–paratope 界面的强度，由非共价作用与 K<sub>D</sub> 刻画；avidity 描述的是总体结合强度，受 binding affinity、valency 与结构排布三者共同决定。在血清这类异质性抗体体系中，avidity 是各抗体与各表位亲和力的总和，因而会随稀释而漂移——稀释改变了参与竞争的抗体群体构成，进而影响检测区分抗原的能力。免疫方式（passive 或 active、sc/im 或口服／吸入）决定了产生的 isotype 谱，也就决定了读出方式该选总抗体、isotype-specific 还是抗原清除。

这几条都是检测设计时需要预先确认的前提，而非可以事后校正的偏差来源。笔记本身止于理论层面，未涉及具体的实验操作参数与判定标准。