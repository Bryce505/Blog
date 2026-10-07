---
draft: true
reviewNotes:
  - "正文过短: 4549/13045=35% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,611 字符（原文 16,405，比例 28%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与亲合力"
date: 2026-10-07
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的读数最终由抗原与抗体之间的结合行为决定。这篇笔记从抗原侧（分子大小与可结合位点数的估算、表位与表位型的界定）和抗体侧（亲和力与亲合力的区别、免疫方式对所产生的抗体类型的影响）两方面整理了这一方法学的理论基础，并交代这些概念在解释数据时的适用边界。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的读数最终由抗原与抗体之间的结合行为决定。这篇笔记从抗原侧（分子大小与可结合位点数的估算、表位与表位型的界定）和抗体侧（亲和力与亲合力的区别、免疫方式对所产生的抗体类型的影响）两方面整理了这一方法学的理论基础，并交代这些概念在解释数据时的适用边界。

## 抗原性的大小考量：可结合位点数的上限估算

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20 nm²，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个结果是一个上限而非真实值：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p. 127）

即：这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

在方法设计上，这类估算的用途是 "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009, p. 127）。

## 表位、表位型与互补位：几个易混术语的界定

抗原侧的基本术语是 epitope，即 antigenic site。与之相邻、容易混淆的是 Epitype：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009, p. 128）

表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

抗体一侧的对应术语是 paratope，即抗体上结合抗原表位的部分。

## 亲和力与亲合力：两个不同层次的结合强度

### 亲和力（affinity）

亲和力指向单个结合位点：

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009, p. 136）

抗体分子与抗原决定簇之间的结合能称为亲和力。它包含三层含义：其一，是单个 epitope 与 paratope 之间的能量；其二，是单一结合位点上抗原表位与抗体互补位之间相互作用的强度；其三，这种作用由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

### 亲合力（avidity）

亲合力又称功能性亲和力（functional affinity），指抗体与抗原的总体结合能。在血清这样的异质体系中：

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009, p. 137）

亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

而在抗体群体水平上：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009, p. 130）

换言之，在每一个结合位点上衡量抗体的总结合强度时，用的量是亲合力；它同时受三个因素影响：结合亲和力、价数（valency），以及抗体与抗原的结构排布（the structural arrangement of the antibody and antigen in question）。

## 稀释会改变血清的亲合力，也会改变其区分抗原的能力

亲合力不是血清的固有常数：

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009, p. 137）

重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释某些群体的抗体。

其机制在于血清中不同亲和力抗体的相对丰度差异：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)."（Crowther, 2009, p. 137）

也就是说：在稀释倍数不大的条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；随着稀释推进，高亲和力抗体被逐步稀释掉，体系最终只剩低亲和力抗体。当用免疫分析比较不同抗血清与抗原的差异活性时，这一问题尤其重要——任何血清的稀释都可能影响其区分抗原的能力。

## 抗体的产生方式决定了检测策略

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

被动免疫（passive immunization）是直接给予中和抗体；主动免疫（active immunization）则是给予抗原，由机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：评估疫苗接种效果时，究竟采用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。对口服/吸入免疫这一情形，问题更为具体：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）

免疫分析工作者必须判断，同型特异性抗体（特别是 IgA）的检测是否比总抗体检测更能深入反映疫苗接种的收益。

## 这些概念的适用边界

把上述内容放在一起看，几条边界值得记住：

第一，由分子表面积推算 Fab 结合位点数，前提是"整个表面都具有抗原性"且"分子达到最大结合"，这两个前提在真实抗原上极少同时成立，因此结果只能当作上限。

第二，亲和力描述单一结合位点，亲合力描述异质抗体群体的总体结合能，二者不可互换使用；亲合力还取决于价数与抗体—抗原的结构排布。

第三，血清的亲合力随稀释而改变，因而会改变其区分不同抗原的能力。这意味着用免疫分析做抗原比较时，稀释方案本身就是一个变量，而不是可以随意调整的操作细节。

第四，抗体的产生方式（主动/被动免疫、sc 或 im 注射、口服或吸入）决定了抗体类型的组成，进而决定评估疫苗效果时应选择总抗体检测、isotype-specific assay 还是抗原清除检测。

本文只处理抗原侧与抗体侧的结合理论；酶反应动力学与浓度—反应关系属于同一主题下另外的环节，此处不展开。