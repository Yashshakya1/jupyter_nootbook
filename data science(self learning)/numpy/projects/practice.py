import numpy as np
import pandas as pd 

Dataset = pd.read_csv("employee_data_100k.csv")

# Check missing values
print("\nMissing values before cleaning:\n", Dataset.isnull().sum())

# Fill missing Salary and Performance Rating first
Dataset["Salary (INR)"] = Dataset["Salary (INR)"].fillna(Dataset["Salary (INR)"].mean())
Dataset["Performance Rating"] = Dataset["Performance Rating"].fillna(Dataset["Performance Rating"].median())

# Replace infinities with NaN
Dataset.replace([np.inf, -np.inf], np.nan, inplace=True)

# ✅ Fill NaNs only in numeric columns
Dataset.fillna(Dataset.mean(numeric_only=True), inplace=True)

# Drop duplicates
Dataset.drop_duplicates(inplace=True)

# Replace negative salaries
Dataset["Salary (INR)"] = np.where(
    Dataset["Salary (INR)"] < 0,
    Dataset["Salary (INR)"].mean(),
    Dataset["Salary (INR)"]
)

# Define and filter salary range (with parentheses)
salary_mean = Dataset["Salary (INR)"].mean()
salary_std = Dataset["Salary (INR)"].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)
Dataset = Dataset[(Dataset["Salary (INR)"] >= lower_bound) & (Dataset["Salary (INR)"] <= upper_bound)]

# Save cleaned data
Dataset.to_csv("employee_data_100k_cleaned.csv", index=False)
print('\n✅ Data successfully cleaned and saved as "employee_data_100k_cleaned.csv"')
