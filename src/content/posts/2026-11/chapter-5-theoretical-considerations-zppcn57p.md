---
draft: true
reviewNotes:
  - "正文过短: 2840/13096=22% < 40%"
  - "空壳章节（正文不足 120 字）: ['免疫应答给出的是多克隆抗体']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,602 字符（原文 16,470，比例 16%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原特性、抗体亲和力与亲合力"
date: 2026-11-19
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量表现，最终取决于抗原一侧的可及表位、抗体一侧的亲和力与亲合力，以及二者结合时的群体行为这三层因素。本篇按这一脉络整理：先看抗原大小如何决定可结合位点的上限及其估算前提，再界定表位与互补位、affinity 与 avidity 两组容易混淆的概念，最后落到抗体应答"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量表现，最终取决于抗原一侧的可及表位、抗体一侧的亲和力与亲合力，以及二者结合时的群体行为这三层因素。本篇按这一脉络整理：先看抗原大小如何决定可结合位点的上限及其估算前提，再界定表位与互补位、affinity 与 avidity 两组容易混淆的概念，最后落到抗体应答、稀释效应与免疫方式对检测设计的影响。

## 抗原分子越大，可结合位点越多，但估算有前提

分子越大，其复杂性也就越高。Fab 的结合面积大概是20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得 Fab 结合位点的最大数量。

这一算法成立的前提必须交代清楚："Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）——即假定整个表面都具有抗原性（这在多数情况下并不成立），且分子达到最大结合。

在实践上，这类计算可用于估算饱和某种试剂所需的抗体量，或测定抗体结合量随可及表面的变化（Crowther, 2009）。

## 表位、表位型与互补位：三个容易混用的术语

- **epitope**：即 antigenic site，抗原上被抗体识别的位点。
- **epitype**：抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。
- **paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity 分属两个层级

**affinity（结合亲和力）**指单一结合位点层面的作用强度，可从三个角度表述：

1. 单个 epitope 与 paratope 之间的能量；
2. 在单个结合位点上，抗原 epitope 与抗体 paratope 之间相互作用的强度；
3. 由非共价作用介导，包括氢键、静电键、范德华力和疏水作用，并以平衡解离常数（K<sub>D</sub>）定义。

**avidity（亲合力，functional affinity）**则是整体层面的量：

1. 与抗原的总体结合能——"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009）；
2. 抗体在每个结合位点上总体结合强度的量度，又称 functional affinity；
3. 受三个因素影响：binding affinity、valency，以及抗体与抗原的结构排布。

## 免疫应答给出的是多克隆抗体

应对抗原刺激产生的是多克隆抗体，且抗体类型并不限于 IgG；各抗体类型的产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 稀释会改变血清的表观亲合力

抗体分子与抗原决定簇之间的结合能称为亲和力。"Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009）。

关键在于，血清的 avidity 在稀释时可能发生变化，因为操作者可能把某些抗体群体稀释掉。设一份血清中同时含有少量对某复合抗原高亲和力的抗体和大量低亲和力抗体：在血清未被大幅稀释的免疫分析条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；而稀释后高亲和力抗体的浓度不断下降，直至体系中只剩低亲和力抗体。当操作者用免疫分析比较不同抗血清与抗原的差异活性时，这类问题很重要——任何血清的稀释都可能影响其区分抗原的能力，根源在于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力）。

## 免疫方式决定该测总抗体还是测同型抗体

passive immunization 是直接给予中和抗体；active immunization 则是给予抗原、由机体产生保护性抗体。

sc（皮下注射）或 im（肌内注射）接种可诱导产生多种抗体类型（isotype），因此必须考虑用总抗体检测、isotype-specific assay，还是检测抗原清除来评估疫苗接种效果。口服/吸入免疫的情形下，"The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）。

## 这些理论前提对检测设计的约束

把上述内容收拢：可及表位数量的估算建立在「整个表面具有抗原性」与「分子最大结合」两个假设之上，只能作为上限参考；affinity 描述单一结合位点，avidity 描述异质性抗体群体的加和，二者不可互换；血清一经稀释，参与竞争的抗体群体即发生改变，表观 avidity 与区分抗原的能力都可能随之变化，这对以不同抗血清比较抗原、或以系列稀释定量抗体的实验是直接的方法学约束；免疫途径与诱导出的 isotype 决定了检测应针对总抗体还是特定同型抗体。

需要说明的是，本笔记只覆盖抗原与抗体两侧的内容，摘要中提到的酶反应动力学与浓度—反应关系并未在正文中展开，这部分仍是空缺。