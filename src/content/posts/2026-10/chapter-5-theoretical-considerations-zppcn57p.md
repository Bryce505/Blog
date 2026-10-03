---
draft: true
reviewNotes:
  - "正文过短: 2740/13045=21% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,996 字符（原文 16,405，比例 18%）超出 9,023～15,585 字符的区间"
title: "ELISA 理论基础：抗原表位、抗体亲和力与 avidity 的辨析"
date: 2026-10-03
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理了 ELISA 理论章节的几组基础概念：抗原的尺寸如何决定可结合位点数量的上限、epitope 与 epitype 的区别、亲和力（affinity）与 avidity 的分野，以及免疫途径如何影响所产生抗体的类型。整理的落点放在几个容易被混用的概念上，以及它们在免疫分析"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理了 ELISA 理论章节的几组基础概念：抗原的尺寸如何决定可结合位点数量的上限、epitope 与 epitype 的区别、亲和力（affinity）与 avidity 的分野，以及免疫途径如何影响所产生抗体的类型。整理的落点放在几个容易被混用的概念上，以及它们在免疫分析方法设计中的实际含义。

## 抗原尺寸决定可结合位点数量的上限

分子越大，其复杂性也就越高。Fab 结合的面积大约是 20 nm²，这大致就是一个 epitope 的表面积。据此可以估算一个抗原分子上 Fab 结合位点数量的上限：先计算分子的球形表面积，再把表面积除以 20。

这个估算有两个明确的前提——整个表面都具有抗原性，以及分子被最大程度地结合。原文对这一点的表述是："Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）。

因此这个数字的意义不在于预测真实的表位数，而在于两个具体用途：计算饱和某一抗原所需的抗体量，或测定抗体结合水平随可用表面积的变化（Crowther, 2009）。

## 表位（epitope）与表位型（epitype）

epitope 即 antigenic site，是抗原上被抗体识别的位点。

epitype 则是抗原上的一个区域，由一组化学结构非常相似的抗体所识别——例如定义重叠或相互关联表位的 mAb。也可以把 epitype 理解为：识别同一抗原位点、但特异性略有差异的那些抗体所对应的区域（Crowther, 2009）。

两者的差别在于描述对象：epitope 对应的是单个抗体–抗原识别所针对的位点，epitype 对应的是一组密切相关抗体共同覆盖的区域，其边界取决于这组抗体之间特异性的细微差异。

## paratope 与亲和力：单一结合位点的结合能

paratope 是抗体上结合抗原表位的部分。

亲和力（affinity，结合亲和力）有三层含义需要注意：

- 它是单个 epitope 与 paratope 之间的能量；
- 更准确地说，它是在单一结合位点上，抗原表位与抗体 paratope 之间相互作用的强度；
- 这一作用由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

抗体分子与抗原决定簇之间的结合能称为亲和力（Crowther, 2009）。

## avidity：总体结合强度与 functional affinity

avidity 与亲和力不在同一个层面上。

- avidity 是与抗原的总结合能，也称为 functional affinity（功能性亲和力）；
- "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"，即 avidity 代表一个抗体群体与不同抗原位点结合时，所有单个亲和力之和所给出的平均结合能（Crowther, 2009）；
- 在血清这类体系中，avidity 可以看作是血清中包含的异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和（Crowther, 2009）；
- 抗体在每一个结合位点上的总结合强度称为 avidity，也就是 functional affinity。

avidity 受三个因素影响：1）结合亲和力（binding affinity）；2）价数（valency）；3）抗体与抗原的结构排布。

## 稀释会改变血清的 avidity

一个血清样本中可以同时存在少量针对某一复杂抗原的高亲和力抗体和大量低亲和力抗体。在血清未被大幅稀释的免疫分析条件下，高、低亲和力抗体会竞争抗原位点，高亲和力抗体优先反应；而一旦稀释，高亲和力抗体的浓度会先被降低，最终只剩下低亲和力抗体（Crowther, 2009）。

因此必须认识到，血清的 avidity 可能在稀释过程中发生变化，因为操作者实际上是在把某些抗体亚群稀释出去（Crowther, 2009）。当用免疫分析、通过不同抗血清对同一组抗原的差异活性来比较抗原时，这一问题尤其重要：任何血清的稀释都可能影响其区分不同抗原的能力，原因在于异质性抗体群体的动力学，即各个抗体分子的相对浓度与亲和力（Crowther, 2009）。

## 免疫途径与抗体 isotype：检测对象的选择

对抗原刺激的应答产物是多克隆抗体，且抗体类型并不仅限于 IgG；各类抗体产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

passive immunization 是直接给予中和抗体；active immunization 则是给予抗原，使机体产生保护性抗体。

疫苗常见的接种方式是 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体 isotype。因此在评估疫苗接种效果时，必须考虑究竟采用总抗体检测、isotype-specific assay，还是检测抗原清除。

口服或吸入免疫的情形下，问题更具体："The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）——即免疫分析人员必须决定，同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地揭示疫苗接种的益处。

## 收尾：这套概念框架的适用边界

把上述内容归拢起来，可以落到四条判断上：

- 用球形表面积除以 20 得到的是 Fab 结合位点数量的上限，其两个前提——整个表面均具抗原性、分子被最大程度结合——在真实体系中很少成立，因此它只适合用于估算饱和抗体用量或结合水平随表面积的变化，不能当作真实表位数。
- 亲和力是单一结合位点的属性，avidity 是群体或多价层面的属性，由亲和力、价数与结构排布共同决定；用单个 K_D 无法描述多克隆血清的行为。
- 血清稀释会改变抗体群体的组成，从而同时改变 avidity 和血清区分不同抗原的能力。用不同抗血清比较抗原的差异反应时，稀释方案本身就是变量。
- 评估免疫效果之前，先要确定检测对象是总抗体、特定 isotype 还是抗原清除，这决定了 assay 的设计方向。

以上是这一章在概念层面给出的边界；具体抗原体系中这些参数如何取值，仍需回到实验数据。