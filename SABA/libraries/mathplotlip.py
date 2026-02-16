import matplotlib.pyplot as pt
import numpy as np

#LINE PLOT

a=np.linspace(0,20,100)
b=np.cos(a)
pt.plot(a,b, label='Cos Wave',color='k',linestyle='-',linewidth=2)
pt.xlabel('X Axis')
pt.ylabel('Y Axis')
pt.title('Line Plot')
pt.legend()
pt.grid()
pt.show()

#SCATTER PLOT
e=np.random.rand(30)
f=np.random.rand(30)
pt.figure(figsize=(9,6))
pt.scatter(e,f,marker='o',label='Data Points',color='k')
pt.xlabel('X Axis')
pt.ylabel('Y Axis')
pt.title('SCATTER PLOT')
pt.legend()
pt.show()

#BAR CHART
c=['1','2','3','4']
v=[10,15,20,25]
pt.figure(figsize=(8,5))
pt.bar(c,v,color=['r','k','b','g'],label=c,width=0.5)
pt.xlabel('X Axis')
pt.ylabel('Y Axis')
pt.title('BAR CHART')
pt.show()

#HORIZONTAL BAR CHART
c=['1','2','3','4']
v=[10,15,20,25]
pt.figure(figsize=(8,5))
pt.barh(c,v,color=['r','k','b','g'],label=c)
pt.xlabel('X Axis')
pt.ylabel('Y Axis')
pt.title('BAR CHART')
pt.show()

# import seaborn as st
#HISTOGRAM
d=np.random.rand(100)
pt.figure(figsize=(8,5))
pt.hist(d,bins=20,color='r', edgecolor='black')
pt.xlabel('value')
pt.ylabel('frequency')
pt.title('Histogram')
pt.show()

#PIE CHART
p=['Happines','Problems','Depression','Good Things']
v=[1,50,40,9]
pt.figure(figsize=(8,5))
pt.pie(v,labels=p,autopct="%1.1f%%",colors=['black','blue','yellow','red'])
pt.title('PIE CHART OF SABA"S LIFE')
pt.show()

#BOX PLOT
dt= [np.random.randn(100), np.random.randn(100), np.random.randn(100)]
pt.figure(figsize=(8,5))
pt.boxplot(dt,patch_artist=True,label=['a','b','c'])
pt.title('BOX PLOT')
pt.show()

 # Violin Plot
pt.figure(figsize=(8, 5))
pt.violinplot(dt)
pt.title('Violin Plot')
pt.show()


# Stem Plot
pt.figure(figsize=(8, 5))
pt.stem(a, b, linefmt='b-', markerfmt='bo', basefmt='r-')
pt.title('Stem Plot')
pt.show()

#SUBPLOT FOR MULTIPLE GRAPH
g, axes = pt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(a, b, 'b')
axes[0, 0].set_title('Line Plot')

axes[0, 1].scatter(e, f, color='r')
axes[0, 1].set_title('Scatter Plot')

axes[1, 0].bar(c, v, color='g')
axes[1, 0].set_title('Bar Chart')

axes[1, 1].hist(d, bins=20, color='c')
axes[1, 1].set_title('Histogram')

pt.tight_layout()
pt.show()