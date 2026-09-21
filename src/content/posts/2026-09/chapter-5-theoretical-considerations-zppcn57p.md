---
draft: true
reviewNotes:
  - "正文过短: 4641/13045=36% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,731 字符（原文 16,405，比例 29%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-09-21
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本文整理 ELISA 体系设计中几个绕不开的基础理论问题：抗原尺寸与可结合位点数量的关系、表位（epitope）与表位型（epitype）的定义、亲和力（affinity）与亲合力（avidity）这对概念的区别，以及抗体的产生方式如何反过来决定检测策略的选择。这些内容不涉及具体"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本文整理 ELISA 体系设计中几个绕不开的基础理论问题：抗原尺寸与可结合位点数量的关系、表位（epitope）与表位型（epitype）的定义、亲和力（affinity）与亲合力（avidity）这对概念的区别，以及抗体的产生方式如何反过来决定检测策略的选择。这些内容不涉及具体操作步骤，但直接决定了抗体用量估算、稀释方案设计和结果解释的边界。

## 抗原尺寸如何决定可结合位点数量的上限

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有明确的前提，Crowther 对此的表述是：

> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally” (Crowther, 2009)

这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

尽管前提苛刻，该计算仍有实际用途：可以据此估算饱和某一试剂所需的抗体量，或者测定抗体结合水平随可用表面变化的函数关系——

> “calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface” (Crowther, 2009)

## 表位、表位型与 paratope：三个不能混用的定义

**epitope** 即 antigenic site，是抗原上被抗体识别的位点。

**Epitype** 是一个容易被忽略的中间层次：

> “An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site” (Crowther, 2009)

表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

**paratope** 则是抗体一侧，即抗体上结合抗原表位的部分。

这三个术语分别落在抗原表面、一组抗体的识别范围、以及抗体自身结构上，在描述抗体配对和表位竞争关系时如果混用，会直接导致对实验结果的误读。

## 亲和力：单一结合位点上的相互作用强度

affinity（binding affinity）在笔记中给出了三层含义：

1. 单个 epitope 与 paratope 之间的能量；
2. 在**单一结合位点**上，抗原 epitope 与抗体 paratope 之间相互作用的强度；
3. 亲和力由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并由**平衡解离常数（K<sub>D</sub>）**定义。

Crowther 对此的概括是：

> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.” (Crowther, 2009)

抗体分子与抗原决定簇之间的结合能称为亲和力。

## 亲合力：多价结合的总体强度，以及稀释带来的偏移

avidity 又称 functional affinity（功能性亲和力）：

1. 与抗原结合的总能量；
2. 抗体在每个结合位点上总结合强度的量度；
3. 三个影响因素：the binding affinity，valency，以及 the structural arrangement of the antibody and antigen in question。

关于 avidity 的两种表述：

> “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites” (Crowther, 2009)

> “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)” (Crowther, 2009)

亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

这里有一个在方法设计上后果直接的推论：

> “It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies” (Crowther, 2009)

重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释掉某些群体的抗体。Crowther 给出的情形值得完整引用：

> “As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).” (Crowther, 2009)

也就是说，血清稀释倍数本身就是一个会改变抗体群体构成的变量，用它来比较不同抗原的差异活性时需要格外小心。

## 抗体如何产生：免疫方式决定该测什么

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；各抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

被动免疫（passive immunization）是直接给予中和抗体；主动免疫（active immunization）是给予抗原、由机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）。因此在评估疫苗接种效果时，必须考虑是使用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。

口服或吸入免疫则引出另一个选择问题：

> “The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody” (Crowther, 2009)

即同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地反映疫苗接种的收益。

## 这些前提在方法设计中的位置

把上述内容归拢起来，可以落到三点边界上。

第一，基于球形表面积除以 20nm^2 得到的 Fab 结合位点数只是一个理论上限，它的两个前提——整个表面都具有抗原性、以及分子达到最大结合——在实践中很少同时成立，因此该数值只能用于估算抗体需求量的量级，不能当作实际结合容量。

第二，affinity 描述的是单一结合位点的结合能，avidity 描述的是多价、多克隆情形下的总结合强度，两者在数值上不可互相替代；avidity 由 binding affinity、valency 和抗体-抗原的结构排布共同决定。

第三，由于血清或抗血清是异质性抗体群体，稀释会改变群体组成，从而改变其 apparent avidity 和区分不同抗原的能力。

尚未解决、或者说需要个案判断的问题是：在主动免疫的效果评价中，总抗体、isotype-specific 抗体（尤其是 IgA）与抗原清除三者之间该如何取舍，笔记本身也只是把这个选择作为一个必须由实验者作出的决定提出来，没有给出通用答案。