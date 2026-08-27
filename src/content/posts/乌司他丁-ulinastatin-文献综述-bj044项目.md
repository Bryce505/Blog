---
title: "乌司他丁分子结构与 O-糖胺聚糖链表征方法学综述——BJ044 项目文献导读"
date: 2026-08-27
category: "00基础"
primaryTag: "00基础/文献/综述"
description: "乌司他丁（Ulinastatin，尿胰蛋白酶抑制剂 Urinary Trypsin Inhibitor / UTI，核心蛋白学名 Bikunin）是 BJ044 项目的研究对象。本文基于 Zotero 文献库 文献/项目文献/BJ044 分类下的 13 篇文献（1999–2023"
tags:
  - "00基础/文献/综述"
sourceNotes:
  - "Antibody-Characterization/乌司他丁(Ulinastatin)文献综述-BJ044项目.md"
---

乌司他丁（Ulinastatin，尿胰蛋白酶抑制剂 Urinary Trypsin Inhibitor / UTI，核心蛋白学名 Bikunin）是 BJ044 项目的研究对象。本文基于 Zotero 文献库 `文献/项目文献/BJ044` 分类下的 13 篇文献（1999–2023年）及 PubMed 补充检索资料，按"分子结构—生物合成—功能机制—表征方法学—跨文献共识"的脉络组织；由于文献集的核心主线是乌司他丁 O-糖胺聚糖（GAG）链的精细结构表征方法学，文章对这一部分着墨最多。所有实验数据均直接转录自原文，凡属经其他文献转引、未经独立核实的内容均在文中注明。

> [!abstract] 摘要
> 乌司他丁是一种从人尿液中提取的强酸性糖蛋白药物，由两个 Kunitz 型丝氨酸蛋白酶抑制结构域组成的核心蛋白携带一条 N-连接的双天线复合型糖链（Asn45）和一条 O-连接于 Ser10 的低硫酸化硫酸软骨素（Chondroitin Sulfate, CS）糖胺聚糖（GAG）链。其 O-糖链的结构参数在 1999、2008、2023 三个年代、三种独立质谱方法中得到高度一致的交叉验证，是理解"糖基化为何是关键质量属性"的核心证据。

> [!summary] 核心要点
> - O-糖胺聚糖链结构在 1999、2008、2023 三个年代、三种独立质谱方法（MALDI-MS/凝胶电泳、FTICR-MS、UHPLC-Orbitrap-HRMS）中得到高度一致的交叉验证：链长约 13–19 个二糖重复单元、4–7 个硫酸基团、优势构型为奇数糖基单元（GalNAc封端）。
> - CS 链本身几乎无蛋白酶抑制活性，但共价连接于核心蛋白后能显著增强核心蛋白的丝氨酸蛋白酶抑制活性（Teshigahara et al., 2020）。
> - 刘博等（2023，中国食品药品检定研究院）建立的 UHPLC-Orbitrap-HRMS O-糖胺聚糖表征方法可能是 BJ044 项目方法学的直接参考或先导工作。
> - 软骨素 ABC 裂解酶消化 + 糖肽/寡糖质谱分析，是本文献集中几乎所有结构表征研究共用的方法学骨架。

## 概述：药物定位与项目背景

乌司他丁是从健康成年男性尿液中提取纯化的一种高度糖基化的强酸性糖蛋白药物（等电点 pI≈2.1），学名尿胰蛋白酶抑制剂（Urinary Trypsin Inhibitor, UTI），其核心蛋白部分的标准生物化学名称为 Bikunin。历史上因分离来源、分离方法不同，文献中还出现过 acid-stable trypsin inhibitor (ASTI)、HI-30、mingin、urinastatin、uristatin 等多个别名；1990 年学界为消除混乱统一定名为 "bikunin"（因其含两个 Kunitz 结构域）(Fries & Blom, 2000)。在日本，该药物的原研厂商为持田制药（Mochida Pharmaceutical），商品名 Miraclid (Pugia et al., 2007a)；文献集中刘博等（2023）的研究即以持田制药产品作为国产仿制/一致性评价的参比制剂。

根据 PubMed 补充检索到的综述文献，乌司他丁**已在日本和中国获批用于休克与胰腺炎适应症**，并在全球范围内有多项在研临床试验；超说明书/研究性用途还包括早产抑制、川崎病（Kawasaki disease）辅助治疗、以及血液、肝、肾、心血管系统相关炎症性疾病 (Atal & Atal, 2016 [PubMed补充检索])。日本儿科文献进一步指出其临床适应症核心为"休克和胰腺炎"，川崎病等属超说明书用药，疗效尚待更多确证性研究 (Saji, 2008 [PubMed补充检索，日文原文仅摘要可读])。

BJ044 关联的文献集（13 篇独立文献）几乎全部聚焦于乌司他丁分子结构、尤其是 O-连接糖胺聚糖链的精细结构及其分析表征方法学，隐含地指向一个药品质量控制 / 仿制药一致性评价的研究背景——这与文献集中唯一的中文文献（刘博等，2023，中国食品药品检定研究院）的研究目的完全吻合，该文明确将其方法定位为"为产品的质量一致性评价奠定基础"。本综述以此为核心主线组织全文，同时兼顾分子生物学背景，帮助建立对乌司他丁的整体认知。

## 分子结构：双 Kunitz 核心蛋白与双重糖基化

### 核心蛋白：两个 Kunitz 结构域

Bikunin 核心蛋白由**两个 Kunitz 型丝氨酸蛋白酶抑制结构域**（domain I、domain II，各约 7 kDa，各含 3 对二硫键）串联而成，中间以短连接肽相连，两端各有一段 10–25 个氨基酸的 N/C 端延伸区 (Fries & Blom, 2000)。核心蛋白全长氨基酸数在不同文献中报告略有差异——Teshigahara et al. (2020) 记为 143 个氨基酸残基，Lepedda et al. (2018) 记为 147 个氨基酸残基，本综述如实记录此处文献间的细微出入，未能进一步核实何者为准（可能与信号肽/前体计数方式不同有关）。

1998 年 X 射线晶体学解析了（缺少 N/C 端延伸区的）人 bikunin 三维结构：两个 Kunitz 结构域呈 V 形排列，domain I 一端与 domain II 中部结构相互作用；每个结构域各有一个蛋白酶结合位点，位于 V 形分子的两个顶点（关键结合残基为 Met36、Arg92）；domain II 对较大蛋白酶（大于胰蛋白酶尺寸）的结合会受 domain I 空间位阻影响 (Fries & Blom, 2000，转引 Xu et al., 1998)。

### Asn45 的 N-连接糖基化

Bikunin 在 Asn45 位点携带一条**同质性很高的"复合型"双天线 N-聚糖**：Enghild et al. (1999) 通过连续外切糖苷酶消化 + MALDI-MS 精确测定其组成为 2 个唾液酸 + 2 个半乳糖 + 2 个 N-乙酰氨基葡萄糖构成的核心结构（质量变化路径：7968.3 → 7393.8 [-2唾液酸] → 7057.2 [-2半乳糖] → 6654.2 [-2 GlcNAc] → 5776.0 Da [糖基完全去除]）。与通常认为糖蛋白 N-糖具有较大异质性不同，该研究特别指出 Asn45 糖链"意外地呈现同质性"。

### Ser10 的 O-连接硫酸软骨素链

这是本项目文献集着墨最多、也是理解乌司他丁"关键质量属性"的核心部分。

**连接区结构**：与所有硫酸软骨素/硫酸乙酰肝素类蛋白聚糖一样，GAG 链通过一个四糖连接区 **Xyl-Gal-Gal-GlcA** 连接到核心蛋白 Ser10 的羟基上，随后以硫酸软骨素二糖重复单元（GlcUA-GalNAc）延伸 (Noborn et al., 2015; Chi et al., 2008)。连接区中一个半乳糖残基可发生 4-位硫酸化：Chi et al. (2008) 通过串联质谱（EDD-MS）确认该连接区四糖的确切结构为 **GlcA-Gal(4S)-Gal-Xylol**，与 Yamada et al. (1995，经 Fries & Blom, 2000 及 Chi et al., 2008 转引) 此前基于分离纯化+质谱的结果一致。此外，连接区木糖残基可发生 **2-位磷酸化**（一种在 CS/HS 糖胺聚糖生物合成延伸起始阶段普遍存在、多数会在延伸后脱去、但部分成熟糖链会保留的修饰）(Noborn et al., 2015; Ramarajan et al., 2022)。

**二糖重复单元与硫酸化模式**：CS 链本体由 GlcUA-GalNAc 二糖单元重复构成，仅在 GalNAc 的 C4 位发生硫酸化（未检出 C6 硫酸化），即人乌司他丁 CS 链属于**硫酸软骨素 A 型（CS-A，chondroitin-4-sulfate）**、且总体硫酸化程度较低 (Enghild et al., 1999; Chi et al., 2008)。链末端糖基类型与二糖单元奇偶数相关：奇数个糖基单元时以 GalNAc 封端，偶数时以 GlcA 封端；文献集中三项独立研究（见下文跨文献汇总表）均发现**天然乌司他丁 CS 链以奇数（GalNAc 封端）构型占绝对优势**。

**链长与硫酸化程度的定量数据**：

- Enghild et al. (1999)：MALDI-MS + 凝胶电泳两种独立方法测得链长 15±3 个二糖单元，硫酸化二糖:未硫酸化二糖比例约 1:3，硫酸化基团更集中在还原端附近；阴离子交换色谱（pH 3.4）分离出 4 种硫酸化程度不同的电荷异构体，相邻异构体质量差约 80 Da（对应 1 个硫酸基团）。
- Chi et al. (2008)：ESI-FTICR-MS 首次报道完整（未消化）蛋白聚糖 GAG 组分的质谱图，测得完整 CS 链分子量范围 5505–7102 Da（混合物分析）；结合分离后再分析，确定 CS 链由 **27–39 个单糖**（约合 13–19 个二糖单元）构成，硫酸基团数为 **4–7 个**，中位链长 33 个单糖，>90% 的链落在 27–35 个单糖的较窄区间内；并首次发现非还原末端三糖也可携带硫酸基团（此前文献普遍认为硫酸化仅集中于还原端附近）。
- 刘博等 (2023)：UHPLC-Orbitrap 高分辨质谱（负离子模式，分辨率 140,000）分析国产及日本持田原研乌司他丁制剂，测得 O-糖胺聚糖二糖重复单元数为 **13–17 个**，硫酸基团数 **4–7 个**，最主要糖型为 GalNAc(GlcAGalNAc)₁₃(SO₃)₅GlcAGalGalXylol（约占 20%）；国产制剂与原研制剂在主要（高丰度）糖型上基本一致，但国产制剂在低丰度（<10%）糖型上表现出略宽的分布（硫酸基团数可达 7 个，二糖单元数可达 17 个，均略超过该研究中检出的原研制剂范围）。

**重链交联（IαI/PαI 复合物中）**：约 90–98% 的血浆 bikunin 并非游离存在，而是通过其 CS 链上一个**未硫酸化的 GalNAc 残基**与"重链"（heavy chain, HC1/HC2/HC3）C 端天冬氨酸残基以酯键共价交联，形成 inter-α-inhibitor（IαI，含 HC1+HC2，人血浆中主要形式）或 pre-α-inhibitor（PαI，含 HC3）(Fries & Blom, 2000; Enghild et al., 1999)。Enghild et al. (1999) 进一步用有限软骨素酶消化实验确定了 HC1、HC2 在 CS 链上的**排列顺序**：两条重链均定位于 CS 链靠近非还原端一侧且彼此相邻，其中 HC2 更靠近 bikunin（还原端），HC1 更远离 bikunin；完整排列可表示为：

> [二糖]ₐ-HC1-[二糖]♭-HC2-[二糖]꜀-Gal-Gal-Xyl-Ser10-bikunin（a+b+c = 12–18 个二糖单元）

## 生物合成与体内代谢

Bikunin 由 **AMBP 基因**（α1-microglobulin/bikunin precursor，人基因约 20 kb，10 个外显子、9 个内含子）编码，其翻译产物是一个同时包含信号肽、α1-微球蛋白（α1-microglobulin）和 bikunin 三部分的前体蛋白，主要在肝脏合成（其次是肾、肠、胃、胰腺，表达量较低）(Fries & Blom, 2000; Pugia et al., 2007a)。前体蛋白在高尔基体内完成糖基化（CS 链的合成由木糖基转移酶 XT 起始，将木糖从 UDP-木糖转移至 Ser 残基）与硫酸化后，经蛋白酶原转化酶在分泌囊泡处切割：一部分游离 bikunin 直接以游离形式分泌入血；另一部分在高尔基体内与重链前体共价偶联后再释放 α1-微球蛋白片段，形成成熟的 IαI/PαI 复合物 (Fries & Blom, 2000; Pugia et al., 2007a)。

人及大鼠血浆中 bikunin 总浓度约 4–7 μM，其中仅 2–10% 为游离形式；尿液中 bikunin 浓度约 0.03–0.05 μM（因为循环中的复合型 bikunin 分子量远超肾小球滤过阈值，尿液中检出的主要是游离/降解片段形式）(Fries & Blom, 2000)。游离 bikunin 经**肾小球滤过**清除，滤过速率约为白蛋白的 80 倍（推测与其伸展的分子构象有关——因 CS 链的伸展构象，bikunin 在凝胶过滤中表现得如同约 67 kDa 的球状蛋白，在 SDS-PAGE 中表观分子量则异常地呈现 35–45 kDa）(Fries & Blom, 2000; Pugia et al., 2007a)。游离 bikunin 血浆及尿液半衰期均很短（Pugia et al., 2007a 综述引用的多项研究报告为 4–30 分钟量级）。

需要说明的是，这一"内源性游离 bikunin 清除动力学"数据与 PubMed 补充检索到的一项日本持田制药体内药代动力学研究（Ohzawa et al., 1997 [PubMed补充检索]，家兔关节腔注射给药）报告的**血浆总放射性半衰期 10.8–11.8 小时**并不直接可比——后者是外源性单次给药后的整体药代动力学（且经淋巴系统部分吸收，呈"flip-flop"动力学特征），与内源性游离 bikunin 经肾脏的持续清除速率是两个不同的药代动力学问题，本综述如实并列呈现、不做强行统一。

## 蛋白酶抑制机制与 O-糖链的功能贡献

### 核心蛋白的丝氨酸蛋白酶抑制谱

Bikunin 通过两个 Kunitz 结构域之一与靶蛋白酶结合而发挥抑制作用，可抑制包括胰蛋白酶、糜蛋白酶、激肽释放酶（kallikrein）、纤溶酶（plasmin）、弹性蛋白酶（elastase）、组织蛋白酶 G（cathepsin G）在内的多种丝氨酸蛋白酶，抑制常数 K_i 范围 0.03–3 μM；对凝血因子 IXa、Xa、XIa、XIIa 的抑制则弱得多（K_i 15–800 μM）(Pugia et al., 2007a)。**domain II 单独存在时对因子 Xa 和血浆激肽释放酶的抑制效率分别比完整分子高约 7 倍和 20 倍**——这与晶体结构显示 domain I 对较大蛋白酶结合 domain II 造成空间位阻的观察相吻合 (Fries & Blom, 2000，转引 Morishita et al., 1994)。

### CS 糖链对蛋白酶抑制活性的增强作用

Teshigahara et al. (2020) 通过酶法"重塑"乌司他丁的糖链（将天然低硫酸化 CS 链替换为透明质酸，得到 HA-hybrid UTI；或彻底水解去除糖胺聚糖，仅保留连接区四糖，得到 linkage-UTI），系统比较了天然 UTI、linkage-UTI、HA-hybrid UTI 三者对胰蛋白酶、糜蛋白酶、纤溶酶、胰弹性蛋白酶的抑制活性：

- 三种形式在**高浓度**下最大抑制率相近（胰蛋白酶 86/84/84%，糜蛋白酶 90/88/89%，纤溶酶 89/80/73%），说明抑制活性的"存在与否"主要由核心蛋白决定；
- 但在**低浓度**（如 1.0 μg/mL）下，天然 UTI 的抑制效力明显强于另两者，IC₅₀ 值证实了这一点（胰蛋白酶：天然 UTI 0.406 μg/mL vs. linkage-UTI 1.458 μg/mL vs. HA-UTI 1.543 μg/mL；糜蛋白酶：0.556 vs. 1.586 vs. 1.537；纤溶酶：1.36 vs. 2.72 vs. 3.88）；
- 用蛋白酶（actinase E）切除核心蛋白、仅保留 CS 链+小肽段的样品**完全不表现出蛋白酶抑制活性**。

结论：**天然的、共价连接于核心蛋白的低硫酸化 CS 链本身并无独立的蛋白酶抑制活性，但它能显著增强核心蛋白在低浓度下的抑制效力**，而透明质酸替代链则无此增强效果，提示这是 CS 链结构特异性的贡献，而非单纯糖基化位阻效应 (Teshigahara et al., 2020)。该研究还指出，已知炎症性疾病严重程度会伴随 CS 链变长、硫酸化程度降低（引用 Mizon et al., 2001; Capon et al., 2003，经本文转引未独立核实），因而糖链结构变化可能直接关联到药物的抗炎效力变化。

## 其他生物学功能、临床应用与病理生理关联

### 其他生物学功能

文献报道的 Bikunin/UTI 其他生物学活性主要来自 Fries & Blom (2000) 与 Pugia et al. (2007a) 两篇综述的系统梳理（以下各项均为综述作者对既往原始研究的转引整理，未逐一溯源至最初原始实验论文）：

- **细胞表面纤溶酶抑制/抗肿瘤转移**：Bikunin 可抑制细胞表面结合型纤溶酶的活性，在体内外实验中均显示抑制肿瘤细胞转移的效应（α2-巨球蛋白、α1-蛋白酶抑制剂等其他血浆蛋白酶抑制剂不具备此性质）(Fries & Blom, 2000)。
- **生长因子样活性**：游离 bikunin（截短形式）最早于 1986 年从人肝癌细胞培养上清中作为内皮细胞生长支持因子被分离；完整 bikunin 也被报道可刺激成纤维细胞增殖（最适浓度 10–100 nM）(Fries & Blom, 2000)。
- **细胞内钙离子调节**：Bikunin 可阻断脂多糖（LPS）诱导的中性粒细胞/内皮细胞胞浆游离 Ca²⁺ 升高，并抑制平滑肌收缩（血管平滑肌、子宫平滑肌），提示其可能通过阻断钙通道发挥抗炎/保胎作用；文献特别指出，在日本 bikunin 被用于治疗急性循环功能不全，其作用机制"尚不清楚"(Fries & Blom, 2000)。
- **细胞外基质稳定作用**：IαI/PαI 可支持卵母细胞-颗粒细胞复合体及成纤维细胞、间皮细胞的透明质酸细胞外基质形成，机制涉及重链从 bikunin 上"转移"结合到透明质酸分子上 (Fries & Blom, 2000)。
- **抑制肾结石形成**：体外实验显示 bikunin 可抑制草酸钙结晶形成；肾结石患者尿液 bikunin 水平低于健康对照 (Fries & Blom, 2000)。
- **蛋白酶激活受体（PAR）信号通路调控**：Bikunin 抑制胰蛋白酶/凝血酶对 PAR 的裂解激活，从而抑制其下游细胞增殖、炎症介质释放等信号转导过程；同时也参与调控 NF-κB 通路介导的细胞凋亡（抑制促炎细胞因子 TNF-α/IL-1/IL-18 的释放，防止 EGFR、TLR-4 异常激活）(Pugia et al., 2007a)。

### 已获批适应症与临床转引

乌司他丁**在日本与中国获批用于休克和急性胰腺炎**；其抗炎作用机制被归纳为：抑制多形核白细胞（PMN）来源的弹性蛋白酶、TNF-α 及其他促炎细胞因子/白介素（IL-1、IL-6、IL-8）的释放，并抑制 PMN 细胞、巨噬细胞、血小板的活化 (Atal & Atal, 2016 [PubMed补充检索])。超说明书/研究性用途包括早产抑制、以及血液系统、肝脏、肾脏、心血管系统疾病（含川崎病等血管炎综合征）(Atal & Atal, 2016; Saji, 2008 [均为 PubMed 补充检索])。

本项目文献集中的中文文献（刘博等, 2023）在其引言部分（转引其参考文献，本综述未独立核实原始来源）提及乌司他丁在 COVID-19 诊疗中的可行性研究、WHO 相关诊疗方案中的推荐，以及用于新生儿坏死性小肠结肠炎、联合低分子肝素治疗急性胰腺炎、联合利奈唑胺治疗重症肺炎、心肺转流术中抗纤溶等多项中文临床研究——**这些均为二手转引，本综述未直接阅读上述被转引的原始论文，读者若需引用应查证原文**。

### 作为炎症/疾病生物标志物的临床病理关联

Pugia et al. (2007a) 系统综述了 Bik/UTI 水平升高与多类疾病状态的关联（据该文 Table 1 整理，为该综述对既往多项研究的汇总，本综述未逐一溯源核实每一项具体关联）：

| 类别 | 涉及疾病举例 |
|---|---|
| 急性炎症 | 急性病毒感染、肾结石、先兆子痫、手术创伤、移植排斥、心肌梗死、充血性心衰、胰腺炎、创伤 |
| 肿瘤 | 乳腺癌、结肠癌、食管癌、各型白血病/淋巴瘤、多发性骨髓瘤、卵巢癌、胰腺癌、胃癌 |
| 慢性炎症 | 急性冠脉综合征、克罗恩病、肺气肿、肝炎、炎症性肠病、类风湿关节炎、系统性红斑狼疮 |
| 感染 | 阑尾炎、细菌性脑膜炎、脓毒症、肺炎、上呼吸道感染、尿路感染 |
| 肾脏疾病 | 淀粉样变性、肾小管疾病、肾小球肾炎 |

### 糖尿病中的 UTI 水平与 CS 结构变化

Lepedda et al. (2018) 是文献集中**直接报告原始临床数据**的研究：纳入 39 例 1 型糖尿病（T1DM）、32 例 2 型糖尿病（T2DM）患者及 52 例健康对照，经阴离子交换色谱分离尿液 UTI、软骨素 ABC 裂解酶完全解聚 CS 链后，用 SDS-PAGE 定量 UTI 蛋白核心含量、FACE（荧光辅助糖电泳）分析 CS 链结构、nano-LC-MS/MS 确认蛋白身份（三组样本经质谱鉴定的蛋白均为 AMBP_HUMAN，UniProt P02760）。主要发现：

- UTI 蛋白核心水平：T1DM、T2DM 均显著高于对照（p=0.001, p=0.006），两类糖尿病之间无显著差异（p=0.160）；
- CS 水平（以糖醛酸含量计）：同样在两类糖尿病中均显著升高（p=0.005, p=0.041）；
- **CS 链硫酸化程度**：两类糖尿病患者均显著低于对照（p=0.046, p=0.021），两类糖尿病之间无差异；
- CS 链长度：三组间无显著差异；
- UTI 蛋白核心水平与 CS 水平在各组内均呈强正相关（T1DM r=0.897，T2DM r=0.911，p<0.001）；
- UTI 水平与糖化血红蛋白（HbA1c%）、白蛋白排泄率（AER，肾功能指标）、年龄均**无显著相关性**。

作者据此推测 UTI 水平升高可能先于肾功能损害出现，或与肾功能无直接因果关联，而是反映糖尿病相关的慢性炎症状态，可作为潜在的独立生物标志物 (Lepedda et al., 2018)。

### 免疫学检测方法与糖基化对检测特异性的影响

Pugia et al. (2007b) 报道了针对 UTI 不同形式（uristatin，即缺失 O-糖链的 Bik 片段 vs. 完整 bikunin vs. 前抑制剂 IαI/PαI）开发单克隆抗体的研究：通过 SELDI 质谱表征抗体结合特异性，发现多克隆抗体存在与 Tamm-Horsfall 蛋白（THP）及前抑制剂的显著交叉反应问题，而筛选出的单克隆抗体（Mab A：临床克隆号 421-3G5；Mab B：421-5G8）可用于尿液 UTI 检测且无该交叉反应；最佳截断值为尿 UTI ≥7.8 mg/L 用于区分有/无炎症（C 反应蛋白 CRP≥2.0 mg/L 定义）患者，Mab A 方法对炎症组识别灵敏度达 100%、对对照组特异度 93%。该研究同时指出 uTi 的 N-连接糖链为双天线结构，但确切糖型数目尚不明确，其糖基化模式（岩藻糖基化、唾液酸化程度）可能是潜在的疾病特异性标志物方向，但截至该文发表时尚未被证实。

## O-糖胺聚糖链结构表征方法学

本节汇总项目文献集中所有直接涉及乌司他丁/Bikunin CS 链结构表征"如何做"的方法学要点，按技术路线归类。

### 完整 GAG 链的"自上而下"质谱分析

Chi et al. (2008) 建立了**自上而下（top-down）+ 自下而上（bottom-up）相结合**的测序策略，直接对完整（未消化）GAG 链进行高分辨质谱分析：

- 材料：持田制药（Mochida）乌司他丁制剂（批号 C170），经透析去除辅料后得到蛋白聚糖（PG），非特异性蛋白酶（Actinase E）消化 + 强阴离子交换纯化得到肽聚糖（pG，得率 21%），最后经还原性 β-消除（0.4 M NaOH + 0.3 M NaBH₄，4°C 24小时）释放完整 GAG 混合物；
- 分析：ESI-FTICR-MS（7T Bruker Apex IV QeFTMS）直接进样分析完整 GAG 混合物；因样品多分散性导致信噪比不足，采用四极杆窄质量窗分段采集再拼接的策略提高信噪比；辅以制备型聚丙烯酰胺凝胶电泳分离出 9 个尺寸区段后分别进行 FTICR-MS 分析；
- 该研究**是完整蛋白聚糖 GAG 组分质谱图的首次报道**，实现了对链长、硫酸化度的直接质量测定，而非此前文献依赖的"完整 PG 质量 − 脱糖后核心蛋白质量"间接计算法。

### 软骨素酶消化 + 残余糖肽/寡糖的位点特异性质谱鉴定

这是当前糖蛋白质组学领域分析 CS 修饰蛋白的主流策略，核心步骤高度一致：胰蛋白酶消化蛋白 → 富集 GAG 修饰肽段（强阴离子交换色谱 SAX，或 10 kDa 超滤截留分子量富集） → 软骨素 ABC 裂解酶消化，将长 CS 链裁剪为固定的**残余六糖结构**（连接区四糖 + 1 个不饱和二糖，末端带 Δ4,5 不饱和糖醛酸） → nanoLC-MS/MS（HCD 和/或 EThcD 碎裂）鉴定糖肽序列与糖基化位点。

- **Noborn et al. (2015)** 首次系统建立该策略并应用于人尿液、脑脊液样本，鉴定出 13 个新的 CS 修饰蛋白聚糖（含 5 个此前被归类为"激素原"的分泌颗粒蛋白：嗜铬粒蛋白 A、胆囊收缩素、神经肽 W、分泌颗粒蛋白-1/-3），并用表面等离子共振证实软骨素-硫酸链可促进嗜铬粒蛋白 A 在酸性环境下的自聚集——提示 CS 修饰可能参与内分泌颗粒的组装机制。该研究以药用级 bikunin（持田制药提供）作为方法建立的模式蛋白：鉴定出连接区糖肽母离子 m/z 1094.43（3+），碎裂谱显示特征性寡糖氧鎓离子 m/z 362.11（[GlcAGalNAc-H₂O+H]⁺）及木糖位点的磷酸化（区别于硫酸化，质量差 79.968 Da vs. 79.957/79.966 Da 需精细质谱分辨）。
- **Ramarajan et al. (2022)** 沿用并拓展该策略（采用 stepped HCD + EThcD 碎裂），对血浆、尿液、皮肤成纤维细胞样本进行更大规模分析，鉴定出 25 个 CS 蛋白聚糖（含 3 个全新发现）；确认 **bikunin 是血浆中最主要的 CSPG**（该研究中鉴定出 10 个 bikunin 相关糖肽，糖基化位点对应于 AMBP 前体 Ser215，即成熟 bikunin 编号的 Ser10），并观察到木糖磷酸化糖型广泛存在于 bikunin 及其他多种 CSPG 中。
- **Cavallero et al. (2022)** 将该策略的检测手段由传统反相液相色谱-质谱（RP-LC-MS）升级为 **nanoHILIC-MS**，专门用于解决糖基化异质性导致的糖肽与非糖基化肽段共洗脱、离子化抑制问题（见下文 UTI-Fc 节）。

### 化学法释放 + UHPLC-Orbitrap-HRMS 定量一致性评价

刘博等（2023，中国食品药品检定研究院化学药品质量研究与评价重点实验室）的研究直接面向**成品质量一致性评价**，技术路线为：

1. **糖链释放**：利用还原条件下的 β-消除反应从丝氨酸侧链释放完整 O-糖胺聚糖。因乌司他丁本身是强酸性蛋白，直接与硼氢化钠接触会发生酸碱中和反应使还原剂失活——该研究通过**将硼氢化钠与氢氧化钠预混后再加入乌司他丁样品**这一实验条件优化解决了此问题（22.698 mg NaBH₄ + 900 μL 2 mol/L NaOH，再加乌司他丁样品室温过夜反应）；
2. **蛋白残基去除**：冰乙酸酸化中和后经超滤，再以高浓度硫酸铵沉淀残余蛋白核心（因蛋白质谱响应远高于糖胺聚糖，若不去除会严重干扰糖链信号）；
3. **色谱-质谱条件**：TSKgel G2000SWXL 尺寸排阻柱、0.1 mol/L 乙酸铵等度洗脱；四极杆静电场轨道阱高分辨质谱（Q Exactive），**负离子模式**（正离子模式易出现 Na⁺/H⁺加合导致的多电荷峰不均一问题），分辨率 140,000，扫描范围 m/z 200–1500；
4. **数据处理**：BiopharmaFinder 软件对原始谱图去卷积得到精确分子量，依据奇偶数糖基单元分别建立理论分子量计算公式进行糖型归属，并以各糖型质谱响应强度的相对比例作为批间/厂间一致性评价指标；
5. **样品设计**：3 批国产原料药（乌司他丁溶液）+ 3 批国产制剂（乌司他丁注射液），对照 1 批日本持田制药原研注射液；
6. **结论**：国产与原研产品在主要（高丰度）O-糖胺聚糖糖型上基本一致，但国产产品在低丰度糖型上呈现略宽的分布范围。作者将该方法定位为"不仅能够实现对于乌司他丁产品中 O 糖修饰的质量评价，也能够对其他糖蛋白类药物的 O 糖修饰表征与分析起到示范性作用"。

### 重组融合蛋白 UTI-Fc：糖基化全面表征

鉴于游离乌司他丁体内半衰期极短，生物制药工程界开发了 **UTI-Fc 融合蛋白**——将乌司他丁通过 GGGGS 短肽连接子与人 IgG1 Fc 段偶联形成同源二聚体，以延长血清半衰期 (Cavallero et al., 2022)。武田制药（Takeda）资助的 Cavallero et al. (2022) 研究采用 **nanoHILIC-MS**（相较传统反相 nanoLC-MS）对该融合蛋白的复杂糖基化进行了迄今最全面的位点特异性表征，核心发现：

- **UTI 结构域**：Ser-10 位点检出 CS 连接区糖肽（含截短变体，提示 CS 链生物合成不完全）；Thr-17 位点检出单/双唾液酸化的 core-1 型 O-聚糖（粘蛋白型），且**首次以高置信度鉴定出 Ser-10 与 Thr-17 同时被糖基化修饰的双糖基化肽段**（此前基于反相方法的研究未能可靠鉴定这类共修饰形式）；
- **Fc 结构域的新型 O-糖基化**：在人 IgG Fc 结构域两个位点（肽段 152–177 与 274–284）鉴定出唾液酸化 core-1 型 O-聚糖——这是该研究首次报道的 Fc 域 O-糖基化位点，此前 Fc 域研究通常仅关注 Asn297 位点的 N-聚糖；
- **连接肽 O-木糖基化**：GGGGS 连接肽的 Ser-145 位点检出多种截短型 CS 连接糖变体，提示连接肽的木糖基化延伸同样不完全，这一现象在其他 (G4S)ₙ 连接肽融合蛋白文献中也有报道（该研究转引，本综述未独立核实原始文献）；
- **方法学结论**：nanoHILIC 相较传统反相 LC-MS，能更好地按糖型（而非仅按肽骨架）在时间维度分离糖肽，从而避免与非糖基化肽段共洗脱造成的离子化抑制，显著提高了低丰度糖型的鉴定置信度，尤其对连接肽及 Fc 域这类"意料之外"的糖基化位点更为关键。

### 背景方法学：糖胺聚糖降解酶工具箱

本项目文献集中还包含两篇不直接研究乌司他丁本身、但为理解上述结构表征方法所依赖的"酶工具"提供背景知识的综述文献：Wang et al. (2016) 及被其大量引用的 Stern & Jedrzejas (2006)（后者本综述仅依据 Wang et al. 2016 的转引与摘要信息进行概述，未逐字精读全文，如读者对透明质酸酶的详细基因组学/晶体结构感兴趣，建议直接查阅该文献原文）。

- **降解机制两大类**：水解酶（hydrolase，水分子参与，标准糖苷酶机制）与裂解酶（lyase，β-消除反应，产物末端形成 C4-C5 不饱和键）。GAG 降解酶按此机制分属糖苷水解酶（GH）家族与多糖裂解酶（PL）家族。
- **透明质酸酶（HAase）**：人基因组含 6 个同源基因（HYAL1–4、PH20、假基因 HYAL-Phyal1），多数为酸性最适 pH，PH20 为中性最适 pH；多数人源 HAase 同时具有一定程度的 CS 降解活性（HYAL-1 甚至被发现降解 CS-A 比降解 HA 更快，而 HYAL-4 则被认为是"名不副实"——完全没有 HA 降解活性、专一降解 CS）(Wang et al., 2016，转引 Yamada, 2015)。
- **软骨素酶（CSase）**：动物体内尚未发现专一降解 CS/DS 的独立酶家族（均归入上述 HAase 家族）；细菌来源的 CSase 分三类——**CSase ABC**（来自变形杆菌 *Proteus vulgaris*，是本文献集几乎所有结构研究实际使用的工具酶，商品化产品其实是内切型 ABC-I 与外切型 ABC-II 的混合物）、**CSase AC**（对 GlcUA 的 C5 差向异构化敏感，仅作用于 CS/HA 而非 DS）、**CSase B**（仅特异降解 DS）。
- 该综述特别提出"HAase"与"CSase"命名存在混淆问题——因二者底物特异性大量重叠，作者建议按识别的糖苷键类型或具体底物特异性命名，而非沿用历史上按最初发现底物命名的传统术语。

## 跨文献交叉验证、共识与文献空白

### 跨文献共识

**CS 链结构参数：三代独立方法的高度收敛**

| 研究 | 年份 | 分析方法 | 链长（二糖单元/单糖数） | 硫酸基团数 | 优势末端构型 |
|---|---|---|---|---|---|
| Enghild et al. | 1999 | MALDI-MS + 凝胶电泳（双法互证） | 15±3 个二糖单元 | 平均每4个二糖1个（比例1:3） | 未明确报告奇偶优势 |
| Chi et al. | 2008 | ESI-FTICR-MS（top-down） | 27–39 个单糖（≈13–19个二糖） | 4–7个（六/七硫酸化为主） | 奇数（GalNAc封端）占绝对优势 |
| 刘博等 | 2023 | UHPLC-Orbitrap-HRMS | 13–17 个二糖单元 | 4–7个 | 奇数占绝对优势（国产、原研均如此） |

三项研究跨越 1999–2023 年、使用三种完全独立的高分辨质谱平台（飞行时间 MALDI、傅里叶变换离子回旋共振、四极杆轨道阱），样品来源也不同（前两者均直接或间接来自持田制药原料，后者另含中国国产制剂），但对 CS 链链长（约 13–19 个二糖重复单元）、硫酸化程度（4–7 个硫酸基团）、末端构型（奇数糖基单元/GalNAc 封端占优势）三项核心结构参数得出了**高度一致**的结论。这种跨方法、跨年代的收敛为"乌司他丁 CS 链具有相对确定、可重复表征的结构分布区间"这一结论提供了较强证据支持，也说明了为何该结构区间可以被用作产品放行/一致性评价的定量指标。

**连接区硫酸化位置的收敛**：Fries & Blom (2000，转引 Yamada et al., 1995) 与 Chi et al. (2008，独立 EDD 串联质谱验证) 两代研究均将连接区硫酸化位点定位于**紧邻 GlcA 的 Gal 残基（C4位）**，即连接区结构为 GlcA-Gal(4S)-Gal-Xylol，两者结论一致，无矛盾。

**软骨素 ABC 裂解酶是共同方法学基石**：除刘博等（2023）采用纯化学法（β-消除）外，Enghild et al. (1999)、Noborn et al. (2015)、Cavallero et al. (2022)、Ramarajan et al. (2022) 等几乎所有基于酶解的结构/糖肽研究均以**软骨素 ABC 裂解酶**作为核心工具酶。CSase ABC 之所以成为行业标准工具，是因为它同时具有内切（ABC-I）和外切（ABC-II）活性，能将 CS/DS/HA 不论硫酸化/差向异构化模式如何都降解至二糖水平，通用性最强。

**特征性寡糖氧鎓离子作为质谱鉴定的通用"指纹"**：Noborn et al. (2015) 与 Ramarajan et al. (2022) 两项独立研究均将 **m/z 362.11**（对应 [GlcA-GalNAc-H₂O+H]⁺，软骨素ABC裂解酶消化产生的特征不饱和二糖氧鎓离子）列为鉴定 CS 修饰糖肽最关键的诊断性碎片离子，二者互为独立验证。

### 文献空白与不确定之处

以下列出现有 13 篇文献未能完全回答或存在潜在矛盾/局限的问题，供读者判断是否需要进一步检索或作为项目研究方向参考：

1. **核心蛋白氨基酸残基数的文献表述不一致**：Teshigahara et al. (2020) 记为 143 个残基，Lepedda et al. (2018) 记为 147 个残基，本综述未能从现有 13 篇文献中找到解释此差异的直接依据（可能涉及信号肽/前体编号方式差异，需查阅原始基因/蛋白序列数据库如 UniProt P02760 予以澄清）。
2. **CS 链硫酸化的功能构效关系尚未在分子层面阐明**：Teshigahara et al. (2020) 证明了"完整糖链能增强活性"，但未进一步区分是何种具体的硫酸化模式/位点/链长在起作用；该文作者本人也在文中提出"研究不同硫酸化模式糖链变体对蛋白酶抑制的影响"是有价值的未来方向，目前本文献集中未见后续研究覆盖此问题。
3. **UTI-Fc 融合蛋白的临床/药代动力学数据尚未见于本文献集**：Cavallero et al. (2022) 仅涉及体外糖基化结构表征，未见该融合蛋白半衰期延长效果的体内药代动力学数据或临床进展信息，武田制药是否已推进该项目的临床开发阶段，本综述现有资料无法确认。
4. **国产乌司他丁与原研产品低丰度糖型差异的临床/质量意义未被讨论**：刘博等（2023）报告了国产制剂在低丰度糖型分布上略宽于原研的现象，但文中未讨论这种差异是否具有临床相关性或是否在药典/注册标准可接受范围内，这是从"科学发现"到"质量决策"之间留下的实际空白，可能是 BJ044 项目后续需要回答的问题。
5. **乌司他丁临床适应症的循证证据强度未经本综述系统评估**：前文列出的多项超说明书临床应用（COVID-19、新生儿坏死性小肠结肠炎等）均为中文文献二手转引，本综述未获取、未阅读、也未验证这些被转引的原始研究，其证据等级、样本量、是否为随机对照试验等均未知，不应视为已确证的临床结论。
6. **补充检索中排除的 2 篇撤稿文献**：PubMed 补充检索发现 2 篇涉及乌司他丁药理机制的文献已被标记为"Retracted Publication"（撤稿声明）——Xing et al. (2021)《Ulinastatin 通过抑制 ERK 通路影响乳腺癌细胞增殖凋亡》（BioMed Research International）与 Saitoh et al. (1999)《乌司他丁对维库溴铵神经肌肉阻滞的影响》（Anesthesia & Analgesia）。本综述未采用二者的任何结论，特此说明以提示读者在自行检索乌司他丁相关文献时注意甄别撤稿状态。

本综述所有实验数据、数值、结构式均来自对应文献原文的直接转录，未做任何推测性填补；凡属"经某文献转引、本综述未独立核实原始来源"的内容均在正文中明确标注，请勿将其等同于本综述已独立验证的一手事实。

## 参考文献

### 本地 Zotero 文献库（`文献/项目文献/BJ044`，13 篇）

1. 刘博, 黄露, 王悦, 许蓉蓉, 范慧红. (2023). 基于液相高分辨质谱联用技术的乌司他丁糖蛋白中O-糖胺聚糖的结构鉴定与评价研究. *中国药学杂志*, 58(18), 1636–1640. DOI: [10.11669/cpj.2023.18.002](https://doi.org/10.11669/cpj.2023.18.002)（中国食品药品检定研究院，国家药品监督管理局化学药品质量研究与评价重点实验室）
2. Cavallero, G. J., Wang, Y., Nwosu, C., Gu, S., Meiyappan, M., & Zaia, J. (2022). O-Glycoproteomic analysis of engineered heavily glycosylated fusion proteins using nanoHILIC-MS. *Analytical and Bioanalytical Chemistry*, 414(27), 7855–7863. DOI: [10.1007/s00216-022-04318-7](https://doi.org/10.1007/s00216-022-04318-7)
3. Fries, E., & Blom, A. M. (2000). Bikunin — not just a plasma proteinase inhibitor. *The International Journal of Biochemistry & Cell Biology*, 32(2), 125–137. DOI: [10.1016/S1357-2725(99)00125-9](https://doi.org/10.1016/S1357-2725(99)00125-9)
4. Pugia, M. J., Valdes, R., & Jortani, S. A. (2007a). Bikunin (Urinary Trypsin Inhibitor): Structure, Biological Relevance, And Measurement. *Advances in Clinical Chemistry*, 44, 223–245. DOI: [10.1016/S0065-2423(07)44007-0](https://doi.org/10.1016/S0065-2423(07)44007-0)
5. Enghild, J. J., Thøgersen, I. B., Cheng, F., Fransson, L.-Å., Roepstorff, P., & Rahbek-Nielsen, H. (1999). Organization of the Inter-α-Inhibitor Heavy Chains on the Chondroitin Sulfate Originating from Ser10 of Bikunin: Posttranslational Modification of IαI-Derived Bikunin. *Biochemistry*, 38(36), 11804–11813. DOI: [10.1021/bi9908540](https://doi.org/10.1021/bi9908540)
6. Chi, L., Wolff, J. J., Laremore, T. N., Restaino, O. F., Xie, J., Schiraldi, C., Toida, T., Amster, I. J., & Linhardt, R. J. (2008). Structural Analysis of Bikunin Glycosaminoglycan. *Journal of the American Chemical Society*, 130(8), 2617–2625. DOI: [10.1021/ja0778500](https://doi.org/10.1021/ja0778500)
7. Teshigahara, Y., Kakizaki, I., Hirao, W., Tanaka, K., & Takahashi, R. (2020). A Chondroitin Sulfate Chain of Urinary Trypsin Inhibitor Enhances Protease Inhibitory Activity of the Core Protein. *Journal of Applied Glycoscience*, 67(2), 63–66. DOI: [10.5458/jag.jag.JAG-2019_0021](https://doi.org/10.5458/jag.jag.JAG-2019_0021)
8. Lepedda, A. J., Nieddu, G., Rocchiccioli, S., Ucciferri, N., Idini, M., De Muro, P., & Formato, M. (2018). Levels of Urinary Trypsin Inhibitor and Structure of Its Chondroitin Sulphate Moiety in Type 1 and Type 2 Diabetes. *Journal of Diabetes Research*, 2018, 1–9. DOI: [10.1155/2018/9378515](https://doi.org/10.1155/2018/9378515)
9. Pugia, M. J., Jortani, S. A., Basu, M., Sommer, R., Kuo, H.-H., Murphy, S., Williamson, D., Vranish, J., Boyle, P. J., Budzinski, D., Valdes, R., & Basu, S. C. (2007b). Immunological evaluation of urinary trypsin inhibitors in blood and urine: Role of N- & O-linked glycoproteins. *Glycoconjugate Journal*, 24(1), 5–15. DOI: [10.1007/s10719-006-9009-9](https://doi.org/10.1007/s10719-006-9009-9)
10. Wang, W., Wang, J., & Li, F. (2016). Hyaluronidase and Chondroitinase. In M. Z. Atassi (Ed.), *Protein Reviews* (Vol. 925, pp. 75–87). Springer Singapore. DOI: [10.1007/5584_2016_54](https://doi.org/10.1007/5584_2016_54)
11. Ramarajan, M. G., Saraswat, M., Budhraja, R., Garapati, K., Raymond, K., & Pandey, A. (2022). Mass spectrometric analysis of chondroitin sulfate-linked peptides. *Journal of Proteins and Proteomics*, 13(4), 187–203. DOI: [10.1007/s42485-022-00092-3](https://doi.org/10.1007/s42485-022-00092-3)
12. Noborn, F., Gomez Toledo, A., Sihlbom, C., Lengqvist, J., Fries, E., Kjellén, L., Nilsson, J., & Larson, G. (2015). Identification of Chondroitin Sulfate Linkage Region Glycopeptides Reveals Prohormones as a Novel Class of Proteoglycans. *Molecular & Cellular Proteomics*, 14(1), 41–49. DOI: [10.1074/mcp.M114.043703](https://doi.org/10.1074/mcp.M114.043703)
13. Stern, R., & Jedrzejas, M. J. (2006). Hyaluronidases: Their Genomics, Structures, and Mechanisms of Action. *Chemical Reviews*, 106(3), 818–839. DOI: [10.1021/cr050247k](https://doi.org/10.1021/cr050247k)（本综述仅据摘要及 Wang et al., 2016 的转引概述，未逐字精读全文）

### PubMed 补充检索文献（不在本地 Zotero 库中）

- S1. Atal, S. S., & Atal, S. (2016). Ulinastatin - a newer potential therapeutic option for multiple organ dysfunction syndrome. *Journal of Basic and Clinical Physiology and Pharmacology*, 27(2), 91–99. DOI: [10.1515/jbcpp-2015-0003](https://doi.org/10.1515/jbcpp-2015-0003) · PMID: 26565549
- S2. Ohzawa, N., Takahashi, Y., Ogihara, T., Nakai, Y., & Ishiguro, J. (1997). Metabolic fate of ulinastatin (2); Pharmacokinetics in rabbits following intra-articular administration. *Biological & Pharmaceutical Bulletin*, 20(7), 732–738. DOI: [10.1248/bpb.20.732](https://doi.org/10.1248/bpb.20.732) · PMID: 9255410
- S3. Saji, T. (2008). [Clinical utility of ulinastatin, urinary protease inhibitor in acute Kawasaki disease]. *Nihon Rinsho (Japanese Journal of Clinical Medicine)*, 66(2), 343–348. PMID: 18265458（日文原文，仅英文摘要可读，无 DOI）
- S4. Guo, Q., Gao, X., Ren, J., et al. (2025). Inhibition of ferroptosis by serine protease inhibitor attenuates acute respiratory distress syndrome. *Archives of Biochemistry and Biophysics*, 773, 110596. DOI: [10.1016/j.abb.2025.110596](https://doi.org/10.1016/j.abb.2025.110596) · PMID: 40849045
- S5. Liu, Z., Zhu, X., Xu, C., et al. (2022). Ulinastatin ameliorates the malignant progression of prostate cancer cells by blocking the RhoA/ROCK/NLRP3 pathway. *Drug Development Research*, 84(1), 36–44. DOI: [10.1002/ddr.22010](https://doi.org/10.1002/ddr.22010) · PMID: 36461611
- S6. Jiang, L., Yang, L., Zhang, M., et al. (2013). Beneficial effects of ulinastatin on gut barrier function in sepsis. *The Indian Journal of Medical Research*, 138(6), 904–911. PMID: 24521634

**已排除的撤稿文献**（不采用其结论，仅记录以供甄别）：Xing et al. (2021) *BioMed Research International*, DOI: 10.1155/2021/9999268（已撤稿）；Saitoh et al. (1999) *Anesthesia & Analgesia*, DOI: 10.1097/00000539-199912000-00048（已撤稿）。