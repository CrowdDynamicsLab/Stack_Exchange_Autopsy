# Modeling the Dynamics of User Content Generation: A Case Study of Stack Exchange Websites
Here's a few alternative titles for the paper:
- **Dynamics of User Content Generation in Stack Exchange Websites: Modeling, Empirical Results, and Applications**
- **Failing at Scale: Modeling the Dynamics of User Content Generation in Stack Exchange Websites**
- **The Size Conundrum: Modeling the Dynamics of User Content Generation in Stack Exchange Websites**
- **Survival of the Fittest, not Fattest: Modeling the Dynamics of User Content Generation in Stack Exchange Websites**




Here's the outline of the paper:
1. **Introduction**
2. **Related Work**
3. **Modeling User Content Generation**
   1. **Desiderata:** The desired properties of our content generation model, e.g., macroscopic, explanatory power, predictive power, parsimony/minimalism, comprehensive. [*Note:* This subsection is optional. The desired properties of model can be reported in Introduction.]
   2. **Problem Formulation:** Formulating the model-- instead of directly modeling content generation as a dynamic process (functions of time), we are modeling it in terms of associated factors, which themselves are dynamic.  [*Note:* This subsection is optional. The problem formulation can be reported in Introduction.]
   3. **Factors of Content Generation:** Recognizing the key factors that drive content generation in CQA platforms. In particular, we recognize two factors of content generation for different types of contents in Stack Exchange websites. 
       1. **User Participation:** The number of users who participate in generating conent.
       2. **Content Dependency:**  The dependency of a type of content (e.g., answers) on other type of content(s) (e.g., questions).
   4. **Basis Functions:** Present alternative basis functions to capture the effect of a single factor on content generation. 
   5. **Interaction among the Factors:** Potential interaction among the factors and resultant relationships. 
   6. **Proposed Model:** A model (based on generalized/power mean) that can represent different possible relationships among the factors. We present special cases of our model, and establish connection between these cases and classical concepts such as the law of the minimum, economic production, etc.
4. **Empirical Analysis I (Model)** [*Note:* This is the first of the two empirical analysis sections.]
   1. **Dataset Description:** Number of websites, time period and other relevant description.
   2. **Bayesian Parameter Estimation:** The parameters of our model, and how we use the Bayesian framework to estimate those.
   3. **Model Fitting Results / Parameter Analysis:** Best fit parameter values (and distribution) for different Stack Exchange websites. --Figure: Plot to show the distributions for different parameters--
   4. **Model Interpretation:** Explaining content generation in Stack Exchange websites in the light of Cobb-Douglas equation (to be found based on fitting) and diminishing return (co-limitation). --Figure: Plot to show the diminishing returns--   
   5. **The Underlying Market Production:** How content generation in Stack Exchange websites reflect market production.
   6. **Case Study:** [*Note:* This subsection is optional. The purpose of this subsection is to present surprising cases (if any).] The curious case of websites deviating from the diminishing return.
   7. **Uncovering Two Key Distributions:** Content generation in the light of two key distributions, user activity and subject POV (perspective). We attempt to establish the hypothesis that as number of users increase, individuals with fewer resources join network. --Figure: Plot to show user activity and subject POV distributions--
   8. **Forecasting Content Generation:** The effectiveness of our model in content prediction task. --Figure: Plot to show prediction accuracy (line chart)--   
   9. **Sensitivity Analysis / Sensitivity to Time Granularity:** The effectiveness study of our model under different time granularity, e.g., day, week, month, quarter. --Figure: Plot to show prediction accuracy for different time granularity (bar chart)--   
   10. **Why Economic Model Works? / Stability of Core:** Showing the presence of a stable core that maintains the economic model. --Plots to show the age and size of core--
5. **Empirical Analysis II (Applications)** 
   1. **Diseconomies of Scale:** Backed by the diminishing returns, Stack Exchange websites undergo diseconomies of scale-- the ratio of answers to questions go down with the increase in number of users. We compare the economic curves with logistic curves to justify effectiveness. --Figure: Plot to show answer to question ratio fit for different number of users--  
   2. **Health of CQA Platforms:** As the survival of CQA platforms direcly depend on content generation, we investigate the adverse effect of scale on a set of health metrics. --Figure: Plot to show correlation between answer to question ratio and health metrics-- 
   3. **Stability of CQA Platforms:** The stability of CQA platforms depend on user activity distribution. We investigate the stability of different Stack Exchange websites. --Figure: Plot to show stability as a function of economic parameters/size/etc.--
   4. **Controllability of CQA Platforms:** The controllability of CQA platforms also depend on user activity distribution. We investigate the controllability of different Stack Exchange websites. --Figure: Plot to show controllability as a function of economic parameters/size/etc.--
6. **Discussion**  [*Note:* This section is optional. The implications of our research can be reported in Conclusion.]
   1. **Analysis of the Best Fit Model:** Presenting analytical results for the Cobb-Douglas model.
   2. **Implications:** The implications of our research and new research questions.
7. **Conclusion**
