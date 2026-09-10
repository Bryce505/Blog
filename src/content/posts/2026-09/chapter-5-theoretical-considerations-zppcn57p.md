---
draft: true
reviewNotes:
  - "正文过短: 2245/13096=17% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 2,452 字符（原文 16,470，比例 15%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位数量、抗体亲和力/亲合力与血清稀释的影响"
date: 2026-09-10
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理的是 ELISA 背后的理论前提：抗原的大小如何决定表位数量的上限，epitope / epitype / paratope 与 affinity / avidity 这几组容易混用的概念如何界定，以及抗血清稀释和免疫途径为什么会改变检测实际测到的东西。顺序是先看抗原"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理的是 ELISA 背后的理论前提：抗原的大小如何决定表位数量的上限，epitope / epitype / paratope 与 affinity / avidity 这几组容易混用的概念如何界定，以及抗血清稀释和免疫途径为什么会改变检测实际测到的东西。顺序是先看抗原一侧，再看抗体一侧，最后落到这些性质对检测设计的含义。

## 抗原的大小决定可能结合位点数目的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积。通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量（Crowther, 2009）。

这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实（Crowther, 2009）。

**应用**：由此可以计算饱和任一试剂所需的抗体量，或测定抗体附着水平与可用表面之间的关系（Crowther, 2009）。

## 表位、表位型与 paratope 的界定

**epitope**：antigenic site。

**Epitype**：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别；表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域（Crowther, 2009）。

**paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一位点的结合能，与整个抗体群的结合强度

### affinity（binding affinity）

1. 单个 epitope 与 paratope 之间的能量；
2. 是抗原 epitope 与抗体 paratope 在**单一位点**上相互作用的强度（at a singular binding site）；
3. 由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

抗体分子与抗原决定簇之间的结合能称为亲和力（Crowther, 2009, p. 136）。

### avidity（functional affinity）

1. 与抗原的总体结合能；
2. 是抗体在每一个结合位点上总结合强度的度量，也称为 functional affinity；
3. 三个影响因素：1）the binding affinity，2）valency，3）the structural arrangement of the antibody and antigen in question。

avidity 可视为血清中所含异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和（Crowther, 2009, p. 137）。

## 血清稀释会改变 avidity，进而改变对抗原的区分能力

血清的 avidity 在稀释时可能会发生变化，因为操作者可能会稀释掉某些群体的抗体（Crowther, 2009, p. 137）。

一个具体的例子：血清中可能同时含有低丰度、对某一复杂抗原高亲和力的抗体，以及高丰度的低亲和力抗体。在血清未被大幅稀释的免疫分析条件下，高亲和力与低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；而在稀释后，高亲和力抗体的浓度不断下降，最终只剩下低亲和力抗体。这类问题在操作者用免疫分析以不同抗血清的差异活性来比较抗原时尤为重要——“The dilution of any serum can affect its ability to discriminate between antigens”，原因是异质性抗体群体的动力学（各个抗体分子的相对浓度与亲和力）发生了变化（Crowther, 2009, p. 137）。

## 免疫刺激产生什么样的抗体，以及该选择哪种检测

抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

passive immunization：直接打中和抗体；active immunization：服用抗原，产生保护性抗体。

疫苗注射方式为 sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型（isotype）；评估疫苗接种效果时，必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测。

口服/吸入免疫的情形下，免疫分析工作者必须决定：同型特异性抗体（尤其是 IgA）的检测，是否比总抗体检测能更深入地揭示疫苗接种的获益（Crowther, 2009, p. 140）。

## 适用边界与尚未解决的问题

几条需要在解读数据时保留的前提：

用球形表面积除以 20 得到的只是 Fab 结合位点数量的**上限**，它的两条前提——整个表面都具有抗原性、分子达到最大结合——在真实抗原上很少同时成立。

affinity 与 avidity 分属两个层次：前者归属于单个抗原决定簇与单个 paratope 之间的作用，后者归属于抗体分子或抗体群的整体，并额外受 valency 与抗体/抗原结构排布的影响。二者不可互换使用。

血清是多克隆的异质性混合物，稀释本身就会改变其 avidity 和区分抗原的能力，因此稀释方案不是中性的操作参数，而是测定条件的一部分。

检测对象的选择——总抗体、isotype-specific assay 还是抗原清除——必须与免疫方式和免疫途径相匹配；口服/吸入免疫下是否改用 IgA 等 isotype-specific 检测，仍是需要由检测设计者判断的问题。

本笔记正文处理的是抗原侧与抗体侧的理论前提；摘要中提到的酶反应动力学及浓度-反应关系，本篇未展开。