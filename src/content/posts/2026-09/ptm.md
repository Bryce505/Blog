---
title: "蛋白翻译后修饰（PTM）全景：酶促修饰与化学修饰的位点、基序与质量属性影响"
date: 2026-09-01
category: "02分子表征"
primaryTag: "02分子表征/PTM/氧化"
description: "蛋白质翻译后修饰（PTM）是治疗性蛋白异质性的重要来源，直接影响蛋白的物理稳定性与生物学活性。本文按酶促修饰与化学修饰两大类，系统梳理常见 PTM 的修饰位点、易感基序（liable motif）、Δmass、形成条件及其对抗体质量属性的影响，并附常用修饰数据库与预测工具入口。"
tags:
  - "02分子表征/PTM/氧化"
sourceNotes:
  - "Antibody-Characterization/PTM.md"
---

蛋白质翻译后修饰（PTM）是治疗性蛋白异质性的重要来源，直接影响蛋白的物理稳定性与生物学活性。本文按酶促修饰与化学修饰两大类，系统梳理常见 PTM 的修饰位点、易感基序（liable motif）、Δmass、形成条件及其对抗体质量属性的影响，并附常用修饰数据库与预测工具入口。

> [!abstract] 摘要
> 本笔记系统梳理了蛋白翻译后修饰(PTM)的全景知识，分为酶促修饰（磷酸化、乙酰化、泛素化、SUMO化、甲基化、糖基化、棕榈酰化、肉豆蔻酰化、法尼基化、香叶基化、硫酸化、羟基化、C端赖氨酸丢失、Gly-loss+Amide、Met-loss）与化学修饰（氧化、脱酰胺、异构化、糖化、焦谷氨酸环化、氨甲酰化）两大类，逐项记录常见修饰位点、基序（motif）、Δmass及对抗体理化性质/生物学功能的影响，并附大量参考文献。

> [!summary] 核心要点
> - 酶促修饰约15种：磷酸化、乙酰化、泛素化、SUMO化、甲基化、糖基化、棕榈酰化、肉豆蔻酰化、法尼基化、香叶基化、硫酸化、羟基化、C端赖氨酸丢失（Carboxypeptidase D介导）、Gly-loss+Amide、Met-loss
> - 化学修饰约7种：氧化（Trp/Met/His）、脱酰胺（Asn）、异构化（Asp）、糖化（Glycation）、焦谷氨酸化（Pyro-Glu from E/Q）、氨甲酰化（Carbamylation）
> - 每种修饰均标注常见位点、易感基序（liable motif）、Δmass及对蛋白稳定性/结合活性的影响

## PTM 对蛋白质量属性的影响与数据库资源

PTM 对蛋白的影响主要体现在两方面：产生 heterogeneity；影响 physical stability 与 biological activity。

常用修饰数据库与工具包括：

- [Mascot database search: Modifications (washington.edu)](https://proteomicsresource.washington.edu/mascot/help/pt_mods_help.html)
- [RESID Database [PIR - Protein Information Resource]](https://proteininformationresource.org/resid/resid.shtml)
- Unimod

![1](/images/ptm/202204022129330.webp)

![](/images/ptm/202204022248100.webp)

## 酶促修饰

酶促修饰约 15 种，以下按修饰性质分组介绍，标注常见位点、基团来源、Δmass、关键酶与功能影响。

### 磷酸化与乙酰化

**磷酸化**（Phosphorylation）：常见位点为 Ser、Thr、Tyr 与 His 残基，真核与原核生物蛋白均可发生；磷酸基来源于 ATP；Δmass 为 80 Da；参与复制、转录、环境应激响应、细胞运动、细胞代谢、凋亡及免疫应答等细胞过程。

**乙酰化**（Acetylation）：常见位点为赖氨酸侧链 ε-氨基，一般为 Nε-乙酰化；由赖氨酸乙酰转移酶（KAT）与组蛋白乙酰转移酶（HAT）催化，乙酰基来源于 acetyl CoA；Δmass 为 42.0367；参与染色质稳定性、蛋白-蛋白相互作用、细胞周期调控、细胞代谢、核转运与肌动蛋白成核等过程。

### 泛素化与SUMO化

**泛素化**（Ubiquitylation）：位点为赖氨酸，活化泛素蛋白（76 个氨基酸）的 C 端与底物赖氨酸 Nε 之间形成共价键；经 ubiquitin–proteasome 通路，由泛素活化酶（E1）、泛素结合酶（E2）与泛素连接酶（E3）催化；参与增殖、转录调控、DNA 修复、复制、胞内运输、病毒出芽、信号转导控制、蛋白降解、固有免疫信号、自噬与凋亡等细胞活动。

**SUMO 化**（SUMOylation）：位点为赖氨酸 ε-氨基；由 4 种酶参与，即活化酶（E1）、结合酶（E2）、连接酶（E3）与 SUMO；共有基序为 WKxE（W 代表 Lys、Ile、Val 或 Phe，X 为任意氨基酸）；参与转录控制、染色质组织、细胞内大分子积聚、基因表达调控与信号转导等基本细胞过程。

### 甲基化

**甲基化**（Methylation）：主要发生于细胞核中的核蛋白；常见位点为赖氨酸与精氨酸，一般为 Nε-赖氨酸甲基化；甲基来源于 S-腺苷甲硫氨酸，由 methyltransferase 催化；Δmass 为 14.0266；功能涉及从转录调控到经由异染色质组装的表观遗传沉默等多个生物学过程的精细调节。

### 糖基化

**糖基化**（Glycosylation）：常见位点为 Ser、Thr、Asn 与 Trp 残基；由 glycosyltransferase 催化；分为 N-糖基化、O-糖基化、C-糖基化、S-糖基化、磷酸糖基化与 GPI 锚定（glypiation）等类型；参与细胞黏附、细胞间与细胞-基质相互作用、分子运输、受体激活、蛋白溶解度调节、蛋白折叠与信号转导、蛋白降解以及胞内运输和分泌等过程。

### 脂质修饰（棕榈酰化、肉豆蔻酰化、法尼基化与香叶基化）

**棕榈酰化**（Palmitoylation）：常见位点为 Cys、Gly、Ser、Thr 与 Lys；由棕榈酰转移酶（PATs）催化，棕榈酸来源于 palmitate-Palmitoyl-CoA（16 碳脂肪酸链）；Δmass 为 238.4088；参与蛋白功能调控、蛋白-蛋白相互作用、膜-蛋白结合、神经元发育、信号转导、凋亡与有丝分裂等过程。

**肉豆蔻酰化**（Myristoylation）：主要发生在胞质真核蛋白；肉豆蔻酸连接至 N 端甘氨酸残基；由 N-肉豆蔻酰转移酶（NMT）催化，识别基序为 Met-Gly-X-X-X-Ser/Thr；Δmass 为 210.3556；参与调节细胞结构，以及稳定蛋白结构成熟、信号传递、细胞外通讯、代谢与酶催化活性调控等过程。

**法尼基化**（Farnesylation）：常见位点为半胱氨酸；法尼基来源于法尼基焦磷酸（15 碳）；识别基序为 CAAX（C 为半胱氨酸，A 为脂肪族氨基酸，X 为任意氨基酸）；由法尼基转移酶（FT）催化；Δmass 为 204.3511；参与蛋白-蛋白相互作用、内吞调控、细胞生长、分化、增殖与蛋白运输等过程。

**香叶基化**（Geranylation）：常见位点为半胱氨酸；香叶基香叶基来源于香叶基香叶基焦磷酸（20 碳）；识别基序为 CAAX；由香叶基转移酶催化；功能与法尼基化相同，参与蛋白-蛋白相互作用、内吞调控、细胞生长、分化、增殖与蛋白运输等过程。

### 酪氨酸硫酸化与羟基化

**酪氨酸硫酸化**（Sulfation）[^15][^16][^17][^18]：常见位点为酪氨酸；基序特点是 Y 两侧有酸性氨基酸，且位于 CDR 区[^19]；由酪氨酸蛋白磺基转移酶 1 和 2（TPST1 与 TPST2）催化，硫酸基来源于 3-磷酸腺苷-5-磷酸硫酸；Δmass 为 80.0632；参与蛋白-蛋白相互作用、白细胞在内皮细胞上的滚动、视觉功能及病毒进入细胞等过程；预测工具为 Sulfinator。

**羟基化**（Hydroxylation）：最常见位点为 Pro 与 Lys，其次为 Arg、Tyr、Trp 与 Phe；由 hydroxylase 催化；胶原中的识别基序为 Xaa-Lys-Gly 或 Xaa-Pro-Gly。

### C端与N端加工（赖氨酸丢失、Gly-loss+Amide与Met-loss）

**C 端赖氨酸丢失**（Loss of Lysine）[^21][^22][^24]：抗体重链 C 端赖氨酸的切除在 CHO 细胞中仅由 carboxypeptidase D 介导[^26]。Carboxypeptidase 按活性中心分为 metallocarboxypeptidase（活性中心为 Zn 离子）、serine carboxypeptidase（活性中心为 Ser）与 cysteine carboxypeptidase（活性中心为 Cys）三类；按底物偏好分为 A 型（偏好芳香族或脂肪族氨基酸）与 B 型（偏好带正电氨基酸）。Carboxypeptidase D 涵盖丝氨酸羧肽酶与金属羧肽酶两类，文献报道的 Carboxypeptidase D 均为 metallocarboxypeptidase。由于 Carboxypeptidase D 是锌结合酶，培养基中 Zn 浓度波动可影响酶活性，进而导致 C 端赖氨酸水平变化：培养基中 Cu 离子浓度升高，C 端赖氨酸比例增加；Zn 离子浓度升高，C 端赖氨酸比例减小。

![](/images/ptm/20221001145954.webp)

**Gly-loss + Amide**：酶促甘氨酸切除后留下酰胺化的 C 端。

![](/images/ptm/20221001145954.webp)

**Met-loss**：由 methionine aminopeptidase 催化；当甲硫氨酸后的残基为 Ala、Cys、Gly、Pro、Ser、Thr 或 Val 时发生；Δmass 为 131 Da。

## 化学修饰

化学修饰主要包括以下类型。

### 氧化（Trp、Met与His）

常见位点为芳香族氨基酸、Met 与 Cys；抗体可变区中暴露的 Met、Trp 与 His 为易氧化位点。

**Trp 氧化**：可导致颜色变化、降低物理稳定性；CDR 环中的 Trp 氧化可降低结合亲和力。

![](/images/ptm/202204031459772.webp)

**Met 氧化**：包括光照氧化与过氧化物氧化两种途径；可降低构象稳定性、产生亲水性变体、引起结构变化并影响抗原结合。

![](/images/ptm/202204031459158.webp)

**His 氧化**：机制包括光氧化与金属催化氧化。

![](/images/ptm/202204031502242.webp)

### 天冬酰胺脱酰胺

**天冬酰胺脱酰胺**（Asn deamidation）：易感基序为 NG、NS、NN、NT 与 NH[^9]；常见发生部位为 CDR-H2 与 CDR-L1 环，β-折叠中发生概率最小[^9][^2]；反应条件为 pH ≥ 6。

脱酰胺途径[^13]：

- 骨架氨基对侧链羰基的亲核反应，形成 succinimide；
- 骨架羰基氧对侧链羰基的亲核反应，形成 isoimide；
- 直接水解，见于 pH 小于 4。

影响因素[^12]：flanking residues 空间位阻、二级与三级结构、溶剂暴露、结构柔性。

Gaza-Bulseco G, Li B, Bulseco A et al (2008) Method to differentiate asn deamidation that occurred prior to and during sample preparation of a monoclonal antibody. Anal Chem 80:9491–9498

![](/images/ptm/202204031317034.webp)

### 天冬氨酸异构化

**天冬氨酸异构化**（Isomerization）：易感基序为 DG、DS、DD、DT 与 DH[^1][^3][^9]；化学本质是 Asp 侧链羰基被 n+1 位残基的离子化胺基亲核攻击；反应条件为低 pH 5-7[^4]，因为侧链 COOH 需要质子才能形成中间产物 succinimide。

影响因素：

- 溶剂介电常数：介电常数越高，Asp 的 pKa 增大（酸越弱、酸解离越少、COOH 越多），侧链 COOH 形式越多，反应性越强，越易发生异构化[^7]；
- 温度：高温加速异构化反应速率；
- flanking residues、电离状态与高级结构[^8]：
  - 空间位阻：Gly 残基位阻低；
  - 质子供体：Ser 与 Thr 残基可在异构化中充当质子供体，如组氨酸；
  - 静电作用：n+1 或 n−1 位带正电残基可通过静电作用加速 Asp 异构化[^10]；
  - 高级结构：溶剂暴露、二级结构、亲核攻击距离（Cγ–Nn+1）与氢键均影响反应；β-折叠中发生概率最小。

影响：

- 主链引入甲基引起构象变化，进而影响表面电荷分布或表面疏水性[^5]；取决于发生位置，可产生 basic、acidic、hydrophobic 与 hydrophilic variant；
- 若发生在 CDR 区，则降低抗原结合亲和力[^6]。

工程化策略：用谷氨酸替代 Asp 可能降低活性；替代邻位氨基酸可减少异构化，同时保持生物活性[^11]。

![](/images/ptm/202204031110609.webp)

### 糖化

**糖化**（Glycation）[^14][^25]：常见位点为 K 与 R；糖基来源于制剂 buffer 中的蔗糖（二糖，可降解为还原糖），也可在细胞培养过程中发生；易感基序为 KD、KXD、KXK 与 KXE；影响包括阻断生物功能位点与诱导聚集；影响因素包括制剂 buffer、储存温度与储存时间。

![](/images/ptm/202204031535994.webp)

### 焦谷氨酸化与氨甲酰化

**焦谷氨酸化**：Pyro-glu from E[^23] 的 Δmass 为 −18.0153；Pyro-glu from Q[^20]。

**氨甲酰化**（Carbamylation）：常见位点为 K 或 R；反应条件为尿素；Δmass 为 43 Da。

![](/images/ptm/202204032145057.webp)

**Carboxylation**

## 参考文献

> 参考资料

> 1. Ref：Post-translational modifications in proteins: resources, tools and prediction methods
> 2. Heterogeneity of monoclonal antibodies - DOI: [10.1002/jps.21180](https://doi.org/10.1002/jps.21180)
> 3. 异质性与功能：Heterogeneity of recombinant antibodies: linking structure to function - PMID: **16375256**
> 4. Post-translational modifications in the context of therapeutic proteins doi.org/10.1038/nbt1252

[^1]: Strohl WR, Strohl LM. Development issues: antibody stability, developability, immunogenicity, and comparability [Internet. In: Therapeutic antibody engineering. Elsevier: Woodhead Publishing; 2012. 377–595. DOI:10.1533/9781908818096.377
[^2]: Robinson NE, Robinson AB. Prediction of protein deamidation rates from primary and three-dimensional structure. Proc Natl Acad Sci U S A. 2001;98(8):4367–72. PMID: 11296285. doi:10.1073/pnas.071066498
[^3]: Wakankar AA, Borchardt RT. Formulation considerations for proteins susceptible to asparagine deamidation and aspartate isomerization. J Pharm Sci. 2006;95(11):2321–36. PMID: 16960822. doi:10.1002/jps.20740
[^4]: Yi L, Beckley N, Gikanga B, Zhang J, Wang YJ, Chih HW, Sharma VK. Isomerization of Asp-Asp motif in model peptides and a monoclonal antibody fab fragment. J Pharm Sci. 2013;102 (3):947–59. PMID: 23280575. doi:10.1002/jps.23423

[^5]: Beck A, Liu H. Macro- and micro-heterogeneity of natural and recombinant IgG antibodies. Antibodies. 2019;8(1):18. PMID: 31544824. doi:10.3390/antib8010018
[^6]: Harris RJ, Kabakoff B, Macchi FD, Shen FJ, Kwong M, Andya JD, Shire SJ, Bjork N, Totpal K, Chen AB. Identification of multiple sources of charge heterogeneity in a recombinant antibody. J Chromatogr B Biomed Sci Appl. 2001;752(2):233–45. PMID: 11270864. doi:10.1016/S0378-4347(00)00548-X.
[^7]: Wakankar AA, Liu J, Vandervelde D, Wang YJ, Shire SJ, Borchardt RT. The effect of cosolutes on the isomerization of aspartic acid residues and conformational stability in a monoclonal antibody. J Pharm Sci. 2007;96(7):1708–18. PMID: 17238195. doi:10.1002/jps.20823.
[^8]: Sreedhara A, Cordoba A, Zhu Q, Kwong J, Liu J. Characterization of the isomerization products of aspartate residues at two different sites in a monoclonal antibody. Pharm Res. 2012;29(1):187–97. PMID: 21809161. doi:10.1007/s11095-011-0534-2.
[^9]: Lu X, Nobrega RP, Lynaugh H, Jain T, Barlow K, Boland T, Sivasubramanian A, Vásquez M, Xu Y. Deamidation and isomerization liability analysis of 131 clinical-stage antibodies. MAbs. 2019;11(1):45–57. PMID: 30526254. doi:10.1080/ 19420862.2018.1548233.
[^10]: Yi L, Beckley N, Gikanga B, Zhang J, Wang YJ, Chih HW, Sharma VK. Isomerization of Asp-Asp motif in model peptides and a monoclonal antibody fab fragment. J Pharm Sci. 2013;102 (3):947–59. PMID: 23280575. doi:10.1002/jps.23423.
[^11]: Patel CN, Bauer SP, Davies J, Durbin JD, Shiyanova TL, Zhang K, Tang JX. N+1 engineering of an aspartate isomerization hotspot in the complementarity-determining region of a monoclonal antibody. J Pharm Sci. 2016;105(2):512–18. PMID: 26869414. doi:10.1016/S0022-3549(15)00185-9.
[^12]: Sydow JF, Lipsmeier F, Larraillet V, Hilger M, Mautz B, Mølhøj M, Kuentzer J, Klostermann S, Schoch J, Voelger HR, et al. Structurebased prediction of asparagine and aspartate degradation sites in antibody variable regions. PLoS One. 2014;9(6):e100736. PMID: 24959685. doi:10.1371/journal.pone.0100736
[^13]: Shire SJ. Stability of monoclonal antibodies (mAbs). In: Monoclonal antibodies. Elsevier: Woodhead Publishing; 2015, 45–92. DOI:10.1016/b978-0-08-100296-4.00003-8.
[^14]: Glycation of antibodies: Modification, methods and potential effects on biological functions
[^15]: Zhao J, Saunders J, Schussler SD, Rios S, Insaidoo FK, Fridman AL, Li H, Liu YH. Characterization of a novel modification of a CHO-produced mAb: evidence for the presence of tyrosine sulfation. MAbs. 2017;9(6):985–95. PMID: 28590151. doi:10.1080/19420862.2017.1332552.
[^16]: Tyshchuk O, Gstöttner C, Funk D, Nicolardi S, Frost S, Klostermann S, Becker T, Jolkver E, Schumacher F, Koller CF, et al. Characterization and prediction of positional 4-hydroxyproline and sulfotyrosine, two post-translational modifications that can occur at substantial levels in CHO cells-expressed biotherapeutics. MAbs. 2019;11(7):1219–32. PMID: 31339437. doi:10.1080/19420862.2019.1635865.
[^17]: Jiang H, Xu W, Liu R, Gupta B, Kilgore B, Du Z, Yang X. Characterization of bispecific antibody production in cell cultures by unique mixed mode size exclusion chromatography. Anal Chem. 2020;92(13):9312–21. PMID: 32497423. doi:10.1021/acs. analchem.0c01641.
[^18]: Gomez N, Lull J, Yang X, Wang Y, Zhang X, Wieczorek A, Harrahy J, Pritchard M, Cano DM, Shearer M, et al. Improving product quality and productivity of bispecific molecules through the application of continuous perfusion principles. Biotechnol Prog. 2020;36(4). PMID: 31991523. doi:10.1002/ btpr.2973.
[^19]: Teramoto T, Fujikawa Y, Kawaguchi Y, Kurogi K, Soejima M, Adachi R, Nakanishi Y, Mishiro-Sato E, Liu MC, Sakakibara Y, et al. Crystal structure of human tyrosylprotein sulfotransferase-2 reveals the mechanism of protein tyrosine sulfation reaction. Nat Commun. 2013;4(1). PMID: 23481380. doi:10.1038/ncomms2593.
[^20]: Determination of the origin of the N-terminal pyro-glutamate variation in monoclonal antibodies using model peptides.- DOI: [10.1002/bit.21260](https://doi.org/10.1002/bit.21260)
[^21]: C-terminal lysine variants in fully human monoclonal antibodies: investigation of test methods and possible causes.- DOI: [10.1002/bit.21855](https://doi.org/10.1002/bit.21855)
[^22]: Processing of C-terminal lysine and arginine residues of proteins isolated from mammalian cell culture. - DOI: [10.1016/0021-9673(94)01255-d](https://doi.org/10.1016/0021-9673(94)01255-d)
[^23]: N-terminal glutamate to pyroglutamate conversion in vivo for human IgG2 antibodies.- DOI: [10.1074/jbc.M110.185041](https://doi.org/10.1074/jbc.m110.185041)
[^24]: Probing of C-terminal lysine variation in a recombinant monoclonal antibody production using Chinese hamster ovary cells with chemically defined media.- DOI: [10.1002/bit.24510](https://doi.org/10.1002/bit.24510)
[^25]: Rates and impact of human antibody glycation in vivo - DOI: [10.1093/glycob/cwr141](https://doi.org/10.1093/glycob/cwr141)
[^26]: Carboxypeptidase D is the Only Enzyme Responsible for Antibody C-Terminal Lysine Cleavage in Chinese Hamster Ovary (CHO) Cells DOI 10.1002/bit.25977

## 相关阅读

- [单抗 CDR 区 Asp 异构化与 Asn 脱酰胺：机制、活性影响与 CQA 控制策略](/posts/mab天冬氨酸异构化与天冬酰胺脱酰胺-文献研究报告)
- [大肠杆菌重组表达蛋白的翻译后修饰与酸性电荷异质性形成机制](/posts/大肠杆菌蛋白修饰与酸性峰)
- [糖基化基础：从单糖立体化学到聚糖结构与生物合成](/posts/糖基化-pert1-基础篇-糖生物学)
