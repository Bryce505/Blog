---
draft: true
reviewNotes:
  - "正文过短: 3832/13096=29% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,260 字符（原文 16,470，比例 26%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与抗体应答"
date: 2026-09-19
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量性能最终由抗原—抗体相互作用的性质决定，而不是由显色体系或读板仪器决定。这篇笔记整理了三个层面的理论前提：抗原一侧的分子大小与表位定义，抗体一侧的亲和力与亲合力，以及免疫应答所产生的抗体群体异质性。把这些前提摆清楚，才能解释为什么同一份样品在不同稀释度、不同抗血"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量性能最终由抗原—抗体相互作用的性质决定，而不是由显色体系或读板仪器决定。这篇笔记整理了三个层面的理论前提：抗原一侧的分子大小与表位定义，抗体一侧的亲和力与亲合力，以及免疫应答所产生的抗体群体异质性。把这些前提摆清楚，才能解释为什么同一份样品在不同稀释度、不同抗血清下会给出不同的读数。

## 抗原的分子大小如何限制可结合的 Fab 位点数

分子越大，其复杂性也就越高。Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

这个计算给出的是上限而非实测值，Crowther 对其前提有明确限定：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"
> 这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。

尽管只是上限，这一估算框架的用途落在两个方向上："calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface" —— 估算饱和任一抗原所需的抗体量，或把抗体结合水平表示为可用表面的函数。

## 表位、表位型与互补位：三个术语的边界

**epitope** 指 antigenic site，即抗原上被抗体识别的位点；**paratope** 指抗体上结合抗原表位的部分。两者分居抗原侧与抗体侧。

**Epitype** 描述的是另一层面的概念：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"
> 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAbs，它们定义重叠或相互关联的表位）识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

区别在于：epitope 是单个抗原决定簇，epitype 描述的是抗体群体对同一区域的重叠识别关系。

## 亲和力与亲合力：单一位点强度与整体结合强度

### 亲和力（affinity，binding affinity）

- the energy between a single epitope and paratope；
- the binding affinity is the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site —— 即抗原表位与抗体互补位在单一结合位点上相互作用的强度；
- Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K<sub>D</sub>)。

### 亲合力（avidity，functional affinity）

亲合力是与抗原的总结合能。"The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites" —— 亲合力代表一群结合不同抗原位点的抗体各自亲和力之和的平均结合能。

它也称为 functional affinity，即抗体在每个结合位点上总结合强度的度量，其三个影响因素是：1) the binding affinity, 2) valency, and 3) the structural arrangement of the antibody and antigen in question（结合亲和力、价数，以及所讨论的抗体与抗原的结构排布）。

对异质性抗体群体，亲合力还有一层含义："Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)" —— 亲合力可看作血清中包含的异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和。

> [!warning] 稀释会改变血清的表观亲合力
> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"
> 重要的是要认识到血清的亲合力在稀释时可能会发生变化，因为操作者可能会稀释掉某些群体的抗体。

Crowther 用一个具体情形说明这一点：血清中可能同时存在低丰度的高亲和力抗体和高丰度的低亲和力抗体。在血清不作大幅稀释的免疫分析条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；但一经稀释，高亲和力抗体的浓度会被降低，直到只剩下低亲和力抗体。这在用免疫分析、以不同抗血清的差异活性比较抗原时尤为重要；由于异质性抗体群体的动态（各个抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分不同抗原的能力。

## 抗体应答：多克隆来源、同种型与免疫途径

### 抗原刺激产生的抗体群体

应对抗原刺激产生抗体，得到的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

抗体分子与抗原决定簇之间的结合能称为亲和力："The binding energy between an antibody molecule and an antigen determinant is termed affinity."

### 被动免疫与主动免疫

passive immunization：直接打中和抗体；active immunization：服用抗原，产生保护性抗体。

疫苗注射方式：sc-皮下注射或 im-肌内注射；这种方式可以诱导产生多种抗体类型-isotype；必须考虑是否使用总抗体检测，isotype-specific assay 或检测抗原清除的检测来评估疫苗接种效果。

口服／吸入免疫则牵涉到另一个判断："The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody" —— 免疫分析工作者必须决定，同型抗体（特别是 IgA）的检测是否比总抗体检测能更深入地反映疫苗接种的收益。

## 这些理论前提对 ELISA 设计与判读意味着什么

把上面的线索归拢起来，可以看到几条直接影响实验设计的约束。

第一，抗原侧的可结合位点数只能作上限估计。球形表面积除以 20nm^2 的算法建立在「整个表面都具有抗原性」和「分子最大结合」两个假设上，而这两个假设很少成立，因此按表面积推算得到的位点数不能当作实测值使用。

第二，亲和力与亲合力是不同层级的量。亲和力描述单个 epitope 与 paratope 在单一结合位点上的相互作用强度，由非共价作用介导、以平衡解离常数定义；亲合力描述的是抗体（或抗体群体）与抗原的整体结合强度，受结合亲和力、价数和抗体—抗原结构排布三者共同影响。讨论多克隆抗血清时，只能谈亲合力。

第三，稀释本身是一个变量，而不只是浓度缩放。稀释会改变异质性抗体群体的组成，从而改变血清的表观亲合力，并影响其区分不同抗原的能力。因此同一份样品在不同稀释度下的读数不必然线性可比。

第四，免疫途径决定抗体同种型谱，进而决定检测策略。sc/im 注射诱导多种 isotype，口服／吸入免疫则把问题引向 IgA 等 isotype-specific 检测与总抗体检测之间的取舍；在评估疫苗效果时，还需要在总抗体、isotype-specific assay 与抗原清除检测之间作出选择。

至于具体的数据处理环节——标准曲线拟合、cut-off 值设定——已超出本章理论讨论的范围。