---
draft: true
reviewNotes:
  - "正文过短: 4477/13096=34% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗体应答：多克隆性与抗体类型的时序']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,534 字符（原文 16,470，比例 28%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与免疫应答"
date: 2026-10-22
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "导读：这篇笔记整理的是 ELISA 在理论层面的几个前置概念：抗原的分子大小如何决定可结合位点的数量，epitope、epitype、paratope 的定义边界，affinity 与 avidity 的区别与构成，以及抗体应答类型与免疫途径如何反过来约束检测形式的选择。内容偏概"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

导读：这篇笔记整理的是 ELISA 在理论层面的几个前置概念：抗原的分子大小如何决定可结合位点的数量，epitope、epitype、paratope 的定义边界，affinity 与 avidity 的区别与构成，以及抗体应答类型与免疫途径如何反过来约束检测形式的选择。内容偏概念澄清，其中稀释对亲合力的影响单独成节，因为它直接关系到用免疫分析做抗原比较时的可靠性。

## 抗原性：分子大小决定表位的最大数量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）
>
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

也就是说，这个除法给出的是一个上界，而非实测值。它的用处在于反向推算：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009）

## epitope、epitype、paratope：三个容易混淆的术语

- **epitope**：antigenic site，即抗原上被抗体识别的位点。
- **paratope**：抗体上结合抗原表位的部分。
- **epitype**：抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）所识别。

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009）
>
> 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

## affinity 与 avidity：单一位点与整体结合强度

### affinity：单一位点的结合能

亲和力（binding affinity）在这个笔记里被反复界定，几个说法指向同一件事：单个 epitope 与 paratope 之间的结合能，作用范围限定在 singular binding site。其分子基础是非共价作用，包括氢键、静电作用、范德华力和疏水相互作用，并以平衡解离常数（K_D）来定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009）

### avidity：功能亲和力

亲合力（avidity）又称 functional affinity，衡量的是抗体在所有结合位点上的总结合强度，即与抗原结合的总能量。

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009）

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009）

它受三个因素影响：1）the binding affinity，2）valency，3）the structural arrangement of the antibody and antigen in question。

## 抗体应答：多克隆性与抗体类型的时序

机体应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\
> (Crowther, 2009)

## 稀释会改变亲合力，进而影响抗原鉴别

这是上一节概念最容易被忽略的推论：

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009）
>
> 重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释某些群体的抗体。

具体机制原文举了一个例子：血清中可能同时存在少量高亲和力抗体和大量低亲和力抗体；在稀释不大的免疫分析条件下，两者竞争抗原位点，高亲和力抗体优先反应；继续稀释后高亲和力抗体浓度下降，最终只剩低亲和力抗体。

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)."（Crowther, 2009）

因此当用免疫分析、以不同抗血清的差异活性来比较抗原时，血清稀释度本身就是变量之一，它会影响血清区分不同抗原的能力。

## 免疫方式决定检测形式的选择

被动免疫（passive immunization）是直接注射中和抗体；主动免疫（active immunization）则是接种抗原，由机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype），因此必须考虑用总抗体检测、isotype-specific assay，还是检测抗原清除，来评估疫苗接种效果。

口服或吸入免疫则引出更细的取舍：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）
>
> 免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 小结

这几个概念之间的关系可以概括为一条链条：分子大小与表面积限定了一个抗原最多能提供多少个表位（且只是一个上界）；单个表位与 paratope 的结合能由 affinity 描述，而血清中异质性抗体对所有表位的总体结合强度由 avidity 描述，后者取决于亲和力、价数和抗体与抗原的结构排布；抗体应答本身是多克隆的，isotype 随时间变化，免疫途径又会进一步塑造 isotype 的组成。由此得到的适用边界也很明确：表位数量的几何估算不能当作实测值；亲合力不是固定属性，稀释会改变血清中抗体群体的相对组成，从而改变亲合力乃至血清区分抗原的能力。笔记在这一点上停留于现象与警示，未给出对稀释效应进行校正的具体做法。