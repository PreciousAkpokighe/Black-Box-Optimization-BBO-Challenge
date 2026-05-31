Model Name
Hybrid Bayesian Optimization Framework for Black-Box Optimisation
Version 1.0
Overview
This model combines:
•	Gaussian Process Regression (GPR)
•	Bayesian Optimization
•	Random Forest Feature Importance
•	SVM-based Exploration
•	Neural Network Concepts
•	Explainable AI Techniques
The objective is to identify high-performing regions of unknown functions while balancing exploration and exploitation.
Intended Use
Suitable Uses
•	Black-box optimisation
•	Experimental design
•	Hyperparameter tuning
•	Educational demonstrations
•	Surrogate modelling
Unsuitable Uses
•	Medical diagnosis
•	Credit approval
•	Criminal justice decisions
•	Autonomous safety-critical systems
Model Details
Weeks 1–2
Exploratory sampling using space-filling inputs.
Weeks 3–4
Introduced Support Vector Machine concepts to identify potential high-performance regions.
Weeks 5–6
Applied Neural Network principles including:
•	SGD
•	Backpropagation
•	Feature interactions
Weeks 7–8
Implemented Bayesian Optimization using:
•	Gaussian Processes
•	Expected Improvement
Weeks 9–10
Added transparency and interpretability through:
•	Feature importance analysis
•	Sensitivity analysis
•	Decision tracking
•	Explainable optimisation
Performance Summary
Function	General Trend
Function 1	Near zero
Function 2	Moderate positive
Function 3	Slight negative
Function 4	Negative but improving
Function 5	Strong positive growth
Function 6	Negative but stabilising
Function 7	Positive growth
Function 8	Consistent positive
Notable Result
Function 5 improved from approximately:
60 → 1700+
through iterative exploitation of high-performing regions.
Assumptions
The model assumes:
1.	Nearby points produce similar outputs.
2.	The underlying function remains stationary.
3.	Historical observations are informative.
4.	Gaussian Process uncertainty estimates are meaningful.
Limitations
Small Dataset
Only a limited number of observations are available for each function.
Local Optima Risk
The optimisation process may become trapped in local optima.
Sampling Bias
Function 5 received more exploitation due to strong performance.
Black-Box Constraints
True mathematical relationships remain unknown.
Ethical Considerations
Transparency is essential because optimisation decisions influence future search directions.
To support reproducibility:
•	All code is documented.
•	Historical inputs and outputs are retained.
•	Query decisions are justified.
•	GitHub tracks model evolution.
This approach improves trustworthiness and allows other researchers to reproduce and evaluate the optimisation process.
Future Improvements
Future versions may include:
•	SHAP explanations
•	XGBoost surrogate models
•	Ensemble Bayesian optimisation
•	Deep Gaussian Processes
•	Multi-objective optimisation
•	Active learning techniques


