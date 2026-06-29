# 1. Previous round results show that the exploration has different effect on different functions. On the other hand, function 5 got better and better when I asked about successful areas of the past vs. exploring totally new areas. This pattern helped me in Week 11 to work harder to find clusters of good inputs and generate candidates around a cluster.

In cases where the outputs were still negative or unstable (Functions 3, 4 and 6), the historical results showed that the broad exploration was not leading to significant improvements. So I switched to a more focused search strategy based on local neighborhoods and cluster centroids, rather than pure random sampling.

2. Yes. I found a number of high performing observations in a relatively tight band of the search space. The strongest evidence of clustering was thus for Function 5. I saw a local optimum that could be exploited more. I also observed moderate clustering behaviour for Functions 1,2,7 and 8 where neighbouring inputs yield similar outputs. However, the clustering signal was weaker for Functions 3, 4 and 6, indicating a more complex landscape or that the current samples have not yet reached promising regions.

Thus for week 11 queries I used a combination of centroid based sampling and local perturbations around the best performing historical observations.

3. The least successful approach was a uniform global exploration of the whole search space. This worked well at first, but became less useful as more and more data was accumulated.

Large random jumps often resulted in solutions much worse than the existing observations, especially for Functions 3, 4 and 6. Higher rates of exploration, which did not take into account past performance, also resulted in declining returns.

To tackle this problem, I reduced the number of candidates in the global search, and improved the local search around the cluster centroids. But I kept a small percentage of exploratory candidates to prevent premature convergence.

4. Clustering algorithms try to find groups of similar observations and to reduce the effect of outliers and noise.

Likewise my week 11 strategy is about looking at areas where multiple observations give consistent positive outputs. I use the dense areas of high performing samples instead of all historical data and discount the effect of isolated poor performing points.

This approach provides a way to discriminate meaningful trends from stochastic variations and focus the effort of optimisation where success is most likely.

5. If I could see the results I would expect to see a number of different clusters that reflected different areas of similar performance.

Function 5 would be a dense cluster of high value observations primarily, suggesting a stable area for further exploitation. Functions 1, 2, 7, 8 may have a strong tendency to cluster in successful regions.  On the other hand we would expect Functions 3, 4 and 6 to be more spread out and show either multiple local optima or that the best regions were not sampled enough.

These visual patterns would inform where further exploitation is warranted, informing the next iteration.  The idea would be to fine tune high performing clusters, to slowly open up hidden opportunities in under performing areas.

