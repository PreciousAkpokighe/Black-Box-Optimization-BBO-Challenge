# What prompt patterns did you use (zero shot, few shot, etc.) and why? How was the prompt structuring different from simplifying the prompt?
 Rather than a random zero-shot exploration, I applied a structured “few-shot” optimization leveraging the knowledge from prior weeks. The following predictions are based on historical examples of output from weeks 1-7. Less structured exploration resulted in more randomness and weaker outputs for some functions, while structured optimisation yielded more stable and consistent query points.

What temperature, top-p, top-k and max-token settings did you use?    What was the impact of the coherence-diversity trade-off on your query of choice?
In principle, the optimization strategy that I used was like a low to moderate temperature, because I preferred solid high performance zones rather than a highly random exploration. Function 5 was treated with low diversity and high coherence in the strongest region. For the weaker functions, functions 7 and 8, I allowed for more diversity and exploration, to avoid getting stuck in bad local regions.

Is the behavior of the model affected by token boundaries or weird input strings? Have you noticed any limits on the number of tokens or output cut off? If there were no such cases, describe how you searched for such cases?
 The optimisation queries were always short and numerical in nature so no major token boundary or truncation issues were observed . I did check however that all the generated inputs were in the correct decimal format and within the boundary constraints of between 0 and 1. This prevented badly formed inputs and submission errors.

What kind of limits did you hit with 17 data points, for example prompt overfitting, attention focusing on irrelevant context, diminishing returns from longer inputs?  
As the dataset grew some functions began to have diminishing returns. More historical points sometimes led to increases in noise and to less sensitivity of the surrogate model to improvements that mattered. I also found that searching over all functions reduced the efficiency of optimisation, especially when there were strong regions in the search space, e.g. Function 5.

What strategies did you employ to reduce hallucinations? For example, did you use more restrictive instructions, retrieval of prior relevant information, or constrain output format?
I forced six decimal places and constrained all generated values to lie between 0 and 1. This resulted in reduced hallucination-like behavior. I also collected previous high performing query points from previous weeks, and generated new inputs around validated regions instead of completely random sampling. Bayesian optimisation further improved consistency, by basing its predictions on past evidence .

How will you scale your prompting and decoding strategies as we move to future rounds with larger data sets or more complex LLMs?
In later rounds I would scale up the optimization with adaptive exploration rates, automated hyperparameter tuning and ensemble surrogate models. I will also cluster the historical outputs into high and low performing regions and then generate new queries. For larger data sets I would remove unnecessary context to focus only on the most relevant historical points to increase computational efficiency.

How did you think about the design choices for prompts and decoding that helped you think like a practitioner trying to balance exploration, risk and computational constraints in a black box setting with incomplete information?
The design decisions got me thinking more strategically about optimization under uncertainty. Instead of random search I learned to balance between exploiting known good areas and exploring some unknown areas. This resonated with realities of ML practice where practitioners need to balance model performance, computational cost and risk, when knowledge about the underlying system is incomplete.

