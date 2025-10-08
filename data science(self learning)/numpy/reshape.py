import numpy as np 
# reshape is using for change the shape of any type of array 
# syntex :- arr.reshape(rows,colums)
# but one condition is here that was the they only when the shape of the size is same 
# other wise it is not work 
arr = np.arange(1,11)
print(arr.reshape(2,5))
