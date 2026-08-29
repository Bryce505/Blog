---
title: "HCP ELISA 稀释线性不通过的判定、报告与早期方法开发策略"
date: 2026-08-29
category: "03质量控制"
primaryTag: "03质量控制/残留/HCP"
description: "这篇文章围绕总 HCP ELISA 稀释线性验证不通过的两个实际问题展开：其一，稀释线性是否必须“通过”、能否支持 III 期前样品检测、如何按 USP〈1132〉Guide 1/2 报告；其二，早期阶段应开发工艺特异性试剂盒还是“商业试剂盒 + 共洗脱 HCP 专属定量”双轨策"
tags:
  - "03质量控制/残留/HCP"
sourceNotes:
  - "Antibody-Characterization/HCP/HCP-ELISA稀释线性不通过的判定报告与早期方法开发策略.md"
---

这篇文章围绕总 HCP ELISA 稀释线性验证不通过的两个实际问题展开：其一，稀释线性是否必须“通过”、能否支持 III 期前样品检测、如何按 USP〈1132〉Guide 1/2 报告；其二，早期阶段应开发工艺特异性试剂盒还是“商业试剂盒 + 共洗脱 HCP 专属定量”双轨策略。全文按“科学本质 → 判定逻辑 → 文献证据 → 策略比较 → 专属定量选型 → 限度与风险 → 监管沟通”的脉络组织，证据基础为 50 篇经 CrossRef 逐条核验的文献与 USP〈1132〉原文。

> [!abstract] 一句话结论
> 稀释线性**不是一条必须“通过”才能放行方法的合格性红线**，而是一个必须被**理解、解释并转化为报告规则**的方法学参数。USP〈1132〉4.3 节明确给出了“永远稀释不到剂量无关点”这一情形的处置办法——报告经稀释倍数校正后、验证范围内的最高 HCP 比值——并给出 Guide 1/Guide 2 两种平均规则。因此，在根因清晰（单一共洗脱 HCP 抗原过量）、机制证据完整（蛋白组学已鉴定）、报告规则预先固化于 SOP 的前提下，该方法**可以支持 III 期前的样品检测与放行**。至于开发策略：文献与药典证据共同支持**“继续使用已验证商业试剂盒 + 对共洗脱 HCP 建立专属定量方法（优先靶向 MS）+ 工艺侧提升清除能力 + 工艺锁定后再评估平台/上游工艺特异性试剂盒”**，即你提出的第二种策略。早期就投入下游工艺特异性试剂盒开发，在文献证据上是**风险最高、回报最不确定**的一条路。

> [!summary] 本文回答什么
> 1. 稀释线性不通过的科学本质是什么，为什么“换试剂盒”通常解决不了；
> 2. 方法验证中稀释线性不通过时的判定逻辑、报告规则（Guide 1 vs Guide 2 vs 第三指南）与 SOP 落地写法；
> 3. 两种开发策略的逐维度比较，以及为什么推荐双轨策略；
> 4. 共洗脱 HCP 专属定量方法（靶向 MS vs 专属 ELISA）的选型依据；
> 5. 限度设定、工艺侧改进手段与监管沟通要点。

## 案例关键事实与稀释线性不通过的科学本质

### 关键事实与适用边界

案例的四个特征共同决定后续判断：更换不同厂家 ELISA 试剂盒，问题依旧；多个批次样品稀释至 QL 以下，仍无法获得稀释线性范围；蛋白组学 HCP 鉴定发现一个主要 HCP，评估确认为共洗脱蛋白；项目处于早期，工艺尚未锁定。这四点构成 USP〈1132〉4.3 节描述的教科书式情形：单一 HCP 与产品共纯化，在多分析物免疫测定格式中超过了可用抗体量。跨厂家复现、跨批次复现、根因已由正交方法（LC-MS/MS）确认——这条证据链恰恰是把“方法失败”转化为“方法已被充分理解”的关键，也是后文所有建议成立的前提。

本文的分析限于总 HCP 免疫测定的稀释线性这一具体参数，不涉及该 HCP 的安全性结论本身（那需要独立的风险评估），也不能替代与所在企业质量部门及监管机构的正式沟通。

### 抗原过量/抗体不足：多分析物测定的结构性限制

USP〈1132〉4.3 节指出，由于单个（或少数几个）HCP 可能与产品共纯化，某个特定 HCP 完全可能超过免疫测定中可用的抗体量。这在多分析物测定中是结构性的——微孔板或磁珠上可用的表面积有限，而需要覆盖的抗 HCP 抗体多达数千种，针对任何单一 HCP 的抗体必然是有限的；多克隆抗血清中针对每一个 HCP 的相对抗体量不受控，因此对每个 HCP 的结合容量各不相同。

总 HCP ELISA 从设计上就不是为“某一个高丰度 HCP”准备的。当一个 HCP 在样品中的相对丰度远超其在免疫原中的丰度时，该 HCP 对应的抗体池被饱和，测得值随稀释而“塌陷”，这正是抗原过量的典型表现。这不是试剂盒质量问题，而是多分析物免疫测定在遇到单一优势分析物时的必然行为。

这也直接解释了换厂家为何无效。不同厂家的免疫原来源、免疫动物、纯化路线各异（关于抗体纯化策略与宿主动物选择的系统比较见 Baldus 等 [10] 与 Seisenberger 等 [11]），但只要它们都是通用 CHO 裂解物免疫获得的多克隆试剂，针对你这个特定共洗脱蛋白的抗体占比就都很低。样品中该蛋白的绝对量若高到超出所有候选试剂盒的抗体容量，换供应商只是在同一个物理约束内平移。

### USP〈1132〉如何定位非线性

〈1132〉的措辞明确：“HCP assay nonlinearity is not uncommon for some samples”——某些样品出现测定非线性并不罕见，应针对同一样品类型的多个批次（如若干临床 DS 批或工艺验证批）进行评估，以确保结果的一致性和正确报告。这包含三层含义：非线性是可预期的现象而非异常事件；评估目的是“确保一致性和正确报告”，而非“确保通过”；要求跨多批次评估——你们已经做到了这一点。

药典随后给出处置阶梯：分析人员必须把样品稀释到测定范围内，即稀释到不再观察到非线性行为的点，此时该 HCP 已被稀释至不再超过可用抗体的浓度。但在某些情况下，测定的灵敏度成为限制因素，永远无法达到测定结果与样品稀释度无关的稀释度；此时应报告验证测定范围内经样品稀释校正后的最高 HCP 比值。换言之，药典预见并接纳了“永远达不到线性区”这一结局，并为它规定了明确的报告方式。

〈1132〉同时给出一条容易被忽视的告诫：历史上一些公司用准确度验证中的加标回收数据来证明线性。这只能证明标准品的线性稀释，不能证明样品中 HCP 的线性稀释——由于抗原过量，标准品的线性稀释是“必要但不充分”条件。另外，若使用均相（一步孵育、试剂间不洗板）夹心免疫测定，这类格式更易发生抗原过量、稀释非线性和高剂量钩状效应，转向异相夹心格式本身就可能改善非线性。

### 必须先排除的其他六种成因

在把根因锁定为“抗体不足”之前，〈1132〉列举了另外六种可能导致稀释非线性的原因，应在验证报告的根因调查部分逐条书面排除：

| # | 潜在成因 | 建议的排除性实验 |
|---|---|---|
| 1 | 抗体与**产品蛋白**发生反应 | 用纯化的自身产品（或近似分子）做梯度加入的空白基质试验；观察信号是否随产品浓度上升 |
| 2 | 存在**非特异性(“黏性”)抗体** | 与无关蛋白基质对照；抗体经 HCP 亲和纯化前后对比 [10] |
| 3 | 抗体与样品中**非 HCP 蛋白**（如蛋白胨、BSA）反应 | 培养基组分单独测定 |
| 4 | **HCP 聚集** | 与 HCP 富集聚集体的表征研究相互印证 [26,27] |
| 5 | **HCP 标准品稀释曲线**不能代表工艺中/终产品 HCP | 标准品与真实样品的稀释曲线并排比较 |
| 6 | **样品基质干扰** | 缓冲液交换后重测；不同工艺中间体的加标回收 |

### 共洗脱是普遍现象，不是你们工艺独有的问题

Zhang 等对 15 个不同单抗的 Protein A 洗脱液做了系统的 2D-LC-HDMSᴱ 比较，发现与单抗结合并共洗脱的 CHO HCP 大多数在各单抗之间是共通的，只有很小一部分（平均约 10%）是某一特定抗体所特有的；决定这些 HCP 在 Protein A 洗脱液中丰度的两个主因是它们在细胞培养液中的丰度以及它们与单抗相互作用的能力 [17]。

机制层面，多项研究把“难以去除”归因于产品结合而非单纯的树脂相互作用：Levy 等鉴定并表征了与产品缔合的 HCP 杂质 [19] 并追踪其在精纯步骤中的行为 [20]；Oh 等系统研究了产品缔合作为 HCP 持留机制的影响因素 [23,24]；Panikulam 等提出 HCP 相互作用网络是 Protein A 层析中的一种新的共洗脱机制 [25]；Singh 等针对利妥昔单抗生物类似药解析了 10 个“难去除”HCP 的滞留机制并提出可指导下游工艺设计的分子解释 [21]；Liu 等在单抗纯化工艺中鉴定并表征了共纯化的 CHO HCP [22]。以 PLBL2 为例，Tran 等证明其在 Protein A 层析中的共洗脱高度依赖于具体抗体分子及层析上样中的 PLBL2 浓度，并受上样密度与洗脱前洗涤条件影响 [18]。类似的“搭便车抗原”现象在亲和纯化研究抗体中也早有报道 [28]。

对策略的直接推论：既然共洗脱 HCP 大多是跨产品共通的高丰度蛋白，且其持留由与产品的分子相互作用主导，那么“重做一套针对本工艺的免疫原”并不会改变这个蛋白在样品中的绝对量，也很难保证新抗血清中针对它的抗体比例足以覆盖其过量。换试剂盒改变的是分母，不是分子。

## 稀释线性不通过的判定逻辑与报告规则

### 判定逻辑：四个条件必须同时成立

稀释线性不是必须“通过”的合格性红线，但必须被解释和处置。USP〈1132〉给出了非线性情形下的报告规则，等于承认这一参数在某些样品类型上无法满足传统意义的线性，而方法仍可用于其预期用途。

方法可以支持 III 期前的样品检测。药典的方法开发生命周期（3.1 节，图 1A）明确设想：在没有平台方法可用的情形下，商业化试剂盒可以配合适当的方法确认（qualification）一直使用到工艺验证阶段；III 期及以后则倾向于平台方法或上游工艺特异性方法，并应做桥接研究支持方法替换。注意药典此处的语境是 qualification，而你们做的是 validation——做到验证级别并不会让处境更糟，但验证报告必须正面处理稀释线性这一项。

报告方式：按预先规定的规则，在验证的测定范围内、对处于线性响应区的数据点做平均。〈1132〉给出 Guide 1 与 Guide 2，并对第三种做法附加了严格条件。以下四个条件必须同时成立，“不通过”才是可接受的：

1. **根因已确认且可解释**——非线性由已鉴定的单一共洗脱 HCP 抗原过量所致，而非基质干扰、抗体交叉反应产品、HCP 聚集等其他成因（见上一节六项排除）。蛋白组学鉴定加共洗脱评估已提供核心证据。
2. **行为具有一致性**——跨多批次、多样品类型可复现，稀释曲线形状稳定。〈1132〉要求跨多批次评估正是为此。
3. **报告规则预先固化**——可平均哪些数据点的规程必须在运行测定之前规定，并通常作为检验规程（test procedure）的一部分予以文件化。事后挑选数据点是不可接受的。
4. **有正交方法补充信息**——总 HCP ELISA 只给出一个数值，且会对高亲和力抗体所针对的 HCP 赋予更大权重，对未被识别或仅被低亲和力抗体识别的 HCP 给予很低或零权重；因此常常需要产品纯度的正交度量。在已知一个 HCP 被系统性低估时，这不是“加分项”而是“必需项”。

Zhu-Shimoni 等的经典论文正是围绕“HCP ELISA 的局限与正交方法的必要性”展开的 [1]，而 Vanderlaan 等汇总的行业经验则说明，监管指导对 HCP 杂质仅要求“尽可能纯”，并未规定数值限度，因为 HCP 暴露的风险往往取决于临床情境（给药途径、剂量、适应症、患者人群）与具体杂质本身 [2]。

### Guide 1、Guide 2 与第三指南：选择依据

〈1132〉表 4 / 图 4 的示例中，测定范围为 1–100 ng/mL，样品先稀释至 10 mg/mL（MRD，此浓度下加标回收已预先确认），再二倍系列稀释至低于测定 QL（1 ng/mL）。三个样品中，样品 1 在全范围内线性稀释，样品 2 与样品 3 在较高样品浓度处出现平台。

| 规则 | 定义 | 特点 | 适用建议 |
|---|---|---|---|
| **Guide 1** | 将**处于最大值 20%（20%–25%）以内**的所有数值平均 | 以“最大值”为锚，直观；纳入点数取决于平台的陡峭程度 | 当平台区较平坦、数据点密集时更稳健 |
| **Guide 2** | 只要所平均数值的 **CV < 20%–25%**，即纳入；**从稀释度最低的样品开始剔除** | 以离散度为准则，自适应；剔除顺序有明确规定 | 当高浓度端塌陷明显、需要客观剔除准则时更合适 |
| **第三种（不推荐作为默认）** | 报告**高于 QL 的最高实测值** | 〈1132〉指出在其示例中该做法给出的结果**至少高 10%**，且其有效性高度依赖方法开发质量 | 仅在方法验证已**非常充分地证明**其适用性时使用 |

〈1132〉对两种规则的合理性给出了统一的论证：20%–25% 的变异处于测定复现性所固有的范围内。在其示例中，两种规则给出的结果非常接近。

具体建议：**优先选 Guide 2**。理由有三：其一，样品在高浓度端塌陷显著，Guide 2 的“优先剔除低稀释度点”规则与抗原过量的物理机制方向一致；其二，Guide 2 以 CV 为客观判据，比“距最大值 20% 以内”更少受单一异常高点的牵动；其三，它天然给出一个可报告的精密度指标，便于趋势分析。但决定必须建立在你们自己的数据上：用已有的多批次稀释系列，把 Guide 1 与 Guide 2 并行计算，比较两者给出的报告值差异与批间一致性，选择差异小、稳健性好的一个写入 SOP。〈1132〉示例中两者结果相近，但这不能默认在你们的样品上成立。**不要选第三种**，除非准备承担“证明其适用性”的额外验证负担，而它带来的唯一后果是报告值系统性偏高。

注意一个前提：〈1132〉的注释指出，样品总是要稀释到 HCP 浓度低于测定 QL 为止。你们描述的“稀释到 QL 以下仍无线性”符合这一操作要求——这一点在报告中应当明确写出。若需要很大的稀释倍数才能进入测定范围，〈1132〉建议做中间稀释以限制稀释相关误差。

### 报告值的性质：下限估计而非真实浓度

按“验证范围内最高 HCP 比值”报告时，这个数值的科学含义是：它是总 HCP 免疫反应性的一个下限估计，不是总 HCP 的真实浓度；由于该共洗脱 HCP 的抗体饱和，该 HCP 对报告值的贡献被系统性低估；因此，该 HCP 的实际水平必须由独立方法给出——这正是策略讨论中“专属定量方法”不可省略的原因。

〈1132〉6.1 节“Assays for Individual HCPs”正是描述这种情形：某些情况下制造工艺可能产生相对高水平的单一 HCP，从而导致报告结果出现偏倚；此时总 HCP 测定中的抗体浓度可能不足以捕获该特定 HCP 的全部；在这种已知存在单一 HCP 的情形下，可能需要针对该单一 HCP 的另一个测定方法。药典还提到一种值得警惕的变体：针对未与产品结合的 HCP 所产生的抗体，可能不识别或很差地识别与产品结合形式的 HCP——共洗脱 HCP 很可能以产品缔合形式存在，这一机制可能同时在起作用，并且无法通过更换总 HCP 试剂盒来解决。

### 验证报告与 SOP 的落地写法

验证报告中稀释线性一节建议按以下结构书写，而不是标记为“不符合”后了事：**观察**（多批次、多试剂盒来源下的稀释响应曲线，附带说明已稀释至 QL 以下）；**根因调查**（LC-MS/MS 鉴定结果，明确该主导 HCP 的身份、丰度、共洗脱证据，逐条排除〈1132〉列举的其他六种成因，说明加标回收不足以证明样品线性）；**药典依据**（引用〈1132〉4.3 关于“灵敏度成为限制、永不达到稀释无关点”情形的处置条款，以及 6.1 关于单一 HCP 专属测定的条款）；**报告规则**（明确 Guide 1 或 Guide 2，写明纳入/剔除准则、最小数据点数、CV 接受限、MRD 与加标回收确认状态，声明该规则在检测执行前已固化）；**方法适用性声明**（本方法用于总 HCP 的趋势监控与批放行，其报告值为免疫反应性 HCP 的下限估计；主导共洗脱 HCP 由专属方法独立定量并单独设限）；**控制策略衔接**（总 HCP 与该单一 HCP 的双指标控制方案、限度、超限调查路径）；**生命周期计划**（工艺锁定后的方法再评估与桥接计划）。

## 为什么早期自研工艺特异性试剂盒不划算

### 工艺特异性并不天然优于平台法

Gunawan 等在一次重大工艺变更后重新评估 HCP ELISA 的适用性，将工艺特异性 ELISA 与平台 ELISA 做了头对头比较：尽管两者的分析标准品在 2D PAGE 上呈现定性差异，LC-MS/MS 显示两者的 HCP 群体是相似的；工艺特异性抗体虽有足够的覆盖率，但对上游工艺中存在的少数优势蛋白更为敏感（即偏倚）；平台抗体覆盖面很宽，能检出该工艺中大多数潜在 HCP 杂质，不偏向少数优势蛋白，且在下游纯化过程中更灵敏；作者据此得出结论：其平台 HCP ELISA 方法优于工艺特异性 HCP ELISA 方法 [9]。

这个结论对你们的情形几乎是量身定做的：你们面临的问题正是“少数优势蛋白造成的偏倚”。用一个以本工艺物料为免疫原的试剂盒，其抗血清将更加偏向那些在免疫原中高丰度的蛋白——如果你们的共洗脱 HCP 在上游物料中同样高丰度，新试剂盒未必改善，甚至可能在其他 HCP 的覆盖上退步。

### 下游工艺特异性方法对工艺变更敏感

〈1132〉3.1 节讨论了一种诱人的想法：把无表达细胞（null cell）物料过第一根（或几根）柱子，用下游柱池免疫动物，从而使免疫原和标准品富集于“最可能进入回收工艺”的 HCP。〈1132〉列出了这一策略的若干顾虑，其中最直接的一条是：如果该测定是作为下游工艺特异性测定开发的，纯化步骤的变更也可能要求用一个与新下游工艺相关的新测定来替换它——这是这类高度特化测定的最大问题，也是平台化测定通常更受青睐的原因，因为下游步骤变更时它们往往不需要新方法。

你们的工艺尚未锁定，且正打算通过工艺优化去提升该 HCP 的清除能力。这意味着下游工艺特异性试剂盒几乎注定要被自己的工艺改进所淘汰。这不是理论风险，而是策略的内在矛盾。〈1132〉对工艺特异性方法的一般定位也很清楚：工艺特异性测定“在用途上是受限的，每一个都必须针对每一个工艺充分确认”；免疫原与校准标准品按设计就是更窄、更针对特定工艺的。

### 自研试剂盒的建立成本与覆盖率论证负担

建立自有 HCP ELISA 是一项系统工程，涉及免疫原制备、宿主动物选择、抗体纯化策略、标准品代表性、覆盖率评价等多个需要独立优化的环节。Seisenberger 等比较了绵羊、山羊、驴、兔、鸡五种免疫动物所得抗体的 HCP 特异性抗体量、覆盖率与夹心 ELISA 性能，发现绵羊、山羊、驴、兔均满足全部测试标准而鸡源抗体不推荐，多物种混合并未带来 ELISA 性能的实质提升 [11]；Baldus 等比较了 Protein A/G 亲和纯化与 HCP 亲和层析两种路线及其组合，前者所得多抗并非完全 HCP 特异，后者更特异但回收更难 [10]；Giordano 等报告了自建 CHO HCP 平台用于 ELISA 监控的可行路径 [12]。

如果自研试剂盒，还必须自证覆盖率，而这一环节的方法学近年正处在被重新审视的阶段：Seisenberger 等用亲和 MS 与间接 ELISA 等正交方法揭示了传统 2D western blot 存在检出盲区，其根因有二——蛋白或抗体量过低无法越过检出限，以及蛋白变性导致构象表位丢失、western blot 假象妨碍 HCP–抗体识别 [13]；Pilely 等提出 ELISA-MS（基于 ELISA 的免疫捕获 + LC-MS/MS 鉴定）以规避现有覆盖率方法的局限，直接给出每种抗体所覆盖的具体 HCP 名单 [14]；Waldera-Lupa 等用定量免疫亲和层析结合蛋白组学（qIAC-MS）评估 ELISA 覆盖率，并考察免疫用 HCP 是否真正代表工艺相关 HCP [15]；Seisenberger 等进一步提出优化的 AP-MS，在 ELISA 抗体上偶联可切割连接子，从而分离真正特异结合的 HCP，显著改善了抗体检出盲区的识别，并有利于“搭便车”HCP 的分析 [16]；Chrone 等在 LC-MS 杂质测定的语境下提出了 HCP 覆盖率方法，用以照亮“暗蛋白组”[47]。

换言之，自研试剂盒不只是“做一套抗体”，还包含一个方法学本身尚未完全收敛的覆盖率论证包。而这些新兴的亲和-MS 覆盖率工具，恰恰同样可以用来论证你们现有商业试剂盒的适用性——这是成本低得多的用法。

## 两种开发策略的比较与推荐

### 策略定义与逐维度比较

**策略 A**：早期即启动工艺特异性试剂盒开发（免疫原制备、免疫、抗体纯化、标准品、覆盖率论证、方法验证），以期获得可通过稀释线性的总 HCP 方法。

**策略 B（你提出的双轨方案）**：继续使用已验证的商业试剂盒（接受稀释线性不通过，按 Guide 规则报告）+ 为共洗脱 HCP 开发专属定量方法（靶向 MS 或专属 ELISA）并设限日常监控 + 纯化工艺优化提升清除 + 工艺验证后工艺锁定，再开发平台/工艺特异性试剂盒。

| 维度 | 策略 A（早期自研工艺特异性试剂盒） | 策略 B（商业试剂盒 + 专属定量 + 工艺优化） |
|---|---|---|
| **能否解决稀释线性问题** | **不确定**。新抗血清对本工艺优势蛋白的偏倚可能更强 [9]；若该 HCP 与产品缔合，针对游离形式的抗体可能识别不了结合形式（〈1132〉6.1） | **不试图解决**，而是绕开：总 HCP 按 Guide 规则报告，问题 HCP 单独定量 |
| **对工艺变更的稳健性** | **差**。下游工艺特异性方法在纯化步骤变更时可能必须整体替换（〈1132〉3.1）；而你们正计划优化工艺 | **好**。商业/平台方法对下游变更不敏感；靶向 MS 方法只依赖肽段，不依赖工艺 |
| **该 HCP 的定量准确性** | 仍是免疫学“当量”值，受抗体可及性支配 | **显著更好**。靶向 MS 给出该蛋白的绝对量，与抗体无关 [42,43] |
| **关键路径时间** | 长（免疫周期 + 覆盖率论证 + 验证） | 短（方法已在用；靶向 MS 方法开发周期以月计） |
| **对风险评估的支撑** | 弱——仍不知道该 HCP 的真实水平 | **强**——可直接支撑 de Zafra 框架 [31] 与高风险 HCP 控制策略 [30] |
| **报废风险** | **高**。工艺锁定后可能需要重做 | 低。工艺锁定后再一次性评估平台/上游工艺特异性方法 |
| **与〈1132〉生命周期图的一致性** | 提前偏离图 1A 路径 | **与图 1A 一致**：商业方法 + 适当确认用至工艺验证，III 期及以后转平台/上游工艺特异性并做桥接 |
| **早期资源占用** | 高，且占用的正是应投向工艺开发的资源 | 中，且投入产生的是可长期复用的资产（MS 方法、限度、机制理解） |

### 推荐策略 B，但需要三处强化

推荐采用策略 B。它与药典的生命周期设计一致，与文献中平台法优于工艺特异性法的实证一致 [9]，与共洗脱 HCP 的分子机制一致（换试剂盒不改变该蛋白的绝对量 [17,18,24,25]），并且它把不确定性最大的一步（自研试剂盒）推迟到不确定性最小的时刻（工艺锁定后）。

三处应当强化：

**强化 1——适用性论证不能停留在“已验证”。** 建议追加两项工作：其一，用亲和-MS 类覆盖率方法（ELISA-MS [14]、qIAC-MS [15]、优化 AP-MS [16]）对现用试剂盒做一次覆盖率评估，产出“被覆盖 HCP 名单”，明确指出该主导 HCP 是否在覆盖名单内以及其抗体容量；其二，做一次免疫耗竭/免疫捕获实验——把该 HCP 从样品中特异性去除后重测总 HCP ELISA，若稀释线性随之恢复，这就是根因的最强直接证据，并且能同时给出“扣除该 HCP 后的其余 HCP 水平”这一有价值的数字。这两项的产出可以直接写进验证报告的根因调查一节。

**强化 2——明确“专属定量方法”优先选靶向 MS**（详见下一节）。

**强化 3——在方案里写明工艺锁定后的决策门与桥接计划**，不要只说“以后再开发”。〈1132〉要求方法替换时做桥接研究；桥接的设计（样品选择、批数、可接受标准）应当在早期就写进方法生命周期计划，否则到 III 期会成为时间瓶颈。

### 策略 A 在什么情况下才应当被重新考虑

不是完全排除。以下情形出现时，应把自研（优先平台/上游工艺特异性，而不是下游工艺特异性）提前：

- 覆盖率评估显示现用商业试剂盒对该工艺 HCP 群体整体覆盖不足（不只是这一个蛋白），即问题不是“一个 HCP 过量”而是“抗体谱不匹配”；
- 供应商侧出现试剂供应或批间一致性风险——〈1132〉专门指出，商业化试剂来自外部供应商，使用者对试剂可得性与批间一致性缺乏控制；Pilely 等的综述也提到抗体库存耗尽会迫使供应商重新免疫，进而要求使用者做桥接研究与 GMP 放行方法的再验证 [3]；
- 细胞培养工艺相对于平台工艺发生显著改变、可能引入显著不同的 HCP 群体——〈1132〉图 1B 的注释正是针对这一情形建议切换到上游工艺特异性方法。

即便如此，上游工艺特异性优于下游工艺特异性，因为前者对纯化变更不敏感。

## 共洗脱 HCP 专属定量：靶向 LC-MS/MS 与专属 ELISA 的选型

### 优先靶向 LC-MS/MS

其一，方法学已经成熟且有完整的验证包先例。Gao 等建立了多重 LC-MRM 测定，同时监测两个已知影响产品质量的高风险脂酶——PLBL2 与 LPLA2——用于工艺开发中的清除追踪；方法在 1–500 ng/mg 的动态范围内线性，且其方法确认包涵盖了批内/批间精密度与准确度、选择性、回收率与基质效应、稀释线性与残留 [42]。请注意：靶向 MS 方法本身的合格性包中就包含稀释线性，并且能够通过——它与总 HCP ELISA 的处境形成鲜明对比，原因就在于它是单分析物测定，不存在抗体容量竞争。

其二，灵敏度足够。Chen 等针对 CHO 培养中常见的三个脂酶 HCP（PLBL2、LPL、LIPA）建立了高分辨 MRM 靶向定量方法，LLOQ 约 1 ng/mL，线性动态范围达三个数量级，并已用于多个自研单抗工艺中间体的表征 [43]。Wang 等进一步报道了 iRT 辅助的靶向质谱实现亚 ppm 灵敏度的高风险 HCP 谱分析 [49]。

其三，它直接服务于“问题 HCP”的定义与控制。E 等的工作标题即为“鉴定并定量一个有问题的 HCP 以支持治疗性蛋白开发”[44]，这与你们的场景高度吻合。Guo 等综述了 LC-MS/MS 方法在 HCP 鉴定与定量以支持工艺开发方面的技术进展与实践考量 [45]；Yu 等报道了用于 HCP 监控与风险控制的 LC-MS 蛋白组学工作流 [50]。

其四，与 USP 的 LC-MS 章节体系衔接。Chrone 等针对 USP〈1132.1〉中的方法做了实验演示、方法确认与比较 [46]，Khalil 等则给出了与 ICH Q2(R2) 对齐的、基于总误差的非靶向蛋白组学 HCP 定量验证方案 [48]。这意味着 MS 路线在药典与验证框架下已有可援引的先例。

其五，不依赖抗体，因而对工艺变更免疫。靶向 MS 依赖的是该蛋白的特征肽段，工艺优化不会使方法失效——这与下游工艺特异性 ELISA 形成对比。

### 专属 ELISA 的适用情形与注意点

单分析物 ELISA 不是错误选项，在以下情形更有优势：需要高通量、低成本的日常放行检测，且样品量大；该 HCP 有商品化的单分析物试剂盒可用（PLBL2 即属此类，行业已有成熟经验 [18,35]）；QC 实验室不具备靶向 MS 的常规运行能力。

但必须注意〈1132〉6.1 的告诫：针对游离蛋白产生的抗体可能不识别或很差地识别与产品结合形式。你们这个 HCP 既然是共洗脱的，就有相当概率以产品缔合形式存在 [19,23,24]，这会让专属 ELISA 重演同一类偏倚。若选择专属 ELISA，必须用靶向 MS 做正交确认，至少在开发阶段完成一次交叉验证。

### 建议的组合

早期用靶向 MS 定量该 HCP（表征 + 工艺开发 + 清除研究 + 限度设定的数据基础），同时评估是否值得再建一个专属 ELISA 作为放行检测。若该 HCP 经工艺优化后清除到远低于关注水平，专属 ELISA 可能根本不必建立——这本身就是策略 B 相对策略 A 的一个隐含优势：它保留了“问题被工艺解决掉”的可能性。

## 限度设定、风险评估与工艺侧改进

### 没有普适数值限度

〈1132〉6.2.1 节的表述很明确：产品开发过程中，随着工艺与产品知识的积累，拒收限（reject limits）可以随着从毒理批 → I/II 期 → III 期 → 商业批的推进而收紧；每个候选药物及其临床方案都是独特的，因此没有单一数值限度适用于所有产品。拒收限主要关乎患者安全，而通常并没有记录“不安全”HCP 水平的具体数据；早期产品的可接受水平应通过风险评估确定（包括非临床数据、公开文献、同一或相似细胞系产品的既往经验等）。

Vanderlaan 等的行业经验综述同样指出，监管指导对 HCP 杂质仅限于“尽可能纯”，未给出数值限度，因为风险取决于临床情境与具体杂质 [2]。IQ DruSafe 的行业调研则汇总了目前企业在总 HCP 与单个 HCP 杂质上所采用的默认限度，以及安全性与免疫原性风险评估方法和全球监管机构反馈 [33]。Molden 等对已上市治疗性蛋白药物的 HCP 谱做了系统分析，为单抗类产品开发提供了基准（benchmark）[34]。

### 建议的双指标控制结构

| 指标 | 方法 | 早期建议 | 依据 |
|---|---|---|---|
| **总 HCP** | 商业 ELISA，按 Guide 1/2 报告 | 设 target 与 alert/action limit；reject limit 基于风险评估与同类产品经验 | 〈1132〉6.2.1；[2,33,34] |
| **该共洗脱 HCP** | 靶向 LC-MS/MS | 单独设 alert/reject 限；基于其生物学性质做风险分级 | 〈1132〉6.1；[30,31,42,43] |

对该 HCP 的风险分级，建议直接套用两个成熟框架：de Zafra 等提出的 HCP 风险评估框架（列举了在评估药品中检出并鉴定的残留 HCP 风险时应考虑的因素及其相对权重，最终形成指导 HCP 控制决策的总体风险评估）[31]；以及 BioPhorum HCP 工作组 26 家公司协作形成的高风险 HCP 共识——其中把有问题的 HCP 界定为具免疫原性、具生物活性或具酶活性（可降解产品分子或制剂辅料）且往往难以通过纯化去除者，并按潜在影响分类、给出建立基于风险评估的完整控制策略的分步建议 [30]。

你需要对这个 HCP 回答的具体问题：它是否与人类同源蛋白高度同源（影响免疫原性风险）？是否具酶活性（脂酶/酯酶会降解聚山梨酯 [38,40]；糖苷酶会降解产品糖基 [39]）？是否具佐剂效应 [37]？给药途径、剂量、疗程与患者人群如何？

### 可援引的免疫原性临床先例

Fischer 等报道的 lebrikizumab 案例是最完整的公开先例：该人源化 IgG4 单抗的临床物料中发现共纯化的 CHO 磷脂酶 B 样蛋白 2（PLBL2），临床研究数据显示约 90% 的受试者产生了针对 PLBL2 的特异性可测免疫应答，同时安慰剂组与治疗组之间观察到的安全性特征相当 [35]。Jawa 等评估了抗体类生物治疗药中 HCP 杂质的免疫原性风险 [36]，Panikulam 等则综述了 HCP 介导的佐剂效应与免疫原性风险 [37]。

这些文献的价值在于：它们说明“存在抗 HCP 免疫应答”与“存在临床安全性问题”不是同一件事，也说明一个共洗脱 HCP 完全可能被识别、被量化、被控制，而产品仍然推进到后期开发。

### 工艺侧：文献支持的清除改进手段

策略 B 的第三条腿是工艺优化，可从文献中直接借鉴的方向包括：

- **Protein A 洗涤步骤优化**——Shukla 等系统开发了改进的柱洗涤步骤以提升 Protein A 层析的 HCP 清除 [29]；Tran 等证明上样密度与洗脱前洗涤条件显著影响 Protein A 洗脱液中 PLBL2 的水平 [18]。这通常是投入产出比最高的第一手段。
- **精纯步骤设计**——Levy 等专门研究了精纯层析步骤中的 HCP 杂质行为 [20]。
- **针对产品缔合机制**——若该 HCP 通过与产品的相互作用持留，单纯改变树脂选择性收效有限；应考虑破坏相互作用的洗涤条件 [19,21,24]，以及 HCP 相互作用网络这一新机制的启示 [25]。
- **聚集体路径**——若该 HCP 富集于聚集体中，SEC/AEX 精纯与聚集体控制可能同时改善 HCP [26,27]。
- **细胞系工程（长期选项）**——Chiu 等通过敲除难去除的 CHO HCP 脂蛋白脂肪酶（LPL）改善了单抗制剂中的聚山梨酯稳定性 [41]。这对早期项目通常太晚，但如果该 HCP 是跨平台反复出现的高风险蛋白，值得纳入平台级改进路线。

一个重要的提醒：〈1132〉指出，FDA 指导允许通过验证免除放行检测要求——一旦清除被证明是一致的；一项适当实施的、作为工艺验证一部分的清除研究可以成为逐批（CoA）检测的可接受替代。也就是说，工艺侧的成功可以从根本上降低分析侧的压力。这是把资源优先投向工艺优化的另一个理由。

## 结论、监管沟通与未决问题

### 与监管沟通：表述为“已被理解和控制的方法学限制”

建议在 IND/临床试验申请及后续沟通中，把这件事表述为“已被理解和控制的方法学限制”而非“验证失败”。六个要点：

1. **现象与根因**：稀释非线性，根因为已鉴定的单一共洗脱 HCP 抗原过量；附 LC-MS/MS 鉴定证据与跨试剂盒、跨批次的复现性数据。
2. **药典依据**：〈1132〉4.3 对该情形的报告规定；6.1 对单一 HCP 专属测定的规定。援引药典条款而非自创逻辑，能显著降低沟通摩擦。
3. **报告规则**：Guide 1/2 的选择依据与预先固化的证据。
4. **双指标控制策略**：总 HCP + 该 HCP 的靶向 MS 定量，各自限度与设限依据。
5. **风险评估**：按 de Zafra 框架 [31] 与 BioPhorum 高风险 HCP 分类 [30] 对该蛋白的评估结论。
6. **工艺改进与生命周期计划**：清除能力提升路线、工艺锁定后的方法评估与桥接研究计划。

### 关键不确定性与本文局限

- **该 HCP 的身份未在本文中使用**。是否为高风险类别（脂酶/酯酶/糖苷酶/与人类同源）会显著改变限度设定与紧迫性，也可能改变对“是否必须建立专属放行检测”的结论。这是你们最应该优先补齐的信息。
- **均相 vs 异相测定格式未知**。若现用为均相格式，格式转换本身可能改善非线性（〈1132〉），应在下结论前排查。
- **未做免疫耗竭实验**。这是把“推断”变成“证明”的关键实验，本文的根因判断在此之前仍属高度合理的推断。
- **Guide 1 与 Guide 2 的选择必须基于你们自己的数据**。本文的偏好（Guide 2）是基于机制方向的建议，不能替代实际比较。
- **本文不构成监管承诺**。所有判定应经企业质量部门审核，并在与相应监管机构的沟通中确认。
- **检索范围**为 PubMed 收录文献 + USP〈1132〉本地文本，未系统覆盖会议报告、行业白皮书（如 BioPhorum 的完整文件集）与各国药典的对应章节（如 Ph. Eur. 2.6.34）。这些来源可能包含额外的实操细节。

## 参考文献

> [!warning] 引用可靠性声明
> 以下 50 条文献的 **DOI、作者、年份、期刊、标题均已逐条通过 CrossRef API 单独查询核验**，全部返回有效记录，无撤稿或勘误标记。**卷/期/页码未做核验，故未列出**；正式引用前请以 PDF 首页为准。USP〈1132〉的引文均取自本库中的 `USP-1132-HCP_2026-08-03-17_21_17.md` 原文。本文中没有任何一条引用是凭记忆生成的。

### 综述与总体框架

1. Zhu-Shimoni et al. Host cell protein testing by ELISAs and the use of orthogonal methods. *Biotechnology and Bioengineering*. 2014. doi:10.1002/bit.25327
2. Vanderlaan et al. Experience with host cell protein impurities in biopharmaceuticals. *Biotechnology Progress*. 2018. doi:10.1002/btpr.2640
3. Pilely et al. Monitoring process-related impurities in biologics–host cell protein analysis. *Analytical and Bioanalytical Chemistry*. 2021. doi:10.1007/s00216-021-03648-2
4. Bracewell et al. The future of host cell protein (HCP) identification during process development and manufacturing linked to a risk-based management for their control. *Biotechnology and Bioengineering*. 2015. doi:10.1002/bit.25628
5. Kornecki et al. Host Cell Proteins in Biologics Manufacturing: The Good, the Bad, and the Ugly. *Antibodies*. 2017. doi:10.3390/antib6030013
6. Hogwood et al. Measurement and control of host cell proteins (HCPs) in CHO cell bioprocesses. *Current Opinion in Biotechnology*. 2014. doi:10.1016/j.copbio.2014.06.017
7. Tscheliessnig et al. Host cell protein analysis in therapeutic protein bioprocessing – methods and applications. *Biotechnology Journal*. 2013. doi:10.1002/biot.201200018
8. Toinon et al. Host cell protein testing strategy for hepatitis B antigen in Hexavalent vaccine – Towards a general testing strategy for recombinant vaccines. *Biologicals*. 2018. doi:10.1016/j.biologicals.2018.05.006

### 试剂盒选型、关键试剂与覆盖率

9. Gunawan et al. Comparison of platform host cell protein ELISA to process-specific host cell protein ELISA. *Biotechnology and Bioengineering*. 2017. doi:10.1002/bit.26466
10. Baldus et al. Comparison of purification strategies for antibodies used in a broad spectrum host cell protein immunoassay. *Biotechnology and Bioengineering*. 2017. doi:10.1002/bit.26482
11. Seisenberger et al. The agony of choice: Impact of the host animal species on the enzyme-linked immunosorbent assay performance for host cell protein quantification. *Biotechnology and Bioengineering*. 2022. doi:10.1002/bit.28265
12. Giordano et al. In-house CHO HCPs platform: A promising approach for HCPs ELISA monitoring. *European Journal of Pharmaceutical Sciences*. 2024. doi:10.1016/j.ejps.2023.106656
13. Seisenberger et al. Questioning coverage values determined by 2D western blots: A critical study on the characterization of anti-HCP ELISA reagents. *Biotechnology and Bioengineering*. 2020. doi:10.1002/bit.27635
14. Pilely et al. A novel approach to evaluate ELISA antibody coverage of host cell proteins—combining ELISA-based immunocapture and mass spectrometry. *Biotechnology Progress*. 2020. doi:10.1002/btpr.2983
15. Waldera-Lupa et al. Host cell protein detection gap risk mitigation: quantitative IAC-MS for ELISA antibody reagent coverage determination. *mAbs*. 2021. doi:10.1080/19420862.2021.1955432
16. Seisenberger et al. Toward optimal clearance: A universal affinity-based mass spectrometry approach for comprehensive ELISA reagent coverage evaluation and HCP hitchhiker analysis. *Biotechnology Progress*. 2022. doi:10.1002/btpr.3244

### 共洗脱机制与“难去除”HCP

17. Zhang et al. Characterization of the co-elution of host cell proteins with monoclonal antibodies during protein A purification. *Biotechnology Progress*. 2016. doi:10.1002/btpr.2272
18. Tran et al. Investigating interactions between phospholipase B-Like 2 and antibodies during Protein A chromatography. *Journal of Chromatography A*. 2016. doi:10.1016/j.chroma.2016.01.047
19. Levy et al. Identification and characterization of host cell protein product-associated impurities in monoclonal antibody bioprocessing. *Biotechnology and Bioengineering*. 2013. doi:10.1002/bit.25158
20. Levy et al. Host cell protein impurities in chromatographic polishing steps for monoclonal antibody purification. *Biotechnology and Bioengineering*. 2015. doi:10.1002/bit.25882
21. Singh et al. Understanding the mechanism of copurification of "difficult to remove" host cell proteins in rituximab biosimilar products. *Biotechnology Progress*. 2019. doi:10.1002/btpr.2936
22. Liu et al. Identification and characterization of co-purifying CHO host cell proteins in monoclonal antibody purification process. *Journal of Pharmaceutical and Biomedical Analysis*. 2019. doi:10.1016/j.jpba.2019.06.021
23. Oh et al. Identification and characterization of CHO host-cell proteins in monoclonal antibody bioprocessing. *Biotechnology and Bioengineering*. 2023. doi:10.1002/bit.28568
24. Oh et al. Factors affecting product association as a mechanism of host-cell protein persistence in bioprocessing. *Biotechnology and Bioengineering*. 2024. doi:10.1002/bit.28658
25. Panikulam et al. Host cell protein networks as a novel co-elution mechanism during protein A chromatography. *Biotechnology and Bioengineering*. 2024. doi:10.1002/bit.28678
26. Oh et al. Characterization and implications of host-cell protein aggregates in biopharmaceutical processing. *Biotechnology and Bioengineering*. 2023. doi:10.1002/bit.28325
27. Herman et al. Analytical characterization of host-cell-protein-rich aggregates in monoclonal antibody solutions. *Biotechnology Progress*. 2023. doi:10.1002/btpr.3343
28. Mechetner et al. The effects of hitchhiker antigens co-eluting with affinity-purified research antibodies. *Journal of Chromatography B*. 2011. doi:10.1016/j.jchromb.2011.07.016
29. Shukla et al. Host cell protein clearance during protein A chromatography: Development of an improved column wash step. *Biotechnology Progress*. 2008. doi:10.1002/btpr.50

### 风险评估、限度与免疫原性

30. Jones et al. "High-risk" host cell proteins (HCPs): A multi-company collaborative view. *Biotechnology and Bioengineering*. 2021. doi:10.1002/bit.27808
31. de Zafra et al. Host cell proteins in biotechnology-derived products: A risk assessment framework. *Biotechnology and Bioengineering*. 2015. doi:10.1002/bit.25647
32. Coye et al. Host Cell Protein Clinical Safety Risk Assessment—An Updated Industry Review. *Biotechnology and Bioengineering*. 2025. doi:10.1002/bit.70029
33. Graham et al. Assessment and Control of Host Cell Proteins in Biologics: Survey of Industry Practices and a Vision for Harmonization. *Biotechnology and Bioengineering*. 2026. doi:10.1002/bit.70154
34. Molden et al. Host cell protein profiling of commercial therapeutic protein drugs as a benchmark for monoclonal antibody-based therapeutic protein development. *mAbs*. 2021. doi:10.1080/19420862.2021.1955811
35. Fischer et al. Specific Immune Response to Phospholipase B-Like 2 Protein, a Host Cell Impurity in Lebrikizumab Clinical Material. *The AAPS Journal*. 2016. doi:10.1208/s12248-016-9998-7
36. Jawa et al. Evaluating Immunogenicity Risk Due to Host Cell Protein Impurities in Antibody-Based Biotherapeutics. *The AAPS Journal*. 2016. doi:10.1208/s12248-016-9948-4
37. Panikulam et al. Host cell protein-mediated adjuvanticity and immunogenicity risks of biotherapeutics. *Biotechnology Advances*. 2025. doi:10.1016/j.biotechadv.2025.108575

### 高风险酶类 HCP 与产品质量影响

38. Li et al. The measurement and control of high-risk host cell proteins for polysorbate degradation in biologics formulation. *Antibody Therapeutics*. 2022. doi:10.1093/abt/tbac002
39. Li et al. Identification and characterization of a residual host cell protein hexosaminidase B associated with N-glycan degradation during the stability study of a therapeutic recombinant monoclonal antibody product. *Biotechnology Progress*. 2021. doi:10.1002/btpr.3128
40. Maier et al. Illuminating a biologics development challenge: systematic characterization of CHO cell-derived hydrolases identified in monoclonal antibody formulations. *mAbs*. 2024. doi:10.1080/19420862.2024.2375798
41. Chiu et al. Knockout of a difficult-to-remove CHO host cell protein, lipoprotein lipase, for improved polysorbate stability in monoclonal antibody formulations. *Biotechnology and Bioengineering*. 2016. doi:10.1002/bit.26237

### 靶向与非靶向质谱定量

42. Gao et al. Targeted Host Cell Protein Quantification by LC–MRM Enables Biologics Processing and Product Characterization. *Analytical Chemistry*. 2019. doi:10.1021/acs.analchem.9b03952
43. Chen et al. A Highly Sensitive LC-MS/MS Method for Targeted Quantitation of Lipase Host Cell Proteins in Biotherapeutics. *Journal of Pharmaceutical Sciences*. 2021. doi:10.1016/j.xphs.2021.08.024
44. E et al. Identification and Quantification of a Problematic Host Cell Protein to Support Therapeutic Protein Development. *Journal of Pharmaceutical Sciences*. 2023. doi:10.1016/j.xphs.2022.10.008
45. Guo et al. Technical advancement and practical considerations of LC-MS/MS-based methods for host cell protein identification and quantitation to support process development. *mAbs*. 2023. doi:10.1080/19420862.2023.2213365
46. Chrone et al. Host cell protein quantitation by LC-MS. Experimental demonstration, qualification, and comparison of methods in USP 1132.1. *Journal of Pharmaceutical and Biomedical Analysis*. 2025. doi:10.1016/j.jpba.2025.117051
47. Chrone et al. Illuminating the Dark Host Cell Proteome: A host cell protein coverage method for LC-MS impurity assays. *Journal of Pharmaceutical and Biomedical Analysis*. 2026. doi:10.1016/j.jpba.2026.117555
48. Khalil et al. Prospective ICH Q2(R2)-Aligned Total-Error Validation of Label-Free Untargeted Proteomics for Host Cell Protein Quantification in Biotherapeutics. *Proteomes*. 2026. doi:10.3390/proteomes14020021
49. Wang et al. High-Risk Host Cell Protein Profiling with Sub-ppm Sensitivity by iRT-Assisted Targeted Mass Spectrometry. *Journal of Proteome Research*. 2026. doi:10.1021/acs.jproteome.5c00680
50. Yu et al. Application of a novel LC–MS-based proteomic workflow for host cell protein monitoring and risk control in biotherapeutics. *Antibody Therapeutics*. 2026. doi:10.1093/abt/tbag013

### 药典

- USP-NF General Chapter 〈1132〉 *Residual Host Cell Protein Measurement in Biopharmaceuticals*. 本文引用的章节：3.1 The Assay Development Cycle；4.3 Sample Linearity；6.1 Assays for Individual HCPs；6.2 Control Strategy。本地文本：`USP-1132-HCP_2026-08-03-17_21_17.md`

> [!Reference] 相关笔记
> 1. HCP-ELISA稀释线性与方法开发策略-文献检索清单
> 2. HCP靶向定量方法综述与CD44-QTOF-PRM试验方案设计
> 3. 乌司他丁CD44-HCP共纯化问题：机制分析与解决方案
> 4. 高风险宿主细胞蛋白分类表（按影响分类）
> 5. HCP鉴定与定量

## 相关阅读

- [宿主细胞蛋白定量中的iBAQ无标记蛋白质组学方法：原理、性能比较与工作流程](/posts/hcp定量-ibaq)
- [ELISA 方法开发中的稀释线性与平行性：MRD 建立、HCP 专属考量与非线性排查](/posts/elisa方法开发-稀释线性和平行性)
- [宿主细胞蛋白（HCP）的质谱鉴定与绝对定量：从定量标准品、Label-free 算法到样品制备方案](/posts/HCP鉴定与定量)
