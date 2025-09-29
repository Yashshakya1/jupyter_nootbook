import numpy as np 
# astype is used for the array conversion into other array like int to float , int to str and so on 
arr = np.array([1.2,1.3,1.4,1.5])
int_arr = arr.astype(int)
print(int_arr)
print("type in this array is :-", int_arr.dtype)