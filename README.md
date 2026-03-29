# Black-Box-Optimization-BBO-Challenge: the structured BBO challenge
Capstone project for Ml/AI Professional Certificate

**What is this challenge about?**
This capstone project mimics a Bayesian optimisation-style competition, 
in which i will try to find the maximum of eight unknown functions, 
also known as black-box functions. I won't have the equations or visuals
of these functions up front – just some initial data and the ability to make smart guesses.
Each function simulates a real-world task such as radiation detection, robot control or drug discovery, 
where evaluations are expensive or limited. Perfect solutions are not expected. I am 
encouraged to demonstrate a sound trial-and-error process throughout this project.

**What will you do?**
I’ll be working with eight synthetic black-box functions. These are unknown mathematical functions 
that accept inputs and return a single output. The goal is to find the inputs that give the highest 
possible output for each function.
Every function is a maximisation problem. I won't see the internal workings of the functions, 
but I’ll be able to observe how they respond to different inputs.

**What if I don't find the best result?** 
That's okay! In real-world ML, most progress is made not through perfect solutions but through 
thoughtful iteration and practical reasoning.
Weekly , for the next 10 weeks or so, i'll submit my query and complete the required reflection.

**What techniques can I use?**
I am free to use any ML method to decide what input to query next. Here are some examples:
Random search using np.random.uniform
Grid search to evaluate points on a grid, such as 10,000 points
Bayesian optimisation using a GP and acquisition functions such as UCB
Manual reasoning using scatter plots or your own insight to pick the next best point
Custom surrogate models to train an ML model to predict  and guide your query

**A note on what's NOT required**
Write and submit an optimiser
Build a full optimisation model from scratch
Find the perfect global maximum for every function
The task is to work with limited data, make smart decisions and reflect on the approach as it goes.

**Summary**

I am maximising eight unknown functions, one query per function per week.

I choose the ML method, such as random, grid, Bayesian optimisation or manual.

I submit my inputs in a precise format via the capstone project portal.

I reflect, revise and iterate over several rounds.

Success isn't just the highest value – it’s showing thoughtful, data-driven decision-making in my reflection.
