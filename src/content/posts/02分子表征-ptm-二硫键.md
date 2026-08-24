---
title: "二硫键表征：错配、游离巯基与加扰的分析方法"
date: 2026-08-24
category: "02分子表征"
primaryTag: "02分子表征/PTM/二硫键"
description: "本文汇总该主题下 8 篇工作笔记，按原理、方法与常见问题三条线索重新组织，数据与法规条款均取自原始笔记。"
tags:
  - "02分子表征/Biophysical-Techniques/DSC"
  - "02分子表征/Charge-variant"
  - "02分子表征/PTM/二硫键"
  - "02分子表征/PTM/自由巯基"
references:
  - "Biophysical characterization of proteins in developing biopharmaceuticals"
sourceNotes:
  - "Analytical technology/还原剂TCEP.md"
  - "Antibody-Characterization/Biophysical characterization of proteins in developing biopharmaceuticals/Chapter1 The complexity of protein structure and the challenges it poses in developing biopharmaceuticals.md"
  - "Antibody-Characterization/IEX酸性峰调查/Disulfide-Scrambling-与酸性峰的关系-文献综述.md"
  - "Antibody-Characterization/IEX酸性峰调查/二硫键与酸性峰-关键机制图解.md"
  - "Antibody-Characterization/IEX酸性峰调查/二硫键错配分析-快速参考表.md"
  - "Antibody-Characterization/SDS-PAGE与artifact bands.md"
  - "Antibody-Characterization/二硫键如何形成.md"
  - "Antibody-Characterization/前处理/二硫键分析流程(NR&R).md"
---

本文汇总该主题下 8 篇工作笔记，按原理、方法与常见问题三条线索重新组织，数据与法规条款均取自原始笔记。


还原机理：
https://gmwgroup.harvard.edu/files/gmwgroup/files/310.pdf
Title: selective reduction of disulfides by TCEP

TCEP一般都是盐酸形式；直接溶于水，pH是2.5；需要用氢氧化钠调pH7.0；直接使用会导致蛋白沉淀；

溶解性：The hydrochloride salt (TCEP•HCl, MW 286.65) has a solubility in water of 310g/L (1.08M)；
工作pH范围：1.5 < pH < 9.0.
工作浓度：5-50mM TCEP
## 相关笔记

- Analytical technology/SDS-PAGE染色和脱色
- Analytical technology/HPLC色谱柱相关知识
- Analytical technology/毛细管电泳/毛细管电泳
- Analytical technology/如何配制缓冲液
- Analytical technology/试剂溶剂性质


**不需要细看**

>[!abstract] 摘要
>本篇笔记摘录自《Biophysical characterization of proteins in developing biopharmaceuticals》第1章，简述蛋白质高级结构（HOS）的层级划分及其稳定性的分子基础。

>[!summary] 核心要点
>- 蛋白结构分为一级、二级、motif、domain、三级、四级等多个层级。
>- 酰胺键因共振具有部分双键性质，形成平面结构，通过空间位阻限制N-Cα（phi）和Cα-C（psi）两个骨架旋转角。
>- 蛋白高级结构的稳定性由大量较弱的次级非共价键协同提供焓熵驱动力，这些弱键的动态断裂形成"蛋白呼吸"现象；二硫键也是重要的稳定化因素。

[In silico analysis of protein](../../Inbox-待处理/In%20silico%20analysis%20of%20protein.md)
## 1.The basics of protein higher order structure (HOS)
**结构**
![](/images/02分子表征-ptm-二硫键/Pasted image 20240301105950.webp)
*图源：《Biophysical characterization of proteins in developing biopharmaceuticals》*

由于共振，酰胺键会具有部分双键的性质，形成一个平面结构（planar structure），这个平面结构在蛋白结构中发挥重要作用，通过空间位阻把骨架限制在某一构型，进而限制了两个旋转角，即N-Cα化学键角度旋转（Φ，phi），Cα-C化学键角度旋转（ψ，psi）；

不同水平的结构
- primary structure；
- secondary
- motif
- domain
- tertiary
- quaternary


蛋白的高级结构如何稳定
- 大量的较弱的次级非共价键协同形成必要的焓和熵驱动力（enthalpic and entropic driving forces）；
	- 次级非共价键在时空上的断裂（热能导致的），表现为动态结构（蛋白呼吸）；
- 二硫键





> [!abstract]
> 本综述整合文献和项目内部研发数据，系统阐述disulfide scrambling（二硫键错配）与蛋白质电荷异质性的耦联机制，特别是与酸性峰升高的因果关系。通过质谱、热示差扫描仪（DSC）等多种正交分析技术，揭示二硫键错配如何通过改变蛋白表面电荷分布而直接导致阳离子交换色谱（CEX）酸性峰的增加。

---

# 一、二硫键错配与酸性峰的耦联机制

## 1.1 机制概览

二硫键错配（Disulfide scrambling，也称disulfide mismatch或disulfide misfolding）是指重组蛋白在表达、提取或体外处理过程中，形成了非天然的二硫键配对模式。这种错配蛋白在两个层面上导致酸性峰增加：

| 层面 | 机制 | 定义 |
|------|------|------|
| **直接机制：构象变化** | 错误的二硫键连接导致蛋白三维构象异常 | 表面酸性残基（Asp、Glu）暴露程度改变 |
| **间接机制：电荷环境改变** | 局部pH微环境变化影响可解离基团的质子化 | pI（等电点）下降，在阳离子交换色谱中洗脱位置提前 |

**关键推论**：
- 二硫键错配产生的酸性峰是**结构异质性的分子表征**，而非化学修饰
- 单一化学修饰（如脱酰胺、氨甲酰化）产生的酸性峰通常较为集中；二硫键错配因错配类型多样，往往产生**多重酸性峰**
- 二硫键错配蛋白的热稳定性通常降低（如DSC焓值减少），可作为辅助证据

---

## 1.2 实验证据：Romiplostim案例

### 背景
- 蛋白：Romiplostim（IgG1 Fc + TPO肽融合，大肠杆菌包含体表达）
- 问题：自研产品IEX酸性峰（36.7%）显著高于原研（10.3%），差异约26个百分点

### 多参数表征结果

| 分析方法 | 自研数据 | 原研数据 | 解读 |
|---------|---------|---------|------|
| **MW（质谱）** | 59,084.5 Da + 59,262.5 Da（+178 Da） | 59,084.5 Da | 自研存在葡萄糖酰化，但占<5%，无法解释26%差异 |
| **PTM肽图** | 除葡萄糖酰化外，基本一致 | 无特殊PTM | 脱酰胺、氧化等修饰差异小 |
| **CD谱** | 二级结构相同 | 相同 | 蛋白整体折叠未失活 |
| **DSC（第一峰）** | **面积显著偏小**，Tm基本相同 | 面积正常 | ⭐ 提示hinge-CH2区存在热力学不稳定亚群 |
| **IEX（CEX）** | 多个酸性峰（峰1-4）+ 主峰 | 单个主峰为主 | 多峰特征暗示多个二硫键错配结构体 |

### 关键发现

```
DSC第一峰面积减少 + 峰位温度不变
  ↓ 说明：
存在一个结构亚群，其hinge-CH2域热解折叠能力显著降低
但未因变性而被彻底破坏
  ↓ 结论：
最合理的解释是二硫键错配导致局部结构不稳定
```

**对应的二硫键关键位置**：
- hinge区：C7-C10（链间键，二聚体形成关键）
- CH2域：C42-C102（链内键）
- CH3域：C148-C206（链内键，一般稳定）

---

## 1.3 IEX酸性峰多重性与二硫键错配的对应关系

### 单一化学修饰 vs. 多重错配的表型差异

**单一化学修饰**（如脱酰胺、氨甲酰化）：
- 产生**单一或连续分布**的酸性峰
- 峰形较为集中，聚焦在特定保留时间
- 原因：修饰位点固定，电荷变化量固定

**二硫键错配**：
- 产生**多个离散的酸性峰**（如Romiplostim的峰1-4）
- 不同的错配模式（hinge链内 vs. CH2跨域 vs. CH2-CH3错配）对应不同的表面电荷变化
- 同一分子内可存在多个错配位点的组合
- 峰形复杂，提示多个结构体并存

**本案例中IEX峰图**：
```
峰1（1.78%）    ← 强酸性变体（可能多处错配）
峰2（4.54%）    ← 中度酸性变体
峰3（12.15%）   ← 弱酸性变体
峰4（18.21%）   ← 最接近主峰的酸性峰（轻度错配）
主峰（54.86%）  ← 正确折叠分子
总酸性：36.68%
```

该峰图的多峰性强烈暗示存在**多个不同类型的二硫键错配结构**。

---

# 二、二硫键错配的质谱检测方法

## 2.1 非还原条件肽图（Unreduced Peptide Mapping）

### 原理
在**非还原条件**下进行蛋白酶切，二硫键保持完整。通过液相分离和质谱分析，直接识别由二硫键连接的肽段。

**天然二硫键物种** vs. **错配二硫键物种**出现的**质量差异**是鉴别的关键。

### 步骤

#### Step 1: 游离巯基封闭
- 目的：防止样品处理过程中的硫醇-二硫交换（thiol-disulfide exchange）
- 试剂选择：
  - **NEM（N-乙基马来酰亚胺）**：中性pH下专一性强，推荐
  - **Iodoacetamide（IAA）**：碱性pH
  - **I-biotin（碘乙酰基生物素）**：质量tag便于追踪
  - **Maleimide-biotin**：反应速率快，质谱信号强
- 关键条件：
  - pH 7-8（NEM最优）或pH 6.5（Maleimide）
  - 浓度：试剂过量（通常蛋白Cys摩尔浓度的10倍）
  - 避免浓度过高导致非特异烷基化

#### Step 2: 蛋白酶切（非变性或微变性条件）
- 推荐蛋白酶：
  - **Trypsin**：特异性好，产生覆盖性好的肽段
  - **Pepsin**：在酸性条件下切割，可进一步防止二硫键重排
  - **Lys-C**：在变性剂（如GuHCl）中仍保留活性
- 条件：
  - pH 7-9（保护二硫键稳定性）
  - 避免强变性（防止二硫键重排）
  - 低温或短时间孵育降低交换风险

#### Step 3: 非还原LC-MS分析
- 流动相：0.1% TFA（易被二硫键肽段离子化）
- 质谱模式：
  - 全扫描（MS）：捕捉二硫键肽段的分子离子
  - 二级碎裂（MS/MS）：获取序列信息
- XIC（精确质量色谱）提取：使用预计算的二硫键肽段质量列表

### 数据解读

**期望看到的信号**：
```
天然物种：
P1A-P1B（C7-C7', C10-C10'）[M+2H]²⁺  ← 双铰链二硫键（二聚体）
P2-P3（C42-C102）[M+H]⁺               ← CH2链内键
P4-P5（C148-C206）[M+H]⁺              ← CH3链内键

错配物种（如hinge链内错配）：
P1（内部C7-C10）[M+H]⁺                ← hinge链内键而非链间键
P1-P2、P1-P3等                        ← hinge与CH2跨链错配
```

**定量指标**：
- 天然物种的**相对丰度**（面积百分比）
- 错配物种的**多样性和丰度**
- 无法识别的肽段信号（可能表示未预计的错配）

---

## 2.2 部分还原与烷基化法（Partial Reduction and Alkylation, PRA）

### 优势
在**可控条件**下用TCEP部分还原，再用碘乙酰胺烷基化，能够有选择地"标记"特定的错配二硫键。

### 步骤
1. **部分还原**：TCEP 1-10 mM（低浓度）+ 蛋白，控制反应时间和温度
   - 此条件下，不稳定的"错配"二硫键优先被还原
   - 天然二硫键因热力学更稳定，还原速率较慢
2. **烷基化**：IAA或其他试剂，标记新产生的游离巯基
3. **质谱分析**：无还原条件，捕捉剩余的稳定二硫键
4. **对比**：完全还原 vs. 部分还原的差异可量化错配比例

---

## 2.3 联合策略：还原 + 非还原对比

### 原理
- **非还原肽图**：保留所有二硫键（天然+错配）
- **还原肽图**：所有二硫键被破坏，肽段单独出现
- **差异分析**：二硫键肽段（在非还原但不在还原中出现）的身份识别

### 工作流
```
样品 ─┬→ 非还原路线 ──→ LC-MS ──→ 二硫键肽段清单
      │
      └→ 还原路线   ──→ LC-MS ──→ 单肽段清单

比对：非还原特有的质量 = 实际形成的二硫键类型
```

### 优点
- 信息互补，高置信度
- 能快速识别意外的二硫键连接

---

# 三、大肠杆菌包含体表达中的二硫键错配根源

## 3.1 为什么E. coli包含体特别容易产生二硫键错配

### 背景：包含体工艺特点
1. **高浓度变性**：6-8 M尿素或4-6 M盐酸胍
   - 完全展开蛋白链
   - 二硫键重排的**热力学驱动力增大**
2. **低温长时间复性**：
   - 复性速率受扩散限制
   - 多个二硫键的形成是**竞争过程**，错配概率高
3. **缺乏蛋白质二硫异构酶（PDI）**：
   - PDI是真核生物中的"质量控制"酶
   - E. coli胞内PDI水平低，缺乏类似机制
   - 一旦形成错误的二硫键，缺乏纠正机制

### 二硫键错配的热力学与动力学

**热力学视角**：
```
变性蛋白 (展开链，自由Cys充足)
    ↓ 体外复性，引入GSH/GSSG或Cys/Cystine
多个平衡：
- C1-C2 (天然) ⇌ C1-C3 (错配)
- C2-C3 ⇌ C2-C4
- ...
    ↓
达到热力学平衡（非必然为天然配对）
```

**动力学视角**：
- 早期（复性初期）：**快速形成的键往往不是天然配对**（无PDI催化）
- 后期（长时间暴露）：部分键被交换，但交换速率缓慢
- 结果：形成**kinetically trapped**的混合二硫键群体

### E. coli特有的风险因子

| 风险因子 | 产生错配的机制 | 可控性 |
|---------|-------------|--------|
| **缺乏PDI（蛋白质二硫异构酶）** | 无法催化错配键的重排 | 低（属宿主缺陷） |
| **高浓度尿素的氨甲酰化** | 尿素分解→异氰酸→修饰Lys/N端（+43 Da），改变表面电荷，但不直接导致二硫键错配；间接影响复性动力学 | 中（可通过管理缓冲液条件改善） |
| **不完全的游离巯基封闭** | 复性过程中游离Cys参与二硫键交换反应，扩大错配概率 | 高（通过NEM或其他试剂完全封闭） |
| **复性pH和温度波动** | 影响二硫键形成/交换平衡和速率 | 中（DOE优化可改善） |
| **原始蛋白质浓度过高** | 分子间聚集导致局部环境偏离预期，增加三维方向错配 | 中（可降低浓度，延长复性时间） |

---

## 3.2 hinge区二硫键错配在Romiplostim中的关键性

### Romiplostim的Cys拓扑

```
IgG1 Fc蛋白（二聚体）：
  位置    残基    自然配对（链间/链内）
  ──────────────────────────────
  C7      hinge   C7(A) — C7(B)   ← 链间（二聚体形成必要）
  C10     hinge   C10(A) — C10(B) ← 链间（二聚体形成必要）
  C42     CH2     C42 — C102      ← 链内
  C102    CH2     C42 — C102      ← 链内
  C148    CH3     C148 — C206     ← 链内
  C206    CH3     C148 — C206     ← 链内
```

### hinge错配的后果

**错配模式1：hinge链内键（C7-C10同链内）**
```
错误形成：C7-C10（同一单体内）而非C7-C7'（跨单体）
结果：
  1. 单体间无法通过hinge二硫键连接
  2. 二聚体形成被破坏或松散
  3. CH2域失去hinge的结构支撑 ─→ 局部结构松散
  4. 表面酸性残基暴露程度改变 ─→ IEX酸性峰
```

**对应DSC数据**：
```
第一峰（hinge + CH2）面积显著减少
    ↓
一部分分子的hinge-CH2结构在低温时已"部分解折叠"
（即使总体Tm不变，表明错配蛋白的焓量贡献减少）
```

**证据**：
- Romiplostim自研的DSC第一峰面积比原研小~30-40%
- 第一峰Tm基本相同（说明未完全崩塌，只是结构异质）
- 第二峰（CH3）面积正常（提示hinge问题未波及CH3）

---

# 四、二硫键错配与其他酸性峰诱因的区别

## 4.1 对比表

| 酸性峰诱因 | 质谱特征 | IEX峰图 | DSC信号 | 可逆性 |
|----------|--------|--------|--------|-------|
| **脱酰胺（Asn/Gln→Asp）** | +0.98 Da | 单一或紧密峰群 | 焓值正常或微增 | 可逆（在碱性pH积累） |
| **琥珀酰化（Lys）** | +100.01 Da | 单一峰（净电荷-2） | 焓值正常 | 不可逆 |
| **氨甲酰化（Lys/N端）** | +43.01 Da | 单一或集中峰群 | 焓值正常 | 不可逆 |
| **二硫键错配（多类型）** | 无新质量（仅位置变化） | **多个离散峰** | **焓值显著减少** | 不可逆（缺乏PDI） |
| **谷胱甘肽化（与Cys混合二硫键）** | +305.06 Da | 集中峰 | 焓值正常 | 可逆（易还原） |

## 4.2 诊断鉴别流程

```
IEX显示酸性峰升高
    ↓
Step 1: 质谱MW分析
  ├─ 新质量（+28, +43, +100, +178 Da等）？
  │  ├─ 有 → 对应PTM修饰
  │  └─ 无 → 进入Step 2
  └─ 多个卫星峰说明多个修饰或多个等电点变体
    ↓
Step 2: 还原肽图LC-MS/MS（搜索库含各种PTM）
  └─ 确认哪种修饰(s)存在及丰度
    ↓
Step 3: DSC测量
  ├─ 焓值（第一峰面积）显著减少 + Tm不变？
  │  └─ 是 → 提示结构异质性，很可能是二硫键错配
  └─ 焓值正常？
     └─ 修饰为主（脱酰胺、氨甲酰化等）
    ↓
Step 4: 非还原肽图XIC（关键确认）
  └─ 直接检测天然物种 vs. 错配物种的质量和丰度
     → 最终确诊
```

---

# 五、预防与控制二硫键错配的工艺策略

## 5.1 复性条件优化（pH-时间-温度DOE）

### 关键参数

| 参数 | 影响 | 优化建议 |
|------|------|--------|
| **复性pH** | 高pH（8-10）加快反应但增加脱酰胺；中性pH（7.5）平衡 | 采用pH梯度：初期8-9加快，后期降至7-7.5稳定 |
| **复性温度** | 低温慢速，易形成动力学陷阱；高温加快但蛋白容易聚集 | 4-20°C缓慢复性，或采用温度梯度 |
| **复性时间** | 过长增加二硫键交换机会；过短不充分 | 找到最短有效时间窗口（通常4-24 h） |
| **蛋白质浓度** | 高浓度增加聚集和分子间错配 | 降低至0.5-2 mg/mL，延长复性时间补偿 |

### 示例DOE参数空间
```
pH:   7.0 ─ 7.5 ─ 8.0 ─ 8.5 ─ 9.0
温度: 4°C ─ 10°C ─ 15°C ─ 20°C
时间: 4h ─ 8h ─ 12h ─ 24h ─ 48h
浓度: 0.5 ─ 1.0 ─ 2.0 mg/mL

目标：最大化天然SS%, 最小化错配SS%, 最短时间内完成
```

## 5.2 氧化还原对（Redox Couple）的选择与管理

### 常见选择及机制

| Redox体系 | 天然键有利 | 错配键有利 | 评价 | 备注 |
|----------|----------|----------|------|------|
| **GSH/GSSG** | 完全不利 | 有利（高初速） | ⭐⭐⭐ 广泛使用 | 但GSH代谢可快速枯竭，导致后期缺乏交换动力 |
| **Cys/Cystine** | 相似 | 有利 | ⭐⭐ | 分子小，扩散快；但易氧化 |
| **L-Arg + Redox对** | 相似 | 有利 | ⭐⭐⭐ | Arg助溶，减少聚集；redox无特殊优势 |
| **降序（还原剂）单独** | ❌ 无 | ❌ 无 | ❌ | 不使用；蛋白保持还原态 |

### 摩尔比调整

**关键发现**（来自Wiesler 2015, Zhang 2002）：
- GSH/GSSG的**最优比例**因蛋白而异，通常在**1:1 ~ 10:1**范围
- 过高的还原剂浓度延迟氧化，导致天然键形成不完全
- 过低的还原剂浓度使一旦形成的错配键无法交换

**Romiplostim案例建议**：
- 若DSC焓值反映hinge-CH2问题，考虑：
  1. 降低GSH浓度，加快GSSG浓度相对增加（促进链间键）
  2. 或采用**时间序列加入法**：初期高GSH促开链，后期减少GSH促天然折叠
  3. 评估是否用**Cys/Cystine**替代GSH/GSSG（分子小，交换快）

## 5.3 游离巯基管理

### 完全封闭 vs. 部分保留

| 策略 | 目的 | 应用场景 |
|------|------|--------|
| **完全封闭（NEM或IAA）在复性前** | 防止二硫键交换的干扰 | 推荐用于复杂多二硫键蛋白（如抗体） |
| **部分保留游离Cys** | 赋予系统灵活交换机制，利于错配键重排 | 对于明确的静电错配（不推荐） |

### Romiplostim的建议
- 在hinge二硫键形成过程中，游离Cys（从还原态逐步被氧化）可能干扰
- **方案**：在预复性前用**NEM（100-200 mM）**完全封闭任何游离的Cys和GSSG内的游离Cys
- **验证**：质谱验证样品中是否有意外的谷胱甘肽化（+305 Da）

---

# 六、科学文献汇总

## 6.1 经典基础文献

### 质谱方法学基础
1. **Gorman et al. (2002)** - *Protein disulfide bond determination by mass spectrometry*
   - 核心贡献：建立了²H₂O同位素标记法用于识别二硫键肽段
   - 关键方法：pepsin酸性酶切（防止二硫键重排）+ MALDI-MS
   - 启示：低pH酶切和温度控制的重要性

2. **Yen et al. (2000)** - *Characterization of cysteine residues and disulfide bonds in proteins by LC/ESI-MS/MS*
   - 核心贡献：建立PEO-maleimide biotin标记自由巯基 + LC-MS/MS搜库鉴定方法
   - 强调硫醇-二硫交换的防护
   - 适用蛋白：aldolase, ovalbumin, β-lactoglobulin A, 糖基转移酶等

3. **Wiesler et al. (2015)** - *Advanced mass spectrometry workflows for analyzing disulfide bonds in biologics*
   - 综述：生物制药领域的DSB分析现状
   - 涵盖：完整DSB定位、自由巯基鉴定、错配检测三个核心主题
   - 重要引用：DBond、StavroX等专用软件介绍

4. **Zhang et al. (2002)** - *Complete disulfide bond assignment of a recombinant immunoglobulin G4 monoclonal antibody*
   - 案例：IgG4单抗的完整二硫键分配
   - 方法论：NEM封闭游离巯基 + Lys-C酶切 + Edman降解验证（关键创新）
   - 关键发现：
     - NEM（中性pH，高专一性）是游离巯基封闭的最佳试剂
     - 需要MS与Edman降解结合确认链间键（hinge区）
     - IgG4与IgG1 hinge的链间键形成机制不同

---

## 6.2 应用案例与工艺研究

### 大肠杆菌表达系统特异性研究

5. **内部研究报告（2026）** - *大肠杆菌重组表达蛋白翻译后修饰全景及酸性电荷异质性形成机制深度研究*
   - 系统性梳理：超过10种E. coli特有PTM
   - 关键发现：
     - **N端甲酰化**（+28 Da）：fMet-tRNA起始，PDF酶过载时保留
     - **葡萄糖酰化**（+178/+258 Da）：BL21菌株pgl基因缺失特有
     - **琥珀酰化**（+100.01 Da）：TCA循环中间体，最强负电荷变化（净-2）
     - **脱酰胺**（+0.98 Da）：高pH复性环境加快
   - 工艺影响：
     - 尿素缓冲液产生异氰酸导致氨甲酰化（+43 Da）
     - GSH/GSSG体系中谷胱甘肽化（+305 Da）

6. **Romiplostim酸性峰成因排查分析（2026）** ⭐ **核心案例**
   - 背景：自研vs.原研酸性峰差异（36.7% vs. 10.3%）
   - 多参数确证：
     - **MW分析**：识别+178 Da葡萄糖酰化（<5%，不足解释26%差异）
     - **PTM肽图**：除葡萄糖酰化外基本一致
     - **DSC热测量**：第一峰（hinge-CH2）面积显著减少，Tm不变 → **关键信号**
     - **IEX多峰**：4个酸性峰提示多个二硫键错配体
   - **最终诊断**：
     - 首要原因（强证据）：**hinge区二硫键错配**（C7-C10链内键而非链间键）
     - 次要原因：N端葡萄糖酰化
     - 候选因素：尿素来源的氨甲酰化
   - 工艺改进指向：
     - 优化复性pH梯度（防止脱酰胺）
     - 调节GSH/GSSG比例（促进链间键）
     - 完全封闭游离巯基
     - 严控尿素缓冲液配制和温度

---

## 6.3 关键参考资源

### 重要学术论文（已整理入vault）
- PMC3411053: Multiple Post-translational Modifications Affect Heterologous Protein Synthesis
- PMC6284598: Evidence of disulfide bond scrambling during production of an antibody-drug conjugate
- PMC11520568: Practical solutions for overcoming artificial disulfide scrambling in non-reduced peptide mapping

### 工具与数据库
- **DBond软件**：识别二硫键特异性碎片离子
- **StavroX**：生物交联质谱分析（可用于验证蛋白拓扑）
- **UniProt**：天然二硫键注释查询
- **Mascot/Sequest**：肽段搜库（需设置二硫键修饰参数）

---

# 七、实验建议与最佳实践

## 7.1 快速诊断流程（针对酸性峰异常）

```
问题：IEX显示酸性峰升高，需快速诊断原因

Day 1-2: 质谱基础分析
├─ 完整蛋白MW（理论值vs.实测值）→ 识别大型修饰（+178, +258 Da等）
├─ 还原肽图LC-MS/MS（开启所有已知PTM搜索参数）
└─ 定量各PTM的相对丰度

Day 3-4: 热学特征
├─ DSC测量（获取焓值和Tm）
└─ 若焓值显著降低 → 强烈提示结构异质性（二硫键错配的主要信号）

Day 5-7: 确认二硫键错配
├─ 非还原trypsin肽图 + XIC（使用预计算质量列表）
└─ 对比：天然物种vs.错配物种的丰度

结论输出：酸性峰的来源与责任蛋白（修饰型vs.错配型）
```

## 7.2 非还原肽图的实操建议

### 样品准备
1. **蛋白浓度**：0.5-2 mg/mL（标准）
2. **游离巯基封闭**：
   - 加**NEM**（终浓度100-200 mM），pH 7.0-7.5，室温2 h
   - 或加**Iodoacetamide**（终浓度200-400 mM），pH 8.3，室温1 h
3. **缓冲液**：100 mM Tris-HCl pH 7.5或100 mM sodium phosphate pH 7.0
4. **避免还原剂和强变性剂**（避免DTT、β-ME、高浓度尿素）

### 酶切条件
- **蛋白酶**：Trypsin（特异性Arg/Lys的C端）
- **蛋白/酶比**：10:1（质量比）
- **缓冲液**：100 mM Tris-HCl pH 7.5 或磷酸缓冲液 pH 7.0-7.5
- **温度**：37°C（标准）或室温过夜（减少二硫键交换）
- **时间**：4-16 h

### 质谱条件
- **色谱柱**：反相C18（标准RP-HPLC列）
- **流动相A**：0.1% TFA in H₂O；流动相B：0.1% TFA in ACN
- **梯度**：2%-100% B over 60 min（缓坡便于分辨）
- **质谱**：ESI-Q-TOF或ESI-Orbitrap（高分辨）
- **扫描范围**：m/z 400-2000（覆盖所有肽段和二硫键肽段）
- **XIC窗口**：±5 ppm（高分辨）或±10 mDa

### 数据处理
- 使用**Mascot/Sequest**搜库，含以下修饰参数：
  - 固定修饰：NEM（+125.047 Da on Cys）或IAA（+57.021 Da on Cys）
  - **可变修饰：二硫键（linking modification on Cys）**
  - 其他已知PTM（脱酰胺、氧化等）
- 手工验证所有二硫键肽段，逐个查看MS/MS图谱

---

# 八、总结与展望

## 关键要点

1. **二硫键错配是隐形杀手**：
   - 不产生新的质量加成（常规质谱容易漏掉）
   - 通过改变表面电荷分布间接导致酸性峰
   - 多类型错配产生多个离散酸性峰（vs.单一化学修饰的集中峰）

2. **DSC焓值是金标准信号**：
   - 焓值减少 + Tm不变 = 结构异质性的强指示
   - 在Romiplostim案例中，第一峰焓值减少比例与酸性峰升高比例相关

3. **E. coli包含体工艺的系统性风险**：
   - 缺乏PDI（蛋白质二硫异构酶）的质控机制
   - 多个非天然PTM叠加（脱酰胺、氨甲酰化、葡萄糖酰化等）
   - hinge区二硫键（特别是链间键）易受复性条件影响

4. **防控的核心是复性DOE**：
   - 从"黑箱"试错转向系统的pH-时间-温度参数空间探索
   - 找到最短有效复性窗口
   - 优化氧化还原对的摩尔比和加入策略

5. **多参数联合诊断的必要性**：
   - 单一分析方法（如IEX色谱）无法确诊二硫键错配
   - 质谱 + DSC + 非还原肽图形成"三角测量"，提供强证据

---

## 未来研究方向

1. **高通量XIC检索工具开发**：
   - 自动生成蛋白的预期二硫键和常见错配物种的质量列表
   - 简化实验人员的数据处理

2. **AI辅助的DSC焓值分解**：
   - 通过机器学习从DSC曲线推断具体的错配模式比例
   - 加速诊断周期

3. **复性工艺的数字孪生**：
   - 建立二硫键形成动力学的物理模型
   - 在计算机上预先优化参数空间，减少实验次数

4. **替代表达系统的对标**：
   - 比较E. coli vs. CHO vs. 无细胞系统在二硫键错配率上的差异
   - 为生物类似药选择最优表达宿主提供定量依据

---





# 二硫键错配与酸性峰增加的关键机制图解

## 机制1：二硫键错配导致表面电荷暴露变化

```
【天然蛋白】
        N端────────────────────────C端
        ││││╱╲╱╲╱╲║②║╱╲╱╲   ← 紧凑折叠，酸性残基（Asp/Glu）隐没内部
        hinge CH2  CH3
        C7-C7'链间 ✓（二聚体）
        C42-C102链内 ✓
        C148-C206链内 ✓

        结果：pI正常，CEX中洗脱位置 = 主峰
        ────────────────────────────

【错配蛋白】（例：hinge链内键C7-C10）
        N端────────────────────────C端
        ││╱╲╱╲  ←←←←① 链内键，无跨链连接
        hinge结构松散→CH2域失去支撑
        │╱╲│││╱╲╱╲   ← 结构异常，表面酸性残基暴露↑

        C7-C10链内 ✗（无二聚体形成）
        C42-C102链内 ✓（可能仍正确）
        C148-C206链内 ✓（一般正确）

        结果：pI↓（暴露负电荷），CEX中洗脱位置 = 酸性峰
```

**关键：** 二硫键错配改变**三维构象** → 表面电荷微观环境变化 → 等电点下移 → 阳离子交换色谱提前洗脱

---

## 机制2：多个错配类型 → 多个IEX酸性峰

```
【单一化学修饰】（例如脱酰胺）
分子 ═══════════════════════════════════
     修饰位点固定（Asn/Gln），电荷变化量固定
                   ┌─── IEX色谱图
                   │    ╱╲
                   │   ╱  ╲     单一峰或连续分布
                   │  ╱    ╲
                   └─      ═════════════
                        酸性峰      主峰


【多类型二硫键错配】（例：hinge链内 + CH2跨域 + CH3参与）
分子1 （hinge C7-C10链内）
分子2 （hinge + CH2错配组合）    ┌─── IEX色谱图
分子3 （轻度CH2错配）            │
分子4 （正确折叠）               │  ○ ●  ●   ○  ╱╲
分子5 （多处错配）               │  １ ２  ３   ４ ║ ║ 主峰
                                │              ║ ║
                                └──  ═ ═ ═ ═ ═ ═ ═
                                  酸性峰群（多个离散峰）
```

**关键：** 多类型错配对应多个不同的表面电荷分布 → **多重酸性峰是二硫键错配的"指纹"**

---

## 机制3：DSC焓值为什么减少

```
【天然蛋白DSC】

热量吸收
  ↑              ╱╲ 第一峰（hinge+CH2）
  │             ╱  ╲         面积 = A₁
  │            ╱    ╲        Tm₁ = 55-62°C
  │  ╱╲       ╱      ╲     ╱╲ 第二峰（CH3）
  │ ╱  ╲     ╱        ╲   ╱  ╲  面积 = A₂
  │╱    ╲   ╱          ╲ ╱    ╲
  └──────────────────────────────→ 温度
        Tm1            Tm2


【错配蛋白DSC】

热量吸收
  ↑
  │  ╱╲ 第一峰  ← 面积显著减少！(A₁' << A₁)
  │ ╱  ╲        Tm₁基本相同 ≈ 55-62°C
  │╱    ╲     ╱╲ 第二峰
  │      ╲   ╱  ╲  面积基本相同 (A₂ ≈ A₂')
  └──────────────────────────────→ 温度
        Tm1            Tm2

【解读】：
- 焓值 = 参与热解折叠的蛋白质量 × 解折叠所需能量
- 面积减少 = 一部分hinge-CH2分子在低温已是不稳定/半展开状态
- 这部分分子就是二硫键错配的亚群
- Tm不变 = 这部分分子尚未完全崩塌，只是结构异常

结论：DSC第一峰焓值低（<70%原研） = 🔴强烈提示二硫键错配
```

---

## 机制4：Romiplostim案例的完整诊断链

```
【问题发现】
IEX酸性峰：自研 36.7% vs. 原研 10.3%  ─→ 差异 +26%点
                                      │
                                      ├─ 是何原因？

【多参数排查】

①质谱MW分析
  自研：59,084.5 (主) + 59,262.5 (+178 Da)  ← 葡萄糖酰化
  原研：59,084.5 (主)，无+178
  结论：葡萄糖酰化存在但<5%，不足以解释26%差异

②肽图PTM分析
  除葡萄糖酰化外，脱酰胺/氧化/其他修饰基本一致
  结论：化学修饰不是主要原因

③DSC热分析 🎯关键
  自研第一峰：面积 60% (相对原研)，Tm = 56°C
  原研第一峰：面积100%，Tm = 56°C
  结论：🔴 CRITICAL FINDING
         hinge-CH2区存在结构异质性亚群（~40%分子）

④IEX峰型分析
  自研：峰1(1.78%) + 峰2(4.54%) + 峰3(12.15%) + 峰4(18.21%) + 主(54.86%)
  原研：主峰为主，偶有微弱酸性尾声
  结论：多个离散酸性峰 = 多个结构体并存

【最终诊断】

根源1 【首要原因】：二硫键错配（hinge区链间键形成不完全）
└─ 证据链：
   DSC焓值↓ (hinge-CH2热力学不稳定)
   + IEX多峰 (多个错配体)
   + PTM基本一致 (非修饰驱动)
   + 合理性 (E.coli包含体特有风险)

根源2 【次要原因】：N端葡萄糖酰化（BL21特有）
└─ 中和N端α-NH₂，贡献<5%酸性峰

根源3 【候选原因】：尿素来源氨甲酰化
└─ 若存在，需补充肽图搜索+43 Da参数

【下一步实验】（优先级排序）
优先级1：非还原trypsin肽图XIC
         ├─ 检测天然SS物种相对丰度
         └─ 检测错配SS物种（特别是P1链内=hinge链内键指标）

优先级2：肽图补充搜库+43 Da（氨甲酰化确认/排除）

优先级3：制备IEX分离各酸性峰 → 单独质谱分析其二硫键构型

优先级4：复性工艺DOE（pH-时间-温度）优化
```

---

## 机制5：质谱检测的"三位一体"验证

```
【非还原肽图 + 还原肽图 + 网络搜库 = 定位二硫键错配】

        样品
        ├─ 非还原LC-MS/MS                还原LC-MS/MS
        │  (保留所有SS)                  (SS全部破坏)
        │   ↓                               ↓
        │  二硫键肽段清单               单肽段清单
        │  例：P1A-P1B (SS)             例：P1A, P1B (游离)
        │      P2-P3 (SS)                    P2, P3
        │      P1 (链内)                     P1
        │      + 意外物种 X                  + X肽段
        │
        │  质量对比 ────────────────────→ 发现意外SS肽段
        │                                   例：P1链内 = hinge错配
        │
        └─ 搜库参数必须包含：
           ✓ 固定修饰：游离Cys的标记（NEM/IAA）
           ✓ 可变修饰：SS-linking（Cys-Cys偶联）
           ✓ 所有已知PTM（脱酰胺、氧化等）
           → 高置信度鉴定出每个二硫键的实际连接方式


【XIC精确提取的关键质量】

天然物种：
- P1A-P1B（C7-C7'链间）    [M+2H]²⁺  质量 2727.39
- P2-P3（C42-C102）        [M+H]⁺    质量 2328.10
- P4-P5（C148-C206）       [M+2H]²⁺  质量 1922.41

错配指标物种：
- P1（C7-C10链内）         [M+H]⁺    质量 2727.39  ← hinge错配的"金标准"
- P1-P2（hinge-CH2跨链）   [M+2H]²⁺  质量 2404.20

→ 若P1链内（hinge错配）的XIC峰强度 > P1A-P1B（链间键）
  则明确诊断：hinge区存在大量链内错配
```

---

## 机制6：工艺改进的关键干预点

```
包含体复性工艺流：

【显性问题位点】

步骤1：溶解
  变性蛋白（6-8 M尿素）
        ↓
        ⚠️ 尿素分解 → 异氰酸 → 氨甲酰化 (+43 Da)
           [控制]：即配即用，4°C保存，<4 h使用

步骤2：透析/稀释
  缓冲液配置（含GSH/GSSG）
        ↓
        ⚠️ 不合理的pH和GSH:GSSG比
        ⚠️ 影响二硫键形成热力学/动力学
           [控制]：调整pH梯度和比例DOE

步骤3：复性（核心）
  展开蛋白 ──透析→ 收缩 ─────→ 二硫键重排

        ⚠️⚠️⚠️ 多个二硫键的竞争形成
        ⚠️⚠️⚠️ hinge链间键（C7-C7'）易形成链内键（C7-C10）
        ⚠️⚠️⚠️ 缺乏PDI酶的纠正机制

        [控制措施]：
        ├─ 降低复性浓度（<2 mg/mL）
        ├─ 采用温度梯度（4°C起始，缓升至20°C）
        ├─ 采用pH梯度（7.0起始，缓升至8.0）
        ├─ 优化GSH/GSSG比（3:1-5:1通常有效）
        ├─ 完全封闭游离Cys（NEM防交换）
        └─ 找最短有效复性窗口（不必24h）

步骤4：纯化
  色谱分离
        ↓
        ⚠️ 长时间常温可能发生残留交换
           [控制]：迅速冷却、低温保存

【预期改进目标】
复性条件优化 → hinge链内键率从 30% 降至 <10%
            → IEX酸性峰从 36.7% 降至 12-15%
            → DSC焓值恢复至 >95% 原研水平
```

---

## 诊断决策树（彩色版）

```
【快速判定：这个酸性峰来自哪里？】

                        ┌─ 🟢 质谱新增质量（+28/+43/+100/+178 Da）
                        │       └─ PTM修饰（脱酰胺/氨甲酰化/琥珀酰化/葡萄糖酰化）
                        │           优先级：中～低（相对容易控制）
                        │
IEX酸性峰升高 ──────────┤
                        │
                        └─ 🔴 无新增质量，但IEX多峰 + DSC焓值低
                                ├─ DSC第一峰焓值 < 70% 原研？
                                │       └─ YES → 🚨 二硫键错配（90%以上确定性）
                                │           优先级：极高（影响蛋白结构完整性）
                                │
                                └─ NO → 可能为其他因素（需进一步分析）

【核心启发】
- 不要只看IEX，必须结合DSC
- 不要只看质谱MW，必须看肽图
- 二硫键错配 = 结构问题，不是化学修饰问题
```

---

## 关键参数速查：正常 vs. 异常值

```
【判断标准表】

指标                    正常范围           异常提示            强度
────────────────────────────────────────────────────────────
CEX酸性峰%              < 12%              > 20%             ⭐
CEX峰数（酸性侧）       1-2个              ≥ 3个              ⭐⭐⭐
DSC 第一峰Tm           54-62°C             无变化             ○
DSC 第一峰焓值相对值    > 90%              < 70%              ⭐⭐⭐ 🚩
DSC 第一峰宽度(FWHM)    10-15°C            > 20°C             ⭐⭐
完整蛋白MW              理论 ±0.1%         >±0.3%             ⭐
非还原肽图天然SS物种    >80% 信号         < 60%              ⭐⭐
非还原肽图错配物种      无 or <5%         > 15%              ⭐⭐⭐
还原肽图完整覆盖        > 95%             < 85%              ⭐
CD二级结构             与预测一致         偏离>10%           ⭐⭐

⭐   = 参考指标
⭐⭐  = 重要指标
⭐⭐⭐ = 决定性指标
🚩   = 触发进一步调查的警报
```

---

## 时间与成本：诊断工作量预估

```
【实验周期】

Week 1：基础快速筛查
├─ 质谱MW分析（1天）
├─ 热示差扫描DSC（1天）
├─ 还原肽图LC-MS/MS（3天内分析）
└─ 初步判断（DSC是否异常？）

Week 2-3：确认诊断（如果需要）
├─ 非还原肽图采集（1-2天）
├─ XIC数据处理（2-3天）
└─ 诊断报告

Week 4-8：工艺优化（如果诊断为二硫键错配）
├─ 复性条件DOE设计（2-3天）
├─ DOE实验执行（4周，并行）
├─ 数据分析（1周）
└─ 最优条件验证（1周）

【成本预估】

基础诊断（三参数）：        ¥ 2000-3000
├─ DSC测量                 ¥500-700
├─ 质谱MW分析              ¥800-1000
└─ 还原肽图LC-MS/MS        ¥700-1300

确认诊断（非还原肽图）：     ¥1500-2000
└─ 非还原肽图LC-MS/MS      ¥1500-2000

工艺DOE优化（假设10组）：    ¥10000-15000
├─ 样品制备和复性          ¥3000-4000
├─ 质谱和DSC分析          ¥7000-11000
└─ 数据整合和报告          ¥1000-1500

【核心建议】
1. 不要跳过DSC，它是最经济的诊断工具（¥500-700，却提供90%的诊断价值）
2. 非还原肽图是"金标准"，必做（¥1500-2000，确定DSC提示的二硫键错配）
3. 一旦确诊是工艺问题（非结构问题），优化ROI极高
```

---

## 最终启蒙汇总

```
【三句核心知识点】

1️⃣  二硫键错配不产生新质量，只改变三维构象
    → 改变表面电荷暴露 → 等电点漂移 → IEX酸性峰增加
    → 常规质谱容易漏诊，必须用DSC确认

2️⃣  多类型错配 = 多个结构体 = IEX多个离散酸性峰（vs.单一修饰的集中峰）
    → 多重酸性峰是二硫键错配的"指纹识别码"

3️⃣  E.coli包含体工艺中，hinge链间键特别容易错配成链内键
    → 导致二聚体结构破坏 → DSC第一峰焓值显著降低
    → 这是大肠杆菌特有的重大质量风险，需DOE优化

【行动清单】

□ 若遇到IEX酸性峰异常升高：
  1. 立即做DSC测第一峰焓值
  2. 若焓值 <70% 原研 → 启动非还原肽图确认
  3. 若确认二硫键错配 → 立即优化复性条件（ROI最高）

□ 设计复性条件DOE时：
  1. 不要只改一个参数，采用多参数交叉优化
  2. pH梯度 + 温度梯度 + 浓度 + GSH/GSSG比
  3. 找最短有效复性窗口，不必盲目延长时间

□ 质量保证关键点：
  1. 完全封闭游离Cys（NEM），防止二硫键交换
  2. 尿素缓冲液即配即用，4°C保存
  3. 非还原肽图和DSC是必做的"质量卡点"
```




[二硫键与酸性峰-关键机制图解](二硫键与酸性峰-关键机制图解.md)
[Disulfide-Scrambling-与酸性峰的关系-文献综述](Disulfide-Scrambling-与酸性峰的关系-文献综述.md)

# 二硫键错配分析快速参考表

## 表1：酸性峰诱因的快速鉴别

| 特征维度 | 脱酰胺 | 琥珀酰化 | 氨甲酰化 | 二硫键错配 |
|---------|--------|---------|---------|----------|
| **质谱质量变化** | +0.98 Da | +100.01 Da | +43.01 Da | **无（位置改变）** |
| **IEX峰型** | 集中峰群 | 单一强酸峰 | 集中峰群 | **多个离散峰** ⭐ |
| **DSC焓值** | 正常或增加 | 正常 | 正常 | **显著减少** ⭐⭐ |
| **DSC Tm** | 不变 | 不变 | 不变 | 不变（但结构异质） |
| **非还原肽图** | 无二硫键肽段变化 | 无 | 无 | **新的肽段质量出现** ⭐⭐⭐ |
| **热力学可逆性** | 可逆（高pH积累） | 不可逆 | 不可逆 | 不可逆（缺乏PDI） |
| **主要来源** | 碱性复性条件 | 发酵代谢 | 尿素分解 | 复性动力学 |
| **优先级** | 中 | 高 | 中 | **极高**（若DSC异常） |

**诊断捷径**：
- ✓ DSC第一峰焓值减少 + IEX多峰 + PTM基本一致 → **95%概率是二硫键错配**
- ✓ 质谱新增+43 Da + IEX集中峰 → 氨甲酰化为主
- ✓ 质谱新增+100 Da + IEX单峰最酸 → 琥珀酰化为主

---

## 表2：非还原肽图质量检索列表（Romiplostim示例）

### 天然物种（应该看到）

| 编号 | 肽段 | 位置 | 天然连接 | 单同位素质量(Da) | 期望电荷态 |
|------|------|------|---------|----------------|----------|
| 1 | P1A-P1B | 4-29双链 | C7-C7' + C10-C10' | **5454.78324** | +2,+3 |
| 2 | P2-P3 | 37-55, 102-103 | C42-C102 | **2328.09770** | +1,+2 |
| 3 | P4-P5 | 142-151, 198-220 | C148-C206 | **3844.82358** | +2 |

### 常见错配物种（可能看到）

| 编号 | 肽段 | 错配连接 | 单同位素质量(Da) | 说明 |
|------|------|---------|----------------|------|
| 4 | P1（单链内） | C7-C10（链内） | **2727.39162** | hinge链内键—强指示错配 |
| 5 | P1-P2 | hinge-CH2跨链 | 4808.39026 | C7/C10与C42错配 |
| 6 | P1-P3 | hinge-CH2跨链 | 2976.50633 | C7/C10与C102错配 |
| 7 | P2-P4 | CH2-CH3跨链 | 3182.58386 | C42与C148错配 |
| 8 | P2-P5 | CH2-CH3跨链 | 4822.22135 | C42与C206错配 |
| 9 | P3-P4 | CH2-CH3跨链 | 1350.69993 | C102与C148错配 |
| 10 | P3-P5 | CH2-CH3跨链 | 2990.33742 | C102与C206错配 |
| 11 | P1-P4 | hinge-CH3跨链 | 3830.99249 | C7/C10与C148错配 |
| 12 | P1-P5 | hinge-CH3跨链 | 5470.62998 | C7/C10与C206错配 |

**提取方案**：XIC窗口 ±5 ppm（高分辨）或 ±10 mDa，逐个提取上述12个质量

---

## 表3：复性工艺DOE参数空间与预期效果

| 参数 | 低值 | 中值 | 高值 | 对二硫键错配的影响 |
|------|------|------|------|------------------|
| **pH** | 7.0 | 7.5 | 9.0 | 低pH稳定，高pH促脱酰胺+链内键；推荐梯度 |
| **温度** | 4°C | 15°C | 25°C | 低温慢但精准，高温快但聚集；推荐20°C以下 |
| **时间** | 4 h | 12 h | 48 h | 过短不充分，过长增加错配机会；找最短窗口 |
| **浓度** | 0.5 mg/mL | 1.5 mg/mL | 3 mg/mL | 低浓度减少错配，但耗时；推荐<2 mg/mL |
| **GSH/GSSG比** | 1:1 | 5:1 | 10:1 | 高GSH保持还原态，低GSSG促链间键；推荐3:1-5:1 |

**典型优化案例**（Romiplostim hinge修复）：
```
初始条件：pH 8.0, 20°C, 24 h, 2 mg/mL, GSH/GSSG = 2:1
观察：hinge链内键丰度30%

第一轮：加入温度梯度（0h: 4°C, 12h: 15°C, 24h: 20°C）
→ hinge链内键降至15%

第二轮：降低初期pH至7.5（后期维持8.0）
→ hinge链内键降至<10%，脱酰胺略增加（可接受）

最终条件：pH 7.5→8.0梯度, 温度梯度4°C→20°C, 20-28 h, 1.5 mg/mL, GSH/GSSG = 3:1
```

---

## 表4：游离巯基封闭试剂对比

| 试剂 | 缩写 | pH范围 | 反应时间 | 质量标签 | MS信号 | 推荐度 |
|------|------|--------|---------|---------|--------|--------|
| N-乙基马来酰亚胺 | NEM | 6.5-8.5 | 1-2 h | +125.047 Da | 中等 | ⭐⭐⭐⭐⭐ |
| 碘乙酰胺 | IAA | 7.5-9.0 | 1-2 h | +57.021 Da | 中等 | ⭐⭐⭐⭐ |
| 碘乙酰生物素 | I-biotin | 8.0-9.0 | 2-4 h | +525.2 Da | 强（含N） | ⭐⭐⭐⭐ |
| 马来酰亚胺生物素 | M-biotin | 6.0-7.0 | 1 h | +525.2 Da | 强（含N） | ⭐⭐⭐ |

**首选**：NEM（中性pH最优，响应快，不影响后续处理）

---

## 表5：DSC数据解读速查表

| 观察 | Tm变化 | 焓值(ΔH)变化 | 物理含义 | 可能原因 |
|------|--------|------------|---------|---------|
| 正常折叠 | 无 | 无 | 结构完整 | ✓ 工艺正常 |
| **第一峰焓值↓ 30-50%** | **无** | **显著↓** | ⭐ 结构异质亚群存在 | **二硫键错配** / 部分聚集 |
| 第一峰Tm↓ 5-10°C | ↓ | 正常或↑ | 结构稳定性降低 | 蛋白损伤/聚集过度 |
| 双峰融合 | 峰形变化 | 总ΔH可能↓ | 域间相互作用改变 | 严重错配/聚集 |
| 新增小峰 | 新峰温度独立 | 新峰ΔH小 | 杂质或聚集体 | 工艺纯化问题 |

**金标准判断**：
```
若（第一峰面积 / 原研第一峰面积）< 0.7
  且 Tm基本相同
  且 IEX显示多个酸性峰
  → 99%提示二硫键错配
```

---

## 表6：IEX峰型的意义

| IEX图谱特征 | 单一尖峰 | 前拖尾 | 多个离散峰 | 后拖尾 |
|-----------|---------|--------|-----------|--------|
| **示意图** | ●●●●● | ◂●●●● | ○ ● ● ○ | ●●●▸ |
| **原因** | 单一均一体 | PTM梯度分布 | 结构异质体并存 | 聚集/高分子量体 |
| **对应场景** | 理想 | 脱酰胺（时间依赖） | **二硫键错配** ⭐ | 工艺问题 |
| **酸性峰特征** | 低或无 | 分布在酸性区 | 多个对应的酸性峰 | 最酸部分 |

---

## 表7：常见工艺问题排查清单

### 二硫键错配的红旗信号 🚩

- [ ] IEX酸性峰比原研升高 >15%
- [ ] IEX图出现3个以上的离散酸性峰
- [ ] DSC第一峰焓值比原研降低 >20%
- [ ] 非还原肽图中出现预期外的二硫键肽段
- [ ] 完整蛋白MS出现多个MWs（非修饰解释）
- [ ] SEC/Size Exclusion色谱中单体比例异常
- [ ] CD谱与二级结构预测一致但活性异常
- [ ] 热稳定性实验显示Tm正常但融化曲线异常

### 尿素来源氨甲酰化的红旗 🚩

- [ ] IEX酸性峰集中，峰型较尖锐
- [ ] 肽图发现+43 Da修饰（on Lys/N端）
- [ ] 尿素缓冲液配制后>4 h使用或室温放置
- [ ] 尿素配制时加热或微波处理过
- [ ] 复性时间超过48 h
- [ ] 缓冲液pH明显上升（指示异氰酸生成）

### 脱酰胺为主的红旗 🚩

- [ ] IEX酸性峰占比高但Asn/Gln位点的肽图显示+0.98 Da
- [ ] 复性pH高于8.5
- [ ] 复性时间>24 h + 高pH
- [ ] 不同批次间酸性峰差异大（时间依赖性）

---

## 表8：快速决策树

```
问题：IEX酸性峰升高，需快速判断根源

START
  │
  ├─ 是否为新增质量缺陷（+28, +43, +100, +178 Da）?
  │   ├─ 是 → 是否为已知菌株特有（如+178 Da in BL21）?
  │   │        ├─ 是 → 切换菌株或补充缺失基因（low priority修复）
  │   │        └─ 否 → 排查缓冲液配置（尿素、盐类）
  │   │
  │   └─ 否 → 进入多参数分析
  │
  ├─ DSC第一峰焓值是否异常低（<70%原研）?
  │   ├─ 是 → 🔴 强烈提示二硫键错配，优先级极高
  │   │        └─ 执行非还原肽图XIC确认
  │   │
  │   └─ 否 → 可能是PTM累加或轻度错配
  │
  ├─ IEX是否显示3个以上离散酸性峰?
  │   ├─ 是 → 多个异质体，提示二硫键错配 or 重聚集
  │   │        └─ 需SEC确认分子量分布
  │   │
  │   └─ 否 → 可能单一修饰
  │
  └─ 最终诊断与优先级
      ├─ 优先级1：非还原肽图 XIC（24-48 h确认）
      ├─ 优先级2：肽图搜库补全PTM参数（4-8 h）
      ├─ 优先级3：复性工艺DOE（2-4周）
      └─ 优先级4：菌株或缓冲液优化（if needed）
```

---

## 表9：文献快速查询

| 需求 | 推荐文献 | 关键内容 | 可信度 |
|------|--------|--------|--------|
| 二硫键质谱基础 | Gorman 2002 | ²H₂O同位素法、pepsin酶切 | ⭐⭐⭐⭐⭐ |
| 自由巯基防护 | Yen 2000, Zhang 2002 | NEM、IAA、避免硫醇交换 | ⭐⭐⭐⭐⭐ |
| 综述与工作流 | Wiesler 2015 | DSB分析的全景方法 | ⭐⭐⭐⭐⭐ |
| **E. coli PTM全景** | **内部报告2026** | 10+种PTM、机制、工艺控制 | ⭐⭐⭐⭐⭐ |
| **Romiplostim案例** | **内部报告2026** | 酸性峰+二硫键错配的实战分析 | ⭐⭐⭐⭐⭐ |
| ADC二硫键 | PMC6284598 | 抗体-药物偶联中的错配检测 | ⭐⭐⭐⭐ |
| 非还原肽图实践 | PMC11520568 | 实用方案与常见陷阱 | ⭐⭐⭐⭐ |
| 包含体复性 | 内部多篇 | hinge区特异性、GSH/GSSG比例 | ⭐⭐⭐⭐ |

---

## 表10：工艺改进前后对标（预期值）

| KPI | 原始工艺 | 优化目标 | 实现难度 | 时间 |
|-----|---------|--------|--------|------|
| **IEX酸性峰%** | 36.7% | 12-15% | 中 | 4-8周 |
| **DSC第一峰焓值** | 低（~60-70%原研） | >95%原研 | 高 | 8-12周 |
| **hinge错配比例** | 20-30% | <5% | 高 | 8-12周 |
| **整体蛋白活性** | 可能降低 | 恢复至原研水平 | 中 | 4-8周 |
| **成本冲击** | 基线 | +0-10%（主要优化复性条件） | 低 | N/A |

---

**使用提示**：
- 本表适合快速查询和决策支持
- 具体实验设计和详细机制请参考完整综述文档
- 所有质量值精度为Da；实际测量时需考虑分析仪器精度





>[!abstract] 摘要
>本笔记系统整理了非还原 SDS-PAGE 中抗体产生额外条带（artifact bands）的多种机制，并总结了通过烷基化试剂（NEM/IAM）封闭自由巯基来抑制样品制备过程中产生假阳性杂带的实验证据。

>[!summary] 核心要点
>- 杂带来源分类：工艺相关杂质（HCP）、产品相关杂质（抗体片段）、样品制备产生的artifact。
>- Artifact形成四大机制：①未组装的轻重链片段（细胞内质量控制机制不完善）；②链内/链间二硫键形成不完全导致自由巯基暴露；③disulfide-bond scrambling（自由巯基催化二硫键重排产生更多低分子量条带）；④肽键断裂与β-消除（β-elimination产生脱氢丙氨酸，分子量降低34Da）。
>- 解决措施：使用NEM（4-10mM，pH适用范围宽）或IAM（40mM，需pH>7）对自由巯基进行烷基化封闭；需先用4-6M盐酸胍物理变性暴露域内巯基才能有效烷基化。
>- 其它影响因素：loading buffer pH越高、加热孵育时间越长，artifact越多。

# non-reducing SDS-PAGE与artifact bands

#SDS-PAGE  #artifact

### Non-reducing SDS-PAGE运用

- purity assay；

- stability indicating assay

### 额外条带（extra bands）的可能来源

- process-related impurities ：HCP
- product-related impurities : antibody fragments
- artifact: generated during sample preparation for SDS-PAGE

### 出现杂带的原因：

​	**Sensitivity** of fragmentation to **sample buffer pH**, **incubation time**, **reducing reagent** and **alkylation reagents** indicated that **fragments** were **formed during sample preparation**, but **not present** in the samples analyzed；artifact bands are generated due to unoptimized sample preparation procedure

- **unassembled antibody fragments** ; **product-related impurities**

  #折叠   #组装

  Assembly of light chain and heavy chain was a major rate limiting step of recombinant antibody production

  天然抗体产生过程中，细胞内存在cellular quality control process[^11]，这个机制控制着抗体的质量；

  <img src="D:\Knowlege_Mapping\image&attachment\image/202201302203668.png" alt="image-20220130220343522" style="zoom: 50%;" />

  > Crucially, heavy chains (HCs) are retained in the cell as dimeric intermediates until two light chains (LCs) assemble with the HC dimer to form a tetramer, which is then released from this retention and secreted from the cell .The HC dimer is retained due to a lack of folding of the CH1 domain in the absence of the cognate LC, resulting in a high-affinity interaction with the intracellular chaperone, immunoglobulin HC-binding protein (BiP) .This interaction is reversed upon LC assembly with the CL domain acting as a template to allow correct folding of the CH1 domain  .This interaction is reversed upon LC assembly with the CL domain acting as a template to allow correct folding of the CH1 domain[^10].

  但是一些非天然抗体，VH能够稳定并辅助折叠CH1，导致HC二聚体分泌。

- **incomplete formation of disulfide bonds**

  - 链内二硫键形成不完全：不会直接形成碎片；native condition下，域内自由巯基不会暴露出来；可以烷基化封闭掉；
    native condition下，蛋白表面没有自由巯基，一旦变性（SDS，加热），域内自由巯基就暴露出来（二硫键形成不完全，变性条件下1mol蛋白大概有0.1-0.2mol自由巯基），自由巯基引发disulfide bond scrambling ，导致形成碎片；

    > 0.02–0.03 mol of free sulfhydryl per mole of antibody can be detected in IgG1, IgG2 and IgG4 recombinant monoclonal antibodies under native condition, while under denaturing conditions, free sulfhydryl level was increased 3–4 times;
    >
    > the presence of unpaired cysteine residues could have provided free sulfhydryl to catalyze disulfide bond scrambling ;

  - 链间二硫键形成不完全：直接形成碎片；无法通过烷基化避免碎片形成；


- **incomplete denaturation**[^1]

  下图是手动制备的等度胶（handcast non-gradient Bis-Tris gel）  ，两种不同的buffer；lane1，2，3分别加了0，3，8M尿素；

  结果显示加8M尿素的lane3，artefact band消失；

  <img src="D:\Knowlege_Mapping\image&attachment\image/202201270734120.png" alt="image-20220127073414752" style="zoom: 50%;" />

  下图是预制梯度胶，两种不同buffer体系；相对于lane1来说，lane3似乎更细点；只跑出一个条带，但是上下图用的蛋白都是相同的，说明预制梯度胶分辨率不足；

  <img src="D:\Knowlege_Mapping\image&attachment\image/202201270739893.png" alt="image-20220127073921719" style="zoom: 50%;" />

- **disulfide bond breakage**[^6][^7]: 自由巯基数量随着时间增加


- **disulfide-bond scrambling**[^2][^8]：形成碎片机制之一；自由巯基数量不会随时间增加，but instead it caused a redistribution of incomplete **intra** chain disulfide bonds to incomplete **inter** chain disulfide bonds and thus resulted in the formation of **more** lower molecular weight bands over time.

  链内二硫键形成不完全，其存在的自由巯基会与链间二硫键反应，发生disulfide-bond scrambling，形成碎片-artifact；

  #disulfide-bond scrambling #Michael addition #NEM

  > 1. Fragmentation of monoclonal antibodies has been routinely observed in non-reducing SDS-PAGE, mainly due to disulfide-bond scrambling catalyzed by free sulfhydryl groups, resulting in a method induced artifact;
  >
  > 2. 5 mM NEM can achieve the same inhibition effect as 40 mM IAM  ;
  >
  > 3. NEM still retained strong activity after prolonged sample heating, whereas IAM lost most of its activity;
  >
  > 4. 结论：NEM appears to have a better inhibition effect than IAM on all tested IgG4 proteins, either with SDS-PAGE or CE-SDS methods
  >
  > 5. 深层次原因：两种试剂反应机制不一样：IAM，亲核取代,direct S-alkylation  ；NEM，麦氏加成,**Michael addition** of the thiolate sulfur across the C=C double bonds in NEM  [^4][^5]
  >
  >    NEM：N-乙基马来酰亚胺
  >
  >    <img src="D:\Knowlege_Mapping\image&attachment\image/202201280751201.png" alt="image-20220128075141095" style="zoom:50%;" />
  >
  >    <img src="D:\Knowlege_Mapping\image&attachment\image/202201291651483.png" alt="image-20220129164905396" style="zoom: 50%;" />
  >
  >
  >
  >    IAM:碘乙酰胺<img src="D:\Knowlege_Mapping\image&attachment\image/202201280753211.png" alt="image-20220128075317124" style="zoom:50%;" />
  >
  >    <img src="D:\Knowlege_Mapping\image&attachment\image/202201280754563.png" alt="image-20220128075459391" style="zoom: 50%;" />

  > Free sulfhydryl in the original sample triggered disulfide bond scrambling during sample denaturing and heating processes, which
  > resulted in the formation of lower molecular weight bands

  incomplete disulfide bonds二硫键形成不完全，含有低比例的自由巯基，直接形成导致碎片

  <img src="D:\Knowlege_Mapping\image&attachment\image/202201292312855.png" alt="image-20220129231228741" style="zoom: 50%;" />


  ==**解决措施**==：disulfide bond scrambling can be prevented by specifically modifying free sulfhydryl using alkylation；NEM（最佳浓度4-10mM，buffer pH较宽), IAM（最佳浓度40mM，pH需要大于7）

  下图：2xloading buffer：125 mM Tris, 4% SDS, 20% v/v glycerol, and 0.005% Bromophenol Blue，pH6.8，不含烷基化试剂，100℃ 1min（lane2），5min（lane3），10min（lane4），20min（lane5），40min（lane6），60min（lane7）；

  <img src="D:\Knowlege_Mapping\image&attachment\image/202201300759840.png" alt="image-20220130075932653" style="zoom:50%;" />

  下图：2xloading buffer含10mM NEM；对比上下图**NEM能减少artifact**；但是，加热时间延长，还是有一些artifact band，可能是其它原因导致的；

  <img src="D:\Knowlege_Mapping\image&attachment\image/202201300801269.png" alt="image-20220130080106188" style="zoom:50%;" />

  **烷基化前处理条件**：free cysteines were only accessible under denaturing conditions；所以需要对抗体进行物理变性，使用盐酸胍

  ​	实验条件：at a molar ratio of 1:100 (antibody:NEM) with **0, 2 M, 4 M and 6 M guanidine hydrochloride** in the sample preparation

  ​	结果：发现0（图A），2M（图B）盐酸胍条件下，质谱结果显示只有一个峰且与理论分子量匹配；4M（图C）,6M（图D）盐酸胍变性，质谱结果显示两个峰，两者之间相差将近250Da，为两个NEM(125Da)分子；

  <img src="D:\Knowlege_Mapping\image&attachment\image/202201300824982.png" alt="image-20220130082429908" style="zoom:50%;" />

  <img src="D:\Knowlege_Mapping\image&attachment\image/202201300824812.png" alt="image-20220130082452741" style="zoom:50%;" />

  ​	 **要避免抗体域内少量巯基，在加热条件下被暴露，导致artifact band；需要用4-6M盐酸（终浓度）物理变性抗体，使域内少量巯基暴露出来，这样NEM才能接触到自由巯基，因此才能被烷基化。**

- peptide bond cleavage  and β-elimination[^3][^9]: 形成碎片机制之二

    #β-elimination  #碎裂

> β-elimination can break disulfide bonds and form **dehydroalanine and thiocysteine**. Thiocysteine is very unstable and can rapidly decompose into free cysteine and elemental sulfur. Formation of dehydroalanine decreases the molecular weight by 34 Da

β消除主要发生在链间二硫键

质谱检测判断依据：LC上的dehydroalanine

<img src="D:\Knowlege_Mapping\image&attachment\image/202201302216983.png" alt="image-20220130221628869" style="zoom: 67%;" />

​	实验前处理：antibody was incubated at 1008C for 60 min in6 M guanidine hydrochloride, 100 mM Tris/HCl, pH 6.8

​	结果：质谱结果显示两个LC信号，两者之间相差34Da，较大的信号与LC理论分子量一致；这说明发生了实验前处理过程发生了β-elimination

<img src="D:\Knowlege_Mapping\image&attachment\image/202201300840064.png" alt="image-20220130084018976" style="zoom:50%;" />

- 其它因素

  1. loading buffer的pH（5.8，6.8，7.8，8.8）loading buffer的pH越高，artifact越多（higher sample buffer pH promoted the formation of those fragments  ；2xloading buffer**配方**:125 mM Tris, 4% SDS, 20% v/v glycerol, and 0.005% Bromophenol Blue;

  2. 加热孵育时间（100℃ 1，5，10，20，40，60min）：加热时间越长，artifact越多；

     <img src="D:\Knowlege_Mapping\image&attachment\image/202201272026414.png" alt="image-20220127202616320" style="zoom:50%;" />


### Reference

[^1]: Zhang, Yuan, Ying Wang, and Yifeng Li. "Major cause of antibody artifact bands on non-reducing SDS-PAGE and methods for minimizing artifacts." *Protein expression and purification* 164 (2019): 105459.
[^2]: Zhu, Zhiqing C., Yingchen Chen, Michael S. Ackerman, Bei Wang, Wei Wu, Bo Li, Linda Obenauer-Kutner et al. "Investigation of monoclonal antibody fragmentation artifacts in non-reducing SDS-PAGE." *Journal of pharmaceutical and biomedical analysis* 83 (2013): 89-95.
[^3]: Cohen, Steven L., Colleen Price, and Josef Vlasak. "β-Elimination and peptide bond hydrolysis: two distinct mechanisms of human IgG1 hinge fragmentation upon storage." *Journal of the American Chemical Society* 129, no. 22 (2007): 6976-6977.

[^4]: Giron P, Dayon L, Sanchez JC (2011) Cysteine tagging for MS-based proteomics. Mass Spectrom Rev 30(3):366–395
[^5]: Nair, Devatha P., Maciej Podgorski, Shunsuke Chatani, Tao Gong, Weixian Xi, Christopher R. Fenoli, and Christopher N. Bowman. "The thiol-Michael addition click reaction: a powerful and widely used tool in materials chemistry." *Chemistry of Materials* 26, no. 1 (2014): 724-744.
[^6]: Liu H, Gaza-Bulseco G, Sun J (2006) Characterization of the stability of a fully human monoclonal IgG after prolonged incubation at elevated temperature. J Chromatogr B Analyt Technol Biomed Life Sci 837:35–43. Epub 2006 Apr 27
[^7]: Cordoba AJ, Shyong BJ, Breen D, Harris RJ (2005) Nonenzymatic hinge region fragmentation of antibodies in solution. J Chromatogr B Analyt Technol Biomed Life Sci 818:115–121

[^8]: Taylor FR, Prentice HL, Garber EA, Fajardo HA, Vasilyeva E, Blake Pepinsky R (2006) Suppression of sodium dodecyl sulfate-polyacrylamide gel electrophoresis sample preparation artifacts for analysis of IgG4 half-antibody. Anal Biochem 353:204–208. Epub 2006 Mar 9
[^9]: Tous GI, Wei Z, Feng J, Bilbulian S, Bowen S, Smith J, Strouse R, McGeehan P, Casas-Finet J, Schenerman MA (2005) Characterization of a novel modification to monoclonal antibodies: thioether cross-link of heavy and light chains. Anal Chem 77:2675–2682
[^10]: Stoyle, Chloe L., Paul E. Stephens, David P. Humphreys, Sam Heywood, Katharine Cain, and Neil J. Bulleid. "IgG light chain-independent secretion of heavy chain dimers: consequence for therapeutic antibody production and design." *Biochemical Journal* 474, no. 18 (2017): 3179-3188.
[^11]: Feige, Matthias J., Linda M. Hendershot, and Johannes Buchner. "How antibodies fold." *Trends in biochemical sciences* 35, no. 4 (2010): 189-198.





>[!abstract] 摘要
>综述二硫键在内质网中的形成机制：由蛋白二硫键异构酶(PDI)催化，其化学环境由谷胱甘肽(GSH/GSSG)的氧化还原平衡维持。

>[!summary] 核心要点
>- 二硫键在ER中形成，由protein disulfide isomerase (PDI)催化
>- 化学环境依赖mM级别浓度的谷胱甘肽(氧化型GSSG/还原型GSH)维持redox balance
>- ER中缺乏Glutathione reductase，GSH/GSSG比例较低；胞质中该酶维持高GSH/GSSG比例

> 综述文献：Mechanisms of Disulfide Bond Formation in Nascent  Polypeptides Entering the Secretory Pathway

**形成位置**：ER，含protein  disulfide isomerase (PDI)；

**二硫键形成的化学环境**：redox balance靠mM级别浓度的==glutathione-谷胱甘肽==，有两种形式：氧化型-GSSG，还原型-GSH；在ER中，不存在Glutathione reductase，所以GSH/GSSG比例较低；而在胞质中，Glutathione reductase维持着高比例的GSH/GSSG;



### 1.试剂

>[!abstract] 摘要
>本笔记是二硫键配对分析（NR&R，非还原/还原对照）样品前处理的实验室SOP，记录所需试剂耗材清单及从蛋白浓缩、NEM封闭游离巯基、盐酸胍变性、trypsin酶切到还原处理的完整操作步骤。

>[!summary] 核心要点
>- 用NEM（N-乙基顺丁烯二酰亚胺）封闭游离巯基，防止酶切过程中发生二硫键错配（disulfide scrambling）。
>- 用7M盐酸胍变性蛋白（37℃ 2h），随后置换buffer并用trypsin 37℃过夜酶切。
>- 酶切液分两份：一份直接加甲酸终止用于NR（非还原）分析二硫键配对；另一份加DTT还原1h后用于R（还原）对照分析。


| NO  | 名称                        | 货号         | 厂家            | 相对分子量 |
| --- | --------------------------- | ------------ | --------------- | ---------- |
| 1   | Na2HPO4                     | S112446      | 阿拉丁          | 141.96     |
| 2   | KH2PO4                      | P104075-500g | 阿拉丁          | 136.09     |
| 3   | N-乙基顺丁烯二酰亚胺（NEM） | E100553-5g   | 阿拉丁          | 125.13     |
| 4   | DL-二硫苏糖醇（DTT）        | D104861-5g   | 阿拉丁          | 154.25     |
| 5   | LC-MS Acetonitrile          | A955-4       | Fisher chemical | NA         |
| 6   | LC-MS water                 | W6-4         | Fisher chemical | NA         |
| 7   | L-MS Formic acid            | A117-50      | Fisher chemical | NA         |
| 8   | Sequencing grade trypsin    | V5111        | Promega         | NA         |
| 9   | 盐酸胍                      | G108674-500g | 阿拉丁          | 95.53      |
| 10    |   碳酸氢钠   |   S112331-500g           |  阿拉丁       |   84.01  |


### 2.耗材
| NO  | 名称                                                                      | 货号         | 规格         | 厂家      |
| --- | ------------------------------------------------------------------------- | ------------ | ------------ | --------- |
| 1   | Nalgene Reusable Bottle Top Filters                                       | DS0320-5045  | 45mm,500ml   | Thermo    |
| 2   | Amicon Ultra-0.5ml                                                        | UFC501024    | 10K          | Millipore |
| 3   | 250ul clear glass insert with polymer feet                                | HM1270       | 250ul        | HAMAG     |
| 4   | Blue open-topped polypropylene cap and pre-slit while PTFE silicone septa | HM-2076      | 90MM         | HAMG      |
| 5   | 2ml clear screw Top sample Vial with patch                                | HM-0713      | 2ml          | HAMG      |
| 6   | 微孔滤膜-水系MCE(混合纤维素）0.22um                                       | F513133-0001 | 50mm，0.22um | 生工      |
| 7    | ACQUITY UPLC Peptide BEH C18 column 130A 1.7um|  186003555            |  2.1mmx100mm            |    Waters       |

### 3. 配制溶液
1. 50mM磷酸盐缓冲液（pH7.0)：称取0.5393g Na2HPO4，0.8438g KH2PO4，溶于200ml纯水，混匀（实测pH6.7）；用1M氢氧化钠调pH值至7.0；
2. 200mM NEM溶液：称取12.5mg NEM，溶于500ul 50mM磷酸盐缓冲液（pH7.0)，混匀；
3. 7M盐酸胍：称取13.37g 盐酸胍，加适量50mM磷酸盐缓冲液（pH7.0)，定容至20ml，混匀，实测pH4.6；用1M氢氧化钠调pH值至7.0；
4. 0.2ug/ul trypsin溶液：取100ul 50mM磷酸盐缓冲液（pH7.0)至20ug胰蛋白粉末中，混匀；
5. 500mM 碳酸氢钠溶液：称取840mg碳酸氢钠，加20ml纯水，溶解，混匀；
6. 1M DTT溶液：称取154mg DTT，加1ml ddH2O，混匀；

### 4. 实验过程
1. 蛋白溶液浓缩和置换buffer：取200ug蛋白置于Amicon滤膜中（使用前用纯水离心，润洗），将buffer置换为50mM磷酸盐缓冲液（pH7.0)，终体积为50ul，蛋白浓度为4mg/ml；测定浓度，计算回收率；
2. 加NEM溶液：加入2ul 200mM NEM溶液，混合；
3. 加盐酸胍溶液进行蛋白变性：加150ul 7M盐酸胍（in 50mM磷酸盐缓冲液 pH7.0），混匀；NEM终浓度为1.98mM，盐酸胍终浓度为5.2M；37℃变性2h；
4. 置换buffer：将变性蛋白溶液置换到50mM磷酸盐缓冲液（pH7.0)中，置换两次；终体积为160ul；
5. 酶切：加入40ul 0.2ug/ul trypsin溶液，混匀；37℃过夜酶切；
6. 酶切结束，将溶液分两份，一份直接用于NR，加0.5ul FA，直接分析二硫键配对；另一份用于R；
7. 用于R的溶液，加20ul 500mM 碳酸氢钠溶液，加5ul 1M DTT，混匀，反应1h；反应后加0.5ul甲酸，混匀；


