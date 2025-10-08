import numpy as np 
# splliting for the split the array 
# there are three function / method for splitting 
# syntex np.split(array_name, how much you need the spliting like 2) 
# 1. np.split for divided in equal parts
# 2. np.vsplit for the vertically 
# 3. np.hsplit for the horizontally 
arr = np.array([1,2,5,4,6,8])
print('orginal array :-\n',arr)
# arr = np.array([1,2,5,4,6]) this array showing error because there are 5 elements 
# it is not possible to splite in the equal parts
print("this array split in equal parts :-\n",np.split(arr,2))
v_array =   np.array([[0,1,2,3,4],
                      [5,7,8,9,4]])
print("this array split in equal parts for vertically :-\n")
print('orginal array :-\n',v_array)
print(np.vsplit(v_array,2)) # vsplit is used for the 2d or more dimension array 
h_array =   np.array([[0,1,2,3,4,49],
                      [5,7,8,9,4,18]])
print("this array split in equal parts for horizantally  :-\n")
print('orginal array :-\n',h_array)
print(np.hsplit(h_array,2))
