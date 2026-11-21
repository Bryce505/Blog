---
draft: true
reviewNotes:
  - "正文过短: 4605/13045=35% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,601 字符（原文 16,405，比例 28%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、亲和力与免疫应答如何决定检测设计"
date: 2026-11-21
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的可靠性并不只取决于操作步骤，它首先取决于对抗原结构、抗体结合性质以及免疫应答异质性的理解。这篇笔记沿着「抗原—抗体—免疫应答」的顺序梳理这些理论前提：先讨论分子大小与表位数量估算及其成立条件，再厘清 epitope/epitype/paratope 与 affini"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的可靠性并不只取决于操作步骤，它首先取决于对抗原结构、抗体结合性质以及免疫应答异质性的理解。这篇笔记沿着「抗原—抗体—免疫应答」的顺序梳理这些理论前提：先讨论分子大小与表位数量估算及其成立条件，再厘清 epitope/epitype/paratope 与 affinity/avidity 这两组容易混淆的概念，最后落到血清稀释效应与疫苗接种效果评估这两个实际操作中容易出问题的环节。

## 抗原性考量：分子大小与表位数量估算

分子越大，其复杂性也就越高。抗原性的复杂程度直接决定了一个抗原分子上可供抗体识别的位点数量，也就决定了一个检测体系需要多大的抗体投入才能达到饱和。

在数量层面，常用的估算方式是：Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这种估算有明确的前提限制，不能当作真实表位数来用：

> [!warning] 估算成立的两个假设
> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）
>
> 这样的计算基于整个表面具有抗原性（很少是真实的）和分子最大结合这两个事实。

即便如此，这个量级估算在方法学上仍有实际用途：据此可以 calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface（Crowther, 2009, p. 127）——即用于推算饱和某一试剂所需的抗体量，或把抗体结合水平作为可用表面的函数来测定。前者用于确定包被与检测抗体的工作浓度上限，后者用于评估固相表面的结合容量。

## 表位与结合位点的术语：epitope、epitype 与 paratope

三个术语分别指向抗原侧、抗原侧的细分区域和抗体侧：

- **epitope**：antigenic site，即抗原上被抗体识别的位点。
- **epitype**：epitope 之下的细分概念，指由一组化学结构识别上高度相关的抗体所界定的抗原区域。
- **paratope**：抗体上结合抗原表位的部分。

epitype 的定义需要完整理解，它描述的是抗体特异性之间的细微差异落在抗原上的位置：

> [!quote] epitype（Crowther, 2009, p. 128）
> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"
>
> 表位型是抗原上的一个区域，由一组化学结构识别非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

这一区分解释了为什么针对同一 antigenic site 的不同 mAb 可以表现出不同的结合行为：它们识别的 epitype 并不完全相同。

## affinity 与 avidity：从单个结合位点到总体结合强度

这两个概念在中文里都常被译作「亲和力」，但在 ELISA 的数据解释中必须分开。

**affinity（binding affinity）** 描述的是单个结合位点层面的结合能，可以从三个角度表述：

1. 单个 epitope 与 paratope 之间的能量；
2. 在**单一结合位点**上，抗原表位与抗体 paratope 之间相互作用的强度；
3. 由**非共价相互作用**介导，包括氢键、静电作用、范德华力和疏水作用，并由**平衡解离常数（K<sub>D</sub>）**定义。

> [!quote] affinity（Crowther, 2009, p. 136）
> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."
>
> 抗体分子与抗原决定簇之间的结合能称为亲和力。

**avidity（functional affinity，功能亲和力）** 描述的则是抗体与抗原之间的总体结合能：

- 它是与抗原的总结合能；
- 它是**抗体群体**与不同抗原位点结合时，所有单个亲和力的总和的平均结合能；
- 抗体在每一个结合位点上的总结合强度的量度即称为 avidity。

> [!quote] avidity（Crowther, 2009, p. 130 / p. 137）
> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"
>
> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"
>
> 亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

### 影响 avidity 的三个因素

avidity 由以下三点共同决定：

1. the binding affinity；
2. valency（效价）；
3. the structural arrangement of the antibody and antigen in question（抗体与抗原的结构排布）。

也就是说，avidity 是一个体系层面的量，随抗体类型、抗原表位分布和两者的空间关系变化，而不只是单个 paratope 的性质。

## 血清稀释会改变 avidity：一个容易忽略的方法学问题

在多克隆血清体系中，avidity 不是恒定值。血清的 avidity 在稀释时可能发生变化，因为操作者可能在稀释过程中把某些抗体群体稀释掉了。

> [!example] 高亲和力与低亲和力抗体群体的竞争
> 设想一份血清中同时含有**少量对某一复杂抗原高亲和力的抗体**和**大量低亲和力抗体**。在血清**未大幅稀释**的免疫学条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；但随着稀释，高亲和力抗体的浓度不断下降，直到体系中只剩下低亲和力抗体。
>
> 当操作者用免疫学方法比较不同抗血清与抗原的差异活性时，这类问题很重要。由于异质性抗体群体的动态（各抗体分子的相对浓度与亲和力），**任何血清的稀释都可能影响其区分抗原的能力**。（Crowther, 2009, p. 137）

对检测设计的直接含义是：稀释倍数的选择不只是把信号拉进标准曲线范围，它同时改变了参与反应的抗体群体的组成。用同一份血清在不同稀释度下比较抗原，得到的结论未必一致。

## 抗体应答的类型与检测策略的选择

动物在抗原刺激下产生的是**多克隆抗体**，且抗体类型并不仅限于 IgG；各抗体类型的产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

免疫方式区分两类：

- **passive immunization（被动免疫）**：直接给予中和抗体；
- **active immunization（主动免疫）**：给予抗原，由机体产生保护性抗体。

在主动免疫的情形下，**疫苗注射方式**（sc-皮下注射或 im-肌内注射）可以诱导产生多种抗体类型（isotype）。因此评估疫苗接种效果时，必须考虑检测目标的选择：是采用总抗体检测、isotype-specific assay，还是检测抗原清除。

对**口服/吸入免疫**途径，这一选择更为突出：

> [!quote] 检测目标的选择（Crowther, 2009, p. 140）
> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"
>
> 免疫分析工作者必须判断：同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地反映疫苗接种带来的益处。

黏膜途径免疫后，总抗体检测可能掩盖真正与保护相关的抗体群体，这正是需要单独考虑 isotype 的原因。

## 这些理论前提的边界

把上述内容归拢起来，有三条边界值得在方法开发时反复确认：

其一，表位数量的表面积估算建立在「整个表面均具抗原性」与「分子最大结合」两个假设之上，前者在真实抗原中很少成立，因此得到的只是上限值，可用于推算饱和所需的抗体量，但不能当作实际可及表位数。

其二，affinity 是单一结合位点的性质，avidity 是抗体群体与多个抗原位点结合的总体性质，受 binding affinity、valency 和抗体—抗原结构排布三者共同影响。用单抗的 affinity 数据推断多抗体系的整体结合行为是不成立的。

其三，多克隆血清是异质性群体，稀释会改变其中各抗体群体的相对比例，从而改变 avidity 乃至区分抗原的能力；同样地，不同免疫途径诱导出的 isotype 谱不同，检测目标是选总抗体还是特定 isotype，需要在方法设计阶段就确定，而不是事后解释数据时才考虑。