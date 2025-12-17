import pandas as pd
df=pd.read_csv("task.csv")
print(df)
# print first five rows
print("First five rows:")
print(df.head())
#last five rows
print("Last five rows:")
print(df.tail())
#info about dataset
print("Dataset information:")
print(df.info())
#missing values
print("\nMissing values in each column:")
print(df.isnull().sum())