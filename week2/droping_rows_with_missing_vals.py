import pandas as pd
import numpy as np 
df=pd.DataFrame({'Age':[25,30,np.nan,40,35], 'Department': ['HR', 'Finance','Finance', np.nan, 'IT']})
print(df,"\n")
df_drop_rows=df.dropna()
print("DataSet after dropping rows with missing values:")
print(df_drop_rows)
