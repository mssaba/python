import seaborn as ss
import matplotlib.pyplot as pt
import pandas as pd
import numpy as np

#1 Seaborn Setting
ss.set_theme(style='whitegrid')
pt.rcParams['figure.figsize']=(7,4)

#2
data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 55],
    "Salary": [30000, 35000, 50000, 65000, 80000, 95000, 110000, 130000],
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance", "Management", "Management"],
    "Experience": [0, 2, 5, 8, 12, 15, 20, 25],
    "Performance": ["Low", "Medium", "Medium", "High", "High", "High", "Excellent", "Excellent"]
}

df=pd.DataFrame(data)

# HISTOGRAM

ss.histplot(df['Salary'])
pt.title("Salary Distribution")
pt.show()

#kde plot

ss.kdeplot(df['Experience'],fill=True)
pt.title('Experience KDE')
pt.show()

#ecdf plot
ss.ecdfplot(df['Age'])
pt.title('AGE ECDF')
pt.show()

#count plot
ss.countplot(df['Department'])
pt.title('Departmnet count')
pt.show()

#bar plot
ss.barplot(x='Department',y='Salary',data=df)
pt.title('Avg Salary by Department')
pt.show()

# Box Plot
ss.boxplot(x="Department", y="Salary", data=df)
pt.title("Salary Distribution by Department")
pt.show()

# Violin Plot
ss.violinplot(x="Department", y="Salary", data=df)
pt.title("Violin Plot - Salary")
pt.show()


# Strip Plot
ss.stripplot(x="Department", y="Salary", data=df, jitter=True)
pt.title("Strip Plot - Salary")
pt.show()

#RELATIONAL PLOTS (CUSTOM DF)
ss.scatterplot(x='Experience',y='Salary',hue='Department',data=df)
pt.title("Scatter Plot")
pt.show()


# Line Plot
ss.lineplot(x="Age", y="Salary", data=df)
pt.title("Age vs Salary (Line Plot)")
pt.show()


# Regression Plot
ss.regplot(x="Experience", y="Salary", data=df)
pt.title("Regression Plot")
pt.show()

# 6. MULTIVARIATE ANALYSIS (CUSTOM DF)
corr_custom = df[["Age", "Salary", "Experience"]].corr()

ss.heatmap(corr_custom, annot=True, cmap="coolwarm")
pt.title("Correlation Heatmap (Custom DF)")
pt.show()

#pair plot
ss.pairplot(df[['Age','Salary','Experience']])
pt.show()

# 7. BUILT-IN SEABORN DATASETS

tips = ss.load_dataset("tips")
iris = ss.load_dataset("iris")

# Scatter Plot
ss.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
pt.title("Tips Dataset Scatter Plot")
pt.show()

# Box Plot
ss.boxplot(data=tips, x="day", y="total_bill")
pt.title("Tips Dataset Box Plot")
pt.show()

# Pair Plot
ss.pairplot(iris, hue="species")
pt.show()


# 8. FIGURE-LEVEL PLOTS

ss.catplot(data=tips, x="day", y="total_bill", kind="bar")
pt.show()

ss.lmplot(data=tips, x="total_bill", y="tip", hue="sex")
pt.show()

# 9. COLOR PALETTES

ss.set_palette("pastel")
ss.barplot(x="Department", y="Salary", data=df)
pt.title("Pastel Palette Example")
pt.show()

ss.set_palette("deep")
ss.barplot(x="Department", y="Salary", data=df)
pt.title("Deep Palette Example")
pt.show()

# 10. SAVE A PLOT

ss.scatterplot(x="Experience", y="Salary", data=df)
pt.title("Saved Plot Example")
pt.savefig("seaborn_custom_dataframe_plot.png")
pt.show()