import matplotlib.pyplot as pt
import pandas as pd
import numpy as np
# import seaborn as ss
# ss.set(style='darkgrid')
# pt.rcParams['figure.figsize']=(7,4)
df=pd.read_csv('amazon_sales_dataset.csv')
# pt.plot(df.model,df.hp,linestyle='-',linewidth=2,color='c')
# pt.xlabel('Model')
# pt.ylabel('HP')
# pt.title("EDA")
# pt.show()
# df['vs'].fillna(df['hp'].mean())
# ss.scatterplot(x='model',y='vs',data=df)

# pt.show()

# print(df.info())

# pt.bar(df.model[0:5],df.cyl[0:5],label='c',width=0.5)
# pt.xlabel('MODEL')
# pt.ylabel('CYL')
# pt.title('BAR PLOT B/W CAR MODEL AND CYILINDER')
# pt.show()

# pt.figure(figsize=(10,5))
# pt.hist(df.model[0:5],bins=20,color='r',edgecolor='black')
# pt.xlabel("MODEL")
# pt.title('Hist Plot of Car Models')
# pt.show()

# pt.pie(df.gear[0:4],labels=df.model[0:4],autopct="%1.1f%%",colors=['black','blue','yellow','red','green'])
# pt.title('PIE CHART OF CAR ')
# pt.show()

# pt.scatter(df.model[0:10],df.drat[0:10],marker='o',label='Data Points',color='k')
# pt.xlabel('MODEL')
# pt.ylabel('DRAT')
# pt.show()

# g, axes = pt.subplots(2, 2, figsize=(10, 8))

# axes[0, 0].pie(df.gear[0:4],labels=df.model[0:4],autopct="%1.1f%%",colors=['black','blue','yellow','red','green'])
# axes[0, 0].set_title('pie Plot')

# axes[0, 1].scatter(df.model[0:10],df.drat[0:10],marker='o',label='Data Points',color='k')
# axes[0, 1].set_title('Scatter Plot')

# axes[1, 0].bar(df.model[0:5],df.cyl[0:5],label='c',width=0.5)
# axes[1, 0].set_title('Bar Chart')

# axes[1, 1].hist(df.model[0:5],bins=20,color='r',edgecolor='black')
# axes[1, 1].set_title('Histogram')

# pt.tight_layout()
# pt.show()
df.drop(['order_id','product_id','quantity_sold','rating','review_count','order_date','customer_region','payment_method'],axis=1,inplace=True)
# print(df)

a=df.columns

r=[]
b=[]

for x in a:
    
    if df[x].dtype == 'object':
        r.append(x)
    else:
        b.append(x)
# print(r)
# print(b)

for i  in r:
    for y in b:
        pt.bar(df[i].head(6),df[y].head(6),color=['r','k','b','g','c']) 
        pt.show()