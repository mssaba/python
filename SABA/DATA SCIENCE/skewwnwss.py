
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (7, 4)

# 1. Load Real Dataset

df = sns.load_dataset("tips")
print("\n--- Dataset Preview ---")
print(df.head())

# 2. Skewness & Kurtosis (PANDAS)

numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns

print("\n--- Skewness & Kurtosis (Before Transformation) ---")
for col in numeric_cols:
    print(f"{col}")
    print(" Skewness :", df[col].skew())
    print(" Kurtosis :", df[col].kurt())
    print("-" * 20)

# 3. Visualize Skewness

sns.histplot(df["total_bill"], kde=True)
plt.title("Total Bill Distribution (Original)")
plt.show()

sns.histplot(df["tip"], kde=True)
plt.title("Tip Distribution (Original)")
plt.show()

# 4. Identify Skewness Problem

# Rule of thumb:
# |skew| > 1  -> highly skewed
# |skew| > 0.5 -> moderately skewed

print("\nSkewness total_bill:", df["total_bill"].skew())
print("Skewness tip:", df["tip"].skew())

# Both are RIGHT SKEWED

# 5. Fix Skewness (Log Transformation)

df["total_bill_log"] = np.log1p(df["total_bill"])
df["tip_log"] = np.log1p(df["tip"])

# 6. Skewness After Transformation

print("\n--- Skewness & Kurtosis (After Log Transformation) ---")
print("total_bill_log")
print(" Skewness :", df["total_bill_log"].skew())
print(" Kurtosis :", df["total_bill_log"].kurt())

print("\ntip_log")
print(" Skewness :", df["tip_log"].skew())
print(" Kurtosis :", df["tip_log"].kurt())

# 7. Visualization After Fixing Skewness

sns.histplot(df["total_bill_log"], kde=True)
plt.title("Total Bill (Log Transformed)")
plt.show()

sns.histplot(df["tip_log"], kde=True)
plt.title("Tip (Log Transformed)")
plt.show()

# 8. Before vs After Comparison

fig, axes = plt.subplots(2, 2, figsize=(10, 7))

sns.histplot(df["total_bill"], kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Original Total Bill")

sns.histplot(df["total_bill_log"], kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Log Transformed Total Bill")

sns.histplot(df["tip"], kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Original Tip")

sns.histplot(df["tip_log"], kde=True, ax=axes[1, 1])
axes[1, 1].set_title("Log Transformed Tip")

plt.tight_layout()
plt.show()

