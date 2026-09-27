---
draft: true
reviewNotes:
  - "正文过短: 3253/13096=25% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,081 字符（原文 16,470，比例 19%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-09-27
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理 ELISA 检测背后的几个理论前提：抗原分子大小与可结合位点数量的关系、表位相关术语的定义、affinity 与 avidity 的区别，以及免疫方式对血清抗体组成的影响。它们共同回答同一个问题：在设计或解读一个 ELISA 之前，哪些抗原与抗体层面的性质会先一步决"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理 ELISA 检测背后的几个理论前提：抗原分子大小与可结合位点数量的关系、表位相关术语的定义、affinity 与 avidity 的区别，以及免疫方式对血清抗体组成的影响。它们共同回答同一个问题：在设计或解读一个 ELISA 之前，哪些抗原与抗体层面的性质会先一步决定结果。

## 抗原的分子大小如何限制可结合位点的数量

分子越大，其复杂性也就越高。

Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量；

这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实（Crowther, 2009）。也就是说，它给出的是可结合位点数量的上限，而非实测值。

**应用**：calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface（Crowther, 2009）。

## 表位相关的基本术语：epitope、epitype 与 paratope

**epitope**：antigenic site。

**Epitype**：表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域（Crowther, 2009）。

**paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：两个层面上的结合强度

### affinity（binding affinity）

1. the energy between a single epitope and paratope；
2. 结合亲和力是抗原的表位与抗体的 paratope 在单个结合位点上的相互作用强度；
3. Affinity 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

### avidity（functional affinity）

1. 与抗原的总结合能。"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009）；
2. 抗体在每个结合位点上总结合强度的量度称为 avidity。Avidity 也称为 functional affinity；
3. **三个影响因素**：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question.

## 血清稀释为什么会改变 avidity

"Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009）。

"It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009）。

一个具体的例子：血清中可能含有少量对某种复杂抗原高亲和力的抗体，同时含有大量低亲和力抗体。在血清未被大幅稀释的免疫分析条件下，高亲和力与低亲和力抗体会竞争抗原位点，高亲和力抗体优先反应。但稀释之后，高亲和力抗体的浓度会不断下降，直到体系中只剩下低亲和力抗体。当操作者用免疫分析、以不同抗血清的差异活性来比较抗原时，这类问题很重要：由于异质性抗体群的动态（各个抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分不同抗原的能力（Crowther, 2009）。

## 抗体的产生与免疫方式对检测选择的影响

应对抗原刺激产生抗体：多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->（Crowther, 2009）

passive immunization：直接打中和抗体；
active immunization：服用抗原，产生保护性抗体。

疫苗注射方式：sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型-isotype；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫：The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody（Crowther, 2009, p. 140）。即免疫分析的设计者必须决定，同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地反映疫苗接种的收益。

## 这些理论前提对 ELISA 设计的约束

把上面几条并起来看，它们指向同一个判断：ELISA 的读数并不直接等于「抗原有多少」或「抗体有多强」。

按表面积除以 20 估算出的结合位点数量只是上限，前提是全部表面都具有抗原性且分子达到最大结合，两者在实际体系中都很少成立。affinity 描述的是单个表位与单个 paratope 之间的相互作用，由非共价作用力和 K<sub>D</sub> 定义；avidity 描述的是抗体群与多个抗原位点之间的总结合能，除亲和力本身外还取决于价数和抗体-抗原的结构排布。两者不是同一件事，任何一处的替换都会改变体系的反应方式。

尤其需要留意的是稀释这一步。血清是异质性抗体群，稀释会优先移除高亲和力抗体，从而改变体系的 avidity，并影响其区分不同抗原的能力。因此用不同稀释度的血清去比较抗原活性，得到的差异未必来自抗原本身。

在免疫学一侧，抗体类型随免疫应答的时间进程变化，注射（sc/im）与口服/吸入途径诱导的 isotype 谱也不同；评估疫苗效果时，选择总抗体检测、isotype-specific 检测还是抗原清除检测，本身就是一个需要事先确定的问题。