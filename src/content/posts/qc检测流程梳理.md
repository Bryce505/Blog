---
draft: true
reviewNotes:
  - "丢图: ['202201241314544.png']"
  - "出现源文没有的数据: ['5.5']"
  - "丢失文献引用过多: 2/3，允许至多 1 条 ['10.1002/elps.201600519', '10.1016/b978-008045154-1.50025-3']"
title: "QC 放行检测实验室方法手册：蛋白定量、免疫印迹、电泳、内毒素与 SEC-HPLC 操作要点"
date: 2026-08-26
category: "02分子表征"
primaryTag: "02分子表征/Size-variant/SEC"
description: "本文是 QC 放行检测实验室常用方法的综合技术手册，按检测技术模块组织：蛋白浓度测定（Bradford/BCA/Lowry/UV 法）、免疫印迹（Western Blot）、LabChip GXII Touch 微流控蛋白纯度分析、SDS-PAGE、细菌内毒素检测（动态显色法与凝"
tags:
  - "02分子表征/Size-variant/SEC"
sourceNotes:
  - "Antibody-Characterization/QC检测流程梳理.md"
---

本文是 QC 放行检测实验室常用方法的综合技术手册，按检测技术模块组织：蛋白浓度测定（Bradford/BCA/Lowry/UV 法）、免疫印迹（Western Blot）、LabChip GXII Touch 微流控蛋白纯度分析、SDS-PAGE、细菌内毒素检测（动态显色法与凝胶法）以及 SEC-HPLC。每个模块覆盖原理、试剂配制、关键操作参数与注意事项，供方法建立与日常检测参考。

> [!abstract] 摘要
> 本笔记是 QC 放行检测实验室常用方法的综合技术手册，系统整理了蛋白浓度测定（Bradford/BCA/Lowry/UV法）、Western Blot 免疫印迹、LabChip GXII Touch 微流控蛋白纯度分析、SDS-PAGE 电泳、细菌内毒素检测（动态显色法与凝胶法）以及 SEC-HPLC 等多项 QC 检测技术的原理、试剂配制和标准操作流程。

> [!summary] 核心要点
> - 蛋白浓度测定：对比 Bradford、双缩脲、Lowry（Folin-酚）、BCA 四种比色法及 UV280/UV205 光谱法的原理、适用范围与干扰因素。
> - Western Blot：详述转膜方法、缓冲液体系、显色检测原理（化学发光/荧光/显色）及完整实验操作流程与troubleshooting。
> - LabChip GXII Touch：微流控毛细管电泳原理（芯片intersection稀释SDS）、Protein Express/Clear HR等assay类型及完整试剂准备、上机、清洁维护流程。
> - SDS-PAGE：Tris-glycine/Bis-Tris/Tris-acetate/Tricine等凝胶化学体系比较、样品制备与染色成像流程。
> - 内毒素检测：动态显色法（kinetic assay）与凝胶法（gel-clot）的原理、标准曲线制备、结果判定及干扰试验。
> - SEC-HPLC：色谱柱选择、系统适用性试验（理论塔板数、分离度、拖尾因子）、定性定量方法及操作参数。

## 蛋白浓度测定：方法对比与选择

### 方法体系概述

常用于蛋白定量的四种方法：

- 蛋白质侧链或肽键的紫外光吸收
- 碱性条件下，在蛋白质和亚铜离子（双缩脲反应）之间形成的复合物的生色反应
  - BCA法：干扰物为糖和还原试剂
- 发色团与蛋白质的结合
  - Bradford法：干扰物为去污剂和氢氧化钠
- 斑点印迹和染色

![image-20211228155823044](/images/qc检测流程梳理/202112281558188.webp)

### Bradford 法

考马斯亮蓝（G-250）属于结合型染料，在溶液中有三种形式：阳离子形式（略带红色的褐色）、中性形式（呈绿色）、阴离子形式（呈蓝色）。考马斯亮蓝在检测到的酸性条件下为棕红色，最大光吸收在465nm；当它与蛋白结合后变成蓝色阴离子，蛋白质-考马斯亮蓝结合物在595nm波长下有最大吸收，其吸收值与蛋白质含量成正比。

![image-20211229084511376](/images/qc检测流程梳理/202112290845441.webp)

试剂盒：Better Bradford Assay Kit（含 G250 溶液及标准蛋白 BSA 2mg/ml），货号 23236，Thermo。

测定范围：0.1-1.5mg/ml。优点：最低检出量1ug；染料与蛋白结合快，只需要2min，结合物的颜色1h内是稳定的。干扰物：大量的TritonX-100，SDS。

**standard Bradford**

| No | 1xPBS(ul) | BSA体积(ul) | 最终浓度（mg/ml) |
| --- | --------- | ----------- | ---------------- |
| A | 25 | 75 2mg/ml BSA | 1.5 |
| B | 100 | 100 2mg/ml BSA | 1 |
| C | 100 | 100 B | 0.5 |
| D | 100 | 100 C | 0.25 |
| E | 100 | 100 D | 0.125 |
| F | 100 | 100 E | 0.0625 |
| G | 100 | 100 F | 0 |

5ulsample/blank/standard + 150ul regeant，mix 10s，RT放置10min，再检测；数据处理和计算用二项式拟合，并计算浓度。

**micro-standard**

| No | 1xPBS(ul) | BSA体积(ul) | 最终浓度（mg/ml) |
| --- | --------- | ----------- | ---------------- |
| A | 100 | 100 2mg/ml BSA | 1000 |
| B | 450 | 50 A | 100 |
| C | 150 | 50 B | 25 |
| D | 200 | 50 B | 20 |
| E | 170 | 30 B | 15 |
| F | 450 | 50 B | 10 |
| G | 380 | 20 B | 5 |
| H | 390 | 10 B | 2.5 |
| I | 150 | 0 | 0 |

50ul样品+50ul 试剂，混合10s，RT放置10min，再检测。

### 铜离子还原法：双缩脲、Lowry 与 BCA

这一类方法的固有缺点：很容易受到还原剂和铜离子螯合剂的干扰。

**双缩脲分析法**：将蛋白质在碱性条件下置于含有铜的溶液时，在蛋白质的肽键和铜离子间能形成有颜色的复合物。产生蓝紫色的是一个有四个氮原子的四配体复合物形成的结果。颜色的形成可用分光光度计在540nm处监测。缺点：缺乏灵敏度，双缩脲试剂不稳定。

![image-20211228172219801](/images/qc检测流程梳理/202112281722874.webp)

**Folin-酚试剂法（Lowry法）**：蛋白质中主要的生色物质是肽的联结，以及半胱氨酸、胱氨酸、酪氨酸和色氨酸的侧链，把二价铜离子还原成一价铜离子，一价铜离子与磷钼/磷钨酸结合，监测750nm处的光度值；磷钼/磷钨酸能提高灵敏度10倍。灵敏范围在5-100ug/ml。目前国内外多数重组蛋白制品原液蛋白含量用该法进行测定。

![image-20211228173106870](/images/qc检测流程梳理/202112281731939.webp)

注意事项：蛋白质与铜反应是在碱性条件进行的，添加磷钼/磷钨酸到碱性溶液中，必须立即混匀。此法非常适用于浓度范围0.01-1.0mg/ml的蛋白质溶液。缺点：碱性铜离子试剂不稳定，需现配现用；受多种物质干扰。优点：灵敏度高，较UV法灵敏10-20倍；不同蛋白间的变异少。

**BCA法**：在碱性条件下基于二价铜离子到一价铜离子蛋白质还原的依赖铜的方法。蛋白中肽键、半胱氨酸、胱氨酸、色氨酸和酪氨酸残基的侧链能够将二价铜离子还原成亚铜离子。亚铜离子可以通过与BCA反应（一个Cu<sup>+</sup>螯合两个BCA分子）检测到，后者是一种水溶性铜离子螯合剂。深紫色的反应产物（在562nm处检测）是由两分子BCA和一个亚铜离子相互作用产生的。BCA工作试剂在碱性条件下与蛋白质结合时，蛋白质将Cu2+还原为Cu+，工作试剂由原来的苹果绿形成紫色复合物，在562 nm处有高的光吸收值并与蛋白质浓度成正比。

![image-20220413165615620](/images/qc检测流程梳理/202204131656720.webp)

BCA法不是真正的终点法，显色会继续发展；但孵育后显色速率足够慢，可允许大批量样品一起测定。优点：BCA工作试剂比Lowry试剂稳定得多，且不需要现配现用，是目前最常用的基于铜离子的检测蛋白质含量的方法。working range：20-2000ug/ml。

BCA Protein Assay Kit & 1L kit（含检测 A、B 液及标准蛋白 BSA 2 mg/ml），货号 23225，Thermo。

| No | 1xPBS(ul) | BSA体积(ul) | 最终浓度（mg/ml) |
| --- | --------- | ----------- | ---------------- |
| A | 25 | 75 2mg/ml BSA | 1.5 |
| B | 100 | 100 2mg/ml BSA | 1 |
| C | 100 | 100 B | 0.5 |
| D | 100 | 100 C | 0.25 |
| E | 100 | 100 D | 0.125 |
| F | 100 | 0 | 0 |

工作液配制：500ul A液+10ul B液，混匀，两天内用完。检测：7ul样品+200ul工作液，mix 30s，37℃孵育30min，然后室温冷却，检测562nm吸光值。检测范围：125-2000ug/ml；线性。

### UV 光谱法（A280 与 A205）

在190-310nm的近紫外区域，蛋白质的有效吸收光有两个最大值，280和200nm。

**A280处的紫外吸收**：含有芳香环侧链的氨基酸包括酪氨酸、苯丙氨酸、色氨酸和组氨酸。如果蛋白质序列已知，理论摩尔吸光系数可以用下公式计算：

ε=5500x#Trp+1490x#Tyr+125x#Cys 氨基酸数目

Lambert-Beer定律：A=a*c*l

- 摩尔吸光系数（ε）：在280nm下，1mol/ml溶液用1cm的光径的吸光度
- 百分比吸收系数（E1%）：在280nm下，1%溶液（1g/100ml）用1cm的光径的吸光度；E0.1% 常用。ε=M/10*E1%

**Concentration calculation**：

![image-20220413161043342](/images/qc检测流程梳理/202204131610424.webp)

**常用sample类型**：

![image-20220413161955061](/images/qc检测流程梳理/202204131619160.webp)

**仪器类型**：

1. Nanodrop：光程是1mm和0.05mm光程；软件会自动将检测到的吸光度转换成10mm光程对应的吸光度，浓度通过A280除以消光系数计算得到
2. 传统分光光度计：10mm光程；吸光度范围0.3-0.7最佳
3. Lunatic：板式双孔芯片 0.1 和 0.7 mm；板式单孔芯片 0.5 mm；波长范围230–750 nm；浓度检测范围：0.02–200 mg/mL。光程越短，测量高浓度样品而不饱和内部检测器的能力越强，从而扩展仪器的吸光度范围

![image-20220413163236708](/images/qc检测流程梳理/202204131632812.webp)

**Corrections**：对光散射伪影造成的任何基线偏移进行校正，基线归一化默认波长为340 nm。

**样品是否适合A280检测**：用ddH2O做blank，然后测sample buffer，要求结果光谱在280nm处相对基线的波动不超过0.04 absorbance（10 mm absorbance equivalent）。

**Control**：2μg/mL Bovine Serum Albumin solution 是日常监测重现性和日间值的常规实验室对照。

**干扰物列表**：

![image-20211228163608646](/images/qc检测流程梳理/202112281636744.webp)

可以用不同波长处测量蛋白质溶液的吸光度来解决：C（mg/ml）=（A235-A280)/2.51

尽管280nm处的适中吸光度可以通过重新调整分光光度计的零点设置来平衡，大多数设备由于偏离光的干扰在高吸光度（≥1）时灵敏度还是会有一个限制范围。建议避免使用280nm处总吸光度（buffer+蛋白）大于1.5的溶液。需要强调的是，将空白缓冲液的280值设定为零并不能消除缓冲液对蛋白质溶液总A280值的影响。

**A205处的紫外吸收**：肽键低于210nm时吸收光子。205nm处的蛋白质检测比280nm处至少灵敏10倍多。

### 斑点印迹与 SDS-PAGE 快速估算

用于初步估算蛋白浓度。

- Western 斑点印迹：在没有预先分离的情况下，将样品通过膜或者滤纸，特定的蛋白质的量就能用免疫学来测定。蛋白质的定量可以通过使用待测蛋白质所特有的抗体来完成
- SDS-PAGE：同一凝胶中加入不同浓度的标准蛋白作为样品，考马斯亮蓝显影

## 免疫印迹（Western Blot）

### 转膜与检测原理

**转膜方法**：扩散印迹（diffusion blotting）；电转印（electrotransfer），包括湿转（wet transfer）、半干转（semi-dry transfer）、干转（dry transfer）。

**转膜缓冲液**：

- Towbin buffer system：25 mM Tris-HCl, pH 8.3, 192 mM glycine, 20% (v/v) methanol
- CAPS buffer system：10 mM CAPS, pH 10.5, 10% (v/v) methanol

一般不含SDS，跟蛋白结合的SDS足够transfer蛋白到膜上。

**检测方式对比**：

- 化学发光（Chemiluminescence）：检测到的光信号是酶-底物反应的瞬时产物。底物由所选择的报告酶决定：luminol-和acridan-based试剂用于化学发光HRP检测；acridan-和1,2-dioxetane-based试剂用于AP检测
- 荧光检测（fluorescent detection）：激发后荧光基团返回基态释放光子产生的瞬时光发射。检测限虽不如化学发光低，但独特优势是可以在同一张印迹膜上同时检测多个靶标
- 显色检测（chromogenic detection）：产生稳定、有色的产物。HRP底物与AP底物（NBT、BCIP）均可

![image-202204151309471](/images/qc检测流程梳理/202204151309471.webp)

![image-202204151318228](/images/qc检测流程梳理/202204151318228.webp)

![image-202204151326887](/images/qc检测流程梳理/202204151326887.webp)

![image-202204151329288](/images/qc检测流程梳理/202204151329288.webp)

**检测标记**：酶标记（AP、HRP）；荧光标记；生物素结合蛋白作为探针。

**洗膜**：目的是去除未结合或弱结合的试剂、降低背景、提高信噪比。洗涤不充分产生高背景，过度洗涤可能因抗体或靶蛋白从膜上洗脱而降低灵敏度。

![image-202204151304113](/images/qc检测流程梳理/202204151304113.webp)

**细胞裂解**：使用 M-PER™ Mammalian Protein Extraction Reagent，货号 78501。悬浮培养哺乳动物细胞裂解流程：2500 × g 离心 10 分钟收集细胞，弃上清；用 wash buffer（如 PBS）重悬洗涤一次，2500 × g 离心 10 分钟；每 100mg（~100µL）湿细胞沉淀加入至少 1mL M-PER Reagent（2 × 10<sup>6</sup> 个 HeLa 细胞约等于 10µL 沉淀体积，即 20mg 细胞，需 200µL M-PER Reagent；100mg 湿细胞沉淀的总蛋白产量约为 6mg，取决于细胞类型）；轻轻摇动 10 分钟，~14,000 × g 离心 5-10 分钟去除细胞碎片；转移上清至新管分析。

### 试剂配制

1）Wash buffer 洗膜液：

5×PBST：按照5×PBS：Tween 20=1000:3制备

| 试剂 | 10x | 5x |
| --- | --- | --- |
| Na2HPO4 | 56mM | 23mM |
| KH2PO4 | 10.58mM | 5.29mM |
| NaCl | 1.54M | 0.77M |

5XPBST配方：

| 试剂 | 重量 |
| --- | --- |
| Na2HPO4 | 3.265g |
| KH2PO4 | 0.72g |
| NaCl | 44.998g |
| 吐温20 | 3ml*1.11g/ml=3.33g |

1×PBST：5×PBST用纯水稀释到1×PBST；1×PBST也可按1xPBS：Tween 20=5000:3制备（如果没有5xPBS）。

2）1×PBS：5×PBS用纯水稀释到1×PBS。

3）1×平衡液：将10X平衡液用纯化水稀释到1X平衡液。

4）1X转印液：将10X转印液用纯化水稀释到1X。

5）5%牛奶：50 g奶粉加1×PBST，定容到1 L。

6）快速封闭液：快速封闭A液和B液按照1：1混合后使用。

7）抗体的配制：

- 粉末类抗体：根据抗体包装瓶上的抗体量，用50%的甘油将抗体稀释为浓度为1ug/ul，待用
- 溶液类抗体：直接使用

loading buffer：

- 5xR loading buffer：300mM Tris，30%甘油（v/v)，10% SDS，0.5%溴酚蓝，250mM DTT，pH6.8
- 5xN loading buffer：250mM Tris，30%甘油（v/v），5%SDS，0.5%溴酚蓝，250mM IAM，pH8.2

### 操作流程

**制备上样表**：在MES系统QC检测（蛋白）中，下载收样表，把需要WB检测的订单复制到WB和跑胶上机表中，打印。跑胶用12孔道胶；第一个和或最后一个孔道加阳参。

![image-20220202220210431](/images/qc检测流程梳理/202202022202507.webp)

![image-20220202220352261](/images/qc检测流程梳理/202202022203330.webp)

**样品准备**。上样量：重组蛋白 R 140ng、N 400ng；抗体 R 3ug、N 80ng。NR 不用煮样；R 需要煮样。Marker 使用 WB-MASTER Protein Standard，直接使用，不用煮样，使用量在2.5-10ul。

![image-20220202221508489](/images/qc检测流程梳理/202202022215561.webp)

![](/images/qc检测流程梳理/202204150913899.webp)

阳参：人抗 human IgG1,Kappa（sigma，货号 I5154）；鼠抗 mouse IgG1,kappa（sigma，货号 M9269）。

**上样和跑胶**：

1. 电泳缓冲液：现配的1xMOPS，加满内槽；外槽不能冒过内槽，但不能低于内槽的2/3
2. 上样：一次上样体积不能超过40ul，超过40ul要压胶；最大上样体积60ul
3. 正负极连接正确，预制胶145v，恒压45min；溴酚蓝到达分离胶底部上方约1cm，关掉电源

**转膜**：

1. PVDF膜裁剪：大小 6.5cmx8.7cm，裁剪戴手套，避免污染
2. PVDF膜活化：用乙醇浸泡5-10s，直到PVDF膜呈半透明状态；标记正面：

| 标签 | 标记简称 |
| --- | --- |
| His | H |
| Gst | G |
| Strep | S |
| Flag | F |
| Rabbit | R |
| human IgG Kappa | HK |
| human IgG lambda | HL |
| mouse IgG Kappa | MK |
| mouse IgG Lambda | ML |

3. 转印液：用10x转印液稀释到1x
4. PVDF膜平衡：将激活的PVDF膜放入10ml 1x转膜液中，平衡2min
5. 凝胶浸润和平衡：取出凝胶板，先短板向上，从边撬开，再反过来，从边撬开；将电泳好的凝胶，轻轻刮掉距离胶孔1cm以上的浓缩胶，把胶放入装有纯水的托盘中，浸润1min；再用eblot L1平衡液（1x）平衡胶
6. 转膜：打开转膜夹，阳极靠近桌面，平铺实验桌面上，在标记为+侧平铺1张干海绵垫，将PVDF膜从转印液中取出，平铺在干海绵垫上（标记面朝上），然后将SDS-PAGE凝胶平铺于PVDF膜上（胶孔对准转膜夹里侧），并用转印液去除气泡，在凝胶上平铺一张干海绵，合上转膜夹。将转膜夹有Front字样面对自己，插入仪器泳道，开始转膜

![image-20220202224032495](/images/qc检测流程梳理/202202022240588.webp)

7. 洗膜：将转印完成的PVDF膜标记面朝上放置在膜盒里，在膜盒倒入10ml的1xPBST溶液洗膜，摇床摇动5min，弃掉1xPBST溶液
8. 封闭：加入10ml（5%脱脂牛奶），摇床上摇动1h，转速60rpm，或者4℃静置过夜；快速封闭液（A:B=1:1），室温5-10min，40rpm
9. 洗膜：封闭结束后，弃掉封闭液，加入1xPBST溶液在摇床上洗膜2次，每次5min，转速60rpm，弃掉1xPBST溶液

方法一（一抗二抗分开孵育）：

10. 孵育一抗：用5%脱脂牛奶进行稀释一抗，摇60min，40rpm
11. 洗膜：加入1xPBST溶液在摇床上洗膜3次，每次5min，转速60rpm，弃掉1xPBST溶液
12. 孵育二抗：用5%脱脂牛奶进行稀释二抗，摇50min，40rpm
13. 洗膜：加入1xPBST溶液在摇床上洗膜4次，每次5min，转速60rpm，弃掉1xPBST溶液

方法二（一抗二抗一起孵育）：

14. 根据蛋白标签或者蛋白本身选择一抗和二抗，按照比例同时加入10ml脱脂牛奶中，混匀
15. 将抗体缓冲液，室温摇床孵育60min
16. 洗膜：1XPBST，洗膜4-5次，每次5min

**显色成像**：打开仪器，仪器CCD自动制冷，点击begin；打开imaging system，取出sample tray（黑色底板），将洗膜完成的膜平铺在sample tray上（一次最多放四张），PVDF膜标记面朝上；往膜上均匀滴加配制的ECL A、B混合液至整张膜都覆盖上，将sample tray推进仪器，关上仪器外盖；Live view 参数：image size 可选 small、medium、large三种；application选择印迹检测-western blot，化学发光选择chemiluminescence，exposure选manual，曝光5s-100s，曝光张数6张。

### 阳参选择与数据要求

1. Mutiple-tag（genscript cat.no M0101)：先用200ul的纯化水溶解冻干粉，使其浓度为1mg/ml，再用5xloading buffer稀释100倍，使其终浓度为0.01mg/ml；用作His，HA阳参时，上样量5ul，用作flag阳参时，上样量10ul
2. human IgG1,Kappa（sigma，货号 I5154）；mouse IgG1,kappa（sigma，货号 M9269）；IgG from rabbit serum（sigma，货号 I5006）
   - 人/鼠阳参（R）：原始蛋白浓度为1mg/ml，用5x还原loading buffer稀释5倍，使其终浓度为0.2mg/ml，上样量10ul
   - 人/鼠阳参（NR）：原始蛋白浓度为1mg/ml，用5x非还原loading buffer稀释50倍，使其终浓度为0.02mg/ml，上样量4ul
   - 兔阳参：原始蛋白浓度为10mg/ml，用5x还原loading buffer稀释50倍，使其终浓度为0.2mg/ml，上样量10ul

数据要求：

- 选择条带信息清晰可见的曝光图片，使用 photoshop 软件标注泳道序号及每个泳道对应的样品名称，图片右下方写明曝光时间

![image-20211222165613650](/images/qc检测流程梳理/202112221656916.webp)

- 原始图片marker以及阳性对照清晰，无背景或弱背景
- 原始图片按照日期保存

常用对照品一抗二抗信息参考表：

![image-20220202224642799](/images/qc检测流程梳理/202202022246906.webp)
![image-20220202224707986](/images/qc检测流程梳理/202202022247084.webp)
![image-20220202224723399](/images/qc检测流程梳理/202202022247482.webp)

### Troubleshooting

1. 蛋白印迹阻断：印迹膜对蛋白质具有高亲和力；需阻断任何剩余的结合位点以防止随后的测定检测抗体的非特异性结合，一般用牛奶
2. 印迹洗涤：确保膜被适当的缓冲液充分覆盖，TBST/PBST。清洗不充分/不均匀，导致质量差斑块印迹和高背景；过度洗涤减少目标信号；优化点为洗涤的数量和持续的时间
3. 印迹抗体：直接检测用单一抗体；间接检测用一抗+二抗（种属特异性），注意正确的抗体和最佳的浓度
4. 印迹分析：放射性/比色/化学发光/荧光
5. 分离不充分/不佳：优化预制胶百分比和跑胶时间
6. 印迹无任何东西：确保印迹时胶和膜的位置正确；电流方向正确
7. 印迹看起来凌乱、斑驳：确保转移时凝胶和膜之间无气泡，确保膜完全浸没在孵育和洗涤溶液中；使用新鲜的封闭试剂
8. 高背景：封闭或洗涤可能不够
9. 对照品结果与预期结果不一致：优化抗体选择/浓度，减少非特异性/脱靶结合
10. 条带太亮/太暗：优化显影时间；条带太亮也表明洗涤过度

![image-202204151338755](/images/qc检测流程梳理/202204151338755.webp)
![image-202204151338970](/images/qc检测流程梳理/202204151338970.webp)
![image-202204151339915](/images/qc检测流程梳理/202204151339915.webp)
![image-202204151339263](/images/qc检测流程梳理/202204151339263.webp)

## LabChip GXII Touch 微流控蛋白纯度分析

### 芯片原理

LabChip 基于传统凝胶电泳原理。样品通过 sipper 吸取，通过压力（在1号孔施加negative pressure）或电压方式吸取，marker和样品进入channel后，3号孔和8号孔间施加电压（injection voltage），推动样品往右边移动；竖向channel（7号和10号孔间）与横向channel间有一个intersection，当样品经过这个intersection时，在7号和10号孔间施加injection voltage，被竖向channel里的离子推动往前走（只有一小部分样品，大概25pL），经过一个较长的separation channel（在含SDS的情况下，分离泳道长度大概1.25cm），在这个过程中充分分离；横向channel（2号孔和9号孔，不含染料和SDS的凝胶）与竖向channel（7号和10号孔间）汇聚在一起，形成第二个intersection，SDS被不断地稀释，稀释到cmc以下（SDS的临界胶束浓度1.7mM，有分离胶的情况下），此时凝胶中无SDS胶束，原先SDS胶束中的染料被释放出来，与蛋白-SDS复合物结合，蛋白-SDS复合物继续往前迁移，到达检测窗口，激光照射，染料被激发，发出激发光而被检测到。

以上过程整合在一个微小的芯片上，集分离、染色、脱色和检测于一体。分离后的电泳稀释步骤（electrophoretic dilution step）运用一个intersection来稀释SDS，使其浓度低于cmc（在检测前），大大降低背景信号，同时增加蛋白信号一个数量级（更多的染料结合到蛋白上）。

机械臂（robotic stage）将样品孔依次对准芯片的sipper。芯片cartridge可对芯片上各孔施加压力或电压：1号孔施加真空，将样品吸入sipper并与染料和marker混合；3号孔和8号孔之间施加交叉进样电压（cross injection voltages）；7号孔和10号孔之间施加进样电压（injection voltages），将皮升级样品塞注入分离通道，通过筛分基质按大小进行电泳分离。通过2号孔和9号孔施加负电压产生流向10号孔的电流，实现自动脱色，去除背景荧光，而与蛋白胶束结合的染料在激光照射下保持明亮。检测到的荧光绘制成电泳图（electropherogram）。

![img](https://media.springernature.com/original/springer-static/image/chp%3A10.1007%2F978-1-4939-9024-5_20/MediaObjects/432279_1_En_20_Fig10_HTML.png)
![image-20220115080500621](/images/qc检测流程梳理/202201150805589.webp)
![image-20220115080617717](/images/qc检测流程梳理/202201150806683.webp)

**蛋白分子量测定方法比较**：SDS-PAGE 传统方法耗时耗力；毛细管凝胶电泳（SDS-CGE）仍耗时，且 UV 检测不够灵敏（280nm；220nm和200nm高背景吸收）。荧光标记分共价标记和非共价标记：共价标记耗时、标记后需要纯化、蛋白上标记的荧光分子数量可变、标记效率取决于反应；非共价荧光标记结合到SDS-蛋白复合物上，为克服高荧光背景，在微流路中添加intersection channel用于SDS稀释。

芯片中的channel尺寸：13um deep，36um wide。染料：SYPRO Orange（excited at 300 nm and emits at 470 nm）或者Agilent dye（excitation/emission 650/680 nm），这些染料结合到SDS上，而非特定的氨基酸上。基于聚丙烯酰胺的筛分基质可以减少电渗流（EOF），原因为粘性增加聚合物对毛细管壁的吸附，因此在芯片使用过程中，溶液在芯片中流动不明显，主要是离子的电泳运动。

**定量与分子量**：marker浓度已知，与样品混合后一同分离，通过marker峰面积与未知峰的比值直接确定浓度；分子量大小通过与sizing ladder比对确定。

### 试剂与耗材

**Protein芯片及其试剂**：

- HT Protein Chip（PN760499）& Reagent Kit（PN CLS960008）& SAMPLE BUFFER（25ml, PN760518）
- 分离范围 14-200KDa，线性范围 5-2000 ng/μL，最大浓度 10 mg/mL（总蛋白）

![image-20220102101945544](/images/qc检测流程梳理/202201021019637.webp)
![image-20220102171146929](/images/qc检测流程梳理/202201021711024.webp)
![image-20220102102052536](/images/qc检测流程梳理/202201021020603.webp)
![image-20220102102301553](/images/qc检测流程梳理/202201021023651.webp)
![image-20220102102359705](/images/qc检测流程梳理/202201021023774.webp)

**板与耗材**：96孔或384孔全裙边PCR板（PerkinElmer 6008870；ABgene AB-0800；BioRad HSP-9631，SAP: DK0800040）；1M DTT（dithiothreitol）；control sample：BSA；0.6 mL离心管和/或96孔板，用于蛋白样品变性。

**耗材价格**：

|  | Protein Express |  |
| --- | --- | --- |
| 760499 | HT PROTEIN EXPRESS LABCHIP Contains: 1 Protein Chip for 400 Samples | ¥7,575 |
| 760528 | HT PROTEIN EXPRESS LABCHIP Contains：4 protein chips |  |
| CLS960008 | HT Protein Express Reagent Kit, Dual Protocol | ¥3,620 |
|  | **Protein Clear HR** |  |
| CLS148695 | HT Protein Clear HR LabChip Contains: 1 Protein Chip for 400 Samples | ￥10,752.00 |
| CLS960014 | HT Protein Clear HR Reagent Kit, Dual Protocol | ￥6,405.00 |
|  | **ProteinEXact** |  |
| CLS150466 | ProteinEXact assay reagent kit |  |
| CLS150337 | ProteinEXact Assay HT LabChip |  |

**仪器价格**：

![image-20220102204830030](/images/qc检测流程梳理/202201022048108.webp)

**应用**：Protein Express Assay、Protein Exact assay、pico protein assay、Low MW Protein Express Assay、Protein Clear HR Assay、Protein Charge Variant Assay、Glycan Profiling Assay。

**上机前准备**：

1. Clean the electrodes and the O-Rings
2. Purging the Pressure Lines：正压去除管线中的潜在液体或碎屑，每天开始、插入芯片前执行
3. Calibrating（仅Protein Clear HR assays）：处理已知蛋白样品，精确设置该assay的电极电流以保证芯片间结果的一致性，选择plate type、assay和Verimab sample孔的位置；Protein Express此步省略
4. Priming the Chip Before the Run（跑前注胶）：耗时20min；插入芯片，放入buffer tube、ladder tube，选择assay类型
5. Prepare the sample plate, ladder, and buffer for the assay
6. 如需要，在Tools>Plate Editor>custom plates tab>add plate中定义新板类型，注意输入错误值会导致芯片和吸头（sip）损坏，严格按照板子供应商提供的规格设置。sip height最小2.5mm，4mm是安全高度，最大取决于样品体积
7. Load the Sample Plate, Ladder tube, and Buffer tube into the instrument

**运行**：Define the parameters of the assay run（home>run>select assay>select plate type>Selection Sip Order）→ Monitor the run → Remove the Plate, Buffer Tube, and Ladder Tube → unload, wash, store the chip

### 样品准备（Protein Express Assay）

关键参数：heating time、heating temperature、sample buffer volume、protein load、dye concentrations。Sample buffer volume被发现显著影响mAb在还原和非还原条件下的纯度结果。

![image-20220115223149548](/images/qc检测流程梳理/202201152231265.webp)

**样品变性溶液（Sample Denaturing Solution）**：

1. 取 700 μL HT Protein Express Sample Buffer（白色管盖）到 2.0 mL离心管中
2. 如果要做还原样品检测，取 24.5 μL DTT (1M in water)，混匀，离心
3. Sample Denaturing Solution的量足以制备96个样品，如果样品数量只有48个或更少，用量减半
4. NR检测：24.5ul IAM（250mM in water)；R检测：24.5ul DTT (1M in water)

**样品和ladder准备**：

注意：样品和buffer使用前必须经0.22um过滤，防止颗粒堵塞芯片；样品中的盐浓度不能超过1M。

1. 对于每一个待分析样品，取 7μL Sample Denaturing Solution 到微孔板的孔里或 0.6 mL离心管中
2. 取 2μL 蛋白样品到上述微孔板或离心管中，使buffer和样品充分混匀。然后可以贴上封口膜或锡箔纸或者盖上管盖以减少蒸发；DTT浓度26mM（如果采用High Sensitivity Assay，则取 5μL 蛋白样品）
3. HT Protein Express Ladder 室温平衡 15-20 分钟后，votex 10 秒。取 12μL 加入到单独的离心管中。不要向Ladder加入变性液
4. 加热变性：将加入了变性液的样品和Ladder于 70℃ 加热 5 分钟。短暂离心，使液体收集于孔底/管底（具体温度取决于样品）
5. 向Ladder中加入 120μL 水，votex数秒使之充分混匀
6. 向每个样品孔或样品管中加入 35μL 水，混匀离心管。在开始分析前1小时内再进行此步骤（如果运行High Sensitivity Assay则加入 32μL 水）
7. 如果样品在离心管中制备，将其以 44μL /孔分装至孔板内，3000 rpm for 5 minutes离心排除气泡
8. 取 120μL 制备好的Ladder转移至 0.2 mL Ladder Tube中。将Ladder Tube插入仪器相应的Ladder插孔中

**Wash Buffer**：加入 750μL HT Protein Express Wash Buffer（紫色管盖）到试剂盒提供的Buffer Tube中；将Buffer Tube插入到仪器相应Buffer插孔中。

样品溶液准备：

| NO | step | reagent | Normal assay(ul) | High sensitivity assay(ul) |
| --- | --- | --- | --- | --- |
| 1 | 加变性溶液（NR or R) | 变性溶液 | 7 | 7 |
| 2 | 加样品（使用前离心） | 样品 | 2 | 5 |
| 3 | 加热变性 | NA | 70℃ 5min | 70℃ 5min |
| 4 | 离心 | NA | 离心15s | 离心15s |
| 5 | 加水（分析前1h内） | MilliQ水 | 35 | 32 |
| 6 | 混匀 | NA | 涡旋混匀 | 涡旋混匀 |
| 7 | 转移（离心管>孔板） | NA | 44 | 44 |
| 8 | 离心排除气泡 | NA | 离心孔板，3000 rpm 5min | 离心孔板，3000 rpm 5min |

ladder准备：室温平衡20min，涡旋10s → 移取12μL ladder至离心管中 → 70℃ 5min加热变性 → 离心15s → 加120μL MilliQ水，涡旋混匀 → 转移至0.2ml ladder tube → 插入相应的ladder插孔。

![image-20220107175942031](/images/qc检测流程梳理/202201071759182.webp)

试剂盒和芯片：

![image-20220107174044269](/images/qc检测流程梳理/202201071740413.webp)
![image-20220107174102801](/images/qc检测流程梳理/202201071741928.webp)
![image-20220107174220749](/images/qc检测流程梳理/202201071742873.webp)

### 芯片准备

**胶-染料溶液（Gel-Dye Solution）**：

1. 染料管（蓝色管盖）室温解冻30min，解冻完后在Vortex上震荡20秒，瞬离（quickly spin down）；染料浓缩液中含DMSO，使用前必须完全解冻
2. 反向吸液法（reverse pipetting，原因胶很黏viscous）取出 520μL（高通量）或 280μL（低通量）胶（HT Protein Express Gel Matrix，红色盖子），加到带有滤膜的离心管（Spin Filter）的滤膜上
3. 向Spin Filter上的胶溶液中加入 20μL（高通量）或 10.7μL（低通量）染料（HT Protein Express Dye Solution，蓝色管盖）
4. 将Spin Filter管盖合上，颠倒混匀并放在Vortex上震荡数秒，使胶-染料溶液充分混匀（uniform blue color）
5. 常温下 9300 rcf 离心 5 分钟。将滤膜取出丢弃，避光保存直至芯片准备完毕
6. 多余的试剂保存：4℃避光保存，三周内使用

| NO | Step | Reagent | Color | High throughput（ul）>48samples | Low throughput（ul）<48 samples |
| --- | --- | --- | --- | --- | --- |
| 1 | 染料解冻，涡旋震荡 | Dye solution | blue | NA | NA |
| 2 | 移取胶至离心管的滤膜上 | HT Protein Express Gel Matrix | red | 520 | 280 |
| 3 | 移取解冻好的染料至滤膜上 | Dye solution | blue | 20 | 10.7 |
| 4 | 颠倒，震荡混匀 | NA | NA | NA | NA |
| 5 | 常温离心5min，9000rcf | NA | NA | NA | NA |

注意事项：染料含DMSO，使用前必须完全溶解；离心胶溶液以及胶-染料溶液时速度切勿超过 9300 rcf，超过 9300 rcf 将会改变胶的性质；染料、制备好的染料-胶溶液和marker需要避光。

**反向吸液法**：

![image-20220113211047290](/images/qc检测流程梳理/202201132110388.webp)

**脱色液（Destain Solution）**：用反向吸液法向另一个带有滤膜的离心管中加入 250μL（高通量）或 180μL（低通量）胶，常温下 9300 rcf 离心 5 分钟。将滤膜取出丢弃，避光保存直至芯片准备完毕。多余的试剂保存：4℃避光保存，三周内使用。

| NO | step | reagent | color | High throughput（ul） | Low throughput（ul） |
| --- | --- | --- | --- | --- | --- |
| 1 | 移取胶至滤膜上 | HT Protein Express Gel Matrix | red | 250 | 180 |
| 2 | 常温离心5min，9000rcf | NA | NA | NA | NA |

**芯片准备**：

1. 芯片经过室温平衡30min后，揭去其上的封膜
2. 将移液枪枪头连接在真空泵上，用枪头吸去试剂孔内的全部液体。真空管上的枪头不要触碰芯片的检测窗口
3. 使芯片始终放置在芯片储存盒内，芯片的sipper使用浸在储存液内
4. 将孔（1，2，3，4，7，8，9 和 10）用MilliQ水润洗 2 次，并将水吸掉。同时请勿让这些孔长时间处于干燥状态
5. 加胶-染色液（Gel-Dye solution）：用反向移液法加一定量胶-染料溶液到孔 3, 7, 8, 10
6. 加脱色液（Destain Solution）：用反向移液法向孔 2，9 内各加入一定量的脱色液
7. 加Protein Express Lower marker：向孔 4 内加入 120μL（高通量）或 50μL（低通量）HT Protein Express Lower Marker（绿色管盖）
8. 芯片放入LabChip GXII Touch前，确认孔 1（真空孔）是空的
9. 将芯片放入LabChip GXII Touch，开始实验

![image-20220102175836336](/images/qc检测流程梳理/202201021758441.webp)

注意：请定期清洁LabChip GX/GXII Touch上的圆形密封圈(O-ring)。清洁时，先将随试剂盒附送的棉签用去离子水蘸湿，之后打圈擦拭。待密封圈晾干后可重新放入芯片。

**Chip Well Aspiration Using a Vacuum**：

![image-20220107180115001](/images/qc检测流程梳理/202201071801243.webp)

### 上机运行与维护

1. 检查样品板、Buffer Tube、Ladder Tube是否都已放置在合适的位置上（Check that the sample plate, Buffer Tube, and Ladder Tube are placed on the instrument properly）
2. 将芯片从芯片储存盒中取出，检查圆形检测窗口是否干净。检测窗口如需清洁，使用Caliper提供的清洁布蘸70%异丙醇（isopropanol solution）擦拭即可（Clean BOTH sides of the chip window with the PerkinElmer-supplied Detection Window Cleaning cloth dampened with a 70% isopropanol solution in DI water）
3. 点击触屏主界面上的Unload Chip按钮，将芯片放入LabChip GX Touch中，把机器舱门关上（Touch the Unload Chip button on the Home screen. For GXII, press the Chip button；Insert the chip into the LabChip GXII Touch instrument and close the chip door securely. For GXII, release the latch, insert the chip, latch the chip cartridge, and push in the cartridge）
4. 点击触屏主界面上的load Plate按钮，样品板会自动收回，此时芯片上的Sipper会插入Buffer Tube中（Touch the Load Plate button on the Home screen to retract the sample plate and move the sipper to the Buffer Tube. For GXII, press the Eject button）

注意：不要长时间地打开机器舱门。染料对光敏感，有可能会产生光漂白。

![image-20220107180843653](/images/qc检测流程梳理/202201071808806.webp)

**运行assay**：

1. 在主界面上，点击Run按钮
2. 选择合适的assay type、plate name、well pattern，以及按列或者按行读取样品。在Adv. Settings选项下选择每孔进样的次数

对于protein express assay：

- Protein Express 100: For sizing of proteins in the 14 kDa to 100 kDa range
- Protein Express 100 High Sensitivity：14 kDa to 100 kDa range；larger amount of sample，Slightly lower resolution
- Protein Express 200：14 kDa to 200 kDa range
- Protein Express 200 High Sensitivity
- Antibody Analysis

![image-20220107181408589](/images/qc检测流程梳理/202201071814720.webp)
![image-20220113212443307](/images/qc检测流程梳理/202201132124420.webp)

3. 在Setup Run界面下，选择operator name、是否读取read barcode、文件保存路径、是否包括sample names、expected peaks以及excluded peaks等。选择Auto Export来自动地导出数据和表格
4. 点击Start按钮开始检测

![image-20220102181624360](/images/qc检测流程梳理/202201021816456.webp)
![image-20220102181641927](/images/qc检测流程梳理/202201021816030.webp)

**结果分析**：Protein Express ladder的典型电泳图：15.9 kDa, 20.4 kDa, 28.9 kDa, 48.4 kDa, 68.4 kDa and 119.2 kDa。Protein Express Assay Lower Marker正常迁移时间窗口为11-13.5秒。

![image-20220113220509297](/images/qc检测流程梳理/202201132205363.webp)

**芯片的清洁和储存**：

1. 用真空泵将芯片上试剂孔内的残留试剂全部吸出
2. 用MilliQ水分别润洗（Rinse and completely aspirate）active well 1，2，3，4，7，8，9 和 10 两次
3. 在上述孔内各加入 120μL MilliQ水
4. 将所有孔用封口膜封住以避免溶液挥发（干了会影响芯片性能），并将芯片放置在室温保存待下次使用（而不用加wash buffer放到机器中wash）
5. 上述过程中芯片需始终放置在芯片储存盒内，且sipper须浸没在液体孔中（submerged in the fluid reservoir）。如果储存时试剂孔内没有buffer，将可能导致芯片堵塞

**芯片托架（Chip Cartridge）清洁**：

- 每日：检查托架内部以及密封圈（O-ring）上是否有残留物；用提供的棉签（lint-free swab）蘸去离子水将密封圈和电极打圈擦拭干净。如果密封圈粘在芯片上或者检测到压力泄露，按照每月清洗流程操作
- 每月：将密封圈从机器上取下，放入去离子水中浸泡数分钟，之后用手指揉搓密封圈表面进行清洁；用去离子水浸湿棉签清洁芯片接触面的顶板；使密封圈和芯片接触面自然晾干，将密封圈重新装到机器上

**维护**：

- Daily：Purging the Pressure Lines；Cleaning the O-rings and chip interface（每天用棉签蘸水擦拭）；clean the electrodes after running any diagnostic test using Test Chip D
- Monthly：Cleaning the Chip Interface（取出o-ring，用水泡数分钟，用手指擦）；Calibrating the Optics（Test Chip C计算校正因子：tools>optics normalization>open chip door>插入芯片test chip C>warm and scan>display new correction factor, apply）

**颗粒控制与注意事项**：

确保芯片孔内、通道和毛细管中没有微小颗粒，以下指南帮助更好地避免芯片中的颗粒：

1. 在使用前将芯片、样品板和相关试剂平衡至室温（大约室温放置 20-30 分钟）
2. 每周清洁芯片接触面上的密封圈，每天清洁电极
3. 避免使用有粉末的乳胶手套。处理芯片、试剂和样品板，以及清洁机器电极和电极块时只使用无粉乳胶手套
4. 只有PerkinElmer提供的清洁布可以用于擦拭芯片检测窗口。使用其他未经检验的擦拭巾可能会残留影响荧光检测的碎片，这样会导致聚焦不稳定
5. 用于Chip-Prep的水必须经过 0.22μm 滤膜过滤，分子生物学纯度级别
6. 使用反向吸液法可以帮助避免在吸取胶或者其他粘稠溶液时使芯片中引入气泡

芯片冲洗（chip washing）：Chips should only be washed on the LabChip GXII Touch or GXII immediately before they are prepared with fresh reagents and primed on the instrument. Chips should not be washed and left with water in the chip channels for any extended period of time.

![image-20220102205223730](/images/qc检测流程梳理/202201022052823.webp)

**compatible Buffers, Salts and Additives**：

![image-20220113223129400](/images/qc检测流程梳理/202201132231489.webp)

**Assay Specifications**：

![image-20220107173007623](/images/qc检测流程梳理/202201071730824.webp)

**Protein Exact assay**：sizing range: 6.5 kDa - 250 kDa

**Protein Clear HR Reagent Kit（P/N CLS960014）**：chip storage at 2°C - 8°C；Reagent Storage: Protein Clear HR Dye Solution (blue cap) at -20°C；all other reagents at 2-8℃。

![image-20220101224344020](/images/qc检测流程梳理/202201012243093.webp)
![image-20220101224455373](/images/qc检测流程梳理/202201012244441.webp)

## SDS-PAGE 电泳

### 凝胶化学体系

**线性胶与梯度胶**：线性胶为单一丙烯酰胺浓度；梯度胶的丙烯酰胺浓度为一个范围。

**连续与非连续胶**：连续胶为单一丙烯酰胺溶液；非连续胶由stacking gel（蛋白上样孔所在处）和分离胶组成。Stacking gel的作用是让所有蛋白样品排成一条线（lined up），以完全相同的时间进入分离层（resolving layer）。原理：蛋白在stacking gel中于高迁移率的先导氯离子（来自凝胶缓冲液）和较慢的尾随甘氨酸离子（来自电泳缓冲液）之间被堆叠。

**电泳条件**：变性条件（SDS-PAGE）下，SDS通过缠绕在疏水部分周围使蛋白质变性并展开，结合比例约为1.4 g SDS per gram of protein；非变性条件为native PAGE。

**凝胶化学体系**：三种离子——leading ion（来自gel buffer）、trailing ion（来自running buffer）、common ion（提供缓冲能力）。

![image-202204142234331](/images/qc检测流程梳理/202204142234331.webp)

**Tris-glycine体系（Laemmli系统）**：氯离子由凝胶缓冲液提供，为先导离子；甘氨酸由电泳缓冲液提供，为尾随离子，其pI为5.97；Tris为common ion。Running buffer为Tris-glycine pH8.3，甘氨酸以两性离子形式存在：pH小于7时带正电荷，大于7时带负电荷，在running buffer中带负电荷。Stacking gel为Tris-HCl pH6.8，提供氯离子作为先导离子；甘氨酸负离子进入stacking gel时，pH6.8下大部分不带电荷，小部分带负电荷，在甘氨酸两性离子（trailing ions）和氯离子（leading ions）之间形成狭窄且陡峭的电势差，蛋白夹在中间被浓缩，所有蛋白同时进入分离胶。Resolving gel为Tris-HCl pH8.8；甘氨酸进入分离胶后变成主要带负电荷的离子，不受胶的影响，超过蛋白层；蛋白在电场作用下朝正极迁移，按分子大小分离。

![image-202204142158570](/images/qc检测流程梳理/202204142158570.webp)

缺点：跑胶时gel中的operating pH是9.5。Laemmli系统的高碱性操作pH可能引起条带变形、分辨率下降或artifact bands。主要问题：

- 高pH下聚丙烯酰胺水解，凝胶保质期短（8 weeks）
- 蛋白质在高pH下发生化学改变，如脱酰胺和烷基化
- 含半胱氨酸蛋白的还原二硫键重新氧化，凝胶的氧化还原状态不恒定
- 在Laemmli sample buffer（pH 5.2）中100℃加热时蛋白Asp-Pro键断裂

**Bis-Tris体系**：氯离子为来自凝胶缓冲液的快速移动先导离子；MES或MOPS（取决于running buffer选择）为尾随离子；Bis-Tris为凝胶中的common ion，Tris由running buffer提供。Gel buffer pH 6.4，running buffer pH 7.3–7.7，跑胶时operating pH是7.0，因此样品完整性和凝胶稳定性更好。

**Tris-acetate体系**：Acetate为来自凝胶缓冲液的先导离子；Tricine为来自电泳缓冲液的尾随离子；Tris为common ion。该体系操作pH显著低于Tris-glycine体系，凝胶诱导的蛋白修饰更少。

**Tricine体系**：传统Tris-glycine凝胶系统的改良，使用非连续缓冲系统，专门设计用于分辨2-20 kDa的低分子量蛋白。Tricine为来自凝胶缓冲液的先导离子。

**MES vs. MOPS**：MES pKa是6.1，buffering range 5.5-6.7，适合分离小分子量蛋白；MOPS pKa是7.2，buffering range 6.5-7.9，适合分离中等大小蛋白。

![image-202204150840649](/images/qc检测流程梳理/202204150840649.webp)
![image-202204150839689](/images/qc检测流程梳理/202204150839689.webp)

**电泳干扰物质**：

![image-202204150826766](/images/qc检测流程梳理/202204150826766.webp)

**样品预处理**：不要将还原和非还原样品放在相邻泳道；变性电泳（还原或非还原）加热样品70°C 2–10分钟可获得最佳结果。

**Marker**：

1. Precision Plus Protein All Blue Prestained Protein Standards #1610373 500ul，50 applications，bio-rad 1610373
2. Precision Plus Protein All Blue Prestained Protein Standards，2.5ml（5x50ul），250applications，bio-rad 1610393
3. Precision Plus Protein Dual Color Standards, 500 µl #1610374

**Buffer recipes**：

![image-202204150901146](/images/qc检测流程梳理/202204150901146.webp)
![image-202204150902274](/images/qc检测流程梳理/202204150902274.webp)

**Laemmli buffer 2x**：100 mM Tris HCl, pH 6.8, 4% SDS, 0.2% bromophenol blue, 20% glycerol

**染色方法**：

- 一般步骤：water wash > Fix gel: acid or alcohol wash > stain > destaining（去除背景）
- Coomassie stains：G250和R250两种染料；检测限ng水平
- Silver stains：硝酸银与羧酸基团（Asp和Glu）、咪唑（His）、巯基（Cys）和胺（Lys）结合；检测限subnanogram水平
- Fluorescent and specialty stains：检测限subnanogram或nanogram水平；SYPRO Orange；SYPRO Ruby；SYPRO Red

### 溶液配制

**样品缓冲液**：SDS使蛋白质变性并线性化，消除电荷对凝胶中蛋白迁移的影响；Glycerol增加样品密度，帮助样品沉入上样孔底部并防止从孔中扩散；Bromophenol Blue帮助观察样品在孔中和在凝胶中的移动；Tris pKa=8.1，buffer range 7-9。

![image-20211222111555875](/images/qc检测流程梳理/202112221115028.webp)

**5xR sample loading buffer配方**：

![image-20220316223433641](/images/qc检测流程梳理/202203162234720.webp)

**5X NR sample loading buffer**：在上面配方中不加2-β ME，其它相同。

**电泳缓冲液**：

1XMOPS：100 ml 20×MOPS，加纯水定容至2000 ml。

![image-20220316223633589](/images/qc检测流程梳理/202203162236656.webp)

1X MES：

![image-202203162236054](/images/qc检测流程梳理/202203162236054.webp)

**eStain L1染色液、脱色液**：eStain L1染色液、eStain L1脱色液。

**Homemade Coomassie R-250 staining**：Staining solution：0.1% (m/v) Coomassie R-250, 40% ethanol and 10% acetic acid solution in deionized water；Destaining solution：10% ethanol and 7.5% acetic acid solution in deionized water。

### 样品制备、电泳与成像

**哺乳动物表达上清样品**：离心，12500g，1min；将样品与5xloading buffer混匀，区分还原和非还原，还原处理需要100℃加热5-10min，使蛋白完全变性；加热后的蛋白瞬离，取上清电泳；编写上样单，排列样品，表明上样量和胶孔对应的样品信息；注意N和R不相邻。

**哺乳动物纯化样品**：将样品与5xloading buffer混匀（4：1），区分还原和非还原，还原处理需要100℃加热5-10min，使蛋白完全变性；编写上样单，标明订单号、上样量和胶孔对应的样品信息；注意N和R不相邻；加热后的蛋白瞬离，取上清电泳。

**样品稀释说明**：

- 浓度大于0.5，用PBS稀释到0.5mg/ml
- 0<C<1：4:1，使用5xloading buffer稀释，蛋白：5xloading buffer=40：10
- 1<C<5：(1:3)(4:1)，先使用1xPBS稀释（10：30），再用5xloading buffer稀释（40：10）
- 5<C<10：(1:9)(4:1)，先使用1xPBS稀释（10：90），再用5xloading buffer稀释（40：10）
- C>10：(1:9)(1:3)(4:1)，先使用1xPBS稀释（10：90）（10:30），再用5xloading buffer稀释（40：10）

上机单具体操作方法：浓度检测完成并上传MES系统后，从MES系统QC检测模板筛选当天检测订单通过批处理工具下载当前数据；将订单号及浓度信息复制到上样单模板上，模板会自动显示制样方式及上样单。将每天的制样单保存到对应日期的检测文件夹中。

![image-20220202144837173](/images/qc检测流程梳理/202202021448470.webp)
![image-20220202144927419](/images/qc检测流程梳理/202202021449511.webp)

说明：使用12孔胶；因胶的边沿效应，胶的第一孔和最后一孔建议不点检测样品，可以加BSA、阳参、预染Marker等进行区分。

**电泳**：必须吹孔（Rinse the sample wells thoroughly with 1x running buffer to remove air bubbles and displace any storage buffer）。

1. 凝胶准备：将预制胶固定在电泳装置上，内外槽加入稀释好的1xMOPS电泳缓冲液。加满电泳内槽，外槽的缓冲液不能没过内槽但不能低于内槽的2/3
2. 上样：将离心后的样品按上样单依次加入胶孔中，一次性上样量一般不超过40ul，超过40ul需要压胶；不要污染相邻孔道
3. 加压：正负极正确连接，预制胶恒压145V，跑至溴酚蓝到达分离胶底部上方约1cm关闭电泳仪电源

**染色脱色**（eStain™ L1 Protein Staining System）：

1. 准备托盘，并在托盘中加入适当的纯化水，完全浸软凝胶。将凝胶拆开放置在托盘中浸润1min，同时浸润单片滤纸
2. 从仪器中取出凝胶固定夹，先将浸润好的单片滤纸，平铺在凝胶固定夹上，尽量靠近夹板中心轴水平放置，接着将浸润好的凝胶放置在滤纸上，不要超出滤纸范围，然后再铺上一张滤纸（滤纸和胶的摆放顺序（从上到下）：滤纸-胶-滤纸），覆盖住整块胶，最后合上凝胶固定夹。将固定夹有网一面正对操作者垂直插入通道
3. 按下对应通道start按键，按键闪烁开始倒计时染色，通常染色时间为10 mins

**成像**：

1. 打开仪器，仪器CCD自动制冷。点击begin，进入使用即时显示界面
2. 选择白色底板，凝胶平铺在底板上。置于仪器基座，推进仪器内部，关上仪器外盖
3. 点击屏幕下方的APPLICATION选择Protein Gels，再选择Coomassie Blue
4. 点击屏幕下方的EXPOSURE选择Set Exposure Automatically，再选择Faint Bands。确认无误后，点击右下角拍摄图形，进行拍摄
5. 拍摄完毕后界面跳转至gallery界面查看拍摄结果，可批量选择所需实验图片，右下角send/save传入共享
6. 用Image Lab软件将拍好的图片导出为JPG格式，并存储到自己所需的位置

**阳参**：

1. BSA：albumin standard，thermo，货号23209，原始蛋白浓度为2mg/ml，用5x还原loading buffer稀释4倍，使其终浓度为0.5mg/ml
2. 阳参：
   - multiple-tag genscript货号M0101，先用纯化水溶解冻干粉，使其终浓度为1mg/ml，再用5x还原loading buffer稀释两倍，使其终浓度为0.5mg/ml
   - 鼠阳参：原始蛋白浓度为1mg/ml，再用5x还原loading buffer稀释5倍，使其终浓度为0.2mg/ml

**Native PAGE**：The ExpressPlusTM PAGE Gels are precast without SDS which is conducive for native PAGE。

试剂配方：

![image-20220316224303825](/images/qc检测流程梳理/202203162243911.webp)

## 细菌内毒素检测（BET）

### 基础知识

**内毒素**：Endotoxins（LPS）是革兰阴性菌外膜的组分，在细菌破坏（死亡、裂解）时释放入循环。其在血液中的存在可引起败血症反应，症状包括发热、低血压、恶心、寒战和休克；高浓度可导致严重并发症，如弥散性血管内凝血（DIC）、内毒素休克和成人呼吸窘迫综合征（ARDS）。内毒素可激活补体、激肽系统、白细胞、血小板和内皮细胞。

**鲎试剂（LAL）**：LAL是从鲎（horseshoe crab）的阿米巴样细胞（amoebocyte，白细胞）溶解物中获得的，其中含C因子、B因子、凝固酶原和凝固蛋白原等。

![image-202201121018733](/images/qc检测流程梳理/202201121018733.webp)
![image-20220112102159717](/images/qc检测流程梳理/202201121022052.webp)

**检测方法分类**：

- 凝胶法（gel clot，复核检测用）：基于凝胶形成
- 光度法
  - 浊度法（turbidimetric technique）：基于内源底物裂解后浊度的发展
  - 显色基质法（chromogenic technique）：基于合成肽-生色团复合物裂解后颜色的发展，包括终点显色法和动态显色法

**标准品与用水**：

- 细菌内毒素标准品分国际标准品、国家标准品、工作标准品
- 凝胶法细菌内毒检测用水：内毒素含量小于0.015 EU/ml
- 光度法细菌内毒素检测用水：内毒素含量小于0.005 EU/ml

**G因子旁路反应**：除细菌内毒素外，鲎试剂还可以与β-葡聚糖反应，产生假阳性结果，原因是激活G因子。解决方案：使用去除G因子的鲎试剂或者G因子反应抑制剂来排除鲎试剂与β-葡聚糖的反应。

**内毒素限值的确定**：公式L=K/M。L为供试品的细菌内毒素限值（EU/ml、EU/mg、EU/U）；K为人每kg体重每小时最大可接受的内毒素剂量（threshold pyrogenic dose of endotoxin per kg of body weight），单位EU/(kg*h)，注射剂一般为5EU/(kg*h)；M为人每kg体重每小时的最大供试品剂量。

**最大有效稀释倍数（MVD）**：指在实验中供试品溶液被允许达到稀释的最大倍数，在不超过此稀释倍数的浓度下进行内毒素限值的检测（the maximum valid dilution is the maximum allowable dilution of specimen at which the endotoxin limit can be determined）。公式：MVD=cL/λ。L为供试品的内毒素限值；c为供试品的浓度（mg/ml）；λ为凝胶法中鲎试剂的标示灵敏度（labeled sensitivity, EU/ml）或者在光度测定法中所使用的标准曲线上最低的浓度。

**鲎试剂标示灵敏度复核**：标示灵敏度为在检查方法规定的条件下，使鲎试剂产生凝集的内毒素最低浓度（EU/ml）。新批次鲎试剂或试验条件发生变化（any changes in the test conditions that may affect the outcome of the test）时，应进行灵敏度复核试验：

- 根据鲎试剂灵敏度的标示值，将细菌内毒素国家标准品用细菌内毒素检查用水溶解，在涡旋仪剧烈涡旋15min
- 制成四个浓度：2λ，λ，0.5λ，0.25λ；每一步稀释混匀
- 每一个浓度分别与等体积的鲎试剂混匀，每一个浓度4个平行管；另外，设置一个阴性组，两个平行管
- 封闭管口，37±1℃恒温保温60±2min，避免振摇

试验有效：2λ管为阳性，0.25λ和阴性对照组均为阴性。灵敏度测定值计算（the genomic mean endpoint concentrations）：λc=antilg(∑X/n)。X为反应终点浓度的对数值，反应终点浓度是指系统递减的内毒素浓度中最后一个呈阳性结果的浓度（the endpoint is the smallest concentration in the series of decreasing concentrations of standard endotoxin that clots the lysate）；n为每个浓度的平行管数。

灵敏度判断：λ检测值在0.5-2λ，方可用于内毒素检测，并以标示灵敏度λ为该批鲎试剂的灵敏度。

**干扰试验（tests for interfering factors）**：目的是检查供试品中是否有物质干扰内毒素检测，若有需要以适当方式排除干扰。供试品溶液要求：未检出内毒素且不超过最大有效稀释倍数的溶液（sample solution at a dilution less than the MVD, not containing any detectable endotoxins）。干扰试验溶液制备：

![image-202112220948013](/images/qc检测流程梳理/202112220948013.webp)

试验有效：A和D的所有平行管都为阴性，C的结果符合鲎试剂灵敏度复核试验要求。当系列溶液B的结果符合鲎试剂灵敏度复核试验要求时，认为供试品在该浓度下无干扰作用。

**内毒素检测的未来——重组表达的C因子检测方法**：Lonza的PyroGene。

![image-20220112103024935](/images/qc检测流程梳理/202201121030066.webp)

### 动态显色法（kinetic assay）

**原理**：LAL来源于东方鲎血液中的阿米巴样细胞的溶解物，其中含C因子、B因子、凝固酶原（Coagulase progenase）和凝固蛋白原（Coagulating propsinogen）等。LAL可以作为内毒素的指示剂（indication），内毒素可以激活C因子，引起一系列的酶促反应，激活凝固酶原形成凝固酶，凝固酶分解人工合成的显色基质，分解为多肽和黄色的对硝基苯胺，对硝基苯胺在405nm处有吸光值，吸光值与内毒素浓度成正比，可以通过外标法测定内毒素的浓度。OD值预设某一值，内毒素浓度与达到预设值的时间成反比，时间越短，内毒素浓度越高。

**操作流程**：

1. 实验准备：把移液器、枪头、试剂、孔板、八孔道等耗材放入无菌操作台，喷洒75%酒精，关闭safety panel，打开UV灯（30min）和通风开关，进行灭菌
2. 仪器预热：打开仪器BIOENDO开关，打开电脑桌面GEN5软件（password: admin）>Read now>Recent: endotoxin_test_update.prt，filename以日期命名（YYYY-MM-DD-serial number），点击OK；软件跳出Load Plate界面，仪器开始预热，当温度到达37℃，就可以load plate
3. 操作时用75%酒精对双手进行消毒
4. 内毒标准品配制：

   4.1 标曲要求：至少三个浓度；相邻稀释倍数不得超过10倍；最低浓度不得低于鲎试剂的标示检测限（0.005EU/ml）

   4.2 取出细菌内毒素工作标准品，查看标准品的规格，开启，加入适量的细菌内毒素检查用水，置涡旋混匀器剧烈振摇（mixing vigorously）15min。100EU的标准品，加2ml细菌内毒素检查用水，浓度为50EU/ml

   4.3 将上述内毒素溶液进一步用细菌内毒素检查用水稀释成所需浓度，每稀释一步均应在涡旋混匀器上剧烈振摇1min。配制好的内毒素标准溶液应在4小时内用完，梯度稀释倍数不得超过10倍

以50EU/ml的内毒素溶液为母液按照下表进行梯度稀释，标曲范围0.005-10EU/ml：

| 序号 | 细菌内毒素检查用水（ul） | 内毒素体积和来源 | 内毒素浓度EU/ml |
| --- | --- | --- | --- |
| A | 0 | 1000ul原液 | 50 |
| B | 400 | 100ul A稀释溶液 | 10 |
| C | 200 | 200ul B稀释溶液 | 5 |
| D | 450 | 50ul C稀释溶液 | 0.5 |
| E | 450 | 50ul D稀释溶液 | 0.05 |
| F | 450 | 50ul E稀释溶液 | 0.005 |

5. 阴性对照：细菌内毒素检查用水

6. 供试品的稀释：根据订单内毒要求、样品的浓度和标曲范围，确定稀释倍数；浓度×内毒要求<标曲上限；一般稀释10倍；每一步稀释后需震荡混匀1min

![image-20220119144522283](/images/qc检测流程梳理/202201191445980.webp)

7. 显色试剂溶解：按标示量用配套的buffer复溶显色试剂，混匀后轻轻摇匀，静置至溶液澄清后使用。如果使用量超过1瓶，将两瓶或更多瓶分别复溶，将复溶后的溶液混合到一起轻轻摇匀，静置至溶液澄清后使用

8. 加样操作：取所需数量的无热原微板条，微板条装至微孔板架上，相应孔中分别加入细菌内毒素检测用水、内毒素标准溶液、供试品各100ul，分别2个重复；用移液器每孔加入100ul鲎试剂，避免气泡！将微孔板放置于已经预热好的鲎试剂微生物快速检测系统，点击检测软件界面"确定"，运行检测程序

9. Load plate，点击OK，孔板进入仪器读数

10. 检测完毕，进行数据分析

**注意事项**：

- 反向吸液加样（reverse pipetting technique）防气泡；悬空加样；先加样品，最后才加标曲溶液
- 无热源指内毒素浓度小于0.001EU/ml
- 稀释好的标准品在放置时间超过10min后，用前须混匀1min；放置4小时以上的内毒素溶液应丢弃
- 显色鲎试剂必须用配套的鲎试剂溶解液溶解，不要用漩涡混合器剧烈震荡；溶解的显色鲎试剂应在10min内使用
- 有效标曲判断：1.浓度点≥3，线性相关系数≥0.98；2.重复性，CV<10%，否则舍弃；3.标曲最低点的T值小于阴性对照组的T值

**结果选择**：

- 平行点的onset time变异系数不大于10%，且供试品平行管的平均值在标准曲线的区间内为有效结果
- onset time变异系数在10-50%之间，若两个值影响到对订单是否合格的判断则安排重新检测，否则舍弃一个较小值，以较大值作为最终的内毒结果
- onset time变异系数>50%，直接重新检测
- 平均值列出现"？？？"，即onset time低于标准品中0.005EU/ml对应的onset time，该稀释倍数对应的内毒素低于0.005EU/ml，检测结果无需考虑CV值是否小于10%，结果判定为稀释倍数乘以0.005EU/ml
- 多个稀释倍数，且onset time都在曲线范围内，当多个倍数最终结果的CV值不大于50%，则以较大值作为最终结果；CV值大于50%，则重新安排检测
- 内毒素水平的计算：内毒素水平（EU/ml）=内毒素检测结果（EU/ml，乘以稀释倍数）/蛋白浓度（mg/ml)

**干扰实验**（动态显色法）：

1. 选择标准曲线中点或一个靠近中点的内毒素浓度（设为λm），作为供试品干扰试验中添加的内毒素浓度。如采用标准曲线为10,5,0.5,0.05,0.005 EU/ml系列时，可以用供试品配制0.05EU/ml内毒素浓度作为实验的供试品阳性对照
2. 用供试品溶液配制浓度为λm的内毒素溶液（即含λm内毒素的供试品阳性对照），测量出该溶液的内毒素浓度，称为Cs
3. 测量出未添加外源内毒素的供试品溶液内毒素浓度，称为Ct
4. 计算该试验条件下的回收率R＝（Cs–Ct）/λm×100％
5. 当R在50％～200％之间，则认为在此试验条件下供试品溶液不存在明显干扰作用；当R在50％～200％之外，则存在干扰，需对供试品进行系列稀释或进行其它处理消除干扰，每一稀释溶液都重复步骤2-4，直到内毒素的回收率R在50％～200％之间。选择回收率R最接近100％的稀释倍数进行内毒素检测

注意事项：细菌内毒素检查用水（用于光度测定法，内毒素含量小于0.005EU/ml）不得与凝胶用内毒素检测用水混用。

### 凝胶法（gel-clot）

**原理**：鲎试剂为鲎科动物东方鲎的血液变形细胞溶解物的冷冻干燥品。鲎试剂中含有C因子、B因子、凝固酶原、凝固蛋白原等。在适宜的条件下，细菌内毒素激活C因子，引起一系列的酶促反应，使鲎试剂产生凝集反应形成凝胶。利用鲎试剂与内毒素产生的凝集反应，反应的速度和凝固的坚固程度与内毒素浓度有关。

G因子旁路反应：1,3-β-D-葡聚糖会激活G因子，进而激活凝固酶原，会干扰内毒素检测。因此，供试品中不得含有1,3-β-D-葡聚糖。

![image-20211221112129434](/images/qc检测流程梳理/202112211121582.webp)

**鲎试剂规格**：2、1、0.5、0.25、0.125、0.06、0.03 EU/ml。

**实验操作步骤**：

1. 计算最大稀释倍数：根据蛋白浓度和所需检测内毒素要求，计算最大稀释倍数N=C*L/λ。C为蛋白浓度（mg/ml）；L为内毒素限度要求（EU/mg）；λ为鲎试剂标示灵敏度（EU/ml）。根据最大稀释倍数，上下浮动，制定其它3-5个需要稀释的倍数
2. 超净工作台紫外灭菌：使用前灭菌30分钟；操作时用75%酒精对双手进行消毒
3. 供试品制备：取出空安瓿瓶，标注相应的稀释倍数，混匀时需用涡旋混匀仪混匀大于30秒
4. 2λ的内毒素工作标准品制备：以50EU规格的细菌内毒素工作标准品和λ为0.25EU/ml的鲎试剂为例，2λ的内毒素工作标准品即浓度0.5EU/ml的标准品
   - 取出内毒素工作标准品，查看标准品的规格，开启，加入适量的细菌内毒素检查用水，置涡旋混匀器剧烈振摇15min，作为原液
   - 按照下表进行系列稀释，每一步稀释后均需在涡旋混匀仪剧烈振摇1min，配制好的内毒素标准品溶液应在4小时内用完。梯度稀释倍数不得超过10倍

| 序号 | 细菌内毒素检查用水（ul） | 内毒素体积（ul）和来源 | 内毒素终浓度（EU/ml） |
| --- | --- | --- | --- |
| A | 450 ul | 50 ul 原液 | 5 |
| B | 450 ul | 50 ul A稀释液 | 0.5 |

5. 加样：取出鲎试剂（为冻干粉），掰开安瓿瓶，按下表标注直接加入到安瓿瓶中即可：

|  | 阴性对照 | 阳性对照 | 供试品阳性对照 | 供试品 |
| --- | --- | --- | --- | --- |
| 细菌内毒素检测用水 | 200 ul | 100 ul | NA | 100ul |
| 2λ的内毒素工作标准品 | NA | 100 ul | 100 ul | NA |
| 供试品 | NA | NA | 100ul | 100ul |

以上四组分别做两个平行管。

6. 温育：用封口膜封口，放入37℃恒温培养箱，反应1h

**结果判断**：

1. 将试管从恒温器中轻轻取出（避免振动），缓缓倒转180°；若管内形成凝胶，且凝胶不变形、不从管壁滑脱者为阳性；未成形凝胶或形成的凝胶不坚实、变形并从管壁滑脱者为阴性
2. 实验有效判断条件：阴性对照的平行管均为阴性，阳性对照和供试品阳性对照平行管均为阳性
3. 内毒素水平计算：内毒素水平=（稀释倍数×灵敏度）/供试品浓度
4. 若供试品溶液的两个平行管均为阴性，判断供试品小于此稀释倍数下的内毒水平
5. 若供试品溶液的两个平行管为阳性，判断供试品大于此稀释倍数下的内毒水平
6. 若同一稀释倍数下的两个平行管中的一个为阳性，一个为阴性，需进行复试
7. 复试时，供试品需要做4支平行管，若所有平行管均为阴性，供试品小于此稀释倍数下的内毒水平；否则判供试品大于此稀释倍数下的内毒水平

**注意事项**：

1. 操作过程避免振动，防止假阴性；避免气泡
2. 保温时间严格控制在一个小时，延长可能会出现假阳性
3. 保温温度，严格按照37℃±1℃
4. 细菌内毒素检查用水，用于凝胶法的，其内毒素含量小于0.015EU/ml

## SEC-HPLC

### 高效液相色谱基础

**色谱柱分类**：

- 反相色谱柱：以键合非极性基团的载体为填充剂。常用载体：硅胶、聚合物复合硅胶和聚合物
- 正相色谱柱：填充剂为硅胶、氨基键合硅胶和氰基键合硅胶
- 离子交换色谱柱：阳离子和阴离子
- 手性分离色谱柱

色谱柱参数：内径、长度、填充剂的形状、粒径与粒径分布、孔径、表面积、键合基团的表面覆盖度、填充剂的致密与均匀黏度。

**检测器**：

- 通用性检测器（对所有物质均有响应）：
  - 蒸发光散射检测器：响应值与被测物质的量在一定范围内呈对数关系，一般需要对数转换；流动相不得含不挥发性成分
  - 电雾式检测器：响应值与被测物质的量在一定范围内呈对数关系，一般需要对数转换；流动相不得含不挥发性成分
  - 示差折光检测器：响应值与被测物质的量在一定范围内呈线性关系
- 选择性检测器（响应值不仅与被测物质的量有关，还与其结构有关）：
  - 紫外-可见光分光检测器：响应值与被测物质的量在一定范围内呈线性关系；考虑有机溶剂的截止使用波长
  - 荧光检测器、电化学检测器：响应值与被测物质的量在一定范围内呈线性关系

**流动相**：用紫外末端波长检测时，宜选用乙腈-水系统。洗脱方式：等度洗脱和梯度洗脱。

**色谱参数调整**：不得改变的参数——填充剂的种类、流动相组分、检测器类型。可以改变的参数——色谱柱内径与长度、填充剂粒径、流动相流速、流动相组分比例、柱温、进样量、检测器灵敏度。

![image](/images/qc检测流程梳理/202112312239054.webp)

**系统适用性试验**：

- 色谱柱的理论塔板数（n）：用于评价色谱柱的效能，n=16(tR/W)^2=5.54(tR/W_h/2)^2
- 分离度（R）：衡量系统分离效能的关键指标，待测峰与相邻色谱峰之间的分离度应不小于1.5
- 灵敏度：评价色谱系统检测微量物质的能力；测不同浓度的信噪比，定量信噪比大于10，定性信噪比大于3
- 拖尾因子：评价色谱峰的对称性，T=W_0.05h/(2d1)；以峰高作为定量参数时，T值在0.95-1.05之间
- 重复性：评价色谱系统连续进样时响应值的重复性能，连续进样五次，峰面积测量值的相对偏差不大于2.0%

![image-20211231232015471](/images/qc检测流程梳理/202112312320752.webp)

**定性定量方法**：

- 定性分析：利用保留时间定性；利用光谱相似度定性（全波长扫描紫外可见光光谱图）；利用质谱检测器提供的质谱信息定性
- 定量分析：
  - 内标法：可避免样品前处理及进样体积误差对测定结果的影响。校正因子 f=(As/cs)/(AR/cR)，As为内标物峰面积或峰高，AR为对照品峰面积或峰高，cs为内标物浓度，cR为对照品浓度。供试品浓度计算时取含有内标物质的供试品溶液进样，记录色谱图，代入校正因子计算
  - 外标法：精密称（量）取对照品和供试品，配制成溶液，分别精密取一定量，进样，记录色谱图
  - 加校正因子的主成分自身对照法：用于测定杂质。待测杂质校正因子=杂质峰面积/浓度与参比物峰面积/浓度之比，或以主成分回归直线斜率与杂质回归直线斜率的比计算。杂质含量测定：按照品种项规定的杂质限度，将供试品溶液稀释成杂质限度相当的浓度作为对照品溶液，必要时调整纵坐标范围使对照溶液的主成分色谱峰的峰高约达满量程的10%-25%。除另有规定外，通常含量低于0.5%的杂质，峰面积测量值的相对标准偏差应小于10%；含量在0.5-2%的杂质，RSD小于5%；含量大于2%的杂质，RSD应小于2%。供试品溶液的记录时间应为主成分色谱峰保留时间的2倍，测量各杂质的峰面积，分别乘以相应的校正因子后与对照溶液主成分的峰面积比较，计算各杂质含量
  - 不加校正因子的主成分自身对照法：无法获得杂质对照品时使用，前提是杂质和主成分结构类似、响应差不多
  - 面积归一化法：测量各峰的面积和色谱图上除溶剂峰以外的总色谱峰面积，计算各峰面积占总峰面积的百分比，一般不用于微量杂质的检查

### 分子排阻色谱法（SEC）

**原理**：分子排阻色谱法是根据待测组分的分子大小进行分离的一种液相色谱技术，分离原理为凝胶色谱柱的分子筛机制。色谱柱多以亲水硅胶、凝胶或经过修饰的凝胶如葡聚糖凝胶（Sephadex）和琼脂糖凝胶（Sepharose）等为填充剂，这些填充剂表面分布着不同孔径尺寸的孔。药物分子进入色谱柱后，不同组分按照其分子大小进入相应的孔内：大于所有孔径的分子不能进入填充剂颗粒内部，在色谱过程中不被保留，最早被流动相洗脱至柱外，表现为保留时间较短；小于所有孔径的分子能自由进入填充剂表面的所有孔径，在色谱柱中滞留时间较长，表现为保留时间较长；其余分子则按分子大小依次被洗脱。

**系统适用性试验**：理论塔板数、分离度、重复性、拖尾因子。在高分子杂质检查时，某些药物分子的单体和其二聚体不能达到基线分离时，其分离度计算公式如下：R=二聚体的峰高/单体与二聚体之间的谷高，分离度应大于2.0。

**测定方法**：

- 分子量测定法：选用与供试品分子大小相适宜的色谱柱和适宜分子量范围的标准物质。除另有规定外，标准物质与供试品均需使用二硫苏糖醇（DTT）和十二烷基硫酸钠（SDS）处理，以打开分子内和分子间的二硫键，并使分子的构型与构象趋于一致。经处理的蛋白和多肽分子通常以线性形式分离。以标准物质分子量（M）的对数值对相应的保留时间（t）制得标准曲线的线性回归方程计算其分子量或亚基的分子量：lgM=a+b*t
- 生物大分子聚合物分子量与分子量分布的测定方法：用于多糖与多聚核苷酸
- 高分子量杂质测定法：通常是药物生产中或贮存过程中产生的高分子聚合物或生产过程中产生过敏反应的高分子物质。包括主成分自身对照法（一般用于高分子杂质含量较低的品种）、面积归一化法、限量法（一般用于混合物中高分子物质的控制）、自身对照外标法

### SEC-HPLC 操作流程

**流动相配制**：

- 1X流动相：0.1 mol/L Na2SO4 in 0.1 mol/L Phosphate Buffer（pH 6.7±0.3）

![image-20220101180241528](/images/qc检测流程梳理/202201011802605.webp)

试剂称量好后，加MilliQ纯化水定容至1L，充分溶解混匀后，调pH至6.7±0.3，0.22um滤膜抽滤，再超声10min排气，防止气体进入色谱柱或检测器引起基线的波动而影响试验结果的准确性。

- 10X流动相：1mol/L Na2SO4 in 1 mol/L Phosphate Buffer（pH 6.7±0.3）

![image-20220101180843349](/images/qc检测流程梳理/202201011808415.webp)

试剂称量好后，用MIlli-Q水定容1L，不需检测pH，放置室温保存。待使用时使用Milli-Q水稀释成0.1 mol/L Na2SO4 in 0.1 mol/L Phosphate Buffer，再调pH至6.7±0.3，0.22um滤膜抽滤，再超声10min排气。

**色谱条件**：

- 色谱柱（TSKgel G3000SWxl Column）：
  - 保护柱：TSKgel guardcolumn SWxl, 6.0 mm × 40 mm（TOSHO, Cat.No. 8543）
  - 主柱：TSKgel G3000SWxl, 7.8 mm × 300 mm，粒径5um（TOSHO, Cat.No.0008541）
- 上样量：蛋白浓度＞0.2mg/ml：上样量20ug；蛋白浓度≤0.2mg/ml：最大上样量为95ul
- 流速：0.7ml/min
- 紫外检测波长：280nm
- 运行时间：25min
- 流动相：0.1 mol/L Na2SO4 in 0.1 mol/L Phosphate Buffer（pH 6.7±0.3）
- 梯度：等度洗脱

**命名规则**：样品命名：订单号_样品描述；报告命名：订单号-样品描述_色谱柱简称-检测日期。

**纯度判断标准**：Gel Filtration Standard：Thyroglobulin（670 kDa）、γ-globulin（158 kDa）、Ovalbumin（44 kDa）、Myoglobin（17kDa）和Vitamin B12（1.35 kDa）。

## 小结

本文覆盖了 QC 放行检测实验室常用的六类方法。蛋白浓度测定中，Bradford 法快速但对去污剂敏感，BCA 法试剂稳定且为目前最常用的铜离子法，Lowry 法灵敏度高但试剂需现配现用，UV 法无需试剂但受缓冲液与光散射干扰，需结合样品buffer评估适用性。免疫印迹与 SDS-PAGE 的关键在于凝胶化学体系选择、样品还原状态处理（N与R不相邻）以及转膜/染色条件的标准化。LabChip GXII Touch 将分离、染色、脱色与检测集成于芯片，核心在于通过intersection稀释SDS至cmc以下以降低背景，操作上需严格控制胶-染料离心速度（不超过9300 rcf）与样品过滤。内毒素检测中，凝胶法操作简便但灵敏度受标示灵敏度限制，动态显色法需关注标准曲线有效性（CV<10%）与供试品干扰（回收率50%～200%）；G因子旁路是两类方法共同的假阳性来源。SEC-HPLC 用于分子量测定与高分子杂质检查，系统适用性试验（分离度≥1.5，高分子杂质检查时≥2.0）是结果可靠的前提。

各方法均需注意：试剂与样品的前处理（过滤、脱气、避光）、仪器维护（电极清洁、芯片储存、色谱柱保护）以及阳参/对照品的同步检测，这些环节直接影响数据的可信度与批间重现性。