---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['135']"
  - "正文过短: 4050/13096=31% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗原刺激后产生的是多克隆抗体，类型不限于 IgG']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,028 字符（原文 16,470，比例 24%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答如何影响检测设计"
date: 2026-11-13
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "导读：ELISA 的可靠性建立在几个上游概念之上——抗原分子的大小与可及表位、抗体与表位之间结合的强度，以及免疫应答本身带来的抗体异质性。本文按「抗原—术语—结合强度—抗体产生—检测策略」的顺序梳理这些理论要点，并标出每一步在方法设计上的落点。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

导读：ELISA 的可靠性建立在几个上游概念之上——抗原分子的大小与可及表位、抗体与表位之间结合的强度，以及免疫应答本身带来的抗体异质性。本文按「抗原—术语—结合强度—抗体产生—检测策略」的顺序梳理这些理论要点，并标出每一步在方法设计上的落点。

## 抗原的分子大小决定理论上可结合的位点数量

分子越大，其复杂性也就越高。

Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009, p. 127）

也就是说，这类计算建立在两个很少成立的假设之上：整个表面都具有抗原性，以及分子达到最大结合。

这一估算的实际用途是反推饱和任意抗原所需的抗体量，或者把抗体结合量作为可及表面积的函数来测量：

> “calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”（Crowther, 2009, p. 127）

## epitope、epitype、paratope：三组容易混淆的术语

- **epitope**：即 antigenic site，抗原上被抗体识别的位点。
- **paratope**：抗体上结合抗原表位的部分。
- **Epitype**：抗原上的一个区域，由一组识别非常相似的化学结构的、密切相关的抗体（例如 mAb，它们定义重叠或相互关联的表位）所界定。表位型可视为识别与同一抗原位点反应的、特异性略有不同的抗体所对应的区域。

> “An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009, p. 128）

三者的区分对检测设计的意义在于：epitope 是单个结合事件的对象，epitype 描述的是一组抗体对同一区域的识别谱，而 paratope 决定了这个谱能有多宽。

## 亲和力与亲合力：两个层级上的结合强度

### affinity：单一结合位点上的强度

抗体分子与抗原决定簇之间的结合能称为亲和力：

> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.”（Crowther, 2009, p. 136）

其定义可以归纳为三点：

1. 单个 epitope 与 paratope 之间的能量；
2. 是抗原 epitope 与抗体 paratope 在单一结合位点上的相互作用强度；
3. 由非共价相互作用介导，包括氢键、静电作用、范德华力和疏水相互作用，并以平衡解离常数（K<sub>D</sub>）定义。

### avidity：多个位点叠加后的总体强度

avidity 又称 functional affinity，指的是与抗原的总结合能：

> “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009, p. 130）

它度量的是抗体在每个结合位点上的总结合强度，并受三个因素影响：1）binding affinity，2）valency，3）抗体与抗原的结构排布。

在多克隆血清的语境下，avidity 可以看作血清中异质性抗体与各抗原位点之间所有不同亲和力的总和：

> “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”（Crowther, 2009, p. 137）

### 稀释会改变血清的表观亲合力

> “It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”（Crowther, 2009, p. 137）

一个典型情形是：血清中同时存在少量对复杂抗原高亲和力的抗体和大量低亲和力抗体。在稀释倍数不大的免疫分析条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；随着稀释，高亲和力抗体浓度下降，最终只剩下低亲和力抗体。

> “Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).”（Crowther, 2009, p. 137）

因此，用不同抗血清比较抗原时，稀释度本身就是一个需要控制的变量。

## 抗原刺激后产生的是多克隆抗体，类型不限于 IgG

抗原刺激机体产生的是多克隆抗体，且抗体类型并不限于 IgG。各抗体类型出现的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

（Crowther, 2009, p. 135）

## 免疫途径不同，检测策略也要跟着变

**被动免疫与主动免疫。**被动免疫指直接给予中和抗体；主动免疫指给予抗原、由机体产生保护性抗体。两者的检测逻辑不同：前者测的是外源给予的抗体量，后者测的是机体自身的应答。

**注射途径。**疫苗经 sc（皮下注射）或 im（肌内注射）给药时，可诱导产生多种抗体类型（isotype）。因此必须考虑：用总抗体检测、isotype-specific assay，还是用检测抗原清除的方法来评估疫苗接种效果。

**口服／吸入免疫。**此时产生的应答以黏膜抗体为主，检测目标的选择更为关键：

> “The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”（Crowther, 2009, p. 140）

即同型抗体（尤其是 IgA）的检测是否比总抗体检测更能反映疫苗接种的获益，需要事先判断，而不是默认用总抗体。

## 收束：这些前提在什么时候会失效

这组理论概念的价值在于给检测设计划出边界。以球形表面积除以 20nm^2 估算最大结合位点数，其前提（整个表面均具抗原性、分子达到最大结合）在真实抗原上很少同时成立，因此该数值只是上限而非预期值。亲和力描述的是单位点强度，亲合力描述的是多位点、多克隆叠加后的总体强度，二者不可互换；在异质性血清中，后者还会随稀释而漂移，这使得不同稀释度下的抗原比较未必可比。抗体类型的多样性则决定了检测目标的选择（总抗体、特定 isotype 或抗原清除）必须与免疫途径和评价目的相匹配，而不存在通用的默认选项。

在这些概念之外，如何把上述前提转化为可执行的判定标准（例如 cut-off 的设定、滴度的表达方式），本文未作展开。