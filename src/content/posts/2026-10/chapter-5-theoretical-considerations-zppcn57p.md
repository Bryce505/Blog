---
draft: true
reviewNotes:
  - "正文过短: 3886/13045=30% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,370 字符（原文 16,405，比例 27%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答"
date: 2026-10-18
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的可靠性建立在几个并不直观的概念之上：抗原分子能提供多少个可被识别的位点，抗体与单个表位之间的结合能有多大，以及多克隆抗血清的整体结合行为如何随稀释而改变。本文按「抗原—抗体—免疫应答」的顺序整理这些概念，并说明它们各自在方法设计中的落点。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的可靠性建立在几个并不直观的概念之上：抗原分子能提供多少个可被识别的位点，抗体与单个表位之间的结合能有多大，以及多克隆抗血清的整体结合行为如何随稀释而改变。本文按「抗原—抗体—免疫应答」的顺序整理这些概念，并说明它们各自在方法设计中的落点。

## 抗原分子的大小决定了可结合位点的上限

分子越大，其复杂性也就越高，可供抗体识别的表面也越多。一个 Fab 的结合面积约为 20nm^2，大致相当于一个 epitope 的表面积；用分子的球形表面积除以 20，即可估算该分子所能容纳的 Fab 结合位点最大数量。

这个估算有两个明确前提：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009）
>
> 这样的计算基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

因此它给出的是上限而非实测值。其用途也相应明确：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"（Crowther, 2009）

即用于计算饱和某一抗原所需的抗体量，或测定抗体结合量随可用表面积的变化。

## 表位、表位型与旁位：三个容易混淆的定义

- **epitope（表位）**：即 antigenic site，抗原上被抗体识别的位点。
- **epitype（表位型）**：抗原上的一个区域，由一组化学结构非常相似的抗体识别，例如定义重叠或相互关联表位的 mAb；可视为识别与同一抗原位点反应的、特异性略有差异的抗体的区域。

  > "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009）

- **paratope（旁位）**：抗体上结合抗原表位的部分。

## affinity 与 avidity：单点结合能与整体结合能

两者都译作「亲和力」的做法会造成混淆，需要分开理解。

**affinity（结合亲和力）**指单个 epitope 与 paratope 之间的能量，即在单一位点上抗原表位与抗体旁位相互作用的强度。它由非共价作用介导，包括氢键、静电键、范德华力和疏水作用，并以平衡解离常数（K_D）定义。

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity."（Crowther, 2009）

**avidity（亲合力，functional affinity）**指与抗原的总结合能，是抗体在每个结合位点上总结合强度的量度。它受三个因素影响：结合亲和力、价数（valency），以及抗体与抗原的结构排布。

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"（Crowther, 2009）

放到血清这一层面，avidity 可以看作血清中异质性抗体与各抗原位点（表位）之间所有不同亲和力的总和：

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"（Crowther, 2009）

## 抗原刺激后的抗体产生与抗体类型的时间顺序

应对抗原刺激，机体产生的是多克隆抗体，且抗体类型并不仅限于 IgG。各类抗体出现的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

免疫方式分为两类：被动免疫（passive immunization）直接给予中和抗体；主动免疫（active immunization）则给予抗原，使机体产生保护性抗体。

## 血清稀释会改变 avidity，进而改变抗原区分能力

这是一个容易被忽略的前提：血清的 avidity 在稀释时可能发生变化，因为操作者可能把某些抗体群体稀释掉了。

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"（Crowther, 2009）

典型情形是血清中同时存在**少量高亲和力抗体**和**大量低亲和力抗体**。在稀释倍数不大的免疫分析条件下，两者竞争抗原位点，高亲和力抗体优先反应；一旦稀释，高亲和力抗体的浓度不断下降，最终只剩低亲和力抗体。

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)."（Crowther, 2009）

因此，当用免疫分析比较不同抗原与不同抗血清的差异活性时，任何血清的稀释都会影响其区分抗原的能力，这一效应来自异质性抗体群体的动力学，即各抗体分子的相对浓度与亲和力。

## 免疫途径与检测策略：总抗体、isotype 还是抗原清除

皮下（sc）或肌内（im）注射可诱导产生多种抗体类型（isotype）。因此在评估疫苗接种效果时，必须考虑采用哪种检测：总抗体检测、isotype-specific assay，还是检测抗原清除。

口服或吸入免疫则引出另一层判断：isotype-specific 抗体（尤其 IgA）的检测，是否比总抗体检测更能深入反映疫苗接种的获益。

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p. 140）

## 小结

这些概念分别约束方法设计的不同环节：抗原侧，球形表面积除以 20 给出的是可结合位点数的上限，前提是「整个表面均具抗原性」且「分子最大结合」，两条都很少全然成立；抗体侧，affinity 描述单一位点的相互作用，avidity 描述血清整体的结合行为，而 avidity 随稀释改变这一点直接限制了对不同抗血清比较实验的解读；免疫应答侧，免疫途径决定了产生的 isotype 组成，进而决定检测应当落在总抗体、isotype-specific 抗体还是抗原清除上。把这些前提写在方法里，比在结果里解释异常要省事得多。