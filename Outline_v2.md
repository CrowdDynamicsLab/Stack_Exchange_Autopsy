# Too big to succeed: Understanding successes and failures at scale in Knowledge Exchange Markets

Here's the outline of the paper:
1. **Introduction**
2. **Related Work**
1. **Problem Formulation:** The desired properties of our content generation model, e.g., macroscopic, explanatory power, predictive power, parsimony/minimalism, comprehensive. Formulating the modeling problem— instead of directly modeling content generation as a dynamic process (functions of time), we are modeling it in terms of associated factors, which themselves are dynamic.  [*Note:* This subsection is optional. The problem formulation can be reported in Introduction.]
4. **Modeling User Content Generation**
   1. **Factors of Content Generation:** Recognizing the key factors that drive content generation in CQA platforms. In particular, we recognize two factors of content generation for different types of contents in Stack Exchange websites.
       1. **User Participation:** The number of users who participate in generating conent.
       2. **Content Dependency:**  The dependency of a type of content (e.g., answers) on other type of content(s) (e.g., questions).
   2. **Basis Functions:** Presenting alternative basis functions to capture the effect of a single factor on content generation.
   3. **Interaction among the Factors:** Potential interaction among the factors and resultant relationships.
   4. **Proposed Model:** Alternative models capturing different possible relationships among the factors. We examine special cases, and establish connection between these cases and classical concepts such as the law of the minimum, economic production, etc.
   5. **User to Asker/Answerer/Commenter:** Computing/predicting number of askers/answerers/commenters from number of users. --Figure: Plot to show the correlation between number of users and number of askers/answerers/commenters--
5. Dataset
6. **Evaluating Our Proposed Models**
In this section, we examine our proposed models from three different perspectives: the accuracy of fitting content generation time series observed in our dataset, the performance of predicting content generation in long and short run, and the perplexity of characterizing content generation dynamics at early stage.
   1. **Parameter Estimation:** The parameters of our model, and how we estimate those.
   2. **Model Fitting Results:** Best fit parameter values (and distribution) for different Stack Exchange websites. --Figure/Table: Plot/table to show the distributions for different parameters--
   3. **Forecasting Content Generation:** The effectiveness of our model in content prediction task. --Figure: Plot to show prediction accuracy (line chart)--
       1. **Sensitivity to Time Granularity:** The effectiveness study of our model under different time granularity, e.g., day, week, month, quarter. --Figure: Plot to show prediction accuracy for different time granularity (bar chart)--
   4. **Transfer Learning:** Using parameter distributions learnt from old Stack Exchange websites as prior distributions for new Stack Exchange websites. --Figure: Plot to compare the posteriors learnt using transfer learning with the posteriors learnt using more data points in future (bar chart)--
7. **Model Interpretation**
In this section, we interpret our model and its foundations by characterizing knowledge market (Section 6.1), revealing two key distributions that control the market (Section 6.2), and uncovering the stable core that maintains market equilibrium (Section 6.3).
   1. **Characterizing Knowledge Market:** Explaining content generation in Stack Exchange websites in the light of Cobb-Douglas equation (to be found based on fitting) and diminishing return (co-limitation). --Figure: Plot to show the diminishing returns--
   2. **Two Key Distributions:** We reveal two key distributions that control content generation in knowledge markets, namely 
user activity and subject POV (perspective). --Figure: Plot to show user activity and subject POV distributions--
   5. **Uncovering the Stable Core:** We show the presence of a stable core of users that control the dynamic market equilibrium hypothesized by the Cobb-Douglas function. --Plots to show the age and size of core--
8. **Diseconomies of Scale**
   1. **Empirical Observation:** Backed by the diminishing returns, Stack Exchange websites undergo diseconomies of scale— the ratio of answers to questions go down with the increase in number of users. We compare the economic curves with logistic curves to justify effectiveness in capturing diseconomies of scale. --Figure: Plot to show answer to question ratio vs number of users fit for economic and logistic curves--
   2. **Decline in Health:** As the survival of CQA platforms direcly depend on content generation, we investigate the adverse effect of scale on a set of health metrics. --Figure: Plot to show correlation between answer to question ratio and health metrics--
   3. **Decline in Stability:** The stability of CQA platforms also depend on user activity distribution. We investigate the stability of different Stack Exchange websites. --Figure: Plot to show stability as a function of economic parameters/size/etc.--
   4. **Affects on Controllability:** The controllability of CQA platforms also depend on user activity distribution. We investigate the controllability of different Stack Exchange websites. --Figure: Plot to show controllability as a function of economic parameters/size/etc.--
9. **Discussion**  [*Note:* This section is optional.]
   1. **Complementary and Alternative Models:** Presenting complementary and alternative models for predicting and explaining user content generation.
       1. **Hawkes Model:** Hawkes intensity process (HIP) to predict and explain user content generation.
   2. **Analysis of the Economic Model:** Presenting analytical results for the Cobb-Douglas model.
10. **Conclusion**
