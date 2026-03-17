import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# 1. Generate normally distributed data

mean = 70       
std_dev = 10    
size = 1000

data = np.random.normal(mean, std_dev, size)

# 2. Basic statistics

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

# 3. Histogram + KDE

sns.histplot(data, kde=True)
plt.title("Normal Distribution (Histogram + KDE)")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show() 

# 4. Plot theoretical normal curve

x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
y = norm.pdf(x, mean, std_dev)

plt.plot(x, y, color="red", linewidth=2)
plt.title("Theoretical Normal Distribution Curve")
plt.xlabel("Values")
plt.ylabel("Probability Density")
plt.show()

# 5. Empirical Rule Visualization

plt.figure(figsize=(8, 4))
sns.histplot(data, stat="density", color="lightblue")

plt.axvline(mean, color="black", linestyle="--", label="Mean")

plt.axvline(mean + std_dev, color="green", linestyle="--", label="±1std")
plt.axvline(mean - std_dev, color="green", linestyle="--")

plt.axvline(mean + 2*std_dev, color="orange", linestyle="--", label="±2std")
plt.axvline(mean - 2*std_dev, color="orange", linestyle="--")

plt.axvline(mean + 3*std_dev, color="red", linestyle="--", label="±3std")
plt.axvline(mean - 3*std_dev, color="red", linestyle="--")

plt.legend()
plt.title("68–95–99.7 Rule Visualization")
plt.show() 



# 6. Z-score example

""" mean = 70       
std_dev = 10
value = 85
z_score = (value - mean) / std_dev
print(f"Z-score for value {value}: {z_score}") """

car=pd.read_csv('Carseats.csv')
# print(car.info())

mn=np.mean(car['Income'])
sigma=np.std(car['Income'])
num_samples=car['Income'].count()

data=np.random.normal(mn,sigma,num_samples)
plt.hist(data,bins=10, density=True, alpha=0.7)

xmin,xmax=plt.xlim()
x=np.linspace(xmin,xmax,num_samples)
p=norm.pdf(x,mn,sigma)
plt.plot(x,p,'r')
plt.show() 

mlen=car['Income']

mu, sigma=norm.fit(mlen)
plt.hist(mlen, bins=30, density=True, alpha=0.9, color='green')

xmin,xmax=plt.xlim()
x=np.linspace(xmin,xmax,100)
p=norm.pdf(x,mu,sigma)
plt.plot(x,p, 'r')
plt.show()

print("meean=",mu)
print("sigma=",sigma) 

from scipy.stats import zscore

mlen=car['Income']
print("zscore=",zscore(mlen)) 

from scipy import stats
mnlen=car['Income']
con_level=0.98
mean=np.mean(mnlen)
std_err=stats.sem(mnlen)
con_intervel=stats.norm.interval(con_level, loc=mean, scale=std_err)

plt.hist(mnlen, bins=10, color='hotpink', alpha=0.7)
plt.axvline(mean, color='red', linewidth=2, label="mean")
plt.axvline(con_intervel[0], color='blue', linestyle='dotted')
plt.axvline(con_intervel[1], color='blue', linestyle='dotted')
plt.legend()
plt.show() 