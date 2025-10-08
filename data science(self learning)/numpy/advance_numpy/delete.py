import numpy as np 
arr = np.array([1,2,3,5,4,8])
print(np.delete(arr,3,axis=None))

arr = np.array([[1,2,3,5,4,8],[8,4,7,5,6,9]])
print("remove for the 2d :-")
print(np.delete(arr,1,axis=0))