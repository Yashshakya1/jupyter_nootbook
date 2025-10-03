import numpy as np 
arr = np.array([[9, 2, 7],
                [4, 6, 5],
                [3, 8, 1]])
print(arr)
print("sort array")
print(np.sort(arr))
print("for the row :-")
print(np.sort(arr , axis=1))
print("for the column :-")
print(np.sort(arr , axis=0))