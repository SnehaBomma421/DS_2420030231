import pandas as pd
import numpy as np

df = pd.read_csv("C:/cllg/3-1/DS/LABS/week3/Iris (3).csv")

print(df.corr(method='pearson', numeric_only='float'))
print(df.corr(method='spearman', numeric_only='float'))