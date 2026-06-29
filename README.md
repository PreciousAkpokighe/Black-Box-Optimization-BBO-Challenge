Black-Box Optimisation (BBO) Capstone Project
## Project Documentation


- [Dataset Datasheet](docs/DATASHEET_NEW.md)
- [Model Card](docs/MODEL%20CARD_NEW.md)
# BLACK-BOX OPTIMIZATION (BBO) CAPSTONE PROJECT

## Non-Technical Explanation of the Project

This project explores how Artificial Intelligence can solve complex optimisation problems when the mathematical formula of the problem is unknown. Instead of knowing exactly how each function works, the model learns from previous attempts by observing which inputs produced better results. Over thirteen weeks, different machine learning and optimisation techniques were progressively introduced to improve decision-making and identify better solutions. The project demonstrates how AI systems can efficiently search for optimal solutions while balancing exploration of new possibilities with exploitation of previously successful regions. It provides practical experience in optimisation under uncertainty and illustrates how modern machine learning techniques can support real-world decision-making where complete information is unavailable.

## Data

The dataset consists of historical query inputs and corresponding objective function outputs collected over thirteen iterative rounds of the Imperial College London Black-Box Optimisation Capstone Project.

Each weekly submission generated:

- Eight optimisation queries (Functions 1–8)
- Corresponding objective function evaluations
- Historical optimisation trajectories
- Performance observations across multiple optimisation strategies

Rather than relying on an external dataset, the project progressively built its own optimisation history. Each new submission incorporated all previously observed inputs and outputs to refine future query selection.

**Data Source**

- Imperial College London – Professional Certificate in Machine Learning and Artificial Intelligence (Emeritus)
- Black-Box Optimisation Capstone Portal
- Weeks 1–13 Query History

## Model

The optimisation framework evolved throughout the project rather than relying on a single model.

Techniques progressively incorporated included:

- Random Search (Baseline)
- Support Vector Regression (SVR)
- Neural Network Regression
- CNN-inspired optimisation concepts
- Bayesian Optimisation
- Ensemble Surrogate Modelling
- K-Means Clustering
- Principal Component Analysis (PCA)
- Reinforcement Learning concepts
  - Multi-Armed Bandits (MAB)
  - Q-Learning
  - Markov Decision Processes (MDPs)

The final optimisation strategy combined these approaches into a hybrid surrogate modelling framework capable of balancing local exploitation with global exploration while adapting to newly observed function evaluations.

## Hyperparameter Optimisation

Several optimisation strategies were investigated during the project to improve candidate selection while avoiding premature convergence.

The primary hyperparameters explored included:

- Exploration vs exploitation ratio
- Bayesian acquisition strategy
- Local search radius
- Cluster radius
- Number of optimisation candidates
- Ensemble weighting
- PCA dimensionality reduction
- Candidate sampling strategy

Bayesian Optimisation was introduced to guide hyperparameter tuning more efficiently than manual trial-and-error. Clustering techniques were later used to identify promising regions within the search space, while PCA reduced redundancy by preserving only the most informative patterns. During the final iteration, Reinforcement Learning concepts informed adaptive decision-making by balancing exploitation of historically successful regions with continued exploration of uncertain areas.

## Results

Across thirteen optimisation rounds, the optimisation strategy became progressively more structured and data-driven.

Major outcomes included:

- Successfully completed all thirteen optimisation rounds.
- Built increasingly accurate surrogate models from historical observations.
- Improved optimisation efficiency using Bayesian Optimisation.
- Applied clustering to identify promising search regions.
- Used PCA to simplify optimisation while preserving informative variance.
- Incorporated Reinforcement Learning concepts to improve sequential decision-making.
- Produced comprehensive project documentation including a Datasheet, Model Card and GitHub repository.

Performance varied across the eight objective functions. Some functions, particularly Function 5, responded well to exploitation-based strategies, while Functions 3, 4 and 6 remained challenging due to their complex response surfaces. These outcomes highlighted the importance of adaptive optimisation rather than relying on a single fixed search strategy.

Overall, the project demonstrated continuous improvement in optimisation methodology, technical implementation and reproducible machine learning practice.

## Repository Structure

```
Black-Box-Optimization-BBO-Challenge/

├── README.md
├── LICENSE
├── docs/
│   ├── DATASHEET.md
│   ├── MODEL_CARD.md
│   └── References.md
├── notebooks/
│   ├── Week01.ipynb
│   ├── ...
│   └── Week13_Final.ipynb
├── data/
│   ├── Inputs/
│   └── Outputs/
└── reports/
    ├── Weekly Reflections
    └── Final Reflection
```

## Technologies Used

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Scikit-learn
- PyTorch
- SciPy
- Matplotlib

## References

Brochu, E., Cora, V.M. & De Freitas, N. (2010) *A Tutorial on Bayesian Optimization of Expensive Cost Functions*. University of British Columbia.

Goodfellow, I., Bengio, Y. & Courville, A. (2016) *Deep Learning*. MIT Press.

Sutton, R.S. & Barto, A.G. (2018) *Reinforcement Learning: An Introduction*. 2nd ed. MIT Press.

Bishop, C.M. (2006) *Pattern Recognition and Machine Learning*. Springer.

Pedregosa, F. et al. (2011) 'Scikit-learn: Machine Learning in Python', *Journal of Machine Learning Research*, 12, pp. 2825–2830.

## Contact

**Precious Akpokighe**

Professional Certificate in Machine Learning & Artificial Intelligence

Imperial College London (via Emeritus)

GitHub: https://github.com/PreciousAkpokighe

LinkedIn: https://www.linkedin.com/in/precious-akpokighe-ceh

## License

This project is released under the MIT License.
