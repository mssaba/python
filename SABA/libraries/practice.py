import pandas as pd
import numpy as np

dict={'Name':['ravi','ram','ashok','mani','saba'],
      'Age':[30,35,40,22,23],
      'Degree':['B.COM','BSC','BBA','B.TECH','MBA'],
      'Score':[50,60,70,90,80]}
d=pd.DataFrame(dict)
print(d)

d.to_excel('file.xlsx',index=False)
d.to_csv('file1.csv',index=False)
print('File Saved')
d= pd.read_csv('file1.csv')
print(d)

import matplotlib.pyplot as pt
pt.plot(d.Name,d.Score,linestyle='-',linewidth=2,color='c')
pt.xlabel("name")
pt.ylabel('score')
pt.title ('line chart')
pt.show()

data=pd.read_csv('student-dataset.csv')
pt.plot(data.name,data.nationality,linestyle='-',linewidth='3',color='r')
pt.xlabel('Name')
pt.ylabel('Nationality')
pt.show()

