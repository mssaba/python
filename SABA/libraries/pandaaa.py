import pandas as pd
import numpy as np
# d=[1,2,3,4,5,6]
# a=pd.Series(d)
# print(a)
# b=pd.Series(d,index=['a','b','c','d','e','f'])
# print(b)
# print("Data type of Series:", b.dtype)
# print("Index of Series:",b.index)
# print("Values of Series:",b.values)
# print("Shape of Series:",b.shape)
# print("Number of dimensions of Series:", b.ndim)
# print("Size of Series:", b.size)
# print("Is Series empty?:", b.empty)

#creating data frame
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data_dict)
print("\nDataFrame:")
print(df)

# Reading & Writing Files
df.to_excel('example.xlsx',index=False)
df.to_csv('example.csv', index=False)
print("file saved") 
df = pd.read_csv('example.csv')
print("\nRead CSV:")
print(df)
# DataFrame Information
""" print("\nInfo:")
print(df.info())
print("\nDescription:")
print(df.describe())
print("\nColumns:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("Index:", df.index)
print("Values:")
print(df.values)
print("Shape:", df.shape)
print("Number of dimensions:", df.ndim)
print("Size:", df.size)
print("Is empty:", df.empty) """

# Selecting Data
print("\nSelecting Column:")
print(df['Name'])
print("\nSelecting Row:")
print(df.loc[1])
print("\nSelecting with Condition:")
print(df[df['Age'] > 30])
print("\nSelecting by Index:")
print(df.iloc[1]) 

# Adding a Column
df['Bonus'] = df['Salary'] * 0.10
print("\nUpdated DataFrame:")
print(df) 

# Deleting a Column
df.drop('Bonus', axis=1, inplace=True)
print("\nAfter Dropping Column:")
print(df)

df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})
print("Original DataFrame:")
print(df)

df = df.rename(columns={'A': 'aa'})
print("Modified DataFrame:")
print(df)

#handiling missing values
df.loc[2,'Age']=np.nan
df.fillna(np.mean(df['Age']))
print(df)
#to drop null value
print(df.dropna())

#sorting data
s=df.sort_values(by="B",ascending=False)
print(s)

#to delete duplicates
print(df.drop_duplicates())

#applying function
def hike(salary):
    return salary * 1.5
df['Hiked Salary']=df['B'].apply(hike)
print(df)

#renaming columns
df.rename(columns={'Age':'Years'},inplace=True)
print(df)

#reset index
r=df.reset_index()
print(r)

#set index
x=df.set_index('aa',inplace=True)
print(x)