import pandas as pd
import numpy as np

d=np.array(['a','e','f','r','t'])
s=pd.Series(d) #converting array to series
print(s)

#using linespace
dt=np.linspace(1,10,5)
f=pd.Series(dt)
print(f)
 
#using range
da=pd.Series( range(2,10))
print(da)

#index changing
ser=pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
print(ser)


dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

df = pd.DataFrame(dict)
#see all data frame
print(df)

#only a column
a=df['degree']
print(a)

#accesing row using index
row=df.iloc[1]
print(row)

#accesing more than one row
e=df.loc[0:2,['name','degree']]
print(e)

#filtering
f=df[df['score']>40]
print(f)

#accessing particular row 
ss=df.at[1,'degree']
print(ss)

#selecting two column
w=df[['name','degree']]
print(w)

#declare a list as new column
age=['25','32','56','58']
df['Age']=age
print(df)
#reading
df.to_excel('example.xlsx',index=False)
df.to_csv('example.csv', index=False)
print("file saved") 
df = pd.read_csv('example.csv')
print("\nRead CSV:")
print(df)

new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,
                        'Position':'PG', 'Age':33, 'Height':'6-2',
                        'Weight':189, 'College':'MIT', 'Salary':99999},
                                                            index =[0])
# simply concatenate both dataframes
ds = pd.concat([ df,new_row]).reset_index(drop = True)
ds.head(5)
print(ds)

s=ds.drop(['Name'],axis=1)
print(s)

row2 = ds.iloc[[3, 4], [1, 2]]
print(row2)

import scipy.stats as st
ds.fillna(st.mode(ds),inplace=True)
ds.fillna(method="ffill")
ds.ffill()
print(ds)


