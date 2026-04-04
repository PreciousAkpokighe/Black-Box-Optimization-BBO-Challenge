🚀 Black-Box Optimisation (BBO) Capstone Project

📌 Project Overview

This project focuses on optimising a set of unknown functions using a Black-Box Optimisation (BBO) approach. Since the mathematical form of the functions is not provided, optimisation is performed iteratively by selecting input values, observing outputs, and refining subsequent inputs based on performance.

The project demonstrates how optimisation can be achieved in real-world machine learning scenarios where the internal structure of a system is unknown or inaccessible.

🎯 Objective

The objective of this project is to maximise the output values of eight unknown functions by identifying optimal input vectors within a bounded domain [0,1]^n.

📊 Problem Setup
	•	Number of functions: 8
	•	Input domain: Continuous values between 0 and 1
	•	Input dimensions: Vary per function (2D to 8D)
	•	Output: Scalar value representing performance (fitness score)

Each function behaves as a black box, meaning:
	•	No gradients are available
	•	No functional form is known
	•	Only input-output pairs can be observed

🔄 Methodology

▶️ Week 1: Initial Exploration
	•	Inputs were selected using structured distributions across the domain.
	•	Purpose: broad exploration of the search space.
	•	Outcome: Established baseline performance for all functions.

▶️ Week 2: Guided Optimisation
	•	Inputs were adjusted based on Week 1 outputs.
	•	Strategy:
	•	Exploitation: refine high-performing inputs (e.g., Function 5)
	•	Exploration: move away from low-performing regions (e.g., Functions 4 and 6)
	•	Outcome: Improved understanding of promising vs poor regions.

▶️ Week 3: Comparative Refinement
	•	Compared Week 1 vs Week 2 outputs for each function.
	•	Strategy:
	•	If performance improved → continue in same direction
	•	If performance worsened → move back toward better region
	•	If performance unclear → explore new region
	•	Outcome: More targeted and efficient optimisation.

🧠 Machine Learning Concepts Applied

This project applies several core ML and optimisation principles:

🔹 Black-Box Optimisation

Optimisation without knowledge of the function structure, relying solely on observed outputs.

🔹 Exploration vs Exploitation
	•	Exploration: searching new regions
	•	Exploitation: refining known high-performing regions

Balancing both is critical for avoiding suboptimal solutions.

🔹 Gradient-Free Optimisation

Since gradients are unavailable, optimisation is performed using:
	•	Heuristic search
	•	Directional updates
	•	Iterative refinement

🔹 Iterative Learning

The optimisation process is sequential:
	1.	Submit inputs
	2.	Observe outputs
	3.	Update strategy
	4.	Repeat

Each iteration improves decision-making.

🔹 Fitness Evaluation

Outputs are treated as fitness scores:
	•	Higher values → better solutions
	•	Lower values → poor solutions

💻 Implementation

The optimisation strategy was implemented using:
	•	Python (Jupyter Notebook)
	•	NumPy for numerical operations

Example Logic Used

def generate_week3(w1, w2, y1, y2):
    diff = w2 - w1

    if y2 > y1:
        # Continue in same direction
        candidate = w2 + 0.6 * diff
    else:
        # Move back toward better region
        candidate = w2 - 0.7 * diff

    return np.clip(candidate, 0, 1)

📈 Key Insights
	•	Large variations in output values indicate non-linear and complex functions
	•	Small input changes can lead to significant output differences
	•	High-performing regions are often localised, requiring careful refinement
	•	Poor regions must be actively avoided through exploration

⚠️ Limitations
	•	Limited number of iterations restricts full convergence
	•	No visibility into function structure limits model-based optimisation
	•	Possible presence of local optima

🚀 Future Improvements
	•	Implement Bayesian Optimisation for smarter sampling
	•	Use surrogate models (e.g., Gaussian Processes)
	•	Increase number of iterations for better convergence
	•	Visualise search space for better interpretability

🧾 Conclusion

This project demonstrates how effective optimisation can be achieved without explicit knowledge of a system’s internal structure. By leveraging iterative learning, performance feedback, and a balance of exploration and exploitation, it is possible to progressively identify high-performing solutions.
