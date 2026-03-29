import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

data={
    "Age":[25, 30, 28, np.nan, 35, 40, 29, 31, np.nan, 36],
    "Salary": [50000, 60000, 58000, 52000, 62000, 70000, 59000, 61000, 53000, 65000],
    "Department": ["HR", "IT", "IT", "HR", "IT", "Finance", "Finance", "HR", "IT", "Finance"]
}

df=pd.DataFrame(data)
#filling null
df['Age'].fillna(df['Age'].mean(),inplace=True)
#deleting duplicates
df.drop_duplicates(inplace=True)
#encoding 
# Option 1: One-hot encoding
df_encoded = pd.get_dummies(df, columns=["Department"], drop_first=True)
l=LabelEncoder()
df['d_l']=l.fit_transform(df['Department'])
# 5. Feature Transformation (Fix Skewness)
print("\nSkewness before transformation:")
print(df_encoded[["Age", "Salary"]].skew())

# Log transform Salary (common for right-skewed data)
df_encoded["Salary_log"] = np.log1p(df_encoded["Salary"])
print("\nSkewness after log transformation:")
print(df_encoded[["Salary_log"]].skew())


# 6. Scaling Features
scaler = StandardScaler()
df_encoded[["Age_scaled", "Salary_scaled"]] = scaler.fit_transform(df_encoded[["Age", "Salary_log"]])


# Or MinMax scaling
minmax_scaler = MinMaxScaler()
df_encoded[["Age_norm", "Salary_norm"]] = minmax_scaler.fit_transform(df_encoded[["Age", "Salary_log"]])

# 7. Outlier Detection (Z-score)
from scipy import stats
z_scores = np.abs(stats.zscore(df_encoded[["Age_scaled", "Salary_scaled"]]))
outliers = np.where(z_scores > 3)
print("\nOutlier indices (Z-score > 3):", outliers)

# 8. Visualization
sns.histplot(df_encoded["Salary"], kde=True, color="blue", label="Original Salary")
sns.histplot(df_encoded["Salary_log"], kde=True, color="green", label="Log Salary")
plt.legend()
plt.show()

print("\n--- Preprocessed Dataset ---")
print(df_encoded)



""" Data preprocessing is the process of preparing
raw data for analysis or machine learning.

Real-world data is often:
    - Incomplete (missing values)
    - Noisy (errors or outliers)
    - Inconsistent
    - Unscaled
    - Containing categorical variables

Proper preprocessing improves:
    - Model accuracy
    - Training speed
    - Interpretability

--------------------------------------------
STEPS WE WILL COVER:
--------------------------------------------

1. Loading data
2. Exploring data
3. Handling missing values
4. Encoding categorical variables
5. Feature scaling
6. Handling outliers
7. Splitting data into train/test sets

--------------------------------------------
"""

# IMPORT REQUIRED LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# SECTION 1: CREATE SAMPLE DATASET

data = {
    "Age": [25, 30, 35, np.nan, 40, 28, 32, 45, 38, np.nan],
    "Salary": [50000, 60000, 65000, 70000, np.nan, 52000, 58000, 80000, 75000, 62000],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance", "IT", "HR", "Finance", "IT"]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)


# SECTION 2: DATA EXPLORATION

"""
Before preprocessing, always explore the data.

Important functions:
    df.info()      -> Structure
    df.describe()  -> Summary statistics
"""

print("\nDataset Info:\n")
print(df.info())

print("\nStatistical Summary:\n")
print(df.describe())

print("\nMissing Values Count:\n")
print(df.isnull().sum())


# SECTION 3: HANDLING MISSING VALUES

"""
Common strategies:

1. Remove rows
2. Replace with mean
3. Replace with median
4. Replace with mode

Here we replace:
- Age with mean
- Salary with median
"""

# Replace missing Age with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Replace missing Salary with median
df["Salary"].fillna(df["Salary"].median(), inplace=True)

print("\nAfter Handling Missing Values:\n")
print(df)


# SECTION 4: ENCODING CATEGORICAL VARIABLES

"""
Machine learning models require numerical input.

Method:
Label Encoding
"""

encoder = LabelEncoder()
df["Department_Encoded"] = encoder.fit_transform(df["Department"])

print("\nAfter Encoding Categorical Variable:\n")
print(df)

print("\nEncoding Mapping:")
for index, label in enumerate(encoder.classes_):
    print(label, "->", index)


# SECTION 5: FEATURE SCALING

"""
Why scaling?

Many ML algorithms are sensitive to scale:
    - KNN
    - SVM
    - Gradient Descent

Two common methods:

1. Standardization:
   (x - mean) / std
   Mean = 0, Std = 1

2. Normalization (Min-Max Scaling):
   Scale between 0 and 1
"""

# Standardization
scaler = StandardScaler()
df[["Age_scaled", "Salary_scaled"]] = scaler.fit_transform(
    df[["Age", "Salary"]]
)

print("\nAfter Standardization:\n")
print(df[["Age_scaled", "Salary_scaled"]])


# SECTION 6: HANDLING OUTLIERS

"""
Outliers can distort model performance.

We detect outliers using:
Z-score method

If |Z| > 3, it's considered an outlier.
"""

from scipy.stats import zscore

df["Salary_Zscore"] = zscore(df["Salary"])

print("\nZ-scores for Salary:\n")
print(df[["Salary", "Salary_Zscore"]])

# Identify outliers
outliers = df[np.abs(df["Salary_Zscore"]) > 3]

print("\nDetected Outliers:\n")
print(outliers)


# SECTION 7: SPLITTING DATA

"""
Before training a model, split data into:

1. Training set (usually 70–80%)
2. Testing set (20–30%)

This prevents overfitting.
"""

X = df[["Age_scaled", "Salary_scaled", "Department_Encoded"]]
y = df["Salary"]  # Example target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Set Size:", X_train.shape)
print("Testing Set Size:", X_test.shape)


# SECTION 8: VISUALIZATION

"""
Visualization helps understand distribution.
"""

plt.hist(df["Salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
