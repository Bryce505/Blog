---
draft: true
reviewNotes:
  - "正文过短: 4772/13096=36% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,921 字符（原文 16,470，比例 30%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体 affinity 与 avidity"
date: 2026-09-24
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇整理 ELISA 检测背后的理论前提，包括抗原一侧的分子大小与表位定义，抗体一侧 affinity 与 avidity 的区别，以及免疫方式如何决定血清中抗体群体的组成。这些概念直接约束着抗体用量估算、稀释方案设计，以及疫苗免疫原性评价中检测项目的选择。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇整理 ELISA 检测背后的理论前提，包括抗原一侧的分子大小与表位定义，抗体一侧 affinity 与 avidity 的区别，以及免疫方式如何决定血清中抗体群体的组成。这些概念直接约束着抗体用量估算、稀释方案设计，以及疫苗免疫原性评价中检测项目的选择。

## 抗原分子大小与可结合位点数量的估算

分子越大，其复杂性也就越高。

Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

这一估算有明确的成立条件：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009)

即，这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。它描述的是理想情形，而非实际结合位点数。

估算的用途在于：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009)

## 表位、表位型与互补位

epitope 即 antigenic site；paratope 是抗体上结合抗原表位的部分。两者之间还有一个容易被忽略的中间概念——epitype：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009)

表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

## affinity 与 avidity：单点结合能与总体结合强度

**affinity** 指单一结合位点上的结合能：

> "the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site" (Crowther, 2009)

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009)

即抗体分子与抗原决定簇之间的结合能称为亲和力。affinity 由非共价相互作用介导：

> "Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K_D)" (Crowther, 2009)

**avidity** 是 functional affinity，即与抗原的总结合能：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009)

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009)

亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。测量的对象不同：The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity。

avidity 有三个影响因素：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

## 免疫方式决定血清中的抗体类型组成

应对抗原刺激产生抗体，得到的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

被动免疫（passive immunization）是直接给中和抗体；主动免疫（active immunization）是给抗原，由机体产生保护性抗体。

疫苗注射方式为 sc-皮下注射或 im-肌内注射，这种方式可以诱导产生多种抗体类型（isotype）；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫时：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)

免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 稀释会改变血清的表观 avidity

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009)

原因是血清中的抗体是异质群体，各亚群的浓度和 affinity 并不相同：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)." (Crowther, 2009)

## 这些前提对检测设计意味着什么

把上述几条放在一起，可以看出几个界：

用分子表面积除以 20 得到的 Fab 结合位点数是上限，前提是"整个表面都具有抗原性"且"分子最大结合"，两者在真实抗原上很少同时成立，因此该数值只能用于估算所需抗体量或描述抗体结合随可用表面的变化趋势。

术语层面需要区分三个层次：epitope 是抗原上的位点，paratope 是抗体上与之结合的部位，epitype 则是由一组识别相近化学结构的抗体（如重叠或关联表位的 mAb）所界定的区域。

定量层面需要区分 affinity 与 avidity：前者是单一结合位点的结合能，由非共价作用决定并以 K_D 表征；后者是总体结合强度，受 binding affinity、valency 以及抗体与抗原的结构排布三者共同影响。在血清这类异质体系中，avidity 是各抗体亚群 affinity 的总和，因而会随稀释而改变——高亲和力亚群被稀释掉之后，剩余的抗体在区分不同抗原时的能力也随之变化。用免疫学方法比较抗原在不同抗血清中的差异活性时，这一点尤其需要注意。

免疫途径则决定了 isotype 的分布，进而决定了评价疫苗接种效果时应当选择总抗体检测还是 isotype-specific 检测（尤其是 IgA），两种选择给出的信息深度并不相同。以上均为概念层面的约束；具体的稀释倍数、检测项目的取舍，仍需由具体实验体系确定。