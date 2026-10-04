---
draft: true
reviewNotes:
  - "正文过短: 4813/13045=37% < 40%"
  - "空壳章节（正文不足 120 字）: ['抗原刺激后的抗体应答：多克隆与抗体类型']"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,956 字符（原文 16,405，比例 30%）超出 9,023～15,585 字符的区间"
title: "ELISA 检测的理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-10-04
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 及同类免疫检测的表现，最终取决于抗原、抗体以及两者相互作用这三方面的理化性质。本篇围绕抗原尺寸与表位数量估算、表位相关术语、亲和力（affinity）与亲合力（avidity）的区分，以及抗原刺激和免疫接种后抗体应答的特点，整理 Crowther《The ELISA "
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 及同类免疫检测的表现，最终取决于抗原、抗体以及两者相互作用这三方面的理化性质。本篇围绕抗原尺寸与表位数量估算、表位相关术语、亲和力（affinity）与亲合力（avidity）的区分，以及抗原刺激和免疫接种后抗体应答的特点，整理 Crowther《The ELISA Guidebook》第 5 章中的若干基础概念。这些概念直接决定抗体用量估算、血清稀释策略和疫苗效果评价方式的选择。

## 抗原尺寸、复杂度与表位数量的估算

分子越大，其复杂性也就越高。Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算带有明确的前提：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"

即它建立在「整个表面都具有抗原性（这很少成立）」和「分子以最大方式结合」这两个假设之上。引用时不宜把算出的位点数当作实测值。

在应用层面，可以据此 "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009, p. 127)。

## 表位、表位型与互补位的界定

epitope：antigenic site，即抗原上的抗原位点。

Epitype 是一个与之相关但不同的概念：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"

也就是说，表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别；可视为识别与同一抗原位点反应的、特异性略有不同的抗体的区域。

paratope：抗体上结合抗原表位的部分，与 epitope 互为结合对。

## 亲和力与亲合力：从单一结合位点到总体结合强度

### affinity 与 avidity 的界定

affinity（binding affinity）描述的是单一结合位点层面的相互作用强度：

- the energy between a single epitope and paratope；
- the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site；
- Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K_D)；

即亲和力由非共价相互作用（氢键、静电作用、范德华力、疏水相互作用）介导，并以平衡解离常数 K_D 表征。Crowther 把它概括为 "The binding energy between an antibody molecule and an antigen determinant is termed affinity" (Crowther, 2009, p. 136)。

avidity（functional affinity）则描述总体结合强度：the measure of the total binding strength of an antibody at every binding site is termed avidity，又称 functional affinity。

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009, p. 137)

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009, p. 130)

### 亲合力的三个影响因素

1）the binding affinity，2）valency，3）the structural arrangement of the antibody and antigen in question。

这一条决定了：单看 K_D 不足以推断检测体系中的实际结合表现，价态与分子排布同样参与其中。

### 稀释如何改变血清亲合力与抗原区分能力

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009, p. 137)

Crowther 给出的说明（p. 137）是：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)."

也就是说，同一份血清在不同稀释度下的区分能力可能不同，稀释本身就是一个会改变体系组成变量的操作。

## 抗原刺激后的抗体应答：多克隆与抗体类型

机体应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

## 免疫接种途径与疫苗评价中的检测选择

被动免疫（passive immunization）是直接给予中和抗体；主动免疫（active immunization）是给予抗原，使机体产生保护性抗体，两者在检测设计上的含义不同。

疫苗接种方式通常为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype），因此必须考虑采用总抗体检测、isotype-specific assay，还是检测抗原清除，来评估疫苗接种效果。

口服或吸入免疫则涉及黏膜免疫途径：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)

这里要决定的是：同型抗体（尤其是 IgA）的检测，是否比总抗体检测更能反映疫苗接种带来的收益。

## 结语

把上述内容串起来，可以看到一条从抗原到检测信号的概念链：抗原尺寸决定了理论上可结合的位点上限，而这一上限以「整个表面均具抗原性」「分子最大结合」为前提，属于上限估计而非实测值；epitope、epitype、paratope 界定了结合的双方，affinity 描述单一结合位点的能量，avidity 描述由亲和力、价态和分子排布共同决定的总体结合强度，两者不可互相替代。

对检测设计而言，需要留意两处边界。其一，血清的 avidity 会随稀释改变，因为稀释可能移除某些抗体群体，这会直接影响用免疫检测比较抗原或抗血清时的判读。其二，抗原刺激产生的是多克隆抗体，类型不限于 IgG，接种途径（sc/im 与口服/吸入）也会影响抗体类型分布，因此评价疫苗接种效果前必须先明确用总抗体、isotype-specific 检测还是抗原清除作为读出。

这些概念本身不解决具体的方法学参数问题——诸如包被浓度、稀释倍数、标准品选择，仍需要结合各自的体系另行确定。