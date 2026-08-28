---

reviewNotes:
  - "减法模式下篇幅 9,104 字符（原文 16,974，比例 54%）超出 9,336～16,125 字符的区间"
title: "宿主细胞蛋白定量中的iBAQ无标记蛋白质组学方法：原理、性能比较与工作流程"
date: 2026-08-28
category: "03质量控制"
primaryTag: "03质量控制/残留/HCP"
description: "宿主细胞蛋白（HCP）是重组治疗性蛋白生产中的关键工艺相关杂质，常规ELISA虽为金标准，但无法鉴定和定量单个HCP物种。本文以基于MS1信号强度的iBAQ无标记定量方法为主线，介绍其原理、与其他无标记定量方法的性能比较、HCP鉴定与定量的工作流程要点、各场景下的应用实例，以及该"
tags:
  - "03质量控制/残留/HCP"
sourceNotes:
  - "Antibody-Characterization/HCP/HCP定量：iBAQ.md"
---

宿主细胞蛋白（HCP）是重组治疗性蛋白生产中的关键工艺相关杂质，常规ELISA虽为金标准，但无法鉴定和定量单个HCP物种。本文以基于MS1信号强度的iBAQ无标记定量方法为主线，介绍其原理、与其他无标记定量方法的性能比较、HCP鉴定与定量的工作流程要点、各场景下的应用实例，以及该方法在HCP定量中的优势与局限。

## HCP背景与iBAQ原理

HCP是来源于宿主生物的工艺相关杂质（单克隆抗体生产中主要为CHO细胞）。法规要求严格管控其水平，通常要求最终药品中降至<100 ppm（ng HCP/mg产品）[1–3]。ELISA仍是常规监测金标准，而基于质谱的蛋白质组学，尤其是采用iBAQ的无标记定量方法，已成为全面鉴定和定量单个HCP物种的有力正交方法[4,5]。

iBAQ由Schwanhäusser等人在2011年关于哺乳动物基因表达控制全局定量的研究中提出[6]。其原理是：对每个鉴定蛋白，将所有肽段峰强度（提取离子流图，XIC）之和除以理论可观测肽段数，以校正大蛋白因产生更多肽段而天然具有更高总强度的偏差；所得iBAQ值与样品中该蛋白的摩尔量成正比[6]：

**iBAQ = (Sum of peptide intensities) / (Number of theoretically observable peptides)**

iBAQ属于MS1-based无标记定量方法，依赖一级质谱扫描中的前体离子信号强度[7]。与NSAF、emPAI等基于MS2谱图计数的方法不同，iBAQ利用的是前体离子色谱峰面积[8]。

## iBAQ与其他无标记定量方法的性能比较

多项研究对iBAQ与其他无标记定量方法做了系统比较。Arike et al. (2012) 在大肠杆菌蛋白质组数据上评估APEX、emPAI和iBAQ，iBAQ的生物学重复间相关性最好，蛋白丰度呈正态分布，核糖体蛋白（预期化学计量相近）的丰度变异性最低；iBAQ与emPAI定量蛋白的总量与Lowry总蛋白定量吻合良好，证实了二者在蛋白质组水平计算绝对蛋白浓度的准确性[9]。

Bubis et al. (2017) 以变异系数（CV）、方差分析（ANOVA）和标准定量误差为标准比较SIN、emPAI、NSAF、MaxLFQ和Quanti五种方法，基于强度的MaxLFQ等方法在精密度上总体优于谱图计数法[10]，与iBAQ作为强度类方法的性能预期一致。

Sánchez et al. (2021) 在酿酒酵母中以生物学重复和批次间技术重复对iBAQ的准确度与精密度做基准测试，显示iBAQ能提供合理的绝对蛋白丰度估计，但由MS强度换算为绝对丰度的转换方法会显著影响准确度与精密度[11]。

Shalit et al. (2015) 在四极杆-Orbitrap仪器上比较iBAQ与Hi-N方法（基于Top N肽段强度），两者在MS1-based无标记蛋白质组学中均具有高精密度和定量准确度[12]。

## HCP鉴定与定量的工作流程

### 样品制备

HCP相对治疗性产品处于ppm级低水平，构成高动态范围挑战[13]。常用策略包括：Protein A去除以移除单克隆抗体、富集HCP[4,5]；产品特异性抗体亲和去除治疗性蛋白[14]；以及经变性、还原、烷基化后通常以胰蛋白酶酶解。

### LC-MS/MS采集

高分辨质谱仪（Orbitrap或Q-TOF）以数据依赖采集（DDA）或数据非依赖采集（DIA）模式运行是标准做法。HCP分析中，使用排除列表（排除产品来源肽段质量）可显著提高低丰度HCP的检出灵敏度[15]。

### 蛋白鉴定与iBAQ定量

数据库搜索同时针对宿主生物蛋白质组（如CHO或E. coli）与治疗性蛋白序列进行。iBAQ值由MaxQuant等已整合该功能的生物信息学工具计算[6,9]，可转换为近似绝对丰度，或用于跨样本相对比较。

## iBAQ在HCP研究中的应用

### 细胞培养过程中的HCP动态监测

Park et al. (2017) 采用纳流LC-MS/MS无标记定量分析了产mAb CHO细胞在批次和补料分批培养中的胞外HCP动态，在补料分批和批次培养中分别鉴定到2145和1934个蛋白，其中1673和1486个得到定量。聚类分析显示Lgmn、Ctsd、Gbl1、B4galt1等HCP与mAb聚集、电荷变体、N-糖基化等关键质量属性的变化相关[16]。

### 下游纯化中的HCP追踪

Chiverton et al. (2016) 应用iTRAQ定量蛋白质组学追踪了由Protein A、阳离子交换和阴离子交换层析组成的完整下游工艺中的HCP谱，各实验共鉴定936个蛋白，证明了追踪单个HCP物种穿越纯化步骤的可行性[17]。Goey et al. (2018) 在HCP去除的质量源于设计（QbD）实施综述中，强调蛋白质组学表征对识别纯化过程中问题HCP的价值[18]。

### 工艺开发支持

Valente et al. (2018) 系统回顾了包括无标记定量在内的蛋白质组学方法在HCP表征中的应用：(1) 考察上游因素（细胞系、活力、工艺条件）对HCP谱的影响；(2) 鉴定可能与mAb产物相互作用而共纯化的HCP；(3) 通过培养基组成、温度改变或基因改造限制HCP表达[4]。

### 监管与可比性研究

Reisinger et al. (2014) 开发了基于MS的排除/包含列表策略，用于可比性研究中的靶向HCP检测[15]。Strasser et al. (2021) 建立了自动化样品制备结合DIA LC-MS/MS的方法，用于mAb药品中HCP的检测与定量，实现亚ppm级别的灵敏检测[19]。Guo et al. (2023) 全面综述了LC-MS-based HCP工作流程中样品制备、采集技术和数据分析的进展，强调LC-MS作为ELISA补充工具贯穿产品生命周期的价值[13]。

## iBAQ用于HCP定量的优势

1. **绝对或半绝对定量**：iBAQ值与蛋白摩尔丰度成正比，支持样品内及跨样品比较不同HCP物种[6,9]。
2. **无需同位素标记**：与SILAC或iTRAQ不同，无标记iBAQ避免了代谢或化学标记试剂的成本与复杂度[7,20]。
3. **样品兼容性好**：适用于任何生物样品，无需专门的培养基或标记方案[8]。
4. **动态范围宽**：结合高分辨MS仪器可检测跨越数个数量级丰度的HCP[12]。

## iBAQ的局限性与注意事项

1. **无标准品时无法得到绝对浓度**：iBAQ提供的是相对丰度估计；真正的绝对定量（如ng/mL）需要同位素标记的肽段标准品或QconCAT蛋白[21]。
2. **受蛋白序列覆盖率影响**：理论可观测肽段数取决于酶解效率、漏切和肽段可检测性，这些因素在不同样品间存在差异[11]。
3. **高动态范围挑战**：治疗性抗体（mg/mL级）与HCP（ng/mL级）的悬殊丰度差，要求有效的去除或分级策略[13]。
4. **技术变异性**：批次间与实验室间重现性仍需关注，需要仔细的归一化处理[11]。

## 展望与小结

该领域正趋向于将iBAQ等无标记定量方法与多属性方法（multi-attribute methods, MAM）整合，在单次LC-MS运行中同时评估产品质量属性与HCP杂质[13]。DIA方法（如SWATH-MS）与iBAQ类定量的结合，以及CHO特异性蛋白序列数据库和谱图库的持续完善，有望实现更全面、可重现的HCP监测[4,13]。LC-MS HCP监测正越来越多地与传统的ELISA方法一同纳入监管申报文件[5,13]。

对CMC与分析人员而言，iBAQ的价值在于以可比的摩尔尺度呈现不同HCP物种的丰度全貌，但其定量上限受样品前处理、数据库完整性和仪器稳定性制约。实际应用中应将LC-MS与ELISA互补使用，并在工艺表征与可比性研究中审慎解读定量结果。

## 参考文献

[1] Hogwood, C. E.; Bracewell, D. G.; Smales, C. M. Measurement and Control of Host Cell Proteins (HCPs) in CHO Cell Bioprocesses. Current Opinion in Biotechnology 2014, 30, 153–160. DOI: 10.1016/j.copbio.2014.06.017

[2] Tscheliessnig, A. L.; Konrath, J.; Bates, R.; Jungbauer, A. Host Cell Protein Analysis in Therapeutic Protein Bioprocessing – Methods and Applications. Biotechnology Journal 2013, 8 (6), 655–670. DOI: 10.1002/biot.201200018

[3] Goey, C. H.; Alhuthali, S.; Kontoravdi, C. Host Cell Protein Removal from Biopharmaceutical Preparations: Towards the Implementation of Quality by Design. Biotechnology Advances 2018, 36 (4), 1223–1237. DOI: 10.1016/j.biotechadv.2018.03.021

[4] Valente, K. N.; Levy, N. E.; Lee, K. H.; Lenhoff, A. M. Applications of Proteomic Methods for CHO Host Cell Protein Characterization in Biopharmaceutical Manufacturing. Current Opinion in Biotechnology 2018, 53, 144–150. DOI: 10.1016/j.copbio.2018.01.004

[5] Pilely, K.; Johansen, M. R.; Lund, R. R.; Kofoed, T.; Jørgensen, T. K.; Skriver, L.; Mørtz, E. Monitoring Process-Related Impurities in Biologics–Host Cell Protein Analysis. Analytical and Bioanalytical Chemistry 2022, 414, 747–758. DOI: 10.1007/s00216-021-03648-2

[6] Schwanhäusser, B.; Busse, D.; Li, N.; Dittmar, G.; Schuchhardt, J.; Wolf, J.; Chen, W.; Selbach, M. Global Quantification of Mammalian Gene Expression Control. Nature 2011, 473 (7347), 337–342. DOI: 10.1038/nature10098

[7] Ankney, J. A.; Muneer, A.; Chen, X. Relative and Absolute Quantitation in Mass Spectrometry–Based Proteomics. Annual Review of Analytical Chemistry 2018, 11, 49–77. DOI: 10.1146/annurev-anchem-061516-045357

[8] Neilson, K. A.; Ali, N. A.; Muralidharan, S.; Mirzaei, M.; Mariani, M.; Assadourian, G.; Lee, A.; van Sluyter, S. C.; Haynes, P. A. Less Label, More Free: Approaches in Label-Free Quantitative Mass Spectrometry. PROTEOMICS 2011, 11 (4), 535–553. DOI: 10.1002/pmic.201000553

[9] Arike, L.; Valgepea, K.; Peil, L.; Nahku, R.; Adamberg, K.; Vilu, R. Comparison and Applications of Label-Free Absolute Proteome Quantification Methods on Escherichia coli. Journal of Proteomics 2012, 75 (17), 5437–5448. DOI: 10.1016/j.jprot.2012.06.020

[10] Bubis, J. A.; Levitsky, L. I.; Ivanov, M. V.; Tarasova, I. A.; Gorshkov, M. V. Comparative Evaluation of Label-Free Quantification Methods for Shotgun Proteomics. Rapid Communications in Mass Spectrometry 2017, 31 (7), 606–612. DOI: 10.1002/rcm.7829

[11] Sánchez, B. J.; Lahtvee, P.; Campbell, K.; Kasvandik, S.; Yu, R.; Domenzain, I.; Zelezniak, A.; Nielsen, J. Benchmarking Accuracy and Precision of Intensity-Based Absolute Quantification of Protein Abundances in Saccharomyces cerevisiae. PROTEOMICS 2021, 21 (6), 2000093. DOI: 10.1002/pmic.202000093

[12] Shalit, T.; Elinger, D.; Savidor, A.; Gabashvili, A.; Levin, Y. MS1-Based Label-Free Proteomics Using a Quadrupole Orbitrap Mass Spectrometer. Journal of Proteome Research 2015, 14 (4), 1979–1986. DOI: 10.1021/pr501045t

[13] Guo, J.; Kufer, R.; Li, D.; Wohlrab, S.; Greenwood-Goodwin, M.; Yang, F. Technical Advancement and Practical Considerations of LC-MS/MS-Based Methods for Host Cell Protein Identification and Quantitation to Support Process Development. mAbs 2023, 15 (1), 2213365. DOI: 10.1080/19420862.2023.2213365

[14] Madsen, J. A.; Farutin, V.; Carbeau, T.; Wudyka, S.; Yin, Y.; Smith, S.; Anderson, J.; Capila, I. Toward the Complete Characterization of Host Cell Proteins in Biotherapeutics via Affinity Depletions, LC-MS/MS, and Multivariate Analysis. mAbs 2015, 7 (6), 1128–1137. DOI: 10.1080/19420862.2015.1082017

[15] Reisinger, V.; Toll, H.; Mayer, R. E.; Visser, J.; Wolschin, F. A Mass Spectrometry-Based Approach to Host Cell Protein Identification and Its Application in a Comparability Exercise. Analytical Biochemistry 2014, 463, 1–6. DOI: 10.1016/j.ab.2014.06.005

[16] Park, J. H.; Jin, J. H.; Lim, M. S.; An, H. J.; Kim, J. W.; Lee, G. M. Proteomic Analysis of Host Cell Protein Dynamics in the Culture Supernatants of Antibody-Producing CHO Cells. Scientific Reports 2017, 7, 44246. DOI: 10.1038/srep44246

[17] Chiverton, L. M.; Evans, C.; Pandhal, J.; Landels, A. R.; Rees, B. J.; Levison, P. R.; Wright, P. C.; Smales, C. M. Quantitative Definition and Monitoring of the Host Cell Protein Proteome Using iTRAQ – a Study of an Industrial mAb Producing CHO‐S Cell Line. Biotechnology Journal 2016, 11 (8), 1014–1024. DOI: 10.1002/biot.201500550

[18] Goey, C. H.; Alhuthali, S.; Kontoravdi, C. Host Cell Protein Removal from Biopharmaceutical Preparations: Towards the Implementation of Quality by Design. Biotechnology Advances 2018, 36 (4), 1223–1237. DOI: 10.1016/j.biotechadv.2018.03.021

[19] Strasser, L.; Oliviero, G.; Jakes, C.; Zaborowska, I.; Floris, P.; Ribeiro da Silva, M.; Füssl, F.; Carillo, S.; Bones, J. Detection and Quantitation of Host Cell Proteins in Monoclonal Antibody Drug Products Using Automated Sample Preparation and Data-Independent Acquisition LC-MS/MS. Journal of Pharmaceutical Analysis 2021, 11 (6), 726–734. DOI: 10.1016/j.jpha.2021.05.002

[20] Hogwood, C. E.; Bracewell, D. G.; Smales, C. M. Measurement and Control of Host Cell Proteins (HCPs) in CHO Cell Bioprocesses. Current Opinion in Biotechnology 2014, 30, 153–160. DOI: 10.1016/j.copbio.2014.06.017

[21] Sánchez, B. J.; Lahtvee, P.; Campbell, K.; Kasvandik, S.; Yu, R.; Domenzain, I.; Zelezniak, A.; Nielsen, J. Benchmarking Accuracy and Precision of Intensity-Based Absolute Quantification of Protein Abundances in Saccharomyces cerevisiae. PROTEOMICS 2021, 21 (6), 2000093. DOI: 10.1002/pmic.202000093

## 相关阅读

- [ELISA 方法开发中的稀释线性与平行性：MRD 建立、HCP 专属考量与非线性排查](/posts/elisa方法开发-稀释线性和平行性)
- [宿主细胞蛋白（HCP）的质谱鉴定与绝对定量：从定量标准品、Label-free 算法到样品制备方案](/posts/HCP鉴定与定量)
