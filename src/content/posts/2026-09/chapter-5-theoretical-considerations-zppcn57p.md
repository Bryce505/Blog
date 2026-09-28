---
draft: true
reviewNotes:
  - "正文过短: 4782/13045=37% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,969 字符（原文 16,405，比例 30%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-09-28
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理的是 ELISA 检测背后的几个理论支点：抗原分子大小与可结合位点数量的关系、epitope / epitype / paratope 这组术语的界定、affinity 与 avidity 的区别，以及抗体产生方式对检测策略选择的影响。内容来自 Crowther《ELIS"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理的是 ELISA 检测背后的几个理论支点：抗原分子大小与可结合位点数量的关系、epitope / epitype / paratope 这组术语的界定、affinity 与 avidity 的区别，以及抗体产生方式对检测策略选择的影响。内容来自 Crowther《ELISA Guidebook》第 5 章，按「抗原 → 抗体结合强度 → 检测策略」的顺序组织。

## 抗原分子大小如何限定可结合位点的上限

分子越大，其复杂性也就越高。

Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量；

> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”

> 🔤这样的计算是基于整个表面具有抗原性(很少是真实的)和分子最大结合的事实🔤

（Crowther, 2009, p. 127）

也就是说，球形表面积除以 20 得到的是理论上限，而不是实际可结合位点数。这个估算的用途在于：

> “calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”

（Crowther, 2009, p. 127）

即用于推算饱和某种试剂所需的抗体量，或把抗体结合水平表示为可用表面积的函数。

## 表位、表位型与 paratope：三个术语的界定

- **epitope**：antigenic site；
- **epitype**：

> “An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”

> 🔤表位型是抗原上的一个区域，由一组化学结构非常相似的抗体(例如, mAbs ,它们定义重叠或相互关联的表位)识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域🔤

（Crowther, 2009, p. 128）

- **paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单价结合能与整体功能亲和力

### affinity（结合亲和力）

1. the energy between a single epitope and paratope;
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
3. Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K_D)；

### avidity（功能亲和力，functional affinity）

1. overall binding energy with an antigen；

> “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”

（Crowther, 2009, p. 130）

2. The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity；
3. **三个影响因素**：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question.

## 血清稀释为什么会改变 avidity 与抗原区分能力

> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.”

（Crowther, 2009, p. 136）🔤抗体分子与抗原决定簇之间的结合能称为亲和力。🔤

> “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”

（Crowther, 2009, p. 137）🔤亲和力可以看作是血清中包含的异质性抗体与各种抗原位点(抗原表位)之间所有不同亲和力的总和。🔤

既然 avidity 是异质性抗体群体的加和，稀释就会改变它：

> “It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”

（Crowther, 2009, p. 137）🔤重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释某些群体的抗体🔤

> “As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).”

（Crowther, 2009, p. 137）

## 抗体产生方式与检测策略的对应关系

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于IgG；抗体类型产生时间顺序见下图

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\
（Crowther, 2009）

- passive immunization：直接打中和抗体；
- active immunization：服用抗原，产生保护性抗体；
- 疫苗注射方式：sc-皮下注射或im-肌内注射；这种方式可以诱导产生多种抗体类型-isotype；必须考虑是否使用总抗体检测，isotype-specific assay或检测抗原清除的检测来评估疫苗接种效果；
- 口服/吸入免疫：

> “The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”

（Crowther, 2009, p. 140）🔤免疫学家必须决定同型抗体(特别是IgA )的检测是否能比总抗体的检测更深入地了解疫苗接种的好处🔤

## 这些理论前提在什么时候不成立

三处边界值得在使用时留意。

其一，由球形表面积推算 Fab 结合位点数的做法，前提是「整个表面具有抗原性」和「分子最大结合」，作者明确指出这两个前提很少成立，因此该数值只能当作上限，用来估算饱和所需的抗体量，而不能当作实测表位数。

其二，avidity 是异质性抗体群体中各亲和力的加和，血清稀释会改变这个群体构成；因此用免疫测定比较不同抗血清对不同抗原的差异活性时，稀释倍数本身就会影响区分能力。

其三，在疫苗接种评估中，究竟用总抗体检测、isotype-specific assay，还是检测抗原清除，是一个需要 assay 设计者事先决定的问题——这取决于想回答的是「有没有抗体」还是「抗体是否带来保护」。

笔记中未展开的部分是：这些项在具体检测体系（直接法、间接法、夹心法、竞争法）中如何转化为可执行的参数，属于滴定与优化环节的内容。