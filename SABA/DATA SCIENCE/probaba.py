import random 
import matplotlib.pyplot as pt 

def t():
    ht=random.randint(0,1)
    if ht ==1:
        return "Heads"
    else:
        return "Tails"

def prob(n):
    r={"Heads":0,"Tails":0}
    for i in range(n):
        r[t()]+=1
    print("Heads:",r["Heads"])
    print("Tails:",r["Tails"])

    print("Heads Prob:",r["Heads"]/n)
    print("Tails Prob:",r["Tails"]/n)

    pt.bar(r.keys(),r.values(),color=['green','yellow'])
    pt.show()

prob(10)

def fruitpick():
    f=['apple','orange','grape']
    p=random.randint(0,3)
    if p==0:
        return "apple"
    elif p==1:
        return "orange"
    else:
        return "grape"
    
    
def pick(n):
    r={'apple':0,'orange':0,'grape':0,}
    for i in range(n):
        r[fruitpick()]+=1
    print(r['apple'])
    print(r['orange'])
    print(r['grape'])
  

    print('prob:',r['apple']/n)
    print('prob:',r['orange']/n)
    print('prob:',r['grape']/n)
  

    pt.bar(r.keys(),r.values(),color=['blue','green','red','yellow'])
    pt.show()
pick(100)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

adult=pd.read_csv("adult.csv")

total=adult["sex"].count()
genders=adult.sex
gender_count={"Male":0,"Female":0}
for i in genders:
    if (i=="Male"):
        gender_count["Male"]+=1
    else:
        gender_count["Female"]+=1
print("Male:",gender_count["Male"])
print("Female:",gender_count["Female"])
print("Male prob:",gender_count["Male"]/total)
print("Female prob:",gender_count["Female"]/total)

values=gender_count.keys()
counts=gender_count.values()
plt.bar(values,counts,color=["black","hotpink"])
plt.show() 

education=adult.education
unique=education.unique()
total=education.count()
counts=education.value_counts()

education_prob=[]
x=0
for i in counts:
    i=i/total
    education_prob.append(i)
    print(unique[x],"prob=",i)
    x+=1

plt.bar(unique,education_prob)
plt.xticks(rotation=45)
plt.show()

plt.plot(unique,education_prob,color="r",linewidth=2,marker="o",mfc="k")
plt.xticks(rotation=45)
plt.title("education probrbility chart")
plt.ylabel("probebility counts")
plt.show() 

print("-------marital_status probebility-------")
marital_status_labels=adult["marital-status"].unique()
marital_status_counts=[]
x=0
for i in adult["marital-status"].value_counts():
    i=i/adult["marital-status"].count()
    marital_status_counts.append(i)
    print(marital_status_labels[x],"prob=",i)
    x+=1

plt.plot(marital_status_labels,marital_status_counts,linewidth=3,color='g',marker='H',ms=7,mec='b',mfc='b')
plt.xticks(rotation=45)
plt.title("marital-status probebility chart")
plt.xlabel("marital-status")
plt.ylabel("probability counts")
plt.show()

print("")
print("-------race probebility--------")
race_labels=adult["race"].unique()
race_counts=[]
x=0
for i in adult["race"].value_counts():
    i=i/adult["race"].count()
    race_counts.append(i)
    print(race_labels[x],"prob=",i)
    x+=1
plt.plot(race_labels,race_counts,color='g',marker='P',ms=5,mec='y',mfc='y')
plt.title("race probebolity chart")
plt.xticks(rotation=10)
plt.ylabel("probebility counts")
plt.show()

print("")
print("-------relationship probebility-------")
relationship_labels=adult["relationship"].unique()
relationship_counts=[]
x=0
for i in adult["relationship"].value_counts():
    i=i/adult["relationship"].count()
    relationship_counts.append(i)
    print(relationship_counts[x],"prob=",i)
    x+=1

plt.plot(relationship_labels,relationship_counts,marker='d',ms=8,mec='m',mfc='m')
plt.title('relationship probebility chart')
plt.xticks(rotation=45)
plt.ylabel("probrbility counts")
plt.show() 

adult.dropna(subset=['occupation'],inplace=True)
# adult["occupation"].dropna(inplace=True) 
occupation_labels=adult["occupation"].unique()
print(occupation_labels)
occupation_counts=[]
x=0
for i in adult["occupation"].value_counts():
    i=i/adult["occupation"].count()
    occupation_counts.append(i)
    print(occupation_labels[x],"prob=",i)
    x+=1
plt.plot(occupation_labels,occupation_counts,marker="D",ms=4,mfc='c',mec='c')
plt.title("occupation probebility chart")
plt.ylabel("probebility counts")
plt.xticks(rotation=45)
plt.show() 