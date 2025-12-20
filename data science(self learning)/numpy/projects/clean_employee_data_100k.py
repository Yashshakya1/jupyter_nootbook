import numpy as np
import pandas as pd 
 # load the 1m employee data set 
Dataset = pd.read_csv("employee_data_100k.csv",encoding="latin1")
print(Dataset)

# clean the data set
#   check for null values 
print(pd.isnull(Dataset).sum())
Dataset["Salary (INR)"].fillna(Dataset["Salary (INR)"].mean() , inplace = True)
Dataset["Performance Rating"].fillna(Dataset["Performance Rating"].median() , inplace = True)

# replace inf values with nan and then fill nan values with mean of the column
Dataset.replace([np.inf, -np.inf] , np.nan, inplace=True)
Dataset.fillna(Dataset.mean() , inplace = True)

# removing the duplicates values
Dataset.drop_duplicates(inplace = True)

# replace the negative salary 
Dataset["Salary (INR)"]  = np.where(Dataset["Salary (INR)"] < 0 ,Dataset["Salary (INR)"].mean() , Dataset["Salary (INR)"])

# set the salary range 
salary_mean = Dataset["Salary (INR)"].mean()
salary_std  = Dataset["Salary (INR)"].std()

lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# remove the salary too much high or low 
# Dataset = Dataset[(Dataset["Salary (INR)"] >= lower_bound & Dataset["Salary (INR)"] <= upper_bound)]
Dataset = Dataset[(Dataset["Salary (INR)"] >= lower_bound) & (Dataset["Salary (INR)"] <= upper_bound)]
Dataset.to_csv("employee_data_100k.csv", index = False)
print('Data is properly clean in this file :- "employee_data_100k.csv "')

