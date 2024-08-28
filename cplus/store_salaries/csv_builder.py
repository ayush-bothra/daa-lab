import numpy as np
import pandas as pd

# Number of employees
num_employees = 2000

# Salary ranges
positive_salary_range = (20000, 50000)
negative_salary_range = (-10000, 40000)
employee_ids = np.arange(1, num_employees + 1)

# Generate positive salary data
positive_salaries_1 = np.random.randint(positive_salary_range[0], positive_salary_range[1], num_employees)
positive_salaries_2 = np.random.randint(positive_salary_range[0], positive_salary_range[1], num_employees)
positive_salaries_3 = np.random.randint(positive_salary_range[0], positive_salary_range[1], num_employees)

# Generate negative salary data
negative_salaries = np.random.randint(negative_salary_range[0], negative_salary_range[1], num_employees)

# Generate salary data with some missing values
salaries_with_missing = np.random.randint(positive_salary_range[0], positive_salary_range[1], num_employees).astype(float)
missing_indices = np.random.choice(num_employees, size=int(num_employees * 0.1), replace=False)  # 10% missing
salaries_with_missing[missing_indices] = np.nan

# Create DataFrames
df_salaries_1 = pd.DataFrame({'Employee ID': employee_ids,'Basic Salary': positive_salaries_1})
df_salaries_2 = pd.DataFrame({'Employee ID': employee_ids,'Basic Salary': positive_salaries_2})
df_salaries_3 = pd.DataFrame({'Employee ID': employee_ids,'Basic Salary': positive_salaries_3})
df_with_negative_salaries = pd.DataFrame({'Employee ID': employee_ids,'Basic Salary': negative_salaries})
df_with_missing_salaries = pd.DataFrame({'Employee ID': employee_ids,'Basic Salary': salaries_with_missing})

# Save to CSV files
df_salaries_1.to_csv('positive_salaries_1.csv', index=False)
df_salaries_2.to_csv('positive_salaries_2.csv', index=False)
df_salaries_3.to_csv('positive_salaries_3.csv', index=False)
df_with_negative_salaries.to_csv('negative_salaries.csv', index=False)
df_with_missing_salaries.to_csv('salaries_with_missing.csv', index=False)

print("CSV files created successfully!")
