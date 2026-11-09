---
draft: true
reviewNotes:
  - "正文过短: 2733/13096=21% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,480 字符（原文 16,470，比例 15%）超出 9,058～15,646 字符的区间"
title: "抗原、抗体与结合力：ELISA 反应体系的理论前提"
date: 2026-11-09
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的方法学讨论多集中在操作与验证层面，而决定抗体用量、稀释方案与检测形式的那几个前提，往往在建立方法之初就被略过了。本文按抗原、抗体、结合力三条线索整理这些理论前提：抗原分子大小与可及表位数的关系，epitope/paratope 与 affinity/avidity "
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的方法学讨论多集中在操作与验证层面，而决定抗体用量、稀释方案与检测形式的那几个前提，往往在建立方法之初就被略过了。本文按抗原、抗体、结合力三条线索整理这些理论前提：抗原分子大小与可及表位数的关系，epitope/paratope 与 affinity/avidity 的概念层次，以及免疫应答与免疫途径如何决定检测对象。

## 抗原分子的大小与可及表位数量

分子越大，其复杂性也就越高。

Fab 与抗原结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有一个必须交代的前提：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009）。也就是说，它假定整个分子表面都具有抗原性——而这很少成立——并且分子处于最大结合状态。因此算得的是上限，不是实际可结合位点数。

**应用**：据此可以估算使某一抗原达到饱和所需的抗体量，或测定抗体结合量随可用表面的变化。

## 抗原位点与抗体结合部位的概念层次

三个术语的区分是后续讨论亲和力的基础：

- **epitope**：即 antigenic site，抗原上被抗体识别的位点。
- **epitype**：抗原上的一个区域，由一组化学结构非常相似的抗体（例如定义重叠或相互关联表位的 mAb）所识别；可视为识别同一抗原位点、但特异性略有差异的抗体所对应的区域。
- **paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单一位点与整体结合

### affinity（结合亲和力）

抗体分子与抗原决定簇之间的结合能称为亲和力。具体包含三层含义：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗原 epitope 与抗体 paratope 在**单一位点**上相互作用的强度；
3. 由**非共价相互作用**介导，包括氢键、静电作用、范德华力和疏水作用，并以平衡解离常数 **K<sub>D</sub>** 定义。

### avidity（功能性亲和力）

avidity 又称 functional affinity，指的是与抗原的总结合能，即抗体在每个结合位点上总结合强度的量度。“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009）。

其影响因素有三个：1）binding affinity，2）valency，3）抗体与抗原的结构排布。

在抗血清这类异质抗体群中，这一概念体现得更为直接：“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”（Crowther, 2009）。

## 免疫应答产生的是异质抗体群

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

由此引出一个容易被忽略的后果：血清的亲和力在稀释时可能会发生变化，因为操作者可能在稀释过程中把某些抗体群稀释掉。

典型情形是血清中同时存在**少量高亲和力抗体**与**大量低亲和力抗体**。在血清未大幅稀释的免疫分析条件下，两类抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度持续下降，最终体系中只剩低亲和力抗体。用免疫分析比较抗原与不同抗血清的差异活性时，这个问题尤其重要——**任何血清的稀释都可能影响其区分抗原的能力**，其根源在于异质抗体群的动态，即各抗体分子的相对浓度与亲和力。

## 免疫途径决定检测对象的选择

- **passive immunization**：直接给予中和抗体。
- **active immunization**：给予抗原，由机体产生保护性抗体。

疫苗经 sc（皮下注射）或 im（肌内注射）途径接种，可诱导产生多种抗体类型（isotype）。因此在评估疫苗接种效果时，必须考虑检测对象究竟是总抗体、采用 isotype-specific assay，还是检测抗原清除。

口服或吸入免疫路径下，问题更具体：免疫分析工作者必须判断，针对 isotype-specific 抗体（尤其是 IgA）的检测，是否比总抗体的检测更能反映疫苗接种的获益。

## 小结

这几条前提在方法上的应用方向各不相同：抗原大小决定的是抗体用量的量级估计，affinity 与 avidity 的区分决定了对稀释与单价/多价结合的敏感程度，抗体群的异质性决定了稀释方案对抗血清区分能力的影响，而免疫途径决定了检测对象是总抗体还是特定 isotype。

同时需要记住两处简化处理的边界：以球形表面积除以 20 估算表位数，前提是整个表面均具抗原性且结合达到最大，实际很少成立；以血清 avidity 表征混合抗体的结合能力，则该值会随稀释而改变。两者给出的都是上限或经验值，不能当作抗原或抗血清的固有常数使用。