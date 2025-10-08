import numpy as np
# insert method is used for add the value of any type of array 
# np.insert(arr_name,index,value,axis = 0/1/none) 
arr = np.arange(1,11)
print(arr)
print(np.insert(arr,7,17,axis=0))

# adding the value for the 2d array 
new_array = np.array([[0,1,2,3,4],
                      [5,7,8,9,4]])
print('2d array\n',new_array)
print("only for rows :-")
print(np.insert(new_array,1,[999,99,9,999,9999],axis=0))
print("for the columns :-")
print(np.insert(new_array,1,[999,99],axis=1))
print("experiment by default axis rows :-")
print(np.insert(new_array,(0,1),100,axis=0))