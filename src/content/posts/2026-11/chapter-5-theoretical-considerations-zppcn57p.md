---
draft: true
reviewNotes:
  - "正文过短: 2134/13096=16% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 1,794 字符（原文 16,470，比例 11%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答"
date: 2026-11-17
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "这篇笔记整理 ELISA 理论中的几个前置概念：抗原分子大小如何限制可结合位点数，epitope、paratope 与 affinity、avidity 的区别，以及多克隆抗体应答和免疫方式对检测选择的影响。内容整理自 Crowther（2009）第 5 章的相关论述，按抗原—抗"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

这篇笔记整理 ELISA 理论中的几个前置概念：抗原分子大小如何限制可结合位点数，epitope、paratope 与 affinity、avidity 的区别，以及多克隆抗体应答和免疫方式对检测选择的影响。内容整理自 Crowther（2009）第 5 章的相关论述，按抗原—抗体结合—免疫应答的顺序展开。

## 抗原分子的大小如何限制可结合位点数

分子越大，其复杂性也就越高。Fab结合的面积大概是20nm^2，也就是epitope的表面积；通过计算分子的球形表面积，再把表面积除以20，可以获得Fab结合位点的最大数量。

这样的计算基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实。因此它给出的是上限，而不是实际表位数。应用上，可用它估算饱和某种抗原或试剂所需抗体量，或把抗体结合水平作为可用表面的函数来测量。

## epitope、epitype 与 paratope 的界定

epitope 即 antigenic site。Epitype 是抗原上的一个区域，由一组化学结构非常相似的抗体（例如，mAbs，它们定义重叠或相互关联的表位）识别。Epitype 可视为识别与同一抗原位点反应的抗体特异性略有不同的区域。

paratope 则是抗体上结合抗原表位的部分。三个术语分别落在抗原侧、抗原表位的精细分区和抗体侧，后续讨论 affinity 与 avidity 时需要区分。

## affinity 与 avidity：单点结合和总体结合

affinity（结合亲和力）是单个 epitope 与 paratope 之间的能量，也就是单一结合位点上抗原表位与抗体 paratope 相互作用的强度。它由非共价相互作用介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K_D）定义。

avidity（功能亲和力）则是与抗原的总结合能。它代表一个抗体群体与不同抗原位点结合时，所有单个 affinity 之和的平均结合能，也是抗体在每个结合位点上总结合强度的量度。Avidity 受三个因素影响：binding affinity、valency，以及抗体与抗原的结构排布。

## 多克隆抗体应答与血清稀释对 avidity 的影响

抗原刺激后产生多克隆抗体，且抗体类型并不仅限于IgG；抗体类型产生时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\

抗体分子与抗原决定簇之间的结合能称为 affinity。Avidity 可看作血清中包含的异质性抗体与各种抗原位点（抗原表位）之间所有不同 affinities 的总和。

血清的 avidity 在稀释时可能发生变化，因为操作者可能稀释掉某些抗体群体。例如，血清中少量高 affinity 抗体与大量低 affinity 抗体共存；未大幅稀释时，两者竞争抗原位点，高 affinity 抗体优先反应；稀释后高 affinity 抗体浓度下降，直至只剩低 affinity 抗体。用免疫分析比较不同抗血清对抗原的差异活性时，这种效应会影响判别能力；稀释可因异质性抗体群体的相对浓度和 affinity 动态而改变血清区分抗原的能力。

## 免疫方式与疫苗效果评估中的抗体检测选择

passive immunization：直接打中和抗体；active immunization：服用抗原，产生保护性抗体。

疫苗注射方式：sc-皮下注射或im-肌内注射；这种方式可以诱导产生多种抗体类型-isotype；必须考虑是否使用总抗体检测，isotype-specific assay或检测抗原清除的检测来评估疫苗接种效果。

口服/吸入免疫：免疫学家必须决定同型抗体（特别是 IgA）的检测是否能比总抗体的检测更深入地了解疫苗接种的好处。

## 结论与适用边界

这组概念划出了几个边界：抗原大小估算给出的是最大 Fab 结合位点数，实际表位数受表面抗原性限制；affinity 描述单一位点，avidity 描述多价、多表位和多克隆背景下的总体结合；血清稀释会改变可检出的抗体群体，从而改变 avidity；免疫途径决定 isotype 分布，也决定总抗体、isotype-specific 或抗原清除检测之间的选择。