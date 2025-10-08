import numpy as np
# insert method is used for add the value of any type of array 
# np.insert(arr_name,index,value,axis = 0/1/none) 
arr = np.arange(1,20)
print(arr)
print(np.insert(arr,7,17,axis=0))