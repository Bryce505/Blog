---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['135']"
  - "正文过短: 4506/13045=35% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,561 字符（原文 16,405，比例 28%）超出 9,023～15,585 字符的区间"
title: "ELISA 理论考量：抗原性、抗体亲和力与亲合力"
date: 2026-09-16
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的信号最终由抗原与抗体之间的相互作用决定，因此理解抗原的抗原性、抗体的结合强度以及抗体群的组成，是判断一个检测体系能测什么、测不准什么的前提。这篇笔记按 Crowther《The ELISA Guidebook》第 5 章的脉络整理：从抗原大小推算可能的 Fab 结合"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的信号最终由抗原与抗体之间的相互作用决定，因此理解抗原的抗原性、抗体的结合强度以及抗体群的组成，是判断一个检测体系能测什么、测不准什么的前提。这篇笔记按 Crowther《The ELISA Guidebook》第 5 章的脉络整理：从抗原大小推算可能的 Fab 结合位点数开始，界定表位相关术语，区分 affinity 与 avidity，再落到抗体应答产生的抗体类型以及血清稀释对亲合力的影响。

## 抗原大小如何限定可能的 Fab 结合位点数

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一算法给出的是上限而非实测值。Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally（Crowther, 2009, p. 127）——即它假设整个表面都具有抗原性，且分子以最大方式结合，而这两个条件很少同时成立。

### 这类估算的用途

它的价值在于反向估算实验用量与结合容量：可以 calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface（Crowther, 2009, p. 127），也就是估算饱和某一抗原所需的抗体量，或测定抗体结合量随可用表面变化的曲线。

## 表位、表位型与互补位

三个术语描述的是结合界面的两侧与识别关系：

- **epitope**（抗原决定簇）：即 antigenic site，抗原上被抗体识别的位点。
- **epitype**（表位型）：An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site（Crowther, 2009, p. 128）。也就是说，表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别；它可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。
- **paratope**（互补位）：抗体上结合抗原表位的部分。

epitope 与 paratope 构成结合对，而 epitype 描述的是这一结合对在抗体群层面上的重叠程度——用单克隆抗体定义表位时，这层区分尤其重要。

## 亲和力与亲合力：两个尺度的结合强度

### affinity（亲和力）

亲和力描述单一结合位点上的相互作用强度，有三层表述：

1. the energy between a single epitope and paratope；
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope **at a singular binding site**；
3. Affinity is mediated by **non-covalent interactions** that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium **dissociation constant (K_D)**。

落到一句话：抗体分子与抗原决定簇之间的结合能称为亲和力（Crowther, 2009, p. 136）。

### avidity（亲合力）

亲合力描述的是总体结合能，又称 functional affinity：

- The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites（Crowther, 2009, p. 130）。
- Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)（Crowther, 2009, p. 137）。即亲合力可以看作血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。
- 抗体在每个结合位点上的总结合强度称为 avidity，即 functional affinity。

亲合力受**三个因素**影响：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。因此 affinity 是分子层面的参数，avidity 是抗体群与多表位抗原共同决定的参数，两者不能互相替代。

## 抗原刺激下的抗体产生与抗体类型

机体应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\
（Crowther, 2009, p. 135）

### 免疫方式决定要测什么

- **passive immunization**（被动免疫）：直接打中和抗体。
- **active immunization**（主动免疫）：服用抗原，产生保护性抗体。

疫苗注射方式为 sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型—isotype；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫则另有一层判断：The immunoassayist must decide whether an assay for **isotype-specific antibodies**, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for **total antibody**（Crowther, 2009, p. 140）。也就是说，需要先回答"测 IgA 等同型特异性抗体，是否比测总抗体更能反映疫苗接种的收益"，再决定检测形式。

## 血清稀释为什么会改变亲合力

It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies（Crowther, 2009, p. 137）。稀释改变的不只是浓度，还可能改变留下来的是哪一群抗体。

一个典型情形是：血清中同时存在 a low quantity of antibodies showing high affinity 针对某一复杂抗原，以及 a high quantity of low-affinity antibody。在血清 not diluted greatly 的免疫分析条件下，高、低亲和力抗体竞争抗原位点，the high-affinity antibodies would react preferentially；而一旦稀释，高亲和力抗体的浓度被降低，until we would be left only with low-affinity antibodies。

这类问题在使用免疫分析 compare antigens by their differential activity with different antisera 时尤其重要，因为 The dilution of any serum can affect its ability to discriminate between antigens——原因在于异质性抗体群的动力学，即各抗体分子的相对浓度与亲和力（Crowther, 2009, p. 137）。

## 这套理论框架的适用边界

把上述内容放在一起，可以得到几条对实验设计的直接约束：

- 由表面积除以 20nm^2 得到的 Fab 结合位点数只是理论上限，它建立在"整个表面均具抗原性"和"分子最大结合"两个很少同时成立的假设上，因此不能直接当作实测结合容量使用。
- affinity 描述单一结合位点，avidity 描述抗体群与多个抗原位点之间的总体结合。两者在稀释、抗体群组成变化时会脱钩：稀释可能优先移除高亲和力抗体群，从而改变血清对抗原的分辨能力。用不同抗血清比较抗原差异活性时，稀释倍数本身就是一个需要固定并说明的变量。
- 检测目标需要在设计阶段就确定：测总抗体、测 isotype-specific 抗体（尤其 IgA），还是测抗原清除，取决于免疫途径（sc/im 与口服/吸入所诱导的抗体类型不同）以及要回答的问题是"是否有抗体"还是"疫苗是否带来收益"。
- 抗体类型不只限于 IgG，其产生有时间顺序，取样时间点因此会影响所测到的抗体谱。