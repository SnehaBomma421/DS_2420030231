import pandas as pd
import numpy as np 
df=pd.DataFrame({'Age':[25,30,np.nan,40,35], 'Department': ['HR', 'Finance','Finance', np.nan, 'IT']})
print("Original DataSet (with missing values):")
print(df,"\n")
df_ffill=df.copy()
df_ffill.ffill(inplace=True)
print("DataSet after Forward Fill:")
print(df_ffill)

#backward fill
df_bfill=df.copy()  
df_bfill.bfill(inplace=True)
print("DataSet after Backward Fill:")
print(df_bfill)