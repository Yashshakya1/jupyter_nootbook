import numpy as np 
'''
Broadcasting means performing operations between arrays of different shapes —
NumPy automatically “expands” the smaller array to match the shape of the larger one 
(without actually copying data).
'''
print("for the 1d :-")
a = np.array([1,2,3,4,5])
b = 5
print(a+b)
print("for the 2d :-")
array =   np.array([[0,1,2,3,4],
                    [5,7,8,9,4]])
print(array + a)



'''
✅ Rule 1: If dimensions are equal → fine
✅ Rule 2: If one dimension is 1 → expand it to match the other
❌ Else: Broadcasting fails (ValueError)
'''
