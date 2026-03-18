import matplotlib.pyplot as pt
import seaborn as ss
from scipy import stats
import numpy as np
a=np.linspace(-5,5,1000)
df=[10,20,30,50,70,90]

for x in df:
    pt.plot(a,stats.t.pdf(a,x),label=f"t-distribution (df={x})")

pt.plot(a,stats.norm.pdf(a),linestyle='--', label="Normal Distribution")
pt.xlabel("a")
pt.ylabel("PDF")
pt.legend()
pt.grid()
pt.show()

# 2. Manual t-statistic Calculation

# Sample data
sample = np.array([22, 25, 21, 24, 23, 26, 27, 24, 22, 23])

# Hypothesized population mean
mu = 20

n = len(sample)
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)  # ddof=1 for sample std
standard_error = sample_std / np.sqrt(n)

t_statistic = (sample_mean - mu) / standard_error

print("\n--- Manual t-statistic Calculation ---")
print("Sample Mean:", sample_mean)
print("Sample Std Dev:", sample_std)
print("t-statistic:", t_statistic)


# 3. One-Sample t-Test using scipy

t_stat, p_value = stats.ttest_1samp(sample, mu)

print("\n--- One-Sample t-Test ---")
print("t-statistic:", t_stat)
print("p-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")


# 4. 95% Confidence Interval for Mean

confidence_level = 0.95
df = n - 1

t_critical = stats.t.ppf((1 + confidence_level) / 2, df)

margin_of_error = t_critical * standard_error

ci_lower = sample_mean - margin_of_error
ci_upper = sample_mean + margin_of_error

print("\n--- 95% Confidence Interval ---")
print("Lower Bound:", ci_lower)
print("Upper Bound:", ci_upper)