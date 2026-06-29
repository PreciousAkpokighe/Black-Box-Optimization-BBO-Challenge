# Week 5 Reflection – Refining Strategy for Black-Box Optimisation

1. Hierarchical Feature Learning and Optimisation Strategy

The concept of hierarchical feature learning influenced my optimisation strategy by shifting my focus from individual input variables to interactions between variables across different dimensions. Instead of adjusting inputs independently as in earlier iterations, I began to treat each input vector as a structured representation where relationships between features determine performance.

By using neural networks as surrogate models, I leveraged their ability to learn layered representations of the input space. This helped identify promising regions where combinations of variables consistently produced higher outputs. As a result, my Week 5 strategy prioritised refining these regions rather than making isolated or random adjustments.

2. Parallel with AlexNet/ImageNet Breakthroughs

The evolution of my approach mirrors the progression seen in breakthroughs such as AlexNet and ImageNet. Early in the capstone, improvements were driven by simple heuristics and broad exploration. However, similar to how deep learning advancements built on incremental architectural and training improvements, my performance gains came from gradually refining the optimisation process.

Introducing neural networks, ensemble modelling, and uncertainty-based selection did not immediately produce perfect results, but each enhancement contributed to more stable and informed predictions. This reflects how real-world AI breakthroughs often emerge from cumulative improvements rather than a single major change.

3. Trade-offs: Depth, Complexity, and Efficiency vs Exploration–Exploitation

I encountered trade-offs similar to those in neural network training when deciding between model complexity and efficiency. More complex models (deeper networks) were better at capturing non-linear patterns but were also more prone to overfitting due to the limited dataset. Simpler models were more stable but lacked expressive power.

This trade-off closely parallels the exploration–exploitation balance in the BBO challenge. Increasing model complexity is similar to exploring richer hypothesis spaces, while simpler models align with exploiting known patterns. In Week 5, I balanced this by using moderately deep networks with regularisation and combining model-driven exploitation with controlled exploration of new regions.

4. Neural Network Building Blocks and Learning Process

Reflecting on neural network building blocks—inputs, activations, loss functions, gradients, and weight updates—helped me better understand how the model learns from data. Backpropagation allowed the model to estimate how changes in inputs affect outputs, effectively providing directional guidance for optimisation.

This insight improved my strategy by enabling more informed adjustments rather than relying purely on trial-and-error. Understanding gradients and weight updates also highlighted the importance of stable training, as unreliable gradients can lead to poor predictions and ineffective optimisation decisions.

5. Framework Perspective: Prototyping vs Production

My optimisation approach aligns more closely with rapid prototyping rather than production-ready design. Throughout the capstone, I prioritised flexibility, experimentation, and iterative improvement over building a fixed pipeline. This approach is similar to how frameworks like PyTorch are used in research settings, where adaptability is essential.

Given the uncertainty inherent in black-box optimisation, this flexible approach allowed me to quickly test different strategies, refine models, and adjust hyperparameters. A production-ready approach would require more robust validation, larger datasets, and stricter model evaluation.

6. Real-World Deep Learning Insights and Benchmarking Success

Insights from real-world deep learning applications influenced how I evaluated success in the capstone. In practice, model performance is judged not only by peak accuracy but also by consistency, robustness, and generalisation.

Applying this to my project, I moved away from focusing solely on maximising individual outputs and instead considered the reliability of predictions across multiple functions. Techniques such as ensemble modelling and uncertainty-aware selection improved robustness, making my optimisation strategy more aligned with real-world machine learning systems.

