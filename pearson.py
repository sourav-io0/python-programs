# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 22:54:42 2026

@author: soura
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data={
      "Math":[78,85,96,80,86],
      "Science":[88,90,94,82,89],
      "English":[72,75,78,70,74]
      }
df=pd.DataFrame(data)
correlation=df["Math"].corr(df["Science"])
print(f"The correlation between Math and Science is {correlation:.4f}")

plt.figure(figsize=(8,6))
corr_matrix=df.corr()
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',fmt='.2f')
plt.title('Pearson Correlation Heatmap')
plt.show()
