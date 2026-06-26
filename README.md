Black-Box Optimisation (BBO) Capstone Project
## Project Documentation


- [Dataset Datasheet](DATASHEET_NEW.md)
- [Model Card](MODEL_CARD_NEW.md)

Project Overview

This repository contains my submission for the Black-Box Optimization (BBO) Challenge completed as part of the Machine Learning and Artificial Intelligence Professional Certificate programme.

The objective of the challenge is to optimize eight unknown black-box functions through iterative query submissions while operating under strict information constraints. At each stage, only input-output observations are available, requiring the development of increasingly sophisticated optimization strategies to identify high-performing regions of the search space.

Over twelve rounds of experimentation, this project evolved from basic exploratory sampling into a structured optimization framework incorporating machine learning, deep learning, clustering, Bayesian optimization, and dimensionality reduction techniques.

Problem Statement

The challenge consists of optimizing eight hidden objective functions ranging from 2-dimensional to 6-dimensional search spaces.

For each iteration:

* New query points are submitted.
* Function outputs are returned.
* Historical observations are accumulated.
* Optimization strategies are refined.
* Future queries are generated using insights learned from prior rounds.

Since the analytical form of the functions is unknown, all optimization decisions must be made using observed data only.

Optimization Strategy Evolution

Week 1 – Baseline Exploration

* Uniform search space sampling
* Initial performance assessment
* Identification of promising and poor-performing regions

Week 2 – Bayesian Optimization

* Surrogate modelling
* Exploration vs exploitation balancing
* Candidate point generation

Week 3 – Support Vector Machine (SVM)

* Classification of high-performing and low-performing regions
* Decision boundary analysis
* Targeted query refinement

Week 4 – Neural Networks

* Feedforward neural network surrogate model
* Stochastic Gradient Descent (SGD)
* Backpropagation learning

Week 5 – Deep Learning Enhancement

* Multi-layer neural architecture
* Improved nonlinear pattern detection
* Local search refinement

Week 6 – CNN-Inspired Optimization

* Feature hierarchy concepts
* Progressive pattern extraction
* Structured exploration of promising regions

Week 7 – Bayesian Hyperparameter Optimization

* Hyperparameter tuning
* Model configuration optimization
* Improved search efficiency

Week 8 – Scaling and Emergence

* Larger candidate search spaces
* Emergent performance pattern analysis
* Search diversification

Week 9 – Transparency and Interpretability

* Explainable optimization decisions
* Feature importance analysis
* Strategy justification

Week 10 – Model Cards and Datasheets

* Reproducibility documentation
* Strategy transparency
* Optimization governance

Week 11 – Clustering-Based Optimization

* K-Means clustering
* Cluster centroid exploration
* Density-based candidate selection
* Discovery of hidden performance patterns

Week 12 – PCA-Based Optimization

* Principal Component Analysis (PCA)
* Variance-driven search
* Redundancy reduction
* Efficient dimensionality management


Methodologies Applied

Machine Learning

* Support Vector Machines (SVM)
* Random Forest Regression
* Gradient Boosting
* Gaussian Process Regression

Deep Learning

* Feedforward Neural Networks
* Stochastic Gradient Descent
* Backpropagation
* CNN-inspired feature extraction

Optimization

* Bayesian Optimization
* Exploitation vs Exploration balancing
* Hyperparameter tuning
* Surrogate modelling

Unsupervised Learning

* K-Means Clustering
* PCA
* Cluster-based sampling


Repository Structure

├── README.md
├── Week 1
│   ├── Inputs
│   ├── Outputs
│   └── Reflection
├── Week 2
│   ├── Bayesian Optimization
├── Week 3
│   ├── SVM Optimizer
├── Week 4
│   ├── Neural Network Model
├── Week 5
│   ├── Deep Learning Strategy
├── Week 6
│   ├── CNN-Inspired Optimization
├── Week 7
│   ├── Bayesian Hyperparameter Tuning
├── Week 8
│   ├── Scaling and Emergence
├── Week 9
│   ├── Explainable Optimization
├── Week 10
│   ├── Datasheet
│   ├── Model Card
├── Week 11
│   ├── Clustering Optimization
├── Week 12
│   ├── PCA Optimization
└── References


Results and Key Findings

Successful Functions

Several functions demonstrated consistent improvement through exploitation of high-performing regions:

* Function 5 showed the strongest and most stable positive trend.
* Functions 7 and 8 benefited from clustering-based refinement.
* Local search strategies frequently outperformed global exploration.

Challenging Functions

Functions 3, 4, and 6 remained difficult to optimize due to:

* Complex response surfaces
* Sparse high-performing regions
* Greater sensitivity to local optima

These functions required continued exploration alongside exploitation strategies.


Lessons Learned

This project demonstrated that:

1. Optimization performance improves significantly when exploration is gradually replaced by informed exploitation.
2. Surrogate models become more effective as additional observations are collected.
3. Clustering and PCA can reveal hidden structure within search spaces.
4. Explainability and documentation are as important as raw optimization performance.
5. No single optimization method performs best across all functions.


Technologies Used

* Python
* NumPy
* Pandas
* Scikit-Learn
* TensorFlow
* PyTorch
* Matplotlib
* Jupyter Notebook


References

Bishop, C.M. (2006). Pattern Recognition and Machine Learning. Springer.

Goodfellow, I., Bengio, Y. and Courville, A. (2016). Deep Learning. MIT Press.

Jolliffe, I.T. and Cadima, J. (2016). Principal Component Analysis: A Review and Recent Developments. Philosophical Transactions of the Royal Society A.

Snoek, J., Larochelle, H. and Adams, R.P. (2012). Practical Bayesian Optimization of Machine Learning Algorithms. NeurIPS.

Shahriari, B., Swersky, K., Wang, Z., Adams, R.P. and De Freitas, N. (2016). Taking the Human Out of the Loop: A Review of Bayesian Optimization. Proceedings of the IEEE.


Author

Precious Otas Akpokighe
Machine Learning & Artificial Intelligence Professional Certificate Candidate
Product Manager | Business Analyst | AI Enthusiast

GitHub: PreciousAkpokighe
