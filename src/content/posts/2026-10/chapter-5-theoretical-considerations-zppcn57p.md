---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['135']"
  - "正文过短: 3252/13096=25% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗体应答产生的是多克隆抗体，且 isotype 有先后顺序']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,098 字符（原文 16,470，比例 19%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论前提：抗原表位、抗体亲和力/亲合力与免疫应答的抗体类型"
date: 2026-10-11
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量表现最终受制于抗原与抗体两侧的物理化学前提：抗原有几个可被识别的位点、抗体的结合强度如何定义与度量、抗血清本身又是一个怎样的混合物。本文按抗原—抗体—免疫应答的顺序整理这些前提，并说明它们对检测设计与结果解读的约束。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量表现最终受制于抗原与抗体两侧的物理化学前提：抗原有几个可被识别的位点、抗体的结合强度如何定义与度量、抗血清本身又是一个怎样的混合物。本文按抗原—抗体—免疫应答的顺序整理这些前提，并说明它们对检测设计与结果解读的约束。

## 抗原分子大小决定了可结合位点数的上限

分子越大，其复杂性也就越高。Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算建立在两个前提之上——整个表面都具有抗原性，以及分子达到最大结合：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009, p. 127)

这两个前提在真实体系中很少同时成立，因此算出的数值只能作为位点数的上限，而非实际可结合的位点数。它的用途在于估算饱和某一试剂所需投入的抗体量，或者测定抗体结合水平随可用表面的变化：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009, p. 127)

## 表位相关术语的界定

- **epitope**：即 antigenic site，抗原表位。
- **epitype**：抗原上由一组化学结构非常相似的抗体所识别的区域，例如定义重叠或相互关联表位的 mAb；也可以把它视为「识别同一抗原位点、但特异性略有差异的抗体」所对应的区域 (Crowther, 2009, p. 128)。
- **paratope**：抗体上结合抗原表位的部分。

这三个术语分别落在抗原侧、抗原侧的抗体群体、抗体侧，混用会直接影响对结合模型的描述。

## affinity 与 avidity：单一位点的结合能与整体的结合能

### affinity：单一结合位点的结合能

- 指单个 epitope 与 paratope 之间的能量；
- 是抗原 epitope 与抗体 paratope 在单一结合位点上的相互作用强度；
- 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡解离常数（K_D）定义。

抗体分子与抗原决定簇之间的结合能称为亲和力 (Crowther, 2009, p. 136)。

### avidity：功能性亲和力

- 指与抗原的整体结合能；
- 是抗体在每个结合位点上总结合强度的度量，也称 functional affinity；
- 影响因素有三个：结合亲和力、价数（valency），以及抗体与抗原的结构排布。

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009, p. 130)

对血清而言，avidity 可以看作是血清中异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和 (Crowther, 2009, p. 137)。

## 抗体应答产生的是多克隆抗体，且 isotype 有先后顺序

应对抗原刺激所产生的是多克隆抗体，抗体类型并不仅限于 IgG；各抗体类型产生的时间顺序见下图 (Crowther, 2009, p. 135)。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 稀释会改变血清的表观 avidity

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009, p. 137)

举例来说，一份血清中可能同时存在少量针对某个复杂抗原的高亲和力抗体，以及大量低亲和力抗体。在不做大幅稀释的免疫测定条件下，高、低亲和力抗体会竞争抗原位点，而高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度被降低，最后只剩下低亲和力抗体。

当操作者用免疫测定通过不同抗血清的差异活性来比较抗原时，这类问题很重要。任何血清的稀释都可能影响其区分抗原的能力，原因在于异质性抗体群体的动力学，即各抗体分子的相对浓度与亲和力 (Crowther, 2009, p. 137)。

## 免疫途径决定了应该检测什么

- passive immunization：直接注射中和抗体；
- active immunization：给予抗原，由机体产生保护性抗体。

疫苗的注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑是使用总抗体检测、isotype-specific assay，还是检测抗原清除来评估疫苗接种效果。

口服或吸入免疫时，检测目标的选择更为关键：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)

## 这些前提对检测设计与结果解读的约束

把上述内容归拢起来，可以看到三层约束。第一层是几何层面：由分子表面积极算出的结合位点数是一个偏乐观的上限，实际可结合位点数取决于表面有多少区域真正具有抗原性、以及结合是否达到饱和。第二层是结合强度层面：affinity 描述单一表位—paratope 位点，avidity 描述抗体群体与抗原上多个位点的总和，二者不可互换使用；判断一个体系的结合行为时，还必须同时考虑价数与抗体、抗原的结构排布。第三层是样品层面：血清或抗血清是异质性抗体群体，稀释会改变其中各群体的相对占比，从而改变表观 avidity 和区分不同抗原的能力。

由此得到的操作边界是：用「球形表面积 ÷ 20」只能做需求量的粗估，实测仍需通过饱和实验确定；在比较不同抗血清或不同抗原时，必须控制稀释方案，否则测到的差异可能来自抗体群体组成的变化而非抗原本身；而疫苗或免疫效果的评估，需要先回答测总抗体、测特定 isotype（如 IgA）还是测抗原清除。本笔记讨论的范围是抗原与抗体一侧的物理化学前提，ELISA 中酶反应动力学与浓度—反应关系不在其中。