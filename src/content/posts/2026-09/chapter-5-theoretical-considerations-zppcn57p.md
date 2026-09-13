---
draft: true
reviewNotes:
  - "正文过短: 4410/13045=34% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,448 字符（原文 16,405，比例 27%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力"
date: 2026-09-13
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "抗原与抗体的结合是 ELISA 定量的底层事件。抗原的尺寸与表位分布决定了一个抗原分子上能容纳多少抗体结合位点；affinity 与 avidity 的区分决定了观测到的结合强度来自单一位点还是整个分子；而免疫或接种后的血清是一个异质抗体群体，其组成还会随稀释而改变。以下按抗原特"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

抗原与抗体的结合是 ELISA 定量的底层事件。抗原的尺寸与表位分布决定了一个抗原分子上能容纳多少抗体结合位点；affinity 与 avidity 的区分决定了观测到的结合强度来自单一位点还是整个分子；而免疫或接种后的血清是一个异质抗体群体，其组成还会随稀释而改变。以下按抗原特性、结合强度的度量、免疫应答中的抗体组成三条线索，整理 Crowther（2009）第 5 章的理论要点。

## 抗原越大，表面可容纳的 Fab 结合位点越多

分子越大，其复杂性也就越高。

Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

但这个数字带有前提。Crowther 对此的限定是：

> "Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally"

> 这样的计算是基于整个表面具有抗原性(很少是真实的)和分子最大结合的事实。

也就是说，只有当整个分子表面都具有抗原性、且抗体以最大数量结合时，该估算才成立，而这两条在实际抗原上都很少满足。

这一思路的用途有两处：估算饱和任一抗原所需抗体的量（calculate how much antibody is needed to saturate any agent），或把抗体附着水平作为可用表面积的函数来测定（measure the level of antibody attachment as a function of available surface）。

## 表位、表位型与互补位：几个容易混用的术语

epitope 即 antigenic site，指抗原上被抗体识别的位点；paratope 是抗体上结合抗原表位的部分。除这两个概念外，还有一个描述抗体侧特异性细分的概念——epitype（表位型）：

> "An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site"

> 表位型是抗原上的一个区域，由一组化学结构非常相似的抗体(例如, mAbs ,它们定义重叠或相互关联的表位)识别。表位型可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

三者描述的层次不同：epitope 是抗原侧的结合位点，paratope 是抗体侧的对应区域，epitype 则是用一组特异性相近的抗体（如 mAb）去描述同一抗原位点时所定义的范围。

## affinity 与 avidity：单一位点与整体结合

affinity（binding affinity）指抗体分子与抗原决定簇之间的结合能，可以从三个角度表述：

- 单个 epitope 与 paratope 之间的能量；
- 抗原表位与抗体互补位在单一结合位点上的相互作用强度；
- 由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并以平衡解离常数（K<sub>D</sub>）定义。

avidity 又称 functional affinity，度量的是整体结合：

- 与一个抗原的总结合能；
- 一个抗体分子在每一个结合位点上的总结合强度；
- 三个影响因素：the binding affinity、valency，以及抗体与抗原的结构排布。

对血清这类异质抗体群体，二者的关系可以这样理解：

> "The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites"

> "Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)"

> 亲合力可以看作是血清中包含的异质性抗体与各种抗原位点(抗原表位)之间所有不同亲和力的总和。

### 稀释会改变血清的亲合力

> "It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies"

> 重要的是要认识到血清的亲和力在稀释时可能会发生变化，因为操作者可能会稀释某些群体的抗体。

具体的机制，Crowther 用一个例子说明：

> "As an example, we could have a serum containing a low quantity of antibodies showing high affinity for a particular complex antigen and a high quantity of low-affinity antibody. Under immunoassay conditions in which that serum is not diluted greatly, we would have competition for antigenic sites between the high- and low-affinity antibodies, and the high-affinity antibodies would react preferentially. On dilution, however, the concentration of the high-affinity antibodies would be reduced until we would be left only with low-affinity antibodies. Such problems are important when an operator is using immunoassays to compare antigens by their differential activity with different antisera. The dilution of any serum can affect its ability to discriminate between antigens owing to the dynamics of the heterogeneous antibody population (relative concentrations and affinities of individual antibody molecules)."

即：血清中可能同时存在少量高亲和力抗体和大量低亲和力抗体。在不作大幅稀释的条件下，两类抗体竞争同一抗原位点，高亲和力抗体优先反应；继续稀释时，高亲和力抗体的浓度先降到无法竞争的水平，体系中剩下的主要是低亲和力抗体。因此稀释会改变血清区分不同抗原的能力，这在用不同抗血清比较抗原差异时是一个不可忽略的变量。

## 免疫应答产生的抗体类型不止 IgG

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于IgG;抗体类型产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 被动免疫与主动免疫

- passive immunization：直接打中和抗体；
- active immunization：服用抗原，产生保护性抗体。

### 接种途径与检测对象的选择

疫苗注射方式为 sc（皮下注射）或 im（肌内注射）；这种方式可以诱导产生多种抗体类型（isotype）；因此必须考虑：究竟使用总抗体检测、isotype-specific assay，还是检测抗原清除来评估疫苗接种效果。

口服或吸入免疫会把这个问题变得更具体：

> "The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody"

> 免疫学家必须决定同型抗体(特别是IgA)的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 适用边界与尚待判断的问题

- 用球形表面积除以 20 来估算 Fab 结合位点数，只有在整个表面都具有抗原性且结合达到饱和时才成立，而这两条在实际抗原上很少满足，因此该值只能作为上限性质的参考，不能直接当作实测位点数。
- 血清的 avidity 会随稀释而变化，稀释倍数因此会影响免疫测定区分不同抗原的能力；用不同抗血清比较抗原差异时，必须把稀释带来的抗体群体组成变化一并考虑，否则看到的"差异"可能来自抗体群体动力学而非抗原本身。
- 免疫后产生的是多克隆、多 isotype 的抗体群体，检测对象的选择（总抗体、isotype-specific assay，还是抗原清除）取决于要回答的问题；在口服/吸入免疫的场景下，IgA 特异性检测能否比总抗体检测提供更多信息，仍是一个需要按具体目的判断的问题。