# Modeling the Dynamics of User Content Generation: A Case Study of Stack Exchange Websites
Here's a few alternative titles for the paper:
- **Dynamics of User Content Generation in Stack Exchange Websites: Modeling, Empirical Results, and Applications**
- **Failing at Scale: Modeling the Dynamics of User Content Generation in Stack Exchange Websites**
- **The Size Conundrum: Modeling the Dynamics of User Content Generation in Stack Exchange Websites**
- **Survival of the Fittest, not Fattest: Modeling the Dynamics of User Content Generation in Stack Exchange Websites**
- **Too big to succeed: Understanding successes and  failures at scale in Knowledge Exchange Markets**
- **Nail it but don't scale it: Understanding  failures at scale in Knowledge Exchange Markets**


Here's the outline of the paper:
1. **Introduction**
2. **Related Work**
3. **Problem Statement**
**Desiderata:** The desired properties of our content generation model, e.g., macroscopic, explanatory power, predictive power, parsimony/minimalism, comprehensive. [*Note:* This subsection is optional. The desired properties of model can be reported in Introduction.]
**Problem Formulation**
3. **Modeling Knowledge Exchange Markets**

   2. **The Cobb-Douglas Model** Formulating the modeling problem— instead of directly modeling content generation as a dynamic process (functions of time), we are modeling it in terms of associated factors, which themselves are dynamic.  [*Note:* This subsection is optional. The problem formulation can be reported in Introduction.]
   3. **Factors of Content Generation:** Recognizing the key factors that drive content generation in CQA platforms. In particular, we recognize two factors of content generation for different types of contents in Stack Exchange websites.
       1. **User Participation:** The number of users who participate in generating conent.
       2. **Content Dependency:**  The dependency of a type of content (e.g., answers) on other type of content(s) (e.g., questions).
   4. **Basis Functions:** Presenting alternative basis functions to capture the effect of a single factor on content generation.
   5. **Interaction among the Factors:** Potential interaction among the factors and resultant relationships.
   <!-- 6. **Proposed Model:** Alternative models capturing different possible relationships among the factors. We examine special cases, and establish connection between these cases and classical concepts such as the law of the minimum, economic production, etc. -->
5. **Datasets**
4. **Evaluating our Proposed Model**
   <!-- 1. **Dataset Description:** Number of websites, time period and other relevant description. -->
   2. **Parameter Estimation:** The parameters of our model, and how we estimate those.
   3. **Model Fitting Results / Parameter Analysis:** Best fit parameter values (and distribution) for different Stack Exchange websites. --Figure/Table: Plot/table to show the distributions for different parameters--
   4. **Forecasting Content Generation:** The effectiveness of our model in content prediction task. --Figure: Plot to show prediction accuracy (line chart)--
   5. **Sensitivity to Time Granularity:** The effectiveness study of our model under different time granularity, e.g., day, week, month, quarter. --Figure: Plot to show prediction accuracy for different time granularity (bar chart)--
   6. **Transfer Learning:** Using parameter distributions learnt from old Stack Exchange websites as prior distributions for new Stack Exchange websites. --Figure: Plot to compare the posteriors learnt using transfer learning with the posteriors learnt using more data points in future (bar chart)--
   7. **User to Asker/Answerer/Commenter:** Computing/predicting number of askers/answerers/commenters from number of users. --Figure: Plot to show the correlation between number of users and number of askers/answerers/commenters--
4. **Interpreting the Economic Model**
   1. **Diminishing Returns:** Explaining content generation in Stack Exchange websites in the light of Cobb-Douglas equation (to be found based on fitting) and diminishing return (co-limitation). --Figure: Plot to show the diminishing returns--
   2. **The Underlying Market Production: (optional? covered by the earlier section)** How content generation in Stack Exchange websites reflect market production.
   3. **Case Study:** [*Note:* This subsection is optional. The purpose of this subsection is to present surprising cases (if any).] The curious case of websites deviating from the diminishing return.
   4. **Two Key Distributions:** Content generation in the light of two key distributions, user activity and subject POV (perspective). We attempt to establish the hypothesis that as number of users increase, individuals with fewer resources join network. --Figure: Plot to show user activity and subject POV distributions--
   5. **Uncovering the Stable Core:** Showing the presence of a stable core that maintains the economic model. --Plots to show the age and size of core--
6. **Diseconomies of Scale**
   1. **Empirical Observation:** Backed by the diminishing returns, Stack Exchange websites undergo diseconomies of scale— the ratio of answers to questions go down with the increase in number of users. We compare the economic curves with logistic curves to justify effectiveness in capturing diseconomies of scale. --Figure: Plot to show answer to question ratio vs number of users fit for economic and logistic curves--
   2. **Decline in Health:** As the survival of CQA platforms directly depend on content generation, we investigate the adverse effect of scale on a set of health metrics. --Figure: Plot to show correlation between answer to question ratio and health metrics--
   3. **Decline in Stability:** The stability of CQA platforms also depend on user activity distribution. We investigate the stability of different Stack Exchange websites. --Figure: Plot to show stability as a function of economic parameters/size/etc.--
   4. **Effect on Controllability:** The controllability of CQA platforms also depend on user activity distribution. We investigate the controllability of different Stack Exchange websites. --Figure: Plot to show controllability as a function of economic parameters/size/etc.--
7. **Discussion**  [*Note:* This section is optional.] [*hs*: you should have a discussion section describing ambiguous cases, or cases not explained well. You should also have a section on limitations; you can briefly mention alternatives, but dont focus on them ]
   1. **Complementary and Alternative Models:** Presenting complementary and alternative models for predicting and explaining user content generation.
       1. **Hawkes Model:** Hawkes intensity process (HIP) to predict and explain user content generation.
   2. **Analysis of the Economic Model:** Presenting analytical results for the Cobb-Douglas model.
8. **Conclusion**
