---
draft: true
reviewNotes:
  - "正文过短: 2924/13096=22% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,190 字符（原文 16,470，比例 19%）超出 9,058～15,646 字符的区间"
title: "ELISA 理论考虑：从抗原表位容量到多克隆抗体的亲和力与亲合力"
date: 2026-09-07
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇梳理免疫测定（尤其是 ELISA）设计之前必须理解的理论问题：抗原分子的大小如何约束可结合的 Fab 数量，epitope、paratope、affinity、avidity 这几个术语分别指什么，以及多克隆抗体自身的异质性会怎样影响测定结果。文章按抗原特性、术语体系、抗体的"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇梳理免疫测定（尤其是 ELISA）设计之前必须理解的理论问题：抗原分子的大小如何约束可结合的 Fab 数量，epitope、paratope、affinity、avidity 这几个术语分别指什么，以及多克隆抗体自身的异质性会怎样影响测定结果。文章按抗原特性、术语体系、抗体的产生与同型演变、稀释效应对多克隆抗体行为的改变依次展开。观点整理自 Crowther（2009）相关章节。

## 抗原大小与表位容量：从分子表面积估算最大 Fab 结合数

抗原性质决定了免疫测定中抗体与被测物之间的结合比例。一个基本的出发点是：分子越大，其复杂性也就越高。

估算一个抗原分子最多能同时结合多少抗体，可以这样操作：

> Fab 结合的面积大概是 20nm²，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一计算有两种实际用途：一是估算使任何试剂达到饱和需要多少抗体，二是以可利用的表面积为函数衡量抗体的附着水平。

需要强调的是，这种估算本身有明确前提：

> Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally.
> 这样的计算基于两个事实：整个表面均具有抗原性（很少是真实的），且分子为最大程度结合。

因此，算出的 Fab 结合位点数量应理解为理论上限，而不是实际测定条件下的真实结合数目。

## 术语基础：epitope、epitype 与 paratope

免疫测定讨论的是抗原与抗体之间的识别，先要把识别所涉及的几个位置概念界定清楚：

- **Epitope**：抗原上的 antigenic site，即被抗体识别的部位。
- **Paratope**：抗体上直接结合抗原表位的部分。
- **Epitype**：介于两者之间的一个层次，原文定义如下：

> An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site.
> 表位型是抗原上的一个区域，由一组识别化学结构非常相似的抗体（例如，识别重叠或相互关联表位的 mAbs）所界定。表位型可视为识别与同一抗原位点反应、但特异性略有差异的抗体的区域。

简言之，epitope 是抗原上的结合位点，paratope 是抗体上的对应结构，而 epitype 描述的是多个相似抗体共同界定的一块抗原区域——它对应的是识别同一抗原位点的一组相近特异性。

## affinity 与 avidity：把单点结合与总体结合分开

### affinity：单个表位-对位结合位点的强度

Affinity 描述的是抗原表位与抗体 paratope 在单一结合位点上的相互作用强度，本质上是单个 epitope 与单个 paratope 之间的结合能。

> The binding energy between an antibody molecule and an antigen determinant is termed affinity.

这种相互作用由非共价键介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡解离常数（KD）来定义。

### avidity：多克隆抗体群体的总结合强度

Avidity 又称 functional affinity，衡量的是抗体分子在所有结合位点上的总结合强度。对多克隆血清而言：

> Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes).
> 亲合力可视为血清中异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和。

它的高低由三个因素共同决定：抗体与抗原结合位点的单点亲和力（binding affinity）、抗体的价数（valency），以及抗体与抗原的结构排布。

## 抗体的产生与同型演变：免疫途径决定你需要测哪种抗体

抗原刺激机体后产生的抗体并不是单一的 IgG。动物免疫应答产生的是多克隆抗体，且抗体类型不限于 IgG；不同抗体类型的产生存在时间上的先后顺序，如下页图所示。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

抗体获取方式有两种基本类型：被动免疫是直接给予中和抗体；主动免疫则是给予抗原，使机体自行产生保护性抗体。

免疫途径会影响测定的设计。疫苗经皮下（sc）或肌内（im）注射可以诱导产生多种抗体同型（isotype），这时需要决定：用总抗体检测、isotype-specific assay，还是通过检测抗原清除来评估疫苗接种效果。而对于口服或吸入途径的免疫，则需要判断另一类问题：

> 免疫分析人员必须决定，针对同型抗体（尤其是 IgA）的检测是否比总抗体检测更能深入揭示疫苗接种的获益。

也就是说，同型特异性测定不是一个默认选项，它是否优于总抗体测定取决于免疫途径和所要回答的免疫学问题。

## 多克隆血清的稀释效应：avidity 不是固定属性

多克隆血清的 avidity 与纯化单克隆抗体不同，它不是一个恒定值。血清稀释本身就可能改变测得的 avidity，因为稀释会选择性降低某些抗体群体的浓度。

一个典型的例子：假设血清中含有少量针对某复合抗原的高亲和力抗体，同时含有大量低亲和力抗体。在血清未被大幅稀释的条件下，高、低亲和力抗体竞争抗原位点，高亲和力抗体优先反应；但随着血清不断稀释，高亲和力抗体的浓度逐渐降低，最后体系中可能只剩下低亲和力抗体。

这一问题在使用免疫测定比较不同抗原与不同抗血清的差异活性时尤为重要：血清的稀释会改变它区分抗原的能力，根源在于异质性抗体群体内部的动态——不同抗体分子的相对浓度和单个亲和力都在随稀释发生变化。

## 小结

ELISA 方法学建立在抗原-抗体相互作用的理论框架之上，几个层面环环相扣：抗原的表面积与表位容量决定了结合比例的理论上限；epitope、epitype、paratope 提供了描述识别位点的语言；affinity 与 avidity 分别刻画单点结合强度和总体结合强度；而免疫途径决定实际血清中抗体的同型构成。多克隆血清的 avidity 对稀释敏感这一点，提示测定结果的解读必须考虑抗体群体的异质性，而不仅是总抗体浓度。具体的数据处理与验证问题，可进一步参见站内关于 ELISA cut-off 值计算、夹心 ELISA 定量法、抗体滴度、EC50/ED50 计算及方法验证等主题的笔记。