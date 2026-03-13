# import random 
# import matplotlib.pyplot as pt 

# def t():
#     ht=random.randint(0,1)
#     if ht ==1:
#         return "Heads"
#     else:
#         return "Tails"

# def prob(n):
#     r={"Heads":0,"Tails":0}
#     for i in range(n):
#         r[t()]+=1
#     print("Heads:",r["Heads"])
#     print("Tails:",r["Tails"])

#     print("Heads Prob:",r["Heads"]/n)
#     print("Tails Prob:",r["Tails"]/n)

#     pt.bar(r.keys(),r.values(),color=['green','yellow'])
#     pt.show()

# prob(10)

# def fruitpick():
#     f=['apple','orange','grape']
#     p=random.randint(0,3)
#     if p==0:
#         return "apple"
#     elif p==1:
#         return "orange"
#     else:
#         return "grape"
    
    
# def pick(n):
#     r={'apple':0,'orange':0,'grape':0,}
#     for i in range(n):
#         r[fruitpick()]+=1
#     print(r['apple'])
#     print(r['orange'])
#     print(r['grape'])
  

#     print('prob:',r['apple']/n)
#     print('prob:',r['orange']/n)
#     print('prob:',r['grape']/n)
  

#     pt.bar(r.keys(),r.values(),color=['blue','green','red','yellow'])
#     pt.show()
# pick(100)


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# adult=pd.read_csv("adult.csv")

# total=adult["sex"].count()
# genders=adult.sex
# gender_count={"Male":0,"Female":0}
# for i in genders:
#     if (i=="Male"):
#         gender_count["Male"]+=1
#     else:
#         gender_count["Female"]+=1
# print("Male:",gender_count["Male"])
# print("Female:",gender_count["Female"])
# print("Male prob:",gender_count["Male"]/total)
# print("Female prob:",gender_count["Female"]/total)

# values=gender_count.keys()
# counts=gender_count.values()
# plt.bar(values,counts,color=["black","hotpink"])
# plt.show() 

# education=adult.education
# unique=education.unique()
# total=education.count()
# counts=education.value_counts()

# education_prob=[]
# x=0
# for i in counts:
#     i=i/total
#     education_prob.append(i)
#     print(unique[x],"prob=",i)
#     x+=1

# plt.bar(unique,education_prob)
# plt.xticks(rotation=45)
# plt.show()

# plt.plot(unique,education_prob,color="r",linewidth=2,marker="o",mfc="k")
# plt.xticks(rotation=45)
# plt.title("education probrbility chart")
# plt.ylabel("probebility counts")
# plt.show() 

# print("-------marital_status probebility-------")
# marital_status_labels=adult["marital-status"].unique()
# marital_status_counts=[]
# x=0
# for i in adult["marital-status"].value_counts():
#     i=i/adult["marital-status"].count()
#     marital_status_counts.append(i)
#     print(marital_status_labels[x],"prob=",i)
#     x+=1

# plt.plot(marital_status_labels,marital_status_counts,linewidth=3,color='g',marker='H',ms=7,mec='b',mfc='b')
# plt.xticks(rotation=45)
# plt.title("marital-status probebility chart")
# plt.xlabel("marital-status")
# plt.ylabel("probability counts")
# plt.show()

# print("")
# print("-------race probebility--------")
# race_labels=adult["race"].unique()
# race_counts=[]
# x=0
# for i in adult["race"].value_counts():
#     i=i/adult["race"].count()
#     race_counts.append(i)
#     print(race_labels[x],"prob=",i)
#     x+=1
# plt.plot(race_labels,race_counts,color='g',marker='P',ms=5,mec='y',mfc='y')
# plt.title("race probebolity chart")
# plt.xticks(rotation=10)
# plt.ylabel("probebility counts")
# plt.show()

# print("")
# print("-------relationship probebility-------")
# relationship_labels=adult["relationship"].unique()
# relationship_counts=[]
# x=0
# for i in adult["relationship"].value_counts():
#     i=i/adult["relationship"].count()
#     relationship_counts.append(i)
#     print(relationship_counts[x],"prob=",i)
#     x+=1

# plt.plot(relationship_labels,relationship_counts,marker='d',ms=8,mec='m',mfc='m')
# plt.title('relationship probebility chart')
# plt.xticks(rotation=45)
# plt.ylabel("probrbility counts")
# plt.show() 

# adult.dropna(subset=['occupation'],inplace=True)
# # adult["occupation"].dropna(inplace=True) 
# occupation_labels=adult["occupation"].unique()
# print(occupation_labels)
# occupation_counts=[]
# x=0
# for i in adult["occupation"].value_counts():
#     i=i/adult["occupation"].count()
#     occupation_counts.append(i)
#     print(occupation_labels[x],"prob=",i)
#     x+=1
# plt.plot(occupation_labels,occupation_counts,marker="D",ms=4,mfc='c',mec='c')
# plt.title("occupation probebility chart")
# plt.ylabel("probebility counts")
# plt.xticks(rotation=45)
# plt.show() 

#PMF,CDF,PDF

import numpy as np
import matplotlib.pyplot as pt
from scipy.stats import binom, norm

# 1. DISCRETE: Probability Mass Function (PMF)
# Use Case: Countable outcomes like coin flips or dice rolls.
n, p = 10, 0.5  # 10 flips, 50% chance of heads
x_discrete = np.arange(0, n + 1)
pmf_values = binom.pmf(x_discrete, n, p)


# 2. CONTINUOUS: Probability Density Function (PDF)
# Use Case: Measurable outcomes like height or temperature.
mu, sigma = 0, 1  # Standard Normal Distribution
x_cont = np.linspace(-4, 4, 100)
pdf_values = norm.pdf(x_cont, mu, sigma)

# 3. CUMULATIVE: Cumulative Distribution Function (CDF)
# Use Case: Probability that a value is LESS than or equal to X.
cdf_discrete = binom.cdf(x_discrete, n, p)
cdf_cont = norm.cdf(x_cont, mu, sigma)


# --- VISUALIZATION ---
fig, axes = pt.subplots(2, 2, figsize=(12, 10))

# Plot PMF (Discrete)
axes[0, 0].bar(x_discrete, pmf_values, color='skyblue', edgecolor='black')
axes[0, 0].set_title("PMF (Binomial: n=10, p=0.5)\nProbability of EXACTLY x successes")
axes[0, 0].set_ylabel("Probability")

# Plot PDF (Continuous)
axes[0, 1].plot(x_cont, pdf_values, color='salmon', lw=2)
axes[0, 1].fill_between(x_cont, pdf_values, alpha=0.2, color='salmon')
axes[0, 1].set_title("PDF (Normal: μ=0, σ=1)\nRelative likelihood of values")
axes[0, 1].set_ylabel("Density")

# Plot CDF (Discrete)
axes[1, 0].step(x_discrete, cdf_discrete, where='mid', color='blue')
axes[1, 0].set_title("CDF (Binomial)\nProbability of x OR FEWER successes")
axes[1, 0].set_ylabel("Cumulative Probability")

# Plot CDF (Continuous)
axes[1, 1].plot(x_cont, cdf_cont, color='red', lw=2)
axes[1, 1].set_title("CDF (Normal)\nProbability value is <= x")
axes[1, 1].set_ylabel("Cumulative Probability")

pt.tight_layout()
pt.show()

# Discrete Example: Dice rolls (PMF & CDF)
n_rolls = 1
p_success = 1/6  # probability of rolling a 6
k = np.arange(0, 2)  # 0 or 1 success

# PMF: probability of exactly k successes
pmf_values = binom.pmf(k, n_rolls, p_success)
print("Dice PMF:", list(zip(k, pmf_values)))

# CDF: probability of <= k
cdf_values = binom.cdf(k, n_rolls, p_success)
print("Dice CDF:", list(zip(k, cdf_values)))

pt.figure(figsize=(10,4))
pt.subplot(1,2,1)
pt.bar(k, pmf_values)
pt.title("PMF: Dice roll success")
pt.xlabel("Success (6 rolled?)")
pt.ylabel("Probability")

pt.subplot(1,2,2)
pt.bar(k, cdf_values)
pt.title("CDF: Dice roll success")
pt.xlabel("Success (6 rolled?)")
pt.ylabel("Cumulative Probability")
pt.show()

# Continuous Example: Student marks (PDF & CDF)
# Synthetic marks dataset
marks = np.array([55, 67, 45, 78, 89, 90, 76, 88, 92, 69])

# Fit a normal distribution
mu = np.mean(marks)
sigma = np.std(marks)

# PDF values
x = np.linspace(40, 100, 100)
pdf = norm.pdf(x, mu, sigma)

# CDF values
cdf = norm.cdf(x, mu, sigma)

pt.figure(figsize=(10,4))
pt.subplot(1,2,1)
pt.plot(x, pdf, color='blue')
pt.title("PDF: Student Marks")
pt.xlabel("Marks")
pt.ylabel("Density")

pt.subplot(1,2,2)
pt.plot(x, cdf, color='green')
pt.title("CDF: Student Marks")
pt.xlabel("Marks")
pt.ylabel("Cumulative Probability")
pt.show()

# Probability example using CDF
# P(student scores <= 80)
prob_80 = norm.cdf(80, mu, sigma)
print(f"Probability student scores <= 80: {prob_80:.2f}")