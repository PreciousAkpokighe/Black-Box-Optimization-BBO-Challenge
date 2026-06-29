# Perfect — now that we can see Functions 6 & 7 outputs, we can refine your Week 2 strategy into a distinction-level approach 🔥



✅ Updated Week 1 Performance Ranking (ALL functions)



From your full screenshot:



🧠 Key Insight (what improves your marks)



Now your strategy becomes much stronger academically because:

You’re not just saying good vs bad

You are showing graded reasoning:

Excellent

Strong

Moderate

Poor

Very Poor



👉 This is exactly what assessors look for.



🎯 Refined Week 2 Strategy (High-Scoring Approach)



1.

Strong Exploitation (Top Performers)



👉 Focus: refine locally

Function 5 (excellent)

Function 8 (strong)



✔ Small adjustments only



2.

Controlled Exploitation (Moderate Performers)



👉 Focus: improve gradually

Function 2

Function 7



✔ Slight adjustments, but still close



3.

Exploration (Poor Performers)



👉 Focus: move away from weak regions

Function 1

Function 3



✔ Moderate change



4.

Aggressive Exploration (Very Poor Performers)



👉 Focus: completely new region

Function 6

Function 4



✔ Large change



🚀 Final Week 2 Input (Optimized & Justified)



Function 1 (Poor → Explore)



[0.65, 0.35]

➡ Move away from ineffective region



Function 2 (Moderate → Exploit)



[0.75, 0.25]

➡ Small refinement near good region



Function 3 (Poor → Explore)



[0.30, 0.55, 0.70]

➡ Shift pattern to test new region



Function 4 (Worst → Aggressive Explore)



[0.80, 0.60, 0.40, 0.20]

➡ Completely different structure



Function 5 (Best → Strong Exploit)



[0.85, 0.65, 0.35, 0.15]

➡ Stay very close to best-performing input



Function 6 (Very Poor → Aggressive Explore)



[0.90, 0.70, 0.50, 0.30, 0.10]

➡ Reverse + relocate search space



Function 7 (Moderate–Low → Controlled Exploit)



[0.88, 0.12, 0.72, 0.28, 0.52, 0.78]

➡ Slight tuning



Function 8 (Strong → Exploit)



[0.10, 0.24, 0.31, 0.46, 0.57, 0.64, 0.79, 0.86]

➡ Small perturbations around strong result



📊 Why THIS version is stronger than before



You are now demonstrating:



✅ 1. Ranking-based reasoning



Not just “good/bad” — but relative performance



✅ 2. Tiered decision-making



Different actions for:

Best

Moderate

Poor

Worst



✅ 3. True BBO thinking



You are:

exploiting high-value regions

exploring low-value regions

balancing both



📝 Distinction-Level Reflection (Use This)



The Week 2 input strategy was developed using a structured evaluation of Week 1 outputs. The outputs were ranked to identify high-performing and low-performing regions of the search space. Function 5 produced a significantly higher output than all others and was therefore treated as the most promising region, followed by Function 8 and Function 2. These functions were exploited through small perturbations of their input values to refine performance.



Functions with moderate outputs, such as Function 7, were adjusted slightly to improve results while maintaining proximity to known regions. In contrast, functions with near-zero or negative outputs (Functions 1 and 3) were explored by introducing moderate changes to their inputs. Functions with strongly negative outputs (Functions 4 and 6) were treated as poor-performing regions and were assigned significantly different input vectors to explore new areas of the search space.



This approach demonstrates a balance between exploration and exploitation, which is a fundamental principle in black-box optimisation. By adapting the magnitude of input changes based on observed performance, the strategy aims to efficiently converge towards optimal solutions despite the absence of explicit knowledge of the underlying functions.



🔥 If you want to go even higher (top 5%)



I can next:



✅ Turn this into a submission-ready report (with headings, Harvard tone)

✅ Create a Week 3 predictive strategy (ahead of your class)

✅ Or show you how to justify this using ML concepts (Bayesian / gradient-free optimisation)



Just tell me 👍

Great—this is exactly how you move your submission into distinction territory.

We’ll now justify your Week 2 strategy using proper ML / optimisation concepts (what assessors want to see).



🧠 1. Black-Box Optimisation (BBO) as an ML Problem



Your task fits into a core ML setting:



👉 We are optimizing an unknown function without access to its formula



This is formally called:

Black-Box Optimisation

A subset of Derivative-Free Optimisation



Mathematically:



\max_{x \in [0,1]^n} f(x)

You don’t know f(x)

You only observe outputs after trying inputs



👉 This is exactly like:

Hyperparameter tuning in ML

Reinforcement learning reward optimization



⚖️ 2. Exploration vs Exploitation (Core ML Principle)



Your Week 2 strategy is based on:



Exploitation

Use inputs close to high-performing points

Assumes local region is promising



Exploration

Try new regions

Avoid getting stuck in poor areas



How your decisions map to ML theory:



Academic justification:



This strategy reflects the exploration–exploitation trade-off, a fundamental concept in machine learning and optimisation, where decisions must balance refining known high-performing regions and investigating new areas to avoid local optima.



📈 3. Gradient-Free Optimisation (Why your method is valid)



In many ML problems:

We use gradients (e.g., gradient descent)



But here:



❌ No gradients available

❌ No function equation



So we use:



👉 Gradient-free methods



Examples:

Random search

Bayesian optimisation

Evolutionary algorithms



Your approach aligns with:



👉 Heuristic Search / Local Search

Small steps near good points → like hill climbing

Big jumps for bad points → like random restart



Academic justification:



Due to the absence of gradient information, a derivative-free optimisation approach was adopted. Local perturbations were applied to high-performing inputs, analogous to hill-climbing techniques, while larger shifts were introduced for poorly performing regions to enable broader search across the solution space.



🎯 4. Fitness Function Interpretation



In ML terms:



👉 Your output = fitness score

High value → good candidate solution

Low value → poor candidate



This is exactly how:

Genetic Algorithms

Reinforcement Learning rewards



work.



Mapping:



Academic justification:



The output values were treated as fitness scores, enabling the comparison of candidate solutions. Higher outputs indicated more optimal regions of the search space, guiding subsequent input selection.



🔁 5. Iterative Learning Process (VERY important)



Your process is:

Submit inputs

Observe outputs

Update strategy

Repeat



👉 This is:



Sequential Learning / Adaptive Optimisation



Used in:

Bayesian optimisation

Reinforcement learning

Active learning



Academic justification:



The optimisation process follows an iterative learning paradigm, where each round of evaluation informs subsequent decisions. This adaptive approach enables progressive refinement of inputs despite the absence of explicit knowledge of the objective function.



🧩 6. Local vs Global Search (Why your changes differ)



You applied:

Local search → small changes (Functions 5, 8)

Global search → large changes (Functions 4, 6)



ML connection:

Local search = exploitation

Global search = escaping local minima



Academic justification:



A combination of local and global search strategies was employed. Local search was used to refine high-performing regions, while global search was applied to escape low-performing areas and identify potentially better regions of the search space.



🧠 7. Optional (High Distinction Boost): Bayesian Thinking



Even though you didn’t formally use Bayesian optimisation, your logic resembles it:

You update beliefs about where good solutions are

You sample more near promising regions



Academic justification:



The strategy implicitly reflects principles of Bayesian optimisation, where prior observations inform future sampling decisions, concentrating evaluations in regions with higher expected performance.



🏁 Final Distinction-Level Justification (Use This)



You can paste this directly into your submission:



The Week 2 optimisation strategy was informed by key machine learning principles associated with black-box optimisation. Since the underlying functions are unknown and gradient information is unavailable, a derivative-free optimisation approach was adopted. The outputs from Week 1 were treated as fitness scores, enabling the ranking of candidate input solutions.



The strategy balances exploration and exploitation, a fundamental concept in optimisation and reinforcement learning. High-performing inputs, particularly for Functions 5 and 8, were refined through local perturbations to exploit promising regions of the search space. Moderately performing inputs were adjusted incrementally, while poorly performing inputs were modified more substantially to explore alternative regions.



This approach also reflects elements of local and global search, where local search is used to refine solutions and global search helps avoid convergence to suboptimal regions. Furthermore, the iterative nature of the process aligns with sequential learning paradigms, where each evaluation informs future decisions.



Overall, the strategy demonstrates a structured and adaptive optimisation process grounded in machine learning concepts, enabling efficient search despite the absence of explicit knowledge of the objective functions.



If you want next level 🔥



I can help you:



✅ Add Harvard references (to secure higher marks)

✅ Turn this into a full 1–2 page report section

✅ Or prepare your Week 3 optimisation strategy early



Just tell me 👍

