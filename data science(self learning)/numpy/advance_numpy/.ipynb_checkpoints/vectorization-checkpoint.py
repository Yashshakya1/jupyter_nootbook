import numpy as np 

li =  [1,2,3,5,4,8]
li1 = [1,2,3,5,4,8]
# list Comprehension
result = [x+y for x,y in zip(li,li1)]
print(result)


# fast way 
array =   np.array([0,1,2,3,4])
array1 = np.array([5,7,8,9,4])
print(array + array1)