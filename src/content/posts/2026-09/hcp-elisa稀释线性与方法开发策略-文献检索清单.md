---
title: "HCP ELISA 稀释线性验证与早期方法开发策略：文献证据层级与获取清单"
date: 2026-09-01
category: "杂记"
primaryTag: "杂记"
description: "本文汇总了围绕两个核心问题的系统性文献检索结果：HCP ELISA 稀释线性验证不通过（共洗脱主导 HCP 所致）能否用于 3 期前样品检测，以及早期项目应选择何种 HCP 方法开发策略。文章按法规药典、同行评议期刊、行业资料三层证据组织文献，标注核验状态与下载优先级，并如实列出"
tags:
  - "杂记"
sourceNotes:
  - "Antibody-Characterization/HCP/HCP-ELISA稀释线性与方法开发策略-文献检索清单.md"
---

本文汇总了围绕两个核心问题的系统性文献检索结果：HCP ELISA 稀释线性验证不通过（共洗脱主导 HCP 所致）能否用于 3 期前样品检测，以及早期项目应选择何种 HCP 方法开发策略。文章按法规药典、同行评议期刊、行业资料三层证据组织文献，标注核验状态与下载优先级，并如实列出检索缺口，可直接作为获取全文的文献清单。

> [!abstract] 文档定位
> 这是 Stage 1（文献检索）的交付物，不是分析报告。全文到位后，再进入撰写 → 引用核验 → 评审 → 输出的后续流程。

## 检索设计与证据分层

检索日期为 2026-08-05，围绕两个核心问题展开：

- **问题 1**：HCP ELISA 方法验证的稀释线性是否必须通过？不通过能否用于临床 3 期前样品检测？如何按 USP ⟨1132⟩ guide 1/guide 2 报告？
- **问题 2**：稀释线性不通过、项目处于早期时，应选 (A) 立即开发工艺特异性试剂盒，还是 (B) 沿用商业化试剂盒 + 共洗脱 HCP 专属定量（MS 靶向/专属 ELISA）+ 设限日常监控 + 同步优化纯化工艺，工艺锁定后再上工艺特异性试剂盒？

证据分层为三档：①法规药典决定「必须/可以」，②同行评议期刊决定「科学上成不成立」，③行业白皮书与厂商技术资料决定「业界实际怎么做」，仅作佐证不作主论据。主题轴覆盖稀释非线性机理、共洗脱/共纯化 HCP 与临床后果、试剂盒选型、抗体覆盖率评估、MS 鉴定与靶向定量、纯化工艺去除、风险评估与限度设定。

> [!warning] 引用可靠性声明
> - **✅ 已核验**：元数据经 PubMed 官方 esummary 接口逐条比对，作者/刊名/年/卷/期/页/DOI 全部确证，可直接引用。
> - **⚠️ 待核**：标题、刊物、DOI 来自多个独立检索源交叉确认，但卷/期/页或完整作者列表尚未逐字核对。引用前必须以 PDF 首页为准。
> - 本清单中没有任何一条是凭记忆生成的。若某条信息无法确证，已明确标注「待核」而非填补。

## 法规与药典：问题 1 答案的主锚点

### USP ⟨1132⟩（本地全文已有）

**USP ⟨1132⟩ Residual Host Cell Protein Measurement in Biopharmaceuticals** 是本次问题的主锚点：

- §4.3 Sample Linearity 明确：抗体不足/抗原过量是非线性首因；「某些情况下测定灵敏度成为限制，永远达不到结果与稀释度无关的稀释度（*one never reaches a dilution where the assay result is independent of the sample dilution*），此时应报告验证范围内经稀释校正后的最高 HCP 比值」。
- Table 4 + 脚注 a 给出 Guide 1（取最大值 20% 以内的值平均）、Guide 2（按 CV<20% 平均，优先剔除稀释倍数低的点）及「第三种指南」的定义与算例。
- §3.1 Figure 1A/1B 给出商业化试剂盒 → Phase III/工艺验证换平台或上游工艺特异性试剂盒的开发周期图。
- §6.1 明确单一高含量 HCP 需另建专属方法；§6.2.1 论述 target/alert/reject limit 与分期收紧。

### 其余法规文件

| 编号 | 文件 | 核心用途 | 状态 |
|---|---|---|---|
| R2 | **USP ⟨1132.1⟩**（2024-11-01 批准、2025-05-01 生效） | ⟨1132⟩ 的 MS 补充通则，支撑质谱靶向定量的药典级依据 | ⚠️ 需订阅获取 |
| R3 | **Ph. Eur. 2.6.34 Host-cell protein assays** | 欧洲药典 HCP 检测通则，工艺特异性方法开发与验证的欧盟侧要求 | ⚠️ 需订阅获取 |
| R4 | **ICH Q6B** | 工艺相关杂质限度设定原则；「生物技术产品绝对纯度难以测定且结果依赖于方法」的经典表述（⟨1132⟩ §6.2.1 引用）；DS 与 DP 杂质相同则 DP 不必重复检测 | 公开免费 |
| R5 | **ICH Q2(R2)**（FDA 版下载页 fda.gov/media/161201/download） | 决定问题 1 的「必须吗」：linearity 作为验证特性对杂质定量方法的适用性判定（as-applicable matrix） | 公开免费 |
| R6 | **ICH Q5E** | 支撑「工艺锁定后换试剂盒需做 bridging study」 | 公开免费 |
| R7 | **ICH Q9(R1)** | 支撑「基于风险的分阶段 HCP 控制策略」整体框架 | 公开免费 |
| R8 | **21 CFR 610.13** | 「free of extraneous material except that which is unavoidable」的法定原文 | 公开免费 |
| R9 | **EMEA/CPMP CPMP/BWP/382/97**（1997） | ⟨1132⟩ 参考文献中唯一列出的法规文件，支撑「清除研究可替代逐批放行检测」 | 公开免费 |
| R10 | **FDA (1997)** 工艺验证清除研究指导 | ⟨1132⟩ §6.2.1 明确引用（"FDA 1997"）；原文未给出完整标题与编号，文件身份待确认，切勿臆测 | ⚠️ 身份待确认 |

## 同行评议期刊：按主题轴的证据地图

以下文献按七个主题轴组织，均为二级证据、主论据来源。核验状态沿用前述声明：✅ 已核验，⚠️ 待核（以 PDF 首页为准）。

### B1 · 稀释非线性、抗原过量与抗体不足

- **B1-1** Zhu-Shimoni J, et al. *Biotechnol Bioeng*. 2014;111(12):2367–2379. doi:10.1002/bit.25327 — **本清单最关键的一篇**：系统论述 HCP ELISA 的多分析物本质与局限，明确把 dilution nonlinearity 与商业试剂盒覆盖不足、缺乏工艺特异性并列为「需要自建 HCP ELISA 的理由」；并指出对 ELISA 数据的正确解读可反过来定位并鉴定共纯化 HCP。同时支撑问题 1 与问题 2 两侧。⚠️ 卷期页与作者序以 PDF 为准。
- **B1-2** Eaton LC. *J Chromatogr A*. 1995;705(1):105–114. doi:10.1016/0021-9673(94)01249-e — HCP 免疫测定方法开发的奠基性文献，抗原过量/抗体限量问题的早期系统描述，用于论证「这不是新问题、业界已有 30 年共识」。✅
- **B1-3** Seisenberger C, et al. *Biotechnol Bioeng*. 2023;120(1):184–193. doi:10.1002/bit.28265 — 免疫动物物种直接影响 anti-HCP 多抗谱系与覆盖度；解释「为什么换了不同厂家的试剂盒仍然过不了稀释线性」——不同试剂盒的抗体来源与标准品不同，但若失败源于同一个高丰度共洗脱 HCP，换厂家并不能解决。✅
- **B1-4** Giordano E, et al. *Eur J Pharm Sci*. 2024;192:106656. doi:10.1016/j.ejps.2023.106656 — Merck Serono 自建 CHO HCP 平台试剂的实证：自建平台方法与商业试剂盒的性能对比，为问题 2 的「何时值得自建」提供近期实测数据。✅

### B2 · 共纯化/共洗脱 HCP 与临床后果

- **B2-1** Vanderlaan M, et al. *Biotechnol Prog*. 2018;34(4):828–837. doi:10.1002/btpr.2640 — 共纯化 HCP 的实战案例集：产品同源物、与产品结合的 HCP 两类典型共纯化机制及其临床后果，是「共洗脱蛋白」归类与风险论证的直接参照。⚠️ 卷期页以 PDF 核。
- **B2-2** Fischer SK, et al. *AAPS J*. 2017;19(1):254–263. doi:10.1208/s12248-016-9998-7 — 业界最著名的共洗脱 HCP 事件：Genentech lebrikizumab 残留 CHO PLBL2 高达约 330 ppm，III 期约 90% 受试者产生 PLBL2 特异性免疫应答（但未观察到与安全性事件的相关性、也未增加抗药抗体发生率）。论证「单一共洗脱 HCP 必须单独设限监控」的最强案例。✅
- **B2-3** Chiu J, et al. *Biotechnol Bioeng*. 2017;114(5):1006–1015. doi:10.1002/bit.26237 — 难去除 HCP 的另一条解决路径：从细胞株层面敲除（CHO 脂蛋白脂肪酶，用于改善单抗制剂中聚山梨酯稳定性）。为问题 2 的策略选项补充第三条腿（宿主细胞工程）。✅
- **B2-4** Vanderlaan M, et al. *BioProcess International*（行业刊，非同行评议）— PLBL2 事件的工艺与分析侧完整叙述，比 B2-2 更偏 CMC 视角。引用时需标注为行业刊物。⚠️ 年份/卷期待核。
- **B2-5** Dolan 等. *Biotechnol Bioeng*. 2026. doi:10.1002/bit.70104 — 最新的共纯化 HCP 分子层面表征（蛋白异构体），说明「同一个 HCP 存在多种形式」对 ELISA 识别的影响。⚠️ 作者全名/卷期页待核。
- **B2-6** *mAbs*. 2024. doi:10.1080/19420862.2024.2375798 —— 系统表征单抗制剂中 CHO 来源水解酶的研究（标题含 "Illuminating a biologics development challenge: systematic characterization of CHO cell-derived hydrolases identified in monoclonal antibody formulations"）。高风险共洗脱 HCP（水解酶类）的系统清单，可用于评估主导 HCP 的风险等级。⚠️ 作者待核。

### B3 · 试剂盒选型：商业化 / 平台 / 工艺特异性

- **B3-1** Graham J, et al. *Biotechnol Bioeng*. 2026. doi:10.1002/bit.70154 — **对问题 2 权重最高的一篇**。IQ DruSafe 杂质安全工作组（生物制品杂质子团队）行业调研，覆盖四大板块：HCP 控制挑战范围、控制与监测实践、HCP 水平的合格性论证方法、与各国药监的互动反馈。文中给出总 HCP 与单个 HCP 的当前业界默认限度，以及全球药监反馈汇总——正是「策略 A 还是策略 B」的业界基准答案。⚠️ 卷期页待核（2026 年新刊）。
- **B3-2** Wang X, Hunter AK, Mozier NM. *Biotechnol Bioeng*. 2009;103:446–458. doi:10.1002/bit.22304 — HCP 领域被引最多的奠基综述，鉴定/定量/风险评估三位一体框架，所有策略论证的通用底座。⚠️ 起止页已确认，期号待核。
- **B3-3** Bracewell DG, Francis R, Smales CM. *Biotechnol Bioeng*. 2015;112(9):1727–1737. doi:10.1002/bit.25628 — 基于风险的分阶段 HCP 管控的纲领性文章，支撑「早期不必强求工艺特异性试剂盒，而应按风险配置分析资源」的核心论点，即策略 B 的理论依据。⚠️ 卷期页来自检索源交叉确认。
- **B3-4** de Zafra CLZ, et al. *Biotechnol Bioeng*. 2015. doi:10.1002/bit.25647 — HCP 风险评估框架的另一篇代表作，与 B3-3 互为补充，用于为主导共洗脱 HCP 做正式风险分级并据此设限。⚠️ 卷期页待核。
- **B3-5** *J Pharm Sci*. 2026（ScienceDirect PII: S0022354926001516）— 论证「何时通用试剂盒不再够用、必须走定制化 ELISA」的近期实证。标题本身即是策略 A 的支持论据；原文聚焦原核 vs 真核体系差异，需读全文判断适用边界。⚠️ 作者/卷期页/DOI 待核。
- **B3-6** *BMC Proceedings*. 2015;9(Suppl 9):P21. doi:10.1186/1753-6561-9-S9-P21 — 平台 HCP 方法开发的会议摘要级材料，篇幅短、证据强度低，仅作补充，不宜作为主论据。⚠️ 作者待核。

### B4 · 抗体覆盖率评估

- **B4-1** Pilely K, et al. *Biotechnol Prog*. 2020;36(4):e2983. doi:10.1002/btpr.2983 — ELISA-MS 覆盖率评估法。关键用途：证明商业试剂盒对主导 HCP 究竟有没有抗体、抗体量够不够——这是区分「抗体不足（可通过稀释解决）」与「抗体缺失（稀释也救不了）」的决定性实验，直接决定策略选择。✅
- **B4-2** ELISA reagent coverage evaluation by affinity purification tandem mass spectrometry（PMC5627587，*mAbs* 2017 前后）— 亲和纯化-串联质谱评估覆盖率的另一路线，与 B4-1 方法学互补。⚠️ 作者/刊物/卷期页/DOI 待核。

> [!note] 覆盖率方法的证据层级提醒
> 2D Western blot、AAE（Antibody Affinity Extraction）与 AAE-MS 的覆盖率对比数据（如 2D-WB 约 50–60%、AAE+2D-PAGE 约 60–85%、AAE-MS 约 70–90%）主要来自 **Cygnus Technologies 的厂商白皮书**，不是同行评议文献。这些数字可以作为「业界常用参考区间」提及，但必须标注来源为厂商技术资料，不能与 B4-1/B4-2 的同行评议结论混同引用。

### B5 · MS 鉴定与靶向定量

- **B5-1** Gao X, et al. *Anal Chem*. 2020;92(1):1007–1015. doi:10.1021/acs.analchem.9b03952 — 单个 HCP 靶向绝对定量的方法学主引，支撑「为共洗脱 HCP 建立专属 MS 定量方法并设限日常监控」这一策略的可行性。✅
- **B5-2** Doneanu C, et al. *J Vis Exp*. 2018;(134). doi:10.3791/55325 — QTOF 离子淌度平台的 HS-MRM 方案，含可操作实验流程。✅
- **B5-3** Reiter K, et al. *J Pharm Biomed Anal*. 2019;174:650–654. doi:10.1016/j.jpba.2019.06.038 — MS 定量与纯化工艺优化联动的实例。✅
- **B5-4** Bracewell DG, et al. *Curr Opin Biotechnol*. 2021;71:98–104. doi:10.1016/j.copbio.2021.06.026 — HCP 分析技术全景综述（近期、权威、篇幅适中），适合作为报告中「方法学选择」一节的总纲引用。✅
- **B5-5** *mAbs*. 2023;15(1). doi:10.1080/19420862.2023.2213365 — LC-MS/MS 支撑工艺开发的技术进展与实操考量综述，含方法选型的实际权衡。⚠️ 作者待核。
- **B5-6** *mAbs*. 2021;13(1). doi:10.1080/19420862.2021.1955811 — 设限的行业基准数据：LC-MS/MS 分析 29 个已上市 mAb 及 mAb 类药物，共鉴定 79 个单个 HCP；剔除一个离群药物后，单个 HCP 相对水平平均约 20 ppm，每个药物平均鉴定出 <7 个 HCP。为共洗脱 HCP 设定专属限度提供横向参照。⚠️ 作者待核。
- **B5-7** *J Pharm Biomed Anal*. 2025（ScienceDirect PII: S0731708525003929）— ⟨1132.1⟩ 中各 MS 定量方法的实测比较与合格性论证。若走 MS 靶向定量路线，这是方法合格性论证的直接依据。⚠️ 作者/卷页/DOI 待核。
- **B5-8** *Anal Bioanal Chem*. 2021. doi:10.1007/s00216-021-03648-2 — ELISA 与 MS 并用的综述，含 ELISA 合格性论证（稀释线性、LOQ、试剂表征）要点。⚠️ 作者/卷页待核。

### B6 · 纯化工艺去除共洗脱 HCP

- **B6-1** Levy NE, et al. *Biotechnol Bioeng*. 2016;113(6):1260–1272. doi:10.1002/bit.25882 — 精纯步骤中 HCP 杂质的滞留机制：产品结合（product association）与共洗脱（co-elution）两类机制均被确认，是判定「共洗脱蛋白」时的机制归类依据。✅
- **B6-2** *J Chromatogr A*. 2024（ScienceDirect PII: S0021967324006034）— 多模式层析清除难去除 HCP 的实例：HCP 在梯度前端、低盐处洗脱，据此设计中间低盐洗涤的阶跃洗脱工艺，总 HCP 降低约 80%。策略 B 中「优化工艺提高去除能力」的具体技术路径。⚠️ 作者/卷页/DOI 待核。
- **B6-3** *Protein Expr Purif* 系列（ScienceDirect PII: S104659281730147X）— 下游 HCP 清除策略综述。⚠️ 作者/刊物/年/卷页/DOI 待核。

### B7 · 风险评估与限度设定

- **B7-1** Haltaufderhyde K, et al. *AAPS J*. 2023;25(5):87. doi:10.1208/s12248-023-00852-z — ISPRI-HCP 工具：基于 T 细胞表位密度与人源同源性评估单个 HCP 的免疫原性潜力。在没有临床数据时，为共洗脱 HCP 设定专属限度提供 in silico 论证。✅
- **B7-2** *mAbs*. 2024;16(1). doi:10.1080/19420862.2024.2333729 — 免疫原性 in silico 评估方法学综述，B7-1 的方法学背景。⚠️ 作者待核。

## 行业组织与厂商资料：仅作佐证的三级证据

> [!caution] 使用规则
> 这一层不是同行评议文献。在最终报告中只能用于说明「业界实际怎么做」，不能作为科学论断或法规义务的主论据，且必须显式标注来源性质。厂商资料尤其存在利益相关（试剂盒供应商天然倾向推荐定制化方案）。

| 编号 | 来源 | 用途 | 性质 |
|---|---|---|---|
| I1 | BioPhorum Host Cell Proteins workstream：HCP risk assessment tool 及配套 position papers | 行业联盟共识的 HCP 风险评估工具，多家 MNC 共同制定，三级证据里可信度最高的一份，适合支撑策略 B 的风险分级做法 | 行业联盟共识 |
| I2 | BioPhorum Phase appropriate approach to assay validation | 分阶段方法验证的行业推荐。主体面向细胞与基因治疗（CGT），直接外推到单抗 HCP ELISA 需说明适用性差异，不可当作单抗领域的通用规则引用 | 行业联盟共识（CGT 侧重） |
| I3 | BEBPA HCP 年会（如 2023 Dubrovnik）摘要集、HCP 行业调研报告、⟨1132.1⟩ 技术简报 | BEBPA 是 HCP 分析领域的专门行业会议，摘要能反映最新业界实践与监管风向 | 会议摘要 |
| I4 | Cygnus Technologies 技术资料：*Establishing Dilution Linearity for Your Samples in an ELISA*、*Poor Dilution Linearity*、AAE 白皮书 | 稀释线性判定可操作准则（相邻倍比稀释间稀释校正值变化 ≤±20%、避开校正前读数低于 2×LOQ 的低端区、MRD 定义）与 AAE 覆盖率方法。实操细节最具体的一份，但供应商利益相关，需与 USP ⟨1132⟩ 交叉印证后使用 | 厂商技术资料 |
| I5 | Alphalyse 关于五个商业 HCP-ELISA 试剂盒比较的技术文章 | 佐证「换厂家试剂盒结果差异」的机理（抗体特异性差异 + 标准品组成差异） | 厂商技术资料 |
| I6 | BioProcess International / BioPharm International / American Pharmaceutical Review 专题文章 | 行业实践与案例的补充读物 | 行业刊物 |
| I7 | Lonza CDMO Notes: Navigating HCP ELISA bridging challenges during customer process tech transfer | HCP ELISA 桥接研究的实操难点，对应「工艺锁定后换工艺特异性试剂盒」时必做的 bridging | CDMO 技术文章 |

### Vault 内既有资料（内部证据）

`Antibody-Characterization/HCP/` 下已有与本问题高度耦合的既有笔记，可在后续报告中直接调用：乌司他丁 CD44-HCP 共纯化问题案例（与本问题背景直接同构，含机制与解决方案）；HCP 靶向定量方法综述与 CD44-QTOF-PRM 试验方案设计（共洗脱 HCP 专属 MS 定量方法的已成型试验方案，是策略 B 的现成落地路径）；高风险宿主细胞蛋白分类表（风险分级速查）；HCP 鉴定与定量、HCP-QTOF 定量文献综述、HCP 定量 iBAQ、HCP 样品前处理流程（方法学基础）；免疫原性风险评估 in silico 方法（与 B7-1 衔接）；CD44 毒性文献综述与患者风险评估（单个 HCP 风险评估的完整范例）。

## 全文获取优先级

> [!tip] 给全文获取的排序建议
> 分三档。**P0 不到位则后续论证会缺主干**；P1 显著增强论证；P2 锦上添花。

**P0 — 必须（缺一不可）**

1. B3-1 Graham et al. 2026, doi:10.1002/bit.70154 — 问题 2 的业界基准与监管反馈
2. B1-1 Zhu-Shimoni et al. 2014, doi:10.1002/bit.25327 — 问题 1 与问题 2 的共同主引
3. B2-1 Vanderlaan et al. 2018, doi:10.1002/btpr.2640 — 共纯化 HCP 案例集
4. R2 USP ⟨1132.1⟩ — MS 路线的药典依据（2025-05-01 生效）
5. R5 ICH Q2(R2) — 决定「稀释线性是否为必须的验证特性」（FDA 官网免费）

**P1 — 强烈建议**

B3-3 Bracewell 2015（分阶段风险管控纲领）、B3-4 de Zafra 2015（风险评估框架）、B4-1 Pilely 2020（判定「抗体不足 vs 抗体缺失」的关键实验）、B5-1 Gao 2020（靶向 MS 定量主引）、B5-6 mAbs 2021 HCP profiling（设限的行业基准数据）、B1-3 Seisenberger 2023（解释「换厂家仍失败」）、R3 Ph. Eur. 2.6.34（欧盟侧法规要求）、I1 BioPhorum HCP 风险评估工具（行业共识，免费注册可下载）。

**P2 — 有余力时补**

B3-2 Wang 2009、B2-2 Fischer 2017（PLBL2 临床免疫原性）、B5-7 ⟨1132.1⟩ 方法比较、B6-1 Levy 2016、B6-2 J Chromatogr A 2024 多模式层析、B7-1 Haltaufderhyde 2023、B1-4 Giordano 2024、B3-5 J Pharm Sci 2026 tailored ELISA、B5-5 mAbs 2023 LC-MS/MS 实操综述。

## 检索缺口与证据边界

> [!warning] 已知的证据缺口 — 不要在最终报告中掩盖
> 1. **没有找到直接论述「稀释线性验证不通过时的监管可接受性」的同行评议文献。** USP ⟨1132⟩ §4.3 的「报告验证范围内最高值」是目前唯一的药典级明文出路，B3-1（Graham 2026）的药监反馈章节是唯一可能提供实际监管态度的二手来源。最终报告必须如实说明：这个结论的证据基础是**药典条款 + 行业调研**，而非受控临床/监管案例研究。
> 2. **⟨1132⟩ 引用的 "FDA 1997" 文件身份未确认**（见 R10）。引用前须确认具体文号与标题。
> 3. **Ph. Eur. 2.6.34 的具体条款内容未获取。** 检索到的「HCP 含量应低于 0.1%」等表述来自二手来源，未经原文核实，不可直接引用。
> 4. **「3 期前可否使用未通过稀释线性验证的方法」没有法规明文。** 该结论只能由 ICH Q2(R2) 的 as-applicable 逻辑、⟨1132⟩ §3.1 的分期试剂策略图、以及 B3-1 的行业实践三者**推导**得出，属于论证而非引证——报告中必须标明推理链条与不确定性。
> 5. **MS 靶向定量方法学**本次未单开专项检索，现有 B5 组文献 + vault 内既有笔记应已够用；若撰写时发现不足，再补检。

后续流程：下载 PDF → Google Drive → Stage 2 撰写技术策略报告（回答问题 1 与问题 2）→ 引用真实性核验（强制门禁）→ 模拟专家评审（CMC/法规/分析三视角 + Devil's Advocate）→ 修订 → 终核验 → 输出最终 MD。

## 相关阅读

- [HCP靶向定量方法综述与CD44-QTOF/PRM靶向定量试验方案设计](/posts/hcp靶向定量方法综述与cd44-qtof-prm试验方案设计)
- [CGE分析F(ab)2片段：峰面积下降与迁移时间漂移的系统分析](/posts/cge_fab2_analysis_report)
- [单抗 CDR 区 Asp 异构化与 Asn 脱酰胺：机制、活性影响与 CQA 控制策略](/posts/mab天冬氨酸异构化与天冬酰胺脱酰胺-文献研究报告)
- [CE-SDS 中 IgG 纯度分析的压力进样可行性、电动进样稳定性策略与 PA800 Plus 参数优化](/posts/cge_injection_optimization_report)
- [HCP ELISA 稀释线性不通过的判定、报告与早期方法开发策略](/posts/hcp-elisa稀释线性不通过的判定报告与早期方法开发策略)
- [糖基化基础：从单糖立体化学到聚糖结构与生物合成](/posts/糖基化-pert1-基础篇-糖生物学)
- [大肠杆菌重组表达蛋白的翻译后修饰与酸性电荷异质性形成机制](/posts/大肠杆菌蛋白修饰与酸性峰)
- [宿主细胞蛋白定量中的iBAQ无标记蛋白质组学方法：原理、性能比较与工作流程](/posts/hcp定量-ibaq)
- [乌司他丁分子结构与 O-糖胺聚糖链表征方法学综述](/posts/乌司他丁-ulinastatin-文献综述)
- [切胶覆盖率样品前处理：银染凝胶条带胶内酶切与nLC-MS/MS分析的完整SOP](/posts/切胶覆盖率)
- [ELISA 方法开发中的稀释线性与平行性：MRD 建立、HCP 专属考量与非线性排查](/posts/elisa方法开发-稀释线性和平行性)
- [生物制品功能学研究策略：覆盖早研至BLA全生命周期的效价测定与方法学体系](/posts/分项策略-功能学研究策略-20260703)
- [宿主细胞蛋白（HCP）的质谱鉴定与绝对定量：从定量标准品、Label-free 算法到样品制备方案](/posts/HCP鉴定与定量)
- [治疗性单抗质量属性与表征方法：结构基础、理化分析、电荷变体机制与放行标准](/posts/00基础-生物制品-单抗)
- [Git & GitHub 学习笔记](/posts/tools-笔记)
- [Claude Code on the Web / Cloud Session 使用笔记](/posts/tools-claude-code-cloud-notes)
