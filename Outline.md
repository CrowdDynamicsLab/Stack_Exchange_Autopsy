# Modeling the Dynamics of User Content Generation: A Case Study of Stack Exchange Websites
Here's a few alternative titles for the paper:
- **Failing at Scale: Modeling the Dynamics of User Content Generation in Stack Exchange Websites**
- **The Size Conundrum: Modeling the Dynamics of User Content Generation in Stack Exchange Websites**
- **Dynamics of User Content Generation in Stack Exchange Websites: Modeling, Empirical Results, and Applications**



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
4. **Empirical Analysis / Empirical Study I** [*Note:* This is the first of two empirical analysis sections.]
   1. **Dataset Description:** Number of websites, time period and other relevant description.
   2. **Bayesian Parameter Estimation:** The parameters of our model, and how we use the Bayesian framework to estimate those.
   3. **Model Fitting Results / Parameter Analysis:** Best fit parameter values (and distribution) for different Stack Exchange websites (with diagrams).
   4. **Model Interpretation:** Explaining content generation in Stack Exchange websites in the light of Cobb-Douglas equation (to be found based on fitting) and diminishing return (co-limitation).   
   5. **The Underlying Market Production:** How content generation in Stack Exchange websites reflect market production.
   6. **Case Study:** [*Note:* This subsection is optional. The purpose of this subsection is to present surprising cases (if any).] The curious case of websites deviating from the diminishing return.
   7. **Uncovering Two Key Distributions:** Content generation in the light of two key distributions, user activity and subject POV (perspective). We attempt to establish the hypothesis that individuals are coming with lower resources.
   8. **Forecasting Content Generation:** the effectiveness of our model in prediction task.
   9. **Model Sensitivity / Sensitivity to Time Granularity:** the effectiveness study of our model under different time granularity, e.g., day, week, month, quarter.
5. **Discussion**
   1. **Analysis of the Best Fit Model:** present theoretical analysis of the best fit model and the implications.
   2. **Implications and Future Directions:** the implications (new applications) of our research and potential research questions. 
6. **Conclusion**
