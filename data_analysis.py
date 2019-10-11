# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:54:25 2018

@author: Tom Mori
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

final_scores = []
valid_moves = []

for file in os.listdir("C:\\Users\\Tom Mori\\Documents\\2048_ML\\v3 Generations Data"):
    df = pd.read_csv("v3 Generations Data\\" + file)
    valid_moves.append(df[df['17'] == 1].shape[0])
    final_scores.append(np.array(df.tail(1)['2']))


plt.scatter(range(len(final_scores)), final_scores)
plt.xlabel('Generation')
plt.ylabel('final_score')
plt.show()

plt.scatter(range(len(valid_moves)), valid_moves)
plt.xlabel('Generation')
plt.ylabel('number of moves')
plt.show()

print(final_scores)
