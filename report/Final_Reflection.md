# Final Reflection on BBO Capstone
Initial codebase
To start my BBO project, I developed an efficient Python implementation that produced candidate query points and trained simple surrogate models with NumPy and scikit-learn. I intentionally built the solution incrementally rather than having a single optimization algorithm, so that the learning of each week could be added to the codebase. This enabled the repository to evolve from basic exploratory search into an organized optimization framework with Support Vector Regression (Week 3), Artificial Neural Networks (Week 4), PyTorch based learning (Week 5), CNN inspired hierarchical feature extraction (Week 6), Bayesian hyperparameter optimisation (Week 7), prompt optimization ideas (Week 8), transparency and interpretability techniques (Weeks 9-10), clustering (Week 11), PCA inspired dimensionality reduction (Week 12) and finally Reinforcement Learning ideas (Week 13).

This modular architecture helped to understand the contribution of each optimization technique rather than treating the solution as a black box.

Code modifications
There were many differences in the code between the thirteen submissions.

Weeks 1 and 2 were spent mostly in exploration, using evenly distributed query points. For example, Function 1 started at approximately (0.211325, 0.788675) and then proceeded towards (0.654299, 0.353479) and finally settled around (0.582812, 0.421077), which was one of the most stable performing regions for the rest of the project.

In Week 3, we introduced Support Vector Regression to approximate the hidden objective functions. Week 4 introduced Neural Networks trained with stochastic gradient descent and backpropagation to improve nonlinear modeling.

By week 5, I started to exploit high performing regions rather than continue to explore new regions. This worked particularly well for Function 5 where candidate points always converged around: (0.57–0.61,0.95,0.95,~0.00)

Across a range of submissions, this region produced the best results consistently, providing further evidence for the value of local exploitation rather than unrestricted exploration.

Week 6 saw the introduction of CNN inspired feature extraction to better model local relationships between neighbouring candidate points. In Week 7 we used Bayesian Optimization to automatically select the parameters, rather than the user selecting them.

Weeks 8–10 improved transparency with structured documentation, Model Cards, Datasheets and GitHub organization. These weeks did not directly lead to improvement in prediction accuracy, but they significantly improved reproducibility and interpretability.

In week 11 we learned clustering techniques to find promising areas to search. Rather than treating all previous evaluations equally, we cluster high and low performing regions before proposing new candidate points.

In week 12 we reduced redundant search behaviour using PCA-inspired dimensionality reduction while preserving informative candidate directions.

Week 13 gave Reinforcement Learning concepts such as exploration-exploitation tradeoff, policy improvement and adaptive feedback. The next generation of queries was more and more informed by the historic performance, instead of restarting the exploration after each iteration.

Final standings
My results were all over the place for the thirteen rounds. This was a demonstration of the difficulty of black-box optimization.

Function 1 was very stable after converging to around (0.582812, 0.421077) and needed very little further tuning. Function 2 also gradually converged to the Golden Ratio inspired solution (0.723607, 0.276393), but other local searches were also tried from time to time.

The biggest success of the project was the function 5. Initial experiments showed large gains after giving up on wide exploration and repeatedly improving the best performing neighborhood. This exploitation strategy always gave the best payoffs, even in later rounds with outputs over 1800.

Functions 3, 4 and 6 were much more difficult than the other functions. The outcomes they obtained were frequently either negative or inconsistent, even when experimenting with various modeling approaches such as Neural Networks, Bayesian Optimization, CNN-inspired architectures, clustering, and PCA. This demonstrated that sophisticated optimization algorithms are not able to fully overcome difficult objective landscapes when observations are limited.

If I did the project again, I’d bring in Bayesian Optimization and clustering much earlier, and scale back extraneous exploration after I found stable, high performing regions.

Trade-offs and decisions
The most important trade-off in the capstone was between exploration and exploitation.

Because there was very little information available, early submissions deliberately sampled widely. But as Week 5 approached, it was becoming increasingly clear that exploring random regions often led to a decrease in overall performance.

Hence, later submissions focused more candidate points around historically successful solutions, while maintaining a small percentage of exploratory samples to avoid premature convergence.

Another big trade-off was the model's complexity. Optimization framework was significantly improved by Neural Networks, Bayesian Optimization and clustering, but also increased computational cost and risk of over-fitting due to the relatively small number of observations for each function.

The project demonstrated that better optimization is possible without more complex models. The careful exploitation of historical information was often more profitable than the introduction of new algorithms.

Learning, application and looking back
The biggest thing I took away is that optimization is fundamentally an iterative learning process, not a prediction problem.

So the outputs of each week then became valuable training data for the next week. Instead of floundering around, I gradually learned which areas to dig deeper into and which ones I could safely ignore.

Multiple optimization strategies were combined to bring a much stronger optimization framework than any of the individual techniques. These included Support Vector Regression, Neural Networks, Bayesian Optimization, CNN inspired feature extraction, clustering, PCA and Reinforcement Learning.

These lessons directly relate to hyperparameter optimization, financial forecasting, AI product development, cybersecurity analytics, and healthcare decision-support systems, where balancing uncertainty with evidence-based optimization is crucial.

The biggest surprise in retrospect was that more and more sophisticated algorithms were not always better.

The largest improvements were often in understanding previous outputs, rather than new modeling techniques per se.

For example, repeatedly improving the successful Function 5 neighbourhood resulted in significantly larger improvements than searching unexplored regions all the time. In addition, stable candidates for Functions 1 and 2 were often more useful than replacing them with completely new exploratory queries.

Another important lesson was learning that the quality of optimization is as much a function of documentation and reproducibility as predictive accuracy. A well-structured GitHub repo, Model Cards and Datasheets, and documenting each week's design decisions led to transparent and reproducible optimization.

Overall, this capstone reminded us that there is no one optimal strategy for black-box problems. Effective optimization includes continuous learning from past observations, adapting the search behavior and balancing exploration and exploitation with increasing amount of evidence. These principles will form the foundation of my future machine learning and optimization projects.

