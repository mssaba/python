# import pandas as pd
# import numpy as np 
# import matplotlib.pyplot as pt
# import seaborn as ss
# df=pd.read_csv('sample_dataset_1000.csv')

# print(df.info())
# # df_1=df.drop_duplicates()
# print(df.duplicated().sum())
# print(df.isnull().sum())
# print(df_1)
# # print(df_1)
# df_1.fillna(np.mean(df_1['Age']))
# print(df_1)
# numeric_cols = df_1.select_dtypes(include=["float64", "int64"]).columns
# for col in numeric_cols:
#     print(df_1[col].skew())

# pt.subplot(1,2,1)
# ss.histplot(df_1['Age'],kde=True)
# # pt.show()

# df_1['Age_log']=np.log1p(df_1['Age'])
# pt.subplot(1,2,2)
# ss.histplot(df_1['Age_log'],kde=True)
# pt.show()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.preprocessing import StandardScaler,MinMaxScaler
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split

# data={
#     "Age":[25,27,29,31,33,35,37,np.nan,np.nan,43],
#     "Name":['Ram','Raj','Ravi','Arun','Rajesh','Mani','Saba','Prem','Velu','Krish'],
#     "Salary":[50000, 60000, 65000, 70000, np.nan, 52000, 58000, 80000, 75000, 62000],
#     "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance", "IT", "HR", "Finance", "IT"]
# }

# df=pd.DataFrame(data)

# #info 
# print(df.info())
# print(df.isnull().sum())
# print(df.describe())

# df['Age']=df['Age'].fillna(df['Age'].mean())
# df['Salary']=df['Salary'].fillna(df['Salary'].mean())
# print(df['Salary'])
# e=LabelEncoder()
# df['encoded_dept']=e.fit_transform(df['Department'])
# print(df['encoded_dept'])

# for index,label in enumerate(e.classes_):
#     print(label,"->",index)


# s=StandardScaler()

# df[['Age_s','Salary_s']]=s.fit_transform(df[['Age','Salary']])

# print(df[['Age_s','Salary_s']])

# from scipy.stats import zscore
# df["Salary_Zscore"] = zscore(df["Salary"])

# print("\nZ-scores for Salary:\n")
# print(df[["Salary", "Salary_Zscore"]])

# outliers = df[np.abs(df["Salary_Zscore"]) > 3]

# print("\nDetected Outliers:\n")
# print(outliers)


# a=df[['Age_s','Salary_s','encoded_dept']]
# b=df['Salary']

# a_train,a_test,b_train,b_test=train_test_split(
#     a,b,
#     test_size=0.2,
#     random_state=42
# )
# print("\nTraining Set Size:", a_train.shape)
# print("Testing Set Size:", a_test.shape)



# plt.hist(df["Salary"], bins=5)
# plt.title("Salary Distribution")
# plt.xlabel("Salary")
# plt.ylabel("Frequency")
# plt.show()

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

""" data=pd.read_csv("Dataset\BreastCancer.csv")

df=data.ffill()
df1=df.copy()

x=df1.drop("Class",axis=1)
y=df1['Class']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
g=GaussianNB()
g.fit(x_train,y_train)
pre=g.predict(x_test)

a=accuracy_score(y_test,pre)
print(a)

test={
    "Id":1,
    "Cl.thickness":20.00,
    "Cell.size":56,
    "Cell.shape":200,
    "Marg.adhesion":58,
    "Epith.c.size":145,
    "Bare.nuclei":20.5,
    "Bl.cromatin":89,
    "Normal.nucleoli":40.00,
    "Mitoses":0,
 
}
e=pd.DataFrame([test])
p=g.predict(e)
print(p)
 """

""" a=pd.read_csv('Dataset\Carseats.csv')
b=a.copy()
l=LabelEncoder()
b["ShelveLoc"]=l.fit_transform(b['ShelveLoc'])
b["Urban"]=l.fit_transform(b['Urban'])
b["US"]=l.fit_transform(b['US'])

x=b.drop('Income',axis=1)
y=b['Income']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
li=LinearRegression()
li.fit(x_train,y_train)

pre=li.predict(x_test)
print(mean_squared_error(y_test,pre))

test={
    "Sales":100,
    "CompPrice":20.5,
    "Advertising":10,
    "Population":70.45,
    "Price":250,
    "ShelveLoc":1,
    "Age":25,
    "Education":0,
    "Urban":89,
    "US":45
}

df=pd.DataFrame([test])
pr=li.predict(df)
print(pr) """

