---
draft: true
reviewNotes:
  - "正文过短: 5110/13096=39% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗体应答的多克隆性质与 isotype 顺序']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 5,304 字符（原文 16,470，比例 32%）超出 9,058～15,646 字符的区间"
title: "ELISA 检测的理论基础：抗原表位、抗体亲和力与血清稀释效应"
date: 2026-09-26
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量表现，最终取决于抗原与抗体两侧的分子性质。这篇整理抗原分子大小与 Fab 可结合位点数目的估算方式，epitope、epitype、paratope 等术语的界定，affinity 与 avidity 的区别及其影响因素，并说明免疫应答中抗体类型的产生顺序以及血"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量表现，最终取决于抗原与抗体两侧的分子性质。这篇整理抗原分子大小与 Fab 可结合位点数目的估算方式，epitope、epitype、paratope 等术语的界定，affinity 与 avidity 的区别及其影响因素，并说明免疫应答中抗体类型的产生顺序以及血清稀释对亲合力的影响。内容以 Crowther 的论述为线索，只涉及检测设计绕不开的前提与边界。

## 抗原分子大小与 Fab 结合位点数目的估算

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" —— 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。(Crowther, 2009, p. 127)

这一估算的用途有两个方向："calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009, p. 127)。

需要留意的是，整个表面都具有抗原性、且分子达到最大结合，这两个前提在真实体系中很少同时成立，因此由表面积除以 20 得到的只是位点数目的上限。

## epitope、epitype 与 paratope：术语层面的区分

三个术语分别指向抗原侧、抗原侧的抗体群体、以及抗体侧：

- **epitope**：antigenic site；
- **epitype**："An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" —— 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。(Crowther, 2009, p. 128)
- **paratope**：抗体上结合抗原表位的部分。

epitope 与 epitype 的差别在于讨论的对象：前者是抗原上的一个位点，后者是一组识别高度相似化学结构的抗体所界定的区域，允许其中各成员的特异性略有出入。

## affinity 与 avidity：结合强度的两个层面

### affinity（binding affinity）

1. the energy between a single epitope and paratope；
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
3. Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K_D)。

affinity 落在单个结合位点的尺度上，由非共价作用提供，并以平衡解离常数 K_D 表征。

### avidity（functional affinity）

1. overall binding energy with an antigen；"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009, p. 130)；
2. The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity；
3. 三个影响因素：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question。

avidity 是各结合位点总结合强度的度量，也称功能亲和力，由 binding affinity、valency 以及抗体与抗原的结构排布三者共同决定。

## 抗体应答的多克隆性质与 isotype 顺序

应对抗原刺激产生抗体，得到的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

(Crowther, 2009)

## 血清稀释为什么会改变亲合力

同一对概念在抗体章节中再次给出，落点更靠近检测操作：

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." —— 抗体分子与抗原决定簇之间的结合能称为亲和力。(Crowther, 2009, p. 136)

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" —— 亲和力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。(Crowther, 2009, p. 137)

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" —— 重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释某些群体的抗体。(Crowther, 2009, p. 137)

对血清而言，avidity 不是单一常数，而是异质抗体群体中各亲和力组分的总和，因此稀释本身就会改写这个总和：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)." (Crowther, 2009, p. 137)

也就是说，用不同抗血清比较抗原时，稀释度是一个会影响结论的变量，而非可以随意选定的操作参数。

## 主动免疫与被动免疫：检测项目的选择

- passive immunization：直接打中和抗体；
- active immunization：服用抗原，产生保护性抗体。

疫苗注射方式：sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型-isotype；必须考虑是否使用总抗体检测，isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫途径下，检测项目的选择更为直接："The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" —— 免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。(Crowther, 2009, p. 140)

## 适用范围与未展开的部分

以上内容覆盖的是抗原—抗体识别这一层：位点数目估算只在「整个表面均有抗原性」和「分子最大结合」两个理想假设下成立，因此结果应视为上限；affinity 描述单位点能量并以 K_D 表征，avidity 描述群体层面的总结合强度，受 binding affinity、valency 与结构排布三者共同影响；血清作为异质抗体群体，其 avidity 会随稀释而改变，用不同抗血清比较抗原时稀释度必须作为变量对待；免疫途径决定所产生的 isotype 谱，进而决定评估疫苗接种效果时是采用总抗体检测还是 isotype-specific assay。

酶反应动力学与浓度—反应关系属于检测的另一层，本篇没有涉及；上述概念如何在具体定量方法中折算，也需要结合相应的方法学内容另行讨论。