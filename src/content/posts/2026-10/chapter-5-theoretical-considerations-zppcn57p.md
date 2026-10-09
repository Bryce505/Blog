---
draft: true
reviewNotes:
  - "正文过短: 3024/13096=23% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗体应答：多克隆与同型分布']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,388 字符（原文 16,470，比例 21%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原尺寸、表位定义、affinity 与 avidity"
date: 2026-10-09
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理免疫检测理论基础中的几个关键概念：抗原尺寸如何决定可结合位点的数量上限，epitope、epitype、paratope 的定义边界，affinity 与 avidity 的区别，以及抗体应答的同型分布、免疫途径和稀释操作对检测结果的影响。内容按「抗原—抗体—实验变量」的"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理免疫检测理论基础中的几个关键概念：抗原尺寸如何决定可结合位点的数量上限，epitope、epitype、paratope 的定义边界，affinity 与 avidity 的区别，以及抗体应答的同型分布、免疫途径和稀释操作对检测结果的影响。内容按「抗原—抗体—实验变量」的顺序组织。

## 抗原尺寸如何决定可结合位点的数量上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个估算本身带有很强的假设：「Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally」（Crowther, 2009）——即假定整个表面都具有抗原性（很少是真实的），且分子达到最大结合。

它的用途在于：「calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface」（Crowther, 2009），也就是估算饱和某一抗原所需的抗体量，或测定抗体结合量随可用表面积的变化。

## 表位、表位型与互补位的定义

- **epitope**：antigenic site，即抗原表位。
- **Epitype**：「An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site」（Crowther, 2009）。表位型是抗原上的一个区域，由一组识别非常相似化学结构的密切相关抗体（例如定义重叠或相互关联表位的 mAbs）识别；可视为识别与同一抗原位点反应的、特异性略有差异的抗体的区域。
- **paratope**：抗体上结合抗原表位的部分。

## Affinity 与 avidity：单一位点结合能与总体结合强度

affinity（binding affinity）包括三层含义：

1. 单一 epitope 与 paratope 之间的能量；
2. 抗原表位与抗体互补位在**单一结合位点**上相互作用的强度；
3. 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

avidity（functional affinity）则是：

1. 与抗原的总体结合能，「The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites」（Crowther, 2009）；
2. 抗体在每一个结合位点上总结合强度的量度，也称 functional affinity；
3. 受三个因素影响：binding affinity、valency，以及抗体与抗原的结构排布。

对于多克隆血清，avidity 还可以看作「the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)」（Crowther, 2009）。

## 抗体应答：多克隆与同型分布

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 免疫途径与检测形式的选择

passive immunization 指直接注射中和抗体；active immunization 则是给予抗原、使机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑采用哪一类检测来评估疫苗接种效果：总抗体检测、isotype-specific assay，还是检测抗原清除。

口服/吸入免疫途径下，需要判断同型抗体检测的价值：「The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody」（Crowther, 2009）。

## 稀释会改变血清的 avidity

血清的 avidity 在稀释时可能发生变化，因为操作者可能把某些抗体群体稀释掉：「It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies」（Crowther, 2009）。

一个具体场景是：血清中可能同时存在「a low quantity of antibodies showing high affinity」与「a high quantity of low-affinity antibody」。在血清不被大幅稀释的免疫检测条件下，高亲和力与低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；而一旦稀释，高亲和力抗体的浓度会下降，直至只剩下低亲和力抗体。当操作者用免疫检测「compare antigens by their differential activity with different antisera」时，这类问题很重要——「The dilution of any serum can affect its ability to discriminate between antigens」，原因是异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力）发生了变化（Crowther, 2009）。

## 这些理论前提给实验设计划出的边界

- 由球形表面积除以 20nm^2 得到的表位数量只是一个上限估计，它同时假定整个表面具有抗原性、且分子达到最大结合，这两个前提很少成立。
- avidity 是群体层面的平均量，受 binding affinity、valency 和抗体—抗原结构排布共同影响；它不是固定参数，会随稀释而改变，因此用不同抗血清比较抗原、或设计稀释系列时需要留意这一点。
- 抗体应答在 isotype 上是多样的，检测形式（总抗体、isotype-specific 还是抗原清除）需要在方法设计阶段就确定，而不是事后补加。