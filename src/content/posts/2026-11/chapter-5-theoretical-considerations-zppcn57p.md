---
draft: true
reviewNotes:
  - "正文过短: 3186/13096=24% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,003 字符（原文 16,470，比例 18%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与亲合力"
date: 2026-11-12
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记梳理 ELISA 反应体系里几个决定信号的前提：抗原大小如何限制可结合的 Fab 数量、epitope 与 epitype 的界定、affinity 与 avidity 的区别与联系，以及免疫途径如何影响该测哪一类抗体。全文按「抗原—抗体—免疫应答」的顺序组织。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记梳理 ELISA 反应体系里几个决定信号的前提：抗原大小如何限制可结合的 Fab 数量、epitope 与 epitype 的界定、affinity 与 avidity 的区别与联系，以及免疫途径如何影响该测哪一类抗体。全文按「抗原—抗体—免疫应答」的顺序组织。

## 抗原大小如何限制可结合的 Fab 数量

分子越大，其复杂性也就越高。

Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量；

这个估算有明确前提。原文的表述是：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009, p. 127）——即假定整个表面都具有抗原性（这很少成立），且分子达到最大结合。

**应用**：“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”（Crowther, 2009, p. 127），也就是据此估算饱和某一试剂所需的抗体量，或把抗体结合水平作为可用表面的函数来测定。

## epitope、epitype 与 paratope：术语的边界

- **epitope**：antigenic site。
- **epitype**：抗原上的一个区域，由一组识别高度相似化学结构的密切相关抗体所界定（例如定义重叠或相互关联表位的 mAb）；可视为识别与同一抗原位点反应、但特异性略有差异的抗体的区域（Crowther, 2009, p. 128）。
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单点作用强度与总体结合强度

### affinity（结合亲和力）

原文给出三条并行的界定：

1. 单个 epitope 与 paratope 之间的能量；
2. 在单一结合位点上，抗原 epitope 与抗体 paratope 之间相互作用的强度；
3. 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

### avidity（亲合力，functional affinity）

1. 与抗原的总结合能。“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009, p. 130）。
2. 抗体在每个结合位点上总结合强度的度量，也称 functional affinity。
3. 三个影响因素：binding affinity、valency，以及抗体与抗原的结构排布。

## 血清的 avidity 不是常数：稀释会改变它

抗体分子与抗原决定簇之间的结合能称为亲和力。Avidity 则可以看作血清中所含异质性抗体与各种抗原位点（epitopes）之间所有不同亲和力的总和（Crowther, 2009, p. 137）。

正因为 avidity 是群体层面的量，血清的 avidity 在稀释时可能发生变化，因为操作者可能正在把某些抗体群体稀释掉。一个典型情形是：血清中同时存在少量对某复杂抗原的高亲和力抗体和大量低亲和力抗体。在血清未大幅稀释的免疫分析条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；而随着稀释，高亲和力抗体的浓度不断下降，直至体系中只剩低亲和力抗体。当用免疫分析比较不同抗血清与抗原的差异活性时，这类问题很重要——任何血清的稀释都可能影响其区分抗原的能力，取决于异质性抗体群体的动态，即各抗体分子的相对浓度与亲和力（Crowther, 2009, p. 137）。

## 免疫方式如何决定该测什么抗体

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

- **passive immunization**：直接注射中和抗体。
- **active immunization**：给予抗原，产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype），因此必须考虑：是用总抗体检测、isotype-specific assay，还是检测抗原清除的 assay 来评估疫苗接种效果。

对于口服/吸入免疫，问题更具体：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”（Crowther, 2009, p. 140）——即免疫分析工作者必须判断，针对 isotype-specific 抗体（尤其是 IgA）的检测是否比总抗体检测更能深入揭示疫苗接种的获益。

## 这些前提对方法设计的含义

把上述几条放在一起，可以对 ELISA 的设计边界做如下归纳：

- 按球形表面积除以单个 Fab 结合面积得到的位点数只是理论上限，它同时依赖「整个表面均具抗原性」和「分子达到最大结合」两个很少同时成立的假设，实际可结合位点数低于此值。
- affinity 描述的是单一 epitope–paratope 位点上的作用强度，由非共价作用与 K<sub>D</sub> 刻画；avidity 描述的是抗体群体对多个抗原位点的总体结合强度，受 binding affinity、valency 和结构排布三者共同影响。二者不能互相替代。
- 血清类样品的 avidity 随稀释而变，因为稀释会改变异质性抗体群体的组成。凡是用不同抗血清比较抗原差异活性、或在不同稀释度下判读结果的场合，都需要把这一点纳入考虑。
- 抗原刺激产生的是多克隆、非单一 isotype 的抗体应答，且不同免疫途径诱导的 isotype 谱不同，因此检测策略（总抗体、isotype-specific 还是抗原清除）必须在方法建立之初就确定下来。

尚未在笔记中展开的问题包括：上述表面积估算在何种抗原类型上偏离最大、以及如何在具体检测中定量刻画稀释对 avidity 的影响。