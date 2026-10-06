---
draft: true
reviewNotes:
  - "正文过短: 4843/13096=37% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,926 字符（原文 16,470，比例 30%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与免疫应答"
date: 2026-10-06
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "本篇整理 ELISA 及其它免疫检测所依赖的几个理论前提：抗原大小与可结合的 Fab 位点数、表位—表位型—互补位的定义、亲和力与亲合力的区别、血清稀释带来的影响，以及免疫方式与 isotype 如何决定该用哪种检测来评价疫苗效果。这些内容不涉及具体操作，但它们决定了抗体用量估算"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

本篇整理 ELISA 及其它免疫检测所依赖的几个理论前提：抗原大小与可结合的 Fab 位点数、表位—表位型—互补位的定义、亲和力与亲合力的区别、血清稀释带来的影响，以及免疫方式与 isotype 如何决定该用哪种检测来评价疫苗效果。这些内容不涉及具体操作，但它们决定了抗体用量估算、稀释方案设计和数据解释的边界。

## 抗原大小与可结合的 Fab 位点数量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009）
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

也就是说，这个数字只是在上述两个前提成立时的上限。它的应用在于两件事：计算饱和某一试剂所需的抗体量，或测定抗体结合量随可用表面的变化——

> “calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”（Crowther, 2009）

## 表位、表位型与互补位

epitope（表位）即 antigenic site。

**Epitype（表位型）** 指的是一组化学结构非常相似的抗体所识别的抗原区域，例如定义重叠或相互关联表位的 mAb；也可以把它理解为识别同一抗原位点、但特异性略有差异的抗体所对应的区域：

> “An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009）
> 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

**paratope（互补位）**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一位点强度与整体结合强度

### affinity（亲和力）

亲和力有三层相互对应的界定：

1. 单个 epitope 与 paratope 之间的能量；
2. 亲和力是抗原表位与抗体互补位在单一位点上相互作用的强度；
3. 亲和力由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡解离常数（K_D）定义。

另有一处等价表述：

> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.”（Crowther, 2009）
> 抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity（亲合力）

avidity 描述的是与抗原的整体结合能，即抗体在每一个结合位点上总结合强度，也称 functional affinity（功能性亲和力）：

> “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009）

它受三个因素影响：the binding affinity、valency，以及 the structural arrangement of the antibody and antigen in question。

对于血清这类异质性体系，亲合力可以看作是其中各抗体与各种抗原位点（表位）之间所有不同亲和力的总和：

> “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”（Crowther, 2009）
> 亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

## 稀释为什么会改变血清的亲合力

> “It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”（Crowther, 2009）
> 重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释掉某些群体的抗体。

这一点在异质性抗体群中尤其明显。设想一份血清中同时存在少量高亲和力抗体和大量低亲和力抗体：在血清未被大幅稀释的免疫检测条件下，两类抗体竞争抗原位点，高亲和力抗体会优先反应；稀释后，高亲和力抗体的浓度不断下降，最终只剩下低亲和力抗体。

> “As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).”（Crowther, 2009）

因此，当操作者用免疫检测、借助不同抗血清的活性差异来比较抗原时，稀释倍数本身就是一个变量：任何血清的稀释都会通过异质性抗体群的动力学（各抗体分子的相对浓度与亲和力）影响其区分抗原的能力。

## 抗体从何而来：免疫方式与 isotype 对检测设计的影响

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\
（Crowther, 2009）

两种免疫思路需要区分：passive immunization 是直接给予中和抗体；active immunization 是给予抗原，使机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：评估疫苗接种效果时，究竟使用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。

口服/吸入免疫则把问题进一步聚焦到 isotype 上：

> “The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”（Crowther, 2009, p. 140）
> 免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 这些前提在解读数据时的边界

把上面几点归拢一下，它们共同划出了理论和数据解释的边界：

由球形表面积除以 20nm^2 得到的 Fab 位点数只是最大可能值，其成立前提是“整个表面都具有抗原性”和“分子达到最大结合”，而这两点很少为真，所以它更适合用来估算饱和所需的抗体量，或考察结合量随可用表面的变化，而不是当作真实表位数。

亲和力与亲合力是两个层次的概念：前者是单一位点上 epitope 与 paratope 之间的结合强度，以 K_D 描述，由非共价相互作用介导；后者是整体（功能性）结合强度，取决于各单个亲和力的总和，并受 affinity、valency 以及抗体—抗原结构排布影响。在血清这类异质性体系中，亲合力还会随稀释而改变——高亲和力与低亲和力抗体群体的相对比例会随着稀释发生变化，进而影响血清区分不同抗原的能力，因此用不同抗血清比较抗原时，稀释方案必须一并考虑。

免疫方式决定了评价指标的选择：sc/im 免疫可诱导多种 isotype，需要在总抗体检测、isotype-specific assay 与抗原清除检测之间做取舍；口服/吸入免疫则把问题具体化为 isotype-specific 抗体（尤其是 IgA）是否比总抗体提供更多信息。这些取舍在笔记中没有给出统一答案，需要按具体疫苗和评价目的判断。