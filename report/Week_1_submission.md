# I can optimize it as far as possible from the portal view alone, but I should be clear: true optimization requires the previous data points and outputs for each function. Without those results, the best strategy is a well-spread exploration set that covers the search space better than using only midpoints.



Use these entries in the portal:



Function 1 (2-D)

0.211325-0.788675



Function 2 (2-D)

0.723607-0.276393



Function 3 (3-D)

0.166667-0.500000-0.833333



Function 4 (4-D)

0.125000-0.375000-0.625000-0.875000



Function 5 (4-D)

0.875000-0.625000-0.375000-0.125000



Function 6 (5-D)

0.150000-0.350000-0.550000-0.750000-0.950000



Function 7 (6-D)

0.900000-0.100000-0.700000-0.300000-0.500000-0.800000



Function 8 (8-D)

0.111111-0.222222-0.333333-0.444444-0.555555-0.666667-0.777778-0.888889



These are better than a simple all-0.5 approach because they:

avoid clustering in one part of the space,

sample both low, middle, and high regions,

create more diversity across dimensions,

reduce the risk of wasting a round on overly similar points.



Here is a full reflection you can paste into your discussion board:



For this round, my main strategy was exploration rather than exploitation. Since the task involves high-dimensional black-box functions and only limited information is available at each stage, I focused on selecting query points that spread across the search space instead of clustering around a single region. My reasoning was that in the early and middle stages of an optimisation problem, diverse sampling gives more useful information about the overall shape of the function, which can later support more targeted decisions.



To guide my choices, I used a space-filling approach. Rather than selecting the same midpoint repeatedly, I varied the values across dimensions so that each query point covered a different part of the possible input range. For lower-dimensional functions, this meant choosing complementary values that balanced low and high regions. For higher-dimensional functions, I used more structured spreads across dimensions to reduce the chance of redundancy. This approach was intended to improve the information gained from each submission and help identify promising regions for future rounds.



The most challenging functions to query were the higher-dimensional ones, especially Functions 7 and 8. As dimensionality increases, it becomes harder to judge whether a query point is informative because there are many more possible combinations of inputs. In two or three dimensions, it is easier to visualise gaps or patterns, but in six or eight dimensions, the search space becomes much larger and more uncertain. This made it difficult to balance broad exploration with the possibility of missing high-performing regions.



Additional information that would have helped includes a clearer record of previous query points and their outputs, along with some indication of uncertainty or local trends around strong-performing regions. Even a simple visual summary of which areas had already been explored would make it easier to avoid duplication and refine future decisions more effectively.



In future rounds, I plan to adjust my strategy based on the new data returned from this submission. If some regions produce stronger outputs, I will begin shifting toward exploitation by sampling nearby points to test whether those regions contain a local optimum. At the same time, I would still keep part of my strategy exploratory so that I do not overcommit too early to one area. Overall, my approach is to begin with diverse exploration, learn from the returned values, and then gradually combine exploration with more targeted optimisation as uncertainty reduces.



Also, in the portal, make sure there are:

no letters,

no spaces,

exactly the right number of values for each function,

every value written with 6 decimal places.

