import numpy as np 
# shape return the how many rows and column in the array 
arr = np.array([[1,2,3,5,6],
                [6,3,2,5,4]])
print(arr)
print("how many rows and columns :- ",arr.shape)


# size return how many element in the array
arr = np.array([[1,2,3,5,6],
                [6,3,2,5,4]])
print("size on this array :- ",arr.size)


# ndim return the how many dimension array 
arr = np.array([[1,2,3,5,6],
                [6,3,2,5,4]])
print("dimension in this array :- ",arr.ndim)

# dtype is return the data type in the array element 
arr = np.array([[1,2,3,5,6],
                [6,3,2,5,4]])
print("data type on this array elements :-",arr.dtype)
