# 1. Why did you submit for this round the tenth time? For each function, what did the patterns in previous rounds lead you to do?
I had a transparency-driven optimization strategy as the basis for my submission for week 10. Instead of just picking the query points based on the predicted performance, I used the historical observations from weeks 1-9 to see how each function behaved with past inputs. Since functions 5, 7 and 8 always produced positive output, I focused on exploitation around their best regions. Function 5 was particularly effective as repeated tweaking around high performing inputs resulted in outputs over 1700, suggesting a highly productive region worth further investigation.

The outputs for Functions 3, 4 and 6 were still negative after several rounds of optimisation. Rather than doing random exploration, I used Bayesian optimisation, Gaussian Process modelling and feature sensitivity analysis to find which input dimensions appeared most influential. This enabled me to do more targeted exploration and keep interpretability. I started to develop a function-specific behaviour, instead of using the same search behaviour for all functions.

2. How transparent is your decision making process? Can anyone else do what you did?
I think that the process of decision making is very transparent, as all questions were supported with historical inputs and outputs, model predictions, uncertainty estimates, and reasoning that was documented. I kept Jupyter notebooks, GitHub documentation, reflection notes and optimisation scripts throughout the project documenting how each new query was generated.

Another researcher would be able to reproduce my approach, using the same historical dataset, Bayesian optimisation framework, Gaussian Process surrogate model, feature importance analysis and acquisition functions. They would also need access to the assumptions I made about exploitation vs exploration and the weighting assigned to uncertainty when selecting candidates. The process is reproducible and auditable, because all decisions are based on documented observations, not just on intuition.

3. What are your assumptions in your search/optimisation strategy?
One of the key assumptions is that neighbouring points in the search space will generate similar outputs. This assumption is the basis of the Gaussian Process model and the Bayesian optimisation strategy. It allows the model to infer promising regions based on previously observed data.

We further assume that the underlying functions are stationary during the challenge, i.e. the mapping from inputs to outputs does not change over time. Also I assume that e.g. regions with high outputs all the time, such as Function 5, will contain valuable solutions also in future rounds. These assumptions are helpful in directing optimisation but can potentially limit performance if the functions have sudden discontinuities or obscure behaviours.

4. Do you see any gaps or possible biases in your dataset?
The primary bias in my data set is the growing emphasis on exploitation. Function 5 continued to produce good outputs so more samples were placed around the high performing region. This improved short-term performance but came at the expense of coverage of other unexplore areas.

Another limitation is that some functions (especially Functions 3, 4 and 6) have been less successfully sampled than Functions 5, 7 and 8. This leads to an imbalance in the dataset and can bias the surrogate model towards regions that are already promising. There are still large regions of the search space that have not been explored where better solutions could exist, but have not yet been sampled.

5. What is a major weakness of your approach?
The biggest limitation of my approach is that the dataset available for each function is quite small. Even after 10 rounds the number of observations is limited compared to the dimensionality of some functions. This leads to a risk of overfitting the surrogate model to local patterns, which may not generalise across the entire search space.

Moreover the optimisation strategy is based on the past performance being a reliable indicator of future success. If the function contains hidden discontinuities, multiple local optima, or unexpected emergent behaviours, the model can wrongly favour familiar regions of the search space over better solutions elsewhere. So, while the strategy is getting more and more data-driven and interpretable, uncertainty remains a fundamental challenge in black-box optimization environments.

