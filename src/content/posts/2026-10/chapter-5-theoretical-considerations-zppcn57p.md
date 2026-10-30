---
draft: true
reviewNotes:
  - "正文过短: 3084/13096=24% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,868 字符（原文 16,470，比例 17%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与亲合力"
date: 2026-10-30
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的检测性能最终由抗原—抗体相互作用的物理化学性质决定。本文从抗原一侧出发，梳理分子大小与表位数量估算的前提、表位相关术语的定义，再转到抗体一侧，区分 affinity 与 avidity，说明多克隆血清在稀释下的行为变化，最后交代不同免疫方式对检测策略选择的影响。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的检测性能最终由抗原—抗体相互作用的物理化学性质决定。本文从抗原一侧出发，梳理分子大小与表位数量估算的前提、表位相关术语的定义，再转到抗体一侧，区分 affinity 与 avidity，说明多克隆血清在稀释下的行为变化，最后交代不同免疫方式对检测策略选择的影响。

## 抗原性考量：分子大小与结合位点数量的估算

### 分子越大，复杂性越高

分子越大，其复杂性也就越高。Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

### 该估算的两个前提

这一计算基于两个事实：整个表面均具有抗原性（很少成立），且分子达到最大结合。原文对此有明确保留：

> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009）

尽管存在上述限制，该估算仍有实际用途：可用于计算饱和任一试剂所需的抗体量，或测定抗体结合水平随可用表面的变化（“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”）。

### 表位相关术语

**epitope**：即 antigenic site（抗原位点）。

**epitype**：抗原上的一个区域，由一组识别非常相似化学结构的密切相关抗体（例如 mAb，它们定义重叠或相互关联的表位）所识别；可视为识别与同一抗原位点反应的、特异性略有不同的抗体所对应的区域。

> “An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009）

**paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：两个层次的结合强度

### affinity：单一位点上的结合能

亲和力指单一 epitope 与 paratope 之间的能量，即抗体分子与抗原决定簇之间的结合能，描述的是**单个结合位点**上的相互作用强度。它由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡解离常数（K<sub>D</sub>）定义。

### avidity：整体结合能

avidity 又称 functional affinity，指与抗原的整体结合能。它可表述为一个抗体群体与不同抗原位点结合时，各个亲和力之和所给出的平均结合能；也可表述为单个抗体在其全部结合位点上总结合强度的度量。avidity 的影响因素有三个：结合亲和力本身、价数（valency），以及抗体与抗原的结构排布。

## 抗体一侧：多克隆应答与群体异质性

### 免疫应答产生的是多克隆抗体

应对抗原刺激产生的是多克隆抗体，且抗体类型并不限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 血清的 avidity 会随稀释改变

亲和力可以看作血清中所含异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和。需要认识到，血清的 avidity 在稀释时可能发生变化，因为操作者可能在稀释过程中把某些抗体群体稀释掉（Crowther, 2009）。

原文给出的例子是：血清中可能同时存在**少量**对某一复杂抗原**高亲和力**的抗体和**大量低亲和力**抗体。在血清未大幅稀释的免疫assay条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；而稀释会使高亲和力抗体的浓度下降，直至体系中只剩低亲和力抗体。当操作者以不同抗血清的差异活性来比较抗原时，这类问题尤其重要——任何血清的稀释都可能影响其区分抗原的能力，根源在于异质性抗体群体的动力学，即各抗体分子的相对浓度与亲和力（Crowther, 2009）。

## 免疫方式及其对检测策略的影响

### passive 与 active immunization

passive immunization 是直接注射中和抗体；active immunization 是给予抗原，使机体产生保护性抗体。

### 接种途径决定抗体的 isotype 组成

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）。这种方式可诱导产生多种抗体类型（isotype），因此必须考虑评估疫苗接种效果时究竟采用总抗体检测、isotype-specific assay，还是检测抗原清除。

口服/吸入免疫则带出另一层判断：检测 isotype-specific 抗体（尤其是 IgA）是否比检测总抗体更能深入反映疫苗接种的获益（Crowther, 2009）。

## 边界与判断要点

把上述内容归拢起来，可以看到三条贯穿全文的判断线索。其一，基于表面积除以 20 得到的 Fab 结合位点数只是**上限**，其成立依赖"整个表面均具抗原性"与"分子达到最大结合"两个很少同时满足的前提，实际可及表位数量应低于该估算值。其二，affinity 描述单一位点，avidity 描述整体；对多克隆血清而言，avidity 是异质性抗体群体各亲和力的总和，因而**不是固定属性**——稀释会改变群体组成，进而改变区分抗原的能力，这在用不同抗血清比较抗原时需要格外注意。其三，免疫途径（sc/im 与口服/吸入）决定了抗体的 isotype 组成，检测策略（总抗体、isotype-specific、抗原清除）须与之匹配，否则测到的信号与想回答的问题可能并不对应。

原文未就"何时应优先选择 isotype-specific assay 而非总抗体检测"给出统一判据，只将其留作免疫assay设计者需要自行判断的问题。