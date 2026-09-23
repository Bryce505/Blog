---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['135']"
  - "正文过短: 4615/13096=35% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 5,281 字符（原文 16,470，比例 32%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、表位定义与亲和力/avidity 的区分"
date: 2026-09-23
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理 ELISA 检测理论基础的几个核心概念：抗原分子大小与 Fab 结合位点数量的关系、epitope / epitype / paratope 的定义边界，以及 affinity 与 avidity 这两个常被混用的结合强度指标。后半部分讨论抗体的产生方式与免疫途径如"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理 ELISA 检测理论基础的几个核心概念：抗原分子大小与 Fab 结合位点数量的关系、epitope / epitype / paratope 的定义边界，以及 affinity 与 avidity 这两个常被混用的结合强度指标。后半部分讨论抗体的产生方式与免疫途径如何影响检测方案的设计。内容取自 Crowther《The ELISA Guidebook》第 5 章的理论部分。

## 抗原越大越复杂，Fab 结合位点数的上限怎么估

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）

即：这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

### 这个估算能用来做什么

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009, p. 127）

也就是说，可以据此估算饱和某种试剂所需的抗体量，或测量抗体结合水平与可用表面积之间的关系。

## epitope、epitype 与 paratope：三个容易混淆的定义

- **epitope**：antigenic site。
- **paratope**：抗体上结合抗原表位的部分。
- **Epitype**：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009, p. 128）

表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

## affinity 与 avidity：单一位点的结合能与整体结合强度

### affinity（结合亲和力）

1. the energy between a single epitope and paratope；
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
3. Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K<sub>D</sub>)；

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009, p. 136）

抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity（功能性亲和力，functional affinity）

1. overall binding energy with an antigen；

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009, p. 130）

2. The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity；

3. 三个影响因素：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009, p. 137）

亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

## 稀释会改变血清的 avidity：异质性抗体群体的竞争

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009, p. 137）

原文给出的例子（Crowther, 2009, p. 137）：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)."

这段话的要点是：血清中低浓度高亲和力抗体与高浓度低亲和力抗体并存时，在稀释不大的免疫分析条件下，二者竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度被稀释掉，最后只剩低亲和力抗体。当操作者用免疫分析比较不同抗血清对同一抗原的差异活性时，这类问题尤其需要注意——任何血清的稀释都可能影响其区分不同抗原的能力，原因在于异质性抗体群体的动力学（各抗体分子的相对浓度与亲和力）。

## 抗体的产生方式与免疫途径如何影响检测方案

### 抗原刺激后产生的是多克隆抗体

应对抗原刺激产生抗体，为多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->（Crowther, 2009, p. 135）

### 被动免疫与主动免疫

- passive immunization：直接打中和抗体；
- active immunization：服用抗原，产生保护性抗体。

### 免疫途径决定需要检测哪一类抗体

疫苗注射方式：sc—皮下注射或 im—肌内注射；这种方式可以诱导产生多种抗体类型（isotype）；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）

免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 这些理论概念的适用边界

把上述内容放在一起，可以得到几点使用上的边界：

- 由球形表面积除以 20nm^2 得到的表位数量只是一个上限，它建立在「整个表面都具有抗原性」和「分子以最大数量结合」这两个前提上，而原文明确指出这两个前提很少成立。
- affinity 描述的是单个 epitope 与 paratope 之间的相互作用，由氢键、静电作用、范德华力和疏水作用等非共价作用介导，用平衡解离常数 K<sub>D</sub> 表征；avidity 则是功能性亲和力，取决于 affinity、价数以及抗体与抗原的结构排布三项因素。
- avidity 是群体层面的量。由于血清中抗体群体本身是异质的，稀释会改变群体的组成，因此用免疫分析比较抗原或比较不同抗血清时，稀释条件必须固定，否则比较结果会被群体动力学干扰。
- 疫苗接种效果的评估方式（总抗体、isotype-specific 抗体，或抗原清除）需要结合免疫途径来选，注射途径与口服/吸入途径诱导的 isotype 谱不同。
- 本笔记摘要中提到的酶反应动力学与浓度-反应关系，正文部分没有展开；抗体类型产生的时间顺序也只以图片形式给出，未在文字中列出具体时间点。