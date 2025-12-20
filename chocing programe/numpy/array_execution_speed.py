import numpy as np
import time  
arr = np.array([1,2,3,4,5,6])
t1 = time.time()
list = [1,2,3,4,5,6]
t2 = time.time()
t = t2 - t1
print(t)