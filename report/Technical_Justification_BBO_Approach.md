# Technical Justification for BBO Approach

The main technical justification for my BBO approach is the use
of surrogate modelling to approximate unknown black-box functions. Since
the true functional form is unavailable, I relied on machine learning
models (SVMs and neural networks) to learn patterns from historical
input-output data and guide future query selection.

This approach is supported by established optimisation methods such
as Bayesian Optimisation, where surrogate models are used to balance
exploration and exploitation efficiently (Shahriari et al., 2016). In my
case, instead of relying solely on probabilistic models, I used SVM
classification and neural networks to approximate the response surface
and identify promising regions. This enabled a transition from random
exploration (Week 1) to data-driven optimisation (Weeks 3--6).

Relevant Academic Ideas and Techniques

My design was guided by several key machine learning concepts:

Support Vector Machines (SVMs): Used to classify high-performing vs
low-performing regions and identify decision boundaries in the input
space (Cortes and Vapnik, 1995).

Neural Networks (Backpropagation & SGD): Used to model non-linear
relationships and iteratively improve predictions (Rumelhart et al.,
1986; Bottou, 2010).

CNN-inspired feature learning: Applied in Week 6 by treating input
vectors as structured signals, allowing the model to capture
interactions between neighbouring variables (LeCun et al., 1998;
Krizhevsky et al., 2012).

Exploration vs Exploitation Trade-off: A core concept in optimisation,
guiding how I balanced searching new regions vs refining known
high-performing areas (Sutton and Barto, 2018).

These techniques strengthened the project by improving prediction
accuracy, generalisation, and optimisation efficiency.

Frameworks and Libraries Used

The main libraries used include:

PyTorch: For building neural networks, implementing backpropagation, and
experimenting with CNN-inspired architectures (Paszke et al., 2019).

Scikit-learn: For SVM modelling and classical machine learning
techniques (Pedregosa et al., 2011).

NumPy: For numerical computation and data manipulation (Harris et al.,
2020).

These frameworks were selected due to their flexibility, scalability,
and strong support within the machine learning community. PyTorch, in
particular, enables rapid prototyping and experimentation, which is
critical in iterative optimisation tasks.

Documentation and Presentation Strategy (GitHub)

To ensure clarity and reproducibility, my GitHub repository is
structured to separate:

Input/output datasets (Weeks 1--6)

Jupyter notebooks for each modelling stage

Weekly reflections

A central README explaining the overall approach

To further strengthen documentation, I plan to:

Add a methodology section outlining model evolution (Random → SVM →
Neural Network → CNN-inspired)

Include detailed code comments and explanations

Provide a summary of results and insights per function

This aligns with best practices in reproducible research and
collaborative software development (Wilson et al., 2014).

Future Improvements and Additional Sources

To refine my approach further, I would explore:

Bayesian Optimisation with Gaussian Processes for uncertainty-aware
optimisation (Rasmussen and Williams, 2006)

Advanced neural architectures such as attention mechanisms (Vaswani et
al., 2017)

Benchmark datasets and optimisation competitions (e.g., Kaggle)

These would enhance both the theoretical grounding and practical
performance of the model.

References

Bottou, L. (2010) 'Large-scale machine learning with stochastic gradient
descent', Proceedings of COMPSTAT, pp. 177--186.

Cortes, C. and Vapnik, V. (1995) 'Support-vector networks', Machine
Learning, 20(3), pp. 273--297.

Harris, C.R. et al. (2020) 'Array programming with NumPy', Nature, 585,
pp. 357--362.

Krizhevsky, A., Sutskever, I. and Hinton, G.E. (2012) 'ImageNet
classification with deep convolutional neural networks', Advances in
Neural Information Processing Systems, 25.

LeCun, Y. et al. (1998) 'Gradient-based learning applied to document
recognition', Proceedings of the IEEE, 86(11), pp. 2278--2324.

Paszke, A. et al. (2019) 'PyTorch: An imperative style, high-performance
deep learning library', Advances in Neural Information Processing
Systems, 32.

Pedregosa, F. et al. (2011) 'Scikit-learn: Machine learning in
Python', Journal of Machine Learning Research, 12, pp. 2825--2830.

Rasmussen, C.E. and Williams, C.K.I. (2006) Gaussian Processes for
Machine Learning. MIT Press.

Rumelhart, D.E., Hinton, G.E. and Williams, R.J. (1986) 'Learning
representations by back-propagating errors', Nature, 323, pp. 533--536.

Shahriari, B. et al. (2016) 'Taking the human out of the loop: A review
of Bayesian optimization', Proceedings of the IEEE, 104(1),
pp. 148--175.

Sutton, R.S. and Barto, A.G. (2018) Reinforcement Learning: An
Introduction. 2nd edn. MIT Press.

Vaswani, A. et al. (2017) 'Attention is all you need', Advances in
Neural Information Processing Systems, 30.

Wilson, G. et al. (2014) 'Best practices for scientific computing', PLoS
Biology, 12(1).
