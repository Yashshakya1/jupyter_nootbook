import numpy as np 
arr = np.array([[1,2,3,5,6],[3,5,4,6,4]])
print(arr)
print(arr.ndim)



arr1 = np.array([[[1,2,3,4],[5,6,7,8]]  , [[8,7,6,5],[4,3,2,1]]])
print(arr1)
print(arr1.ndim)
# linspace is a method which is using for generate the matrix 
# (starting , ending , /)
array = np.linspace(1,100,100)
# reshape method using for breakdown the array 
# arr.reshape(10,10)
array.reshape(10,10)
print(array)

# random is a method to genrate the random number 
arr3 = np.random.randint(1,10,4)
print("random :-")
arr3.reshape(2,2)
print(arr3)

# eye is used for making identity matrix
# np.eye(dimention number)
arr_ident = np.eye(3)
print("identity")
print(arr_ident)

# shape 
arrary1 = np.array([[1,2,3,4,5],[8,4,6,8,4]] , ndmin=4)

print(arrary1,arrary1.shape)


# ones and zeroes 
print(np.ones(10, dtype=int))
print(np.zeros(10,dtype=int))
# some new methods 