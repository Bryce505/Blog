---
draft: true
reviewNotes:
  - "正文过短: 3286/13096=25% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,132 字符（原文 16,470，比例 19%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与 avidity 的边界条件"
date: 2026-11-01
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量结果最终取决于抗原与抗体之间那一步结合，而这一步受分子大小、表位定义、亲和力与 avidity 的共同约束。本文按抗原性质、抗体性质、以及操作变量（稀释）三条线索，梳理建立方法时需要预先想清楚的理论前提。"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量结果最终取决于抗原与抗体之间那一步结合，而这一步受分子大小、表位定义、亲和力与 avidity 的共同约束。本文按抗原性质、抗体性质、以及操作变量（稀释）三条线索，梳理建立方法时需要预先想清楚的理论前提。

## 抗原性考量：分子大小与可及表位数量

分子越大，其结构复杂性越高，可被抗体识别的位点也就越多。Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这个估算有两个隐含前提，且都不容易成立：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"（Crowther, 2009, p.127）

即假设整个表面都具有抗原性（很少是真实的），并且分子达到最大结合。

即便如此，该计算仍有实际用途：可用于估算饱和任意抗原所需的抗体量，或测量抗体结合水平随可用表面的变化（"calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface"，Crowther, 2009, p.127）。

## 表位、表位型与互补位：三个容易混用的术语

- **epitope（表位）**：即 antigenic site，抗原上被抗体识别的位点。
- **paratope（互补位）**：抗体上结合抗原表位的部分。
- **epitype（表位型）**：抗原上的一个区域，由一组化学结构非常相似的抗体（例如 mAb，它们定义重叠或相互关联的表位）所识别；可视为识别与同一抗原位点反应、但特异性略有不同的抗体的区域。

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"（Crowther, 2009, p.128）

## 亲和力与 avidity：单点结合能 vs 总结合强度

**affinity（亲和力）**指抗体分子与抗原决定簇之间的结合能，即抗原 epitope 与抗体 paratope 在**单个结合位点**上的相互作用强度。它由**非共价相互作用**介导，包括氢键、静电作用、范德华力和疏水作用，并以平衡**解离常数（K_D）**定义。

**avidity（亲合力）**又称 functional affinity，指与抗原的总结合能。The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites（Crowther, 2009, p.130）。在血清层面，avidity 可以看作血清中包含的异质性抗体与各种抗原位点（表位）之间所有不同亲和力的总和。

avidity 受三个因素影响：

1. binding affinity；
2. valency（效价）；
3. 抗体与抗原的结构排布。

## 免疫应答产生的抗体：多克隆与同型差异

抗原刺激后产生的是多克隆抗体，且抗体类型并不限于 IgG；各抗体类型出现的时间顺序见下图（Crowther, 2009, p.135）。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\

被动免疫（passive immunization）是直接注射中和抗体；主动免疫（active immunization）则是给予抗原、由机体产生保护性抗体。

疫苗经 sc（皮下注射）或 im（肌内注射）途径接种时，可诱导产生多种抗体类型（isotype）。因此在评估疫苗接种效果时，必须先确定是检测总抗体、采用 isotype-specific assay，还是检测抗原清除。

口服/吸入免疫的情形下，则需要判断同型抗体（尤其是 IgA）的检测是否能比总抗体检测提供更深入的疫苗获益信息：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"（Crowther, 2009, p.140）

## 稀释会改变 avidity，进而改变抗原区分能力

血清的 avidity 在稀释时可能发生变化，因为操作者可能把某些抗体群体稀释掉了。

一个典型情形是：血清中同时含有**少量针对某复杂抗原的高亲和力抗体**和**大量低亲和力抗体**。在血清**未大幅稀释**的免疫分析条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；一旦稀释，高亲和力抗体的浓度不断下降，最终只剩下低亲和力抗体。

这在用免疫分析比较不同抗血清对抗原的差异活性时尤其重要：由于异质抗体群体的动力学（各抗体分子的相对浓度与亲和力），任何血清的稀释都可能影响其区分抗原的能力。

## 这些前提对方法设计的含义

把上述内容归拢起来，可以看到几条约束：

- 表面积除以 20nm^2 得到的只是 Fab 结合位点数的**上限估计**，实际可及表位取决于抗原表面有多少真正具有抗原性、以及结合是否达到饱和；
- affinity 描述的是单个 paratope–epitope 位点、以 K_D 表征的非共价结合强度，而 avidity 才是抗体分子与整个抗原（或在血清层面，异质抗体群体与多个表位）的总结合表现，二者不可互相替代；
- avidity 随 valency 与分子排布变化，因此同一个抗体在不同形式抗原上的表现可能不同；
- 稀释不是中性操作，它会改变血清中抗体群体的组成，从而改变 avidity 和区分抗原的能力；
- 涉及疫苗评价时，检测对象（总抗体、特定 isotype 还是抗原清除）需要先行确定，而不是事后选择。

尚未解决的问题在笔记中并未展开，例如如何在实际体系中量化"整个表面具有抗原性"这一假设的偏离程度，以及稀释引起的 avidity 漂移在定量方法中应如何控制。