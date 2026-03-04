import numpy as np
import seaborn as ss
import pandas as pd
import matplotlib.pyplot as pt

ss.set(style='darkgrid')
pt.rcParams['figure.figsize']=(7,4)

data = {
    "Age": [23, 45, 31, 35, np.nan, 62, 27, 45, 52, 29],
    "Salary": [40000, 80000, 60000, 65000, 70000, 120000, 48000, 82000, 110000, 54000],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Management", "IT", "Finance", "Management", "IT"],
    "Experience": [1, 20, 5, 8, 7, 35, 3, 22, 30, 4],
    "Purchased": [0, 1, 0, 1, 0, 1, 0, 1, 1, 0]
}

df=pd.DataFrame(data)

#Basic understanding of data

print('\nShape of Data')
print(df.shape)

print('\n Data Info')
print(df.info)

print("\n Statistical Summary ")
print(df.describe)

print("\n Missing values")
print(df.isnull().sum())

print("\n fill null value")
df['Age'].fillna(df['Age'].mean())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

#age distribution
ss.histplot(df["Age"])
pt.title("Age Distribution")
pt.show()

#Salary boxplot
ss.boxplot(x=df["Salary"])
pt.title("Salary Boxplot")
pt.show()


# Department count
ss.countplot(x="Department", data=df)
pt.xticks(rotation=45)
pt.title("Department Count")
pt.show()

# 6. Bivariate Analysis

# Experience vs Salary
ss.scatterplot(x="Experience", y="Salary", data=df)
pt.title("Experience vs Salary")
pt.show()

# Salary by Department
ss.boxplot(x="Department", y="Salary", data=df)
pt.xticks(rotation=45)
pt.title("Salary by Department")
pt.show()

# Purchased distribution
ss.countplot(x="Purchased", data=df)
pt.title("Purchased Distribution")
pt.show()

# 7. Multivariate Analysis
corr = df.corr(numeric_only=True)

ss.heatmap(corr, annot=True, cmap="coolwarm")
pt.title("Correlation Heatmap")
pt.show()

# 8. Feature vs Target Analysis

ss.boxplot(x="Purchased", y="Salary", data=df)
pt.title("Salary vs Purchased")
pt.show()

ss.boxplot(x="Purchased", y="Age", data=df)
pt.title("Age vs Purchased")
pt.show()

# 9. Final Dataset Preview
print("\n--- Final Dataset ---")
print(df.head())

print("\nEDA completed successfully.")
 
