import pandas as pd 

#load the data set 
df = pd.read_csv('retail_dashboards.csv', encoding='latin-1')

#how big is the dataset 
print("Shape: ", df.shape)

#What columns do we have 
print("\nColumns:", df.columns.tolist())

#print the first five rows
print("\nFirst 5 rows: ")
print(df.head())

#Any missing values
print("\nMising Values:")
print(df.isnull().sum())