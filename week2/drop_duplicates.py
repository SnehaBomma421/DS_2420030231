import pandas as pd
df=pd.DataFrame({'ID':[1,2,3,4,5],
                'Name':['Alice','Bob','Charlie','Alice','Eve'],
                'Age':[25,30,35,25,40],
                 })
print("Original DataSet (with duplicate values):")
print(df,"\n")
df_exact=df.drop_duplicates()
print("DataSet after removing exact duplicate values:")
print(df_exact)