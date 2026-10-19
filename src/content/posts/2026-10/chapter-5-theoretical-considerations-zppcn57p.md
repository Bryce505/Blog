---
draft: true
reviewNotes:
  - "正文过短: 4044/13096=31% < 40%"
  - "1 张图没取到，正文里留着「图片暂缺」占位"
  - "减法模式下篇幅 4,020 字符（原文 16,470，比例 24%）超出 9,058～15,646 字符的区间"
title: "ELISA 的理论基础：抗原表位、抗体亲和力与亲合力，以及免疫应答产生的抗体类型"
date: 2026-10-19
category: "02分子表征"
primaryTag: "02分子表征/相互作用/亲和力Affinity"
description: "ELISA 的定量表现，最终由抗原侧的表位数量与分布、抗体侧的结合强度，以及两者在溶液中的结合平衡共同决定。本文从抗原的尺寸与表位、epitope/epitype/paratope 的界定入手，区分单点结合的 affinity 与整体结合的 avidity，再讨论免疫应答产生的抗"
tags:
  - "02分子表征/相互作用/亲和力Affinity"
sourceNotes:
  - "Analytical technology/ELISA Assay/Chapter-5-Theoretical-Considerations-ZPPCN57P.md"
---

ELISA 的定量表现，最终由抗原侧的表位数量与分布、抗体侧的结合强度，以及两者在溶液中的结合平衡共同决定。本文从抗原的尺寸与表位、epitope/epitype/paratope 的界定入手，区分单点结合的 affinity 与整体结合的 avidity，再讨论免疫应答产生的抗体类型及稀释对表观亲合力的影响，把这几条理论前提落到检测设计上。

## 抗原的大小如何决定可结合位点的数量

分子越大，其复杂性也就越高。

Fab 结合的面积大概是 20nm^2，也就是 epitope 的表面积；通过计算分子的球形表面积，再把表面积除以 20，可以获得 Fab 结合位点的最大数量。

这一估算有明确的前提：**这样的计算是基于整个表面具有抗原性（很少是真实的）和分子最大结合的事实**。因此它给出的是上限而非实测值。

其用途在于反向推算——**calculate how much antibody is needed to saturate any agent, or measure the level of antibody attachment as a function of available surface**，即估算饱和某一试剂所需的抗体量，或测定抗体结合水平随可用表面的变化。

## epitope、epitype 与 paratope：三个容易混淆的术语

- **epitope**：即 antigenic site，抗原上被抗体识别的位点。
- **epitype**：**An epitype is an area on an antigen that is identified by a closely related set of antibodies identifying very similar chemical structures (e.g., mAbs, which define overlapping or interrelated epitopes). An epitype can be regarded as an area identifying slightly different specificities of antibodies reacting with the same antigenic site**——即由一组化学结构非常相似的抗体（例如定义重叠或相互关联表位的 mAb）所识别的抗原区域，可视为识别同一抗原位点、但特异性略有差异的抗体所对应的区域。
- **paratope**：抗体上结合抗原表位的部分。

三个概念分处抗原侧与抗体侧：epitope/epitype 描述抗原被识别的区域，paratope 描述执行识别的一方。

## affinity 与 avidity：单点结合强度与整体结合强度

### affinity（结合亲和力）

- 定义为单个 epitope 与 paratope 之间的能量，即 **the strength of the interaction between the antigen's epitope and the antibody's paratope at a singular binding site**；**The binding energy between an antibody molecule and an antigen determinant is termed affinity.**
- Affinity is mediated by non-covalent interactions that include hydrogen bonds, electrostatic bonds, Van der Waals forces, and hydrophobic interactions and is defined by the equilibrium dissociation constant (K_D)。

### avidity（功能性亲和力）

- **The measure of the total binding strength of an antibody at every binding site is termed avidity. Avidity is also known as the functional affinity**，即与抗原结合的总能量。
- 有两种互补的表述：**The avidity represents an average binding energy from the sum of all the individual affinities of a population of antibodies binding to different antigenic sites**；以及 **Avidity can be regarded as the sum of all the different affinities between the heterogeneous antibodies contained in a serum and the various antigenic sites (epitopes).**
- 三个影响因素：1) the binding affinity，2) valency，3) the structural arrangement of the antibody and antigen in question。

简言之，affinity 是单一结合位点层面的量，avidity 是分子乃至抗体群层面的量，后者同时受价数与空间排布制约。

## 免疫应答产生的抗体类型及其对检测选择的影响

### 多克隆应答与抗体类型的时序

应对抗原刺激产生的是多克隆抗体，且抗体类型并不仅限于 IgG；抗体类型产生的时间顺序见下图。

*[图片暂缺]*<!--missing-image: TMX6RAKJ.png|-->

### 被动免疫与主动免疫

- **passive immunization**：直接给予中和抗体。
- **active immunization**：给予抗原，由机体产生保护性抗体。

疫苗经 sc（皮下）或 im（肌内）注射，这种方式可以诱导产生多种抗体类型（isotype）。因此必须考虑：是使用总抗体检测、isotype-specific assay，还是检测抗原清除，来评估疫苗接种效果。

### 口服与吸入途径

口服/吸入免疫会引出同型选择的问题——**The immunoassayist must decide whether an assay for isotype-specific antibodies, notably IgA, may provide deeper insight into the benefits of vaccination than an assay for total antibody**，即需要判断针对 isotype-specific 抗体（尤其是 IgA）的检测，是否比总抗体检测更能反映疫苗接种带来的收益。

## 稀释为什么会改变血清的表观亲合力

**It is important to realize that the avidity of a serum may change on dilution because an operator may be diluting out certain populations of antibodies.**

这一点的机制在于血清中抗体群的异质性。举例而言，某份血清中可能含有**少量对特定复杂抗原有高亲和力的抗体**，同时含有**大量低亲和力抗体**。在**未大幅稀释**的免疫测定条件下，高、低亲和力抗体竞争抗原位点，**高亲和力抗体优先反应**；而一旦稀释，高亲和力抗体的浓度不断下降，直至体系中只剩低亲和力抗体。

这一点在**用免疫测定、以不同抗血清的差异活性来比较抗原**时尤其需要注意——**The dilution of any serum can affect its ability to discriminate between antigens**，其原因正是异质性抗体群的动态，即各抗体分子的相对浓度与亲和力。

## 结论与适用边界

把上述几条线索归拢：

- 表位数量按「球形表面积 ÷ 20nm²」估算，其成立依赖「整个表面都具有抗原性」与「分子最大结合」两个假设，而后者很少为真，故结果只能看作上限。
- affinity 描述单一 epitope–paratope 位点的结合强度，由非共价作用与 K_D 定义；avidity 描述整体结合强度，受结合亲和力、价数与抗体–抗原结构排布三者共同决定。讨论「结合强弱」时必须先说明是哪一层。
- 免疫应答产生的是多克隆、非单一 isotype 的抗体群，其组成随时间变化；注射途径（sc/im 与口服/吸入）会影响 isotype 谱，因而检测策略（总抗体、isotype-specific、抗原清除）需要在方法设计之初就确定。
- 血清的表观亲合力不是固定属性：稀释会改变抗体群组成，从而改变其对抗原的区分能力。凡涉及不同抗血清间比较的实验，稀释体系必须受控。

尚未解决、也最容易被忽略的一点是：以上讨论都建立在抗体群组成的动态之上，而这一组成在稀释、竞争与时间三个维度上同时变化，单一稀释点的测定结果无法外推到其他浓度条件。