#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

week1_inputs = [
    np.array([0.211325, 0.788675]),
    np.array([0.723607, 0.276393]),
    np.array([0.166667, 0.5, 0.833333]),
    np.array([0.125, 0.375, 0.625, 0.875]),
    np.array([0.875, 0.625, 0.375, 0.125]),
    np.array([0.15, 0.35, 0.55, 0.75, 0.95]),
    np.array([0.9, 0.1, 0.7, 0.3, 0.5, 0.8]),
    np.array([0.111111, 0.222222, 0.333333, 0.444444, 0.555555, 0.666667, 0.777778, 0.888889])
]

week1_outputs = np.array([
    1.1327056288856873e-125,
    0.5675786892822564,
    -0.032385408076210126,
    -17.20744048260943,
    60.223125,
    -1.3287857969718009,
    0.34356041660314957,
    9.0501517903694
])


# In[2]:


for i, (x, y) in enumerate(zip(week1_inputs, week1_outputs), start=1):
    print(f"Function {i}")
    print("Input:", x)
    print("Output:", y)
    print("-" * 40)


# In[3]:


week2_inputs = [
    np.array([0.50, 0.50]),                                  # Function 1
    np.array([0.78, 0.22]),                                  # Function 2
    np.array([0.33, 0.50, 0.67]),                            # Function 3
    np.array([0.30, 0.45, 0.60, 0.75]),                      # Function 4
    np.array([0.85, 0.65, 0.35, 0.15]),                      # Function 5
    np.array([0.20, 0.40, 0.50, 0.70, 0.85]),                # Function 6
    np.array([0.75, 0.20, 0.60, 0.35, 0.45, 0.70]),          # Function 7
    np.array([0.15, 0.25, 0.35, 0.45, 0.60, 0.70, 0.80, 0.90]) # Function 8
]


# In[4]:


for i, x in enumerate(week2_inputs, start=1):
    print(f"Function {i} Week 2 Input: {x}")


# In[5]:


np.save("week2_inputs.npy", np.array(week2_inputs, dtype=object))
print("Saved successfully!")


# In[ ]:




