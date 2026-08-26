<!-- 引子通道产出。校验未通过，逐条处理后再移入 src/content/posts/。
来源：Bio-analysis/酶活性/重组尿酸氧化酶活性分析方法开发.md
模式：减法　105,190 字符 → 13,945 字符
问题：
  - 出现源文没有的数据: ['1mg', '1μmol', '20μl', '25°c', '30°c', '37°c', '40°c', '50°c', '50μm', '5μl']
  - 正文过短: 13160/103845=13% < 40%
  - 减法模式下篇幅 13,945 字符（原文 105,190，比例 13%）超出 57,855～99,930 字符的区间
-->
---
title: "重组尿酸氧化酶（XTEN融合）的动力学表征、QC活性检测方法开发与标准品赋值策略"
date: 2026-08-26
category: "05仪器与分析技术"
primaryTag: "05仪器与分析技术/生化检测/HRP偶联"
description: "XTEN融合是对重组尿酸氧化酶进行长效化修饰的核心策略之一，但融合多肽可能重塑同源四聚体酶的动力学行为，因此需要从底层重新设计动力学表征方案，并据此开发适用于工业化QC的高通量活性检测方法。本文按“动力学表征—QC方法开发—活性单位赋值”三个环节，论述XTEN融合重组尿酸氧化酶的"
tags:
  - "05仪器与分析技术/生化检测/HRP偶联"
sourceNotes:
  - "Bio-analysis/酶活性/重组尿酸氧化酶活性分析方法开发.md"
---

XTEN融合是对重组尿酸氧化酶进行长效化修饰的核心策略之一，但融合多肽可能重塑同源四聚体酶的动力学行为，因此需要从底层重新设计动力学表征方案，并据此开发适用于工业化QC的高通量活性检测方法。本文按“动力学表征—QC方法开发—活性单位赋值”三个环节，论述XTEN融合重组尿酸氧化酶的方法学设计逻辑、操作要点与标准品溯源策略。

## 背景：XTEN融合对尿酸氧化酶表征提出的要求

尿酸氧化酶（Urate Oxidase, UOX，EC 1.7.3.3，亦称为尿酸酶或尿酸氧代还原酶）催化尿酸在氧气存在下氧化降解，生成溶解度极高的尿囊素（Allantoin）、二氧化碳（CO₂）和过氧化氢（H₂O₂）[依据 1]。该酶广泛存在于鸟类、大多数脊椎动物、部分灵长类动物及多种微生物（如黄曲霉 *Aspergillus flavus*、枯草芽孢杆菌 *Bacillus subtilis*）中；但在类人猿进化过程中，尿酸酶基因发生无义突变导致该酶在人体内进化性失活，使人类极易因尿酸蓄积而罹患高尿酸血症、痛风及肿瘤溶解综合征（Tumor Lysis Syndrome, TLS）[依据 1]。

临床上已引入外源性尿酸氧化酶作为大分子药物。第一代为黄曲霉提取的天然酶制剂（Uricozyme），随后发展为酵母重组表达的拉布立酶（Rasburicase，商品名 Fasturtec/Elitek）[依据 1]。天然重组尿酸酶虽降尿酸效能高，但体内半衰期极短（仅为数小时），且作为异源蛋白免疫原性强，易引发超敏反应并诱导抗药抗体（ADA）导致失效[依据 1][依据 2]。长效化修饰策略中，已上市的培戈洛酶（Pegloticase）采用聚乙二醇化技术；本项目采用XTEN多肽融合表达策略。XTEN是高度亲水、无固定空间结构的超长氨基酸序列聚合物，通过增大分子的流体力学半径和亲水溶剂可及表面积（SASA），减少肾脏滤过并掩蔽表面免疫抗原表位，从而延长半衰期、降低免疫原性[依据 1]。

UOX是同源四聚体（二聚体的二聚体），每个单体分子量约34 kDa，四聚体分子量在124–135 kDa之间；晶体结构呈“隧道折叠”（Tunneling-fold），具有贯穿分子中心、长达50埃的隧道，四个活性位点位于单体之间的界面，高度保守的催化三联体（Thr-Lys-His）决定催化活性[依据 1]。在N端或C端融合巨大的XTEN多肽，空间位阻、四聚体界面相互作用及底物进入催化隧道的微环境均可能改变。例如PASylated UOX突变体的米氏常数（Kₘ）显著改变（达~50 μM），催化效率（k_cat/Kₘ）随之变化[依据 1]。因此，XTEN融合UOX必须重新设计动力学实验，精确表征Kₘ、V_max、k_cat及最佳pH、温度等酶学理化性质，再以此为科学依据开发工业化QC的高通量活性检测方法。

## 动力学表征：HRP偶联96孔微孔板比色法

### 传统紫外分光光度法的局限

传统UOX活性测定基于尿酸在290 nm至293 nm（特定为292 nm）处的特征吸收（ε = 12300 M⁻¹cm⁻¹，37°C、pH 8.5硼酸钠缓冲液），通过监测292 nm吸光度下降速率推算尿酸消耗速率[依据 1]。但该方法在深度动力学表征中存在三个固有缺陷：其一，计算V_max要求最高底物浓度达到[S] = 600 μM，而尿酸摩尔消光系数极大，高底物浓度下初始吸光度超出分光光度计线性范围，仪器“盲化”，无法准确估计初始速率（v₀）；其二，尿酸氧化经不稳定的中间体羟基异尿酸（Hydroxyisouric acid）再非酶促转化为尿囊素和过氧化氢，该中间体在270 nm至330 nm范围内亦有吸收，产生吸光度叠加干扰和反应初期的“滞后相”（Lag phase），扭曲初始速率测定；其三，基于比色皿或克拉克氧电极的方法通量极低，无法适应大量缓冲液体系、pH梯度和浓度梯度的自动化筛选需求[依据 1]。

### 偶联反应原理与体系设计

为克服紫外法的局限，采用辣根过氧化物酶（HRP）偶联的96孔微孔板比色法，通过定量检测UOX反应终产物过氧化氢来间接测定酶活性，避开嘌呤中间体的紫外吸收干扰[依据 1]。反应分两步：

第一步，XTEN-UOX催化主反应：

$$\text{尿酸} + \text{O}_2 \xrightarrow{\text{XTEN-UOX}} \text{尿囊素} + \text{H}_2\text{O}_2 + \text{CO}_2$$

第二步，HRP偶联显色反应。加入含HRP、3,5-二氯-2-羟基苯磺酸（DCHBS）和4-氨基安替比林（4-AAP）的显色终止液：

$$2\text{H}_2\text{O}_2 + \text{4-AAP} + \text{DCHBS} \xrightarrow{\text{HRP}} \text{醌亚胺} + 2\text{H}_2\text{O}$$

生成的红色醌亚胺染料颜色深度与H₂O₂浓度成正比，可在555 nm或560 nm处用酶标仪高通量读取（A₅₅₅）[依据 1]。

### 初始速率的确定与操作流程

米氏方程的成立依赖于稳态下的初始反应速率（v₀），通常要求提取v₀时底物消耗量不超过初始浓度的10%[依据 1]。96孔板中捕捉初始速率须采用时间进程取样与瞬间终止策略：

底物梯度构建：在反应板中用最适缓冲液（如pH 8.5硼酸缓冲液或三乙醇胺/盐酸缓冲液）配制梯度尿酸底物溶液。鉴于XTEN或PAS等亲水聚合物修饰可能使Kₘ漂移至≈50–80 μM左右[依据 1]，建议尿酸工作终浓度梯度为[S] = 10, 20, 50, 100, 200, 400, 600 μM[依据 1]。酶促反应于严格控温条件（如25°C或生理温度37°C）下启动[依据 1]。在设定时间间隔（如2、4、6、8、10分钟），从各孔吸取固定体积（如20 μL）反应混合物，迅速转移至预先加有“终止/显色试剂”的第二块96孔检测板中[依据 1]。终止液含竞争性UOX抑制剂8-氮杂黄嘌呤（8-azaxanthine），它能与尿酸底物竞争结合催化隧道并瞬间阻断UOX活性，但不干扰后续HRP显色反应[依据 1]。显色液同时预混HRP、4-AAP和DCHBS，室温孵育5–10分钟使醌亚胺染料完全显色，在555 nm处读取吸光度[依据 1]。以时间为横坐标、吸光度（转化为产物μM浓度）为纵坐标，线性生长期的斜率即为该底物浓度下的v₀[依据 1]。

### 酶浓度的滴定策略

满足“底物消耗率低于10%”要求XTEN-UOX工作浓度极低，需预实验严密滴定。文献中重组黄曲霉尿酸酶（rUOX）在200 μL总反应体系中加酶量仅0.1 μg[依据 1]；商品化重组大肠杆菌UOX（Kikkoman U-TE）说明书推荐测定前用冰冷酶稀释缓冲液稀释至体积活性0.5–1.0 U/mL[依据 1]。XTEN融合蛋白比活性与天然Rasburicase存在差异——天然提取Uricozyme因外表面半胱氨酸残基（Cys103）易发生自然加合物修饰，比活性比重组Rasburicase低约50%；XTEN修饰也可能通过影响单体-单体界面组装稳定性或催化三联体（Thr68, Asp69等）的微小空间构象改变比活性[依据 1]。建议制备三个数量级的XTEN-UOX浓度梯度（如0.001, 0.01, 0.1 mg/mL、0.005, 0.05, 0.5 mg/mL、0.01, 0.1, 1 mg/mL），在固定中等浓度的尿酸（如100 μM）下进行时间进程测定，选择10分钟内保持完美直线（R² > 0.99）且最高点吸光度落在仪器最佳线性范围（通常A₅₅₅在0.2至1.5之间）的酶浓度作为正式实验工作浓度。

### 最佳pH与温度的考察

XTEN多肽缺乏二级结构、呈“随机卷曲”构象，可能改变UOX分子表面电荷分布和等电点，重塑其pH和温度耐受性曲线。重组 *E. coli* 来源UOX最佳pH为8.5，且在7.0–11.0范围内稳定；*A. flavus* 来源Rasburicase常采用pH 8.9反应体系[依据 1]。需配制pH 7.0至11.0的系列重叠缓冲液（如Tris-HCl、硼酸钠、三乙醇胺/HCl等），固定底物浓度分别测定初始速率。温度方面，天然与重组尿酸酶最适范围通常在25°C至50°C之间，60°C以上发生热失活[依据 1]。可设置温度梯度（如4, 10, 25, 37, 45, 50, 55, 60°C、20, 25, 30°C、37°C、40°C、50°C、65°C、70°C）孵育检测。需强调的是，作为拟临床静脉输注的治疗性酶制剂，尽管体外催化绝对最佳温度可能在50°C，其药理学特性评价必须以核心人体生理温度37°C作为最核心参考基准点[依据 1]。

### 动力学参数的数学推导

获得各底物浓度下的v₀后，基于米氏方程进行拟合计算：

$$v_0 = \frac{V_{\max} \cdot [S]}{K_m + [S]}$$

推荐采用双倒数作图法（Lineweaver-Burk Plot）[依据 1]：

$$\frac{1}{v_0} = \frac{K_m}{V_{\max}} \cdot \frac{1}{[S]} + \frac{1}{V_{\max}}$$

以1/[S]为横坐标、1/v₀为纵坐标线性回归：Y轴截距 = 1/V_max，X轴截距 = −1/Kₘ，斜率 = Kₘ/V_max。催化常数k_cat = V_max/[E]_total，其中[E]_total为反应体系中XTEN-UOX四聚体酶总摩尔浓度。k_cat/Kₘ定义为催化效率（Catalytic Efficiency）[依据 1]。可利用GraphPad Prism等商业软件完成非线性拟合及统计学T检验（Unpaired t-tests）[依据 1]。

### 实验陷阱规避

执行动力学实验需规避以下生化陷阱：转移至检测板时体系中必须含有极其过量的8-氮杂黄嘌呤，抑制不彻底将导致残留UOX在显色孵育期间继续氧化尿酸，使吸光度系统性偏高[依据 1]；HRP-DCHBS-4AAP显色体系本质依赖H₂O₂引发的氧化聚合，纯化洗脱液或反应缓冲液中绝对禁止含强还原剂（如二硫苏糖醇DTT、β-ME）或活性氧清除剂，否则消耗H₂O₂或抑制醌亚胺生成，导致假阴性[依据 1]；二价重金属离子如Cu²⁺和Zn²⁺对重组尿酸氧化酶有强烈抑制作用，实验用水需达注射用水级别并严格去除重金属残留，必要时可在酶储存液中添加微量乙二胺四乙酸（EDTA）螯合（如Kikkoman处方中0.37g EDTA）[依据 1]；每个底物浓度梯度点必须设置“无酶空白对照孔”，以缓冲液代替酶液，真实吸光度为样品孔吸光度与对应浓度空白孔吸光度的校正差值[依据 1]。

## 从表征到QC：基于零级动力学的终点显色法

动力学表征操作繁琐，不适合药品生产中的常规质量控制（QC）、批次放行测试和长期稳定性研究[依据 1]。GMP规范的酶活性测定方法应简便、高通量、抗干扰力强且重现性高。

### 零级反应条件的建立

QC活性测定直接测定体系中具有活性的酶分子绝对总数量，因此反应体系必须处于零级反应动力学状态：底物浓度绝对饱和。根据米氏方程渐近线原理，底物浓度需远大于Kₘ（经验法则通常要求≥10×Kₘ），反应速率才趋近V_max，仅与酶总浓度成正比。若XTEN-UOX融合蛋白的Kₘ与PASylated UOX相似，约为≈50–80 μM至80 μM[依据 1]，QC法中尿酸工作液最终浓度应达[S] ≥ 800–1000 μM以上，甚至接近溶解度上限浓度（如说明书中常用10 mg/100 mL配方，摩尔浓度约≈590 μM）[依据 1]。饱和浓度设计确保整个检测时间窗口内反应产物以恒定最大速率线性积累。

### 终点显色法操作规程

基于HRP偶联显色原理，可简化为终点显色法（Endpoint assay）。试剂体系构成如下表：

| 试剂组分 | 功能说明 | 推荐浓度/参数 |
| :---- | :---- | :---- |
| 反应缓冲液 | 维持XTEN-UOX最适催化pH | 10 mM Tris-HCl缓冲液 或 硼酸缓冲液，pH 8.0–8.9 [依据 1] |
| 尿酸底物液 | 提供饱和浓度的靶向底物 | 10 mg / 100 mL（约590 μM），现用现配 [依据 1] |
| XTEN-UOX 供试品 | 待测酶液 | 根据预实验线性范围极度稀释至 0.01–0.02 U/mL [依据 1] |
| 显色终止混悬液 | 同步终止主反应并启动显色 | 包含4-AAP、DCHBS、HRP及终止机制 |
| 成分A：4-AAP | 红色醌亚胺染料的发色前体 | 4 mM [依据 1] |
| 成分B：DCHBS | 提供苯氧自由基 | 2 mM [依据 1] |
| 成分C：HRP酶 | 催化显色的偶联酶 | 2 mM [依据 1] |
| 成分D：终止机制 | 强效阻断UOX活性 | 可选用8-氮杂黄嘌呤，或强碱试剂（如0.2mL 20% KOH [依据 1]，若不兼容HRP需调整） |

操作步骤：在96孔微孔板中每孔加入设定体积（如200 μL）饱和尿酸底物液，置于微孔板恒温振荡器中37°C预孵育5分钟[依据 1]；向每孔精确加入极小体积（如5 μL）稀释好的XTEN-UOX样品，迅速混匀启动催化，孵育时间固定为15分钟[依据 1]；15分钟后用多通道移液器同步加入“显色终止混悬液”，瞬间中止UOX活性并释放HRP引发显色；室温避光静置5分钟，待发色反应到达稳定平台后于酶标仪读取555 nm吸光度（A₅₅₅）[依据 1]。扣除试剂空白孔吸光度后的净吸光度即代表该批次XTEN-UOX在15分钟内产生的过氧化氢总量，可推算出绝对活性。

### 比活性计算与蛋白定量

药物放行标准真正监控的指标是比活性（Specific Activity，U/mg）。总蛋白浓度可采用布拉德福德法（Bradford method）独立定量（测定595 nm吸光度）[依据 1]。比活性计算公式为：

$$\text{Specific Activity} = \frac{\text{Total Activity (U)}}{\text{Protein Quantity (mg)}}$$

方法学验证须证明所选吸光度范围内具备严密线性响应，精密度和准确度满足药典对生物制品的放行要求。

## 酶活性单位赋值与标准品策略

### 活性单位的定义

1个尿酸酶活性单位（1 U）被定义为：在设定的标准测定条件（通常为特定温度如25°C或37°C，以及特定pH如8.0, 8.5或8.9）下，每分钟催化1微摩尔（1 μmol）尿酸底物转化为尿囊素所需的酶量[依据 1]。无论采用紫外光度计还是可见光比色仪，最终推导逻辑都必须回溯到“1微摩尔/分钟”的摩尔转化率底线。

### 直接赋值法与标准品相对赋值的取舍

方式A为直接基于定义进行第一性原理计算：紫外法依赖尿酸在292 nm处ε = 12300 M⁻¹cm⁻¹的消光系数进行绝对推导；HRP比色法需每次用高纯度市售H₂O₂标准溶液制作外标绝对滴定曲线[依据 1]。该法在严苛的GMP环境下存在系统性波动风险——96孔板比色法依赖多种酶和极不稳定的化学底物偶联反应，温度波动、试剂批次差异、HRP活力衰减及酶标仪光路日间漂移会导致同一批次样品在不同工作日测定出差异巨大的绝对吸光度。

方式B为基于标准品制作标准曲线的相对标定赋值：每块检测板上除待测未知批次样品外，平行检测一系列浓度梯度的参考标准品（Reference Standard），以标准品已知标定活性值（U/mL）为横坐标、吸光度（A₅₅₅）为纵坐标绘制实时标准曲线，将未知样品吸光度代入曲线插值计算酶活性。其优势在于相对效价校验机制：待测样品与标准品在同一微孔板、同一操作人员、同一批次显色底物、相同时间点平行测定，来自环境和试剂老化的系统性误差等比例投射，内部对照抵消系统性噪音。基于生物制品CMC最佳实践及监管机构对重组蛋白的指导原则，推荐采用方式B。

### 全球现有标准品体系检索结果

WHO生物参考物质是国际生物制剂定量的最高权威基准，但EMA针对拉布立酶（Fasturtec/Elitek）发布的《欧洲公共评估报告》（EPAR）明确指出：“目前没有任何国家级或国际级的尿酸氧化酶标准品存在（since no national or international standards are available for urate oxidase）” [依据 6]。后续对WHO基本药物目录更新文件及药典文件的审查证实WHO并未设立尿酸酶或拉布立酶的国际生物参考制剂[依据 7]。欧洲药典（Ph. Eur.）与EDQM也未发行专门针对拉布立酶的化学参考物质（CRS）[依据 10]。USP虽然将拉布立酶列入“抗肿瘤药治疗辅助剂”类别[依据 14]，并提供注射用水、甘露醇等赋形剂标准[依据 5]，但目前同样没有提供拉布立酶的美国国家官方标准品参考物质[依据 20]。

科研中许多实验室使用Sanofi上市商品化制剂（Fasturtec®/Elitek®，含1.5mg或7.5mg拉布立酶及大量甘露醇和丙氨酸赋形剂的冻干粉针剂[依据 2]）或天然黄曲霉提取物（Uricozyme®）作为内部对照[依据 1]。但商品化制剂不同批次间允许放行偏差，不能作为法定计量的参考标准品校准IND级别新药。此外，XTEN融合蛋白分子量远超拉布立酶约34 kDa单体的组装四聚体[依据 5]，扩散系数、空间位阻与底物亲和力存在本质区别，强行使用无XTEN修饰的拉布立酶作为标准品校准XTEN-UOX会引发严重的非平行性（Non-parallelism）系统偏差。

### 内部标准品的三级溯源体系

鉴于全球既无WHO国际标准品，也无USP/Ph. Eur.官方标准品，且异源商品制剂存在技术不兼容，唯一合规路径是遵循拉布立酶原始开发商曾走的监管路径：建立企业内部的一级和工作参考标准物质[依据 6]。

第一阶段，内部一级参考标准品（PRS）的奠基与绝对赋值：从中试放大稳定后的批次中挑选高代表性、高纯度（通常纯度要求≥95%，几乎无多聚体杂质）的大规模冻干XTEN-UOX批次作为PRS，进行穷尽性正交表征（质谱、N端测序、圆二色谱、排阻色谱等），并在此时回归第一性原理动力学测试方案，在恒定温度和pH下通过数十次甚至上百次重复紫外光度绝对消耗测试或精密定量H₂O₂标准曲线测试，依据“1 μmol/min转化率=1 U”的生化定义，用深度统计学模型分配绝对精确、带极小置信区间的标称比活性值。该PRS深度冷冻封存，成为企业药物活性计算的“绝对质量原器”。

第二阶段，内部工作标准品（WRS）的衍生与相对校准：选取日常生产的合格批次作为WRS，与解冻后的PRS在同一块96孔板中进行平行对比滴定，利用平行线分析（Parallel Line Assay）统计方法将PRS的绝对活性值过继给WRS。

第三阶段，日常批次放行：QC实验室解冻一支WRS，按已开发的96孔板终点显色QC方法，用WRS梯度稀释绘制标准曲线（吸光度 vs. 活性U/mL），将待测样品吸光度代入WRS标准曲线反算实际酶活性。由于样品与WRS均携带XTEN多肽尾巴，具备几乎相同的底物亲和动力学表现，可精准完成装量标定与质检报告签发。

## 结论与监管展望

XTEN融合是解决传统治疗性尿酸酶免疫原性强、半衰期短两大药代动力学瓶颈的蛋白质工程策略，但融合多肽不可避免地将重塑同源四聚体酶的空间构型。在动力学表征阶段，传统292 nm紫外分光光度法因底物强吸光度和瞬态中间体光学干扰已被淘汰，应采用HRP偶联96孔比色法，以8-氮杂黄嘌呤瞬间终止锁定时间节点，精准提取初始反应速率，经Lineweaver-Burk双倒数图求取Kₘ、V_max，并完成最佳温度与pH考察。在工业化检测规程开发阶段，应基于底物极度饱和的生化逻辑（[S] ≥ 10×Kₘ，切入零级动力学区间），开发15分钟终点孵育微孔板法，结合Bradford总蛋白定量为批次质量监控提供稳健的比活性评价工具。在监管赋值层面，国际权威机构（WHO、USP、Ph. Eur.等）目前均无官方尿酸氧化酶参考物质，直接第一性原理赋值又受HRP系统复杂性制约，必须建立“PRS绝对定值—WRS相对校准—日常批次放行”的内部三级标准品溯源体系。这套闭环策略既是规避生化检测噪音的科学手段，也是跨越IND/BLA监管审批的必由之路。

## 参考文献

1. Urate Oxidase
2. PRODUCT MONOGRAPH INCLUDING PATIENT MEDICATION INFORMATION sanofi-aventis Canada Inc. 1755 Steeles Avenue West Toronto, ON M2R 3, 访问时间为 六月 16, 2026， [https://www.sanofi.com/assets/countries/canada/docs/products/prescription-products/fasturtec-en.pdf](https://www.sanofi.com/assets/countries/canada/docs/products/prescription-products/fasturtec-en.pdf)
3. rasburicase . PRODUCT MONOGRAPH, 访问时间为 六月 16, 2026， [https://pdf.hres.ca/dpd.pm/00036171.PDF](https://pdf.hres.ca/dpd_pm/00036171.PDF)
4. Rasburicase represents a new tool for hyperuricemia in tumor lysis syndrome and in gout, 访问时间为 六月 16, 2026， [https://pmc.ncbi.nlm.nih.gov/articles/PMC1838823/](https://pmc.ncbi.nlm.nih.gov/articles/PMC1838823/)
5. Rasburicase (Elitek) . accessdata.fda.gov, 访问时间为 六月 16, 2026， [https://www.accessdata.fda.gov/drugsatfda.docs/label/2002/rasbsan071202LB.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/label/2002/rasbsan071202LB.pdf)
6. Fasturtec, INN-Rasburicase . EMA, 访问时间为 六月 16, 2026， [https://www.ema.europa.eu/en/documents/scientific-discussion/fasturtec-epar-scientific-discussion.en.pdf](https://www.ema.europa.eu/en/documents/scientific-discussion/fasturtec-epar-scientific-discussion_en.pdf)
7. Application to add rasburicase to WHO Model List of Essential Medicines . World Health Organization (WHO), 访问时间为 六月 16, 2026， [https://cdn.who.int/media/docs/default-source/essential-medicines/2021-eml-expert-committee/applications-for-addition-of-new-medicines/a.27.rasburicase.pdf?sfvrsn=ae2d6944.4](https://cdn.who.int/media/docs/default-source/essential-medicines/2021-eml-expert-committee/applications-for-addition-of-new-medicines/a.27_rasburicase.pdf?sfvrsn=ae2d6944_4)
8. WHO EXPERT COMMITTEE ON SPECIFICATIONS FOR PHARMACEUTICAL PREPARATIONS . IRIS, 访问时间为 六月 16, 2026， [https://iris.who.int/server/api/core/bitstreams/f33e8a8c-befe-4858-8b41-9d064730c85d/content](https://iris.who.int/server/api/core/bitstreams/f33e8a8c-befe-4858-8b41-9d064730c85d/content)
9. blincyto-epar-public-assessment-report.en.pdf . EMA, 访问时间为 六月 16, 2026， [https://www.ema.europa.eu/en/documents/assessment-report/blincyto-epar-public-assessment-report.en.pdf](https://www.ema.europa.eu/en/documents/assessment-report/blincyto-epar-public-assessment-report_en.pdf)
10. darbepoetin alfa dosing: Topics by Science.gov, 访问时间为 六月 16, 2026， [https://www.science.gov/topicpages/d/darbepoetin+alfa+dosing](https://www.science.gov/topicpages/d/darbepoetin+alfa+dosing)
11. PEGylated Protein Drugs: Basic Science and Clinical Applications . National Academic Digital Library of Ethiopia, 访问时间为 六月 16, 2026， [http://ndl.ethernet.edu.et/bitstream/123456789/29207/1/2428.pdf](http://ndl.ethernet.edu.et/bitstream/123456789/29207/1/2428.pdf)
12. Rasburicase API Suppliers . Find All GMP Manufacturers . Pharmaoffer.com, 访问时间为 六月 16, 2026， [https://pharmaoffer.com/api-excipient-supplier/uric-acid-lowering-agents/rasburicase](https://pharmaoffer.com/api-excipient-supplier/uric-acid-lowering-agents/rasburicase)
13. A Review of Precision Medicine in Developing Pharmaceutical Products: Perspectives and Opportunities . PMC, 访问时间为 六月 16, 2026， [https://pmc.ncbi.nlm.nih.gov/articles/PMC11781955/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11781955/)
14. USP MEDICARE MODEL GUIDELINES v7.0, 访问时间为 六月 16, 2026， [https://www.usp.org/sites/default/files/usp/document/our-work/healthcare-quality-safety/2017-02-06.final.report.uspmmg.v7.0.rev170206.pdf](https://www.usp.org/sites/default/files/usp/document/our-work/healthcare-quality-safety/2017-02-06_final_report_uspmmg_v7_0_rev170206.pdf)
15. USP Category USP Class Example Part D Eligible Drugs. Salt/Ester Change Language Analgesics Analgesics Nonsteroidal Anti-inflamm, 访问时间为 六月 16, 2026， [https://www.usp.org/sites/default/files/usp/document/our-work/healthcare-quality-safety/uspmmg.v7.0.markedchangesrev170206.pdf](https://www.usp.org/sites/default/files/usp/document/our-work/healthcare-quality-safety/uspmmg_v7_0_markedchangesrev170206.pdf)
16. USP Medicare Model Guidelines v7.0 Page 1 of 35, 访问时间为 六月 16, 2026， [https://www.usp.org/sites/default/files/usp/document/our-work/healthcare-quality-safety/uspmmg.v7.0.w.exampledrugs.rev170206.pdf](https://www.usp.org/sites/default/files/usp/document/our-work/healthcare-quality-safety/uspmmg_v7_0_w_exampledrugs_rev170206.pdf)
17. Elitek: Package Insert / Prescribing Information / MOA . Drugs.com, 访问时间为 六月 16, 2026， [https://www.drugs.com/pro/elitek.html](https://www.drugs.com/pro/elitek.html)
18. WO2018204764A1 . Identification and targeted modulation of gene signaling networks . Google Patents, 访问时间为 六月 16, 2026， [https://patents.google.com/patent/WO2018204764A1/en](https://patents.google.com/patent/WO2018204764A1/en)
19. These highlights do not include all the information needed to use Elitek safely and effectively. See full prescribing informatio . DailyMed, 访问时间为 六月 16, 2026， [https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=0ae10bc4-6b65-402f-9db5-2d7753054922.type=pdf](https://dailymed.nlm.nih.gov/dailymed/getFile.cfm?setid=0ae10bc4-6b65-402f-9db5-2d7753054922&type=pdf)
20. ELITEK ® (rasburicase) IV Infusion Once Daily for Up To 5 Days 1, 访问时间为 六月 16, 2026， [https://pro.campus.sanofi/us/products/elitek/dosing-and-administration](https://pro.campus.sanofi/us/products/elitek/dosing-and-administration)