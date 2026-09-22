import pandas as pd
df=pd.DataFrame({'ID':[1,2,2,3,4,4,5],
                 'Name':['Alice','Bob','Bob','Charlie','David','David','David'],
                'Age':[25,30,30,35,40,40,40]})
print("Original DataSet (with duplicate values):")
print(df,"\n")
df_subset_id=df.drop_duplicates(subset=['ID'])
print("DataSet after removing duplicates based on 'ID':")
print(df_subset_id) 
df_subset_name=df.drop_duplicates(subset=['Name'])
print("DataSet after removing duplicates based on 'Name':")     
print(df_subset_name)