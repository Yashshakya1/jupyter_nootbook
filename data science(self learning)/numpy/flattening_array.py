import numpy as np 
arr = np.array([[1,2,3,4,5,6],[9,8,7,4,5,4]])
print(arr.ravel())   # ravel for the view 
print(arr.flatten()) # flatten for the copy
