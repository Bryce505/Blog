---
draft: true
reviewNotes:
  - "正文过短: 3697/13096=28% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗体应答与抗体类型的产生']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,653 字符（原文 16,470，比例 22%）超出 9,058～15,646 字符的区间"
title: "ELISA 检测的理论基础：抗原性、抗体亲和力与抗体产生"
date: 2026-10-12
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理自 Crowther 关于 ELISA 理论的章节，从抗原分子的尺寸与表位容量讲起，界定 epitope、epitype、paratope 等术语，进而区分 affinity 与 avidity，最后落到抗体的产生方式及其对检测策略的影响。全文围绕一个问题展开：在 E"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理自 Crowther 关于 ELISA 理论的章节，从抗原分子的尺寸与表位容量讲起，界定 epitope、epitype、paratope 等术语，进而区分 affinity 与 avidity，最后落到抗体的产生方式及其对检测策略的影响。全文围绕一个问题展开：在 ELISA 中决定结合行为的参数究竟是什么，以及它们各自的适用边界。

## 抗原分子的尺寸与表位容量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。这种估算有其前提：「这样的计算是基于整个表面具有抗原性(很少是真实的)和分子最大结合的事实」(Crowther, 2009)。

### 估算结果的用途

这一计算可以用来 calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface (Crowther, 2009)。

## 术语界定：epitope、epitype 与 paratope

- **epitope**：antigenic site，即抗原表位。
- **epitype**：「表位型是抗原上的一个区域，由一组化学结构非常相似的抗体(例如, mAbs ,它们定义重叠或相互关联的表位)识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域」(Crowther, 2009)。
- **paratope**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单一位点与总体结合强度

### affinity

affinity（binding affinity）指单一结合位点上的作用强度：

1. the energy between a single epitope and paratope;
2. the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site;
3. Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K<sub>D</sub>);

「抗体分子与抗原决定簇之间的结合能称为亲和力。」(Crowther, 2009)

### avidity

avidity 又称 functional affinity：

1. overall binding energy with an antigen;「The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites」(Crowther, 2009);
2. The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity;
3. 影响因素有三：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question.

「亲和力可以看作是血清中包含的异质性抗体与各种抗原位点(抗原表位)之间所有不同亲和力的总和。」(Crowther, 2009)

## 血清稀释会改变 avidity，进而影响对抗原的判别

「重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释某些群体的抗体」(Crowther, 2009)。

以一个血清样本为例：其中可能含有「a low quantity of antibodies showing high affinity」for a particular complex antigen and「a high quantity of low-affinity antibody」. Under immunoassay conditions in which that serum is「not diluted greatly」, we would have competition for antigenic sites between the high- and low-affinity antibodies, and「the high-affinity antibodies would react preferentially」. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies.「Such problems are important」when an operator is using immunoassays to「compare antigens by their differential activity with different antisera」.「The dilution of any serum can affect its ability to discriminate between antigens」owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules). (Crowther, 2009)

## 抗体应答与抗体类型的产生

应对抗原刺激产生抗体，产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 免疫途径与检测策略的选择

passive immunization：直接打中和抗体；
active immunization：服用抗原，产生保护性抗体；

疫苗注射方式：sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型-isotype；必须考虑是否使用总抗体检测，isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫则涉及另一层判断：「免疫学家必须决定同型抗体(特别是 IgA)的检测是否能比总抗体的检测更深入地了解疫苗接种的好处」(Crowther, 2009)。

## 这些理论参数对检测设计的约束

综合来看，以上概念构成了 ELISA 设计的约束条件。以表面积除以 20 估算 Fab 结合位点数量时，需同时接受「整个表面具有抗原性」与「分子最大结合」两个前提，而这两者在实际抗原上很少同时成立 (Crowther, 2009)。血清的 avidity 会随稀释改变，因此当操作者用免疫测定比较不同抗血清对同一抗原的差异活性时，稀释倍数本身就会影响判别能力 (Crowther, 2009)。在评估疫苗接种效果时，是采用总抗体检测、isotype-specific assay 还是抗原清除检测，取决于所关注的抗体类型，尤其是经黏膜途径产生的 IgA (Crowther, 2009)。这些边界条件决定了理论估算与实际检测之间始终存在的差距。