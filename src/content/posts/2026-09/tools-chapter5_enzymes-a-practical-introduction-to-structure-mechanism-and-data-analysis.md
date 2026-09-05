---
title: Chapter5_Enzymes.-A-Practical-Introduction-to-Structure-Mechanism-and-Data-Analysis
date: '2026-09-05'
category: 工具与效率
tags:
- 工具与效率/翻译
description: 'STEADY-STATE KINETICS OF SINGLE-SUBSTRATE ENZYME REACTIONS KEY LEARNING
  POINTS - The development of steady-state theory '
---

## STEADY-STATE KINETICS OF SINGLE-SUBSTRATE ENZYME REACTIONS

## KEY LEARNING POINTS

- The development of steady-state theory was first done for simple enzyme systems that act on a single substrate. Nevertheless, the general features of this kinetic analysis are extendable to more complex systems.

- The term steady state refers to a situation in which the concentration of the binary ES complex is constant over time. This condition is relatively well satisfied when the substrate is present in great excess over enzyme concentration and during the early time points after enzyme and substrate are mixed. The initial velocity is measured during this early stage of the reaction.

- The initial velocity is a saturable function of substrate concentration at a fixed, low concentration of enzyme. The maximum initial velocity is termed \( {V}_{\max } \) , and the concentration of substrate that results in half-maximal velocity \( \left( {1/2{V}_{\max }}\right) \) is termed the \( {K}_{\mathrm{m}} \) .

- Three kinetic constants can be quantified by fitting initial velocity as a function of substrate concentration: \( {k}_{\text{ cat }},{K}_{\mathrm{m}} \) , and \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \cdot  {k}_{\text{ cat }} \) is a measure of the rate of enzyme turnover and relates to the rate-limiting step(s) of chemical reactions that occur after the formation of the ES complex. \( {K}_{\mathrm{m}} \) is related to the thermodynamic dissociation constant for the ES complex under steady-state conditions. The ratio \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) provides a measure of the catalytic efficiency of the enzyme and relates to the difference in free energy between the free reactants and the enzyme-bound transition state of the reaction.

- Various graphic methods can be used to extract values of \( {k}_{\text{ cat }} \) and \( {K}_{\mathrm{m}} \) from steady-state measurements of initial velocity at varying substrate concentrations. The most direct and accurate graphical method is a direct plot, either on a linear-linear or semi-log scale. Historically, other graphical methods have been used to linearize such data.

Enzyme-catalyzed reactions can be studied in a variety of ways to explore different aspects of catalysis. Enzyme-substrate and enzyme-inhibitor complexes can be rapidly frozen and studied by spectroscopic means. Many enzymes have been crystallized and their structures determined by X-ray diffraction methods. More recently, enzyme structures have been determined by multidimensional NMR and cryo-electron microscopy methods (Chapter 3). Steady-state kinetic analysis of enzyme-catalyzed reactions, however, is the most commonly used means of elucidating enzyme mechanism and, especially when coupled with protein engineering, identifying catalytically relevant structural components. In this chapter, we shall explore the use of steady-state enzyme kinetics as a means of defining the catalytic efficiency and substrate affinity of simple enzymes. As we shall see, the term steady state refers to experimental conditions in which the enzyme-substrate complex can build up to an appreciable and constant "steady-state" level. These conditions are easily obtained in the laboratory, and they allow for convenient interpretation of the time courses of enzyme reactions. All the data analysis described in this chapter rests on the ability of the scientist to conveniently measure the initial velocity of the enzyme-catalyzed reaction under a variety of conditions. For our discussion, we shall assume that some convenient method for determining the initial velocity of the reaction exists. In Chapter 7, we shall address specifically how initial velocities are measured and describe a variety of experimental methods for performing such measurements.

### 5.1 THE TIME COURSE OF ENZYMATIC REACTIONS

Upon mixing an enzyme with its substrate in solution and then (by some convenient means) measuring the amount of substrate remaining and/or the amount of product produced over time, one will observe progress curves like those shown in Figure 5.1. Note that the substrate depletion curve is the mirror image of the product appearance curve. At early times, substrate loss and product appearance change rapidly with time, but as time increases, these rates diminish, approaching zero as all the substrate has been converted to product by the enzyme. Such time courses are well modeled by pseudo-first-order kinetics, as discussed in Chapter 2:

\[
\left\lbrack  \mathrm{S}\right\rbrack   = \left\lbrack  {\mathrm{S}}_{0}\right\rbrack  {e}^{-{kt}} \tag{5.1}
\]

where [S] is the substrate concentration remaining at time \( t,\left\lbrack  {\mathrm{\;S}}_{0}\right\rbrack \) is the starting substrate concentration, and \( k \) is the pseudo-first-order rate constant for the reaction. The velocity \( v \) of such a reaction is thus given by:

\[
v = \frac{-d\left\lbrack  \mathrm{\;S}\right\rbrack  }{dt} = \frac{d\left\lbrack  \mathrm{P}\right\rbrack  }{dt} = k\left\lbrack  {\mathrm{\;S}}_{0}\right\rbrack  {e}^{-{kt}} \tag{5.2}
\]

*[图片暂缺]*<!--missing-image: 1_512_1583_602_437_0.jpg|-->

Figure 5.1 Reaction progress curves for the loss of substrate [S] and production of product [P] during an enzyme-catalyzed reaction.

*[图片暂缺]*<!--missing-image: 2_485_241_643_454_0.jpg|-->

Figure 5.2 Reaction progress curve for the production of the product during an enzyme-catalyzed reaction. The inset highlights the early time points at which the initial velocity can be determined from the slope of the linear plot of [P] versus time.

Let us look more carefully at the product appearance profile for an enzyme-catalyzed reaction (Figure 5.2). If we restrict our attention to the very early portion of this plot (shaded area), we see that the increase in product formation (and substrate depletion as well) tracks approximately linear with time. For this limited time period, the initial velocity \( {v}_{0} \) can be approximated as the slope (change in \( y \) over change in \( x \) ) of the linear plot of [S] or [P] as a function of time:

\[
{v}_{0} =  - \frac{\Delta \left\lbrack  \mathrm{S}\right\rbrack  }{\Delta t} = \frac{\Delta \left\lbrack  \mathrm{P}\right\rbrack  }{\Delta t} \tag{5.3}
\]

Experimentally, one finds that the time course of product appearance and substrate depletion is well modeled by a linear function up to the time when about \( {10}\% \) of the initial substrate concentration has been converted to product (Chapter 2). We shall see in Chapter 7 that by varying solution conditions, we can alter the length of time over which an enzyme-catalyzed reaction will display linear kinetics. For the rest of this chapter, we shall assume that the reaction velocity is measured during this early phase of the reaction, which means that from here \( v = {v}_{0} \) , the initial velocity.

### 5.2 EFFECTS OF SUBSTRATE CONCENTRATION ON VELOCITY

From Equation 5.2, one would expect the velocity of a pseudo-first-order reaction to depend linearly on the initial substrate concentration. When early studies were performed on enzyme-catalyzed reactions, however, scientists found instead that the reactions followed the substrate dependence as illustrated in Figure 5.3. Figure 5.3A illustrates the time course of the enzyme-catalyzed reaction observed at different starting concentrations of the substrate; the velocities for each experiment are measured as the slopes of the plots of [P] versus time. Figure 5.3B replots these data as the initial velocity \( v \) as a function of [S], the starting concentration of substrate. Rather than observing the linear relationship expected for first-order kinetics, we find the velocity apparently saturable at high substrate concentrations. This behavior puzzled early enzymologists.

*[图片暂缺]*<!--missing-image: 3_428_241_766_1087_0.jpg|-->

Figure 5.3 (A) Progress curves for a set of enzyme-catalyzed reactions with different starting concentrations of substrate [S]. (B) Plot of the reaction velocities, measured as the slopes of the lines from (A), as a function of [S].

Three distinct regions of this curve can be identified: at low substrate concentrations the velocity appears to display first-order behavior, tracking linearly with substrate concentration; at very high concentrations of substrate, the velocity switches to zero-order behavior, displaying little dependence on substrate concentration; and in the intermediate region, the velocity displays a curvilinear dependence on substrate concentration. How can one rationalize these experimental observations?

A qualitative explanation for the substrate dependence of enzyme-catalyzed reaction velocities was provided by Brown (1902). While the kinetic characteristics of enzyme reactions were being explored, evidence for complex formation between enzymes and their substrates was also accumulating. Brown thus argued that enzyme-catalyzed reactions could best be described by the following reaction scheme:

\[
\mathrm{E} + \mathrm{S}\underset{{k}_{-1}}{\overset{{k}_{1}}{ \rightleftharpoons  }}\mathrm{{ES}}\overset{{k}_{2}}{ \rightarrow  }\mathrm{E} + \mathrm{P} \tag{5.4}
\]

This scheme predicts that the reaction velocity will be proportional to the concentration of the ES complex as: \( v = {k}_{2} \) [ES]. Suppose that we held the total enzyme concentration constant at some low level and varied the concentration of S. At low concentrations of S, the concentration of ES would be directly proportional to [S]; hence, the velocity would depend on [S] in an apparent first-order fashion. At very high concentrations of S, however, practically all the enzymes would be present in the form of the ES complex. Under such conditions, the velocity depends on the rate of the chemical transformations that convert ES to EP, and the subsequent release of the product to re-form the free enzyme. Adding more substrate under these conditions would not effect a change in reaction velocity; hence, the slope of the plot of velocity versus [S] would approach zero (as seen in Figure 5.3B). The complete [S] dependence of the reaction velocity (Figure 5.3B) predicted by the model of Brown resembles the results seen from the Langmuir isotherm Equation (Chapter 4) for equilibrium binding of ligands to receptors. This is not surprising, since in the model of Brown, catalysis is critically dependent on the initial formation of a binary ES complex through equilibrium binding.

### 5.3 THE RAPID EQUILIBRIUM MODEL OF ENZYME KINETICS

Although the model of Brown provided a useful qualitative picture of enzyme reactions, to be fully utilized by experimental scientists, it needed to be put into a rigorous mathematical framework. This was accomplished first by Henri (1903) and subsequently by Michaelis and Menten (1913), Ironically, Michaelis and Menten are more widely recognized for this contribution, although they themselves acknowledged the prior work of Henri. The basic rate equation derived in this section is commonly referred to as the Michaelis-Menten equation. Several writers have recently taken to referring to the equation as the Henri-Michaelis-Menten equation, to correct this neglect of Henri's contributions. The reader should be aware, however, that most of the scientific literature continues to use the traditional terminology.

The Henri-Michaelis-Menten approach assumes that a rapid equilibrium is established between the reactants \( \left( {\mathrm{E} + \mathrm{S}}\right) \) and the ES complex, followed by slower conversion of the ES complex back to free enzyme and product(s); that is, this model assumes that \( {k}_{2} \ll  {k}_{-1} \) in the scheme presented in Section 5.2. In this model, the free enzyme \( {\mathrm{E}}_{\mathrm{f}} \) first combines with the substrate \( \mathrm{S} \) to form the binary \( \mathrm{{ES}} \) complex. Since the substrate is present in large excess over enzyme, we can use the assumption that the free substrate concentration \( {\left\lbrack  \mathrm{S}\right\rbrack  }_{\mathrm{f}} \) is well approximated by the total substrate concentration added to the reaction [S]. Hence, the equilibrium dissociation constant for this complex is given by:

\[
{K}_{\mathrm{s}} = \frac{{\left\lbrack  \mathrm{E}\right\rbrack  }_{\mathrm{f}}\left\lbrack  \mathrm{S}\right\rbrack  }{\left\lbrack  \mathrm{{ES}}\right\rbrack  } \tag{5.5}
\]

Like the treatment of receptor-ligand binding in Chapter 4, here the free enzyme concentration is given by the difference between the total enzyme concentration [E] and the concentration of the binary complex [ES]:

\[
{\left\lbrack  \mathrm{E}\right\rbrack  }_{\mathrm{f}} = \left\lbrack  \mathrm{E}\right\rbrack   - \left\lbrack  \mathrm{{ES}}\right\rbrack \tag{5.6}
\]

and therefore,

\[
{K}_{\mathrm{s}} = \frac{\left( {\left\lbrack  \mathrm{E}\right\rbrack   - \left\lbrack  \mathrm{{ES}}\right\rbrack  }\right) \left\lbrack  \mathrm{S}\right\rbrack  }{\left\lbrack  \mathrm{{ES}}\right\rbrack  } \tag{5.7}
\]

This can be rearranged to give an expression for [ES]:

\[
\left\lbrack  \mathrm{{ES}}\right\rbrack   = \frac{\left\lbrack  \mathrm{E}\right\rbrack  \left\lbrack  \mathrm{S}\right\rbrack  }{{K}_{\mathrm{S}} + \left\lbrack  \mathrm{S}\right\rbrack  } \tag{5.8}
\]

Next, the ES complex is transformed by various chemical steps to yield the product of the reaction and to recover the free enzyme. In the simplest case, a single chemical step, defined by the first-order rate constant \( {k}_{2} \) , results in product formation. More likely, however, there will be a series of rapid chemical events following ES complex formation. For simplicity, the overall rate for these collective chemical steps can be described by a single first-order rate constant \( {k}_{\text{ cat }} \) . Hence:

\[
\mathrm{E} + \mathrm{S} \rightleftharpoons  \mathrm{{ES}}\underset{{K}_{\mathrm{S}}}{ \rightarrow  }\mathrm{{ES}}\overset{{k}_{\text{ cat }}}{ \rightarrow  }\mathrm{E} + \mathrm{P}
\]

and the rate of product formation is thus given by the first-order equation:

\[
v = {k}_{\text{ cat }}\left\lbrack  \mathrm{{ES}}\right\rbrack \tag{5.9}
\]

Combining Equations 5.8 and 5.9, we obtain:

\[
v = \frac{{k}_{\text{ cat }}\left\lbrack  \mathrm{E}\right\rbrack  \left\lbrack  \mathrm{S}\right\rbrack  }{{K}_{S} + \left\lbrack  \mathrm{S}\right\rbrack  } \tag{5.10}
\]

Equation 5.10 is similar to the equation for a Langmuir isotherm, as derived in Chapter 4 (Equation 4.23). This, then, describes the reaction velocity as a hyperbolic function of [S], with a maximum value of \( {k}_{\text{ cat }}\left\lbrack  \mathrm{E}\right\rbrack \) at infinite [S]. We refer to this value as the maximum reaction velocity or \( {V}_{\max } \) .

\[
{V}_{\max } = {k}_{\text{ cat }}\left\lbrack  E\right\rbrack \tag{5.11}
\]

Combining this definition with Equation 5.10, we obtain:

\[
v = \frac{{V}_{\max }\left\lbrack  \mathrm{S}\right\rbrack  }{{K}_{\mathrm{S}} + \left\lbrack  \mathrm{S}\right\rbrack  } = \frac{{V}_{\max }}{1 + \frac{{K}_{\mathrm{s}}}{\left\lbrack  \mathrm{S}\right\rbrack  }} \tag{5.12}
\]

Equation 5.12 is the final equation derived independently by Henri and Michaelis and Menten to describe enzyme kinetic data. Note the striking similarity between this equation and the forms of the Langmuir isotherm equation presented in Chapter 4 (Equations 4.21 and 4.23). Thus, much of enzyme kinetics can be explained in terms of a simple equilibrium model involving rapid equilibrium between free enzyme and substrate to form the binary ES complex, followed by chemical transformation steps to produce and release the product.

### 5.4 THE STEADY-STATE MODEL OF ENZYME KINETICS

The original derivations by Henri and by Michaelis and Menten depended on a rapid equilibrium approach to enzyme reactions. This approach is quite useful in rapid kinetic measurements, such as single-turnover reactions, as described in Chapter 8. Most experimental measurements of enzyme reactions, however, occur when the ES complex is present at a constant, steady-state concentration (as defined below). Briggs and Haldane (1925) recognized that the equilibrium-binding approach of Henri and Michaelis and Menten could be described more generally by a steady-state approach that did not require \( {k}_{2} \ll  {k}_{-1} \) . The following discussion is based on this description by Briggs and Haldane. As we shall see, the final equation that results from this treatment is very similar to Equation 5.12, and despite the differences between the rapid equilibrium and steady-state approaches, the final steady-state equation is commonly referred to as the Henri-Michaelis-Menten equation.

Steady state refers to a time period of the enzymatic reaction during which the rate of formation of the ES complex is exactly matched by its rate of decay to free enzymes and products. This kinetic phase can be attained when the concentration of substrate molecules is in great excess of the free enzyme concentration. To achieve a steady state, certain conditions must be met, and these conditions allow us to make some reasonable assumptions, which greatly simplify the mathematical treatment of kinetics. These assumptions are as follows:

1. During the initial phase of the reaction progress curve (i.e., conditions under which we are measuring the linear initial velocity), there is no appreciable buildup of any intermediates other than the ES complex. Hence, all the enzyme molecules can be accounted for by either the free enzyme or by the enzyme-substrate complex. The total enzyme concentration [E] is, therefore, given by:

\[
\left\lbrack  \mathrm{E}\right\rbrack   = {\left\lbrack  \mathrm{E}\right\rbrack  }_{\mathrm{f}} + \left\lbrack  \mathrm{{ES}}\right\rbrack \tag{5.13}
\]

2. As in the rapid equilibrium treatment, we assume that the enzyme is acting catalytically, so that it is present in a very low concentration relative to the substrate, that is, [S] \( \gg \) [E]. Hence, the formation of the ES complex does not significantly diminish the concentration of free substrate. We can, therefore, make the approximation: \( {\left\lbrack  S\right\rbrack  }_{f} \sim  \left\lbrack  S\right\rbrack \) , where \( {\left\lbrack  S\right\rbrack  }_{f} \) is the free substrate concentration and \( \left\lbrack  S\right\rbrack \) is the total substrate concentration.

3. During the initial phase of the progress curve, very little product is formed relative to the total concentration of substrate. Hence, during this early phase \( \left\lbrack  \mathrm{P}\right\rbrack   \sim  0 \) and therefore depletion of [S] is minimal. At the initiation of the reaction, there will be a rapid burst of formation of the ES complex followed by a kinetic phase in which the rate of formation of the new ES complex is balanced by the rate of its decomposition back to free enzyme and product. In other words, during this phase the concentration of ES is constant. We refer to this kinetic phase as the steady state, which is defined by:

\[
\frac{d\left\lbrack  \mathrm{{ES}}\right\rbrack  }{dt} = 0 \tag{5.14}
\]

Figure 5.4 illustrates the development and duration of the steady state for the enzyme cytochrome \( c \) oxidase interacting with its substrates cytochrome \( c \) and molecular oxygen. As soon as the substrates and enzyme are mixed, we see a rapid pre-steady state buildup of ES complex, followed by a long time window in which the concentration of ES does not change (the steady-state phase), and finally, a post-steady-state phase characterized by significant depletion of the starting substrate concentration.

With these assumptions made, we can now work out an expression for the enzyme velocity under steady-state conditions. As stated previously, for the simplest of reaction schemes, the pseudo-first-order progress curve for an enzymatic reaction can be described by:

\[
v = {k}_{2}\left\lbrack  \mathrm{{ES}}\right\rbrack \tag{5.15}
\]

Now,[ES] is dependent on the rate of formation of the complex (governed by \( {k}_{1} \) ) and the rate of loss of the complex (governed by \( {k}_{-1} \) and \( {k}_{2} \) ). The rate equations for these two processes are thus given by:

\[
\frac{d\left\lbrack  \mathrm{{ES}}\right\rbrack  }{dt} = {k}_{1}{\left\lbrack  \mathrm{E}\right\rbrack  }_{\mathrm{f}}{\left\lbrack  \mathrm{S}\right\rbrack  }_{\mathrm{f}}\text{ and } - \frac{d\left\lbrack  \mathrm{{ES}}\right\rbrack  }{dt} = \left( {{k}_{-1} + {k}_{2}}\right) \left\lbrack  \mathrm{{ES}}\right\rbrack \tag{5.16}
\]

*[图片暂缺]*<!--missing-image: 7_459_1219_710_504_0.jpg|-->

Figure 5.4 Development of the steady state for the reaction of cytochrome \( c \) oxidase with its substrates, cytochrome \( c \) , and molecular oxygen. The absorbance at 444 nm reflects the ligation state of the active site heme cofactor of the enzyme. Prior to substrate addition (time \( < 0 \) ), the heme group is in the \( {\mathrm{{Fe}}}^{3 + } \) oxidation state and is ligated by a histidine group from the enzyme. Upon substrate addition, the active site heme iron is reduced to the \( {\mathrm{{Fe}}}^{2 + } \) state and rapidly reaches a steady-state phase of substrate utilization in which the iron is ligated by some oxygen species. The steady-state phase ends when a significant portion of the molecular oxygen in the solution has been used up. At this point, the heme iron remains reduced (Fe2+) but is no longer bound to a ligand at its sixth coordination site; this heme species has a much larger extinction coefficient at \( {444}\mathrm{\;{nm}} \) ; hence, the rapid increase in absorbance at this wavelength following the steady-state phase. [Data adapted and redrawn from Copeland (1991).]

Under steady-state conditions these two rates must be equal; hence:

\[
{k}_{1}{\left\lbrack  \mathrm{E}\right\rbrack  }_{\mathrm{f}}{\left\lbrack  \mathrm{S}\right\rbrack  }_{\mathrm{f}} = \left( {{k}_{-1} + {k}_{2}}\right) \left\lbrack  \mathrm{{ES}}\right\rbrack \tag{5.17}
\]

This can be rearranged to obtain an expression for [ES]:

\[
\left\lbrack  \mathrm{{ES}}\right\rbrack   = \frac{{\left\lbrack  \mathrm{E}\right\rbrack  }_{\mathrm{f}}{\left\lbrack  \mathrm{S}\right\rbrack  }_{\mathrm{f}}}{\frac{{k}_{-1} + {k}_{2}}{{k}_{1}}} \tag{5.18}
\]

At this point, let us define the term \( {K}_{\mathrm{m}} \) as an abbreviation for the kinetic constants in the denominator of the right-hand side of Equation 5.18:

\[
{K}_{\mathrm{m}} = \frac{{k}_{-1} + {k}_{2}}{{k}_{1}} \tag{5.19}
\]

For now, we will consider \( {K}_{\mathrm{m}} \) to be merely an abbreviation to make our subsequent mathematical expressions less cumbersome. Later, however, we shall see that \( {K}_{\mathrm{m}} \) has a more significant meaning. The reader should note that different authors use a lower case (m) or upper case (M) for the subscript in this term, so that one may see this term in the literature presented as either \( {K}_{\mathrm{m}} \) or \( {K}_{\mathrm{M}} \) . Substituting Equation 5.19 into Equation 5.18, we obtain:

\[
\left\lbrack  \mathrm{{ES}}\right\rbrack   = \frac{{\left\lbrack  \mathrm{E}\right\rbrack  }_{\mathrm{f}}{\left\lbrack  \mathrm{S}\right\rbrack  }_{\mathrm{f}}}{{K}_{\mathrm{m}}} \tag{5.20}
\]

Now, since substrate depletion is insignificant during the steady-state phase, we can replace the term \( {\left\lbrack  \mathrm{S}\right\rbrack  }_{\mathrm{f}} \) by the total substrate concentration \( \left\lbrack  \mathrm{S}\right\rbrack \) (which is much more easily measured in real experimental situations). We can also use the equality of Equation 5.13 to replace \( {\left\lbrack  \mathrm{E}\right\rbrack  }_{\mathrm{f}} \) by ([E]-[ES]). With these substitutions, Equation 5.20 can be recast as follows:

\[
\left\lbrack  \mathrm{{ES}}\right\rbrack   = \left\lbrack  \mathrm{E}\right\rbrack  \frac{\left\lbrack  \mathrm{S}\right\rbrack  }{\left\lbrack  \mathrm{S}\right\rbrack   + {K}_{\mathrm{m}}} \tag{5.21}
\]

If we now combine this expression for [ES] with the velocity expression of Equation 5.15, we obtain:

\[
v = {k}_{2}\left\lbrack  \mathrm{\;E}\right\rbrack  \frac{\left\lbrack  \mathrm{S}\right\rbrack  }{\left\lbrack  \mathrm{S}\right\rbrack   + {K}_{\mathrm{m}}} \tag{5.22}
\]

Or we can generalize Equation 5.22 for more complex reaction schemes by substituting \( {k}_{\text{ cat }} \) for \( {k}_{2} \) :

\[
v = {k}_{\text{ cat }}\left\lbrack  \mathrm{E}\right\rbrack  \frac{\left\lbrack  \mathrm{S}\right\rbrack  }{\left\lbrack  \mathrm{S}\right\rbrack   + {K}_{\mathrm{m}}} \tag{5.23}
\]

As described earlier, as the concentration of substrate goes toward infinity, the velocity reaches a maximum value that we have defined as \( {V}_{\max } \) . Under these conditions, the \( {K}_{\mathrm{m}} \) term is a very small contribution to Equation 5.23. Therefore:

\[
\mathop{\lim }\limits_{{\left\lbrack  \mathrm{S}\right\rbrack   \rightarrow  \infty }}\frac{\left\lbrack  \mathrm{S}\right\rbrack  }{\left\lbrack  \mathrm{S}\right\rbrack   + {K}_{\mathrm{m}}} \cong  \frac{\left\lbrack  \mathrm{S}\right\rbrack  }{\left\lbrack  \mathrm{S}\right\rbrack  } = 1 \tag{5.24}
\]

and thus, we again arrive at Equation 5.11: \( {V}_{\max } = {k}_{\text{ cat }}\left\lbrack  \mathrm{E}\right\rbrack \) . Combining this with Equation 5.24, we finally arrive at an expression very similar to that first described by Henri and Michaelis and Menten (i.e., similar to Equation 5.12):

\[
v = \frac{{V}_{\max }\left\lbrack  \mathrm{S}\right\rbrack  }{{K}_{\mathrm{m}} + \left\lbrack  \mathrm{S}\right\rbrack  } = \frac{{V}_{\max }}{1 + \frac{{K}_{\mathrm{m}}}{\left\lbrack  \mathrm{S}\right\rbrack  }} \tag{5.25}
\]

This is the central expression for steady-state enzyme kinetics. While it differs from the equilibrium expression derived by Henri and by Michaelis and Menten, it is nevertheless universally referred to as the Michaelis-Menten or Henri-Michaelis-Menten equation.

In our definition of \( {K}_{\mathrm{m}} \) (Equation 5.19), we combined first-order rate constants \( \left( {{k}_{-1}\text{ and }{k}_{2}}\right. \) , which have units of reciprocal time) with a second-order rate constant \( \left( {{k}_{1},}\right. \) which has units of reciprocal molarity, reciprocal time) in such a way that the resulting \( {K}_{\mathrm{m}} \) has units of molarity, as does [S]. If we set up our experimental system so that the concentration of substrate exactly matches \( {K}_{\mathrm{m}} \) , Equation 5.25 will reduce to:

\[
v = \frac{{V}_{\max }\left\lbrack  \mathrm{S}\right\rbrack  }{\left\lbrack  \mathrm{S}\right\rbrack   + \left\lbrack  \mathrm{S}\right\rbrack  } = \frac{{v}_{\max }}{2} \tag{5.26}
\]

This provides us with a working definition of \( {K}_{\mathrm{m}} \) : The \( {K}_{\mathrm{m}} \) is the substrate concentration that provides a reaction velocity that is half of the maximal velocity obtained under saturating substrate conditions. The \( {K}_{\mathrm{m}} \) value is often referred to in the literature as the Michaelis constant. In comparing Equation 5.25 for steady-state kinetics with Equation 5.12 for the rapid equilibrium treatment, we see that the equations are identical except for the substitution of \( {K}_{\mathrm{m}} \) for \( {K}_{\mathrm{s}} \) in the steady-state treatment. It is, therefore, easy to confuse these terms and to treat \( {K}_{\mathrm{m}} \) as if it were the thermodynamic dissociation constant for the ES complex. However, the two constants are not always equal, even for the simplest of reaction schemes, as presented here. Recall that \( {K}_{\mathrm{s}} \) can be defined by the ratio of the reverse and forward reaction rate constants:

\[
{K}_{\mathrm{S}} = \frac{{k}_{-1}}{{k}_{1}} \tag{5.27}
\]

This value is not identical to the expression for \( {K}_{\mathrm{m}} \) given in Equation 5.19. Only under the specific conditions that \( {k}_{2} \ll  {k}_{-1} \) are \( {K}_{\mathrm{m}} \) and \( {K}_{\mathrm{s}} \) equivalent. For more complex reaction schemes, one would replace the \( {k}_{2} \) term in Equation 5.19 by \( {k}_{\text{ cat }} \) . Recall that \( {k}_{\text{ cat }} \) reflects a summation of multiple chemical steps in catalysis. Hence, depending on the details of the reaction mechanism and the values of the individual rate constants, situations can arise in which the value of \( {K}_{\mathrm{m}} \) is less than, greater than, or equal to \( {K}_{\mathrm{s}} \) . Therefore, \( {K}_{\mathrm{m}} \) should generally be considered as a kinetic, not thermodynamic, constant.

### 5.5 THE SIGNIFICANCE OF \( {k}_{\text{ cat }} \) AND \( {K}_{\mathrm{m}} \)

We have gone to great lengths in this chapter to define and derive expressions for the kinetic constants \( {k}_{\text{ cat }} \) and \( {K}_{\mathrm{m}} \) . What value do these constants add to our understanding of the enzyme under study? Table 5.1 summarizes the relationship of these steady-state kinetic constants to specific steps along the reaction coordinate of an enzyme-catalyzed reaction. The text to follow describes these steady-state kinetic parameters in more detail.

Table 5.1 Relationship between steady-state kinetic constants and specific steps along the reaction coordinate of enzyme-catalyzed reactions

<table><tr><td>Steady-State Parameter</td><td>Related Reaction Step</td><td></td></tr><tr><td>\( {K}_{\mathrm{m}} \)</td><td>Relates to ES dissociation</td><td>\( \mathrm{{ES}} \rightarrow  \mathrm{E} + \mathrm{S} \)</td></tr><tr><td>\( 1/{K}_{\mathrm{m}} \)</td><td>Relates to ES association</td><td>\( \mathrm{E} + \mathrm{S} \rightarrow  \mathrm{{ES}} \)</td></tr><tr><td>\( {k}_{\mathrm{{cat}}} \)</td><td>Relates to transition from ES to transition state</td><td>\( \mathrm{{ES}} \rightarrow  {\mathrm{{ES}}}^{ \ddagger  } \)</td></tr><tr><td>\( {k}_{\mathrm{{cat}}}/{K}_{\mathrm{m}} \)</td><td>Relates to transition from reactant state to transition state</td><td>\( \mathrm{E} + \mathrm{S} \rightarrow  {\mathrm{{ES}}}^{ \ddagger  } \)</td></tr></table>

Source: Taken from Copeland (2013).

#### 5.5.1 \( {K}_{\mathrm{m}} \)

The value of \( {K}_{\mathrm{m}} \) varies considerably from one enzyme to another, and for a particular enzyme with different substrates. We have already defined \( {K}_{\mathrm{m}} \) as the substrate concentration that results in half-maximal velocity for the enzymatic reaction. An equivalent way of stating this is that the \( {K}_{\mathrm{m}} \) represents the substrate concentration at which half of the enzyme active sites in the sample are filled (i.e., saturated) by substrate molecules in the steady state. Hence, while \( {K}_{\mathrm{m}} \) is not equivalent to \( {K}_{\mathrm{s}} \) under most conditions, it can nevertheless be used as a relative measure of substrate binding affinity. In some instances, changes in solution conditions (pH, temperature, etc.) can have selective effects on the value of \( {K}_{\mathrm{m}} \) . Also, one sometimes observes effects on the value of \( {K}_{\mathrm{m}} \) in the course of comparing different mutants or isoforms of an enzyme, or different substrates with a common enzyme. In these cases, one can reasonably relate the changes to effects on the stability (i.e., affinity) of the ES complex. As we shall see below, however, the ratio \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) is generally a better measure of effects on substrate binding.

#### 5.5.2 \( {k}_{\text{ cat }} \)

Considering Equations (5.23-5.25), we see that if one knows the concentration of enzyme used experimentally, the value of \( {k}_{\text{ cat }} \) can be directly calculated by dividing the experimentally determined value of \( {V}_{\max } \) by [E]. The value of \( {k}_{\text{ cat }} \) is sometimes referred to as the turnover number for the enzyme since it defines the number of catalytic turnover events that occur per unit time. The units of \( {k}_{\text{ cat }} \) are reciprocal time (e.g., \( {\min }^{-1},{\mathrm{\;s}}^{-1} \) ). Turnover numbers, however, are typically reported in units of molecules of product produced per unit time per molecules of enzyme present. As long as the same units are used to express the amount of product produced and the amount of enzyme present, these units will cancel and, as expected, the final units will be reciprocal time. It is important, however, that the units of product and enzyme concentration be expressed in molar or molarity units. In crude enzyme samples, such as cell lysates and other nonhomogeneous protein samples, it is often impossible to know the concentration of enzyme in anything other than units of total protein mass. The literature is thus filled with enzyme activity values expressed as the number of micrograms of product produced per minute per microgram of protein in the enzyme sample. While such units may be useful in comparing one batch of the crude enzyme to another (see the discussion of specific activity measurements in Chapter 7), it is difficult to relate these values to kinetic constants, such as \( {k}_{\text{ cat }} \) .

In the laboratory, we can easily determine the turnover number as \( {k}_{\text{ cat }} \) , by measuring the reaction velocity under conditions of \( \left\lbrack  \mathrm{S}\right\rbrack   \gg  {K}_{\mathrm{m}} \) so that \( v \) approaches \( {V}_{\max } \) . The rate of enzyme turnover under most physiological conditions in vivo, however, is very different from our laboratory situation. In vivo, the concentration of substrate is often more typically \( {0.1} - {1.0}{K}_{\mathrm{m}} \) . When \( \left\lbrack  \mathrm{S}\right\rbrack   \ll  {K}_{\mathrm{m}} \) , we must change our expression for velocity to:

\[
v = \frac{{k}_{\text{ cat }}}{{K}_{\mathrm{m}}}\left\lbrack  \mathrm{E}\right\rbrack  {\left\lbrack  \mathrm{S}\right\rbrack  }_{\mathrm{f}} \tag{5.28}
\]

Since \( \left\lbrack  \mathrm{S}\right\rbrack   \ll  {K}_{\mathrm{m}} \) here, the free enzyme concentration is well approximated by the total enzyme concentration [E]; thus, we used this term in Equation 5.28 in place of \( {\left\lbrack  \mathrm{E}\right\rbrack  }_{\mathrm{f}} \) . Recalling our definition of \( {K}_{\mathrm{m}} \) , we note that:

\[
\frac{{k}_{\text{ cat }}}{{K}_{\mathrm{m}}} = \frac{{k}_{\text{ cat }}{k}_{1}}{{k}_{-1} + {k}_{\text{ cat }}} \tag{5.29}
\]

Thus, under our laboratory conditions, where \( \left\lbrack  \mathrm{S}\right\rbrack   \gg  {K}_{\mathrm{m}} \) , formation of the ES complex is rapid and often is not the rate-limiting step. In vivo, however, where \( \left\lbrack  \mathrm{S}\right\rbrack   \ll  {K}_{\mathrm{m}} \) , the overall reaction may be limited by the diffusional rate of encounter of the free enzyme with the substrate, which is defined by \( {k}_{1} \) . The rate constant for diffusional encounters between molecules like enzymes and substrates is typically in the range of \( {10}^{8} - {10}^{9}{\mathrm{M}}^{-1}{\mathrm{\;s}}^{-1} \) . Thus, we must keep in mind that the rate-limiting step in catalysis is not always the same in vivo as in vitro. Nevertheless, measurement of \( {k}_{\text{ cat }} \) (i.e., velocity under saturating substrate concentration) gives us the most consistent means of comparing rates for different enzymatic reactions.

The significance of \( {k}_{\text{ cat }} \) is that it defines for us the maximal velocity at which an enzymatic reaction can proceed at a fixed concentration of enzyme and infinite availability of substrate. Because \( {k}_{\text{ cat }} \) relates to the chemical steps after the formation of the ES complex, changes in \( {k}_{\text{ cat }} \) , brought about by changes in the enzyme (e.g., mutagenesis of specific amino acid residues, or comparison of different enzymes), in solution conditions (e.g., pH, ionic strength, and temperature), or in substrate identity (e.g., structural analogs or isotopically labeled substrates), define perturbations that affect the chemical steps in enzymatic catalysis. In other words, changes in \( {k}_{\text{ cat }} \) reflect perturbations of the chemical steps after initial substrate binding. Since \( {k}_{\text{ cat }} \) reflects multiple chemical steps, it does not provide detailed information on the rates of any of the individual steps after substrate binding. Instead, \( {k}_{\text{ cat }} \) provides a lower limit on the first-order rate constant of the slowest (i.e., rate-determining) step(s) following substrate binding that leads eventually to product release (most often formation of the bound transition state; Table 5.1).

## \( {5.5.3}{k}_{\text{ cat }}/{K}_{\mathrm{m}} \)

The catalytic efficiency of an enzyme is best defined by the ratio of the kinetic constants, \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) . This ratio has units of a second-order rate constant and is generally used to compare the efficiencies of different enzymes to one another.

The values of \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) are also used to compare the utilization of different substrates for a particular enzyme. As we shall see in Chapter 6, in comparisons of different substrates for an enzyme, the largest differences often are seen in the values of \( {k}_{\text{ cat }} \) , rather than in \( {K}_{\mathrm{m}} \) . This is because substrate specificity often results from differences in the transition state, rather than ground-state binding interactions (see Chapter 6 for more details). Hence, the ratio \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) captures the effects of differing substrates on either kinetic constant and provides a lower limit for the second-order rate constant of productive substrate binding (i.e., substrate binding leading to ES \( {}^{ \ddagger  } \) complex formation and eventual product formation); this ratio is, therefore, considered to be the best measure of substrate specificity.

The ratio \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) is also used to compare the efficiency with which an enzyme catalyzes a particular reaction in the forward and reverse directions. Enzymatic reactions are in principle reversible, although for many enzymes, the reverse reaction is thermodynamically unfavorable. The presence of an enzyme in the solution does not alter the equilibrium constant \( {K}_{\mathrm{{eq}}} \) between the free substrate and free product concentrations. Hence, the value of \( {K}_{\text{ eq }} \) is fixed for specific solution conditions, and this constrains the values of \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) that can be achieved in the forward (f) and reverse (r) directions. At equilibrium, the forward and reverse reactions occur with equal frequency so that:

\[
{\left( \frac{{k}_{\mathrm{{cat}}}}{{K}_{\mathrm{m}}}\right) }_{f}\left\lbrack  \mathrm{E}\right\rbrack  \left\lbrack  \mathrm{S}\right\rbrack   = {\left( \frac{{k}_{\mathrm{{cat}}}}{{K}_{\mathrm{m}}}\right) }_{r}\left\lbrack  \mathrm{E}\right\rbrack  \left\lbrack  \mathrm{P}\right\rbrack \tag{5.30}
\]

hence,

\[
{K}_{\mathrm{{eq}}} = \frac{{\left( {k}_{\mathrm{{cat}}}/{K}_{\mathrm{m}}\right) }_{\mathrm{f}}}{{\left( {k}_{\mathrm{{cat}}}/{K}_{\mathrm{m}}\right) }_{\mathrm{r}}} \tag{5.31}
\]

Equation 5.31, known as the Haldane relationship, provides a useful measure of the directionality of an enzymatic reaction under a specific set of solution conditions.

In either direction, the ratio \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) can be related to the free energy difference between the free reactants (E and S, in the forward direction) and the transition state complex \( \left( {\mathrm{{ES}}}^{ \ddagger  }\right) \) . If we normalize the free energy of the reactant state to zero, the free energy difference is defined by:

\[
\Delta {G}_{{\mathrm{{ES}}}^{ \ddagger  }} =  - {RT}\ln \left( \frac{{k}_{\mathrm{{cat}}}}{{K}_{\mathrm{m}}}\right)  + {RT}\ln \left( \frac{{k}_{\mathrm{B}}T}{h}\right) \tag{5.32}
\]

where \( {k}_{\mathrm{B}} \) is the Boltzmann constant, \( T \) is the temperature in degrees Kelvin, and \( h \) is Planck’s constant, so that at a fixed temperature the term \( {RT}\ln \left( {{k}_{\mathrm{B}}T/h}\right) \) is a constant. This relationship holds because generally attainment of the transition state is the most energetically costly component of the multiple steps contributing to \( {k}_{\text{ cat }} \) . If we compare different substrates for a single enzyme or different enzymes or mutants with a common substrate, we can calculate the difference in transition-state energies \( \left( {{\Delta \Delta }{G}_{{\mathrm{{ES}}}^{ \ddagger  }}}\right) \) from experimentally measured values of \( {k}_{\mathrm{{cat}}}/{K}_{\mathrm{m}} \) at constant temperature:

\[
{\Delta \Delta }{G}_{{\mathrm{{ES}}}^{ \ddagger  }} =  - {RT}\ln \left\lbrack  \frac{{\left( {k}_{\mathrm{{cat}}}/{K}_{\mathrm{m}}\right) }^{1}}{{\left( {k}_{\mathrm{{cat}}}/{K}_{\mathrm{m}}\right) }^{2}}\right\rbrack \tag{5.33}
\]

where superscripts 1 and 2 refer to the different substrates or enzymes being compared. By this type of analysis, one can quantitate the thermodynamic contributions of particular structural components to catalysis. For example, suppose one suspected that an active site tyrosine residue was forming a critical hydrogen bond with the substrate in the transition state of the enzymatic reaction. Through the tools of molecular biology, one could replace this tyrosine with phenylalanine (which would be incapable of forming an \( \mathrm{H} \) bond) by site-directed mutagenesis and measure the value of \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) for both the wild-type and the Tyr \( \rightarrow \) Phe mutant. Suppose these values turned out to be \( {88}{\mathrm{M}}^{-1}{\mathrm{\;s}}^{-1} \) for the wild-type enzyme and \( {0.1}{\mathrm{M}}^{-1}{\mathrm{\;s}}^{-1} \) for the mutant. The ratio of these \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) would be 880 and, from Equation 5.31, this would correspond to a difference in transition-state free energy of 4 kcal/mol, consistent with a strong H-bonding interaction of the tyrosine (of course this does not prove that the exact role of the tyrosine OH group is H-bonding, but the data do prove that this OH group plays a critical role in catalysis). A good example of the use of this approach can be found in the paper by Wilkinson et al. (1983).

#### 5.5.4 Diffusion-Controlled Reactions and Kinetic Perfection

For an enzyme in solution, the rate-determining step in catalysis will be either \( {k}_{1} \) , the rate of ES formation, or one of the multiple steps contributing to \( {k}_{\text{ cat }} \) . If \( {k}_{\text{ cat }} \) is rate limiting, the catalytic events that occur after substrate binding are slower than the rate of formation of the ES complex. If, however, \( {k}_{1} \) is rate limiting, the enzyme turns over essentially instantaneously once the ES complex has formed. In either case, we see that the fastest rate of catalysis for an enzyme in a solution is limited by the rate of diffusion of molecules in the solution. Some enzymes, such as carbonic anhydrase, display \( {k}_{\mathrm{{cat}}}/{K}_{\mathrm{m}} \) values of \( {10}^{8} - {10}^{9}{\mathrm{M}}^{-1}{\mathrm{\;s}}^{-1} \) , which is at the diffusion limit. Such enzymes are said to have achieved kinetic perfection because they convert substrate to the product as fast as the substrate is delivered to the active site of the enzyme!

The diffusion limit would seem to set an upper limit on the value of \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) that an enzyme can achieve. This is true for most enzymes in solution. However, some enzyme systems have overcome this limit by compartmentalizing themselves and their substrates within close proximity in subcellular locals where three-dimensional diffusion no longer comes into play. This can be accomplished by assembling enzymes and substrates into organized systems, such as multienzyme complexes or cellular membranes. Two examples are presented.

We first consider the respiratory electron transfer system of the inner mitochondrial membrane. Here enzymes in a cascade are localized near one another within the membrane bilayer. The product of one enzyme is the substrate for the next in the cascade. Because of the proximity of the enzymes in the membrane, the product leaves the active site of one enzyme and is presented to the active site of the next enzyme without the need for diffusion through the solution.

The second example comes from the de novo synthetic pathway for pyrimidines. The first three steps in the synthesis of uridine monophosphate are performed by a supercomplex of three enzymes that are noncovalently associated within a multiprotein complex. This supercomplex, referred to as CAD, comprises the enzymes carbamoyl phosphate synthase, aspartate transcarbamoylase, and dihydroorotase. Because the active sites of the three enzymes are compartmentalized inside the supercomplex, the product of the first enzyme is immediately in proximity to the active site of the second enzyme, and so on. In this way, the supercomplex can overcome the diffusion barrier to rapid catalysis.

### 5.6 EXPERIMENTAL MEASUREMENT OF \( {k}_{\text{ cat }} \) AND \( {K}_{\mathrm{m}} \)

#### 5.6.1 Graphical Determinations from Untransformed Data

The kinetic constants \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) are determined graphically with initial velocity measurements obtained at varying substrate concentrations. The graphical methods are best illustrated by working through examples with some numerical data. The quality of the estimates of \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) depends on covering a substrate concentration range that spans a significant portion of the binding isotherm. Experimentally, a convenient method for choosing substrate concentrations is to first make a stock solution of the substrate at the highest concentration that is experimentally reasonable (based, for example, on the solubility limit of the substrate). Then, 2-fold or 3-fold serial dilutions (see Chapter 4) can be made from this stock to produce a range of lower substrate concentrations. For example, let us say that the highest concentration of the substrate to be used in an enzymatic reaction is \( {250\mu }\mathrm{M} \) . We could make a \( {2.5}\mathrm{{mM}} \) stock solution of the substrate that would be diluted 10-fold into the final assay reaction mixture (i.e., to give a final concentration of \( {250\mu }\mathrm{M} \) ). We could then take a portion of this stock solution and dilute it with an equal volume of buffer to yield a \( {1.25}\mathrm{{mM}} \) solution, which upon dilution into the assay reaction mixture would give a final substrate concentration of \( {125\mu }\mathrm{M} \) . A portion of this solution could also be diluted in half with buffer or solvent, and so on, to yield a series of solutions of diminishing substrate concentrations. The final substrate concentrations presented in Table 5.2 illustrate the use of such a 2-fold serial dilution scheme. Let us suppose that we are studying a simple enzymatic reaction for which the true values of \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) are \( {100\mu }\mathrm{M}/\mathrm{s} \) and \( {12\mu }\mathrm{M} \) , respectively. In Table 5.2, we have listed experimental values for the initial velocity \( v \) at each of the substrate concentrations used. In generating this table, some random error has been added to each of the velocity values to better simulate real experimental conditions. The largest percent errors in this table occur at the lowest substrate concentrations, where in real experiments one encounters the greatest difficulty in obtaining accurate velocity measurements.

Table 5.2 Initial velocity (with random error added) as a function of substrate concentration for a model enzymatic reaction

<table><tr><td>[S] \( {\left( \mu \mathrm{M}\right) }^{a} \)</td><td>\( v\left( {\mu \mathrm{M}}\right. \) product formed \( {\mathrm{s}}^{-1} \) )</td><td>\( 1/v\left( {\mu {\mathrm{M}}^{-1}\mathrm{\;s}}\right) \)</td><td>\( 1/\left\lbrack  \mathrm{S}\right\rbrack  \left( {\mu {\mathrm{M}}^{-1}}\right) \)</td></tr><tr><td>0.98</td><td>10</td><td>0.100</td><td>1.024</td></tr><tr><td>1.95</td><td>12</td><td>0.083</td><td>0.512</td></tr><tr><td>3.91</td><td>28</td><td>0.036</td><td>0.256</td></tr><tr><td>7.81</td><td>40</td><td>0.025</td><td>0.128</td></tr><tr><td>15.63</td><td>55</td><td>0.018</td><td>0.064</td></tr><tr><td>31.25</td><td>75</td><td>0.013</td><td>0.032</td></tr><tr><td>62.50</td><td>85</td><td>0.012</td><td>0.016</td></tr><tr><td>125.00</td><td>90</td><td>0,011</td><td>0.008</td></tr><tr><td>250.00</td><td>97</td><td>0.010</td><td>0.004</td></tr></table>

\( {}^{a} \) Substrate concentrations reflect a 2-fold serial dilution starting with an initial solution that provides \( {250\mu }\mathrm{M} \) substrate to the final assay reaction mixture.

The first and most straightforward way of graphing the data is as a direct plot of velocity as a function of [S]; we shall refer to such a plot as a Michaelis-Menten plot. Figure 5.5 is a Michaelis-Menten plot for the data in Table 5.2, plotted on a linear-linear scale (A) and as a semi-log plot (B); in both cases, the line drawn through the data was generated by a nonlinear least-squares fit of the data to Equation 5.25. With modern computer graphics programs, the reader has a wide choice of options for performing such curve fitting. For the data in Figure 5.5, both \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) were unknowns that were simultaneously solved for by the curve-fitting routine. The estimates of \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) determined in this way were \( {100.36\mu }\mathrm{M}/\mathrm{s} \) and \( {11.63}/\mu \mathrm{M} \) , respectively, in excellent agreement with the true values of these constants. Such direct fits of the untransformed data provide the most reliable estimates of both kinetic constants.

With the widespread availability of computer curve-fitting programs, what limitations are there on our ability to estimate \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) from experimental data? As mentioned above, the accuracy of such estimates will depend on the range of substrate concentrations over which the initial velocity has been determined. If measurements are made only at low substrate concentrations, the data will appear to be first ordered (i.e., \( v \) will appear to be a linear function of [S]). This is illustrated in Figure 5.6A for the data in Table 5.1 between substrate concentrations of 0.98and \( {3.91\mu }\mathrm{M} \) (i.e., \( \left. { \leq  {0.33}{K}_{\mathrm{m}}}\right) \) . In this concentration range, the enzyme active sites never reach saturation, and graphically, both \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) appear to be infinite (but see Section 5.8). On the other hand, Figure 5.6B illustrates what happens when measurements are made at very high substrate concentrations only; here the data for substrate concentrations above \( {60\mu }\mathrm{M} \) are considered (i.e., \( \left\lbrack  \mathrm{S}\right\rbrack   \geq  5{K}_{\mathrm{m}} \) ). In this saturating substrate concentration range, the velocity appears to be almost independent of substrate concentration. While a rough estimate of \( {V}_{\max } \) might be obtained from these data (although the reader should note that the true \( {V}_{\max } \) is only reached at infinite substrate concentration; hence any experimentally measured velocity at high [S] may approach, but never fully reach \( {V}_{\max } \) ), there is no way to determine the \( {K}_{\mathrm{m}} \) value here.

The plots in Figure 5.6 emphasize the need for exploring a broad range of substrate concentrations to accurately determine the kinetic constants for the enzyme of interest. Again, there may be practical limits on the range of substrate concentrations over which such measurements can be performed. In Chapter 4 we suggested that to best characterize a ligand binding isotherm, it is necessary to cover a ligand concentration range that resulted in 20-80% receptor saturation. Likewise, in determining the steady-state kinetic constants for an enzymatic system, it is best to at least cover substrate concentrations that yield velocities of \( {20} - {80}\% \) of \( {V}_{\max } \) ; this corresponds to [S] of \( {0.25} - {5.0}{K}_{\mathrm{m}} \) .

*[图片暂缺]*<!--missing-image: 15_243_1585_1140_347_0.jpg|-->

Figure 5.5 (A) Michaelis-Menten plot for the velocity data in Table 5.2. The solid line through the data points represents the nonlinear least-squares best fit to Equation 5.25. (B) As in (A) but with the \( x \) axis (substrate concentration) plotted on a \( {\log }_{10} \) scale, as described in Chapter 4 (see Figure 4.8), illustrating the clearer visualization of \( {K}_{\mathrm{m}} \) and \( {V}_{\max } \) obtained with this plotting format.

*[图片暂缺]*<!--missing-image: 16_453_243_706_1046_0.jpg|-->

Figure 5.6 Michaelis-Menten plots for restricted data from Table 5.2. (A) The range of [S] values are inappropriately low \( \left( { \leq  {0.33}{\mathrm{\;K}}_{\mathrm{m}}}\right) \) , hence \( {K}_{\mathrm{m}} \) and \( {V}_{\max } \) appear to be infinite. (B) The range of [S] values are inappropriately high, with the result that every data point represents near-saturating conditions; one may be able to approximate \( {V}_{\max } \) , but \( {K}_{\mathrm{m}} \) cannot be determined.

Since the kinetic constants are unknowns prior to these experiments, it is common to perform initial experiments with a limited number of data points that span as broad a range of substrate concentrations as possible (at least a 100-fold substrate concentration range) to obtain a rough estimate of \( {K}_{\mathrm{m}} \) and \( {V}_{\max } \) . Improved estimates can then be obtained by narrowing the substrate concentration range between 0.25 and \( {5.0}{K}_{\mathrm{m}} \) and obtaining a larger number of data points within this range. Table 5.2 illustrates an ideal situation for determining \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) . The data span a 250-fold range of substrate concentrations that cover the range from 0.08 to \( {20.8}{K}_{\mathrm{m}} \) . Hence, use of such a twofold serial dilution setup, starting with the highest substrate concentration that is feasible, is highly recommended.

Alternatively, one could perform a limited number of experiments by using a fivefold serial dilution setup starting at our maximum substrate concentration of \( {250\mu }\mathrm{M} \) . With only five experiments, we would then cover the substrate concentrations250,50,10,2, and \( {0.4\mu }\mathrm{M} \) . Data from such a hypothetical experiment are shown in Figure 5.7A and would yield an estimate of \( {K}_{\mathrm{m}} \) of about \( {10\mu }\mathrm{M} \) . With this initial estimate in hand, one might then choose to expand the number of data points within the narrower range of \( {0.25} - {5.0}{K}_{\mathrm{m}} \) to obtain better estimates of the kinetic constants. Figure 5.7B, for example, illustrates the type of data one might obtain from velocity measurements at substrate concentrations of2.5,5,10,15,20,25,30,35,40,45, and \( {50\mu }\mathrm{M} \) . From this second set of measurements, values of \( {102\mu }\mathrm{M}/\mathrm{s} \) and \( {12\mu }\mathrm{M} \) for \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) , respectively, would be obtained.

#### 5.6.2 Lineweaver-Burk Plots of Enzyme Kinetics

The widespread availability of user-friendly nonlinear curve-fitting programs is a relatively recent development; in the past, determination of the kinetic constants for an enzyme from untransformed data was not so routine. To facilitate work in this area, scientists searched for means of transforming the data to produce linear plots from which the kinetic constants could be determined simply with graph paper and a straightedge. While today most of us have nonlinear curve-fitting programs at our disposal (and this is the preferred means of determining the values of \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) ), there is still some value in linearized plots of enzyme kinetic data. As we shall see in subsequent chapters, these plots are useful in diagnosing the mechanistic details of multisubstrate enzymes and for determining the mode of interaction between an enzyme and an inhibitor. Table 5.3 summarizes some of the more commonly used plotting methods for the linearization of steady-state kinetic data; these various methods are presented below.

*[图片暂缺]*<!--missing-image: 17_456_929_716_1050_0.jpg|-->

Figure 5.7 Experimental strategy for estimating \( {K}_{\mathrm{m}} \) and \( {V}_{\max } \) . (A) A limited data set is collected over a broad range of [S] to get a rough estimate of the kinetic constants. (B) Once a rough estimate of \( {K}_{\mathrm{m}} \) has been determined, a second set of experiments is performed with more data within the range of \( {0.25} - {5.0}{K}_{\mathrm{m}} \) to obtain more precise estimates of the kinetic constants.

The most used method for linearizing enzyme kinetic data is that of Lineweaver and Burk (1934). We start with the same steady-state assumption described earlier. Applying some simple algebra, we can rewrite Equation 5.25 in the following form:

\[
v = {V}_{\max }\left( \frac{1}{1 + \frac{{K}_{\mathrm{m}}}{\left\lbrack  \mathrm{S}\right\rbrack  }}\right) \tag{5.34}
\]

Now we simply take the reciprocal of this equation and rearrange it to obtain:

\[
\frac{1}{v} = \left( {\frac{{K}_{\mathrm{m}}}{{V}_{\max }}\frac{1}{\left\lbrack  \mathrm{\;S}\right\rbrack  }}\right)  + \frac{1}{{V}_{\max }} \tag{5.35}
\]

Comparing Equation 5.35 with the standard equation for a straight line, we have

\[
y = {mx} + b \tag{5.36}
\]

where \( m \) is the slope and \( b \) is the \( y \) intercept. We see that Equation 5.35 is an equation for a straight line with a slope of \( {K}_{\mathrm{m}}/{V}_{\max } \) and \( y \) intercept of \( 1/{V}_{\max } \) .

Thus, if the reciprocal of initial velocity is plotted as a function of the reciprocal of [S], we would expect from Equation 5.35 to obtain a linear plot. For the same reasons described earlier for untransformed data, these plots work best when the substrate concentration covers the range of \( {0.25} - {5.0}{K}_{\mathrm{m}} \) . Within this range, good linearity is observed, as illustrated in Figure 5.8 for the data between \( \left\lbrack  \mathrm{S}\right\rbrack   = {3.91} \) and \( \left\lbrack  \mathrm{S}\right\rbrack   = {62.50\mu }\mathrm{M} \) in Table 5.2. A plot like that in Figure 5.8 is known as a Lineweaver-Burk plot.

The kinetic constants \( {K}_{\mathrm{m}} \) and \( {V}_{\max } \) can be determined from the slope and intercept values of the linear fit of the data in a Lineweaver-Burk plot. Since the \( x \) axis is reciprocal substrate concentration, the value of \( x = 0 \) (i.e., \( 1/\left\lbrack  \mathrm{S}\right\rbrack   = 0 \) ) corresponds to \( \left\lbrack  \mathrm{S}\right\rbrack   = \) infinity. Hence, the extrapolated value of the \( y \) intercept corresponds to the reciprocal of \( {V}_{\max } \) . The value of \( {K}_{\mathrm{m}} \) can be determined from a Lineweaver-Burk plot in two ways. First, we note from Equation 5.35 that the slope is equal to \( {K}_{\mathrm{m}} \) divided by \( {V}_{\max } \) . if we, therefore, divide the slope of our best fit line by the y intercept value (i.e., by \( 1/{V}_{\max } \) ), the product will be equal to \( {K}_{\mathrm{m}} \) . Alternatively, we could extrapolate our linear fit to the point of intersecting the \( x \) axis. This \( x \) intercept is equal to \( - 1/{K}_{\mathrm{m}} \) ; thus, we could determine \( {K}_{\mathrm{m}} \) from the absolute value of the reciprocal of the \( x \) intercept of our plot.

Table 5.3 Some popular linear plotting methods for steady-state enzyme kinetic data

<table><tr><td>Name</td><td>\( X \) -Axis Term</td><td>Y-Axis Term</td><td>\( {K}_{\mathrm{m}} \) Determination</td><td>\( {V}_{\max } \) Determination</td></tr><tr><td>Lineweaver-Burk</td><td>1/[S]</td><td>1/v</td><td>slope \( \times  {\mathrm{V}}_{\max } \) or \( \left( {-1}\right) /x \) intercept</td><td>1/y intercept</td></tr><tr><td>Eadie-Hofstee</td><td>v/[S]</td><td>\( \mathcal{V} \)</td><td>(-1) × slope</td><td>\( Y \) intercept</td></tr><tr><td>Hanes-Wolf</td><td>[S]</td><td>[S]/v</td><td>\( Y \) intercept/slope</td><td>1/slope</td></tr><tr><td>Eisenthal-Cornish-</td><td>-[S]</td><td>\( \mathcal{V} \)</td><td>\( X \) axis value at the <br> point of line</td><td>\( Y \) axis value at the <br> point of line</td></tr><tr><td>Bowden</td><td></td><td></td><td>intersection</td><td>intersection</td></tr></table>

*[图片暂缺]*<!--missing-image: 19_473_245_680_487_0.jpg|-->

Figure 5.8 Lineweaver-Burk double-reciprocal plot for selected data from Table 5.2 within the range of \( \left\lbrack  \mathrm{S}\right\rbrack   = {0.25} - {5.0}{K}_{\mathrm{m}} \) .

We have noted several times that the preferred way to determine \( {K}_{\mathrm{m}} \) and \( {V}_{\max } \) values is from the nonlinear fitting of untransformed data to the Michaelis-Menten equation. Figure 5.8 illustrates why we have stressed this point. In real experimental data, small errors in the measured values of \( v \) are amplified by the mathematical transformation of taking the reciprocal. The greatest percent error is likely to be associated with velocity values at low substrate concentration. Unfortunately, in the reciprocal plot, the lowest values of [S] correspond to the highest values of \( 1/\left\lbrack  \mathrm{S}\right\rbrack \) , and because of the details of linear regression, these data points are weighted more heavily in the analysis. Hence, the experimental error is amplified and unevenly weighted in this analysis, resulting in poor estimates of the kinetic constants even when the experimental error is relatively small. To illustrate this, let us compare the estimates of \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) obtained for the data in Table 5.2 by various graphical methods; this is summarized in Table 5.4. The true values of \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) for the hypothetical data in Table 5.2 were \( {100\mu }\mathrm{M}/\mathrm{s} \) and \( {12\mu }\mathrm{M} \) , respectively. The fitting of the untransformed data to the Michaelis-Menten equation provided estimates of 100.36 and 11.63 for the two kinetic constants, with deviations from the true values of only 0.36 and \( {3.08}\% \) , respectively. The linear fitting of the data in Figure 5.8, on the other hand, yields estimates of \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) of 91.84 and 9.17, with deviations from the true values of 8.16 and \( {23.58}\% \) , respectively. The errors are even greater when the double-reciprocal plots are used for the full data set in Table 5.2, as illustrated in Figure 5.9 and Table 5.2. Here the inclusion of the low substrate data values ( \( < \left\lbrack  \mathrm{S}\right\rbrack   = {3.91}/\mu \mathrm{M} \) ) is very heavily weighted in the linear regression and further limits the precision of the kinetic constant estimates. The values of \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) derived from this fitting are 79.28 and 7.57, representing deviations from the true values of 20.72% and 36.92%, respectively.

Table 5.4 Estimates of the kinetic constants \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) from various graphical treatments of the data from Table 5.2

<table><tr><td>Graphical Method</td><td>\( {K}_{\mathrm{m}}\left( {\mu \mathrm{M}}\right) \)</td><td>Deviation from True \( {K}_{\mathrm{m}}\left( \% \right) \)</td><td>\( {V}_{\max }\left( {\mu \mathrm{M}/\mathrm{s}}\right) \)</td><td>Deviation from True \( {V}_{\max }\left( \% \right) \)</td></tr><tr><td>True values</td><td>12.00</td><td></td><td>100.00</td><td></td></tr><tr><td>Michaelis-Menten</td><td>11.63</td><td>3.08</td><td>100.36</td><td>0.36</td></tr><tr><td>Lineweaver-Burk (full data set)</td><td>7.57</td><td>36.92</td><td>79.28</td><td>20.72</td></tr><tr><td>Lineweaver-Burk ([S] = 0.25-5.0 \( {K}_{\mathrm{m}} \) only)</td><td>9.17</td><td>23.58</td><td>91.84</td><td>8.16</td></tr><tr><td>Eadie-Hofstee</td><td>9.66</td><td>19.50</td><td>94.45</td><td>5.55</td></tr><tr><td>Hanes-Wolff</td><td>11.84</td><td>1.33</td><td>100.97</td><td>0.97</td></tr><tr><td>Eisenthal-Cornish-Bowden</td><td>11.53</td><td>3.92</td><td>100.64</td><td>0.64</td></tr></table>

*[图片暂缺]*<!--missing-image: 20_448_957_720_520_0.jpg|-->

Figure 5.9 Lineweaver-Burk double-reciprocal plot for the full data set from Table 5.2. Note the strong influence of the data points at low [S] (high 1/[S] values) on the best fit line from linear regression.

The foregoing example should convince the reader of the limitations of using linear transformations of the primary data for determining the values of the kinetic constants. Nevertheless, the Lineweaver-Burk plots are still commonly used by many researchers and, as we shall see in later chapters, are useful tools for certain purposes. In these situations (described in detail in Chapters 10 and 13), we make the following recommendation. Rather than using linear regression to fit the reciprocal data in Lineweaver-Burk plots, one should determine the values of \( {V}_{\max } \) and \( {K}_{\mathrm{m}} \) by nonlinear regression analysis of the untransformed data fit to the Michaelis-Menten equation. These values are then inserted as constants into Equation 5.35 to create a line through the reciprocal data on the Lineweaver-Burk plot. The line drawn by this method may not appear to fit the reciprocal data as well as a linear regression fit, but it will be a much more accurate reflection of the kinetic behavior of the enzyme. The use of this method will be clearer when it is applied in Chapters 10 and 13 to studies of enzyme inhibition and multisubstrate enzyme mechanisms, respectively.

If one is to ultimately present experimental data in the form of a double-reciprocal plot, it is desirable to choose substrate concentrations that will be evenly spaced along a reciprocal \( x \) axis (i.e., 1/[S]). This is easily accomplished experimentally as follows. One picks a maximum value of \( \left\lbrack  S\right\rbrack  \left( \left\lbrack  {S}_{\max }\right\rbrack  \right) \) to work with and makes a stock solution of substrate that will give this final concentration after dilution into the assay reaction mixture. Additional initial velocity measurements are then made by adding the same final volume to the enzyme reaction mixture from stock substrate solutions made by diluting the original stock solution by 1:2, 1:3, 1:4, 1:5, and so on. In this way, the data points will fall along the 1/[S] axis at intervals of 1, 2, 3, 4, 5, ..., units.

For example, let us say that we have decided to work with a maximum substrate concentration of \( {60\mu }\mathrm{M} \) in our enzymatic reaction. If we prepare a \( {600\mu }\mathrm{M} \) stock solution of substrate for this data point, we might dilute it 1:10 into our assay reaction mixture to obtain the desired final substrate concentration. If, for example, our total reaction volume was \( {1.0}\mathrm{\;{mL}} \) , we could start our reaction by mixing \( {100\mu }\mathrm{L} \) of substrate stock, with \( {900\mu }\mathrm{L} \) of the other components of our reaction system (enzyme, buffer, cofactors, etc.). Table 5.5 summarizes the additional stock solutions that would be needed to prepare final substrate concentrations evenly spaced along a 1/[S] axis.

Table 5.5 Setup for an experimental determination of enzyme kinetics using a Lineweaver-Burk plot

<table><tr><td>Stock [S] (μM)</td><td>Final [S] in Reaction Mixture (μM)</td><td>1/[S] \( \left( {\mu {\mathrm{M}}^{-1}}\right) \)</td></tr><tr><td>600</td><td>60.0</td><td>0.017</td></tr><tr><td>300</td><td>30.0</td><td>0.033</td></tr><tr><td>200</td><td>20.0</td><td>0.050</td></tr><tr><td>150</td><td>15.0</td><td>0.067</td></tr><tr><td>120</td><td>12.0</td><td>0.083</td></tr><tr><td>100</td><td>10.0</td><td>0.100</td></tr><tr><td>86</td><td>8.6</td><td>0.116</td></tr><tr><td>75</td><td>7.5</td><td>0.133</td></tr><tr><td>67</td><td>6.7</td><td>0.149</td></tr><tr><td>60</td><td>6.0</td><td>0.167</td></tr><tr><td>55</td><td>5.5</td><td>0.182</td></tr><tr><td>50</td><td>5.0</td><td>0.200</td></tr></table>

### 5.7 OTHER LINEAR TRANSFORMATIONS OF ENZYME KINETIC DATA

Despite the errors associated with this method, the Lineweaver-Burk double reciprocal plot has become the most popular means of graphically representing enzyme kinetic data. There are, however, a variety of other linearizing transformations. Again, the use of these transformation methods is no longer necessary because most researchers have access to computer-based nonlinear curve-fitting methods, and the direct fitting of untransformed data by these methods is highly recommended. For the sake of historic perspective, however, we shall describe three other popular graphical methods for presenting enzyme kinetic data: Eadie-Hofstee, Hanes-Wolff, and Eisenthal-Cornish-Bowden direct plots. These linear transformation methods, which are here applied to enzyme kinetic data, are identical to the Wolff transformations described in Chapter 4 for receptor-ligand binding data.

#### 5.7.1 Eadie-Hofstee Plots

If we multiply both sides of Equation 5.25 by \( {K}_{\mathrm{m}} + \left\lbrack  \mathrm{S}\right\rbrack \) , we obtain:

\[
v\left( {{K}_{\mathrm{m}} + \left\lbrack  \mathrm{S}\right\rbrack  }\right)  = {V}_{\max }\left\lbrack  \mathrm{S}\right\rbrack \tag{5.37}
\]

If we now divide both sides by [S] and rearrange, we obtain:

\[
v = {V}_{\max } - {K}_{\mathrm{m}}\left( \frac{v}{\left\lbrack  \mathrm{\;S}\right\rbrack  }\right) \tag{5.38}
\]

Hence, if we plot \( v \) as a function of \( v/\left\lbrack  \mathrm{S}\right\rbrack \) , Equation 5.38 would predict a straight-line relationship with a slope of \( - {K}_{m} \) and \( y \) intercept of \( {V}_{\max } \) . Such a plot, referred to as an Eadie-Hofstee plot, is illustrated in Figure 5.10.

*[图片暂缺]*<!--missing-image: 22_477_1473_668_495_0.jpg|-->

Figure 5.10 Eadie-Hofstee plot of enzyme kinetic data. [Data taken from Table 5.2.]

#### 5.7.2 Hanes-Wolff Plots

If one multiplies both sides of the Lineweaver-Burk Equation (Equation 5.35) by [S], one obtains:

\[
\frac{\left\lbrack  \mathrm{S}\right\rbrack  }{v} = \left\lbrack  \mathrm{\;S}\right\rbrack  \left( \frac{1}{{V}_{\max }}\right)  + \frac{{K}_{\mathrm{m}}}{{V}_{\max }} \tag{5.39}
\]

This treatment also leads to linear plots when [S]/ \( v \) is plotted as a function of [S]. Figure 5.11 illustrates such a plot, which is known as a Hanes-Wolff plot. In this plot the slope is \( 1/{V}_{\max } \) , the \( y \) intercept is \( {K}_{\mathrm{m}}/{V}_{\max } \) , and the \( x \) intercept is \( - {K}_{\mathrm{m}} \) .

#### 5.7.3 Eisenthal-Cornish-Bowden Direct Plots

In our final method, pairs of \( v \) ,[S] data (as in Table 5.2) are plotted as follows: values of \( v \) along the \( y \) axis and the negative values of [S] along the x axis (Eisenthal and Cornish-Bowden, 1974). For each pair, one then draws a straight line connecting the points on the two axes and extrapolates these lines past their point of intersection (Figure 5.12). When a horizontal line is drawn from the point of intersection of these lines to the \( y \) axis, the value at which this horizontal line crosses the \( y \) axis is equal to \( {V}_{\max } \) . Similarly, when a vertical line is dropped from the point of intersection to the \( x \) axis, the value at which this vertical line crosses the \( x \) axis defines \( {K}_{\mathrm{m}} \) . Plots like Figure 5.12 are referred to as Eisenthal-Cornish-Bowden direct plots and are considered to give the best estimates of \( {K}_{\mathrm{m}} \) and \( {V}_{\max } \) of any of the linear transformation methods. Hence, they are highly recommended when it is desired to determine these kinetic parameters, but a nonlinear curve fitting to Equation 5.25 is not feasible.

*[图片暂缺]*<!--missing-image: 23_464_967_693_510_0.jpg|-->

Figure 5.11 Hanes-Wolff plot of enzyme kinetic data. [Data taken from Table 5.2.]

*[图片暂缺]*<!--missing-image: 23_478_1576_669_538_0.jpg|-->

Figure 5.12 Eisenthal-Cornish-Bowden direct plot of enzyme kinetic data. [Selected data taken from Table 5.2.]

### 5.8 MEASUREMENTS AT LOW SUBSTRATE CONCENTRATIONS

In some instances, the concentration range of substrates suitable for experimental measurements is severely limited because of poor solubility or some physicochemical property of the substrate that interferes with the measurements above a critical concentration. If one is limited to measurements in which the substrate concentration is much less than the \( {K}_{\mathrm{m}} \) , the reaction will follow pseudo-first-order kinetics, and it may be difficult to find a time window over which the reaction velocity can be approximated by a linear function. Even if quasi-linear progress curves can be obtained, a plot of initial velocity as a function of [S] cannot be used to determine the individual kinetic constants \( {k}_{\text{ cat }} \) and \( {K}_{\mathrm{m}} \) , since the substrate concentration range that is experimentally attainable is far below saturation (as in Figure 5.6A). In such situations, one can still derive an estimate of \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) by fitting the reaction progress curve to a first-order equation at some fixed substrate concentration.

Suppose that we were to follow the loss of substrate as a function of time under first-order conditions (i.e., where \( \left\lbrack  \mathrm{S}\right\rbrack   \ll  {K}_{\mathrm{m}} \) ). The progress curve could be fit by the following equation:

\[
\left\lbrack  \mathrm{S}\right\rbrack   = \left\lbrack  {\mathrm{S}}_{0}\right\rbrack  {e}^{-{kt}} \tag{5.40}
\]

where [S] is the substrate concentration remaining after time \( t,\left\lbrack  {\mathrm{\;S}}_{0}\right\rbrack \) is the starting concentration of substrate, and \( k \) is the observed first-order rate constant. When \( \left\lbrack  \mathrm{S}\right\rbrack   \ll  {K}_{\mathrm{m}} \) , the \( \left\lbrack  \mathrm{S}\right\rbrack \) term can be ignored in the denominator of Equation 5.25. Combining this with our definition of \( {V}_{\max } \) from Equation 5.11 we obtain:

\[
- \frac{d\left\lbrack  \mathrm{\;S}\right\rbrack  }{dt} = \frac{{k}_{\mathrm{{cat}}}}{{K}_{\mathrm{m}}}\left\lbrack  \mathrm{E}\right\rbrack  \left\lbrack  \mathrm{S}\right\rbrack \tag{5.41}
\]

Rearranging Equation 5.41 and integrating, we obtain:

\[
\left\lbrack  \mathrm{S}\right\rbrack   = \left\lbrack  {\mathrm{S}}_{0}\right\rbrack  \exp \left( {\frac{{k}_{\mathrm{{cat}}}}{{K}_{\mathrm{m}}}\left\lbrack  \mathrm{E}\right\rbrack  t}\right) \tag{5.42}
\]

Comparing Equation 5.42 with Equation 5.40, we see that:

\[
k = \frac{{k}_{\text{ cat }}}{{K}_{\mathrm{m}}}\left\lbrack  \mathrm{E}\right\rbrack   = \frac{{V}_{\max }}{{K}_{\mathrm{m}}} \tag{5.43}
\]

Thus, if the concentration of enzyme used in the reaction is known, an estimate of \( {k}_{\text{ cat }}/{K}_{\mathrm{m}} \) can be obtained from the measured first-order rate constant of the reaction progress curve when \( \left\lbrack  \mathrm{S}\right\rbrack   \ll  {K}_{\mathrm{m}} \) (Chapman et al.,1993; Wahl,1994).

### 5.9 DEVIATIONS FROM HYPERBOLIC KINETICS

In most cases, enzyme kinetic measurements fit remarkably well with the Henri-Michaelis-Menten behavior discussed in this chapter. However, occasional deviations from the hyperbolic dependence of velocity on substrate concentration are seen (e.g., Ferdinand, 1966). Such anomalies occur for several reasons. Some physical methods of measuring velocity, such as optical spectroscopies, can lead to experimental artifacts that have the appearance of deviations from the expected behavior, and we shall discuss these in detail in Chapter 7.

Nonhyperbolic behavior can also be caused by the presence of certain types of inhibitors as well. In the most often encountered case, substrate inhibition, a second molecule of the substrate can bind to the ES complex to form an inactive ternary complex, SES. Because the formation of the ES complex must precede the formation of the inhibitory ternary complex, substrate inhibition is usually realized only at high substrate concentrations, and it is detected as a lower-than-expected value for the measured velocity at these high substrate concentrations. Figure 5.13 illustrates the type of behavior one might see in an enzyme that exhibits substrate inhibition. At low substrate concentrations, the kinetics follow simple Michaelis-Menten behavior. Above a critical substrate concentration, however, the data deviate significantly from the expected behavior. The binding of the second, inhibitory, molecule of the substrate can be accounted for by the following equation:

\[
v = \frac{{V}_{\max }\left\lbrack  \mathrm{S}\right\rbrack  }{{K}_{\mathrm{m}} + \left\lbrack  \mathrm{S}\right\rbrack  \left( {1 + \frac{\left\lbrack  \mathrm{S}\right\rbrack  }{{K}_{\mathrm{i}}}}\right) } \tag{5.44}
\]

or dividing the top and bottom of the right-hand side of Equation 5.44 by [S], we obtain:

\[
v = \frac{{V}_{\max }}{1 + \frac{{K}_{\mathrm{m}}}{\left\lbrack  \mathrm{S}\right\rbrack  } + \frac{\left\lbrack  \mathrm{S}\right\rbrack  }{{K}_{\mathrm{i}}}} \tag{5.45}
\]

where the term \( {K}_{\mathrm{i}} \) in Equations 5.44 and 5.45 represents the dissociation constant for the inhibitory SES ternary complex. Inhibition effects at very high substrate concentrations also can be readily detected as nonlinearity in the Lineweaver-Burk plots of the data. Here, one observes a sudden and dramatic ascending curvature of the data near the \( y \) -axis intercept.

*[图片暂缺]*<!--missing-image: 25_455_1428_712_504_0.jpg|-->

Figure 5.13 Michaelis-Menten plot for an enzyme reaction displaying substrate inhibition at high substrate concentrations: dashed line, best fit of the data at low substrate concentrations to Equation 5.25; solid line, fit of all the data to Equation 5.45. The constant \( {K}_{\mathrm{i}} \) (Equation 5.45) will be described further in subsequent chapters.

Another cause of nonhyperbolic kinetics is the presence of more than one enzyme acting on the same substrate (see also Chapter 4, Section 4.3.2.2). Many enzyme studies are performed with only partially purified enzymes, and many clinical diagnostic tests that rely on measuring enzyme activities are performed on crude samples (of blood, tissue homogenates, etc.). When the substrate for the reaction is unique to the enzyme of interest, these crude samples can be used with good results. If, however, the sample contains more than one enzyme that can act on the substrate, deviations from the expected kinetic results occur. Suppose that our sample contains two enzymes; both can convert the substrate to product, but they display different kinetic constants. Suppose further that for one of the enzymes \( {V}_{\max } = {V}_{1} \) and \( {K}_{\mathrm{m}} = {K}_{\mathrm{t}} \) , and for the second enzyme \( {V}_{\max } = {V}_{2} \) and \( {K}_{\mathrm{m}} = {K}_{2} \) . The velocity of the overall mixture then is given by:

\[
v = \frac{{V}_{1}\left\lbrack  \mathrm{\;S}\right\rbrack  }{{K}_{1} + \left\lbrack  \mathrm{\;S}\right\rbrack  } + \frac{{V}_{2}\left\lbrack  \mathrm{\;S}\right\rbrack  }{{K}_{2} + \left\lbrack  \mathrm{\;S}\right\rbrack  } \tag{5.46}
\]

This can be rearranged to give the following expression (Schulz, 1994):

\[
v = \frac{\left( {{V}_{1}{K}_{2} + {V}_{2}{K}_{1}}\right) \left\lbrack  \mathrm{S}\right\rbrack   + \left( {{V}_{1} + {V}_{2}}\right) {\left\lbrack  \mathrm{S}\right\rbrack  }^{2}}{{K}_{1}{K}_{2} + \left( {{K}_{1} + {K}_{2}}\right) \left\lbrack  \mathrm{\;S}\right\rbrack   + {\left\lbrack  \mathrm{S}\right\rbrack  }^{2}} \tag{5.47}
\]

Equation 5.47 is a polynomial expression, which yields behavior very different from the rectangular hyperbolic behavior we expect; this is illustrated in Figure 5.14.

One last example of deviation from hyperbolic kinetics is that of enzymes displaying coop-erativity of substrate binding. In the derivation of Equation 5.25, we assumed that the active sites of the enzyme molecules behave independent of one another. As we saw in Chapters 3 and 4, sometimes proteins occur as multimeric assemblies of subunits. Some enzymes occur as homomultimers, each subunit containing a separate active site. It is possible that the binding of a substrate molecule at one of these active sites could influence the affinity of the other active sites in the multisubunit assembly (see Chapters 9 and 15 for more details). This effect is known as cooperativity. It is said to be positive when the binding of a substrate molecule to one active site increases the affinity for the substrate of the other active sites. On the other hand, when the binding of substrate to one active site lowers the affinity of the other active sites for the substrate, the effect is called negative cooperativity. The number of potential substrate binding sites on the enzyme and the degree of cooperativity among them can be quantified by the Hill coefficient, \( h \) . The influence of cooperativity on the measured values of velocity can be easily considered by modifying Equation 5.25 as follows:

\[
v = \frac{{V}_{\max }}{1 + {\left( \frac{{K}_{1/2}}{\left\lbrack  \mathrm{\;S}\right\rbrack  }\right) }^{h}} \tag{5.48}
\]

*[图片暂缺]*<!--missing-image: 26_462_1453_694_512_0.jpg|-->

Figure 5.14 Effects of multiple enzymes acting on the same substrate. The dashed line represents the fit of the data to Equation 5.25 for a single enzyme, while the solid line represents the fit to Equation 5.47 for two enzymes acting on the same substrate with \( {V}_{1} = {120\mu }\mathrm{M}/\mathrm{s},{V}_{2} = {75\mu }\mathrm{M}/\mathrm{s},{K}_{1} = {65\mu }\mathrm{M} \) , and \( {K}_{2} = {3\mu }\mathrm{M} \) .

where \( {K}_{1/2} \) (also referred to in the literature as \( {K}^{\prime } \) ) is related to \( {K}_{\mathrm{m}} \) but also contains terms related to the effect of substrate occupancy at one site on the substrate affinity of other sites (see Chapter 15). Figure 5.15 illustrates how positive cooperativity can affect the Michaelis-Menten and Lineweaver-Burk plots of an enzyme reaction.

The velocity data for cooperative enzymes can be presented in a linear form by use of Equation 5.49:

\[
\log \left( \frac{v}{{V}_{\max } - v}\right)  = h\log \left\lbrack  \mathrm{\;S}\right\rbrack   - \log \left( {K}^{\prime }\right) \tag{5.49}
\]

Thus, a plot of \( \log \left( {v/{V}_{\max } - v}\right) \) as a function of \( \log \left\lbrack  \mathrm{S}\right\rbrack \) should yield a straight line with a slope of \( h \) and a \( y \) intercept of \( - \log \left( {K}_{1/2}\right) \) , as illustrated in Figure 5.16. The utility of such plots is limited, however, by the requirement of knowing the value of \( {V}_{\max } \) a priori and because the linear relationship described by Equation 5.49 holds over only a limited range of substrate concentrations (in the region of \( \left\lbrack  \mathrm{S}\right\rbrack   = {K}_{1/2} \) ). Hence, whenever possible, it is best to determine \( {V}_{\max }, h \) , and \( {K}_{\mathrm{m}} \) for cooperative enzymes from a direct nonlinear curve that fits Equation 5.48.

*[图片暂缺]*<!--missing-image: 27_290_1578_1044_394_0.jpg|-->

Figure 5.15 Effects of positive cooperativity on the kinetics of an enzyme-catalyzed reaction: (A) data graphed as a Michaelis-Menten (i.e., direct) plot and (B) data from (A) replotted as a Lineweaver Burk double-reciprocal plot.

*[图片暂缺]*<!--missing-image: 28_462_246_693_515_0.jpg|-->

Figure 5.16 Hill plots for the data from Figure 5.15: \( \log \left\lbrack  {v/\left( {{V}_{\max } - v}\right) }\right\rbrack \) is plotted as a function of \( \log \left\lbrack  S\right\rbrack \) . The slope of the best fit line provides an estimated of the Hill coefficient \( h \) , and the \( y \) intercept provides an estimate of \( - \log \left( {K}_{1/2}\right) \) .

These examples illustrate the more commonly encountered deviations from hyperbolic kinetics. Several other causes of deviations are known, but they are less common. A more comprehensive discussion of such deviations can be found in the texts by Segel (1975) and Bell and Bell (1988).

### 5.10 SUMMARY

This chapter focused on steady-state kinetic measurements since these are the easiest to perform in a standard laboratory. These methods provide important kinetic and mechanistic information, mainly in the form of two kinetic constants, \( {k}_{\text{ cat }} \) and \( {K}_{\mathrm{m}} \) . Graphical methods for determining the values for these kinetic constants were presented.

## REFERENCES AND FURTHER READING

Bell, J. E., and Bell, E. T. (1988) Proteins and Enzymes, Prentice-Hall, Englewood Cliffs, NJ.

Briggs, G. E., and Haldane, J. B. S. (1925) Biochem. J. 19, 383.

Brown, A. J. (1902) J. Chem. Soc. 81, 373.

Chapman, K. T., Kopka, I. E., Durette, P. I., Esser, C. K., Lanza, T. J., Izquierdo-Martin, M., Niedzwiecki, L., Chang, B., Harrison, R. K., Kuo, D. W., Lin, T.-Y., Stein, R. L., and Hagmann, W. K. (1993) J. Med. Chem. 36, 4293.

Cleland, W. W. (1967) Adv. Enzymol. 29, 1-65.

Copeland, R. A. (1991) Proc. Natl. Acad. Sci. U.S.A. 88, 7281.

Copeland, R. A. (2013) Evaluation of Enzyme Inhibitors in Drug Discovery: A Guide for Medicinal Chemists and Pharmacologists, 2nd ed., Wiley, Hoboken, NJ.

Cornish-Bowden, A., and Wharton, C. W. (1988) Enzyme Kinetics, IRL Press, Oxford.

Eisenthal, R., and Cornish-Bowden, A. (1974) Biochem. J. 139, 715.

Ferdinand, W. (1966) Biochem. J. 98, 278.

Fersht, A. (1985) Enzyme Structure and Mechanism, Freeman, New York.

Henri, V. (1903) Lois Générales de l'action des diastases, Hermann, Paris.

Lineweaver, H., and Burk, J. (1934) J. Am. Chem. Soc. 56, 658.

Michaelis, L., and Menten, M. L. (1913) Biochem. Z. 49, 333.

Schulz, A. R. (1994) Enzyme Kinetics from Diastase to Multi-enzyme Systems, Cambridge University Press, New York.

Segel, L. H. (1975) Enzyme Kinetics, Wiley, New York.

Wahl, R. C. (1994) Anal Biochem. 219, 383.

Wilkinson, A. J., Fersht, A. R., Blow, D. M., and Winter, G. (1983) Biochemistry 22, 3581.