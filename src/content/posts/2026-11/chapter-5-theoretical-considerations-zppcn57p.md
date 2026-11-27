---
draft: true
reviewNotes:
  - "正文过短: 2475/13045=19% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,702 字符（原文 16,405，比例 16%）超出 9,023～15,585 字符的区间"
title: "ELISA 检测的理论基础：抗原表位、抗体亲和力与亲合力，以及由此决定的检测策略"
date: 2026-11-27
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的可靠性建立在几个并不直观的概念上：抗原表面能容纳多少抗体结合位点、亲和力与亲合力分别指什么、血清稀释会如何改变抗体的结合行为。本文按抗原—抗体相互作用的理论要点整理，依次说明分子大小与结合位点数的估算及其前提、表位相关术语的边界、亲合力随稀释变化的机制，以及免疫应答"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的可靠性建立在几个并不直观的概念上：抗原表面能容纳多少抗体结合位点、亲和力与亲合力分别指什么、血清稀释会如何改变抗体的结合行为。本文按抗原—抗体相互作用的理论要点整理，依次说明分子大小与结合位点数的估算及其前提、表位相关术语的边界、亲合力随稀释变化的机制，以及免疫应答产生的抗体类型如何影响检测策略的选择。

## 分子大小与可结合位点数目：一个只能当上限的估算

分子越大，其结构复杂性也就越高。Fab 与抗原结合的面积大概是 20nm^2，可视为一个 epitope 所占的表面积。按此思路，先计算分子的球形表面积，再除以 20，即可得到该分子可容纳的 Fab 结合位点数量的最大值。

> [!warning] 估算的前提
> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally” —— 这样的计算基于整个表面具有抗原性（很少是真实的）和分子达到最大结合这两个事实。

因此，该数值是理论上限。它的用途在于估算饱和某一试剂所需的抗体量，或把抗体结合水平作为可用表面的函数来测量。

## 表位、表位型与结合部位：术语各自的边界

**epitope** 即 antigenic site（抗原位点）；**paratope** 是抗体上结合抗原表位的部分。

**Epitype（表位型）** 指抗原上的一个区域，由一组化学结构非常相似的、密切相关的抗体（例如 mAb，它们定义重叠或相互关联的表位）所识别。表位型可视为识别与同一抗原位点反应的、特异性略有不同的抗体所对应的区域。

抗体的结合强度需要区分两个层级：

- **affinity（结合亲和力）**：单一 epitope 与 paratope 之间的能量；是单个结合位点上抗原表位与抗体 paratope 相互作用的强度。它由非共价相互作用介导，包括氢键、静电键、范德华力和疏水作用，并以平衡解离常数（K<sub>D</sub>）定义。
- **avidity（亲合力，即 functional affinity）**：与抗原的总结合能，是抗体群体结合不同抗原位点所有单个亲和力的总和所代表的平均结合能；也是抗体在每个结合位点上总结合强度的度量。

亲合力受三个因素影响：1) the binding affinity，2) valency，3) 抗体与抗原的结构排布。

## 血清的亲合力会随稀释而改变

抗体分子的结合能与其对抗原决定簇的结合强度，构成亲和力的定义：

> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.”

而血清层面的亲合力是异质性抗体的总和：

> “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”

正因为它是“总和”，稀释就会改变它：

> “It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”

典型情形是：血清中同时存在少量对某复杂抗原高亲和力的抗体和大量低亲和力抗体。在稀释倍数不大的免疫分析条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；随稀释推进，高亲和力抗体的浓度不断下降，最终只剩低亲和力抗体。在用不同抗血清比较抗原的差异活性时，这一点尤其重要——任何血清的稀释都可能影响其区分不同抗原的能力，这取决于异质性抗体群体的动力学，即各抗体分子的相对浓度与亲和力。

## 免疫应答产生的抗体类型与检测形式的选择

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

免疫方式本身也决定后续检测该怎么设计：

- **passive immunization**：直接给予中和抗体。
- **active immunization**：给予抗原，使机体产生保护性抗体。

疫苗采用 sc（皮下）或 im（肌内）注射时，可诱导产生多种抗体类型（isotype）。因此在评估疫苗接种效果时，必须考虑是采用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。

口服或吸入免疫则提出更具体的选择：免疫分析的设计者必须决定，针对 isotype-specific 抗体（尤其是 IgA）的检测是否能比总抗体检测更深入地反映疫苗接种的获益。

## 适用边界与结论

把上述几点归拢：

1. **表面积除以 20 得到的位点数只是上限**，因为它假定整个表面都具有抗原性且分子达到最大结合，而这两条在真实抗原上很少同时成立；引用该数值时必须带上这个前提。
2. **亲和力与亲合力不在同一层级**：前者描述单个 epitope–paratope 的相互作用并以 K<sub>D</sub> 表征，后者是群体、多价位与结构排布共同决定的“功能亲和力”。在多克隆血清中混用两者会导致误判。
3. **稀释是变量而不是中性操作**：血清亲合力随稀释改变，可能改变抗体区分不同抗原的能力，因此比较不同抗血清或不同抗原时，稀释方案必须固定并说明。
4. **检测形式的选择取决于免疫途径与目标抗体类型**：总抗体、isotype-specific（如 IgA）与抗原清除三类检测回答的问题不同，皮下/肌内注射与口服/吸入免疫所需的判断并不一致。笔记本身把“isotype-specific 是否优于总抗体”留作分析设计者的判断，而没有给出普适答案。

在这些前提明确之后，后续关于试剂滴定与浓度–反应关系的内容才有可比较的基础。