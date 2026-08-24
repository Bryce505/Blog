---
title: "HPLC 方法开发：柱选择、梯度设计与峰形诊断"
date: 2026-08-24
category: "05仪器与分析技术"
primaryTag: "05仪器与分析技术/色谱分析/HPLC"
description: "本文汇总该主题下 11 篇工作笔记，按原理、方法与常见问题三条线索重新组织，数据与法规条款均取自原始笔记。"
tags:
  - "00基础/文献"
  - "02分子表征/肽图"
  - "03质量控制/RP-HPLC"
  - "03质量控制/SEC"
  - "05仪器与分析技术/液相色谱/色谱柱"
  - "05仪器与分析技术/色谱分析/HPLC"
  - "05仪器与分析技术/色谱分析/RP-HPLC"
  - "05仪器与分析技术/色谱分析/SEC"
sourceNotes:
  - "Analytical technology/HILIC-HPLC/HILIC色谱柱汇总.md"
  - "Analytical technology/HPLC色谱柱相关知识.md"
  - "Analytical technology/IEX-HPLC/IEX色谱柱信息汇总.md"
  - "Analytical technology/RP反相/New trends in reversed-phase liquid chromatographic separations of therapeutic peptides and proteins Theory and applications.md"
  - "Analytical technology/RP反相/反相色谱柱.md"
  - "Analytical technology/RP反相/梯度洗脱.md"
  - "Analytical technology/RP反相/肽图.md"
  - "Analytical technology/SEC-HPLC/SEC SOP.md"
  - "Analytical technology/SEC-HPLC/SEC-HPLC.md"
  - "Analytical technology/SEC-HPLC/SEC色谱柱信息汇总.md"
  - "Analytical technology/USP Classification of HPLC Columns.md"
---

本文汇总该主题下 11 篇工作笔记，按原理、方法与常见问题三条线索重新组织，数据与法规条款均取自原始笔记。


[HILIC and NPC Stationary Phases](https://doi.org/10.1016/B978-0-12-803684-6.15003-6 "Persistent link using digital object identifier")

## 相关笔记

- Analytical technology/HPLC色谱柱相关知识.md
- Analytical technology/USP Classification of HPLC Columns.md
- Analytical technology/试剂溶剂性质.md
- Analytical technology/RP反相/梯度洗脱.md
- Analytical technology/SEC-HPLC/SEC SOP.md



Chapter 6 - General Aspects Regarding the HPLC Analytical Column
[https://doi.org/10.1016/B978-0-12-803684-6.00004-4](https://doi.org/10.1016/B978-0-12-803684-6.00004-4 "Persistent link using digital object identifier")

## 相关笔记

- Analytical technology/HPLC色谱柱相关知识.md
- Analytical technology/USP Classification of HPLC Columns.md
- Analytical technology/试剂溶剂性质.md
- Analytical technology/RP反相/梯度洗脱.md
- Analytical technology/SEC-HPLC/SEC SOP.md



[Ion Exchange and Ion-Moderated Stationary Phases](https://doi.org/10.1016/B978-0-12-803684-6.15004-8 "Persistent link using digital object identifier")

[Chapter 9 - Stationary Phases and Columns for Ion Exchange, Ion-Moderated, and Ligand Exchange Chromatography](https://doi.org/10.1016/B978-0-12-803684-6.00009-3 "Persistent link using digital object identifier")

## 相关笔记

- Analytical technology/HPLC色谱柱相关知识.md
- Analytical technology/USP Classification of HPLC Columns.md
- Analytical technology/试剂溶剂性质.md
- Analytical technology/RP反相/梯度洗脱.md
- Analytical technology/SEC-HPLC/SEC SOP.md



#03质量控制/RP-HPLC #05仪器与分析技术/液相色谱 
>**来源**：
>[Reversed-Phase Liquid Chromatography for the Analysis of Therapeutic Proteins and Recombinant Monoclonal Antibodies (chromatographyonline.com)](https://www.chromatographyonline.com/view/reversed-phase-liquid-chromatography-analysis-therapeutic-proteins-and-recombinant-monoclonal-antibo)

### 0 补充
**色谱柱分类**：[https://www.uspnf.com/sites/default/files/usp_pdf/EN/USPNF/revisions/hplcclassification.pdf](https://www.uspnf.com/sites/default/files/usp_pdf/EN/USPNF/revisions/hplcclassification.pdf)

**HPLC Columns List in PQRI & USP Chromatographic Database**
网站：[https://apps.usp.org/app/USPNF/columnsDB.html](https://apps.usp.org/app/USPNF/columnsDB.html)
1. PQRI column database：寻找类似的色谱柱，来替换原先的色谱柱；基于以下来挑选等同选择性的色谱柱
    - hydrophobicity “H”; 
    - Column steric interaction “S”; 
    - Column hydrogen-bond acidity “A”; 
    - Column hydrogen-bond basicity “B”; 
    - Column ion-exchange capacity “C”
2.**U.S. Pharmacopeia (USP) Chromatographic Database**

**色谱基础理论**：[PPT - Introduction to Chromatography PowerPoint Presentation, free download - ID:9291870 (slideserve.com)](https://www.slideserve.com/cthurston/introduction-to-chromatography-powerpoint-ppt-presentation)

反相固定相种类[^1]
1. organic monolithic
2. fully porous
3. core-shell type

### 1 传统反相在分离蛋白时遇到的问题
1. 峰变宽（broadened peak shapes），原因1：蛋白分子量，有不同的构象，翻译后修饰，多个同分异构体；原因2：这些分子尺寸大，其分子扩散系数小；
2. 缺乏可靠的参考品，无法进行绝对定量和方法验证；


### 2 Basic requirements of conventional RPLC stationary phases

>二氧化硅科普
>synthetic silica polymers are typically formed from ==tetraethoxysilanes==， ==tetraethoxysilanes==会部分水解成聚乙氧基硅氧烷(一种粘性的液体)，这种物质在乙醇水混合物中剧烈搅拌下发生乳化，搅拌导致颗粒结合形成球形，这些球形经过催化诱导水解缩合（Unger method），通过表面的硅烷醇大量的交联，形成silica hydrogel；silica hydrogel然后再加热得到highly porous silica xerogel(sometimes called sol-gel)；pH,温度，催化剂，溶剂和硅烷醇浓度这些一起控制颗粒大小和孔径；
>另一种制作工艺：在尿素/甲醛溶液中，silica microparticles聚集产生微球颗粒-microspheres（‘sil-gel’）；microparticles的浓度和直径，反应条件控制着sil-gel的尺寸和孔径；
>![](/images/05仪器与分析技术-色谱分析-hplc/20221123140101.webp)


microparticulate  (2–5 m) porous silica，其表面修饰有正烷基的silane；表面未修饰的silica使用small reactive silane来封闭，这叫end-cap，目的减少暴露的silanol-硅烷醇基；Silica-based packings在碱性中容易解离，使用时需要注意pH,不要超过8;
**常见的配基：
1. n-octadecyl (C18)；
2. n-butyl (C4) ； 
3. n-octyl (C8)；
4. phenyl ；
5. cyanopropyl ligands；

**填料的哪些参数影响保留？**
- the relative  hydrophobicity of the ligand
- surface coverage
- ligand density
- carbon load
- flexibility
- the degree of exposure of the surface  silanol

两个指标：
1. **Particle Size**：颗粒尺寸分布，分布越小，分离度越好；颗粒尺寸分布好坏评价标准：D10/90 ratio – which is the ratio of particle sizes at the 10 and 90th percentiles of the normally distributed range of particles(分布的宽度)，一般小于1.2，越小越好；
![](/images/05仪器与分析技术-色谱分析-hplc/20221123203150.webp)
2. pore size; 大部分表面积位于孔内部，占99%的表面积；颗粒的表面积与孔径成反比；孔径可以用于控制分析物的保留；
    - 80-120A˚：适用于分析小分子(< 3,000 Da)；小分子很容易渗透进入孔内，与硅烷表面接触最多；
    - 孔径选择原则：Typically the pore diameter needs to be ==three times== the times the hydrodynamic diameter of the analyte in order to be accessible
![](/images/05仪器与分析技术-色谱分析-hplc/20221123203319.webp)
![](/images/05仪器与分析技术-色谱分析-hplc/20221123204520.webp)

在选择蛋白分离的反相柱时，固定相的孔径是一个至关重要的参数；
- 对于小蛋白和多肽（≤14kDa）：选孔径200 A˚以内的填料即可；1A˚=0.1nm
- 大于更大的蛋白（＞14kDa）：选孔径大于200 A˚的填料；
**选择依据**：the solute molecular diameter must be approximately ==one-tenth== the size of the pore diameter to avoid the restricted diffusion of the solute and to allow the total surface area of the sorbent material to be accessible；==三倍较合理==
抗体（PDB: 1IGT）的水合半径（hydrodynamic volume）：==11nm==；Fab（PDB: 3WD5)的水和半径：7nm；
> 数据来源：[List of protein hydrodynamic diameters | Dynamic Biosensors (dynamic-biosensors.com)](https://www.dynamic-biosensors.com/project/list-of-protein-hydrodynamic-diameters/)

### 3 Method development in RPLC separations of proteins
DryLab software for the computer-assisted method development of RPLC protein separations，这种电脑协助的方法开发在肽图中更常见[^2]；

#### 3.1 Classical approach, improving the selectivity
基于氨基酸序列描述多肽和蛋白的保留行为的模型，可以利用这些模型快速开发分离方法；
1. solvophobic theory
2. linear solvent strength theory

对于蛋白或多肽来说，提高选择性和分辨率最高的方法：改变有机修饰剂的浓度，选择合适的离子对试剂；
1. 首先考虑溶剂选择性三角法-==solvent selectivity triangle approach==[^3]；溶剂根据相对偶极性，碱度和酸度进行分类；确定流动相混合比例范围，提供合适的保留范围，洗脱样品在这个范围内；
2. 选择合适的离子对试剂-ion-pairing reagents
    - Anionic counterions: hexanesulfonic acid, orthophosphoric acid, and trifluoroacetic acid；与蛋白的碱性氨基酸-精氨酸，赖氨酸和组氨酸，N端氨基；
    - Cationic counterions： triethylammonium  and tetrabutylammonium；与蛋白的酸性氨基酸结合
    - The actual effect on retention depends  strongly on the hydrophobicity and concentration of the ion-pair  
     reagent and the number of oppositely charged groups on the protein.
3. 优化柱温和梯度-gradient profile：如何优化梯度：两个梯度间的洗脱时间三倍(相同的开始和结束比例)，评估洗脱时间对总体分辨率的影响；
![](/images/05仪器与分析技术-色谱分析-hplc/20221123222004.webp)

#### 3.2 Another approach, improving the kinetic efficiency
如果蛋白间的分子结构差异非常小，光靠选择性无法分离蛋白，这时需要考虑kinetic efficiency；那么在方法开发过程需要考虑固定相和温度；改变填料基质类型，其次改变固定相化学；还有改变柱长；
- core–shell-type materials
- sub-2 um porous particles 
- wide-pore monolithic columns

### 4 Improvements to conventional RPLC
#### 4.1 Kinetic performance
**Van Deemter Equation**
![](/images/05仪器与分析技术-色谱分析-hplc/20221124071711.webp)
- A项-多路径效应： 完全依赖于柱子，与填料的形状和直径成正比；
![](/images/05仪器与分析技术-色谱分析-hplc/20221124082920.webp)
- B项-纵向扩散系数：与流动相扩散系数成正比；
- C项：物质传输，与流动相扩散系数成反比，与粒径成正比；
 **流动相和温度**
- 温度升高时，流动相黏度明显下降，导致流动相扩散系数大幅提高；
- 温度升高，流动相的表面张力下降
- 温度身高时，分析物表面的正电荷与带负电荷的硅烷醇间的离子相互作用减弱，减少拖尾






















### Reference

[^1]:  New trends in reversed-phase liquid chromatographic separations of therapeutic peptides and proteins: Theory and applications [doi.org/10.1016/j.jpba.2012.03.024](https://doi.org/10.1016/j.jpba.2012.03.024 "Persistent link using digital object identifier")
[^2]: W. Hancock (Ed.), New Methods in Peptide Mapping for the Characterization of Proteins, CRC Press, Boca Raton, FL, 1996, pp. 31–56.
[^3]: Chromatographic selectivity triangles  -   DOI: [10.1016/j.chroma.2010.09.046](https://doi.org/10.1016/j.chroma.2010.09.046)

## 相关笔记

- Analytical technology/RP反相/反相色谱柱.md
- Analytical technology/RP反相/梯度洗脱.md
- Analytical technology/HPLC色谱柱相关知识.md
- Analytical technology/RP反相/肽图.md
- Analytical technology/试剂溶剂性质.md






[Chapter 7 - RP-HPLC Analytical Columns](https://doi.org/10.1016/B978-0-12-803684-6.00007-X "Persistent link using digital object identifier")

填料孔径大小
- 分析物＜4000Da：采用80A
- 4,000-500,000Da：采用300A；

## 相关笔记

- Analytical technology/RP反相/反相色谱柱.md
- Analytical technology/RP反相/梯度洗脱.md
- Analytical technology/HPLC色谱柱相关知识.md
- Analytical technology/RP反相/肽图.md
- Analytical technology/试剂溶剂性质.md




[Chapter 14 - Gradient Elution](https://doi.org/10.1016/B978-0-12-803684-6.00014-7 "Persistent link using digital object identifier")

[梯度优化](https://www.chromatographyonline.com/view/secrets-successful-gradient-elution)
- 空白梯度：不进样，检查基线是否波动，如果波动较大，则改变检测波长，或者使用无吸收的溶剂；
- Scouting gradient: 基于第一个和最后一个洗脱峰；跑一个梯度较宽的test，如5%-90%B
![|304](/images/05仪器与分析技术-色谱分析-hplc/gradient.webp)

式中
1. B<sub>initial</sub>：初始梯度；
2. B<sub>final</sub>：最终梯度；
3. t<sub>g</sub>: 梯度时间；
4. t<sub>i</sub>: 第一个峰的洗脱时间（min，从梯度开始计算？）；
5. t<sub>f</sub>：最后一个峰（min，从梯度开始计算？）；
6. V<sub>D</sub>：dwell volume(ml)，系统驻留体积；


**计算梯度时间**

$$
tG = \frac{k\times \Delta\Phi V_m S}{F}
$$
- K: gradient retention factor，默认5，可以以5为起点上调；
- Vm：  the volume of mobile phase in the column;估算公式：$V_m = Ld_c^2/2$;
- $\Phi$: 梯度；
- S： average slope of the retention equation for a series of solutes against the cosolvent volume fraction；取值5；
- F：流速

> [!NOTE] 系统驻留体积及其测定
> 定义：梯度形成点和色谱柱入口之间系统的总体积；
> 延迟体积是色谱系统的物理特征参数，主要来自于泵。它指的是梯度输送控制装置与色谱柱柱 头之间的体积差，通常又称为“梯度延迟体积”
> [系统驻留体积测定](https://cn-support.waters.com/KB_Chem/Other/WKB50707_How_do_I_determine_system_dwell_volume)
> ![|694](/images/05仪器与分析技术-色谱分析-hplc/dwell-volume-cal.webp)
> ACQUITY UPLC H-Class 系统驻留体积＜400ul （使用100ul混合器）
![](/images/05仪器与分析技术-色谱分析-hplc/H-class-DwellVolume.webp)
![|564](/images/05仪器与分析技术-色谱分析-hplc/dwell-vloume2.webp)
![](/images/05仪器与分析技术-色谱分析-hplc/Pasted image 20240905132540.webp)

[ACQUITY UPLC H-class plus system with binary solvent management system](https://lcms.cz/labrulez-bucket-strapi-h3hsga3/720006416en_eb1e2bbfab/720006416en.pdf)
Gradient delay volume: <span style="background:#fff88f">≤90ul</span>；
**Extra column volume** – all volume with an HPLC system from the sample loop to the detector, excluding the column. Dead volume contributes a portion of this volume
**Extra column volume**<12ul

## 相关笔记

- Analytical technology/RP反相/反相色谱柱.md
- Analytical technology/RP反相/梯度洗脱.md
- Analytical technology/HPLC色谱柱相关知识.md
- Analytical technology/RP反相/肽图.md
- Analytical technology/试剂溶剂性质.md




> 资料1：  B05 - PEPTIDE MAPPING(Revision 1):[000219440.pdf (pmda.go.jp)](https://www.pmda.go.jp/files/000219440.pdf)
> 

```toc
```

## 1.介绍
目的：蛋白分子量大，且异质性高，无法仅靠完整分子量来鉴定；需要从肽段水平来鉴定蛋白；
肽图：是一种比较性方法，样品和参考品经相同的处理和分析，通过样品结果与参考品的结果比对，以此鉴定蛋白，确认样品的氨基酸序列与参考品的一致；


## 2.用途
肽图：一个比较性的方法，检测样品的结果与参考品（reference standard）的做比对，确保检测样品的一级结果跟参考品的相同；

**用途**
-   Peptide mapping comparison during scale up or manufacturing changes can support studies of process consistency；证明工艺一致性；
-   peptide mapping can be used to determine the degree and specific amino acid location of modifications such as  
glycosylation and conjugation；测定修饰程度和修饰位点；

肽图用途：
- 蛋白组学研究
- protein biopharmaceutical analysis
	- structural characterization
		- Pattern conforms to primary structure
		- used with MS for primary structure determination
		- Non-reduced mapping for disulfide bond assignment
	- protein modification
		- identify post-translational modifications: glycosylation, substitution, truncation;
		- determine product-related impurities: deamidation, oxidation, etc;
		- characterization of variants observed in other methods(IEX, SEC);
	- protein identity
		- confirm presence of "signature peptides"
		- product integrity- lot-to-lot analysis;


## 3.开发肽图鉴定检测方法的注意事项
identity test
- level of specifity：足够多的专属性；
- 理解目的蛋白的特性

![](https://708838228.oss-cn-shanghai.aliyuncs.com/img/peptide-mapping.png)

### 3.1 前处理
- 纯化：去除干扰，如辅料和载体蛋白；开发过程需要评估残余干扰物质或纯化对终样肽图检测的影响；
- 变性处理：展开蛋白，暴露酶切位点；需要对额外的纯化或透析以去除变性剂；
- 还原和烷基化：

需要在方法开学中调查以上前处理对方法专属性和精密度的影响，在方法验证时把这些前处理放到耐用性（robustness）中做；

### 3.2 酶切

| 酶或试剂                                  | 酶切位点                                      |
| ------------------------------------- | ----------------------------------------- |
| trypsin                               | K/R-Xaa                                   |
| chymotrypsin                          | F/W/Y/L/M/A-Xaa                           |
| pepsin                                | 下铰链区EL<font color="#ff0000">/</font>LGGP  |
| panpain                               | 上铰链区SCDKTH<font color="#ff0000">/</font>T |
| Lys-C                                 | K-Xaa                                     |
| Glu-C/V8 protease                     | E/D-Xaa                                   |
| Asp-N                                 | Xaa-Asp                                   |
| Arg-C                                 | Arg-Xaa                                   |
| Cyanogen bromide                      | Xaa-M                                     |
| 2-Nitro-5-thiocyanobenzoic acid（NTCB) | Xaa-C                                     |
| O-Iodosobenzoic acid                  | W/Y-Xaa                                   |
参考文献：Identification of alternative products and optimization of 2-nitro-5-thiocyanatobenzoic acid cyanylation and cleavage at cysteine residues； - DOI: [10.1016/j.ab.2004.08.008](https://doi.org/10.1016/j.ab.2004.08.008)
NTCB切割C之前的肽键
![|330](/images/05仪器与分析技术-色谱分析-hplc/NTCB.webp)

影响蛋白酶切效率和重复性的因素
- pH
- 酶切buffer
- 温度
- 时间
- 酶蛋白比例

副反应
- 非特异性断裂
- 脱酰胺
- 二硫键异构化
- 氧化
- k发生carbmylation
- 多肽N端的谷氨酰胺脱酰胺，形成pyroglutamic;

蛋白酶自水解（autolysis）
- 如何减少：配制蛋白酶溶液，其pH抑制酶活性，或者现配现用；trypsin，加50mM醋酸溶解，原因就在此；
- 采用经修饰的蛋白酶：如trypsin上的K被甲基化或乙酰化；
- 如何鉴定digestion artifact: blank digestion control, 不加样，只有酶；

### 3.3 分离

- 色谱柱
	- 一般采用Octadecylsilane (C18) with <font color="#ff0000">300 A </font>or smaller pores
	- 填料pore size；或者基于二氧化硅，聚合物，hybrid的无孔填料；
	- 填料粒径
流动相中一般添加0.05%-0.2%TFA;
流动相为何加TFA？
- 降低pH，使pH低于反相色谱柱上残余的二氧化硅的pka，抑制蛋白或多肽的碱性模块与去质子二氧化硅之间的次级相互作用，减少峰拖尾；
- 通过形成离子对，增加分析物在色谱柱上的保留；
	- 理论1：对带电荷的分析物形成中性的或电荷较少的复合物，从而增强疏水性，分析物保留也增加；
	- 理论2：离子对试剂疏水部分与烷基固定相结合，离子对试剂带电荷部分与溶质的带电部分之间离子相互作用，从而提高保留；

### 3.4 检测
UV: 214nm；
UV+MS

### 3.5 数据分析
比较项目：
- 保留时间
- 峰响应（峰面积或峰高）
- 峰数量
- overall elution pattern
比较所有关键峰的保留时间和峰响应比率，如果一致，则确认样品是目的蛋白；

如抗体样品：把常见的Fc多肽用作reference peak；关键峰的保留时间和峰响应分别reference peak的相比，得到相对值；再比较样品和参考品的保留时间相对值和峰响应相对值；


## 4.肽图验证时考虑点

system suitability criteria
analytical method validation acceptance criteria

质谱检测可以用于评估以下性能参数
- coverage：对于肽图方法，一般要求95%；
- specific bond cleavages: 以表格形式列出鉴定的多肽（按照理论酶切位点酶切），多肽序列，保留时间，峰面积等；
- 主要峰（major peaks）
- partial cleavage（漏切）：部分断裂或不完全断裂，鉴定出酶切不完全的多肽及其色谱峰；
- Minor/Non-specific Cleavages（错切）：以表格形式列出非特异性酶切的多肽；
- Protease-derived Peaks：应识别出源自蛋白酶的任何高于背景信号的峰，并在适当的情况下加以限制；
- Undigested “Core” Protein：应鉴定出未酶切或部分酶切的蛋白，并限制这种情况发生；
- Mean Peptide Length：10-20个残基；太短，结构选择性高但峰多，图谱复杂；太长，峰少图谱简单，对于结构变体分辨率不足；
- Resolution Capacity：理论有多少多肽，实际分离出多少多肽，其他多肽可能发生共洗脱或非保留；识别出有问题的分离方法，进行优化；

System Suitability Criteria Selection
- 评估参考品酶解色谱图
- performance characteristics
	- 定性比较：与参考品色谱图的相似性；
	- 酶解的程度；
	- 漏切
	- 非特异性酶切
	- 峰高/信号与噪音之比
	- 峰形状
	- 峰保留时间
	- 特定峰的分离度

## 5.验证

在验证之前，方法必须成型，并附有系统适应性标准；每次实验后，按照系统适用性可接受标准，评估实验结果，评估方法是否产生可重复的与以前测试一致的结果；
### 5.1 专属性
需要进行风险评估，以理解需要何种程度的专属性才能区分测试样品和在同一加工区生产的其他蛋白；

Peptide mapping is a comparative technique confirming that the primary structure of the test protein matches that of the reference protein

参考物质与以下比较，建立专属性
- 结构相关的蛋白：如，针对其他靶点的抗体；
- 同一加工区生产的其他蛋白；
具体做法：结构相关蛋白或其它蛋白产品，参考物质，参考物质与前者1:1混合物，分别酶切，上机分析；

证明肽图的专属性是否受氨基酸侧链修饰影响
对参考物质进行强制降解试验：不同pH，温度，化学试剂；分别对强制降解样品和未处理的参考品做肽图，进行比较；

### 5.2 重复性和中间精密度
指标：相对峰面积和相对保留时间

One approach is to make peak response and peak retention time comparisons that are  expressed relative to a highly reproducible reference peak within the same chromatogram

### 5.3 Robustness（耐用性）



梯度与保留时间
Spicer, V., Grigoryan, M., Gotfrid, A., Standing, K. G., & Krokhin, O. V. (2010). Predicting
retention time shifts associated with variation of the gradient slope in peptide RP-HPLC. Analytical chemistry,
82(23), 9678-9685.

## 问题
### 问题1
蛋白纯度（purity）-amino acid misincorporation, disulfide bond scrambling, post-translational modifications and degradation, 可以使用quantitative peptide mapping测定，如何测定？
>   The purity of the test protein with regard to amino acid misincorporation or other misassembly such as disulfide bond scrambling, post-translational modifications, and degradation can be determined using a quantitative  peptide map

## 相关笔记

- Analytical technology/RP反相/反相色谱柱.md
- Analytical technology/RP反相/梯度洗脱.md
- Analytical technology/HPLC色谱柱相关知识.md
- Analytical technology/RP反相/肽图.md
- Analytical technology/试剂溶剂性质.md





[链接](https://app.yinxiang.com/shard/s33/nl/1/d9fd8a25-e056-4c6d-9ff8-dd4f4116f04e?title=SEC%E6%A3%80%E6%B5%8B)

## 相关笔记

- Analytical technology/SEC-HPLC/SEC SOP.md
- Analytical technology/HPLC色谱柱相关知识.md
- Antibody-Characterization/mAb特性表征.md
- Analytical technology/RP反相/梯度洗脱.md
- Mass Spectrometry/MS基本原理.md





[减少SEC分析中的次级相互作用-流动相优化](../../Antibody-Characterization/减少SEC分析中的次级相互作用-流动相优化.md)
SEC色谱柱信息汇总


the elution process should be controlled only by **entropy**, and therefore the solvent should assure the minimization of the **enthalpic interactions** (ionic and hydrophobic) of macromolecular species with stationary phase

- 减少分析物和色谱柱之间的electrostatic interactions
	- pH
	- 盐浓度
	- 氨基酸添加剂：精氨酸，甘氨酸和丙氨酸；10%以内
- 减少hydrophobic interaction
	- 有机试剂：5-10%
## 色谱柱填料
- Porous silica materials (with or without surface modification)
	- 在bare silica表面化学键和1,2丙二醇功能基团
		- 在填料表面形成亲水层
		- 中和二氧化硅表面酸性硅羟基，减少硅羟基与大分子相互作用，改善峰型；
		- ethylene-bridged hybrid inorganic-organic (BEH) material：增加填料的化学稳定性，更耐高压，减少硅醇基活性；
- Polymeric materials
	- hydrophilic crosslinked materials
	- 凝胶
	- 经过修饰的凝胶：葡聚糖凝胶-Sephadex; 琼脂糖凝胶-Sepharose；
![](/images/05仪器与分析技术-色谱分析-hplc/SEC-HPLC-resin1.webp)
![](/images/05仪器与分析技术-色谱分析-hplc/SEC-HPLC-resin2.webp)

## 方法开发
> [Developing SEC Methods for Biologics Analysis - Developing SEC Methods for Biologics Analysis (windows.net)](https://chromacademyliveblobs.blob.core.windows.net/chromacademy-live-blobs/5ec854fe-a939-4ca3-a851-018d83d426ef/index.html?endpoint=https://www.chromacademy.com/umbraco/api/&auth=Basic%20ZGNiN2QxYjQ5Mjc1ZWQzOWFkYzhhNDdjNDA3NzJiOWQ6YThkYWVmYzJiYjJiMjk4NDhkNzI2NGE1Y2I5MDY0YmE=&actor=%7B%22objectType%22:%22Agent%22,%22name%22:%5B%22-%22%5D,%22mbox%22:%5B%2220015375@myrp.edu.sg%22%5D%7D&moduleId=5ec854fe-a939-4ca3-a851-018d83d426ef&activity_id=Developing%20SEC%20Methods%20for%20Biologics%20Analysis&activity_name=Developing%20SEC%20Methods%20for%20Biologics%20Analysis&memberId=dce079ed-7d62-48f7-8838-ed419b244774&LearningArticleNodeGuid=8430a1fe-5482-41ff-b894-a7f247d78b26#/lessons/ZmEDovaAuu1_kwkH6UVcr_a5kVACskmf)
> [Chapter 11 - Stationary Phases and Columns for Size Exclusion](https://doi.org/10.1016/B978-0-12-803684-6.00011-1 "Persistent link using digital object identifier")
> [Size Exclusion Techniques - Selection of Columns and Conditions for Bio Size Exclusion Chromatography (windows.net)](https://chromacademyliveblobs.blob.core.windows.net/chromacademy-live-blobs/ac6a35ad-422f-42fe-bd7d-17676ac8f8ab/index.html?endpoint=https://www.chromacademy.com/umbraco/api/&auth=Basic%20ZGNiN2QxYjQ5Mjc1ZWQzOWFkYzhhNDdjNDA3NzJiOWQ6YThkYWVmYzJiYjJiMjk4NDhkNzI2NGE1Y2I5MDY0YmE=&actor=%7B%22objectType%22:%22Agent%22,%22name%22:%5B%22-%22%5D,%22mbox%22:%5B%2220015375@myrp.edu.sg%22%5D%7D&moduleId=ac6a35ad-422f-42fe-bd7d-17676ac8f8ab&activity_id=Size%20Exclusion%20Techniques&activity_name=Size%20Exclusion%20Techniques&memberId=dce079ed-7d62-48f7-8838-ed419b244774&LearningArticleNodeGuid=dcc87f07-4170-45d6-8da3-d125fcb11be0#/lessons/AuOIetrOWyVMytrDCU8wJpgiq_hJUnSB)
### 1. 色谱柱填料孔径
孔径大小能影响分辨率，所以需要测试不同孔径，以匹配分析物；尤其在不知道分析物的流体力学半径的情况下；
选择合适的填料表面孔径大小（看柱子孔径规格：多少A，1nm=10A），单体和二聚体都能渗进孔内；
原则：the pore size of the column should be **three times** the diameter of the molecules of interest；
![](/images/05仪器与分析技术-色谱分析-hplc/SEC-HPLC-size.webp)

例如thyroglobulin-甲状腺球蛋白，670kDa，其流体动力学半径（hydrodynamic radius）10nm；抗体，150kDa，流体动力学半径5nm；对于抗体来说，要分离单体和聚体，最佳孔径为聚体分子流体力学半径的三倍，即30nm=300A；

孔径300A，最佳
![](/images/05仪器与分析技术-色谱分析-hplc/SEC-HPLC-pore-size.webp)
孔径200A，偏小；抗体单体出峰晚于BSA二聚体；
![](/images/05仪器与分析技术-色谱分析-hplc/1-SEC-HPLC-pore-size.webp)
孔径450A，偏大；分辨力差
![](/images/05仪器与分析技术-色谱分析-hplc/SEC-HPLC-pore-size3.webp)

### 2.色谱柱尺寸
内径影响流速和进样体积
两种规格：
- 4.6mm：流速一般为0.35ml/min
- 7.8mm：流速一为1.0ml/min
流速不宜过快，分析物需要足够的时间扩散进入孔内静态的流动相中，或者从中扩散出来；

色谱柱柱长

### 3.柱温
最好采用柱温箱控温；温度的变化，影响粘度，影响到柱压和分析物扩散过程；


### 4.流动相
ionic strength
pH：靠近蛋白pI，限制次级相互作用
buffer composition

初始方法
![](/images/05仪器与分析技术-色谱分析-hplc/SEC-HPLC-initial-method.webp)



## 中国药典

### 0514 分子排阻色谱法
色谱柱填料：
- 亲水硅胶
- 凝胶
- 经过修饰的凝胶：葡聚糖凝胶-Sephadex; 琼脂糖凝胶-Sepharose；

  高分子杂质测定法


## USP

## 相关笔记

- Analytical technology/SEC-HPLC/SEC SOP.md
- Analytical technology/HPLC色谱柱相关知识.md
- Antibody-Characterization/mAb特性表征.md
- Analytical technology/RP反相/梯度洗脱.md
- Mass Spectrometry/MS基本原理.md




[Size-Exclusion Stationary Phases](https://doi.org/10.1016/B978-0-12-803684-6.15006-1 "Persistent link using digital object identifier")

## 相关笔记

- Analytical technology/SEC-HPLC/SEC SOP.md
- Analytical technology/HPLC色谱柱相关知识.md
- Antibody-Characterization/mAb特性表征.md
- Analytical technology/RP反相/梯度洗脱.md
- Mass Spectrometry/MS基本原理.md




色谱柱分类
[doi.org/10.1016/B978-0-12-803684-6.15001-2](https://doi.org/10.1016/B978-0-12-803684-6.15001-2 "Persistent link using digital object identifier")

## 相关笔记

- Analytical technology/HPLC色谱柱相关知识.md
- Analytical technology/USP Classification of HPLC Columns.md
- Analytical technology/试剂溶剂性质.md
- Analytical technology/RP反相/梯度洗脱.md
- Analytical technology/SEC-HPLC/SEC SOP.md
