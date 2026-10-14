---
draft: true
reviewNotes:
  - "正文过短: 4002/13096=31% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,916 字符（原文 16,470，比例 24%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、表位与抗体亲和力／亲合力"
date: 2026-10-14
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理 ELISA 检测背后的理论概念，沿两条线索展开：抗原一侧的分子大小、可接触表面积与表位定义，抗体一侧的亲和力（affinity）、亲合力（avidity）与免疫应答的异质性。最后归拢这些前提对检测设计的约束——抗体用量怎么估、稀释为什么可能改变结论、什么时候该测总抗"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理 ELISA 检测背后的理论概念，沿两条线索展开：抗原一侧的分子大小、可接触表面积与表位定义，抗体一侧的亲和力（affinity）、亲合力（avidity）与免疫应答的异质性。最后归拢这些前提对检测设计的约束——抗体用量怎么估、稀释为什么可能改变结论、什么时候该测总抗体而不是某一个 isotype。

## 抗原性由分子大小与可接触表面积决定

分子越大，其复杂性也就越高。Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个估算有两个前提，原书明确指出：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally” (Crowther, 2009)——这样的计算基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。也就是说，由表面积除以 20 得到的只是**理论上限**，实际可结合位点数通常低于该值。

该估算的用途在于：“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface” (Crowther, 2009)——计算饱和某一试剂所需的抗体量，或测定抗体结合水平随可用表面的变化。

## 表位、表位型与抗原结合部位的界定

三个术语需要区分清楚：

- **epitope**：antigenic site，即抗原上被抗体识别的位点；
- **paratope**：抗体上结合抗原表位的部分；
- **Epitype（表位型）**：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site” (Crowther, 2009)——表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别；可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

## 亲和力与亲合力不是同一件事

### affinity：单一位点的结合能

affinity 有三层含义：其一，单个 epitope 与 paratope 之间的能量；其二，它是抗原表位与抗体 paratope 在**单一结合位点**上的相互作用强度；其三，这种作用由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。原书表述为：“The binding energy between an antibody molecule and an antigen determinant is termed affinity.” (Crowther, 2009)。

### avidity：多个位点结合的总和

avidity 又称 functional affinity（功能性亲和力），是与抗原结合的总能量：“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites” (Crowther, 2009)。换言之，抗体在每一个结合位点上结合强度的总和称为 avidity。

### 影响 avidity 的三个因素

1）the binding affinity，2）valency，3）the structural arrangement of the antibody and antigen in question——即单个位点的亲和力、抗体的价数、以及抗体与抗原的空间排布。

## 抗体群体的异质性会随稀释而改变检测结果

对血清这类多克隆样本而言，avidity 的定义要放到群体层面：“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)” (Crowther, 2009)——亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

这一点直接引出一个容易被忽略的操作后果：“It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies” (Crowther, 2009)。原书举的例子是：血清中可能同时存在**少量高亲和力抗体**和**大量低亲和力抗体**；在血清**未大幅稀释**的条件下，两者竞争抗原位点，**高亲和力抗体优先反应**；而一旦稀释，高亲和力抗体的浓度被降低，最终只剩下低亲和力抗体。这类问题在操作者用免疫分析、以不同抗血清的差异活性来**比较抗原**时尤为重要——“The dilution of any serum can affect its ability to discriminate between antigens”，原因在于异质性抗体群体的动力学（各个抗体分子的相对浓度与亲和力）(Crowther, 2009)。

## 免疫方式决定该测总抗体还是 isotype

抗原刺激机体产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|--> (Crowther, 2009)

**被动免疫（passive immunization）** 是直接注射中和抗体；**主动免疫（active immunization）** 是给予抗原、由机体产生保护性抗体。

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑：用总抗体检测、isotype-specific assay，还是检测抗原清除，来评估疫苗接种效果。

口服／吸入免疫则另有侧重：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody” (Crowther, 2009)——免疫分析工作者必须判断，同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地反映疫苗接种的收益。

## 这些理论前提对检测设计的约束

把上述概念收拢，可以落到三条设计约束上。

其一，由分子表面积估算 Fab 结合位点数的做法，前提是“整个表面都具有抗原性”和“分子达到最大结合”，而前者很少成立，因此它给出的是上限而非实测值；用它来推算饱和抗体用量或结合水平随可用表面的变化时，需要意识到这一点。

其二，亲和力描述单一结合位点，亲合力描述总结合强度，后者还受价数与抗体–抗原空间排布影响；在多克隆血清中，亲合力是异质性抗体群与各表位亲和力的总和，会随稀释而改变，进而影响血清区分不同抗原的能力——因此用不同抗血清做抗原比较时，稀释方案本身就是一个变量。

其三，抗原刺激产生的是多克隆抗体且不限于 IgG，注射（sc／im）与口服／吸入诱导的 isotype 谱不同，检测端必须在总抗体、isotype-specific assay（如 IgA）与抗原清除之间预先做出选择。

需要留待具体体系判断的是：结合位点数的理论上限与实际可及表位之间的差距、以及稀释对特定血清区分能力的影响幅度，都依赖具体抗原与抗体群体，无法由这些一般性概念直接给出。