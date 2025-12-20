# Q.13 Convert a pandas series to numpy array?
import numpy as np
import pandas as pd 
li = [4,5,8,9,6] 
df = pd.Series(li)
arr = np.array(df)
print(df)
print(arr)
print(df.to_numpy)