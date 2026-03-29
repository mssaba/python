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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import train_test_split

data={
    "Age":[25,27,29,31,33,35,37,np.nan,np.nan,43],
    "Name":['Ram','Raj','Ravi','Arun','Rajesh','Mani','Saba','Prem','Velu','Krish'],
    "Salary":[50000, 60000, 65000, 70000, np.nan, 52000, 58000, 80000, 75000, 62000],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance", "IT", "HR", "Finance", "IT"]
}

df=pd.DataFrame(data)

#info 
print(df.info())
print(df.isnull().sum())
print(df.describe())