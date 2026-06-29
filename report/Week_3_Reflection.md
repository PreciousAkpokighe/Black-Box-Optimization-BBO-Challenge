# Part 2: Reflection on my strategy

Strategy change from Week 2 to Week 3

I used an SVM-inspired margin strategy for Week 3. Since each function only had two observed points, training a full soft-margin or kernel SVM was not statistically robust. Instead, I treated the better-performing point between Week 1 and Week 2 as the positive side of the margin and generated the Week 3 input by moving slightly further in that direction, while clipping all values to the valid range of 0 to 1. This approach approximates the idea of moving deeper into a higher performing region while remaining consistent with the limited available data.

Use of exploration and exploitation

In Week 3, I applied a more refined balance between exploration and exploitation:

Exploitation: For functions where Week 2 performed well or remained competitive (e.g., Functions 5 and 8), I made small adjustments in the same direction to refine performance.

Correction (Reverse Exploitation): For functions where Week 2 performed worse than Week 1 (e.g., Functions 2, 3, 6, and 7), I moved the inputs back toward the Week 1 values to recover performance.

Exploration: For Function 1, where both outputs were extremely close to zero, I treated the region as uncertain and selected a completely new input to explore a different part of the search space.

Directed Exploration: For Function 4, where Week 2 improved compared to Week 1, I continued moving in the same direction to further explore that improving region.

This approach ensured that I did not overcommit to poor regions while still refining promising ones.

SVM influence of Week 2 results

Using Support Vector Machines (SVMs) would introduce a more structured, model-based approach to the optimisation process. Instead of relying purely on observed outputs, I could label input points as high-performing or low-performing based on a chosen threshold and train an SVM to learn the boundary between these regions.

A soft-margin SVM would be particularly useful because the data is likely noisy and not perfectly separable. It would allow some misclassification while still identifying the general trend between good and poor-performing inputs. Since the response surface appears to be non-linear (as seen from the large variation in outputs), a kernel SVM (e.g., RBF kernel) would be more effective than a linear SVM. This would help capture complex relationships between input variables and performance.

Overall, using SVMs could guide the optimisation by helping identify promising regions of the input space more efficiently, rather than relying solely on trial-and-error exploration.

Model assumptions and limitations

The variation in outputs across weeks suggests that the underlying functions are non-linear and complex.

Large changes in output values from small input adjustments indicate that simple linear models would not capture the true behaviour.

The presence of both very high positive values and strong negative values suggests a highly irregular response surface.

Because of this, the strategy relied on empirical testing and adaptive updates rather than assuming a specific model structure.

What overall impact does this challenge have in influencing my thinking to align more closely with that of a data scientist?

The black-box setup encourages thinking like a data scientist by requiring decisions to be made under uncertainty and incomplete information. Since the underlying functions are unknown, I had to rely on observed outputs, identify patterns, and iteratively refine my approach rather than applying a fixed formula.

This process developed key data science skills such as:

Hypothesis testing (trying inputs and observing results)

Iterative learning (improving decisions based on feedback)

Balancing exploration and exploitation when searching for optimal solutions

Working with limited data to make informed decisions

It also reinforced the importance of being adaptive, as strategies needed to change when results did not improve. Overall, the experience mirrors real-world data science problems where models must be built and refined without full visibility into the system.

