---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['1.8', '10%', '2003', '2012', '2017', '2026', '25%', '500', '50pmol', '56%']"
title: "Label-free 绝对蛋白质组定量：两种定量策略的比较与 HCP 应用衔接"
date: 2026-08-26
category: "03质量控制"
primaryTag: "03质量控制/残留/HCP"
description: "质谱 label-free 绝对定量是蛋白质组学研究的基础工具，也是生物制药宿主细胞蛋白（HCP）分析的重要方法学来源。本文以 2012 年的大肠杆菌蛋白质组比较研究为主线，先梳理 label-free 绝对定量的算法分类，再分述归一化法（riBAQ）与基于 UPS2 内标的标准"
tags:
  - "03质量控制/残留/HCP"
sourceNotes:
  - "Antibody-Characterization/HCP/2012-Comparison and applications of label-free absolute proteome quantification methods on Escherichia coli.md"
---

质谱 label-free 绝对定量是蛋白质组学研究的基础工具，也是生物制药宿主细胞蛋白（HCP）分析的重要方法学来源。本文以 2012 年的大肠杆菌蛋白质组比较研究为主线，先梳理 label-free 绝对定量的算法分类，再分述归一化法（riBAQ）与基于 UPS2 内标的标准曲线法的原理与关键流程，比较两种策略在不同算法上的表现差异，最后将结论延伸到 HCP 定量场景的方法学选择。

## 质谱定量的底层信号与算法分类

绝对定量方法按是否使用同位素内标可分为两大类。精确同位素稀释法（precise isotope dilution based methods）以稳定同位素标记的肽段或蛋白为内标，其奠基策略是 AQUA（Absolute QUAntification）——以重标合成肽段为内标实现蛋白绝对定量及 PTM 化学计量比测定[依据3]。

Label-free 方法不使用同位素内标，按底层信号的不同再分两类：

- **基于前体离子色谱峰面积（precursor ion current areas）**：MSE、T3PQ、iBAQ，以及同属 MS1 强度类的 Top3[依据2]。
- **基于二级谱图特征（protein sequence coverage / spectral counting）**：emPAI、APEX。

iBAQ 是 MS1 类算法中应用最广的一种。它将匹配到某一特定蛋白质的所有前体肽段的 MS1 色谱峰强度加和，再除以该蛋白质的理论可观测肽段数（通常定义为长度 6–30 个氨基酸的所有理论酶切肽段）。除以理论肽段数的本质是消除蛋白质长度/质量偏差，使原本与质量成正比的强度信号转换为与摩尔量成正比的量[依据1]。

Top3 依赖一个经验观察：每摩尔蛋白质中信号最强的三个肽段的平均 MS 信号响应值，在不同蛋白质之间近似恒定，误差在 ±10% 以内[依据2]。这一关系使 Top3 不需要完整肽段覆盖即可进行绝对定量，适合鉴定深度有限的场景；它也解释了基于 Top3 的 Hi3 策略无需全蛋白组覆盖即可给出绝对量的可行性。

emPAI 与 APEX 均以二级谱图计数为底层信号。这两类方法的共同限制是：MS/MS 计数在高丰度肽段趋于饱和，且动态范围通常较窄，这在后文的策略比较中会再次体现。

## 归一化法（riBAQ）：从摩尔比到绝对质量

归一化法属于 label-free quantification，不需要额外购买和掺入同位素内标，基于数据内部的比例关系推导绝对含量。它在 iBAQ 算法中的实现称为 riBAQ（Relative iBAQ）——即样品中单一蛋白的 iBAQ 值除以全部鉴定蛋白 iBAQ 值之和。

**1. 通过 iBAQ 计算摩尔比。** iBAQ 算法的核心在于将肽段的总强度除以理论肽段数，使 iBAQ 与蛋白质的摩尔数量成正比。因此，将单一鉴定蛋白的 iBAQ 值除以样品中所有鉴定蛋白 iBAQ 值的总和，得到的正是该蛋白在混合物中的摩尔百分比。

**2. 结合相对分子量计算质量比和 ppm。** 将每个蛋白的 iBAQ 值乘以其相对分子量（MW），就能得到代表其质量比例的数值：

$$
ppm(单个HCP)=\frac{iBAQ_{HCP}\times MW_{HCP}}{iBAQ_{目的蛋白}\times MW_{目的蛋白}}\times 10^6
$$

$$
ppm(总体HCP)=\frac{\sum (iBAQ_{HCP}\times MW_{HCP})}{iBAQ_{目的蛋白}\times MW_{目的蛋白}}\times 10^6
$$

**3. 结合总蛋白量计算绝对质量。** 若要把上述质量占比转化为真实的绝对质量（μg 或 ng），必须依靠外部手段（如 Lowry 法、BCA 法或紫外吸收等）独立测定样品的总蛋白量。将特定 HCP 的质量比例乘以测得的总蛋白量，即可计算出该 HCP 的绝对质量。

> [!info]
> **文献1（Krey et al., 2014）**：MaxQuant reports summed intensity for each protein, as well as its iBAQ value. In the iBAQ algorithm, the intensities of the precursor peptides that map to each protein are summed together and divided by the number of theoretically observable peptides, which is considered to be all tryptic peptides between 6 and 30 amino acids in length. This operation converts a measure that is expected to be proportional to mass (intensity) into one that is **proportional to molar amount (iBAQ)**.
> **文献2（Rozanova et al., 2021）**：In the intensity-based absolute quantitation (iBAQ) algorithm, the summed intensities of the precursor peptides that map to each protein are divided by the number of theoretically observable pep-tides, which is considered to be all tryptic peptides between 6 and 30 amino acids in length. This operation converts a measure that is expected to be proportional to mass (intensity) into one that is **proportional to molar amount (iBAQ)**. Interestingly, iBAQ and dividing Top3 by the number of identified peptides gave the most accurate quantitation. Here iBAQ shows less bias when calculating the abundance of smaller proteins.  Relative iBAQ (riBAQ), which is the iBAQ (calculated by MaxQuant) for a protein or protein group divided by all non-contaminant, non-reversed iBAQ values for a replicate, is an equivalent to normalized molar intensity.

**注意事项与局限性**

- **高度依赖鉴定覆盖率**：归一化法的一个核心假设是“贡献了总蛋白池的绝大多数蛋白质都被成功鉴定和定量了”。鉴定深度不足会直接损害分母的完整性。
- **总蛋白量测定的准确度要求极高**：最终算出的绝对质量，其准确度不仅受限于质谱定量的偏差，还直接受限于测定“样品总蛋白量”的生化方法本身的准确度。

## 基于 UPS2 内标的标准曲线法：操作流程与关键控制点

标准曲线法利用已知浓度的掺入标准蛋白（UPS2）建立线性关系，进行绝对定量。UPS2（Proteomics Dynamic Range Standard）为 48 种人源蛋白的混合物，浓度跨越 5 个数量级（50 pmol、5 pmol、500 fmol、50 fmol、5 fmol、500 amol）[依据2]，适合构建宽动态范围的标准曲线。以下为比较研究中的完整流程。

**样本裂解与蛋白提取。** 收集 _E. coli_ 稳态培养物并洗涤、液氮速冻。将细胞沉淀悬浮于冰浴的尿素裂解缓冲液（含 6 M 尿素、2 M 硫脲、10 mM Hepes，pH 8.0）中，加入玻璃珠在 4°C 下剧烈震荡 15 分钟以破碎细胞，离心去除细胞碎片和玻璃珠，使用 2D Quant 试剂盒测定上清液中的总蛋白质浓度。

**内标物的配制与精确掺入。** 将 10.6 μg 的 UPS2 溶解于 20 μl 尿素裂解缓冲液中。**在进行酶切消化之前**，将 1.1 μg 的 UPS2 加入 3 μg 的 _E. coli_ 细胞裂解物中混匀。提前混合确保外源标准品与目标样本共同经历后续所有变性、酶切和质谱分析步骤，从而校正系统误差。

**还原、烷基化与双酶切。** 室温下加入 10 mM DTT 反应 30 分钟还原，随后加入 50 mM IAA 在避光室温下烷基化 20 分钟。第一步加入内切酶 LysC（酶与蛋白质量比 1:50），室温孵育 3 小时；第二步用 50 mM 碳酸铵缓冲液将样本稀释 4 倍以降低尿素浓度对酶活性的抑制，加入测序级胰蛋白酶（1:50），室温过夜孵育。加入 0.1% 的三氟乙酸（TFA）终止酶切，C18-StageTips 除盐。

**质谱分析与搜库设置。** 原始数据导入 MaxQuant（内置 Andromeda 引擎）处理。搜库用的 FASTA 数据库必须同时包含 _E. coli_ 目标序列、UPS2 标准蛋白序列以及常见污染物序列（如角蛋白和胰蛋白酶）。设置肽段和蛋白质 FDR 均严格控制在 1% 以内；**必须勾选开启 iBAQ quantification 选项**；建议开启匹配时间窗口为 1.5 分钟的 “Match between runs” 功能以提高定量覆盖度。

**标准曲线拟合与绝对量计算。** 提取 UPS2 中 48 种蛋白的原始 iBAQ 值，以已知绝对摩尔量（fmol）为横坐标、iBAQ 值为纵坐标，在双对数（Log-log）尺度下线性回归拟合，生成单一标准曲线（该文献中验证此曲线跨越 4 个数量级，R2=0.94）。将 _E. coli_ 样本中任意目标蛋白的 iBAQ 值代入拟合方程，即可换算出其在样本中的真实绝对摩尔量。若进一步将绝对摩尔浓度乘以阿伏伽德罗常数得到分子总数，再除以实验中通过平板计数法独立测得的实际细胞数量（约 8−9×109 cells/ml），即可推导出“每个细胞中的蛋白质拷贝数”。

## 两种定量策略的比较：数据证据与机制解释

该研究用两种方式计算绝对蛋白浓度：一是基于掺入标准蛋白（UPS2，Sigma）已知量的标准曲线线性关系；二是将单一蛋白贡献归一化到样品总蛋白分析量。比较标准蛋白丰度计算结果显示：

- **对 APEX 和 emPAI（光谱计数法）**：使用“标曲法”和“归一化法”两种策略计算出的蛋白丰度，其 Pearson 平方相关系数（R2）**没有差异**（revealed no difference，见 Supplementary Fig. 1B and C vs. E and F）。
- **对 iBAQ（MS1 强度法）**：策略选择带来差异。当放弃“标曲法”而改用“归一化法”时，iBAQ 定量的相关系数从 0.94 明显下降至 0.92（Supplementary Fig. 1A and D）。

差异的机制可以从底层信号特性解释。光谱计数法（APEX、emPAI）在处理高浓度蛋白或复杂样本时，非常容易遇到“饱和效应（saturation effects）”，动态范围通常覆盖 3 个数量级。由于 MS/MS 计数信号本身存在瓶颈，即使套用再精准的“标准曲线”，也无法显著改善最终相关系数。相反，基于 MS1 的 iBAQ 拥有更宽广的动态范围（可达 4 个数量级），通过引入成分复杂的 UPS2 标准品绘制标曲，能够很好地校正不同蛋白质之间电离效率的差异，从而将定量准确性发挥到极致（R2=0.94）。

在该比较中，使用内标标准品的 iBAQ 方法胜出：动态范围广，且线性最好。

## 从大肠杆菌到宿主细胞蛋白：定量策略的衔接与选择

E. coli 全蛋白质组的这两类定量策略，在宿主细胞蛋白（HCP）分析中有直接对应关系。HCP 分析采用三层递进的方法学结构：第一层用 HCP ELISA 做总量筛查；第二层用非靶向 LC-MS 鉴定 HCP 身份与相对丰度；第三层用靶向 MRM/PRM 加重标特征肽段对单个 HCP 做绝对定量[依据4]。吐温降解酶的控制实践是这一结构的典型体现：行业已形成“非靶向 LC-MS 发现 → 靶向 LC-MS 绝对定量 →（必要时）单个 HCP ELISA/酶活检测”的三段式策略[依据6]。

非靶向 LC-MS（第二层）通常使用 Hi3/Top3 或 iBAQ 做半定量，准确度一般在真实值的 1.5–1.8 倍范围内[依据4]。这一精度足以支持 HCP 分级与工艺清除趋势判断，但不足以作为放行限度的方法学基础。行业实践印证了这一分工：IQ DruSafe 对 41 家成员公司的调查（回收 17 份）显示，56%（9/16）的公司将 LC-MS 用于识别高风险 HCP，用于常规广谱 profiling 的仅 25%（4/16）[依据5]。

回到本文的核心比较，归一化法与标准曲线法在 HCP 场景的取舍可以归纳如下：

- **发现阶段用 riBAQ 快速排序**。riBAQ 无需标准品即可给出 ppm 量级的质量占比，适合对大量候选 HCP 做相对排序。但其正确性依赖“绝大多数蛋白被鉴定”的核心假设，这一假设在抗体高丰度背景下的痕量 HCP 场景往往难以成立。
- **高风险 HCP 转入靶向绝对定量**。对已确认身份的高风险 HCP，应转入第三层，采用稳定同位素稀释质谱法（SID-MS），以重标合成特征肽段为内标，实现可溯源的绝对定量[依据4]。在工艺开发侧，面向 HCP 清除监控的模块化自适应 LC-MS 平台（Walker 等）已经投入使用[依据4]。
- **UPS2/UPS1 用于平台性能评估**。多浓度梯度标准品更适合作为 LC-MS/MS 系统性能评估、方法学验证与定量基准[依据2]，而非日常样品定量的常规内标。

## 结论：适用边界与尚未解决的问题

两种策略的本质差异在于对外源内标与鉴定覆盖率的依赖不同。归一化法（riBAQ）无需标准品，适合深覆盖样本（如模式生物全蛋白组）的全局定量；标准曲线法（UPS2 内标）以 48 种蛋白的梯度标曲校正电离效率差异，动态范围可达 4 个数量级（R2=0.94），但依赖内标与样本的同步处理及标准品自身的浓度跨度。

算法对策略的敏感度不同是本文比较的核心发现：MS1 强度类方法（iBAQ）能从精细标曲中获益（0.94 vs 0.92），而光谱计数类方法（APEX、emPAI）因饱和效应与窄动态范围的制约，对策略变化不敏感。这意味着在 HCP 定量中，如果底层算法是谱图计数，优化标曲的意义有限；若使用 iBAQ 类 MS1 强度法，则值得投入标准品标曲。

尚未解决的问题主要集中在方法学验证层面：归一化法的覆盖率假设在复杂基质（如抗体原液）中难以直接验证；标准曲线法的有效性受限于 UPS2 的浓度范围与单批次内标的重现性；从相对定量到靶向绝对定量的切换阈值（何时某个 HCP 的 ppm 水平需要转入第三层精确测量）也缺乏统一标准。这些都需要在具体项目中结合风险等级与工艺数据确定。

## 依据与出处

1. 笔记：`Antibody-Characterization/HCP/HCP鉴定与定量.md` —— 引用要点：iBAQ 将匹配到某一特定蛋白质的所有前体肽段的 MS1 色谱峰总强度加和，除以该蛋白质在理论上可观测到的肽段数量，以消除质量/长度偏差、回归蛋白质摩尔数
2. 笔记：`Antibody-Characterization/HCP/HCP鉴定与定量.md` —— 引用要点：Top3 利用信号最强的三个肽段的平均 MS 信号响应值在不同蛋白质间近似恒定（±10% 以内）这一实验观察；UPS2 为 48 种人源蛋白、浓度跨越 5 个数量级（50 pmol 至 500 amol），常作为 LC-MS/MS 系统性能评估与方法学验证基准
3. 笔记：`Antibody-Characterization/HCP/HCP靶向定量方法综述与CD44-QTOF-PRM试验方案设计.md` —— 引用要点：Gerber 等（2003）首提 AQUA 策略，以重标合成肽段为内标实现蛋白绝对定量及 PTM 化学计量比测定
4. 笔记：`Antibody-Characterization/HCP/HCP靶向定量方法综述与CD44-QTOF-PRM试验方案设计.md` —— 引用要点：HCP 分析呈三层递进（ELISA 总量筛查 → 非靶向 LC-MS 鉴定与相对定量 → 靶向 MRM/PRM 加重标肽段绝对定量）；非靶向 LC-MS 半定量准确度通常在真实值的 1.5–1.8 倍范围内；SID-MS 为可溯源绝对定量的确证手段；Walker 等（2017，mAbs）发表的模块化自适应 LC-MS 平台用于支持 HCP 清除
5. 笔记：`SCI-Paper/2026-Graham-Assessment and Control of Host Cell Proteins in Biologics Survey of Industry Practices and a Vision for Harmonization.md` —— 引用要点：56%（9/16）的公司用 LC-MS 识别高风险 HCP，常规广谱 profiling 仅 25%（4/16）
6. 笔记：`Antibody-Characterization/HCP/吐温降解酶(高风险HCP)及其检测方法系统综述.md` —— 引用要点：行业已形成“非靶向 LC-MS 发现 → 靶向 LC-MS 绝对定量 →（必要时）单个 HCP ELISA/酶活检测”的三段式检测策略