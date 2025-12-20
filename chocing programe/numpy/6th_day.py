import numpy as np 
arrary = np.random.randint(1,10,10)
print(np.sort(arrary))
arr = arrary.reshape(5,2)
print(arr)
# 0 for row 1 for column
print(np.sort(arr ,axis=0))
# for finding the square root 
a = 49
print(np.sqrt(a))

# ceil or floor for finding the rounoff value ceil for the forward and floor for the backward
a = 6.548
print(np.ceil(a))
print(np.floor(a))