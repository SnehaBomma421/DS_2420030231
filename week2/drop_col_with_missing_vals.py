import pandas as pd
import numpy as np 
df=pd.DataFrame({'Age':[25,30,np.nan,40,35], 'Department': ['HR', 'Finance','Finance', np.nan, 'IT']})
print(df,"\n")
df_drop_col=df.dropna(axis=1)
print("DataSet after dropping columns with missing values:")
print(df_drop_col)