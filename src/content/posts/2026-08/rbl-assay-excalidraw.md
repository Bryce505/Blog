---
draft: true
reviewNotes:
  - "正文过短: 1849/21934=8% < 40%"
  - "6 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 1,896 字符（原文 27,692，比例 7%）超出 15,231～26,307 字符的区间"
title: "RBL 细胞脱颗粒活性检测：传统酶法与 NFAT 报告基因法"
date: 2026-08-28
category: "03质量控制"
primaryTag: "03质量控制/活性/细胞活性"
description: "RBL（大鼠嗜碱性白血病）细胞脱颗粒活性检测是过敏原诊断中的一类细胞学方法。本文围绕两种检测原理展开——基于组胺与 β-氨基己糖苷酶释放的传统酶法，以及基于 NFAT 驱动的荧光素酶表达的报告基因法；内容涵盖方法在过敏原诊断体系中的定位、传统酶法的灵敏度局限与刺激 buffer "
tags:
  - "03质量控制/活性/细胞活性"
sourceNotes:
  - "Analytical technology/细胞活性分析/RBL assay.excalidraw.md"
---

RBL（大鼠嗜碱性白血病）细胞脱颗粒活性检测是过敏原诊断中的一类细胞学方法。本文围绕两种检测原理展开——基于组胺与 β-氨基己糖苷酶释放的传统酶法，以及基于 NFAT 驱动的荧光素酶表达的报告基因法；内容涵盖方法在过敏原诊断体系中的定位、传统酶法的灵敏度局限与刺激 buffer 优化、报告基因法的细胞系与优势，以及两条路径的适用取舍。

## RBL assay 在过敏原诊断中的定位

sIgE 检测是过敏诊断的中心环节：The measurement of sIgE levels in the blood of individuals with suspected allergy is at the center of allergy diagnosis. 在此前提下需区分两个概念：sensitization 指 IgE 占据肥大细胞和嗜酸性粒细胞上的 FceRI；allergy 指临床症状。

目前过敏原诊断的方法包括：

- serological sIgE tests；
- cellular tests
  - Skin prick test（SPT）：皮内注入测试样品后，取血样检测激活的肥大细胞；
  - basophil activation test（BAT）；
  - humanized rat basophilic leukemia（RBL）assay。

*[图片暂缺]*<!--missing-image: Pasted Image 20240919101703_895.png|-->

## 传统酶法：脱颗粒释放标志物的检测

传统酶法（biochemical assay）以 RBL 细胞脱颗粒释放的组胺（Histamine）与 β-氨基己糖苷酶（beta-hexosaminidase）为检测对象。β-氨基己糖苷酶通过底物水解产生可定量信号，其他底物：4-MUG；酶解产物4-MU，fluorescence signal at Ex/Em 360/465 nm. 检测用细胞系为改造 RBL-2H3，最小免化剂量（sensitizing dose）：10ng/ml IgE。

*[图片暂缺]*<!--missing-image: Pasted Image 20240919104014_973.png|-->
*[图片暂缺]*<!--missing-image: Pasted Image 20240919105551_820.png|-->

## 传统酶法的灵敏度局限与刺激 buffer 优化

传统酶法的主要问题是灵敏度不够，对应有两种刺激 buffer 解决方案：

- 解决方案1: 最常用的刺激buffer-50%D2O，可能是通过稳定微管增加灵敏度（微管参与胞吐过程中分泌囊泡的移动）；
- 解决方案2：刺激buffer使用5′-(Nethyl)carboxyamidoadenosine (NECA)，激活磷脂酶C，增加RBL抗原依赖性脱颗粒；

两种方案共同的代价是背景值也会变高，信噪比降低。

## 报告基因法：NFAT 驱动的荧光素酶表达

报告基因法的核心是 NFAT-dependent expression of the firefly luciferase reporter gene，即 NFAT 依赖的萤火虫荧光素酶报告基因表达，所用细胞系为 RS-ATL8。相对于传统酶法，其优势包括：

- 检测灵敏度高，无需用提高灵敏度的试剂；
- 方法稳健，不受淬灭剂和温度的影响；
- 可以使用更高稀释比的血清，避免毒性，同时不影响灵敏度。

*[图片暂缺]*<!--missing-image: Pasted Image 20240919112011_924.png|-->
*[图片暂缺]*<!--missing-image: Pasted Image 20240919171449_268.png|-->

## 两条检测路径的取舍与适用边界

传统酶法直接测定脱颗粒释放的组胺与 β-氨基己糖苷酶，贴近天然释放过程，但基线灵敏度不足，D2O 与 NECA 的优化在提高信号的同时抬高背景；报告基因法则以 NFAT 转录激活偶联荧光素酶表达，在灵敏度、稳健性和血清耐受性上更有优势，且无需增敏试剂。选择哪条路径，取决于实验对检测灵敏度、背景控制与血清耐受性的具体需求。

*[图片暂缺]*<!--missing-image: Pasted Image 20240919171849_426.png|-->