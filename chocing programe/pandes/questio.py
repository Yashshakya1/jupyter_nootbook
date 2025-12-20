 # Q.11 obtain the frequency(no of time paticular element occur) of elements in column 3?
import pandas as pd 
import numpy as np
df = pd.read_csv("german_credit_risk.csv")
print(df)
frequence = df["Job"].value_counts()
print(frequence)