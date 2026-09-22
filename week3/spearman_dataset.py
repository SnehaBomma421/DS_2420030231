import pandas as pd
df=pd.read_csv("week3/Iris (3).csv")
print(df.corr(method='spearman',numeric_only=float))