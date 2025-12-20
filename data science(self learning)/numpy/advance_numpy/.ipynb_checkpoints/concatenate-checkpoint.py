import numpy as np 
# by default axis row 
arr = np.array([1,2,3])
arr1 = np.array([4,5,6])
print(np.concatenate((arr,arr1))) # axis=0
print(np.concatenate((arr,arr1), axis=0))