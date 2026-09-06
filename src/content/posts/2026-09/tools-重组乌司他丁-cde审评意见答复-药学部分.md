---
title: 重组乌司他丁 IND 审评意见答复（药学部分）
date: '2026-09-06'
category: 工具与效率
tags:
- 工具与效率/乌司他丁
description: abstract 本文是什么 针对 CDE 对重组乌司他丁（拟替代人尿提取乌司他丁，适应症：急性胰腺炎）IND 申请提出的 10 条药学审评意见，逐条给出：意见的技术实质
  → 科学与文献依据 → 建议的研究方案 → 答复口径 → 是否纳入质
---

> [!abstract] 本文是什么
> 针对 CDE 对**重组乌司他丁**（拟替代人尿提取乌司他丁，适应症：急性胰腺炎）IND 申请提出的 **10 条药学审评意见**，逐条给出：意见的技术实质 → 科学与文献依据 → 建议的研究方案 → 答复口径 → 是否纳入质量标准。
> 全文结论均有可溯源文献支撑，引用规则见文末[[#引用可靠性声明]]。

> [!warning] 使用前必读
> 本文提供的是**科学论证与答复框架**，不是可直接提交的答复正文。文中以 `〔待填：…〕` 标注的位置必须由申报方以自有工艺与检测数据填充；未经数据填充的答复不具备提交条件。
> 文中涉及的临床用药与疗效表述仅用于说明质量属性与临床终点的关联，不构成诊疗建议。

> [!Reference] 相关笔记
> - [[对话记录|急性胰腺炎发病机制与主流治疗]]
> - 乌司他丁技术文档（`乌司他丁/乌司他丁技术文档.html`、`乌司他丁/乌司他丁.docx`）
> - 参考文献 PubMed 核对清单（`乌司他丁/参考文献-PubMed核对清单.txt`）

---

## 一、审评意见清单与答复索引

| # | 分类 | 审评意见（摘要） | 答复章节 | 拟纳入标准 |
|---|---|---|---|---|
| 质-1 | 质量研究与控制 | 持续积累多批次糖基化类型及比例，关注糖型分布对安全性和有效性的影响 | [[#质-1 糖型分布的持续监测与影响评估]] | 部分（见正文） |
| 质-2 | 质量研究与控制 | C 端缺失氨基酸变异体批间差异明显，分析原因并评估影响 | [[#质-2 C 端缺失变异体的批间差异与影响评估]] | 待定 |
| 质-3 | 质量研究与控制 | 开展电荷异质性研究，必要时纳入质量标准 | [[#质-3 电荷异质性研究]] | 建议纳入 |
| 质-4 | 质量研究与控制 | 工艺相关杂质检测与安全性评估，如 MSX 残留 | [[#质-4 工艺相关杂质：MSX 残留的检测与安全性评估]] | 建议纳入 |
| 质-5 | 质量研究与控制 | 完善纯度（SDS-PAGE）方法，明确 Marker 分子量分布，关注蛋白条带较宽的原因 | [[#质-5 SDS-PAGE 纯度方法、Marker 与条带弥散]] | 方法学修订 |
| 质-6 | 质量研究与控制 | 积累多批次原液及制剂数据与稳定性数据，合理收紧标准限度 | [[#质-6 多批次数据积累与标准限度收紧]] | 限度修订计划 |
| 稳-1 | 内包材和稳定性 | 规范长期稳定性考察；年度点全检，关注效价、纯度、糖基化修饰趋势 | [[#稳-1 长期稳定性考察与年度点全检]] | 考察项目修订 |
| 稳-2 | 内包材和稳定性 | 使用中稳定性补充不溶性微粒、无菌、细菌内毒素等检项 | [[#稳-2 使用中稳定性：微粒、无菌与细菌内毒素]] | 使用期限依据 |
| 稳-3 | 内包材和稳定性 | 临床样品保存、运输、使用确保在经确认条件范围内 | [[#稳-3 临床试验用样品的储运与使用控制]] | SOP/方案 |
| 稳-4 | 内包材和稳定性 | 药包材相容性研究与安全性风险评估，关注储液袋、滤膜 | [[#稳-4 药包材相容性与安全性风险评估]] | 风险评估报告 |

---

## 二、立论基础：本品与常规重组蛋白的三点根本差异

这 10 条意见看似分散，实际全部指向同一个技术事实：**乌司他丁不是一个普通的重组蛋白，而是一个小分子蛋白聚糖（proteoglycan）**。答复如果不先把这一点讲透，后面每一条都会变成孤立的"补数据"承诺。

### 2.1 一半的分子量不是蛋白

天然尿源乌司他丁（urinary trypsin inhibitor, UTI / bikunin）的核心蛋白为 143 个氨基酸、计算分子量 15 340 Da，含两个 Kunitz 结构域；其 N 端 21 残基延伸段以 **O-糖苷键**、"非活性"结构域以 **N-糖苷键**分别连接大分子糖基，因此 SDS-PAGE 表观分子量达约 30 000 Da[^1]；两类糖基的连接方式与位置由同一系列研究的后续工作确定[^2]。O 位修饰的化学身份是一条**硫酸软骨素（chondroitin sulfate, CS）糖胺聚糖链**，共价连接于核心蛋白的 **Ser10**[^3][^4]；完整 CS 链自身的分子量即为 5 505–7 102 Da[^7]。N 位修饰位于 **Asn45**，为双天线复合型 N-糖，呈双唾液酸型／单唾液酸型／去唾液酸型的混合[^12]。

> [!important] 对审评意见的直接含义
> "分子量""纯度""电荷"这三个常规质量属性，在本品上**都不是单一数值，而是分布**。质-3（电荷）与质-5（条带弥散）本质上是同一个物理事实在两种分析方法上的投影。

### 2.2 糖链不是"修饰"，而是功能单元 —— 但只对部分功能如此

必须把"糖基化影响有效性"这句话拆开，否则答复会失焦：

- **蛋白酶抑制活性主要由核心蛋白决定。** 抗胰蛋白酶活性由 **C 端 Kunitz 结构域（KD-II）** 承担[^1]；标准机制抑制剂的 P1 残基插入酶的 S1 特异性口袋，是决定特异性与结合强度的关键位点[^15]。重组表达的 KD-II 单独即可抑制胰蛋白酶、纤溶酶、白细胞弹性蛋白酶与胰凝乳蛋白酶，并竞争性抑制 FXa 与血浆激肽释放酶、显著延长 APTT[^14]。杆状病毒表达的**无 GAG 链、无 N-糖的重组 bikunin，其胰蛋白酶抑制活性与含糖前体相同**[^28]。
- **N-糖所在位置决定了它对抑制活性的影响有限。** N-连接糖链所在的天冬酰胺位于**"非活性"的 Kunitz 结构域内**（原始文献按 122 残基编号记为 Asn24，对应 143 残基成熟链的 Asn45）[^2]，而该结构域即 KD-I（Lys22–Arg77）[^19]。晶体结构进一步显示，KD-I 的反应位点环无遮挡，而 **KD-II 的环靠近 KD-I，其蛋白酶结合可能受 KD-I 影响甚至被阻断**，因而两结构域之间的切割会改变 KD-II 的底物特异性[^13] —— 这一点对[[#质-2 C 端缺失变异体的批间差异与影响评估]]同样关键。
- **但 CS 链在低浓度区定量增强这一活性。** 用糖链重塑技术制备核心蛋白完全相同、仅糖链不同的三种乌司他丁，天然 UTI 对胰蛋白酶／胰凝乳蛋白酶／纤溶酶的 IC₅₀（0.406／0.556／1.36 µg/mL）低于 linkage-UTI（1.458／1.586／2.72 µg/mL）与 HA-UTI（1.543／1.537／3.88 µg/mL）[^17]。linkage-UTI 与 HA-UTI 数值接近，提示增强效应来自**硫酸化/电荷**而非"有一条等长糖链占位"。

- **非蛋白酶抑制的活性则依赖 O-连接 CS 链，而不依赖 N-糖。** 去 O-糖的 UTIc 在细胞结合竞争实验中 IC₅₀ 较天然 UTI 高 **29 倍**，而去 N-糖的 UTIn 与天然 UTI 无法区分[^19]；溶酶体膜稳定活性同样依赖 O-糖链，去 N-糖不影响[^20]；抑制 LPS 诱导的胞内游离钙升高亦依赖 CS 链[^21]；与细胞的高亲和力结合位点需要 CS 链[^22]。

> [!example] 一处表面矛盾，以及它为什么恰恰是关键证据
> 同一研究组更早的论文报告 **HA-UTI 的胰蛋白酶抑制活性与天然型"相似"**[^18]，与上述纤溶酶 2.9 倍 IC₅₀ 差异看似冲突。后续论文给出了调和：在 10 µg/mL（按蛋白浓度）时，UTI／linkage-UTI／HA-UTI 对胰蛋白酶的最大抑制率分别为 **86%／84%／84%**，对胰凝乳蛋白酶为 90%／88%／89% —— **几乎无法区分**；作者明确指出糖链结构差异导致的抑制程度差异**在较高浓度下被消除**，增强效应只在较低浓度下明显[^17]。
> → 两篇论文并不矛盾，只是**测定浓度不同**。这正是下面那条方法学结论的实证基础。

> [!important] 对审评意见的直接含义
> **效价方法的选择决定了质-1 与质-6 能否成立。** 若效价仅以胰蛋白酶抑制的**终点法/饱和浓度**测定，则 O-糖链的变化会被系统性漏检 —— 糖型对 IC₅₀ 的影响约 2.0–3.8 倍，而在 10 µg/mL 饱和浓度下三种糖型的最大抑制率差异仅 86% vs 84%，已落在噪声范围内[^17]。**建议将效价方法改为可分辨 2 倍差异的动力学/剂量-反应方法，并在答复中主动说明这一点。** 这是回应"糖型分布对有效性的影响"最有说服力的方式。

### 2.3 CS 链使本品与 OSCS 污染肝素事件处于同一化学家族

这是本品**最需要主动设限、也最容易被追问**的安全性属性。

2007–2008 年，过硫酸化硫酸软骨素（oversulfated chondroitin sulfate, OSCS）作为肝素污染物导致严重类过敏反应。机制已明确：OSCS 直接激活人血浆中的**激肽-激肽释放酶通路**生成缓激肽，并诱导补体 C3a、C5a 生成[^52]；其抗凝活性主要经**肝素辅因子 II** 介导，且与 FXIIa 紧密结合，为 FXIIa 依赖的缓激肽生成提供了生化机制[^53][^54]；在麻醉大鼠中，静脉给予 OSCS 或 OSCS 污染肝素可致剂量与给药途径依赖的舒张压下降，该效应可被缓激肽 B2 受体拮抗剂完全阻断，而皮下给药无此效应[^56]。

更关键的一项证据是**剂量-构效关系**：以合成方法制备不同硫酸化程度的硫酸软骨素并逐一比较，未修饰的硫酸软骨素抗凝活性极低，而**随硫酸化程度升高，经肝素辅因子 II 介导的抗凝活性与前激肽释放酶激活能力同步上升**，激肽系统的激活（以缓激肽计）经激肽释放酶生成实现[^55]。

> [!danger] 对审评意见的直接含义
> 本品的 CS 链硫酸化度**不是一个中性的糖型参数，而是一个具有明确毒理学通路的安全性属性**。质-1（糖型分布对安全性的影响）与质-3（电荷异质体对安全性的影响）应当**合并论证**：二者测的是同一件事 —— GAG 的负电荷密度分布。建议在答复中主动提出以"过硫酸化/高电荷组分上限"作为安全性相关的质量属性，并配套**功能学**评估（APTT、前激肽释放酶激活/缓激肽生成），而不是仅做糖谱的化学表征。

### 2.4 天然来源的"批间差异"参照系不适用于重组品

天然 bikunin 的 CS 链长度与硫酸化度**本身随供体的炎症状态系统性改变**：健康人平均 14 ± 3 个二糖单元、其中 5 ± 1.5 个为 4-O-硫酸化；脓毒性休克患者为 20 ± 5 个二糖单元、仅 3 ± 2.5 个 4-O-硫酸化，非硫酸化区段由 9 个二糖延长至 17 个[^10]；且糖链尺寸随炎症严重程度增大[^11]。同一提取制剂内部即为电荷异构体的混合物，可经阴离子交换 HPLC 分离为多个组分[^9]。

> [!important] 对审评意见的直接含义
> 重组品**不应以"与提取品一致"作为糖型判据** —— 提取品自身就没有一致的糖型。正确的做法是：以重组工艺自身的多批次数据建立糖型分布的历史区间，并以毒理学/功能学数据为高硫酸化端设上限。这一论证同时服务于质-1、质-3 与质-6。

---

## 三、质量研究与控制（（三）项）

### 质-1 糖型分布的持续监测与影响评估

> [!quote] 审评意见原文
> 临床期间请继续完善本品质量研究，例如，本品含有 1 个 N-糖基化位点和 2 个 O-糖基化位点，N-糖和 O-糖修饰类型较为复杂，建议临床期间持续积累多批次糖基化类型及比例的检测结果，关注糖型分布对产品安全性和有效性的影响。

#### 1）先厘清"2 个 O-糖基化位点"的身份

答复的第一步不是承诺积累数据，而是**明确两个 O 位点各自的化学身份**，因为它们的检测方法、变异来源与风险等级完全不同：

- **Ser10 — GAG（硫酸软骨素）起始位点。** 身份明确、证据充分：CS 链经 O-糖苷键连接于 Ser10[^3]；该 CS 链还参与 bikunin 与重链之间的"蛋白-糖胺聚糖-蛋白"共价交联[^4][^5][^6]。此位点的糖链是一条**长度与硫酸化度均呈分布**的聚糖[^7][^8][^9]。
- **第二个 O 位点** — **公开文献无对应描述。** 经典结构研究明确指出乌司他丁的糖链"连接于两个位置"：一条经 O-糖苷键连于 N 端延伸段的 Ser10，另一条经 N-糖苷键连于非活性 Kunitz 结构域的天冬酰胺，全分子糖含量约 50%[^2]。即公开文献描述的是 **1 个 O 位 + 1 个 N 位，共两处**。〔待填：请明确第二个 O 位点为黏蛋白型 O-GalNAc 修饰还是其他类型，并给出位点鉴定数据（O-糖肽 LC-MS/MS）〕。若为黏蛋白型 O-糖，则与 Ser10 的 GAG 属两类不同修饰，**必须分开表述、分开设定控制策略**；将二者笼统称为"O-糖"会在后续审评中被继续追问。

> [!tip] 答复口径建议
> 用一张表把三个位点讲清：位点 → 修饰类型 → 位点占有率 → 结构异质性维度 → 检测方法 → 已知功能影响 → 控制策略。这比任何叙述都更有效。

#### 2）重组表达能否装配 CS 链，是本品的前置科学问题

这一点直接决定糖型策略：

- Ser10 所在的 Glu-Gly-Ser-Gly 微环境是 GAG 起始的保守序列，**bikunin 是木糖基转移酶（XT）的极高效受体**：以重组人 bikunin 为受体测定血清 XT 活性时，其 K<sub>M</sub> 为 0.9 µmol/L，而丝素与去糖基化软骨蛋白聚糖分别为 545 与 155 µmol/L[^103]；游离 bikunin 与 α1-微球蛋白/bikunin 前体均可作为体外木糖基化的底物[^28]。人 XT-II 对修饰型 bikunin 肽的 K<sub>M</sub> 为 1.9 µM，为其最优受体[^29]；XT-I 与 XT-II 的受体特异性存在差异[^30]。
- 但**表达系统决定结果**：杆状病毒感染昆虫细胞表达的重组 bikunin **既无半乳糖胺聚糖链、也无 N-连接寡糖**[^28]；毕赤酵母表达的重组人 bikunin 呈 24 kDa 与 21 kDa 两种形式，具胰蛋白酶抑制活性[^31][^32]。此外，转化的肝细胞系（如 HepG2）已丧失正确合成 bikunin 蛋白的能力，而原代人肝细胞可产生与血浆一致的产物，提示 GAG 交联发生在分泌途径晚期且依赖完整的生物合成机器[^6]。

> [!tip] 答复口径建议
> 〔待填：明确本品表达系统（宿主细胞、是否 GS/MSX 系统）及 Ser10 GAG 的实际装配情况〕。
> - **若本品带 CS 链**：糖型控制的重点是 GAG 的链长与硫酸化度分布（安全性关切，见 2.3），以及 N-糖的非人源表位。
> - **若本品不带 CS 链（无 GAG 型）**：这是与提取品的**实质性结构差异**，应主动申明，并以功能学数据说明其对非蛋白酶抑制活性的影响（去 O-糖使细胞结合 IC₅₀ 升高 29 倍[^19]、丧失溶酶体膜稳定作用[^20]），同时说明急性胰腺炎适应症下的有效性主张主要建立在何种机制上。**回避这一差异是风险最高的选择。**

#### 3）建议的糖型监测方案（三层）

| 层级 | 监测对象 | 建议方法 | 关联风险 |
|---|---|---|---|
| L1 位点占有率 | Asn45、Ser10、第二 O 位点的糖基化占有率 | 糖肽 LC-MS/MS（PNGase F / 酶解对照） | 工艺一致性 |
| L2 N-糖谱 | 中性/单唾液酸/双唾液酸型比例、非人源表位（Neu5Gc、α-Gal）、核心岩藻糖 | 释放糖 HILIC-FLR + MS | 免疫原性、清除 |
| L3 O-连接 GAG | 二糖组成（Δdi-0S/4S/6S 比例）、链长分布、**过硫酸化组分** | 软骨素酶 ABC/AC 酶解 + 二糖 HPLC/LC-MS；完整糖链 ESI-FTMS[^8]；阴离子交换 HPLC 分级[^9] | **安全性（接触系统激活）**、效价 |

制剂间可比性评价可参照已有的多方法组合实践：以 SDS-PAGE、醋酸纤维素膜电泳、HP-SEC、CE 与 MALDI-TOF MS 比较不同批次与不同厂家的乌司他丁制剂，其中糖链（硫酸软骨素二糖组成与 N-连接寡糖）可作为制剂可比性评价的标志物[^23]。

#### 4）糖型对安全性与有效性的影响：论证要点

**安全性**
- GAG 硫酸化度 ↑ → 肝素辅因子 II 介导的抗凝活性 ↑、前激肽释放酶激活 ↑ → 缓激肽生成 ↑[^55]；这正是 OSCS 污染肝素致类过敏反应的通路[^52][^53][^54][^56]。→ **建议将"过硫酸化组分"设为安全性相关质量属性并设上限。**
- N-糖的非人源唾液酸 Neu5Gc：人体普遍存在预存抗 Neu5Gc 抗体，其临床影响在已上市生物制品中尚无确证的严重不良事件归因，但仍属需评估与最小化的风险，且应规范分析与报告[^59][^60][^61]。
- 糖基化是影响治疗性蛋白免疫原性的既定结构因素之一[^58]；糖基化对产物的稳定性、半衰期与免疫原性的整体影响见综述[^57]。

**有效性/药代**
- 唾液酸化程度决定清除途径与器官分布：唾液酸化程度不同的 TSH 制剂在大鼠中的清除器官显著不同，去唾液酸型主要经肝清除[^63]；去唾液酸糖蛋白受体（ASGP-R）可介导极快的清除（半衰期 < 1 min）[^62]。
- 治疗性蛋白的 PK 评价本身受结合蛋白、代谢物与抗体形成干扰，方法学选择会影响参数估计[^64]。
- 本品的天然对照物 UTI 在人体内血浆半衰期为 0–3 h 段 33 min、其后 2 h，主要经肾脏代谢（大鼠注射后 15 min 44% 放射性在肾、9% 在肝）[^27]。→ 说明**肾清除主导**，这为糖型-清除关系的评估提供了本品特异的背景。

#### 5）答复承诺（建议表述）

1. 明确三个糖基化位点的化学身份与位点占有率，随首批答复提交位点鉴定数据；
2. 建立 L1–L3 三层糖型分析方法并完成方法学验证，随临床期间**每批**检测，累积 ≥〔待填〕批建立历史区间；
3. 完成"糖型-活性"相关性研究：以阴离子交换 HPLC 按电荷（硫酸化度）分级后分别测定抑制动力学与接触系统激活，建立量效关系；
4. 效价方法升级为可分辨 2 倍差异的剂量-反应方法；
5. **纳入标准**：过硫酸化/高电荷组分上限（安全性）；N-糖主要糖型比例作为一致性指标暂以内控标准控制，III 期前评估是否转入放行标准。

---

### 质-2 C 端缺失变异体的批间差异与影响评估

> [!quote] 审评意见原文
> C 端缺失氨基酸变异体在不同批次间存在明显差异，请分析差异原因并评估对产品安全性和有效性的影响。

#### 1）先定位切点 —— 这决定问题的严重程度

本品的 C 端位于 **KD-II 内部**，而 KD-II 是抗胰蛋白酶活性的主要承担者：P1 位 Arg 紧邻 Cys91[^1]，KD-II 单独即可抑制多种丝氨酸蛋白酶并延长 APTT[^14]。

> [!danger] 分级判断
> - 若缺失仅涉及结构域外的末端 1–2 个残基 → 对功能影响可能有限，属可控质量属性；
> - 若缺失侵入 KD-II 的二硫键框架或反应位点环 → **直接损失主要药效**，属关键质量属性，必须严格控制。
>
> 因此答复的第一步是**用完整分子量 LC-MS + C 端肽段肽图精确定位切点与缺失残基数**，而不是先解释批间差异。〔待填：切点鉴定结果、各批次变异体比例〕

#### 2）差异原因的排查顺序（三条假设，按可控性排序）

**假设 A：宿主羧肽酶加工（最可能，且可控）**

抗体产品的同类问题已有明确结论，可直接借鉴其排查逻辑：

- CHO 细胞中抗体 C 端赖氨酸的切除**完全由羧肽酶 D（CpD）承担** —— CpD 表达量最高，RNAi 下调使 C 端 Lys 残留升高，CRISPR 敲除后 C 端 Lys 切除完全消失[^42]；
- 切除程度受**培养基痕量元素**调控：铜浓度升高、锌浓度降低均使 C 端 Lys 残留水平升高[^43]；酵母水解物中的铜含量变化即可改变 C 端 Lys 水平[^46]；
- 也受**培养基氨基酸浓度**调控：Arg 与 Lys 由 2 mM 升至 10 mM 时，变异体水平由 18.7% 升至 31.8%，机制为对碱性羧肽酶的**产物抑制**[^44]；
- 温度与培养时长亦有影响[^43]。

→ 这三类参数（痕量元素、Arg/Lys 浓度、培养时长/温度）正是**可解释"批间明显差异"的最常见根因，且全部可控**。建议按此顺序做回顾性关联分析。

**假设 B：产品自身的蛋白酶敏感性**

- **bikunin 的 Kunitz 结构域已被直接证实是 mesotrypsin 的特异性底物**（与 APLP2、HAI2 一同以特异性底物的动力学特征被切割）[^25]；对 **bikunin 的 Kunitz 结构域 II** 做二硫键工程可将其对 mesotrypsin 的蛋白水解抗性提高 6.6 倍[^26] —— 后者说明 **KD-II 正是易被蛋白水解的部位**，与 C 端缺失变异体的位置吻合；
- IαI 家族本身存在"被其所抑制的酶水解"的双通路机制：蛋白酶可与两个独立位点之一结合，分别形成抑制性复合物或导向水解的复合物，两条通路同时进行[^16]。

→ 提示需评估**收获液与纯化过程中的蛋白酶暴露时间窗**（收获时机、温度、pH、是否加抑制剂）。

**假设 C：表达构建体设计**

若曾考虑以删除 C 端残基的方式降低异质性，需注意其代价：表达 C 端缺失 Lys（-K）抗体的克隆比生产率显著低于野生型或缺失 Gly-Lys（-GK）的克隆，原因指向重链合成变慢与降解加快[^45]。→ **"用序列改造消除异质性"可能以产量与稳定性为代价，需权衡后再决策。**

#### 3）影响评估方案

1. **制备/富集变异体**：弱阳离子交换分级；必要时以羧肽酶 B 处理制备对照品（该策略在抗体 C 端变异体研究中为标准做法[^43][^48]）；
2. **有效性评估**：对各组分分别测定胰蛋白酶/糜蛋白酶/纤溶酶抑制的 K<sub>i</sub> 或 IC₅₀（剂量-反应法，非终点法）、APTT；
3. **安全性评估**：新生 C 端为潜在新表位，纳入免疫原性风险评估；同时评估对 FXa/血浆激肽释放酶抑制谱的改变[^14]；
4. **CQA 判定**：C 端异质性是重组蛋白的常见修饰之一[^47]，但其**是否为本品的 CQA 必须以本品自身数据回答**，不得援引抗体产品的通用结论。

#### 4）答复承诺（建议表述）

1. 提交 C 端切点鉴定数据与各批次变异体定量结果；
2. 提交根因分析：培养基痕量元素、Arg/Lys 浓度、收获时机与温度的回顾性关联分析 + 确证性小试；
3. 提交富集组分的功能学对比数据；
4. **纳入标准**：待影响评估完成后判定。若证实为 CQA，则以放行标准控制上限；若证实非 CQA，则以内控标准控制批间一致性，并在答复中给出判定依据。

---

### 质-3 电荷异质性研究

> [!quote] 审评意见原文
> 建议临床期间开展电荷异质性研究，关注不同电荷异质体组分组成及对产品安全性和有效性的影响，必要时纳入质量标准。

#### 1）本品电荷异质性有两个来源，必须分开处理

| 来源 | 化学本质 | 与抗体类产品相比 | 风险性质 |
|---|---|---|---|
| **蛋白层面** | C 端加工、脱酰胺、氧化、N 端修饰 | 相同 | 一致性 |
| **GAG 层面** | CS 链的硫酸化度与链长分布 | **本品特有** | **安全性 + 有效性** |

**蛋白层面**的规律可借鉴抗体经验：对一株鼠源 IgG1 的系统解析表明，去除 C 端赖氨酸后 IEF 图谱由复杂简化为 9 个主要异构体，定量异天冬氨酸提示**脱酰胺是电荷异质性的主要来源**，重链与轻链各有一个脱酰胺位点；表面等离子共振显示各异构体间结合参数无显著差异[^48]。电荷变体亦与糖型分布相关联：N 端焦谷氨酸形成与 C 端 Lys 切除解释了大部分电荷异质性，且碱性变体中 G1F 降低、Man5 与 G0F-GN 升高[^51]。

**GAG 层面**是本品独有的：天然 UTI 制剂内部即为电荷异构体混合物，各异构体在硫酸化度与链长两个维度上均存在差异，可经阴离子交换 HPLC 分离为多个组分[^9]。

> [!warning] 一个不能外推的结论
> 对某重组人源化 IgG1，分离得到的酸性、碱性与主峰组分在效价、FcRn 结合与大鼠 PK 上均无差异[^49]。
> **这一"电荷变体无影响"的结论不能外推至本品** —— 抗体的酸性变体来自脱酰胺，而本品的酸性变体可能直接对应**高硫酸化 GAG**，后者具有明确的接触系统激活通路[^55]。援引该结论会削弱答复的可信度。

#### 2）建议方案

1. **双正交分离**：icIEF/cIEF（反映整体表观 pI）+ 强阴离子交换 HPLC（专门分辨 GAG 硫酸化度）[^9]；
2. **分级后表征**：各组分做完整分子量 LC-MS、肽图、GAG 二糖组成；分级组分的结构-功能表征已是生物类似药领域的成熟做法[^50]；
3. **功能学评估（关键）**：各组分分别测定
   - 有效性：蛋白酶抑制 IC₅₀/K<sub>i</sub>（剂量-反应法）；
   - **安全性：APTT、肝素辅因子 II 依赖的抗凝活性、前激肽释放酶激活/缓激肽生成**[^52][^53][^55]；
4. **建立量效关系**：以硫酸化度为自变量，作抗凝活性与激肽系统激活的剂量-反应曲线，据此为高电荷端设定限度。

#### 3）答复承诺（建议表述）

1. 建立并验证 icIEF + AEX-HPLC 双方法，临床期间逐批检测，建立电荷异构体分布的历史区间；
2. 完成分级组分的结构与功能表征，重点评估酸性/高电荷端的接触系统激活风险；
3. **纳入标准（建议主动提出）**：以"高电荷（过硫酸化）组分上限"作为安全性相关放行项；主峰含量与酸/碱性组分比例先以内控标准控制，III 期前评估转入放行标准。

---

### 质-4 工艺相关杂质：MSX 残留的检测与安全性评估

> [!quote] 审评意见原文
> 建议对工艺相关杂质进行检测和安全性评估，如 MSX（L-蛋氨酸亚砜亚胺）残留等，必要时纳入质量标准。

#### 1）来源说明

MSX 是谷氨酰胺合成酶（GS）表达系统的筛选剂：GS-CHO 系统通过 MSX 抑制宿主内源性 GS，制造谷氨酰胺营养缺陷，由表达载体编码的 GS 互补，从而筛选高表达克隆[^33][^36]。相关事实：

- 宿主内源性 GS 表达会干扰筛选效率，故有 GS 敲除宿主与减弱型 GS 突变体作为改进方案[^34][^35]；
- 维持稳定表达通常需要在培养中**持续存在 MSX**[^33]；
- 种子扩增阶段提高 MSX 浓度可提升 10–19% 的效价并改善生产稳定性，且该做法已在 500 L / 1000 L 生物反应器验证[^37]；
- **MSX 并非 GS 专一抑制剂**：它对谷氨酸半胱氨酸连接酶（GCL，谷胱甘肽合成的关键酶）的抑制程度与对 GS 相当[^36]。

→ 结论：MSX 属于**上游培养基引入的工艺相关杂质**，来源明确、可预期，必须做清除研究与残留控制。

#### 2）毒理学定性 —— 这是设限的依据，不能按普通助剂处理

> [!danger] MSX 是经典惊厥剂
> - MSX（MSO）诱导的惊厥与人类"大发作"型癫痫相似，伴脑内谷氨酰胺合成酶受抑[^38]；
> - 品系间敏感性差异极大：CBA/J 小鼠给药后 5–6 h 出现强直惊厥并**死于癫痫持续状态**；C57BL/6J 小鼠 8–14 h 出现强直与阵挛发作、死亡率 2%[^39]；经选育的 MSO-Fast 与 MSO-Slow 品系在剂量-反应曲线上呈现极大差异[^38]；
> - 机制之一是抑制 GS 造成**内源性氨中毒**：给药约 3 h 后即产生皮层突触后抑制的解除（"去抑制"），此时脑内氨升至正常值的 290%[^40]；MSX 亦是星形胶质细胞毒性的经典模型物质之一；
> - 大鼠腹腔 **75 mg/kg** 被作为**非惊厥剂量**用于癫痫模型的预处理[^41]。

→ 具有明确的中枢神经系统毒性终点与显著的个体/品系敏感性差异。**安全系数的设定必须覆盖这一差异。**

#### 3）建议方案

1. **清除研究**：以加标（spiking）方式，在纯化各单元操作前后定量 MSX，给出逐步清除倍数与总清除倍数；对最差情形（最高上游 MSX 浓度、最短纯化）做保守估算；
2. **检测方法**：LC-MS/MS；LOQ 应至少比拟定限度低一个数量级；完成方法学验证（专属性、线性、准确度、精密度、基质效应、LOQ）；
3. **限度推导路径**：
   - 以文献报道的非惊厥剂量（大鼠 ip 75 mg/kg[^41]）与惊厥/致死剂量[^38][^39]为出发点确定毒理学起点；
   - 按 PDE（允许日暴露量）思路推导，安全系数须覆盖：种属差异、个体敏感性差异（品系间差异极大[^38]）、给药途径差异（本品为静脉给药，无首过效应）、适应症人群状态（急性胰腺炎/重症患者可能存在肾功能不全，而 UTI 主要经肾清除[^27]）；
   - 以临床最大日剂量折算为原液/制剂中的浓度限度；
4. **控制策略**：
   - 若连续 ≥〔待填，建议 ≥6〕批实测均 < LOQ 且清除研究支持数个数量级的安全裕度 → 可提出以"工艺控制 + 定期确认（skip testing）"替代逐批放行检测；
   - 否则 → **纳入质量标准**，逐批放行检测。

#### 4）不要只答 MSX —— 主动扩展到其他工艺相关杂质

审评意见用了"如……等"的表述，仅答 MSX 会留下缺口。建议同时覆盖宿主细胞蛋白（HCP）、宿主 DNA、亲和配基脱落、消泡剂、以及一次性系统浸出物（见[[#稳-4 药包材相容性与安全性风险评估]]）。

其中 **HCP 中的水解酶类**值得单列，因为它有明确后果且难以清除：CHO 来源的脂肪酶类可水解聚山梨酯并生成游离脂肪酸颗粒，威胁制剂稳定性[^76]；脂蛋白脂肪酶（LPL）被证实对 PS-80/PS-20 具酶活，CRISPR/TALEN 敲除后收获液的聚山梨酯降解显著减轻[^74]；肝羧酸酯酶（CES）可通过高灵敏 LC-MS/MS-MRM（LOQ 0.05 ppm）实现亚 ppm 级监测[^75]。

> [!tip] 一个反例，值得写进答复以体现科学严谨
> 磷脂酶 B 样蛋白 2（PLBD2）曾被提出为聚山梨酯降解的元凶，但基因敲除与免疫消减实验显示去除 PLBD2 后 PS20/PS80 的降解**并未减轻或消除**，多个已配制抗体产品中 PLBD2 含量与 PS20 降解程度亦无相关性[^77]。
> → **杂质归因必须有实验证据，不能靠推测。** 在答复中体现这一原则，有助于建立方法学可信度。

---

### 质-5 SDS-PAGE 纯度方法、Marker 与条带弥散

> [!quote] 审评意见原文
> 建议完善本品纯度（如 SDS-PAGE）检测方法，明确 Marker 分子量分布情况，并关注本品蛋白条带分布较宽的原因。

#### 1）核心答复口径

> [!success] 一句话结论
> **本品在 SDS-PAGE 上呈弥散宽带，是蛋白聚糖分子的本征性质，而非纯度缺陷或降解。** 但这一结论必须用**酶解对照实验**证明，不能仅作声明。

#### 2）弥散的三重机制（均有文献支撑）

**机制一：GAG 链的长度与硫酸化度呈分布**

CS 链的分子量分布为 5 505–7 102 Da[^7]；以 ESI-FTMS 直接测定完整糖链，血浆 bikunin 的糖链以奇数个单糖残基者为主，链长 29–41 个单糖残基，多数为四硫酸化或五硫酸化[^8]；同一制剂内部即为硫酸化度与链长均不同的电荷异构体混合物[^9]；健康人与炎症患者之间链长与硫酸化度系统性不同[^10][^11]。一条分子量跨度约 1 600 Da、且电荷密度不均一的糖链，必然在 SDS-PAGE 上表现为弥散带。

**机制二：同类蛋白聚糖的直接实证**

> [!example] 最有说服力的类比证据
> XV 型胶原在人体组织中是一种硫酸软骨素蛋白聚糖。Western blot 显示其呈**平均 ≥400 kDa 的弥散涂抹（diffuse smear）**；经**软骨素酶消化后**，该涂抹收敛为脐带中的单一 250 kDa 条带，以及胎盘、肺、结肠与骨骼肌中的 250 kDa 与 225 kDa 双带[^65]。
> → 这为本品"弥散带 + 软骨素酶消化收敛"的证明实验提供了**完全同源的方法学先例**，建议在答复中直接引用。

**机制三：糖蛋白在 SDS-PAGE 中的普遍异常迁移**

糖蛋白在聚丙烯酰胺凝胶中存在异常迁移，同一样品在不同缓冲体系（Fairbanks vs Laemmli）中的迁移率不同，这一现象甚至被用于构建二维分离体系以分辨糖蛋白与非糖蛋白[^67]。另一例中，携带单条 CS 链的 SNORC 蛋白其 SDS-PAGE 异常迁移被归因于多肽自身的一级结构特征[^66] —— 说明异常迁移可同时来自糖链与多肽本身，需实验拆分。

本品的具体数据亦支持：核心蛋白理论分子量 15 340 Da（143 aa），而 SDS-PAGE 表观约 30 000 Da[^1]；以 SDS-PAGE、醋酸纤维素膜电泳、HP-SEC、CE 与 MALDI-TOF MS 系统比较不同批次与不同厂家的乌司他丁制剂，**SEC 与 SDS-PAGE 所得分子量与 MALDI-TOF MS 结果显著不同**[^23]。

#### 3）建议的证明实验（可直接写入答复）

| 实验 | 处理 | 预期结果 | 证明什么 |
|---|---|---|---|
| E1 | 软骨素酶 ABC（或 AC/B）消化前后并行 SDS-PAGE | 弥散带塌缩为锐利条带 | 弥散主要源于 CS 链分布 |
| E2 | PNGase F 消化 | 条带下移一个离散台阶 | N-糖的贡献（离散，非弥散） |
| E3 | E1 + E2 联合消化 | 单一锐利带，与核心蛋白理论 15.3 kDa 对齐[^1] | 核心蛋白均一、无降解 |
| E4 | 完整分子量 LC-MS / MALDI-TOF MS | 与 SDS-PAGE 表观值显著不同 | 表观分子量仅作鉴别，不作绝对定量依据[^23] |
| E5 | 阴离子交换 HPLC 分级后各组分 SDS-PAGE | 各组分迁移位置随硫酸化度递变 | 弥散 = 电荷异构体的连续分布[^9] |

> [!note] 关于 Marker
> 常用蛋白分子量 Marker 均为**非糖基化标准品**，其迁移行为与糖蛋白/蛋白聚糖不可直接比较。建议在答复中：
> 1. 列明所用 Marker 的品牌、批号与各条带标称分子量；
> 2. 说明本品与 Marker 迁移行为不可比的机理[^66][^67]；
> 3. 增加**糖蛋白 Marker** 与**本品酶解对照品**作为定位参照；
> 4. 将 SDS-PAGE 的定位由"分子量测定"改为"鉴别与限度检查"。

#### 4）纯度方法体系的重新定位

| 方法 | 用途 | 说明 |
|---|---|---|
| SDS-PAGE（还原/非还原） | 鉴别、杂质条带限度检查 | 不作为分子量绝对测定依据[^23] |
| CE-SDS | 定量纯度 | 精密度优于凝胶 |
| SEC-HPLC | 聚集体/片段 | 表观值受 GAG 流体力学行为影响，需说明[^23] |
| RP-HPLC / IEX-HPLC | 主成分与变异体 | IEX 兼作电荷异质性（见质-3） |
| 完整分子量 MS | 分子量确证 | 正交方法 |

制备型 SDS-PAGE 结合阴离子交换富集，是获得高纯度 UTI 样品供结构与功能研究的既有方法[^24]，可用于制备上述酶解对照品。

---

### 质-6 多批次数据积累与标准限度收紧

> [!quote] 审评意见原文
> 请随临床研究推进积累多批次原液及制剂检测结果及稳定性数据，合理收紧标准限度。

#### 1）先讲清"收紧"的统计学前提

早期以有限批次数据设限的常规做法（样本均值 ± 2–4 倍标准差）存在已知缺陷。设定与修订标准限度的可选统计方法包括参考区间、(Min, Max) 法、**容许区间（tolerance interval）**与分位数的置信限，各自的统计性质与适用条件不同[^68]。

> [!tip] 答复口径建议
> 主动说明将采用**容许区间/分位数置信限**方法，并给出批次数与置信-覆盖水平的对应关系，比笼统承诺"随批次收紧"更有说服力。

#### 2）分层设限原则（建议在答复中明确提出）

| 层级 | 属性举例 | 限度来源 | 是否随工艺能力收紧 |
|---|---|---|---|
| **A 安全性驱动** | 过硫酸化组分、MSX 残留、细菌内毒素、不溶性微粒、HCP、宿主 DNA | **毒理学/临床安全性推导** | 否 —— 不因工艺能力好就放宽，也不因工艺能力差就放宽 |
| **B 有效性驱动** | 效价、主峰纯度 | **临床暴露批的实测范围**为锚 | 可收紧，但不得宽于临床验证过的范围 |
| **C 一致性驱动** | 糖型分布、电荷分布、C 端变异体、表观分子量 | 工艺能力（历史区间） | 是，随批次累积逐步收紧 |

#### 3）一个应当引用的警示性实例

对来自中国 6 家与美国 1 家共 7 个重组人 IFNα2b 制剂、以及同一厂家 4 个批次，用 LC/Q-TOF 比较变异体与位点特异性修饰：5 个制剂检出 N 端半胱氨酸、甲硫氨酸与乙酰化半胱氨酸三种主要 N 端形式，而另一制剂仅检出天然 N 端形式；纯度最低的两个样品 N 端乙酰化水平最高[^69]。

> [!important] 含义
> **"符合药典"不等于"批间一致"，更不等于"厂家间一致"。** 历史区间必须由本品自建，不能援引同类产品或药典限度。这一实例同时支持质-1、质-2、质-3 的"自建区间"策略。

#### 4）答复承诺（建议表述）

1. 提交批次累积计划：至〔待填〕时点累积原液 ≥N 批、制剂 ≥M 批；
2. 明确限度修订的两个节点：**III 期临床启动前**、**上市申请时**，各做一次系统性修订；
3. 明确各质量属性所属层级（A/B/C）及其限度推导依据；
4. 稳定性数据同步纳入限度修订（货架期限度 vs 放行限度的差异化设定）。

---

## 四、内包材和稳定性（（四）项）

### 稳-1 长期稳定性考察与年度点全检

> [!quote] 审评意见原文
> 请继续规范开展原液和制剂的长期稳定性考察，结合质量标准完善情况完善稳定性研究考察项目；另外，建议在关键时间点（年度点）进行全检，关注效价、纯度及糖基化修饰的变化趋势。

#### 1）同意年度点全检，但需科学分层，避免变成无差别加项

> [!info] 哪些属性会随贮存变化，哪些不会

**会变的（必须列为趋势项）**

- **聚集体与亚可见微粒**：见[[#稳-2 使用中稳定性：微粒、无菌与细菌内毒素]]；
- **脱酰胺/氧化**：有直接实证 —— 某 IgG1 在贮存中形成的阳离子交换酸性峰，其降解物已被解析[^73]；脱酰胺是电荷异质性的主要来源[^48]，故电荷谱是脱酰胺的敏感指示；
- **原液冻融与冻存的特有风险**：
  - 冷冻使缓冲液 pH 漂移，磷酸钠体系在 +25 → −30 ℃ 时变化最大；组氨酸盐酸盐、醋酸钠、组氨酸醋酸盐、枸橼酸盐、琥珀酸盐均 < 1 个 pH 单位，Tris-HCl 约升高 1.2 个单位；该研究中聚集体形成与 pH 变化无关，而取决于是否存在非结晶性冷冻保护剂，且相变时间越长聚集越多[^72]；
  - 大容器冻存存在显著的**冷冻浓缩**：冻结态最浓处可达约 3 倍，解冻后未混匀前仍达 2.5 倍，且冻结态与解冻态的浓度梯度分布形态不同[^71]；
  - 但在系统评估冻融速率、冻结方式、容器、浓度与处方五个变量后，典型的**单次冻融**未见对原液质量的影响[^70]。

**通常不变的（但仍需监测，其价值在于反证）**

- N-糖与 O-连接 GAG 均为**共价修饰**，在无酶活条件下贮存期内不预期改变。
- → 因此"糖基化修饰变化趋势"这一项的**真正价值是反证残留宿主酶（糖苷酶/蛋白酶/脂肪酶）受控** —— 宿主水解酶在长期贮存中的缓慢作用是已被反复证实的现实风险[^74][^75][^76]，而归因必须有实验[^77]。建议在答复中把这一逻辑讲明，使该趋势项有明确的科学目的而非例行公事。

#### 2）建议的年度点全检项目

```
年度点全检 = 常规放行全项
           + N-糖谱（释放糖 HILIC-FLR/MS）
           + O-连接 GAG 二糖组成与链长分布
           + 电荷异构体谱（icIEF + AEX-HPLC）
           + C 端变异体定量（LC-MS 肽图）
           + 完整分子量（LC-MS）
           + 亚可见微粒（光阻法 + 流式成像）
```

#### 3）需补充的针对性研究

1. **冻融研究**：明确原液允许的冻融次数上限与冻结/解冻速率范围[^70]；
2. **冷冻浓缩评估**：按实际冻存容器规格评估浓度与 pH 梯度，并明确解冻后的混匀要求[^71]；
3. **缓冲体系冷冻 pH 漂移**：〔待填：本品处方缓冲体系〕若为磷酸盐体系，需重点评估[^72]；
4. **强制降解与降解途径鉴定**：为稳定性指示方法提供依据。

---

### 稳-2 使用中稳定性：微粒、无菌与细菌内毒素

> [!quote] 审评意见原文
> 制剂使用中稳定性考察请完善不溶性微粒、无菌、细菌内毒素等安全性相关检项的检查，否则建议取出后药液尽快输注。

> [!important] 这条意见本质上是一个交换条件
> **做研究 → 换取更宽的使用期限标签；不做研究 → 接受"尽快输注"的严格限制。** 建议明确选择前者，并按下述方案设计。

#### 1）使用中稳定性必须模拟真实输注链路，而不只是"稀释后放置"

> [!warning] 输注装置本身就是微粒来源
> 对利妥昔单抗与 IVIG 的系统研究显示：**蠕动泵**（Medifusion DI-2000）较重力输注系统产生显著更多的亚可见微粒（以 < 25 µm 为主），且随流速升高而加剧，在无表面活性剂的处方中尤为明显；稀释剂种类（0.9% 氯化钠 vs 5% 葡萄糖）与注射器是否含硅油同样增加微粒数[^78]。
> → 使用中稳定性方案必须覆盖：**输液袋材质 × 稀释剂 × 稀释浓度 × 输注方式（重力/泵）× 流速 × 注射器材质 × 放置温度 × 放置时长 × 光照**。

其他必须覆盖的因素：

- **低浓度吸附损失**：低剂量、高活性生物制品在静脉给药时存在真实的吸附损失与氧化降解风险，需通过处方开发与在用研究共同控制，方能实现 0.1–0.5 mg 总蛋白量级的临床给药[^79]。本品若在稀释后浓度较低，此项为**关键风险**。
- **可参照的研究深度**：已上市生物类似药的在用稳定性研究通常覆盖 PE 与 PVC 输液袋、2–8 ℃ 贮存 2/4/6 周 + 室温 24 h，检测亚可见微粒、杂质、电荷变体、重轻链含量，并含细胞水平结合活性与 CDC 功能试验[^80]。

#### 2）不溶性微粒：方法与判读

- 光阻法是 2–100 µm 区间最常用的定量技术，但无法区分微粒类型；**0.1–2 µm 区间目前无常规方法**[^83]；
- 各类可见与亚可见微粒分析方法的原理、优势与局限见系统综述[^82]；悬浮微通道谐振器等新方法可依浮力质量区分硅油液滴与蛋白微粒（约 0.5–5 µm）[^84]；
- **行业共识需要如实引用**：亚可见微粒与临床免疫原性之间的因果关系**尚未被明确证实**；受限于测量技术、容器/密封系统、浓度、黏度与批间固有异质性，此类测量目前**不适合作为放行与稳定性的质量标准或可比性依据**，其价值在于产品开发与表征[^81]。
- 容器与器具材质的影响：聚合物预灌封注射器与玻璃注射器在未润滑时聚集与微粒水平相近，**硅油润滑**是主要变量[^85]。

> [!tip] 答复口径建议
> 对不溶性微粒，建议明确区分：**药典项（≥10 µm / ≥25 µm，放行与稳定性执行）** 与 **表征项（亚可见微粒全谱，用于开发与在用研究，不设放行限度）**。主动引用行业共识[^81]说明后者不设限度的理由，可避免被要求为表征项设定标准。

#### 3）关于终端在线过滤器

在儿科多药输注模型中引入在线过滤器可使微粒总数由 416 974 个降至 7 551 个，≥10 µm 与 ≥25 µm 的大微粒亦显著减少；但在过滤器出口再加延长管（内容积 1.7 mL）会重新显著增加微粒污染[^86]。

> [!caution] 若拟在说明书中推荐在线过滤
> 必须同时验证**滤膜对本品的吸附损失**与**滤膜浸出物**（见[[#稳-4 药包材相容性与安全性风险评估]]）。对低浓度稀释液，吸附可能造成实际给药剂量偏低[^79]。

#### 4）细菌内毒素：不要默认合规

稀释后体系（尤其含枸橼酸/磷酸盐 + 聚山梨酯的处方）存在**低内毒素回收（LER）**争议：

- 一项研究在枸橼酸、组氨酸、磷酸、醋酸钠等含聚山梨酯的多种基质中，以内毒素加标法考察至 6 个月，均获得可接受的回收率，认为未观察到掩蔽效应，并强调研究设计对结论的决定性影响[^87]；
- 另一项研究则显示掩蔽动力学随 LPS 结构（粗糙型 vs 光滑型）而异，LAL 与 rFC 动力学相近，而单核细胞激活试验（MAT）对被掩蔽内毒素的回收更好[^88]。

> [!tip] 答复口径建议
> 结论有分歧 → 因此**必须做本品自己的加标回收（hold-time spike recovery）研究**，而不是引用任一方结论。建议在使用中稳定性方案中固化该研究，并说明方法（LAL/rFC，必要时 MAT 佐证）。

#### 5）无菌

使用中稳定性中的无菌考察应结合**配制环境**（病房配制 vs 静配中心）设定最差情形；若拟支持较长的稀释后放置时间，需以微生物挑战试验数据支持，而非仅以化学稳定性数据外推。

#### 6）答复承诺（建议表述）

1. 提交覆盖上述全部变量的使用中稳定性方案与数据；
2. 明确稀释后在 2–8 ℃ 与室温下的最长放置时间，并以数据替代"尽快输注"的表述；
3. 提交内毒素加标回收研究；
4. 若推荐在线过滤，同时提交滤膜吸附与浸出物数据。

---

### 稳-3 临床试验用样品的储运与使用控制

> [!quote] 审评意见原文
> 临床试验用样品的保存、运输和使用请确保在经过确认的条件范围内。

核心原则：**"经确认的条件范围"必须与稳定性数据的边界严格对齐** —— 每一个允许的操作条件都要能追溯到一项稳定性研究。

| 环节 | 控制要求 | 数据支撑 |
|---|---|---|
| 原液冻存与运输 | 冻融次数上限、冻结/解冻速率、容器规格、解冻后混匀要求 | 冻融研究[^70]；冷冻浓缩梯度[^71]；缓冲体系冷冻 pH 漂移[^72] |
| 制剂运输 | 运输验证含最坏情形（夏/冬季、最长在途、振动）；全程温度监控 | 加速与长期稳定性；运输模拟 |
| 温度偏移 | 允许的偏移次数与累计时长 | 温度循环研究 |
| 中心贮存 | 温度范围、监控频次、报警与响应 | 长期稳定性 |
| 配制与给药 | 开瓶后/稀释后最长放置时间、输液袋与输注装置材质、输注时长 | 使用中稳定性[^78][^80] |
| 偏差处理 | 偏差 → 质量影响评估 → 可用性判定的书面流程 | 稳定性数据边界 |

> [!tip] 答复承诺（建议表述）
> 1. 提交临床试验用药品管理手册（含储运、配制、给药与偏差处理规程）；
> 2. 提交运输验证报告（含最坏情形）；
> 3. 明确温度偏移的允收标准及其稳定性数据依据；
> 4. 建立温度监控数据的定期回顾机制。

---

### 稳-4 药包材相容性与安全性风险评估

> [!quote] 审评意见原文
> 请规范开展原液、制剂的药包材相容性研究和安全性风险评估，关注生产中直接接触产品的储液袋、滤膜等的相容性。

建议将研究分为**两层**：生产用一次性系统（储液袋、管路、滤膜）与直接接触药品的内包材及给药器具。

#### 1）生产用一次性系统：已知高风险浸出物必须点名

> [!danger] bDtBPP —— 一次性系统最著名的细胞毒性浸出物
> 双(2,4-二叔丁基苯基)磷酸酯（bDtBPP）是聚乙烯膜材中常用抗氧剂 Irgafos 168 的降解产物，**经辐照灭菌（γ 辐照）后生成显著增加**；在远低于 ppm 的浓度即对多种哺乳动物细胞系产生明显生长抑制，并迅速降低线粒体膜电位；其从聚乙烯膜材的迁移呈时间与温度依赖[^94]。
> 后续研究进一步显示，两株 CHO 细胞在 **0.035–0.1 mg/L** 即受抑制，低于此前报道的 0.12–0.73 mg/L 区间，而这一浓度恰好处于生物工艺早期即可浸出的水平，**接种阶段即面临风险**[^95]；另有研究以 PER.C6 细胞系评估其敏感性并考察新型生物相容膜材[^96]。改进后的新一代一次性生物反应器膜材可显著降低包括 bDtBPP 在内的浸出物丰度并改善 CHO 细胞生长；值得注意的是，该已知浸出物在体外内分泌干扰测试中表现出**雄激素拮抗**潜力[^97]。

→ **结论：储液袋筛选不能只做化学谱，必须做细胞生长/细胞毒性评估。** 这一点建议在答复中主动提出。

其他基础数据：

- 系统化的可提取物研究已从多种工艺接触材料中鉴定并定量出 **200 余种**有机可提取物[^92]；
- 对 4 类市售一次性生物工艺设备的非靶向分析共鉴定出 **53 种**有机可提取物[^90]；
- 大规模评估覆盖 34 种一次性袋膜材，以代表最差情形的溶剂体系提取并在加速老化条件下考察浸出物，采用 GC-headspace（挥发性）、高分辨 GC-Orbitrap-MS/MS（半挥发性）与高分辨 LC-Orbitrap 分析[^89]；另有针对一次性袋可提取物的分析与验证评价方法[^91]。

**清除能力可量化**：将 7 种代表性可提取物/浸出物（三甲基硅醇、己酸、丁内酯、叔丁醇、己内酰胺、乙腈、苯甲醇）加标至 4 种代表性蛋白溶液，以定量 NMR 监测超滤/透析过滤（UF/DF）过程，结果显示最高 1 000 ppm 的初始负载可在 **9 个透析体积**内清除至 < 1 ppm；但部分情形下回收液中存在**回弹（rebound）**至 > 1 ppm 的现象[^93]。

> [!tip] 用法提示
> 该清除数据可作为方案设计的依据，但**不能直接引用为本品的清除结论** —— 必须做本品自己的加标清除研究，并特别关注回弹现象。

#### 2）滤膜

- **吸附损失**：低浓度原液或稀释后药液经无菌过滤时的回收率必须实测；低剂量生物制品的吸附损失是已证实的风险[^79]；
- **滤膜浸出物**：纳入可提取物研究范围；
- 建议在滤器验证（细菌截留、化学相容性、可提取物）中**同时纳入产品回收率**。

#### 3）直接接触药品的内包材与给药器具

- **PVC 输液器的 DEHP 浸出**：紫杉醇输液可从 PVC 材料中浸出增塑剂 DEHP，故其配制与给药应使用无 PVC 材料；该研究同时评估了多种给药器具与在线过滤器组合的适用性[^98]；
- **注射器材质与硅油**：未润滑的聚合物注射器与玻璃注射器在聚集与微粒上相近，硅油润滑是主要变量[^85]；
- 内包材（西林瓶、胶塞）的相容性与密封完整性按常规要求开展。

#### 4）风险评估路径

建议采用基于 ICH Q9 与 ICH Q8(R2) 原则的**整体性、分阶段（phase-appropriate）**策略：从材料筛选/选择/确认阶段的可提取物研究，推进到终产品的浸出物研究；提取研究需审慎考虑溶剂化效应、pH、离子强度、温度、产品接触表面与接触时长[^92]。

#### 5）答复承诺（建议表述）

1. 提交**材料清单**：所有产品接触材料（膜材、管路、滤膜、储液袋、连接件、内包材）及其牌号、灭菌方式（**注明是否辐照** —— 直接关系 bDtBPP[^94]）；
2. 提交**接触矩阵**：材料 × 接触介质 × 温度 × 时长 × 表面积/体积比；
3. 提交**可提取物研究方案与结果**（模型溶剂、加速老化、GC/LC-HRMS）[^89][^90][^91]；
4. 提交**细胞生长影响评估**（储液袋膜材，覆盖 bDtBPP 敏感浓度区间）[^94][^95][^96][^97]；
5. 提交**浸出物确认研究**时点（拟定：III 期临床用批 + 注册批）与**毒理学评估**（安全性关注阈值/PDE 判定）；
6. 提交**清除研究**（UF/DF 加标清除，含回弹考察）[^93]；
7. 提交**滤膜吸附与回收率**数据[^79]。

---

## 五、临床有效性背景（供药学答复中"对有效性的影响"表述时引用）

答复中多处需要论述"对有效性的影响"。有效性主张的临床证据基础需如实呈现，避免夸大：

- 一项针对**重症急性胰腺炎**的系统评价与荟萃分析（PRISMA 2020，纳入 7 项研究）显示乌司他丁可显著降低死亡风险[^99]；
- 乌司他丁**联合生长抑素/类似物**的荟萃分析（9 篇、1 037 例 RCT）显示联合治疗显著降低 ARDS、AKI 与 MODS 的并发症率[^100]；
- 但 **Cochrane 系统评价**指出，急性胰腺炎在支持治疗之外，各类药物干预的作用**仍不明确**；由于缺乏潜在效应修饰因素的信息且各比较纳入人群存在差异，未能按计划完成网状荟萃分析[^101]；
- 在**脓毒症**适应症上，纳入 13 项 RCT 与 2 项前瞻性研究、共 1 358 例的荟萃分析显示乌司他丁显著降低全因死亡率（OR = 0.48, 95% CI 0.35–0.66）、APACHE II 评分与 MODS 发生率[^102]。

> [!warning] 表述纪律
> 在药学答复中援引临床证据时，应同时呈现 Cochrane 的保留意见[^101]。**只引用阳性结果会削弱整份答复的可信度**；如实呈现证据强度反而更有助于说明"为何必须把质量属性控制住" —— 正因为临床效应量存在不确定性，质量属性的漂移空间才更小。

---

## 六、答复完整性自查清单

- [ ] 三个糖基化位点的化学身份已明确（尤其第二个 O 位点）
- [ ] 已说明重组表达系统中 Ser10 GAG 的实际装配情况，并主动申明与提取品的结构差异
- [ ] 效价方法已升级为可分辨 2 倍差异的剂量-反应方法
- [ ] 过硫酸化组分已作为安全性属性提出，并配套功能学（APTT/前激肽释放酶）评估
- [ ] C 端切点已精确定位（完整分子量 + C 端肽图）
- [ ] C 端变异体的根因分析已覆盖痕量元素、Arg/Lys 浓度、收获时机
- [ ] 电荷异质性方案含 icIEF 与 AEX-HPLC 双正交
- [ ] MSX 清除研究、LC-MS/MS 方法学验证、PDE 推导三件齐备
- [ ] MSX 之外的工艺相关杂质（HCP 水解酶类等）已一并覆盖
- [ ] SDS-PAGE 弥散的酶解对照实验（E1–E5）已完成
- [ ] Marker 的品牌/批号/标称分子量已列明，并说明与本品不可比的机理
- [ ] 标准限度已按 A/B/C 三层分类，并明确两个修订节点
- [ ] 年度点全检项目已列明，并说明糖型趋势项的科学目的
- [ ] 使用中稳定性已覆盖输注装置、流速、注射器材质等真实链路变量
- [ ] 内毒素加标回收研究已纳入
- [ ] 一次性系统灭菌方式（是否辐照）已注明，bDtBPP 风险已评估
- [ ] 滤膜吸附回收率数据已提交
- [ ] 全部 `〔待填〕` 项已由自有数据填充

---

## 七、局限性与本文未覆盖的内容

> [!failure] 本文不能替代的工作
> 1. **无本品自有数据。** 全部工艺、检测与批次数据均以 `〔待填〕` 标注，需由申报方填充。文中的机理论证可直接使用，数据结论不可。
> 2. **检索仅覆盖 PubMed。** 未覆盖：中国药典与 ICH/USP/EP 指导原则原文（属一次文献，需另行逐条比对）、CDE 已发布的技术指导原则、行业白皮书（BPOG、PDA TR 系列）、未被 PubMed 收录的中文文献、企业内部数据与专利文献。
> 3. **法规条款未逐条核对。** 文中涉及 ICH Q6A/Q9/Q8(R2) 的表述来自二次文献的转述[^68][^92]，**引用前须核对指导原则原文**。同理，不溶性微粒、无菌、细菌内毒素的具体药典方法与限度须以现行版《中国药典》为准。
> 4. **"2 个 O-糖基化位点"的第二位点身份未能从公开文献确认。** 公开文献一致支持 Ser10 的 GAG 位点[^3][^4]，第二个 O 位点的鉴定依赖申报方自有数据。
> 5. **CrossRef 独立核验未能完成**（原因见下）。

---

## 引用可靠性声明

> [!warning] 请先读这一段再使用本文的任何引用
> **已完成的核验：** 本文引用 103 篇文献，全部经 NCBI PubMed E-utilities 在本次工作中**实时检索并逐条取回原始记录**；题名、作者、期刊、年份与 DOI 均取自返回的记录字段，**无一条从记忆重建**。已对全部取回记录扫描 PubMed 的 `Retracted Publication` / `Erratum` / `Expression of Concern` / `Corrected` 标记，命中 **1 篇**（PMID 10589650，"The ulinastatin-induced effect on neuromuscular block caused by vecuronium"，*Anesth Analg* 1999，已撤稿）—— **该文未被本文引用**。
>
> **未能完成的核验：** 本工作环境的出站网络策略**封禁了 `api.crossref.org`**（网关对 CONNECT 请求返回 403），因此计划中的"逐个 DOI 经 CrossRef 独立解析"**未能执行**。这意味着 DOI 字符串的正确性目前**仅由 PubMed 单一来源保证**，未获第二来源交叉确认。
> → **正式提交前，请对全部 100 个 DOI 做一次 CrossRef 或出版商侧解析。**
>
> **其他限制：**
> - **卷、期、页码未经核验，故一律未列**（格式化时如需补充，请核对 PDF 首页）；
> - **3 篇**文献 PubMed 未著录 DOI（文献 **4**、**5**、**103**），参考文献表中已粗体标注，引用时请以 PMID 检索；
> - 部分结论来自摘要而非全文，涉及具体数值时已标注原文表述。

### 检索方法学附录

| 项 | 内容 |
|---|---|
| 数据库 | PubMed（经 MCP 接口调用 NCBI E-utilities） |
| 检索日期 | 2026-09-06 |
| 检索轮次 | 3 轮（自然语言 → 布尔/引号短语 → 机制、方法与反证词） |
| 主题域 | 14 个（糖基化生物学、重组表达与 GAG 装配、GS/MSX 系统、MSX 毒理、C 端变异体、电荷异质性、OSCS 安全性、糖型-免疫原性-清除、SDS-PAGE 迁移、标准限度统计、稳定性与冻融、HCP 水解酶、使用中稳定性与微粒、可提取物与浸出物、临床有效性） |
| 取回并建库记录数 | 154 篇 |
| 引用篇数 | 103 篇 |
| 全文核对 | 1 篇（文献 17，经 PMC 取回全文核对 Table 1 的 IC₅₀ 数值与浓度依赖性表述） |
| 饱和判据 | 窄化后的短语检索（如 `"C-terminal" AND clipping AND CHO`、`"sialic acid" AND hydrolysis AND storage`）返回 0 或无新增记录，判定该主题检索饱和 |
| 反证检索 | 已执行。例：聚山梨酯降解的 PLBD2 归因反例[^77]；电荷变体"无影响"的抗体证据[^49]；内毒素掩蔽"不存在"的证据[^87] |
| 接口特性说明 | 该 PubMed 接口对长自然语言查询逐词 AND，导致零召回；已改用 ≤5 词的短语式布尔查询 |
| 未覆盖 | 药典/ICH 原文、CDE 指导原则、行业白皮书（BPOG/PDA TR）、非 PubMed 收录中文文献、专利 |

---

## 参考文献

> 编号与正文脚注一一对应。全部条目来自本次实时取回的 PubMed 记录；卷/期/页未经核验故未列。

### 分组索引

| 组 | 主题 | 编号 |
|---|---|---|
| A | 乌司他丁分子结构、糖基化与功能 | 1-27 |
| B | 重组表达、糖链装配与 GS/MSX 宿主系统 | 28-37、103 |
| C | MSX 毒理学 | 38-41 |
| D | C 端变异体与羧肽酶加工 | 42-47 |
| E | 电荷异质性 | 48-51 |
| F | 硫酸化糖胺聚糖的安全性风险（OSCS 事件） | 52-56 |
| G | 糖基化对安全性、有效性与药代的影响 | 57-64 |
| H | SDS-PAGE 表观分子量与条带弥散 | 65-67 |
| I | 标准限度制定与批间一致性 | 68-69 |
| J | 原液/制剂稳定性、冻融与降解途径 | 70-77 |
| K | 使用中稳定性、不溶性微粒与细菌内毒素 | 78-88 |
| L | 药包材相容性、可提取物与浸出物 | 89-98 |
| M | 乌司他丁临床有效性证据 | 99-102 |

### 文献条目

[^1]: Wachter E, Hochstrasser K. Kunitz-type proteinase inhibitors derived by limited proteolysis of the inter-alpha-trypsin inhibitor, IV. The amino acid sequence of the human urinary trypsin inhibitor isolated by affinity chromatography. *Hoppe Seylers Z Physiol Chem*. 1981. DOI: [10.1515/bchm2.1981.362.2.1351](https://doi.org/10.1515/bchm2.1981.362.2.1351). PMID: 6171496.
[^2]: Hochstrasser K, Schönberger OL, Rossmanith I, et al. Kunitz-type proteinase inhibitors derived by limited proteolysis of the inter-alpha-trypsin inhibitor, V. Attachments of carbohydrates in the human urinary trypsin inhibitor isolated by affinity chromatography. *Hoppe Seylers Z Physiol Chem*. 1981. DOI: [10.1515/bchm2.1981.362.2.1357](https://doi.org/10.1515/bchm2.1981.362.2.1357). PMID: 6171497.
[^3]: Chirat F, Balduyck M, Mizon C, et al. A chondroitin-sulfate chain is located on serine-10 of the urinary trypsin inhibitor. *Int J Biochem*. 1991. DOI: [10.1016/0020-711x(91)90216-a](https://doi.org/10.1016/0020-711x(91)90216-a). PMID: 1794445.
[^4]: Enghild JJ, Salvesen G, Thøgersen IB, et al. Presence of the protein-glycosaminoglycan-protein covalent cross-link in the inter-alpha-inhibitor-related proteinase inhibitor heavy chain 2/bikunin. *J Biol Chem*. 1993. **PubMed 未著录 DOI**. PMID: 7682553.
[^5]: Enghild JJ, Thøgersen IB, Pizzo SV, et al. Analysis of inter-alpha-trypsin inhibitor and a novel trypsin inhibitor, pre-alpha-trypsin inhibitor, from human plasma. Polypeptide chain stoichiometry and assembly by glycan. *J Biol Chem*. 1989. **PubMed 未著录 DOI**. PMID: 2476436.
[^6]: Thøgersen IB, Enghild JJ. Biosynthesis of bikunin proteins in the human carcinoma cell line HepG2 and in primary human hepatocytes. Polypeptide assembly by glycosaminoglycan. *J Biol Chem*. 1995. DOI: [10.1074/jbc.270.31.18700](https://doi.org/10.1074/jbc.270.31.18700). PMID: 7543108.
[^7]: Chi L, Wolff JJ, Laremore TN, et al. Structural analysis of bikunin glycosaminoglycan. *J Am Chem Soc*. 2008. DOI: [10.1021/ja0778500](https://doi.org/10.1021/ja0778500). PMID: 18247611.
[^8]: Laremore TN, Leach FE, Amster IJ, et al. Electrospray ionization Fourier transform mass spectrometric analysis of intact bikunin glycosaminoglycan from normal human plasma. *Int J Mass Spectrom*. 2011. DOI: [10.1016/j.ijms.2010.09.020](https://doi.org/10.1016/j.ijms.2010.09.020). PMID: 21860600.
[^9]: Kakizaki I, Takahashi R, Ibori N, et al. Diversity in the degree of sulfation and chain length of the glycosaminoglycan moiety of urinary trypsin inhibitor isomers. *Biochim Biophys Acta*. 2006. DOI: [10.1016/j.bbagen.2006.09.026](https://doi.org/10.1016/j.bbagen.2006.09.026). PMID: 17175105.
[^10]: Capon C, Mizon C, Lemoine J, et al. In acute inflammation, the chondroitin-4 sulphate carried by bikunin is not only longer, it is also undersulphated. *Biochimie*. 2003. DOI: [10.1016/s0300-9084(03)00066-x](https://doi.org/10.1016/s0300-9084(03)00066-x). PMID: 12765780.
[^11]: Mizon C, Mairie C, Balduyck M, et al. The chondroitin sulfate chain of bikunin-containing proteins in the inter-alpha-inhibitor family increases in size in inflammatory diseases. *Eur J Biochem*. 2001. DOI: [10.1046/j.1432-1327.2001.02168.x](https://doi.org/10.1046/j.1432-1327.2001.02168.x). PMID: 11322893.
[^12]: Toyoda H, Ikei T, Demachi Y, et al. Structural analysis of the N-linked oligosaccharides from human urinary trypsin inhibitor. *Chem Pharm Bull (Tokyo)*. 1992. DOI: [10.1248/cpb.40.2882](https://doi.org/10.1248/cpb.40.2882). PMID: 1464122.
[^13]: Xu Y, Carr PD, Guss JM, et al. The crystal structure of bikunin from the inter-alpha-inhibitor complex: a serine protease inhibitor with two Kunitz domains. *J Mol Biol*. 1998. DOI: [10.1006/jmbi.1997.1582](https://doi.org/10.1006/jmbi.1997.1582). PMID: 9566199.
[^14]: Morishita H, Yamakawa T, Matsusue T, et al. Novel factor Xa and plasma kallikrein inhibitory-activities of the second Kunitz-type inhibitory domain of urinary trypsin inhibitor. *Thromb Res*. 1994. DOI: [10.1016/0049-3848(94)90098-1](https://doi.org/10.1016/0049-3848(94)90098-1). PMID: 8191413.
[^15]: Lu W, Apostol I, Qasim MA, et al. Binding of amino acid side-chains to S1 cavities of serine proteinases. *J Mol Biol*. 1997. DOI: [10.1006/jmbi.1996.0781](https://doi.org/10.1006/jmbi.1996.0781). PMID: 9047374.
[^16]: Pratt CW, Pizzo SV. Mechanism of action of inter-alpha-trypsin inhibitor. *Biochemistry*. 1987. DOI: [10.1021/bi00384a029](https://doi.org/10.1021/bi00384a029). PMID: 2440471.
[^17]: Teshigahara Y, Kakizaki I, Hirao W, et al. A Chondroitin Sulfate Chain of Urinary Trypsin Inhibitor Enhances Protease Inhibitory Activity of the Core Protein. *J Appl Glycosci (1999)*. 2021. DOI: [10.5458/jag.jag.JAG-2019_0021](https://doi.org/10.5458/jag.jag.JAG-2019_0021). PMID: 34354530.
[^18]: Kakizaki I, Takahashi R, Yanagisawa M, et al. Enzymatic synthesis of hyaluronan hybrid urinary trypsin inhibitor. *Carbohydr Res*. 2015. DOI: [10.1016/j.carres.2015.05.009](https://doi.org/10.1016/j.carres.2015.05.009). PMID: 26142361.
[^19]: Suzuki M, Kobayashi H, Tanaka Y, et al. Structure and function analysis of urinary trypsin inhibitor (UTI): identification of binding domains and signaling property of UTI by analysis of truncated proteins. *Biochim Biophys Acta*. 2001. DOI: [10.1016/s0167-4838(01)00167-4](https://doi.org/10.1016/s0167-4838(01)00167-4). PMID: 11343788.
[^20]: Kato Y, Kudo M, Shinkawa T, et al. Role of O-linked carbohydrate of human urinary trypsin inhibitor on its lysosomal membrane-stabilizing property. *Biochem Biophys Res Commun*. 1998. DOI: [10.1006/bbrc.1998.8100](https://doi.org/10.1006/bbrc.1998.8100). PMID: 9480817.
[^21]: Kanayama N, Maehara K, Suzuki M, et al. The role of chondroitin sulfate chains of urinary trypsin inhibitor in inhibition of LPS-induced increase of cytosolic free Ca2+ in HL60 cells and HUVEC cells. *Biochem Biophys Res Commun*. 1997. DOI: [10.1006/bbrc.1997.7344](https://doi.org/10.1006/bbrc.1997.7344). PMID: 9299551.
[^22]: Hirashima Y, Kobayashi H, Suzuki M, et al. Characterization of binding properties of urinary trypsin inhibitor to cell-associated binding sites on human chondrosarcoma cell line HCS-2/8. *J Biol Chem*. 2001. DOI: [10.1074/jbc.M009906200](https://doi.org/10.1074/jbc.M009906200). PMID: 11278581.
[^23]: Matsuno YK, Nakamura H, Kakehi K. Comparative studies on the analysis of urinary trypsin inhibitor (ulinastatin) preparations. *Electrophoresis*. 2006. DOI: [10.1002/elps.200500854](https://doi.org/10.1002/elps.200500854). PMID: 16786482.
[^24]: Nieddu G, Formato M, Lepedda AJ. A Method for Urinary Trypsin Inhibitor (UTI) Purification Combining Anion-Exchange Chromatography Enrichment and Preparative SDS-PAGE. *Methods Mol Biol*. 2023. DOI: [10.1007/978-1-0716-2946-8_17](https://doi.org/10.1007/978-1-0716-2946-8_17). PMID: 36662474.
[^25]: Pendlebury D, Wang R, Henin RD, et al. Sequence and conformational specificity in substrate recognition: several human Kunitz protease inhibitor domains are specific substrates of mesotrypsin. *J Biol Chem*. 2014. DOI: [10.1074/jbc.M114.609560](https://doi.org/10.1074/jbc.M114.609560). PMID: 25301953.
[^26]: Cohen I, Coban M, Shahar A, et al. Disulfide engineering of human Kunitz-type serine protease inhibitors enhances proteolytic stability and target affinity toward mesotrypsin. *J Biol Chem*. 2019. DOI: [10.1074/jbc.RA118.007292](https://doi.org/10.1074/jbc.RA118.007292). PMID: 30700553.
[^27]: Jönsson-Berling BM, Ohlsson K. Distribution and elimination of intravenously injected urinary trypsin inhibitor. *Scand J Clin Lab Invest*. 1991. DOI: [10.3109/00365519109104564](https://doi.org/10.3109/00365519109104564). PMID: 1767247.
[^28]: Falkenberg C, Wester L, Belting M, et al. Expression of a functional proteinase inhibitor capable of accepting xylose: bikunin. *Arch Biochem Biophys*. 2001. DOI: [10.1006/abbi.2000.2213](https://doi.org/10.1006/abbi.2000.2213). PMID: 11368189.
[^29]: Casanova JC, Kuhn J, Kleesiek K, et al. Heterologous expression and biochemical characterization of soluble human xylosyltransferase II. *Biochem Biophys Res Commun*. 2007. DOI: [10.1016/j.bbrc.2007.10.206](https://doi.org/10.1016/j.bbrc.2007.10.206). PMID: 18023272.
[^30]: Roch C, Kuhn J, Kleesiek K, et al. Differences in gene expression of human xylosyltransferases and determination of acceptor specificities for various proteoglycans. *Biochem Biophys Res Commun*. 2009. DOI: [10.1016/j.bbrc.2009.11.121](https://doi.org/10.1016/j.bbrc.2009.11.121). PMID: 19944077.
[^31]: Jian-qiu W, Feng-qin Y, Dou-dou W, et al. Expression and purification of active recombinant human bikunin in Pichia pastoris. *Protein Expr Purif*. 2008. DOI: [10.1016/j.pep.2008.03.025](https://doi.org/10.1016/j.pep.2008.03.025). PMID: 18501630.
[^32]: Yao M, Zhang J, Wang X. High-level secretion of human bikunin from recombinant Pichia pastoris. *Lett Appl Microbiol*. 2015. DOI: [10.1111/lam.12470](https://doi.org/10.1111/lam.12470). PMID: 26202000.
[^33]: de la Cruz Edmonds MC, Tellers M, Chan C, et al. Development of transfection and high-producer screening protocols for the CHOK1SV cell system. *Mol Biotechnol*. 2006. DOI: [10.1385/mb:34:2:179](https://doi.org/10.1385/mb:34:2:179). PMID: 17172663.
[^34]: Fan L, Kadura I, Krebs LE, et al. Improving the efficiency of CHO cell line generation using glutamine synthetase gene knockout cells. *Biotechnol Bioeng*. 2011. DOI: [10.1002/bit.24365](https://doi.org/10.1002/bit.24365). PMID: 22068567.
[^35]: Lin PC, Chan KF, Kiess IA, et al. Attenuated glutamine synthetase as a selection marker in CHO cells to efficiently isolate highly productive stable cells for the production of antibodies and other biologics. *MAbs*. 2019. DOI: [10.1080/19420862.2019.1612690](https://doi.org/10.1080/19420862.2019.1612690). PMID: 31043114.
[^36]: Feary M, Racher AJ, Young RJ, et al. Methionine sulfoximine supplementation enhances productivity in GS-CHOK1SV cell lines through glutathione biosynthesis. *Biotechnol Prog*. 2016. DOI: [10.1002/btpr.2372](https://doi.org/10.1002/btpr.2372). PMID: 27689785.
[^37]: Tian J, He Q, Oliveira C, et al. Increased MSX level improves biological productivity and production stability in multiple recombinant GS CHO cell lines. *Eng Life Sci*. 2020. DOI: [10.1002/elsc.201900124](https://doi.org/10.1002/elsc.201900124). PMID: 32874175.
[^38]: Boissonnet A, Hévor T, Cloix JF. Phenotypic differences between fast and slow methionine sulfoximine-inbred mice: seizures, anxiety, and glutamine synthetase. *Epilepsy Res*. 2011. DOI: [10.1016/j.eplepsyres.2011.08.012](https://doi.org/10.1016/j.eplepsyres.2011.08.012). PMID: 22050980.
[^39]: Bernard-Helary K, Lapouble E, Ardourel M, et al. Correlation between brain glycogen and convulsive state in mice submitted to methionine sulfoximine. *Life Sci*. 2000. DOI: [10.1016/s0024-3205(00)00756-6](https://doi.org/10.1016/s0024-3205(00)00756-6). PMID: 11021361.
[^40]: Raabe WA, Onstad GR. Ammonia and methionine sulfoximine intoxication. *Brain Res*. 1982. DOI: [10.1016/0006-8993(82)90312-2](https://doi.org/10.1016/0006-8993(82)90312-2). PMID: 7116136.
[^41]: Pawlik M, Czarnecka AM, Kołodziej M, et al. Attenuation of initial pilocarpine-induced electrographic seizures by methionine sulfoximine pretreatment tightly correlates with the reduction of extracellular taurine in the hippocampus. *Epilepsia*. 2023. DOI: [10.1111/epi.17554](https://doi.org/10.1111/epi.17554). PMID: 36808593.
[^42]: Hu Z, Zhang H, Haley B, et al. Carboxypeptidase D is the only enzyme responsible for antibody C-terminal lysine cleavage in Chinese hamster ovary (CHO) cells. *Biotechnol Bioeng*. 2016. DOI: [10.1002/bit.25977](https://doi.org/10.1002/bit.25977). PMID: 26989081.
[^43]: Luo J, Zhang J, Ren D, et al. Probing of C-terminal lysine variation in a recombinant monoclonal antibody production using Chinese hamster ovary cells with chemically defined media. *Biotechnol Bioeng*. 2012. DOI: [10.1002/bit.24510](https://doi.org/10.1002/bit.24510). PMID: 22473810.
[^44]: Zhang X, Tang H, Sun YT, et al. Elucidating the effects of arginine and lysine on a monoclonal antibody C-terminal lysine variation in CHO cell cultures. *Appl Microbiol Biotechnol*. 2015. DOI: [10.1007/s00253-015-6617-y](https://doi.org/10.1007/s00253-015-6617-y). PMID: 25947244.
[^45]: Hu Z, Tang D, Misaghi S, et al. Evaluation of heavy chain C-terminal deletions on productivity and product quality of monoclonal antibodies in Chinese hamster ovary (CHO) cells. *Biotechnol Prog*. 2017. DOI: [10.1002/btpr.2444](https://doi.org/10.1002/btpr.2444). PMID: 28188688.
[^46]: Mitchelson FG, Mondia JP, Hughes EH. Effect of copper variation in yeast hydrolysate on C-terminal lysine levels of a monoclonal antibody. *Biotechnol Prog*. 2017. DOI: [10.1002/btpr.2411](https://doi.org/10.1002/btpr.2411). PMID: 27863144.
[^47]: Liu H, Gaza-Bulseco G, Faldu D, et al. Heterogeneity of monoclonal antibodies. *J Pharm Sci*. 2008. DOI: [10.1002/jps.21180](https://doi.org/10.1002/jps.21180). PMID: 17828757.
[^48]: Perkins M, Theiler R, Lunte S, et al. Determination of the origin of charge heterogeneity in a murine monoclonal antibody. *Pharm Res*. 2000. DOI: [10.1023/a:1026461830617](https://doi.org/10.1023/a:1026461830617). PMID: 11087044.
[^49]: Khawli LA, Goswami S, Hutchinson R, et al. Charge variants in IgG1: Isolation, characterization, in vitro binding properties and pharmacokinetics in rats. *MAbs*. 2010. DOI: [10.4161/mabs.2.6.13333](https://doi.org/10.4161/mabs.2.6.13333). PMID: 20818176.
[^50]: Yüce M, Sert F, Torabfam M, et al. Fractionated charge variants of biosimilars: A review of separation methods, structural and functional analysis. *Anal Chim Acta*. 2021. DOI: [10.1016/j.aca.2020.12.064](https://doi.org/10.1016/j.aca.2020.12.064). PMID: 33648647.
[^51]: Yang JM, Ai J, Bao Y, et al. Investigation of the correlation between charge and glycosylation of IgG1 variants by liquid chromatography-mass spectrometry. *Anal Biochem*. 2013. DOI: [10.1016/j.ab.2013.11.020](https://doi.org/10.1016/j.ab.2013.11.020). PMID: 24287081.
[^52]: Kishimoto TK, Viswanathan K, Ganguly T, et al. Contaminated heparin associated with adverse clinical events and activation of the contact system. *N Engl J Med*. 2008. DOI: [10.1056/NEJMoa0803200](https://doi.org/10.1056/NEJMoa0803200). PMID: 18434646.
[^53]: Guerrini M, Beccati D, Shriver Z, et al. Oversulfated chondroitin sulfate is a contaminant in heparin associated with adverse clinical events. *Nat Biotechnol*. 2008. DOI: [10.1038/nbt1407](https://doi.org/10.1038/nbt1407). PMID: 18437154.
[^54]: Li B, Suwan J, Martin JG, et al. Oversulfated chondroitin sulfate interaction with heparin-binding proteins: new insights into adverse reactions from contaminated heparins. *Biochem Pharmacol*. 2009. DOI: [10.1016/j.bcp.2009.04.012](https://doi.org/10.1016/j.bcp.2009.04.012). PMID: 19389385.
[^55]: Hogwood J, Naggi A, Torri G, et al. The effect of increasing the sulfation level of chondroitin sulfate on anticoagulant specific activity and activation of the kinin system. *PLoS One*. 2018. DOI: [10.1371/journal.pone.0193482](https://doi.org/10.1371/journal.pone.0193482). PMID: 29494632.
[^56]: Corbier A, Le Berre N, Rampe D, et al. Oversulfated chondroitin sulfate and OSCS-contaminated heparin cause dose- and route-dependent hemodynamic effects in the rat. *Toxicol Sci*. 2011. DOI: [10.1093/toxsci/kfr072](https://doi.org/10.1093/toxsci/kfr072). PMID: 21436127.
[^57]: Costa AR, Rodrigues ME, Henriques M, et al. Glycosylation: impact, control and improvement during therapeutic protein production. *Crit Rev Biotechnol*. 2013. DOI: [10.3109/07388551.2013.793649](https://doi.org/10.3109/07388551.2013.793649). PMID: 23919242.
[^58]: Hermeling S, Crommelin DJ, Schellekens H, et al. Structure-immunogenicity relationships of therapeutic proteins. *Pharm Res*. 2004. DOI: [10.1023/b:pham.0000029275.41323.a6](https://doi.org/10.1023/b:pham.0000029275.41323.a6). PMID: 15212151.
[^59]: Yehuda S, Padler-Karavani V. Glycosylated Biotherapeutics: Immunological Effects of N-Glycolylneuraminic Acid. *Front Immunol*. 2020. DOI: [10.3389/fimmu.2020.00021](https://doi.org/10.3389/fimmu.2020.00021). PMID: 32038661.
[^60]: Mastrangeli R, Audino MC, Palinsky W, et al. Current views on N-glycolylneuraminic acid in therapeutic recombinant proteins. *Trends Pharmacol Sci*. 2021. DOI: [10.1016/j.tips.2021.08.004](https://doi.org/10.1016/j.tips.2021.08.004). PMID: 34544608.
[^61]: Ghaderi D, Zhang M, Hurtado-Ziola N, et al. Production platforms for biotherapeutic glycoproteins. Occurrence, impact, and challenges of non-human sialylation. *Biotechnol Genet Eng Rev*. 2012. DOI: [10.5661/bger-28-147](https://doi.org/10.5661/bger-28-147). PMID: 22616486.
[^62]: Park EI, Manzella SM, Baenziger JU. Rapid clearance of sialylated glycoproteins by the asialoglycoprotein receptor. *J Biol Chem*. 2002. DOI: [10.1074/jbc.M210612200](https://doi.org/10.1074/jbc.M210612200). PMID: 12464602.
[^63]: Szkudlinski MW, Thotakura NR, Tropea JE, et al. Asparagine-linked oligosaccharide structures determine clearance and organ distribution of pituitary and recombinant thyrotropin. *Endocrinology*. 1995. DOI: [10.1210/endo.136.8.7628367](https://doi.org/10.1210/endo.136.8.7628367). PMID: 7628367.
[^64]: Mahmood I, Green MD. Pharmacokinetic and pharmacodynamic considerations in the development of therapeutic proteins. *Clin Pharmacokinet*. 2005. DOI: [10.2165/00003088-200544040-00001](https://doi.org/10.2165/00003088-200544040-00001). PMID: 15828849.
[^65]: Li D, Clark CC, Myers JC. Basement membrane zone type XV collagen is a disulfide-bonded chondroitin sulfate proteoglycan in human tissues and cultured cells. *J Biol Chem*. 2000. DOI: [10.1074/jbc.M000519200](https://doi.org/10.1074/jbc.M000519200). PMID: 10791950.
[^66]: Jaiswal PK, Aljebali L, Gaumond MH, et al. Biochemical characteristics of the chondrocyte-enriched SNORC protein and its transcriptional regulation by SOX9. *Sci Rep*. 2020. DOI: [10.1038/s41598-020-64640-x](https://doi.org/10.1038/s41598-020-64640-x). PMID: 32385306.
[^67]: Thompson S, Rennie CM, Maddy AH. A re-evaluation of the surface complexity of the intact erythrocyte. *Biochim Biophys Acta*. 1980. DOI: [10.1016/0005-2736(80)90478-2](https://doi.org/10.1016/0005-2736(80)90478-2). PMID: 7407144.
[^68]: Dong X, Tsong Y, Shen M. Statistical considerations in setting product specifications. *J Biopharm Stat*. 2015. DOI: [10.1080/10543406.2014.972511](https://doi.org/10.1080/10543406.2014.972511). PMID: 25358110.
[^69]: Yu L, Tao L, Zhao Y, et al. Analysis of Molecular Heterogeneity in Therapeutic IFNα2b from Different Manufacturers by LC/Q-TOF. *Molecules*. 2020. DOI: [10.3390/molecules25173965](https://doi.org/10.3390/molecules25173965). PMID: 32878126.
[^70]: Rayfield WJ, Kandula S, Khan H, et al. Impact of Freeze/Thaw Process on Drug Substance Storage of Therapeutics. *J Pharm Sci*. 2017. DOI: [10.1016/j.xphs.2017.03.019](https://doi.org/10.1016/j.xphs.2017.03.019). PMID: 28343990.
[^71]: Kolhe P, Badkar A. Protein and solute distribution in drug substance containers during frozen storage and post-thawing: a tool to understand and define freezing-thawing parameters in biotechnology process development. *Biotechnol Prog*. 2011. DOI: [10.1002/btpr.530](https://doi.org/10.1002/btpr.530). PMID: 21302371.
[^72]: Kolhe P, Amend E, Singh SK. Impact of freezing on pH of buffered solutions and consequences for monoclonal antibody aggregation. *Biotechnol Prog*. 2010. DOI: [10.1002/btpr.377](https://doi.org/10.1002/btpr.377). PMID: 20039442.
[^73]: Gandhi S, Ren D, Xiao G, et al. Elucidation of degradants in acidic peak of cation exchange chromatography in an IgG1 monoclonal antibody formed on long-term storage in a liquid formulation. *Pharm Res*. 2011. DOI: [10.1007/s11095-011-0536-0](https://doi.org/10.1007/s11095-011-0536-0). PMID: 21845507.
[^74]: Chiu J, Valente KN, Levy NE, et al. Knockout of a difficult-to-remove CHO host cell protein, lipoprotein lipase, for improved polysorbate stability in monoclonal antibody formulations. *Biotechnol Bioeng*. 2016. DOI: [10.1002/bit.26237](https://doi.org/10.1002/bit.26237). PMID: 27943242.
[^75]: E SY, Hu Y, Molden R, et al. Identification and Quantification of a Problematic Host Cell Protein to Support Therapeutic Protein Development. *J Pharm Sci*. 2022. DOI: [10.1016/j.xphs.2022.10.008](https://doi.org/10.1016/j.xphs.2022.10.008). PMID: 36220394.
[^76]: Weiß L, Schmieder-Todtenhaupt V, Haemmerling F, et al. Multi-lipase gene knockdown in Chinese hamster ovary cells using artificial microRNAs to reduce host cell protein mediated polysorbate degradation. *Biotechnol Bioeng*. 2023. DOI: [10.1002/bit.28563](https://doi.org/10.1002/bit.28563). PMID: 37743807.
[^77]: Zhang S, Xiao H, Goren M, et al. Putative Phospholipase B-Like 2 is Not Responsible for Polysorbate Degradation in Monoclonal Antibody Drug Products. *J Pharm Sci*. 2020. DOI: [10.1016/j.xphs.2020.05.028](https://doi.org/10.1016/j.xphs.2020.05.028). PMID: 32534029.
[^78]: Hada S, Shin IJ, Park HE, et al. In-use stability of Rituximab and IVIG during intravenous infusion: Impact of peristaltic pump, IV bags, flow rate, and plastic syringes. *Int J Pharm*. 2024. DOI: [10.1016/j.ijpharm.2024.124577](https://doi.org/10.1016/j.ijpharm.2024.124577). PMID: 39137820.
[^79]: Morar-Mitrica S, Puri M, Beumer Sassi A, et al. Development of a stable low-dose aglycosylated antibody formulation to minimize protein loss during intravenous administration. *MAbs*. 2015. DOI: [10.1080/19420862.2015.1046664](https://doi.org/10.1080/19420862.2015.1046664). PMID: 26073995.
[^80]: Kim SJ, Kim KW, Shin YK, et al. In-Use Stability of the Rituximab Biosimilar CT-P10 (Truxima) Following Preparation for Intravenous Infusion and Storage. *BioDrugs*. 2019. DOI: [10.1007/s40259-019-00336-7](https://doi.org/10.1007/s40259-019-00336-7). PMID: 30747341.
[^81]: Singh SK, Afonina N, Awwad M, et al. An industry perspective on the monitoring of subvisible particles as a quality attribute for protein therapeutics. *J Pharm Sci*. 2010. DOI: [10.1002/jps.22097](https://doi.org/10.1002/jps.22097). PMID: 20310025.
[^82]: Zölls S, Tantipolphan R, Wiggenhorn M, et al. Particles in therapeutic protein formulations, Part 1: overview of analytical methods. *J Pharm Sci*. 2011. DOI: [10.1002/jps.23001](https://doi.org/10.1002/jps.23001). PMID: 22161573.
[^83]: Narhi LO, Jiang Y, Cao S, et al. A critical review of analytical methods for subvisible and visible particles. *Curr Pharm Biotechnol*. 2009. DOI: [10.2174/138920109788488905](https://doi.org/10.2174/138920109788488905). PMID: 19519412.
[^84]: Patel AR, Lau D, Liu J. Quantification and characterization of micrometer and submicrometer subvisible particles in protein therapeutics by use of a suspended microchannel resonator. *Anal Chem*. 2012. DOI: [10.1021/ac300976g](https://doi.org/10.1021/ac300976g). PMID: 22794526.
[^85]: Krayukhina E, Tsumoto K, Uchiyama S, et al. Effects of syringe material and silicone oil lubrication on the stability of pharmaceutical proteins. *J Pharm Sci*. 2014. DOI: [10.1002/jps.24184](https://doi.org/10.1002/jps.24184). PMID: 25256796.
[^86]: Perez M, Décaudin B, Abou Chahla W, et al. Effectiveness of in-Line Filters to Completely Remove Particulate Contamination During a Pediatric Multidrug Infusion Protocol. *Sci Rep*. 2018. DOI: [10.1038/s41598-018-25602-6](https://doi.org/10.1038/s41598-018-25602-6). PMID: 29769547.
[^87]: Bolden JS, Claerbout ME, Miner MK, et al. Evidence against a bacterial endotoxin masking effect in biologic drug products by limulus amebocyte lysate detection. *PDA J Pharm Sci Technol*. 2014. DOI: [10.5731/pdajpst.2014.00999](https://doi.org/10.5731/pdajpst.2014.00999). PMID: 25336418.
[^88]: Burgmaier L, Pölt S, Avci-Adali M, et al. The impact of LPS mutants on endotoxin masking in different detection systems. *Biologicals*. 2024. DOI: [10.1016/j.biologicals.2024.101808](https://doi.org/10.1016/j.biologicals.2024.101808). PMID: 39586167.
[^89]: Dorival-García N, Carillo S, Ta C, et al. Large-Scale Assessment of Extractables and Leachables in Single-Use Bags for Biomanufacturing. *Anal Chem*. 2018. DOI: [10.1021/acs.analchem.8b01208](https://doi.org/10.1021/acs.analchem.8b01208). PMID: 29943976.
[^90]: Marghitoiu L, Liu J, Lee H, et al. Extractables analysis of single-use flexible plastic biocontainers. *PDA J Pharm Sci Technol*. 2015. DOI: [10.5731/pdajpst.2015.01001](https://doi.org/10.5731/pdajpst.2015.01001). PMID: 25691714.
[^91]: Pahl I, Dorey S, Barbaroux M, et al. Analysis and evaluation of single-use bag extractables for validation in biopharmaceutical applications. *PDA J Pharm Sci Technol*. 2014. DOI: [10.5731/pdajpst.2014.00996](https://doi.org/10.5731/pdajpst.2014.00996). PMID: 25336417.
[^92]: Li K, Rogers G, Nashed-Samuel Y, et al. Creating a Holistic Extractables and Leachables (E&L) Program for Biotechnology Products. *PDA J Pharm Sci Technol*. 2015. DOI: [10.5731/pdajpst.2015.01073](https://doi.org/10.5731/pdajpst.2015.01073). PMID: 26429108.
[^93]: Magarian N, Lee K, Nagpal K, et al. Clearance of extractables and leachables from single-use technologies via ultrafiltration/diafiltration operations. *Biotechnol Prog*. 2016. DOI: [10.1002/btpr.2277](https://doi.org/10.1002/btpr.2277). PMID: 27071939.
[^94]: Hammond M, Nunn H, Rogers G, et al. Identification of a leachable compound detrimental to cell growth in single-use bioprocess containers. *PDA J Pharm Sci Technol*. 2013. DOI: [10.5731/pdajpst.2013.00905](https://doi.org/10.5731/pdajpst.2013.00905). PMID: 23569073.
[^95]: Kelly PS, McSweeney S, Coleman O, et al. Process-relevant concentrations of the leachable bDtBPP impact negatively on CHO cell production characteristics. *Biotechnol Prog*. 2016. DOI: [10.1002/btpr.2345](https://doi.org/10.1002/btpr.2345). PMID: 27557043.
[^96]: Hammond M, Marghitoiu L, Lee H, et al. A cytotoxic leachable compound from single-use bioprocess equipment that causes poor cell growth performance. *Biotechnol Prog*. 2014. DOI: [10.1002/btpr.1869](https://doi.org/10.1002/btpr.1869). PMID: 24497314.
[^97]: Kelly PS, Dorival-García N, Paré S, et al. Improvements in single-use bioreactor film material composition leads to robust and reliable Chinese hamster ovary cell performance. *Biotechnol Prog*. 2019. DOI: [10.1002/btpr.2824](https://doi.org/10.1002/btpr.2824). PMID: 31017345.
[^98]: Mass B, Huber C, Krämer I. Plasticizer extraction of Taxol infusion solution from various infusion devices. *Pharm World Sci*. 1996. DOI: [10.1007/BF00579710](https://doi.org/10.1007/BF00579710). PMID: 8739262.
[^99]: Bandyopadhyay S, Samajdar SS, Das S. Ulinastatin for the treatment of severe acute pancreatitis: a systematic review and meta-analysis. *BMC Gastroenterol*. 2025. DOI: [10.1186/s12876-025-04239-6](https://doi.org/10.1186/s12876-025-04239-6). PMID: 40890662.
[^100]: Horváth IL, Bunduc S, Fehérvári P, et al. The combination of ulinastatin and somatostatin reduces complication rates in acute pancreatitis: a systematic review and meta-analysis of randomized controlled trials. *Sci Rep*. 2022. DOI: [10.1038/s41598-022-22341-7](https://doi.org/10.1038/s41598-022-22341-7). PMID: 36289288.
[^101]: Moggia E, Koti R, Belgaumkar AP, et al. Pharmacological interventions for acute pancreatitis. *Cochrane Database Syst Rev*. 2017. DOI: [10.1002/14651858.CD011384.pub2](https://doi.org/10.1002/14651858.CD011384.pub2). PMID: 28431202.
[^102]: Wang H, Liu B, Tang Y, et al. Improvement of Sepsis Prognosis by Ulinastatin: A Systematic Review and Meta-Analysis of Randomized Controlled Trials. *Front Pharmacol*. 2019. DOI: [10.3389/fphar.2019.01370](https://doi.org/10.3389/fphar.2019.01370). PMID: 31849646.
[^103]: Weilke C, Brinkmann T, Kleesiek K. Determination of xylosyltransferase activity in serum with recombinant human bikunin as acceptor. *Clin Chem*. 1997. **PubMed 未著录 DOI**. PMID: 8990221.
