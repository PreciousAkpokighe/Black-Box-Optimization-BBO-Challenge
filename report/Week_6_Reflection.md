# Week 6 Reflection – CNN-Informed Optimisation Strategy

1. Progressive Feature Extraction and Strategy Refinement

The concept that CNNs progressively extract features—from simple patterns to more complex representations—significantly influenced my Week 6 optimisation strategy. Instead of treating each iteration independently, I approached the BBO process as a layered learning system where insights from previous weeks accumulate and guide future decisions.

This was particularly evident in how I handled Function 5. The significant performance improvement observed in Week 5 indicated that the model had identified a highly promising region in the input space. Rather than exploring new areas, I adopted a CNN-inspired refinement approach by focusing on small adjustments around this high-performing input. This reflects how deeper CNN layers refine and enhance previously learned features.

2. Parallels with CNN Breakthroughs (LeNet to Modern CNNs)

The evolution of my approach mirrors the progression seen in CNN architectures such as LeNet and more advanced models. Early stages of the capstone relied heavily on broad exploration and simple heuristics, similar to early shallow models. As more data became available, I incorporated more sophisticated techniques such as SVMs, neural networks, and CNN-inspired surrogate models.

The decision to exploit Function 5 in Week 6 parallels how modern CNNs refine learned representations rather than discarding them. Just as CNN breakthroughs came from building on strong intermediate results, my optimisation strategy improved by reinforcing and fine-tuning high-performing regions rather than restarting exploration.

3. Trade-offs: Depth, Overfitting, and Exploration vs Exploitation

CNN training involves balancing model depth, computational cost, and overfitting risks. I encountered similar trade-offs in the BBO challenge. While more complex models provided better representation of non-linear relationships, they also risked overfitting due to limited data.

This trade-off is closely related to the exploration–exploitation dilemma. In Week 6, I made a deliberate decision to shift toward exploitation for Function 5 because of its strong performance gain, while maintaining controlled exploration for the remaining functions where the response surface was still uncertain.

This selective strategy allowed me to:

Maximise gains where confidence is high (Function 5)

Continue learning in less stable regions (other functions)

4. Influence of CNN Concepts (Convolutions, Activations, Gradients)

Key CNN concepts shaped my optimisation thinking:

Convolutions encouraged me to consider relationships between neighbouring input variables rather than treating them independently

ReLU activations enabled modelling of non-linear patterns in the input space

Loss functions and gradients guided how the model adjusts predictions based on errors

Backpropagation played a crucial role in helping the model learn from accumulated data and refine predictions. This aligns with the decision to make incremental adjustments to Function 5, as gradients indicate that small changes near a high-performing region are more likely to yield further improvements.

5. Learning from Accumulated Data

With an expanded dataset from Weeks 1 to 5, the optimisation process became more informed and stable. The accumulation of data allowed clearer identification of high-performing regions and reduced uncertainty in predictions.

Function 5 served as a strong example of this learning process. The dramatic improvement in Week 5 suggested that the model had converged toward a promising region. In Week 6, I leveraged this by focusing on refinement rather than exploration, demonstrating how accumulated data can guide more confident optimisation decisions.

6. Real-World Deployment and Benchmarking Success

The discussion on real-world CNN deployment highlighted the importance of reliability, efficiency, and consistency. In practical applications, models are not judged solely by peak performance but by their ability to produce stable and repeatable results.

Applying this to my capstone, I defined success in Week 6 not just by achieving higher outputs but by:

Confirming the stability of high-performing regions (Function 5)

Maintaining consistent performance across other functions

Using a balanced optimisation strategy that adapts to different levels of uncertainty

This reflects real-world machine learning systems, where strategic refinement is often more valuable than continuous exploration.

Conclusion

Week 6 represents a more advanced and targeted optimisation approach influenced by CNN principles. By treating the optimisation process as a progressive learning system and strategically exploiting high-performing regions such as Function 5, I was able to refine my approach and improve decision-making. This balance between exploitation and exploration, guided by accumulated data and deep learning concepts, aligns closely with real-world AI optimisation practices.