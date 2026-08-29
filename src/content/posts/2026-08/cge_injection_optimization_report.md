---
title: "CE-SDS 中 IgG 纯度分析的压力进样可行性、电动进样稳定性策略与 PA800 Plus 参数优化"
date: 2026-08-29
category: "05仪器与分析技术"
primaryTag: "05仪器与分析技术/Capillary-Electrophoresis"
description: "本文围绕 PA800 Plus 平台上 SDS-CGE 进样优化的完整评估展开：IgG 纯度/F(ab')₂ 分析的 CE-SDS 方法在序列运行中采用电动进样时出现峰面积递减。文章按问题背景与总体判断、压力（流体力学）进样可行性评估、电动进样八项稳定化策略、PA800 Plus"
tags:
  - "05仪器与分析技术/Capillary-Electrophoresis"
sourceNotes:
  - "Analytical technology/Capillary electrophoresis methods for pharmaceutical analysis/峰面积不稳定/CGE_Injection_Optimization_Report.md"
---

本文围绕 PA800 Plus 平台上 SDS-CGE 进样优化的完整评估展开：IgG 纯度/F(ab')₂ 分析的 CE-SDS 方法在序列运行中采用电动进样时出现峰面积递减。文章按问题背景与总体判断、压力（流体力学）进样可行性评估、电动进样八项稳定化策略、PA800 Plus 推荐方法参数与序列设计依次展开，最后给出根因诊断与分步行动方案。全文基于 12+ 篇同行评议文献、仪器厂商技术说明和专业学会工作坊报告整理。

## 问题背景与总体判断

SDS-CGE 方法用于 IgG 纯度/F(ab')₂ 分析，在一段序列运行中采用电动进样，出现峰面积渐进性下降。峰面积递减是生物制药 QC 实验室中记录充分的问题。根据文献，**凝胶缓冲液蒸发**是最常见的根因：溶剂蒸发使凝胶粘度、电导率和有效进样体积渐进变化。本报告评估三条路径：

1. **压力（流体力学）进样**——可行，但因粘性凝胶基质的实际限制，在标准 CE-SDS 中很少使用
2. **电动进样稳定化**——推荐方案，按有效性排序提出八项策略
3. **PA800 Plus 方法参数优化**——针对 IgG CE-SDS 纯度/异质性分析的具体参数

**核心建议：** Implement mineral oil overlay on gel buffer vials (Strategy #1) combined with corrected peak area normalization (Strategy #2) and gel buffer replenishment every 4–6 runs (Strategy #5). 这三项措施同时作用于根因及其分析后果。

## 压力进样的可行性评估

CGE 可以采用压力驱动进样，但行业标准仍是电动进样。关键挑战在于 SDS-CGE 使用的凝胶基质（通常为基于 PEG 或 dextran 的可更换聚合物溶液，含 SDS）粘度显著高于自由溶液 CE 的背景电解质，使压力进样"cumbersome" [1, 2]。

Cianciulli 等（2012）在 Agilent HP³D CE 系统上演示了 CE-SDS 蛋白分析的压力进样，定量精密度可接受 [3]，这是压力进样在 CGE 中的主要文献参考。Maurice 平台（Bio-Techne/ProteinSimple）则是压力进样的商业化实现：使用"橙色压力帽"进行压力驱动进样，并以 10 kDa 内标归一化 [4]。

### 进样体积与参数

压力进样体积遵循 **Hagen-Poiseuille 方程**：

```
V = (ΔP · π · d⁴ · t) / (128 · η · L)
```

其中 ΔP = 施加压力，d = 毛细管内径，t = 进样时间，η = 凝胶粘度，L = 毛细管总长。

| 参数 | 典型值 | 说明 |
|-----------|--------------|-------|
| **Applied pressure** | 0.5–5.0 psi (3.4–34.5 kPa) | Cianciulli used 4 bar (~58 psi) external pressure for rinsing; injection pressure is lower |
| **Injection time** | 3–10 seconds | ≥3 s recommended for precision [1] |
| **Capillary ID** | 50 µm | Standard for CE-SDS |
| **Gel viscosity** | ~50–200 cP (highly variable) | 10–100× higher than free-solution BGE; depends on polymer concentration and temperature |
| **Injection volume** | ~1–10 nL | Calculated; must not exceed ~1–2% of capillary volume |

Cianciulli 等方法的参数 [3]：

| 参数 | 值 |
|-----------|-------|
| Capillary | Bare fused-silica, 50 µm ID, 375 µm OD |
| Effective length (Leff) | 33 cm |
| Total length (Ltot) | 24.5 cm |
| Injection | Electrokinetic: −5 kV, 20 sec (primary method) |
| Separation voltage | −16.5 kV / −30 µA |
| Temperature | 25°C |
| Rinsing | 0.1 M NaOH → 0.1 M HCl → H₂O → SDS Gel Buffer, 4 bar external pressure |
| Detection | UV, 220 nm |
| Gel buffer | Beckman Coulter SDS Gel Buffer |
| Sample buffer | 100 mM Tris-HCl, 1% SDS, pH 8.0 |

### 压力进样与电动进样的对比

| 方面 | 压力（流体力学） | 电动 |
|--------|------------------------|----------------|
| **Precision** | Generally better; volume-based, non-discriminative | Mobility-dependent; discriminative based on charge/size |
| **Bias** | No mobility-based bias; representative injection | Preferentially injects higher-mobility species |
| **Sensitivity** | Lower (smaller injection plug possible) | Higher (can stack/concentrate via field amplification) |
| **Gel displacement** | Risk of pushing gel out of capillary inlet | No gel displacement |
| **Practicality** | Cumbersome with viscous gels; requires precise pressure control | Simple; standard practice |
| **Commercial support** | Maurice (Bio-Techne); limited on PA800 Plus for CE-SDS | Universal support across all CE-SDS platforms |
| **Reproducibility** | Dependent on pressure precision and gel viscosity consistency | Affected by sample conductivity, gel depletion, capillary surface |

### 压力进样的验证考虑

若在 PA800 Plus 或类似仪器上实施压力进样：

1. **Gel matrix displacement**——监测毛细管入口处的凝胶挤出（gel extrusion）；使用最低有效压力
2. **Injection volume calibration**——verify injected volume is within 1–2% of total capillary volume
3. **Viscosity monitoring**——凝胶粘度随温度和存放时间（age）变化，进样体积随之变化
4. **Comparability study**——与电动进样对全部目标分析物进行并排比较（side-by-side comparison）
5. **Regulatory**——any change from the validated electrokinetic method requires formal method transfer/validation per ICH Q2(R2)

**小结：** 压力进样**可行，但不推荐作为峰面积下降的主要解决方案**。峰面积下降更可能由凝胶缓冲液降解/蒸发引起——该因素影响两种进样模式——而非电动进样固有变异。稳定化电动进样更实用，商业方法支持也更充分。

## 电动进样稳定化的八项策略

以下策略按对"序列运行中峰面积渐进下降"这一具体问题的影响排序。

### 策略 1：凝胶缓冲液瓶矿物油覆盖（HIGHEST IMPACT）

凝胶缓冲液蒸发是序列运行中峰面积渐进下降的最常见根因。溶剂从仪器上敞开的凝胶缓冲液瓶中蒸发后，凝胶浓度升高，粘度和电导率随之增加，改变有效进样量（对 EKI 而言是场强变化；对两种模式而言迁移时间都会漂移）。MedImmune/SCIEX 合作研究（Shepherd 等）将其确认为迁移时间漂移的主要来源，并证明矿物油覆盖可消除该问题[5]。

实施要点：
- Add a thin layer (~200–500 µL) of light mineral oil (or use pre-prepared gel vials with oil overlay) to all gel buffer inlet and outlet vials
- Use fresh gel buffer vials with oil overlay at the start of each sequence
- Store gel buffer at 2–8°C; equilibrate to room temperature before use

预期效果：Eliminates the primary cause of progressive drift; migration time RSD improvement from >2% to <0.5% reported [5].

证据级别：Strong — demonstrated in commercial biopharma setting with PA800 Plus [5].

### 策略 2：校正峰面积（CPA）归一化（HIGH IMPACT）

CE 中不同淌度的分析物在检测窗口停留时间不同，快速迁移物种的原始峰面积成比例偏小。CE-SDS 定量必须进行速度校正[1, 6]。

```
CPA = Raw Peak Area / Migration Time

%CPA(species) = [CPA(species) / Σ CPA(all species)] × 100
```

实施：在 32 Karat™ 或 Empower™ 软件中启用速度校正峰面积，所有纯度结果以 %CPA 报告，而非原始 %area。这可以校正运行间迁移时间漂移造成的表观峰面积变化。

预期效果：相比未校正面积，表观峰面积变异性降低 30–60%。不解决底层物理问题，但归一化其分析影响。

证据级别：Strong — standard practice per USP, ICH, and all major biopharmaceutical CE-SDS methods [1, 6, 7].

### 策略 3：10 kDa 内标归一化（HIGH IMPACT）

10 kDa 蛋白内标与样品共迁移，承受相同的进样变异、凝胶状态变化和检测路径效应。将目标峰面积归一到内标可校正逐次进样和运行间变异[1, 4]。

实施要点：
- Add 10 kDa internal standard to every sample at a fixed concentration (per kit instructions; typically 5–10 µL of 10 kDa standard per 100 µL sample)
- 计算：Normalized CPA = CPA(target) / CPA(IS)
- 纯度分析用 %CPA（速度校正）通常足够；内标对绝对定量最关键
- The Maurice CE-SDS kit includes a "25X Internal Standard" for this purpose [4]

证据级别：Strong — standard practice in validated CE-SDS methods [1, 4, 7].

### 策略 4：毛细管调理优化（MODERATE-HIGH IMPACT）

裸熔融石英（bare fused-silica）毛细管内表面在重复分离中会退化，SDS-蛋白复合物可吸附于管壁，改变电渗流（EOF）和有效电场。严格的调理可在运行间恢复一致的表面状态[1, 8]。

新毛细管首次使用：

| 步骤 | 试剂 | 时间 | 压力 |
|------|---------|------|----------|
| 1 | 0.1–1.0 M NaOH | 10–20 min | 20–50 psi |
| 2 | Deionized water | 5–10 min | 20–50 psi |
| 3 | 0.1 M HCl | 5–10 min | 20–50 psi |
| 4 | Deionized water | 5 min | 20–50 psi |
| 5 | SDS Gel Buffer | 10 min | 20–50 psi |

运行间调理（方法预调理）：

| 步骤 | 试剂 | 时间 | 压力 |
|------|---------|------|----------|
| 1 | 0.1 M NaOH | 2–5 min | 20 psi |
| 2 | 0.1 M HCl | 2–5 min | 20 psi |
| 3 | Deionized water | 2 min | 20 psi |
| 4 | Fresh SDS Gel Buffer | 5 min | 20 psi |

- Some methods use NaOH only (no HCl); optimization may be method-specific
- Cianciulli et al. used the full NaOH → HCl → H₂O → Gel Buffer sequence [3]
- Track capillary lifetime; replace every 100–200 injections or when system suitability fails

证据级别：Strong — universal CE best practice [1, 3, 8].

### 策略 5：凝胶缓冲液更换计划（MODERATE-HIGH IMPACT）

即使有矿物油覆盖，入口和出口凝胶缓冲液中的 SDS 和凝胶聚合物也会因电迁移和残留逐渐消耗。定期更换新鲜凝胶可保证分离条件一致[5, 6]。

| 方式 | 频率 | 说明 |
|----------|-----------|----------|
| **Conservative** | Every 4 runs | Recommended for critical GMP/QC work |
| **Standard** | Every 6 runs | Most common industry practice |
| **Extended** | Every 8–10 runs | Acceptable with mineral oil overlay and short separations |

实施：将凝胶缓冲液瓶更换编入 PA800 Plus 方法序列；冲洗与分离使用独立胶瓶防止交叉污染；预填充的替换瓶加矿物油覆盖。

证据级别：Moderate-strong — industry best practice; specific frequency depends on method [5, 6, 9].

### 策略 6：严格控温 25°C（MODERATE IMPACT）

Gel viscosity changes ~2–3% per °C [1, 10]。对电动进样，粘度直接影响电导率和进样量；对分离则影响迁移时间和分辨率。PA800 Plus 使用循环液体冷却毛细管卡盒，但环境温度波动会影响样品/缓冲液瓶。

实施要点：
- Set capillary cartridge temperature to 25.0°C (standard for CE-SDS)
- Ensure laboratory ambient temperature is controlled (20–25°C, ±2°C)
- Allow gel buffer and samples to equilibrate to room temperature before loading
- 关键工作中可考虑将缓冲液/样品盘置于温控仓内

证据级别：Moderate — well-established principle; Guttman & Filep demonstrated temperature effects on CE-SDS resolution [10].

### 策略 7：样品制备一致性（MODERATE IMPACT）

电动进样有选择性——进样量取决于样品的离子强度、电导率和分析物淌度。样品基质在制备间的差异会导致进样变异[1, 2]。

实施要点：
- Prepare all samples at identical protein concentration (typically 1.0 mg/mL for IgG)
- Use consistent sample buffer: 100 mM Tris-HCl, 1% SDS, pH 8.0 (or per kit instructions)
- Heat denature at 70°C for 10 min (non-reduced) or 100°C for 5 min (with β-mercaptoethanol/DTT for reduced)
- 使用一次性样品瓶——电动进样会耗尽毛细管尖端附近的样品，不要从同一瓶重复进样
- 加热后离心去除颗粒；保持瓶内样品体积一致（影响液面高度和进样）

证据级别：Moderate — standard CE-SDS sample preparation practice [1, 6, 7].

### 策略 8：预平衡与支架（bracketing）运行（MODERATE IMPACT）

新调理毛细管的前 1–3 次运行常表现出与后续运行不同的迁移时间和峰面积。预平衡"驯化"系统可消除序列早期离群值[8, 9]。

实施要点：
- Run 2–3 blank or system suitability standard injections before the sample sequence
- Bracket samples with system suitability standards (e.g., IgG control standard every 6 samples)
- 系统适用性标准：
  - Migration time RSD ≤ 2.0% (or ≤ 1.0% for RMT with IS)
  - %CPA of main peak ≤ ±2.0% absolute from reference
  - Peak area of IS ≤ ±10% from initial value
- Discard pre-equilibration run data

证据级别：Moderate — standard analytical practice; recommended in CASSS CE Pharm troubleshooting workshops [9].

### 策略优先级汇总

| Rank | Strategy | Impact on Peak Area Decline | Implementation Effort | Addresses Root Cause? |
|------|---------------------------|---------------------------|--------------------|----------------------|
| 1 | Mineral oil overlay | ⭐⭐⭐⭐⭐ | Low | **Yes** — prevents gel evaporation |
| 2 | CPA normalization | ⭐⭐⭐⭐ | Low | No — corrects data mathematically |
| 3 | 10 kDa internal standard | ⭐⭐⭐⭐ | Low | No — normalizes injection variability |
| 4 | Capillary conditioning | ⭐⭐⭐⭐ | Medium | Partially — maintains capillary surface |
| 5 | Gel buffer replenishment | ⭐⭐⭐⭐ | Medium | **Yes** — prevents gel depletion |
| 6 | Temperature control | ⭐⭐⭐ | Low | Partially — eliminates thermal drift |
| 7 | Sample prep consistency | ⭐⭐⭐ | Medium | Partially — reduces injection variability |
| 8 | Pre-equilibration runs | ⭐⭐⭐ | Low | No — removes initial instability |

## PA800 Plus 方法参数与序列设计

以下为 IgG CE-SDS 纯度/异质性分析的推荐参数，区分标准法与高速（High-Speed, HS）法。

### 标准非还原 CE-SDS 方法参数

| 参数 | 标准方法 | 高速（HS）方法 | 说明 |
|----------------|-----------|----------------------|-------|
| **Instrument** | PA800 Plus (SCIEX) | PA800 Plus or BioPhase 8800 | |
| **Capillary** | Bare fused-silica, 50 µm ID, 375 µm OD | Same | |
| **Effective length (Leff)** | ~20 cm | ~10 cm | Cartridge-dependent |
| **Total length (Ltot)** | ~30 cm | ~20 cm | Cartridge-dependent |
| **Injection mode** | Electrokinetic | Electrokinetic | Reverse polarity (cathode at inlet) |
| **Injection voltage** | −5 kV | −5 kV | Negative polarity |
| **Injection time** | 20 seconds | 10–20 seconds | ≥3 s for precision |
| **Separation voltage** | −15 kV | −15 to −16.5 kV | Constant voltage mode |
| **Separation current limit** | ~30 µA | ~30 µA | Current limit for safety |
| **Separation time** | 25–35 min | 8–12 min | Until all peaks elute |
| **Capillary temperature** | 25°C | 25°C | Liquid-cooled cartridge |
| **Detection** | UV, 220 nm | UV, 220 nm | PDA optional |
| **Gel buffer** | SDS-MW Gel Buffer (SCIEX/Beckman Coulter, P/N 390953) | Same | Replaceable polymer solution |
| **Sample buffer** | SDS-MW Sample Buffer (100 mM Tris-HCl, 1% SDS, pH 8.0) | Same | P/N 390955 |
| **10 kDa Internal Standard** | 10 kDa protein standard | Same | P/N 390961 |
| **Denaturing conditions** | 70°C, 10 min (non-reduced); 100°C, 5 min (reduced with β-ME) | Same | |
| **Sample concentration** | 1.0 mg/mL (typical) | 0.5–2.0 mg/mL | Optimize for sensitivity vs. overloading |

### 方法预调理（运行间）

| 步骤 | 操作 | 试剂 | 压力 | 时长 |
|------|------|------|---------|----------|
| 1 | Forward rinse | 0.1 M NaOH | 20 psi | 3 min |
| 2 | Forward rinse | 0.1 M HCl | 20 psi | 1 min |
| 3 | Forward rinse | Deionized water | 20 psi | 1 min |
| 4 | Forward rinse | SDS Gel Buffer | 70 psi | 5 min |
| 5 | Wait | — | — | 5 min (equilibration) |
| 6 | Dip | Water vial | — | — (remove excess at capillary tip) |

*Note: Some optimized methods omit the HCl step or adjust pressures/times. The above reflects the Cianciulli/Wätzig protocol adapted for PA800 Plus [3].*

### 序列结构

| 位置 | 样品类型 | 目的 |
|------------|---------------------------|-------------|
| 1–3 | Blank / SDS Gel Buffer | Pre-equilibration (discard data) |
| 4 | System suitability standard (IgG) | Verify migration time, peak area, resolution |
| 5–10 | Samples | Analytical runs |
| 11 | System suitability standard (IgG) | Bracketing standard |
| — | **Replace gel buffer vials** | Every 4–6 injections |
| 12–17 | Samples | Analytical runs |
| 18 | System suitability standard (IgG) | Final bracket |

### 系统适用性标准

| 参数 | 接受标准 | 计算 |
|-------------------|---------------------|-----------|
| Migration time RSD (IS) | ≤ 2.0% | Across all runs in sequence |
| Relative migration time (RMT) RSD | ≤ 1.0% | Target peak MT / IS MT |
| %CPA main peak (reference standard) | ≤ ±2.0% absolute from expected | (CPA_main / CPA_total) × 100 |
| IS peak area RSD | ≤ 10% | Across all runs in sequence |
| Resolution (LC–HC or specific pair) | ≥ 1.5 | Per pharmacopeial requirements |

### 凝胶缓冲液更换方案

| 参数 | 建议 |
|-----------|---------------|
| Replenishment frequency | Every 4–6 injections |
| Mineral oil overlay | 200–500 µL light mineral oil per vial |
| Gel buffer storage | 2–8°C; equilibrate to RT before use |
| Gel buffer expiry (opened) | Use within 30 days (per kit insert) |
| Separate rinse vs. separation vials | Yes — prevents depletion of separation vials |

### BioPhase 8800 多毛细管性能基准

作为参考，SCIEX BioPhase 8800（8-capillary system）在 CE-SDS IgG 方法上达到以下精密度[11]：

| 指标 | Inter-capillary RSD |
|---------------------|---------------|
| Relative migration time (RMT) | < 0.38% |
| Corrected peak area % (%CPA) | < 0.30% |
| Migration time (absolute) | < 0.50% |

## 峰面积下降的诊断与行动方案

### 最可能的根因排序

按文献，峰面积递减的最可能原因依次为：

1. **凝胶缓冲液蒸发**——仪器上的敞口瓶在数小时内损失溶剂，浓缩凝胶并改变电导率，改变有效进样量和迁移行为[5]
2. **凝胶缓冲液耗竭**——重复分离和冲洗消耗缓冲液瓶中的 SDS 和聚合物[5, 6]
3. **毛细管表面退化**——SDS-蛋白复合物在管壁渐进吸附，改变 EOF 和进样行为[8]
4. **温度漂移**——长序列中环境温度变化导致粘度、进样和分离变异[10]

### 分步行动方案

**第 1 步（当天）——实施矿物油覆盖：**
- 向所有凝胶缓冲液瓶（入口和出口）加入 200–500 µL 矿物油
- 运行标准序列，与之前序列的峰面积趋势对比
- 预期：峰面积渐进下降显著减少或消除

**第 2 步（当天）——确认 CPA 归一化：**
- 确认数据系统（32 Karat / Empower）报告的是速度校正峰面积
- 若报告原始面积，改为 CPA = area / migration time
- 纯度以 %CPA 报告

**第 3 步（一周内）——优化序列结构：**
- 在样品前加入 2–3 次预平衡运行
- 每 6 个样品插入支架标准（bracketing standards）
- 每 4–6 次运行设置一次凝胶缓冲液瓶更换
- 定义并应用系统适用性标准（见上文）

**第 4 步（一周内）——检查毛细管调理：**
- 确认运行间预调理包含 NaOH → HCl → water → fresh gel buffer
- 跟踪毛细管使用次数；在 ≤200 次注射或 SST 失败时更换

**第 5 步（问题持续时）——考虑硬件替代方案：**
- BioPhase 8800：多毛细管、高通量、精密度更好
- Maurice：压力进样、集成内标、工作流更简单
- 两个平台都能规避 PA800 Plus 手动静电进样优化的许多难点

## 参考文献

1. SepScience. "Injection precision and sensitivity in CE — key considerations." SepScience, 2024. Available: https://www.sepsci.com/knowledge/injection-precision-and-sensitivity-in-ce/

2. Breadmore MC. "A Combinatorial Approach to Injection in CE." *Bioanalysis*. 2009;1(5):889–894. doi:[10.4155/bio.09.73](https://doi.org/10.4155/bio.09.73)

3. Cianciulli C, Wätzig H. "Hydrodynamic and electrokinetic injection in capillary electrophoresis for the analysis of pharmaceutical proteins." *Electrophoresis*. 2012;33(22):3321–3330. doi:[10.1002/elps.201200177](https://doi.org/10.1002/elps.201200177). PMID: [22969056](https://pubmed.ncbi.nlm.nih.gov/22969056/)

4. Bio-Techne/ProteinSimple. "Maurice CE-SDS Application Guide." Available: https://resources.bio-techne.com/bio-techne-assets/docs/literature/Maurice_CE-SDS_Application_Guide.pdf

5. Shepherd R, et al. (MedImmune/SCIEX). "Mineral Oil Overlay for Improved Migration Time Reproducibility in CE-SDS." SCIEX Technical Note. Available: https://sciex.com/content/dam/SCIEX/pdf/tech-notes/all/Medimmune_TN.pdf

6. Felten C, Salas-Solano O. "CE-SDS Method Development and Robustness." SCIEX Technical Note AIB-16385. Available: https://sciex.com/content/dam/SCIEX/pdf/tech-notes/ce1/AIB-16385.pdf

7. Pettit DK, Krull IS, Toby TK. "Separation and Characterization of Proteins and Antibodies by Capillary SDS–Gel Electrophoresis." *Chromatographia*. 2006;64(1):1–8. doi:[10.1365/s10337-006-0825-7](https://doi.org/10.1365/s10337-006-0825-7)

8. SepScience. "Capillary conditioning in CE — best practices." SepScience, 2024. Available: https://www.sepsci.com/knowledge/capillary-conditioning-in-ce/

9. Sänger-van de Griend CE, Blanc T. "Troubleshooting CE-SDS: Baseline Disturbances, Peak Area Repeatability and the Presence of Ghost Peaks." CASSS CE Pharm 2015 Workshop Report. Available: https://www.casss.org/docs/default-source/ce-pharm/reports-troubleshooting-workshops/troubleshooting-ce-sds---baseline-disturbances---peak-area-repeatability-and-the-presence-of-ghost-peaks.pdf

10. Guttman A, Filep C. "Fine-Tuning Temperature for CE-SDS Separation of New Modality Biotherapeutics." SCIEX Technical Note. Available: https://sciex.com/content/dam/SCIEX/pdf/tech-notes/all/TN-CE-SDS-temperature.pdf

11. SCIEX. "BioPhase 8800 Multi-Capillary Electrophoresis System — IgG Purity Precision Study." SCIEX Technical Note MKT-33259-A. Available: https://sciex.com/content/dam/SCIEX/pdf/tech-notes/biopharma/MKT-33259-A_High_speed_method_from_PA_800_to_BP_V5.11.6.24.pdf

12. Zhu Z, Lu JJ, Liu S. "Protein separation by capillary gel electrophoresis: A review." *Analytica Chimica Acta*. 2012;709:21–31. doi:[10.1016/j.aca.2011.10.022](https://doi.org/10.1016/j.aca.2011.10.022)