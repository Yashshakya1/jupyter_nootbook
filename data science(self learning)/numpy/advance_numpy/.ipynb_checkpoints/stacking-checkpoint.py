import numpy as np 
arr1 = np.array([1,2,5,4,6])
arr2 = np.array([1,2,5,4,10])
print("rows wise :-\n",np.vstack((arr1,arr2)))
print("columns wise :-")
print(np.hstack((arr1,arr2)))

# np.vstack is for vertically 
# np.hstack for the horizontally 