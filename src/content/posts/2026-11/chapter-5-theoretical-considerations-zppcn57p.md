---
draft: true
reviewNotes:
  - "正文过短: 3572/13045=27% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 3,466 字符（原文 16,405，比例 21%）超出 9,023～15,585 字符的区间"
title: "ELISA 的理论基础：抗原性、抗体亲和力与免疫应答"
date: 2026-11-14
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "导读：ELISA 的信号强度最终取决于「抗原表位—抗体—酶」这条链上的一系列物理化学性质。本文依次整理抗原性与表位数量的估算方式、结合界面上的几个基本术语（epitope、epitype、paratope）、affinity 与 avidity 的区分以及稀释对后者的影响，最后说"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/ELISA Guidebook-John R. Crowther/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

导读：ELISA 的信号强度最终取决于「抗原表位—抗体—酶」这条链上的一系列物理化学性质。本文依次整理抗原性与表位数量的估算方式、结合界面上的几个基本术语（epitope、epitype、paratope）、affinity 与 avidity 的区分以及稀释对后者的影响，最后说明免疫途径如何决定抗体类型，并进而决定检测形式的选择。

## 抗原性首先由分子大小决定

分子越大，其复杂性也就越高。

Fab 与抗原结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一算法成立有两个前提：整个表面都具有抗原性（很少是真实的），以及分子达到最大结合。原文的表述是：“Such a calculation is based on the facts that the whole surface is antigenic (rarely true) and that the molecules bind maximally”（Crowther, 2009）。因此该计算给出的是结合位点数的上限，而不是实测的结合化学计量比。

它的实际用途在于两个方向：“calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface”（Crowther, 2009），也就是反推饱和某种试剂所需的抗体量，或者把抗体结合水平作为可用表面积的函数来测定。

## 表位、表位型与互补位：结合界面的三个术语

**epitope**：即 antigenic site。

**Epitype（表位型）**：“An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site”（Crowther, 2009）。也就是说，表位型是抗原上被一组化学结构识别上高度相近的抗体（例如表位重叠或相互关联的 mAb）所界定的区域；同一抗原位点上，特异性略有差异的抗体可以据此区分。

**paratope（互补位）**：抗体上结合抗原表位的部分。

## affinity 与 avidity 不是同一层次的量

**affinity**（binding affinity）指单一结合位点层面的结合能，可以从三个角度定义：

1. 单个 epitope 与 paratope 之间的能量；
2. 抗原表位与抗体互补位在**单一结合位点**上的相互作用强度；
3. 由**非共价相互作用**介导，包括氢键、静电键、范德华力和疏水相互作用，并由平衡解离常数（K<sub>D</sub>）定义。

**avidity** 又称 functional affinity，是与抗原的总体结合能：“The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites”（Crowther, 2009）；“Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes)”（Crowther, 2009）。换言之，它是抗体在每一个结合位点上结合强度的总和度量。

avidity 受三个因素影响：1）the binding affinity，2）valency，3）the structural arrangement of the antibody and antigen in question。

## 血清稀释会改变 avidity，进而改变抗原区分能力

avidity 是群体性质，因此会随稀释而改变：“It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies”（Crowther, 2009）。

一个典型的血清可能同时含有**少量高亲和力抗体**与**大量低亲和力抗体**。在稀释程度不高时，两者竞争抗原位点，高亲和力抗体优先反应；随着稀释进行，高亲和力抗体的浓度不断下降，最后只剩低亲和力抗体。这一点在“compare antigens by their differential activity with different antisera”时尤为关键——“The dilution of any serum can affect its ability to discriminate between antigens”，原因在于异质性抗体群体的动力学，即各抗体分子的相对浓度与亲和力。

## 免疫途径决定抗体类型，也决定检测形式

针对抗原刺激产生的抗体是多克隆的，且抗体类型并不仅限于 IgG；各类抗体产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->\
（Crowther, 2009）

免疫方式分为两类：passive immunization 是直接注射中和抗体；active immunization 是给予抗原，由机体产生保护性抗体。

疫苗注射通常采用 sc（皮下注射）或 im（肌内注射），这种方式可以诱导产生多种抗体类型（isotype）。因此评估疫苗接种效果时，必须考虑检测形式的选择：使用总抗体检测、isotype-specific assay，还是检测抗原清除的检测。

口服/吸入免疫的考量有所不同：“The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody”（Crowther, 2009, p. 140）。

## 这些概念在方法设计中的位置

把上面几条放在一起，可以看到它们各自约束着 ELISA 设计的不同环节：由分子大小与球形表面积推算出的 Fab 结合位点数只是一个上限，实际可用的抗原位点取决于真正具有抗原性的表面比例和结合是否饱和；affinity 描述单一结合位点，avidity 描述抗体群体的总体结合，二者不可互换使用，而 avidity 又会随稀释漂移，所以用不同抗血清比较抗原差异时，稀释度本身就是变量；免疫途径决定了 isotype 的构成，进而决定应当用总抗体检测还是 isotype-specific 检测来回答问题。对于抗原粗提物、多克隆血清这类异质性体系，上述边界条件尤其需要在方法开发阶段就明确下来。