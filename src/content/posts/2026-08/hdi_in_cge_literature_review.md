---
draft: true
reviewNotes:
  - "减法模式下篇幅 9,851 字符（原文 19,263，比例 51%）超出 10,595～18,300 字符的区间"
title: "毛细管凝胶电泳中的水动力进样：蛋白分析的文献证据、技术可行性与定量应用"
date: 2026-08-31
category: "05仪器与分析技术"
primaryTag: "05仪器与分析技术/Capillary-Electrophoresis"
description: "水动力（压力）进样（HDI）在毛细管凝胶电泳（CGE/CE-SDS）蛋白分析中的应用已有报道并成功验证，但在生物制药领域仍属少数实践。本文按\"直接文献证据—技术可行性—进样模式比较—应用现状—仪器支持\"的脉络组织，核心结论是：HDI 在凝胶填充毛细管中技术上可行，定量精度与基质独"
tags:
  - "05仪器与分析技术/Capillary-Electrophoresis"
sourceNotes:
  - "Analytical technology/Capillary electrophoresis methods for pharmaceutical analysis/峰面积不稳定/HDI_in_CGE_Literature_Review.md"
---

水动力（压力）进样（HDI）在毛细管凝胶电泳（CGE/CE-SDS）蛋白分析中的应用已有报道并成功验证，但在生物制药领域仍属少数实践。本文按"直接文献证据—技术可行性—进样模式比较—应用现状—仪器支持"的脉络组织，核心结论是：HDI 在凝胶填充毛细管中技术上可行，定量精度与基质独立性优于电动力学进样（EKI），但在 mAb 纯度等标准 QC 场景中尚未取代 EKI。

## 水动力进样在 CGE 蛋白分析中的直接文献证据

生物制药 CE-SDS 的标准实践（如 IgG 纯度、mAb 分析）使用电动力学进样（EKI），由商业试剂盒制造商（SCIEX SDS-MW Analysis Kit）规定。少量但重要的文献——主要来自 Janssen Vaccines 组（van Tricht、Geurink 等）和 TU Braunschweig 的 Wätzig 组——证明 HDI 在凝胶填充毛细管中技术可行，且定量精度更优、基质依赖更低。

### Van Tricht 等（2015）：流感疫苗蛋白分析的奠基性工作

> van Tricht E, Geurink L, Pajic B, Nijenhuis J, Backus H, Germano M, Somsen GW, Sänger-van de Griend CE. "New capillary gel electrophoresis method for fast and accurate identification and quantification of multiple viral proteins in influenza vaccines." *Talanta*, 2015 Nov 1; 144: 1030–1035. DOI: 10.1016/j.talanta.2015.07.047. PMID: 26452923.

- 开发并验证了一种 CGE（CE-SDS）方法，用于流感病毒和病毒体样品中多种病毒蛋白（HA1、HA2、基质蛋白 M、核蛋白 NP）的鉴定与定量
- 采用水动力进样，通过全因子设计与分离电压、毛细管温度共同优化
- 使用商业 SCIEX SDS-MW 凝胶缓冲体系
- HDI 的定量性能良好，精密度与准确度优于 RP-HPLC

该工作成为 HDI 在疫苗蛋白 CGE 分析中的奠基性文献。

### Geurink 等（2021）：四步 CGE 方法开发中的进样选择

> Geurink L, van Tricht E, Dudink J, Pajic B, Sänger-van de Griend CE. "Four-step approach to efficiently develop capillary gel electrophoresis methods for viral vaccine protein analysis." *Electrophoresis*, 2021 Jan; 42(1-2): 10–18. DOI: 10.1002/elps.202000107. PMID: 32640046. PMCID: PMC7361255.

- 明确以 100 mbar、100 s 的水动力进样作为 CE-SDS 疫苗蛋白方法（mini-hemagglutinin 与灭活脊髓灰质炎疫苗蛋白）的标准进样条件
- 作者对定量分析明确偏好 HDI："Generally, we prefer hydrodynamic injection over electrokinetic injection for quantitative analysis, as it is generally more precise, non-selective, and matrix independent, whereas electrokinetic injection is selective and matrix dependent."
- 凝胶缓冲液稀释对两种进样的影响机制不同：
  - HDI 进样体积取决于粘度（而非电导率），稀释凝胶缓冲液降低粘度、增大进样体积
  - EKI 取决于凝胶缓冲液与样品之间的电导率比，稀释凝胶降低电导率、减少进样量
- 70% 稀释凝胶缓冲液下，HDI 校正峰面积约为 100% 凝胶缓冲液时的 2.6 倍，与粘度下降相符
- 验证方法实现校正峰面积重复性 0.8% RSD (n = 9)
- 仪器：Agilent 7100 CE 配 DAD，以及 SCIEX CESI 8000 Plus；毛细管为 50 µm ID 裸熔融石英，33 cm 总长

### Cianciulli 等（2012）：HDI 与 EKI 的直接比较

> Cianciulli C, Hahne T, Wätzig H. "Capillary gel electrophoresis for precise protein quantitation." *Electrophoresis*, 2012 Nov; 33(22): 3321–3328. DOI: 10.1002/elps.201200177.

- 在 CGE（CE-SDS）蛋白分析中直接比较 HDI 与 EKI，应用包括单克隆抗体相关分析
- 结论："The application of hydrodynamic injection is beneficial for the precision of the method compared to the traditionally used electrokinetic one."
- 提高样品浓度与进样体积对获得高 S/N 比（>70）至关重要
- 两种进样模式在长序列运行（n = 48）中进行了比较
- 充分优化后，HDI 可实现 RSD < 2% 的高精度 CGE 定量

这是针对生物制药相关蛋白定量最直接的 HDI 与 EKI 比较。

### Dawod 等（2017）：综述的独立确认

> Dawod M, Arvin NE, Kennedy RT. "Recent advances in protein analysis by capillary and microchip electrophoresis." *Analyst*, 2017 May 30; 142(11): 1847–1866. DOI: 10.1039/c7an00198c. PMID: 28470231. PMCID: PMC5516626.

- 在 CGE 综述部分评述了 van Tricht 等的工作："In the optimized CGE described in this paper, the influenza proteins were injected hydrodynamically at 100 mbar for 100 s which provided similar results (based on peak area, S/N, and migration time) compared to electrokinetic injection (EKI) at −18 kV for 100 s."
- 明确指出："However, hydrodynamic injection (HDI) is less affected by sample matrix and provides better precision."

作为独立综述，该文确认了 HDI 在 CGE 蛋白分析中的有效性与优势。

## 技术可行性：凝胶填充毛细管能否支持压力进样

**可以，但有重要注意事项。** 水动力进样的原理是：在毛细管两端施加压力差，将定义好的样品塞推入毛细管入口。CGE 的挑战在于毛细管中充满高粘度凝胶缓冲液（如基于葡聚糖的 SCIEX SDS-MW 凝胶），高粘度限制了给定压力下可实现的流速，因此需要：

- 更高压力（100 mbar，而自由溶液 CE 通常为 50 mbar）
- 更长进样时间（100 s，而自由溶液 CE 通常为 5–10 s）

### 进样体积的定量描述

HDI 的进样体积遵循 Hagen-Poiseuille 方程：

$$V_{inj} = \frac{\Delta P \cdot \pi \cdot d^4 \cdot t_{inj}}{128 \cdot \eta \cdot L}$$

其中 ΔP 为施加的压力差，d 为毛细管内径，t_inj 为进样时间，η 为凝胶缓冲液动态粘度，L 为毛细管总长。由于凝胶缓冲液的 η 很高（约为水的 10–50 倍），需要高得多的 P × t 乘积。Geurink 等（2021）的粘度测量证实了这一点：70% 浓度凝胶缓冲液的粘度比水样背景高 2.2–2.7 倍。

### 堆叠效应与分离效率

HDI 不具备 EKI 固有的样品堆叠效应。在 EKI 中，电场集中在低电导率样品区，同时完成进样与浓缩。HDI 条件下：

- 必须控制进样塞长度以避免过载
- 堆叠仅发生在分离阶段，由样品塞与凝胶缓冲液之间的电导率差驱动
- 凝胶缓冲液稀释会降低 HDI 的堆叠能力：凝胶从 100% 稀释至 70% 时，板数降低约 2.4 倍（从约 10⁵ 降至 3–5 × 10⁴）

### 典型技术参数对比

| 参数 | HDI（van Tricht/Geurink） | 标准 EKI（SCIEX SDS-MW Kit） |
|---|---|---|
| 进样模式 | Hydrodynamic (pressure) | Electrokinetic |
| 压力/电压 | 100 mbar | −5 kV (mAb) / −18 kV (viral proteins) |
| 进样时间 | 100 s | 20 s (mAb) / 100 s (viral proteins) |
| 毛细管 | 50 µm ID BFS, 33 cm | 50 µm ID BFS, 30–33 cm |
| 凝胶缓冲液 | SCIEX SDS-MW gel buffer | SCIEX SDS-MW gel buffer |
| 检测 | UV 214 nm | UV 214 nm or LIF |

## 电动力学进样与水动力进样的权衡

### HDI 相对 EKI 的优势

| 优势 | 说明 | 参考文献 |
|---|---|---|
| 精密度更优 | HDI 不受样品电导率/离子强度变化影响 | Cianciulli 2012; Geurink 2021; Dawod 2017 |
| 基质独立 | EKI 进样量随样品缓冲液组成变化，HDI 不受影响 | Geurink 2021; Dawod 2017 |
| 非选择性进样 | EKI 按荷质比选择性进样，HDI 按比例进样所有组分 | Geurink 2021 |
| 更利于定量 | RSD < 2% 可实现，已演示 0.8% RSD | Cianciulli 2012; Geurink 2021 |
| 无样品偏差 | 所有分析物按浓度而非淌度比例进样 | Breadmore 2009 |

### EKI 相对 HDI 的优势

| 优势 | 说明 | 参考文献 |
|---|---|---|
| 固有样品堆叠 | 进样同时浓缩样品，提高灵敏度 | Geurink 2021 |
| 检测限更低 | 堆叠效应对稀样品提供更低 LOD | Zhu 2012 |
| 标准方法 | 商业 CE-SDS 试剂盒均围绕 EKI 设计 | SCIEX Application Guide |
| 进样更快 | 进样时间可更短（20 s vs. 100 s） | SCIEX SDS-MW Kit |
| 无压力相关凝胶扰动 | 避免凝胶移位或气泡形成风险 | General CE theory |

### 通用 CE 进样选择的参考

> Breadmore MC. "Electrokinetic and hydrodynamic injection: making the right choice for capillary electrophoresis." *Bioanalysis*, 2009 Aug; 1(5): 889–894. DOI: 10.4155/bio.09.73. PMID: 21083060.

该综述覆盖所有 CE 模式（不限于 CGE），结论是：HDI 通常更适合定量工作，因其独立于样品基质；EKI 通过堆叠提供更佳灵敏度，但代价是精密度和基质依赖。

## 生物制药与抗体 CGE 的进样模式现状

### 现行标准：EKI 是常态

mAb 纯度与异质性测试的主流 CE-SDS 方法使用电动力学进样，规定于：

- SCIEX IgG Purity/Heterogeneity Assay Kit（AB Sciex）：−5 kV、20 s EKI
- SCIEX SDS-MW Analysis Kit Application Guide：默认 EKI
- USP <129> "Analytical Procedures for Recombinant Therapeutic Monoclonal Antibodies"：引用 CE-SDS 与 EKI
- ProteinSimple Maurice 系统：基于 EKI 的卡盒式 CE-SDS

关键方法学参考：Felten C, Salas-Solano O. "CE-SDS, Technology Overview and Application to the Quality Control of Biopharmaceuticals"（SCIEX Technical Notes AIB-16384 和 AIB-16385）。

### HDI 用于 mAb CE-SDS：有限但已有演示

Cianciulli 等（2012）的研究确立了以下事实：

- HDI 在 CE-SDS 蛋白定量中的精密度更优（<2% RSD）
- 长序列运行（n = 48）中 HDI 的一致性优于 EKI
- 该方法可直接适用于 IgG 纯度分析

但未发现已发表的文献专门描述在已验证的制药 QC 环境中使用 HDI 进行 IgG 纯度测定或 F(ab')₂ 定量。HDI 的演示主要来自研发环境（疫苗蛋白分析）和精密度比较研究。

### 对 IgG 纯度 / F(ab')₂ 定量的适用性与方法转移要求

基于现有文献证据，HDI 在技术上应当可行：

1. 已在 mAb 分析所用的同一凝胶缓冲体系（SCIEX SDS-MW）中得到验证
2. 目标蛋白大小范围（IgG 片段、重链、轻链 25–150 kDa）落在已验证的病毒蛋白范围（14–75 kDa）之内
3. 精度改进对要求 RSD < 2% 的定量纯度测量尤其有价值

然而，从 EKI 转移至 HDI 需要重新优化：

- 进样压力与时间（在灵敏度充分与不过载之间权衡）
- 样品浓度（HDI 可能需要更高浓度以补偿堆叠的缺失）
- 新进样条件下的线性、准确度与精密度验证

## 商业仪器的压力进样支持

### 支持 HDI 的 CE 平台

- **SCIEX PA 800 Plus**：同时支持水动力与电动力学进样；压力进样范围 0.1–25 psi (6.9–1724 mbar)；标准 CE-SDS 方案使用 EKI，但硬件完全支持 HDI。van Tricht 与 Geurink 组均在 SCIEX 平台（AB Sciex CESI 8000 Plus）上完成了相关工作。
- **SCIEX BioPhase 8800**：8 毛细管 CE 系统，面向生物制药 QC；支持压力进样；标准 CE-SDS 方案使用 EKI，HDI 模式可用但未见于已发表的应用。
- **Agilent 7100 CE**：支持两种进样；标准压力进样最高 100 mbar（外部压力可更高）；Geurink 等（2021）在 100 mbar、100 s 条件下使用该系统开发 HDI-CGE 方法。
- **Lumex Capel 系列**：支持两种进样模式；在生物制药领域较少使用；HDI 技术上可能，但未发现已发表的 CE-SDS 应用。

### 仅支持 EKI 的平台

- **ProteinSimple Maurice / Maurice S**：预填充卡盒式 CE-SDS；进样为电动力学（内置于卡盒系统）；不支持用户配置的水动力进样。

## 结论与适用边界

| 问题 | 回答 |
|---|---|
| HDI 是否已用于 CGE 蛋白分析？ | 是。已在病毒疫苗蛋白（van Tricht 2015、Geurink 2021）以及蛋白定量（含 mAb 相关分析，Cianciulli 2012）中得到验证。 |
| 技术上是否可行？ | 是。凝胶粘度要求更高的压力 × 时间乘积（已报道 100 mbar × 100 s），但可与标准商业凝胶缓冲液配合使用。 |
| 是否优于 EKI？ | 精密度与基质独立方面是。HDI 的定量重复性更优（已演示 0.8% RSD），且不受样品离子强度影响；EKI 通过堆叠提供更好的灵敏度。 |
| 是否用于 mAb/IgG 纯度？ | 标准实践中没有。所有商业 mAb CE-SDS 试剂盒默认 EKI；Cianciulli 2012 在 mAb 相关的 CGE 语境中演示了 HDI 的精确蛋白定量，但未发现使用 HDI 的已验证 IgG 纯度 QC 方法。 |
| 哪些仪器支持？ | PA 800 Plus、BioPhase 8800、Agilent 7100 均支持 HDI 硬件；Maurice 不支持。 |
| HDI 在 CGE 中常见吗？ | 不常见，仅约 3 个主要研究组发表过相关工作；绝大多数 CE-SDS 文献采用 EKI。 |

需要指出的是，HDI 的灵敏度受限于缺乏堆叠效应，适用于同等重视定量精度与基质稳健性的场景，而非极低浓度样品的痕量分析。在 mAb 纯度 QC 中，HDI 尚缺乏已验证的应用案例，从 EKI 转移所需的重新优化与完整验证工作也未见报道，这是该方向尚未解决的主要问题。

## 参考文献

1. van Tricht E, Geurink L, Pajic B, Nijenhuis J, Backus H, Germano M, Somsen GW, Sänger-van de Griend CE. "New capillary gel electrophoresis method for fast and accurate identification and quantification of multiple viral proteins in influenza vaccines." *Talanta*, 2015 Nov 1; 144: 1030–1035. DOI: 10.1016/j.talanta.2015.07.047. PMID: 26452923.
2. Geurink L, van Tricht E, Dudink J, Pajic B, Sänger-van de Griend CE. "Four-step approach to efficiently develop capillary gel electrophoresis methods for viral vaccine protein analysis." *Electrophoresis*, 2021 Jan; 42(1-2): 10–18. DOI: 10.1002/elps.202000107. PMID: 32640046. PMCID: PMC7361255.
3. Cianciulli C, Hahne T, Wätzig H. "Capillary gel electrophoresis for precise protein quantitation." *Electrophoresis*, 2012 Nov; 33(22): 3321–3328. DOI: 10.1002/elps.201200177.
4. Dawod M, Arvin NE, Kennedy RT. "Recent advances in protein analysis by capillary and microchip electrophoresis." *Analyst*, 2017 May 30; 142(11): 1847–1866. DOI: 10.1039/c7an00198c. PMID: 28470231. PMCID: PMC5516626.
5. Breadmore MC. "Electrokinetic and hydrodynamic injection: making the right choice for capillary electrophoresis." *Bioanalysis*, 2009 Aug; 1(5): 889–894. DOI: 10.4155/bio.09.73. PMID: 21083060.
6. Zhu Z, Lu JJ, Liu S. "Protein separation by capillary gel electrophoresis: A review." *Analytica Chimica Acta*, 2012 Jan 6; 709: 21–31. DOI: 10.1016/j.aca.2011.10.022. PMCID: PMC3227876.
7. Stepanova S, Kasicka V. "Capillary Gel Electrophoresis of Proteins: Historical overview and recent advances." *TrAC Trends in Analytical Chemistry*, 2023; 162: 117024. DOI: 10.1016/j.trac.2023.117024.
8. Peng X, Chen DDY. "Variance contributed by pressure induced injection in capillary electrophoresis." *Journal of Chromatography A*, 1997; 767(1-2): 205–216. DOI: 10.1016/S0021-9673(96)01100-4.
9. Felten C, Salas-Solano O. "CE-SDS, Technology Overview and Application to the Quality Control of Biopharmaceuticals." SCIEX Technical Notes AIB-16384 and AIB-16385.

## 相关阅读

- [CE-SDS 中 IgG 纯度分析的压力进样可行性、电动进样稳定性策略与 PA800 Plus 参数优化](/posts/cge_injection_optimization_report)
