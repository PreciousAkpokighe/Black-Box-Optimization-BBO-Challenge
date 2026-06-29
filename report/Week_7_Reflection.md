# Week 7 Reflection – Hyperparameter Tuning Strategy

For this round, I focused on tuning the most influential hyperparameters in my surrogate optimisation model. The key parameters I adjusted were learning rate, kernel choice, exploration–exploitation balance, regularisation strength, and the number of optimisation iterations. I prioritised these because they directly affect prediction accuracy, convergence speed, and how effectively the model searches promising regions of the black-box functions.

Hyperparameter tuning significantly changed my query strategy compared with earlier rounds. In the beginning, my submissions were more heuristic and exploratory, using broad sampling across the search space. With more historical data now available, tuning allowed me to become more targeted. I relied less on random exploration and more on data-driven exploitation, especially for Function 5, where previous outputs showed strong gains in a specific region. This meant my Week 7 queries balanced preserving successful zones while still exploring uncertain functions.

The main tuning methods I applied were manual adjustment and Bayesian Optimisation. Manual tuning helped me quickly refine parameters such as step size and exploration weights based on observed outputs. Bayesian Optimisation was more effective for systematically searching combinations of hyperparameters and selecting those with the highest expected improvement. Compared with grid search, it was more efficient because it avoided testing many poor combinations. The main trade-off I noticed was computational time versus precision: more tuning improved results, but also increased model complexity.

As the dataset grew to 16 points, some model limitations became clearer. A few functions showed diminishing returns, where additional tuning only created small improvements. There is also a risk of overfitting to historical outputs, especially when one function performs well repeatedly. To manage this, I used regularisation and maintained limited exploration for weaker-performing functions.

In future rounds with larger datasets, I would expand tuning to include adaptive learning rates, ensemble surrogate models, and automated early stopping. For more complex ML projects, I would also consider Hyperband or random search when speed is important.

Overall, this black-box optimisation exercise has helped me think like a professional ML practitioner. In real-world problems, perfect information is rare, so success depends on iteratively testing assumptions, tuning parameters, learning from results, and adjusting strategy using evidence rather than guesswork.

