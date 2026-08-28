---
draft: true
reviewNotes:
  - "出现源文没有的数据: ['574.3da']"
title: "蛋白质与多肽测序的碎裂离子解析：命名体系、质荷比计算与手动谱图解读"
date: 2026-08-26
category: "05仪器与分析技术"
primaryTag: "05仪器与分析技术/质谱/测序sequencing"
description: "本文围绕蛋白/多肽测序中的碎裂离子主题，依次梳理测序策略（Edman 降解与基于质谱的 de novo sequencing）、碎裂离子命名体系（Roepstorff/Biemann）与质荷比计算方法，比较不同碎裂方式产生的离子类型差异，并通过三个完整案例演示手动谱图解析流程，最"
tags:
  - "05仪器与分析技术/质谱/测序sequencing"
sourceNotes:
  - "Antibody-Characterization/protein sequencing与离子类型.md"
---

本文围绕蛋白/多肽测序中的碎裂离子主题，依次梳理测序策略（Edman 降解与基于质谱的 de novo sequencing）、碎裂离子命名体系（Roepstorff/Biemann）与质荷比计算方法，比较不同碎裂方式产生的离子类型差异，并通过三个完整案例演示手动谱图解析流程，最后归纳谱图判读的实用技巧与肽段衍生化策略。

> [!abstract] 摘要
> 本文系统讲解蛋白/多肽测序策略、肽段碎裂离子命名体系与计算方法，并结合三个完整的手动谱图解析实战案例，介绍如何通过碎裂离子系列推导多肽序列。

> [!summary] 核心要点
> - 测序策略对比：化学Edman降解 vs 基于质谱的de novo sequencing / 数据库检索鉴定（bottom-up/top-down）。
> - 离子命名体系：Roepstorff/Biemann命名法的a/b/c/x/y/z骨架碎裂离子、immonium ions（诊断氨基酸组成）、satellite离子（d/v/w，用于区分I/L）。
> - 碎裂方式差异：低能CID主要产生b/y离子（伴脱氨脱水）；高能CID产生d/v/w离子（边链断裂）；ETD/ECD主要产生c/z离子并保留不稳定PTM。
> - 碎裂离子质荷比计算公式及b离子不易观察到（b1）、a2/b2离子对确认序列等实用判读技巧。
> - 三个完整案例：从单/双电荷前体离子出发，逐步定位b/y离子系列、验证反离子质量、结合MS3确认未覆盖序列。
> - 肽段衍生化策略：同位素标记（H6/D6-乙酸酐）简化离子系列归属，N端强碱性/强酸性基团修饰调控b/y离子生成偏向。

## 测序策略：化学法与质谱法的边界

化学法 Edman 降解不能分析化学修饰的蛋白；基于质谱的肽段测序分析含等重氨基酸的序列时会出现错误，不能对任意蛋白进行 unambiguous sequencing。但质谱可以有效地进行蛋白鉴定（protein identification），其基础是序列与数据库记录的关联（sequence correlation with database records），对应 bottom-up 与 top-down 两种策略。

De novo sequencing 通常难以给出完整且无歧义的结构解析（seldom allows for a complete and unambiguous structure elucidation）。多数问题源于可能断裂的键数量过多，且并非所有记录的碎片离子都是 sequence-specific 的。

数据采集有几点经验：

- 关于碰撞能量：碰撞能量先尽可能低，进行尝试，原因是避免断裂键太多、峰少、容易注释；如果获取的信息太少，再提高碎裂能量；也可采用 automatic adjustment of the collision energy-ramping。
- 关于离子电荷数：如果采用的是 ESI 离子化技术，use all the multiple-charged ions for fragmentation；原因是单电荷和双电荷前体离子的碎片谱图往往提供不同但互补的信息（different but complementary fragmentation）。
- Good practice suggests starting the analysis with a spectrum showing more high intensity peaks, preferably equally abundant over the whole mass range。
- multistage fragmentation: never too much data, used for sequence validation。

测序流程依次为：识别 sequence-specific 离子（a、b、c、x、y、z）；利用 non-sequence specific 但具有诊断价值的 immonium ions；将 sequence-specific 离子识别并归属到正确的离子系列；相邻离子间的质量差对应氨基酸双自由基（amino acid biradical，亦称为 amino acid residue）的质量。氨基酸残基定义为氨基酸分子去掉 α-氨基上的一个氢和 α-羧基上的一个羟基后的部分。

## 碎裂离子命名体系与离子类型

碎裂离子类型受四个因素影响：

- primary sequence：碱性基团的数量和位置强烈影响各离子系列在谱图中的丰度与强度；
- the amount of internal energy；
- 能量引入方式：CID、SID、HCD、ETD、EThcD 等；
- charge state。

### Roepstorff 与 Biemann 命名法

Roepstorff 命名法将骨架断裂产生的离子分为 a/b/c（N 端系列）与 x/y/z（C 端系列）[^1][^4]，即 backbone fragmentation：

![](/images/protein-sequencing与离子类型/202204241039321.webp)
![](/images/protein-sequencing与离子类型/202204280712143.webp)

注意：**c、y离子从前体离子中抓了一个质子，其它离子-H**；上图离子带一个单电荷。

Biemann 命名法[^5]在 Roepstorff 基础上引入 immonium ions 和 satellite ions：

![](/images/protein-sequencing与离子类型/202204241042093.webp)

### Internal cleavage 与 immonium ions

双骨架断裂（double backbone cleavage）产生内部碎片离子，通常是 b 型与 y 型断裂组合，形成 amino-acylium ions（氨基酰基离子）；也可能通过 a 型与 y 型断裂，产生 amino-immonium ion：

![](/images/protein-sequencing与离子类型/202204262244231.webp)

Immonium ion[^2] 是一种只含单个侧链的内部碎片（internal fragment with just a single side chain），由 a 型与 y 型断裂组合形成，实质是氨基酸残基的碎片离子；其产生需要肽骨架在同一残基的两侧断裂。质量计算公式为：immonium ion质量= 氨基酸相对分子质量-18(H2O)-28(CO)+1(H)。

![](/images/protein-sequencing与离子类型/202204252215923.webp)

Immonium ions 作为诊断离子，用于判断是否存在某一氨基酸，但不能判断其位置；缺少某一 immonium ion 并不意味着对应的氨基酸不存在。下表中黑体字代表丰度最强的峰（the most abundant peaks），其它是信号弱的峰。

![](/images/protein-sequencing与离子类型/202204262253294.webp)
![](/images/protein-sequencing与离子类型/202209031518432.webp)

### Satellite ions：d/v/w 与 I/L 区分

卫星离子的生成本质是要形成共轭体系；能量很高时，边链断裂。Collision induced dissociation of ions at keV energies can generates additional ion types due to side chain cleavages。

![](/images/protein-sequencing与离子类型/202204272122764.webp)

- d离子：N端离子，a型断裂+边链β碳和γ碳间的键断裂，R'为β碳上的取代基，即 the loss of an olefin(烯烃) from the side chain of the C-terminal amino acid of a_n ion；对于L，质量掉43Da（CH3CHCH3)；对于I，质量掉29Da（掉CH2CH3）。
- v离子：C端离子，y型断裂+alpha碳和β碳间的键断裂，侧链完全断裂。
- w离子：C端离子，z型断裂+边链β碳和γ碳间的键断裂，R'为β碳上的取代基；用于区分L和I。

![](/images/protein-sequencing与离子类型/IL-differentiation.webp)

## 碎裂方式与子离子质荷比计算

### 不同碎裂方式产生的离子类型

- 低能 CID（Low Energy CID）：主要沿骨架断裂，主要产生 b 和 y 离子；伴随脱氨、脱水；不产生边链断裂的 satellite ions。
- 高能 CID（High Energy CID）：不像低能 CID 那样容易丢失氨或水；d、v、w 离子出现，肽骨架和边链均断裂。d 离子＝a 离子边链部分断裂；v 离子＝y 离子边链完全断裂；w 离子＝z 离子边链部分断裂。
- Post Source Decay（MALDI-TOF PSD）：最丰富的碎片离子类型是 a、b 和 y。
- ETD/ECD：主要产生 c、z+1、z+2 离子，并保留不稳定的 PTM。

### 子离子质荷比计算公式

![](/images/protein-sequencing与离子类型/202204280736513.webp)

说明：**c、y离子（带氨基）从前体离子中抓了一个质子，其它离子-H**。

计算规则：

1. N：the molecular weight of neutral N-terminal group；[N]=**+1Da**
2. C：the molecular weight of neutral C-terminal group，[C]=**+17Da**
3. M：the molecular weight of neutral amino acid residues，残基质量；
4. 注意：上表是计算中性分子的质量；如果要计算阳离子质荷比，加质子，再除以质子数；
5. 对于b/y离子：b离子-`[N]+M-H`; y离子-`[C]+M+H`；
6. 对于a/x离子：a离子-`[N]+M-CO-H`; x离子-`[C]+M+CO-H`;
7. 对于c/z离子：c离子-`[N]+M+NH+H`; z离子`[C]+M-NH-H`；
8. c离子比b离子大17Da；z离子比y离子小16Da；
9. 计算中性质量时，凡属c/y离子，都+H，其它都-H。

### 为什么 b 离子要减 1（-H）

根据 mobile proton model 理论，质子（电荷）先移动到酰胺键上的氨基上；接着 n-1 位处氨基酸的羰基氧亲和攻击 n 位处氨基酸的羰基碳，形成一个复合物，再解离成 b 离子和 y 离子；y 离子 N 端氨基带走了一个质子，那么 b 离子就少了一个质子。外推：凡属c/y离子（含断裂位点附近的氨基），都+H，其它都-H。

> Mobile and localized protons: a framework for understanding peptide dissociation (doi: 10.1002/1096-9888(200012)35:12<1399::AID-JMS86>3.0.CO;2-R）

![](/images/protein-sequencing与离子类型/202204232048545.webp)

以一个电荷为例：

![](/images/protein-sequencing与离子类型/202204241103915.webp)

注意：

- 是残基质量，即氨基酸质量减去18；
- a离子在b离子基础上，掉一个CO（28），所以-28；
- b离子为什么不用加18，因为b离子C端肽键断裂，留下羰基，C端氨基酸也脱水了；而y离子C端羧基是完整的，未脱水，需要+18；
- 相邻离子，相差一个残基质量；
- amino acid immonium ion质量计算：**残基质量-27（-CO+H）**

![](/images/protein-sequencing与离子类型/202204242301374.webp)

## 影响碎裂的因素与低能CID谱图特征

### 影响肽段碎裂的因素

- 肽段 m/z：
  - 大小：larger peptides require more energy to fragment;
  - 电荷数：higher charge states require less energy to fragment;
  - 氨基酸组成：amino acid composition of peptide;
- 碰撞条件：
  - 能量大小：more energy induces more fragmentation;
  - collision gas type and pressure;
- 质谱仪：
  - laser power（MALDI-MS/MS）
  - ion trap vs Q-Tof

![](/images/protein-sequencing与离子类型/202204282156970.webp)

- 解离方式（CID vs ETD/ECD）：
  - CID for precursor <5kDa；
  - ETD/ECD not as mass dependent。

### 质谱采集的考虑

- available modes of fragmentation
- available modes of product ion analysis
- scan rates
- scan range - 1/3 rule on traps
- mass accuracy
- mass resolution

### 低能CID谱图的常见观察

- b2/a2 pair：通常可以观察到 b2/a2 离子对；a2 是 b2-28；b1 基本观察不到（essentially never observed），因为 N 端没有邻位的羰基协助形成 oxazolone 环；通常可以看到来自 N 端残基的强 immonium ion，与 a1 离子相同。
- 不含碱性残基（或末端附近无碱性残基）的肽段，可能在内部碱性残基周围发生广泛碎裂。
- 增强碎裂：C-terminal side of His（H-Xaa）；C-terminal side of Asp and Glu（D/E-Xaa）；Asp-Pro。
- 抑制碎裂：Gly，特别是 Gly-Gly 或 Gly-Ala 序列。
- 不稳定的翻译后修饰可能发生中性丢失。

### 难以区分的质量组合与氨基酸参考数据

除 I/L 外，以下质量组合也难以区分：

![](/images/protein-sequencing与离子类型/202204282202820.webp)

此外还有：

- AlaAsn and GlyGln
- SerGlu and ThrAsp
- Phe and Met(O)
- Trp, GlyGlu and SerVal
- Arg and GlyVal

常用氨基酸参考数据：

![](/images/protein-sequencing与离子类型/202205011550903.webp)
![](/images/protein-sequencing与离子类型/202205011551285.webp)
![](/images/protein-sequencing与离子类型/202205011808795.webp)

## 手动谱图解析的三个完整案例

### 案例一：574.3 Da 单电荷前体（离子阱）

precursor mass is 574.3，singly charged；仪器是 ion-trap analyzer。

![](/images/protein-sequencing与离子类型/202205011126164.webp)

**Step 1**：从前体质量附近开始，识别 N 端和 C 端的前几个氨基酸。在谱图中，b_n--m/z 556.1 对应前体离子脱水，尽管这个峰是 non-sequence specific，但是可以作为 a specific starting point for the entire b-ion series。

**Step 2**：寻找 b 系列中其他峰，只需查找质量差等于氨基酸残基质量的峰：

- b<sub>n-1</sub>：425.1 跟556.1相差131.1，对应的是M；
- b<sub>n-2</sub>：278.0跟425.1相差147.1，对应的是F；
- b<sub>n-3</sub>：221.0跟278.0相差57.0，对应的是G;

再往下没有更小的碎裂离子，原因是离子阱分析器采集时应用的低质量截止（the low-mass cut-off of the ion trap analyzer）。可以利用离子阱多级碎裂模式，通过选择和碎裂二级谱图中低质荷比的离子，采集三级谱图，拓展碎裂的有效质荷比范围。

**Step 3**：寻找 a 离子。b 离子通常伴有 a 离子（来自不同的骨架断裂）；a 离子比对应 b 离子低 28 Da（丢失 CO）；a/b 离子对可作为序列归属正确性的高置信度标记，especially if they cover multiple adjacent AA residues。397.2 is a-ion accompanying 425.1 b-ion。

此时已鉴定出部分序列 GFM-OH，鉴定多肽质量为353.1Da（57.02[G]+147.06[F]+131.04[M]+18.01[H2O]），完整多肽离子质量为573.3Da（574.3-1），完整多肽质量-鉴定多肽质量=220.2Da，很可能还差两个氨基酸。

**Step 4**：寻找 y<sub>n-1</sub> 峰。N 端氨基酸可通过前体离子质量与最重 y 离子（y<sub>n-1</sub>）的质量差识别。与 N 端系列不同，低能碎裂中 y 离子很少伴随 x 或 z 离子。本例中大部分最强峰属于 N 端碎片，C 端候选峰强度低，注释需谨慎——低强度峰可能来自检测器噪声；但只要能看到两到三个氨基酸的序列串，且该信息与其他结果一致，就可以用于测序。

> Page 208
> the majority of most intense peaks belong to  N-terminal fragments, leaving only low intensity peaks for potential C-terminal ions. In  such cases, care should be taken on peak annotation as such low intensity peaks can also result from detector noise. However, they can be used for sequencing as long we can see at least a two to three AA sequence string, and the information obtained this way is consistent with other results

在高质量区发现411.3跟574.3相差163，对应的W；继续寻找 y 系列，发现354.1和297.1对应两个G，N端序列为NH2-YGG。测序结果为NH2-YGGFM-OH。

**Step 5**：验证。首先检查所得序列的分子量与 precursor 质量吻合；其次，对二级谱图中的 b3 离子做 MS3 碎裂以确认其身份——从谱图中发现221.0对应的是b2离子，193对应的a2离子，136.1对应的是a1离子，a2和a1相差一个G氨基酸。

![](/images/protein-sequencing与离子类型/202205011314932.webp)
![](/images/protein-sequencing与离子类型/202205011320058.webp)

本例肽段只含中性氨基酸，正离子模式下唯一保留电荷的碱性基团是 N 端氨基，因此最强峰属于 N 端碎片，对应 a 和 b 离子系列。

### 案例二：双电荷与单电荷前体的互补分析

本例肽段略大，同时使用单电荷和双电荷前体。测序分析优先从多电荷母离子开始，因为 ESI 产生的多电荷离子碎裂效率高，能比单电荷母离子提供更多的 sequence-specific fragments ions。

![](/images/protein-sequencing与离子类型/202205011531850.webp)
![](/images/protein-sequencing与离子类型/202205011532940.webp)

双电荷前体碎裂谱图的判读规则：

- 前体离子带两个电荷，碎裂离子可能是一个电荷，也可能是两个电荷；
- 所有两个电荷的碎裂离子，其质荷比小于前体离子的；
- 一个电荷的碎裂离子，质荷比有可能大于前体离子的；质荷比超过前体离子的，都是单电荷离子；
- 质荷比小于前体离子的，有单电荷和双电荷的碎裂离子；分析每一个isotopic cluster获得电荷数；
- 有时电荷数不同的碎裂离子，其质荷比差异非常小，无法可靠的获得其电荷数。在这种情况下，用未知电荷数的峰测的序列需要用其它碎裂离子来确认。

**Step 1**：从双电荷前体（precursor ion: 550.1）的碎片谱图开始测序。

测C端序列（双电荷 b 离子）：

- b<sub>n</sub>-H2O:  540.8    -9
- b<sub>n-1</sub>-H2O:  505.3,与前体离子相差35.3，为A, first C-terminal amino acid;
- b<sub>n-2</sub>-H2O:  461.8,与前体离子相差43.5，为S,  second C-terminal amino acid;
- b<sub>n-3</sub>-H2O:  397.7,与前体离子相差64.1，为K/Q;
- C端氨基酸序列：...(K/Q)SA

测N端序列（双电荷 y 离子）：

- y<sub>n-1</sub>: 476.3,与前体离子相差73.9，为F, first N-terminal amino acid;
- y<sub>n-2</sub>: 447.8,与前体离子相差28.5，为G, second N-terminal amino acid;
- y<sub>n-3</sub>: 419.4,与前体离子相差28.4，为G，third  N-terminal amino acid;
- y<sub>n-4</sub>: 345.7,与前体离子相差73.6，为F，fourth N-terminal amino acid;

目前推测的序列为：H-FGGF-....-(K/Q)SA-OH。

**Step 2**：用双电荷前体碎片谱图中的单电荷系列验证已获得的序列。

验证C端：

- b<sub>n-1</sub>: 1027.6，未发现此碎裂离子；
- b<sub>n-2</sub>: 922.5,与前体离子相差176（71+87+18），为SA;
- b<sub>n-3</sub>: 794.4,与前体离子相差128，为K/Q;

该序列串无法进一步延伸。

验证N端：

- y<sub>n-1</sub>: 951.5,与前体离子相差147.1，为F，N端首个氨基酸；
- y<sub>n-2</sub>: 894.5,与前体离子相差57.02，为G；
- y<sub>n-3</sub>: 837.4,与前体离子相差57.02，为G；
- y<sub>n-4</sub>：690.4,与前体离子相差147，为F；
- y<sub>n-5</sub>: 589.4,与前体离子相差101，为T；
- y<sub>n-6</sub>: 532.3,与前体离子相差57，为G；

再往低质量区处理很困难，因为大量单电荷和双电荷峰混合在一起。这进一步验证了双电荷离子碎片谱图获得的序列信息，同时获得额外信息 FGGFTG....

**Step 3**：分析单电荷母离子的碎片谱图。Short examination of the fragment ion spectrum from a singly charged precursor is not particularly helpful。

![](/images/protein-sequencing与离子类型/202205021516231.webp)

这是 de novo sequencing 中典型的情形：存在一段没有任何离子系列覆盖的序列。并非所有氨基酸间的键强度相同，其中一些可能对碰撞特别耐受，导致质量位移（以及对应残基）缺失。处理办法有两种：

- 逐一检查谱图中的绝大多数峰（包括低强度峰），尝试寻找缺失的序列串；此法耗时且容易出错，因为某些质量位移可能纯属巧合匹配（fitted by pure coincidence）。
- 计算缺失序列可能的氨基酸组成，只检查有限氨基酸组合对应的质量位移。

**Step 4**：计算缺失序列可能的氨基酸组成。

1097.6-870=227.6

- three amino acid pairs：AlaArg, (Ile/Leu)Asn, (Gln/Lys)Val；
- two triplets：AlaGlyVal and GlyGly(Leu/Ile)

仔细检查谱图，发现461.8（双电荷b离子）处的峰，观察isotopic cluster，发现有两个重叠的碎裂离子，低质量的shoulder peak461.3 为另一个碎裂离子，其与532.3（y<sub>n-6</sub>)相差71(A)，那么461.3属于y<sub>n-7</sub>离子；与305.3（y<sub>3</sub>=y<sub>n-8</sub>），相差156，为R。因此，得出全长序列为 H-FGGFTGAR(K/Q)SA。

![](/images/protein-sequencing与离子类型/202205021615231.webp)

**Step 5**：寻找间接线索。缺失的氨基酸之一是强碱性的精氨酸。肽骨架断裂后，含精氨酸的碎片优先保留电荷，因此谱图中大多数碎片离子都含碱性氨基酸，其质量位移反而无法找到。如果下一个氨基酸是碱性的赖氨酸（而非谷氨酰胺），这一效应会更加强烈。This phenomenon also explains why any b-ions below b8 (after loss of lysine) cannot be found in the case of a singly charged precursor fragmentation。

如果多肽来自天然来源，可用序列数据库搜索可能的序列。本例序列来自 Nociceptin/OrphaninQ (1–11) fragment，序列为 H-FGGFTGARKSA-OH。

![](/images/protein-sequencing与离子类型/202205021732315.webp)
![](/images/protein-sequencing与离子类型/202205021633710.webp)

本例含两个碱性氨基酸，位于序列中间偏 C 端。谱图包含大量 C 端和 N 端碎片峰，双电荷离子丰富，两个碱性氨基酸均存在于碎裂离子中。碱性残基的存在使 b/y 离子数量更均衡，但也导致碱性残基附近的键断裂碎片很难获得。

### 案例三：胰蛋白酶肽的离子系列归属

该肽来自未知蛋白的胰蛋白酶解，是其中最大的肽段。C 端精氨酸和 N 端氨基均能保留电荷，因此谱图上几乎可以看到完整的 b/y 离子系列。通常精氨酸和赖氨酸对质子的亲和力略高于 α-氨基，因此 C 端离子强度更高。

![](/images/protein-sequencing与离子类型/202205021650002.webp)

观察谱图特征：

- almost no abundant doubly charged ions；
- does not cover the mass range near the precursor m/z region；
- there are a number of very intense peaks with mass differences specific for particular amino acids。

从274.2开始，可以获得部分序列，但不知道这些离子是N端还是C端碎裂离子。

| peak   | mass shift | amino acid     |
| ------ | ---------- | -------------- |
| 387.4  | 113.2      | Leu/Ile        |
| 500.6  | 113.2      | Leu/Ile        |
| 571.4  | 70.8       | Ala            |
| 686.7  | 115.3      | Asn(114.2)     |
| 813.6  | 126.9      | Lys/Gln(128.0) |
| 960.7  | 147.1      | Phe            |
| 1017.7 | 57         | Gly            |
| 1180.8 | 163.1      | Tyr            |
| 1309.6 | 128.8      | Glu            |

得到序列：(L/I)(L/I)AN(K/Q)FGYE，但不知道N端或C端。有三种基本方法鉴定离子系列：

1. 最直接的方法基于 a-ions linked to b-ions：如果已识别峰中存在至少一到两个 28 Da 的质量位移，有较大概率是找到了 b 离子系列。
2. 第二种方法更耗时但结果更可靠：因为序列串覆盖了大部分肽段，未知末端碎片不超过两到三个氨基酸，其质量可能足够特异以确定归属。
3. 第三种方法寻找反向离子系列：同一键断裂产生的 b 离子和 y 离子质量之和等于整个前体质量加 1 Da。例如，若肽段有10个氨基酸，b8 与 y2 离子质量之和等于单电荷前体质量 +1 Da。

本例采用第三种方法。两个电荷的母离子741.0，那么一个电荷的母离子质荷比为1481。

- 从1180.8入手，其相反离子质荷比为1481+1-1180.8=301.2；
- 1017.7的相反离子质荷比为1481+1-1017.7=464.3，在谱图找到，与301.2相差163.1，为Y，进一步证实了该氨基酸；
- 1309.6的相反离子质荷比为1481+1-1309.6=172.4，未找到，与301.2相差128.8，为E；
- 从274.2入手，其反离子质荷比为1207.8，与1306.7相差98.9，为V；这不仅证明之前归属的序列正确，还向 N 端扩展了一个残基：V(L/I)(L/I)AN(K/Q)FGYE；
- 1207.8这一系列离子的下一个离子为1306.7，其与一个电荷母离子1481相差174.3(156+18脱水)，为R；该肽来源于胰蛋白酶的酶切物。

到此为止，获得的多肽序列为：. . .EYGFQNALIVR-OH。剩下171.1，可能是两个氨基酸对：G（L/I) 或 AV，目前数据无法证实是哪种组合，也无法鉴定氨基酸的顺序。完整测序需要额外的串联质谱数据，最好是对其中一个低质量 y 离子做 MS3 碎裂；如果该肽来自生物样本，可以使用数据库来鉴定剩下的氨基酸组成和顺序：H-LGEYGFQNALIVR-OH。

脱氨（ammonia，-17Da）来源于酰胺（N/Q）或R残基；本例中 high-mass b-ions（b7-b11）都有-17Da峰伴随，b7以下则无；脱水来自 S/T 侧链-OH 的消除反应。

![](/images/protein-sequencing与离子类型/202205031036907.webp)

## 实用技巧与肽段衍生化

### 谱图解析的实用技巧

- 低质量区：y1 离子质量等于 C 端氨基酸质量 +18 Da；b1 离子质量等于 N 端氨基酸质量 +1 Da（含 N 端氢）。这些离子可用于将序列串归属到 N 端或 C 端离子系列。低质量区结合高能碎裂时，immonium ions 不提供氨基酸顺序信息，但可作为高度特异的标记判断特定氨基酸是否存在。
- 高质量精度分析仪：在离子阱实验中，可测序的最大肽约为15个氨基酸；更好的离子分辨率可减少重叠峰问题，或基于精确质量区分赖氨酸和谷氨酰胺。
- 数据库搜索工具：如果肽段来自生物材料，应使用序列数据库（Mascot、Protein Prospector、Sequest）。
- 酶解：
  - Edman Degradation；
  - Carboxypeptidase Y：从 C 端连续切除氨基酸。在合适的酶活与孵育时间下，可产生包含原肽和逐级丢失 C 端氨基酸的肽阶梯（ladder），相邻肽的质量差对应连续的 C 端氨基酸；
  - Aminopeptidase N：类似地从 N 端切除；
  - 序列特异性酶：trypsin 切割 Lys 和 Arg 的 C 端侧（下一个氨基酸是 Pro 时除外）；protease V8 切割 Asp 和 Glu 的 C 端侧。主要困难是即使完成所有片段的测序，仍需确定片段在蛋白内的顺序；解决办法是用两种不同特异性的酶独立实验，或对原始肽段直接获得部分 de novo 测序信息。

### 衍生化的目的

de novo sequencing 有时会失败，原因是串联质谱图质量低，很可能是由于某一多肽的碎裂类型不好（unfavorable fragmentation pattern of a given peptide）。化学衍生化的两个目的：

- 通过促进或抑制特定离子系列的形成，简化碎裂模式（simplification of the fragmentation pattern）；
- 稳定同位素标记，用于简单地将离子归属到正确的离子系列（stable-isotopic labelling for simple assignment of ions to proper ion series）。

### 简化碎裂模式的衍生化策略

多数衍生化技术修饰肽段的 N 端，原因是相对于 C 端羧基，N 端氨基更容易修饰；此外 K 侧链氨基与 N 端氨基的 pKa 存在差异，某些反应仅修饰 N 端氨基，K 侧链氨基保持完整。羧基修饰（如酯化 esterification）倾向于同时影响 C 端羧基和酸性侧链基团。

氨基酸的化学性质对碎裂模式影响显著：碱性基团的数量和位置强烈影响各离子系列在谱图中的丰度与强度。因此，引入强碱性基团可以促进某些离子的生成，而强酸性基团效果相反。

大多数应用基于 tryptic peptides。这些多肽 C 端有碱性氨基酸，谱图中有大量 y 离子，b 离子强度相对较低，不能提供重要的序列信息。在 N 端引入强碱性基团，如 dimethylalkylammonium acetyl (DMAA) 或 tris(2,4,6-trimethoxyphenyl)phosphonium acetate，可以显著增强 b 离子和 a 离子的信号强度。相反，在 N 端引入强负电荷的 sulfonic acid，则从谱图中完全消除 b 离子，因此促进 y 离子的形成。

此类修饰在肽段碎裂效率差（poor fragmentation efficiency）或 sequence-specific 离子数量有限时很有帮助。

### 稳定同位素标记

化学标记的核心思路是简化谱图峰归属：如果肽段的 C 端或 N 端被特异性同位素簇标记，标记离子在谱图中容易识别，序列串的确定不再是问题。

- H6/D6-乙酸酐（1:1）标记 N 端：衍生后，一半多肽的 N 端含 light acetyl groups，另外一半含 heavy acetyl group；两种多肽分子量相差3Da，混合物的谱图呈现 characteristic isotopic pattern with "doublets" of the equally intense peaks；C 端离子不含同位素标签，以简单单峰出现；两种离子系列立即被区分。
- N 端乙酰化：仅修饰 N 端氨基，不影响赖氨酸侧链；主要缺点是乙酰基封闭了 N 端在碎裂过程中保留电荷的能力，若肽段 C 端含碱性氨基酸（tryptic peptides 即如此），N 端离子系列会变弱。
- 其他 N 端修饰试剂：succinic anhydride、propionic anhydride、N-acetoxysuccinimide。
- C 端标记（18O）：消化缓冲液含 50% H2 16O 和 50% H2 18O，标记可在消化过程中完成；肽段 C 端产生 2 Da-split doublet；主要缺点是羧基的氧原子不稳定，18O 可与溶液中的 16O 交换，导致标记受损。
- C 端酯化：用 1:1 甲醇/D3-甲醇酯化，产生 3 Da-split doublet；该策略并不容易，不推荐。

## 总结

质谱法在蛋白鉴定上非常有效，但 de novo sequencing 很少能给出完整且无歧义的结构解析。实际应用受几个边界条件限制：低能 CID 适合 5 kDa 以下前体；离子阱实验中可测序肽段长度约15个氨基酸；ESI 多电荷前体提供互补的碎裂信息，应尽量利用；等重氨基酸（I/L 及多种质量组合）无法仅靠低分辨 MS/MS 区分。

手动谱图解析需要结合多种证据：b2/a2 离子对、同键 b/y 互补关系、多电荷离子的 charge state 分析、MS3 验证、以及数据库搜索。当离子系列出现覆盖缺口时，可计算缺失序列的氨基酸组成，或借助衍生化改善碎裂模式。

尚未解决的问题集中在：某些肽键对碰撞特别耐受，导致系统性的序列覆盖缺口；低丰度峰可能来自噪音，注释需谨慎；仅凭 MS/MS 数据无法区分的质量组合需要额外实验或高分辨数据支持。

## 参考资料

- [Microsoft PowerPoint - Section 6 Peptide Sequencing ASMS 2009.ppt（semanticscholar.org）](https://pdfs.semanticscholar.org/presentation/e3ae/f896d4020e669f5f5c65ecf51067185d403d.pdf)
- [Mascot database search: Peptide fragmentation（washington.edu）](https://proteomicsresource.washington.edu/mascot/help/fragmentation_help.html)
- 《mass spectrometry instrumention, interpretation, and applications》第六章
- [De Novo Peptide Sequencing 教程（ionsource.com）](http://www.ionsource.com/tutorial/DeNovo/DeNovoTOC.htm)
- [Protein ID 教程（ionsource.com）](http://www.ionsource.com/tutorial/protID/idtoc.htm)
- [Interpreting Electrospray Mass Spectra（ionsource.com）](http://www.ionsource.com/tutorial/spectut/spec1.htm)
- Mobile and localized protons: a framework for understanding peptide dissociation（DOI: 10.1002/1096-9888(200012)35:12<1399::AID-JMS86>3.0.CO;2-R）
- Wysocki VH, Resing KA, Zhang Q et al (2005) Mass spectrometry of peptides and proteins. Methods (San Diego) 35:211–222
- Shukla AK, Futrell JH (2000) Tandem mass spectrometry: dissociation of ions by collisional activation. J Mass Spectrom 35:1069–1090

[^1]: Novel fragmentation process of peptides by collision-induced decomposition in a tandem mass spectrometer: differentiation of leucine and isoleucine
[^2]: Papayannopoulos IA (1995) The interpretation of collision-induced dissociation tandem mass spectra of peptides. Mass Spectrom Rev 14:49–73
[^3]: Collision-induced fragmentation of (M + H)+ ions of peptides. Side chain specific sequence ions（[DOI: 10.1016/0168-1176(88)80060-0](https://doi.org/10.1016/0168-1176(88)80060-0)）
[^4]: P. Roepstorff and J. Fohlman, Proposal for a Common Nomenclature for Sequence Ions in Mass Spectra of Peptides. Biomed. Mass Spectrom., 11(1984): 601.
[^5]: R. S. Johnson, S. A. Martin, K. Biemann, J. T. Stults, and J. T. Watson, Novel Fragmentation Process of Peptides by Collision-Induced Decomposition in a Tandem Mass Spectrometer: Differentiation of Leucine and Isoleucine. Anal. Chem., 59(1987): 2621–2625