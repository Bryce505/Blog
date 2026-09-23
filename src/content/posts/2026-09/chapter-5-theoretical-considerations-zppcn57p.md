---
draft: true
reviewNotes:
  - "正文过短: 4192/13045=32% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗原刺激后的抗体应答：多克隆与抗体类型']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,110 字符（原文 16,405，比例 25%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与 avidity"
date: 2026-09-23
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量能力建立在几组分子层面的前提之上：抗原表面能提供多少个可被识别的位点、抗体与单个位点之间的结合强度、以及一个异质性抗体群体与一个抗原之间的总体结合强度。这篇笔记按「抗原—抗体—免疫应答」的顺序，梳理 Crowther 在 The ELISA Guidebook "
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量能力建立在几组分子层面的前提之上：抗原表面能提供多少个可被识别的位点、抗体与单个位点之间的结合强度、以及一个异质性抗体群体与一个抗原之间的总体结合强度。这篇笔记按「抗原—抗体—免疫应答」的顺序，梳理 Crowther 在 *The ELISA Guidebook* 第五章中提出的这些理论考虑，并指出它们在饱和实验设计、抗原比较和疫苗评价中的直接后果。

## 抗原大小与表位数量：球形表面积估算的用途与前提

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

### 「表面积 ÷ 20」这个算法成立的前提

这个数字只是上限而非实测值。原文指出：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally” —— 这样的计算是基于整个表面具有抗原性(很少是真实的)和分子最大结合的事实 (Crowther, 2009)。

### 估算结果用在哪里

这类计算的实际用途是反向推算实验条件：可以据此估算饱和任意一种试剂需要多少抗体，或测定抗体结合水平随可用表面积变化的关系 (Crowther, 2009)。也就是说，球形表面积除以 20 得到的是设计饱和实验时的起点，而不是对抗原真实表位数量的测量。

## 表位、表位型与 paratope：三个层级的概念划分

**epitope**（抗原表位）即 antigenic site。

**Epitype**（表位型）指抗原上的一个区域，由一组化学结构非常相似的抗体识别。原文的界定是：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site” —— 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体(例如, mAbs ,它们定义重叠或相互关联的表位)识别；表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域 (Crowther, 2009)。

**paratope**（互补位）则是抗体上结合抗原表位的部分。

三个概念的层级关系是清楚的：epitope 描述抗原一侧的位点，paratope 描述抗体一侧的结合区，而 epitype 描述的是「同一抗原位点被一组特异性略有差异的抗体所识别」这一区域层面的现象。

## affinity 与 avidity：从单个结合位点到抗体群体

### affinity：单一结合位点上的结合强度

binding affinity 在笔记中给出三种等价界定：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗原的 epitope 与抗体 paratope <span style="background-color: #ff666680">在单一结合位点上</span>的相互作用强度；
3. Affinity 由<span style="background-color: #ff666680">非共价相互作用</span>介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡<span style="background-color: #ff666680">解离常数（K</span><sub>D</sub><span style="background-color: #ff666680">）</span>定义。

原文的概括是：“The binding energy between an antibody molecule and an antigen determinant is termed affinity.” —— 抗体分子与抗原决定簇之间的结合能称为亲和力 (Crowther, 2009)。

### avidity：整个抗体群体的功能性亲和力

**avidity** 又称 functional affinity，衡量的是与抗原的总体结合能。它是抗体在每一个结合位点上总结合强度的度量，也可以理解为血清中异质性抗体与各种抗原位点之间所有不同亲和力的总和：

- “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”；
- “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)” (Crowther, 2009)。

影响 avidity 的因素有三个：1) the binding affinity, 2) valency, 3) the structural arrangement of the antibody and antigen in question。

## 抗原刺激后的抗体应答：多克隆与抗体类型

机体应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\
(Crowther, 2009)

## 免疫途径如何决定检测策略：总抗体还是 isotype-specific

两类免疫方式需要区分：**passive immunization** 是直接注射中和抗体；**active immunization** 是给予抗原、由机体产生保护性抗体。

疫苗注射通常采用 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：评估疫苗接种效果时，究竟应当使用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。

口服或吸入免疫则把问题进一步聚焦到黏膜抗体上。原文强调：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody” —— 免疫学家必须决定同型抗体(特别是 IgA )的检测是否能比总抗体的检测更深入地了解疫苗接种的好处 (Crowther, 2009, p. 140)。

## 稀释对血清 avidity 的影响

血清的 avidity 会随稀释而改变，因为稀释过程可能把某些抗体群体一并稀释掉。这一点在抗原比较实验中尤为关键。

一个具体的机制是：血清中可能存在**少量针对某一复杂抗原的高亲和力抗体**与**大量低亲和力抗体**。在血清**未被大幅稀释**的免疫测定条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；随着稀释进行，高亲和力抗体的浓度不断下降，直至体系中只剩下低亲和力抗体。当操作者用免疫测定、通过不同抗血清的差异活性来**比较抗原**时，**这类问题很重要**。由于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力），**任何血清的稀释都可能影响其区分抗原的能力** (Crowther, 2009)。

## 收尾：这些理论前提对方法学的约束

把上述内容放在一起，可以看到几条对实验设计的约束。表位数量只能按球形表面积估算上限，前提是「整个表面均具抗原性、且分子达到最大结合」，两者在真实体系中都不成立，因此该数值只能用于估算饱和试剂所需的抗体量，不能当作抗原真实表位数的测量。affinity 与 avidity 分属不同层级：前者是单一 epitope–paratope 的相互作用，由 K<sub>D</sub> 描述；后者是异质性抗体群体对多个抗原位点的总结合强度，同时受 binding affinity、valency 和抗体—抗原的结构排布三者影响，因此二者不可互换使用。

由此还派生出一个操作层面的边界：稀释本身会改变血清 avidity，进而改变抗体区分抗原的能力。凡是以不同抗血清的差异活性比较抗原、或用抗体检测评估疫苗接种效果的工作，都需要先明确检测的是总抗体还是特定 isotype（如 IgA），并把稀释条件当作方法学变量而非单纯的浓度调整。笔记本身未给出这些判断的定量阈值（例如高、低亲和力抗体的浓度比与稀释倍数的关系），这一部分需要结合具体体系自行确定。