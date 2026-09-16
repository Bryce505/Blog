---
draft: true
reviewNotes:
  - "正文过短: 4273/13096=33% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,305 字符（原文 16,470，比例 26%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与免疫应答评估"
date: 2026-09-16
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的表现并不只取决于操作步骤，它受制于抗原侧和抗体侧的一系列物理化学前提。本文从抗原的尺寸与表位定义出发，梳理亲和力（affinity）与亲合力（avidity）的区别、稀释对血清表观亲合力的影响，最后落到抗体产生方式如何决定检测形式的选择。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的表现并不只取决于操作步骤，它受制于抗原侧和抗体侧的一系列物理化学前提。本文从抗原的尺寸与表位定义出发，梳理亲和力（affinity）与亲合力（avidity）的区别、稀释对血清表观亲合力的影响，最后落到抗体产生方式如何决定检测形式的选择。

## 抗原的尺寸与可结合位点数的上限估算

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20 nm²，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

> [!warning] 这个估算的成立前提
> “Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009）
>
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

这一估算的用途在于：计算饱和某一试剂需要多少抗体，或测定抗体结合水平随可用表面的变化（Crowther, 2009）。

### 表位相关术语的界定

- **epitope**：antigenic site，即抗原位点。
- **epitype**：抗原上的一个区域，由一组识别非常相似化学结构的密切相关的抗体所识别（例如 mAbs，它们定义重叠或相互关联的表位）。表位型可视为识别与同一抗原位点反应的、特异性略有不同的抗体的区域。原文表述为：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009）
- **paratope**：抗体上结合抗原表位的部分。

## 亲和力与亲合力：单一结合位点的能量与整体结合能

### affinity：单一结合位点的结合能

- 是单个 epitope 与 paratope 之间的能量；
- 结合亲和力是抗原表位与抗体旁位**在单一结合位点上**相互作用的强度；
- 亲和力由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

> “The binding energy between an antibody molecule and an antigen determinant is termed affinity.”（Crowther, 2009）
>
> 抗体分子与抗原决定簇之间的结合能称为亲和力。

### avidity：功能亲和力

- 与抗原的整体结合能；
- 抗体在**每一个**结合位点上总结合强度的量度，也称为功能亲和力；
- 三个影响因素：binding affinity、valency，以及抗体与抗原的结构排布。

> “The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009）

> “Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”（Crowther, 2009）
>
> 亲合力可以看作是血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同亲和力的总和。

## 稀释会改变血清的表观亲合力

对异质性抗血清而言，稀释不是一个中性操作。

> “It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”（Crowther, 2009）

> “As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules).”（Crowther, 2009）

也就是说：血清中可能同时存在低丰度的高亲和力抗体与高丰度的低亲和力抗体，在血清未被大幅稀释时可观察到高亲和力抗体优先与抗原位点结合；随着稀释推进，高亲和力抗体被逐步「稀释掉」，体系中只剩下低亲和力抗体，血清区分不同抗原的能力也随之改变。

## 抗体的产生方式与检测形式的选择

### 免疫应答产生的是多克隆抗体

应对抗原刺激，机体产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图（Crowther, 2009）。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 被动免疫与主动免疫

- passive immunization：直接打中和抗体；
- active immunization：服用抗原，产生保护性抗体。

### 免疫途径决定需要检测什么

疫苗注射方式为 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑是使用总抗体检测、isotype-specific assay，还是检测抗原清除来评估疫苗接种效果。

口服/吸入免疫则另有一层选择：

> “The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”（Crowther, 2009, p. 140）

## 适用边界与仍待判断的问题

把上述内容归拢起来，有几点边界需要在使用时守住。

第一，由球形表面积除以 20 nm² 得到的是**最大**结合位点数，它的前提是「整个表面都具有抗原性」且「分子以最大数量结合」，而原书明确指出前者很少为真，因此这个数字只能当作上限，不能当作预期值。

第二，affinity 描述的是单一结合位点上的相互作用，由 K<sub>D</sub> 定义；avidity 描述的是抗体与抗原的整体结合，受亲和力、价数与结构排布三者共同影响。在讨论多克隆抗血清时，二者不能混用。

第三，对异质性抗体群体而言，稀释会改变血清的亲合力和区分抗原的能力，因此在用免疫检测比较不同抗血清、或比较同一抗血清对不同抗原的差异活性时，稀释条件本身就是一个需要固定并交代的变量。

第四，疫苗免疫效果的评价形式没有统一答案：皮下/肌内注射会诱导多种 isotype，口服/吸入免疫则涉及是否单独检测 IgA 的问题——究竟用总抗体检测还是 isotype-specific assay，需要由方法的开发者结合所回答的问题作出判断（Crowther, 2009, p. 140）。