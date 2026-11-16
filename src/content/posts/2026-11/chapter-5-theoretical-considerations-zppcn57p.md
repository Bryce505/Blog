---
draft: true
reviewNotes:
  - "正文过短: 3943/13045=30% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,943 字符（原文 16,405，比例 24%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与亲合力"
date: 2026-11-16
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理了 ELISA 反应体系设计背后的几个理论要点：抗原分子大小如何限制可结合位点的数量，epitope、epitype 与 paratope 如何界定，affinity 与 avidity 的区别与联系，以及抗体应答的异质性为什么会让稀释操作改变检测结果。全文按抗原、抗"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理了 ELISA 反应体系设计背后的几个理论要点：抗原分子大小如何限制可结合位点的数量，epitope、epitype 与 paratope 如何界定，affinity 与 avidity 的区别与联系，以及抗体应答的异质性为什么会让稀释操作改变检测结果。全文按抗原、抗体、免疫与检测形式三个层次依次展开。

## 抗原分子大小如何限制 Fab 结合位点数

分子越大，其复杂性也就越高。Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

### 估算成立的前提

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009)

也就是说，这种计算默认整个分子表面都具有抗原性（这在实际中很少成立），并假定分子处于最大结合状态。所以得到的只是上限值，不是实际可及位点数。

### 这个估算可以用来做什么

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009)

也就是用来估算饱和某一抗原所需的抗体量，或者测定抗体结合量随可用表面变化的曲线。

## epitope、epitype 与 paratope：三个容易混淆的术语

**epitope**（表位）即 antigenic site（抗原位点）。**paratope** 是抗体上结合抗原表位的部分。

**Epitype**（表位型）的界定更细：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009)

也就是说，表位型是抗原上的一个区域，由一组化学结构识别非常相近的抗体（例如定义重叠或相互关联表位的 mAb）共同界定；它可以看作这样一个区域：识别作用于同一抗原位点、特异性略有差异的抗体。

## Affinity 与 avidity：单点作用强度与总体结合强度

### Affinity

Affinity 指单个 epitope 与 paratope 之间的结合能，即抗原表位与抗体 paratope 在**单一结合位点**上相互作用的强度。它由**非共价相互作用**介导，包括氢键、静电作用、范德华力和疏水相互作用，并以**平衡解离常数（K<sub>D</sub>）**来定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009)

### Avidity

Avidity 又称 functional affinity（功能性亲和力），指与抗原结合的总体结合能。它是抗体在每个结合位点上结合强度的总和度量。

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009)

在血清层面，avidity 可以理解为：

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009)

### 影响 avidity 的三个因素

1）binding affinity；2）valency（价数）；3）抗体与抗原的结构排布。

## 稀释为什么会改变血清的 avidity

Avidity 不是血清的固有常数，它随稀释而变：

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009)

典型情形如下：血清中同时存在**少量高亲和力抗体**和**大量低亲和力抗体**。在稀释度不大时，两者竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度被稀释到很低，体系中实际上只剩低亲和力抗体。

> "Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)." (Crowther, 2009)

也就是说，如果要用不同抗血清的差异反应性来区分抗原，血清稀释度本身就是影响分辨能力的变量。

## 免疫方式如何决定该选哪种检测形式

应对抗原刺激产生的抗体是多克隆抗体，类型并不限于 IgG；各抗体类型的产生存在时间先后顺序：

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 被动免疫与主动免疫

被动免疫是直接注射中和抗体；主动免疫是给予抗原，由机体产生保护性抗体。

### 免疫途径与检测形式

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种途径可以诱导产生多种抗体类型（isotype）。因此评估疫苗接种效果时，必须先确定采用哪种检测：总抗体检测、isotype-specific assay，还是检测抗原清除。

口服或吸入免疫则涉及另一层判断：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)

即同型抗体（尤其是 IgA）的检测是否比总抗体检测更能反映疫苗接种带来的获益。

## 这些前提对方法设计的实际意义

把这些内容放在一起，可以看出几条边界条件：

- 由分子表面积推算的 Fab 结合位点数只是理论上限，因为“整个表面都具抗原性”和“分子最大结合”这两个前提在实际中很少同时成立。
- affinity 描述单一结合位点的强弱，以 K<sub>D</sub> 定义；avidity 描述总体结合强度，由 affinity、价数与结构排布三者共同决定，两者不可互换使用。
- 血清的 avidity 随稀释而变；用不同抗血清比较抗原时，稀释度会直接改变分辨能力，因此稀释方案需要固定并记录。
- 免疫途径决定了产生的 isotype 谱，检测形式（总抗体、isotype-specific 或抗原清除）必须先于实验设计确定。

笔记中没有展开的是：上述估算与判断在具体基质（如血清、细胞培养上清）中的偏差有多大，以及抗体类型随时间变化的定量规律——这两点需要回到原始文献与实测数据。