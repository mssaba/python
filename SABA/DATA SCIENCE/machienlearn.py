#GaussianNB
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# c=pd.read_csv('Company_Data.csv')
# c_copy=c.copy()
l=LabelEncoder()
# c_copy['ShelveLoc']=l.fit_transform(c_copy['ShelveLoc'])
# c_copy['Urban']=l.fit_transform(c_copy['Urban'])
# c_copy['US']=l.fit_transform(c_copy['US'])

# x=c_copy.drop(['US'],axis=1)
# y=c_copy['US']

# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
# gb=GaussianNB()
# gb.fit(x_train,y_train)
# y_preb=gb.predict(x_test)
# # print(y_preb)

# a=accuracy_score(y_test,y_preb)
# print("Accuray:",a)

# test={
#     "Sales": 8.79,
#     "CompPrice": 132.0,
#     "Income": 38.0,
#     "Advertising": 19.0,
#     "Population": 420.0,
#     "Price": 130.0,
#     "ShelveLoc": 0,
#     "Age": 40.0,
#     "Education": 67.0,
#     "Urban": 3,
# }

# df=pd.DataFrame([test])
# pre=gb.predict(df)
# print(pre[0])

#RandomForestClassifier
# from sklearn.ensemble import RandomForestClassifier

# d=pd.read_csv('College.csv')
# c=d.copy()
# c['Private']=l.fit_transform(c['Private'])

# x=c.drop(['Private'],axis=1)
# y=c['Private']

# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# r=RandomForestClassifier()
# r.fit(x_train,y_train)
# y_pre=r.predict(x_test)

# a=accuracy_score(y_test,y_pre)
# print("Accuracy:",a)

# f={
#     "Apps": 1000,
#     "Accept": 500,
#     "Enroll": 200,
#     "Top10perc": 50,
#     "Top25perc": 75,
#     "F.Undergrad": 1500,
#     "P.Undergrad": 200,
#     "Outstate": 20000,
#     "Room.Board": 5000,
#     "Books": 500,
#     "Personal": 2000,
#     "PhD": 80,
#     "Terminal": 70,
#     "S.F.Ratio": 10.0,
#     "perc.alumni": 20.0,
#     "Expend": 10000,
#     "Grad.Rate": 90.0
# }

# df=pd.DataFrame([f])
# pred=r.predict(df)
# print(pred)

""" from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

h=pd.read_csv("honey.csv")
v=h.copy()
x=v.drop(['priceperlb','state'],axis=1)
y=v['priceperlb']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
l=LinearRegression()
l.fit(x_train,y_train)

pre=l.predict(x_test)
print(mean_squared_error(y_test,pre)) """

#UNSUPERVISED LEARNING 
#KMEANS
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as pt

# a=pd.read_csv("Dataset\Admission.csv")
# ad=a.drop(['Serial No.'],axis=1)

s=StandardScaler()
# s.fit_transform(ad)

# k=KMeans(n_clusters=2,random_state=42)
# ad['k_cluster']=k.fit_predict(ad)
# print(ad)
# pt.scatter(ad['GRE Score'],ad['CGPA'],c=ad['k_cluster'],cmap='Set1',s=100,edgecolor='k')
# pt.show()

""" bc=pd.read_csv('Dataset\BreastCancer.csv')
bc.dropna(inplace=True)
bcc=bc.drop(['Id'],axis=1)
scalar=StandardScaler()
scalar.fit_transform(bcc)

kmean=KMeans(n_clusters=2,random_state=42)
bcc['cluster']=kmean.fit_predict(bcc)
print(bcc)

pt.scatter(bcc['Cl.thickness'],bcc['Cell.size'],c=bcc['cluster'],cmap='bone',s=150,edgecolor='k')
pt.show() """

from scipy.cluster.hierarchy import dendrogram,linkage,fcluster

i=pd.read_csv('Dataset\irisdataset.csv')
id=i.drop(['Class'],axis=1)
x=s.fit_transform(id)
l=linkage(x,method='ward')
dendrogram(l,orientation='top',distance_sort='descenting')
pt.show()