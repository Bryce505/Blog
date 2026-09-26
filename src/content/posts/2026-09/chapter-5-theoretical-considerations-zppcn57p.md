---
draft: true
reviewNotes:
  - "正文过短: 4258/13045=33% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,274 字符（原文 16,405，比例 26%）超出 9,023～15,585 字符的区间"
title: "ELISA 理论基础：从抗原性、亲和力/亲合力到免疫后抗体的产生"
date: 2026-09-26
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量表现，最终由三件事决定：抗原表面究竟能提供多少个可被识别的结合位点、抗体与单个表位之间的结合强度如何累加为整体结合强度、以及抗血清作为一个异质性抗体群体在不同稀释条件下会表现出什么行为。本文按抗原性考量、表位相关定义、亲和力与亲合力、免疫与接种后抗体产生这几条线"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量表现，最终由三件事决定：抗原表面究竟能提供多少个可被识别的结合位点、抗体与单个表位之间的结合强度如何累加为整体结合强度、以及抗血清作为一个异质性抗体群体在不同稀释条件下会表现出什么行为。本文按抗原性考量、表位相关定义、亲和力与亲合力、免疫与接种后抗体产生这几条线索，整理 Crowther 在 ELISA 理论基础一章中的核心概念，并交代每个概念成立的前提。

## 抗原性考量：分子大小与可结合位点数

分子越大，其复杂性也就越高。

### Fab 结合面积与最大位点数的估算

Fab 结合的面积大概是 20 nm²，也就是 epitope 的表面积。通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009)

也就是说，这样的计算基于两个假设：整个表面具有抗原性（很少是真实的），以及分子达到最大结合。

### 这一估算的用途

在承认上述前提的条件下，该估算可以用来 "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009)——即计算饱和某一试剂所需的抗体量，或测定抗体结合水平随可用表面变化的曲线。

## 表位、表位型与互补位

- **epitope**：antigenic site，即抗原决定簇。
- **Epitype**："An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009)。即表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别；表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：两个层级的结合强度

### affinity（结合亲和力）

1. the energy between a single epitope and paratope；
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
3. Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K<sub>D</sub>)。

### avidity（亲合力，functional affinity）

1. overall binding energy with an antigen；"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009)；
2. the measure of the total binding strength of an antibody at every binding site is termed avidity；avidity is also known as the functional affinity；
3. 三个影响因素：1) the binding affinity, 2) valency, 3) the structural arrangement of the antibody and antigen in question。

### 从抗体分子与异质性血清两个角度再看

"The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009)——抗体分子与抗原决定簇之间的结合能称为亲和力。

"Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009)——亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和。

## 稀释为什么会改变血清的表观亲合力

"It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009)。

一个具体的例子是：血清中可能含有针对某一复杂抗原的**少量高亲和力抗体**和**大量低亲和力抗体**。在血清**未大幅稀释**的免疫分析条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度不断下降，直到只剩下低亲和力抗体。当操作者用免疫分析**通过不同抗血清的差异活性来比较抗原**时，这类问题很重要。**任何血清的稀释都可能影响其区分抗原的能力**，原因在于异质性抗体群体的动力学——各抗体分子的相对浓度与亲和力。

## 免疫与接种后的抗体产生

应对抗原刺激所产生的抗体是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 被动免疫与主动免疫

- passive immunization：直接打中和抗体；
- active immunization：服用抗原，产生保护性抗体。

### 接种途径与检测策略的选择

疫苗注射方式为 sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：究竟是用总抗体检测、isotype-specific assay，还是检测抗原清除，来评估疫苗接种效果。

对于口服/吸入免疫，问题更为具体："The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)——免疫分析工作者必须判断，同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地反映疫苗接种的收益。

## 这些理论前提在方法设计中的位置

把上述内容收拢，可以看到几处对 ELISA 设计直接起约束作用的前提与边界：

- 用「球形表面积 ÷ 20」估算 Fab 结合位点数，只在两个假设同时成立时才有意义——整个表面具有抗原性、且分子达到最大结合；这两条在真实抗原上都很少成立，因此该估算给出的是上限量级，而非实测位点数。
- affinity 描述单一表位与互补位之间在单一结合位点上的相互作用，由非共价作用（氢键、静电作用、范德华力、疏水作用）介导，用平衡解离常数 K<sub>D</sub> 定义；avidity 描述抗体在全部结合位点上的总结合强度，受结合亲和力、价数以及抗体与抗原的结构排布三者共同影响。
- 血清的亲合力会随稀释而变化，因为稀释会改变高亲和力与低亲和力抗体群体的相对组成。当实验目的是用不同抗血清比较抗原时，稀释度本身就会影响血清区分抗原的能力，这一点必须在设计阶段就纳入考虑。
- 接种途径（sc/im 与口服/吸入）诱导的 isotype 谱不同，检测端因而需要在总抗体、isotype-specific 检测（尤其 IgA）与抗原清除之间做出选择。原文并未给出统一的取舍规则，而是把这一判断留给免疫分析工作者，依据具体疫苗的免疫机制决定。