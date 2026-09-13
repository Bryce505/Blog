---
draft: true
reviewNotes:
  - "正文过短: 4604/13096=35% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗原刺激后的抗体应答：多克隆性与同种型']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,723 字符（原文 16,470，比例 29%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原尺寸、affinity/avidity 与抗体应答的检测选择"
date: 2026-09-13
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理自 ELISA 的理论章节，回答四个问题：抗原分子的大小如何决定可结合位点的数量上限；epitope、epitype 与 paratope 这些术语各自指什么；affinity 与 avidity 分别描述哪一层级的结合强度、受哪些因素影响；以及抗原刺激或接种之后，抗"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理自 ELISA 的理论章节，回答四个问题：抗原分子的大小如何决定可结合位点的数量上限；epitope、epitype 与 paratope 这些术语各自指什么；affinity 与 avidity 分别描述哪一层级的结合强度、受哪些因素影响；以及抗原刺激或接种之后，抗体的多克隆性与同种型构成如何决定检测方案的选择。论述以 Crowther (2009) 的原文判断为准，其中的定量估算与前提限定一并保留。

## 抗原尺寸与可结合位点数：一个上限估算

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20 nm²，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算依赖两个前提，Crowther 明确指出它们通常并不成立：

> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”
>
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。
>
> —— Crowther, 2009, p. 127

即便只是上限，它仍有实用价值：可以用来计算饱和某一试剂所需的抗体量，或者测量抗体结合水平随可用表面的变化 —— “calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”（Crowther, 2009, p. 127）。

## 表位、表位型与 paratope

epitope 即 antigenic site；paratope 是抗体上结合抗原表位的部分。

epitype 的层级与之不同：它不是一个单一的化学位点，而是一组化学结构高度相似的抗体所共同识别的区域。

> “An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”
>
> 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。
>
> —— Crowther, 2009, p. 128

## affinity 与 avidity：单一结合强度与整体结合强度

affinity（结合亲和力）可以从三个角度界定：它是单个 epitope 与 paratope 之间的能量；它是抗原 epitope 与抗体 paratope 在单一结合位点（at a singular binding site）上相互作用的强度；这种作用由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.”
>
> 抗体分子与抗原决定簇之间的结合能称为亲和力。
>
> —— Crowther, 2009, p. 136

avidity（亲合力，即 functional affinity）描述的是另一个层级：它是与抗原结合的总能量，是抗体在每一个结合位点上结合强度的总和度量。

> “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”
>
> —— Crowther, 2009, p. 130

> “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”
>
> 亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。
>
> —— Crowther, 2009, p. 137

影响 avidity 的因素有三个：binding affinity、valency，以及抗体与抗原自身的 structural arrangement。

## 血清稀释会改变 avidity

avidity 不是血清的固定属性，稀释本身就会改变它：

> “It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”
>
> 重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释某些群体的抗体。
>
> —— Crowther, 2009, p. 137

原文用高、低亲和力抗体共存的情形说明后果：

> “As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).”
>
> —— Crowther, 2009, p. 137

也就是说，当用免疫测定比较不同抗血清对同一抗原的差异活性时，稀释倍数本身就是一个变量，因为它改变了异质性抗体群中各抗体分子的相对浓度与亲和力构成。

## 抗原刺激后的抗体应答：多克隆性与同种型

应对抗原刺激，机体产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 免疫接种背景下的检测策略选择

passive immunization：直接注射中和抗体；active immunization：给予抗原，产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫则涉及另一层判断：

> “The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”
>
> 免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。
>
> —— Crowther, 2009, p. 140

## 小结：这些概念的适用边界

尺寸估算给出的是 Fab 结合位点数的理论最大数量，其前提——整个表面具有抗原性、分子结合达到最大——在现实中很少成立，因此它只能用于估算饱和所需的抗体量，或刻画抗体结合随可用表面的变化，不能当作实际表位数。

affinity 与 avidity 处于不同层级：前者描述单一结合位点，后者描述异质性抗体群与多表位抗原之间的整体结合，并受 binding affinity、valency 和结构排布三者影响；更重要的是，avidity 会随血清稀释而改变，所以用免疫测定比较不同抗血清的差异活性时，稀释倍数本身就是一个必须交代的变量。

抗原刺激产生的是多克隆、多 isotype 的抗体应答，免疫途径（sc/im，或口服/吸入）决定了应当在总抗体检测、isotype-specific 检测与抗原清除检测之间如何取舍。至于摘要中提到的酶反应动力学与浓度-反应关系，本篇笔记正文并未展开。