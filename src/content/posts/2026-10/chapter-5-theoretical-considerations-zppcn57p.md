---
draft: true
reviewNotes:
  - "正文过短: 4753/13096=36% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,869 字符（原文 16,470，比例 30%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位数量、抗体亲和力/亲合力与稀释效应"
date: 2026-10-07
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理自 Crowther (2009) 第 5 章 \"Theoretical Considerations\"，把 ELISA 背后几个容易被跳过、却直接影响实验设计与数据解读的前提梳理一遍：抗原大小与可结合抗体数量的关系、epitope/epitype/paratope "
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理自 Crowther (2009) 第 5 章 "Theoretical Considerations"，把 ELISA 背后几个容易被跳过、却直接影响实验设计与数据解读的前提梳理一遍：抗原大小与可结合抗体数量的关系、epitope/epitype/paratope 的界定、affinity 与 avidity 的分野、稀释对血清表观亲合力的影响，以及免疫途径与抗体 isotype 对检测策略的约束。

## 抗原大小如何决定可结合的抗体数量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个估算成立与否取决于两个前提，原文写得很明确：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009)

也就是假定整个表面都具有抗原性（很少是真实的）、且分子达到最大结合。所以这个数字给出的是上限，不是预期值。

在应用层面，这类计算有两个用途：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009)

即估算饱和某一试剂所需的抗体量，或测定抗体结合水平随可用表面的变化。

## 表位相关术语：epitope、epitype 与 paratope

**epitope**：antigenic site，抗原表位。

**epitype** 的定义是：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009)

也就是说，epitype 是抗原上由一组化学识别结构非常相似的抗体（例如定义重叠或相互关联表位的 mAbs）所识别的区域；可以把它理解为：针对同一抗原位点、但特异性略有差异的那组抗体所对应的区域。

**paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单一位点能量与整体结合强度

### affinity

affinity（结合亲和力）在笔记中有三层表述：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗原的 epitope 与抗体的 paratope 在**单一位点**上相互作用的强度；
3. affinity 由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡**解离常数（K<sub>D</sub>）**定义。

### avidity

avidity 即 functional affinity，笔记给出三层表述：

1. 与抗原的总结合能：

   > "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009)

2. 抗体在每一个结合位点上总结合强度的量度，也称为 functional affinity；
3. 三个影响因素：the binding affinity、valency，以及 the structural arrangement of the antibody and antigen in question。

在血清层面，avidity 的含义进一步扩展：

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009)

也就是说，血清的 avidity 是异质性抗体群体与各个抗原表位之间全部亲和力的总和——它是一个群体层面的平均量，而不是单分子的常数。

## 血清稀释如何改变表观亲合力

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009)

原文给出的具体场景是：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)." (Crowther, 2009)

翻译过来：一份血清中可能同时含有「少量高亲和力抗体」和「大量低亲和力抗体」。在不作大幅稀释的免疫分析条件下，高、低亲和力抗体会竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度会被降低，直到体系中只剩下低亲和力抗体。当操作者用不同抗血清、以差异活性来比较抗原时，这个问题尤其重要——由于异质性抗体群体本身的动力学（各抗体分子的相对浓度与亲和力），任何血清的稀释都会影响它区分不同抗原的能力。

## 免疫途径与抗体类型如何决定检测策略

### 抗体产生的多样性

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|--> (Crowther, 2009)

### 主动免疫与被动免疫

- passive immunization：直接打中和抗体；
- active immunization：服用抗原，产生保护性抗体。

### 免疫途径决定能看到什么

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：评估疫苗接种效果时，究竟使用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。

对口服／吸入免疫而言，这一取舍更加突出：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009)

即免疫分析工作者必须判断：同型抗体（特别是 IgA）的检测，是否能比总抗体检测更深入地揭示疫苗接种带来的获益。

## 这些理论前提对 ELISA 设计与解读意味着什么

把上面的内容合起来看，这套理论考量约束的是四件事：

- **抗原侧的估算只是上限。** 表面积除以 20nm^2 得到的是 Fab 结合位点的最大数量，其前提是「整个表面都具有抗原性」和「分子最大结合」，两者都很少同时成立，因此结果只能当上限用，不能当作预期值。
- **结合强度分两个层次。** affinity 描述单个 epitope–paratope 位点的结合能，由非共价作用介导并以 K<sub>D</sub> 定义；avidity 是功能性的整体结合强度，取决于 binding affinity、valency 以及抗体与抗原的结构排布。血清的 avidity 是异质性抗体群体与各表位亲和力的总和，是一个群体平均值，不是常数。
- **稀释不是中性操作。** 稀释会改变抗体群体的组成，进而改变血清区分不同抗原的能力；用不同抗血清比较抗原的差异活性时，这一点必须纳入考虑。
- **抗体类型的可见性取决于免疫途径。** sc／im 注射会诱导多种 isotype；口服或吸入免疫则可能需要 isotype-specific（尤其 IgA）检测，才能看到总抗体检测掩盖掉的差异。

这四条都属于方法学前提层面的判断。笔记本身止步于这些理论概念，没有延伸到具体的检测形式与数据处理。