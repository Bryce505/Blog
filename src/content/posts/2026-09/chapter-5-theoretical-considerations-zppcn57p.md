---
draft: true
reviewNotes:
  - "正文过短: 4611/13045=35% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,696 字符（原文 16,405，比例 29%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原表位、亲和力/亲合力与抗体应答"
date: 2026-09-30
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "理解 ELISA 的定量行为，前提是弄清抗原侧可供结合的位点有多少、抗体侧的结合强度如何定义，以及抗体应答本身如何随免疫方式变化。这篇笔记围绕三条线索组织：抗原性与表位数量的估算及其边界，表位、表位型、互补位的术语界定与亲和力/亲合力的区分，以及不同免疫途径下抗体类型的差异对检测"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

理解 ELISA 的定量行为，前提是弄清抗原侧可供结合的位点有多少、抗体侧的结合强度如何定义，以及抗体应答本身如何随免疫方式变化。这篇笔记围绕三条线索组织：抗原性与表位数量的估算及其边界，表位、表位型、互补位的术语界定与亲和力/亲合力的区分，以及不同免疫途径下抗体类型的差异对检测策略选择的影响。

## 分子大小与表位数量的上限估算

分子越大，其复杂性也就越高。Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally" (Crowther, 2009, p. 127)

也就是说，这样的计算基于两个前提：整个表面具有抗原性（很少是真实的），以及分子达到最大结合。因此这个数字是上限，不是实测值。

它的用途是双向的——既可以据此估算饱和任一试剂所需的抗体量，也可以把抗体结合水平作为可用表面积的函数来测量：

> "calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" (Crowther, 2009, p. 127)

## 表位、表位型与互补位

epitope 即 antigenic site。paratope 指抗体上结合抗原表位的部分。

Epitype 是抗原上的一个区域，由一组化学结构非常相似的抗体识别（例如定义重叠或相互关联表位的 mAb）；也可以视为识别与同一抗原位点反应的、特异性略有不同的抗体的区域：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site" (Crowther, 2009, p. 128)

## 亲和力与亲合力是两个不同层级的量

### 亲和力：单一位点上的结合能

抗体分子与抗原决定簇之间的结合能称为亲和力：

> "The binding energy between an antibody molecule and an antigen determinant is termed affinity." (Crowther, 2009, p. 136)

其定义包含三个要点：

1. 单个 epitope 与 paratope 之间的能量；
2. 是抗原表位与抗体互补位在**单一结合位点上**（at a singular binding site）的相互作用强度；
3. 由**非共价作用**（non-covalent interactions）介导，包括氢键、静电键、范德华力和疏水作用，并由平衡解离常数 **K<sub>D</sub>** 定义。

### 亲合力：抗体群体的总体结合强度

亲合力（avidity）又称功能性亲和力（functional affinity），指抗体与抗原的总体结合能。它是与不同抗原位点结合的抗体群体中，各个亲和力的加和所给出的平均结合能：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" (Crowther, 2009, p. 130)

置于血清这样的异质体系中，亲合力可以看作是血清中异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和：

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" (Crowther, 2009, p. 137)

亲合力受三个因素影响：1）the binding affinity，2）valency，3）the structural arrangement of the antibody and antigen in question。

### 稀释会改变血清的表观亲合力

一个容易被忽略的前提是，血清的亲合力在稀释时可能发生变化，因为操作者可能把某些抗体群体稀释掉了：

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies" (Crowther, 2009, p. 137)

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)." (Crowther, 2009, p. 137)

换言之，当免疫assay被用来通过不同抗血清的活性差异来比较抗原时，稀释度本身就是一个会影响区分能力的变量。

## 抗原刺激后的抗体应答

### 主动免疫与被动免疫

被动免疫（passive immunization）是直接注射中和抗体；主动免疫（active immunization）是给予抗原，由机体产生保护性抗体。二者的检测含义不同：前者测的是外源给予的抗体，后者测的是机体自身的应答。

### 免疫途径决定抗体类型的组成

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）；必须考虑是否使用总抗体检测、isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

抗体类型产生的时间顺序见下图：

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 口服/吸入免疫与 isotype-specific 检测

经口服或吸入途径免疫时，问题从「抗体总量够不够」变成「测哪一类抗体更有信息量」：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" (Crowther, 2009, p. 140)

## 这些理论前提对检测设计的约束

把上述内容归拢起来，可以提炼出三条约束：

第一，由球形表面积除以 20nm^2 得到的是结合位点的**上限**，其成立依赖「整个表面具有抗原性」和「分子达到最大结合」两个前提，而这两者在真实体系中很少同时满足；它更适合用于估算饱和试剂所需的抗体量，或把结合水平作为可用表面积的函数来测量。

第二，亲和力是单一位点层级的量，亲合力是群体层级的量，二者的换算关系取决于亲和力分布、价数和抗体-抗原的结构排布；在血清这类异质体系中，稀释会改变抗体的群体组成，进而改变表观亲合力与区分不同抗原的能力。用不同抗血清比较抗原活性时，稀释度是需要固定并交代的条件。

第三，免疫途径（sc/im 与口服/吸入）会带来不同的 isotype 组成，因此在设计评价疫苗接种效果的方案时，必须先决定采用总抗体检测、isotype-specific assay（尤其是 IgA），还是抗原清除相关的检测——这个选择不是检测环节的技术细节，而是由抗体应答本身的特征决定的。

尚未解决的部分在于：上述估算与定义给出的是框架，具体抗原的抗原性表面占比、血清中高/低亲和力抗体的相对浓度，都需要实测才能确定。