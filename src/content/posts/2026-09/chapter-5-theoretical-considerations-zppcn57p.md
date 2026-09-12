---
draft: true
reviewNotes:
  - "正文过短: 3311/13096=25% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,225 字符（原文 16,470，比例 20%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与亲合力"
date: 2026-09-12
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量表现最终受制于抗原本身的性质和抗体的结合特性。这篇笔记整理了 Crowther 在 ELISA 理论部分给出的几组基础概念：抗原分子大小与可及表位数量的关系，epitope／epitype／paratope 的定义，affinity 与 avidity 的区别，"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量表现最终受制于抗原本身的性质和抗体的结合特性。这篇笔记整理了 Crowther 在 ELISA 理论部分给出的几组基础概念：抗原分子大小与可及表位数量的关系，epitope／epitype／paratope 的定义，affinity 与 avidity 的区别，以及免疫应答产生的抗体类型如何反过来决定检测方案的选择。最后一节讨论异质性抗体群体在稀释条件下的行为差异。

## 抗原分子的大小与可结合 Fab 位点的上限

分子越大，其复杂性也就越高；Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

这个估算成立有两个前提，需要一并记住：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）

在实际使用中，这类计算可以回答两类问题：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"

## 表位、表位型与 paratope 的定义

- **epitope**：antigenic site；
- **paratope**：抗体上结合抗原表位的部分；
- **Epitype**：抗原上由一组化学结构非常相似的抗体所识别的区域。

Epitype 的原文定义是：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"

## 亲和力与亲合力：单一位点强度与总体结合强度

### affinity（结合亲和力）

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."

笔记中给出三条并列的界定：一是单个 epitope 与 paratope 之间的能量；二是抗原 epitope 与抗体 paratope 在单一结合位点上的相互作用强度；三是这种相互作用由非共价作用介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡解离常数（K_D）来定义。

### avidity（亲合力，functional affinity）

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"

即抗体在所有结合位点上总结合强度的量度，也称 functional affinity。它由三个因素决定：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question.

## 免疫应答产生的抗体类型与检测方案的选择

机体应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\
（Crowther, 2009）

两类免疫方式需要区分：passive immunization 是直接给予中和抗体；active immunization 是给予抗原，由机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑究竟采用总抗体检测、isotype-specific assay，还是检测抗原清除的 assay 来评估疫苗接种效果。口服或吸入免疫途径则另有侧重：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）

## 稀释会改变血清的表观亲合力

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"

原文给出的典型情形是：一份血清中可能同时存在少量高亲和力抗体和大量低亲和力抗体。在稀释倍数不大的免疫检测条件下，高、低亲和力抗体会竞争抗原位点，而高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度被稀释掉，最后只剩下低亲和力抗体。当操作者用免疫检测、以不同抗血清的差异活性来比较抗原时，这类问题尤其重要——血清的稀释会影响其区分不同抗原的能力，原因就在于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力）。

## 小结

这几组概念共同构成了 ELISA 的边界条件：

- Fab 结合位点数目的估算，建立在"整个表面都具有抗原性"且"分子以最大方式结合"这两个前提上，而前者很少是真实情况；
- affinity 描述的是单个 epitope 与 paratope 之间的结合能，avidity 描述的是血清中异质性抗体与各个抗原位点结合能的汇总，两者不能互换使用；
- avidity 受结合亲和力、价数以及抗体与抗原的结构排布三者共同影响；
- 血清一经稀释，其中的抗体群体组成可能改变，进而改变其区分抗原的能力。

因此，凡是涉及抗血清比较、稀释系列设计或抗体类型选择的实验，都需要回到上述前提来判断结论是否成立。