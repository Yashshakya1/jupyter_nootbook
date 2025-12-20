# aggergation is return the statestic like min,max,std,mean,veriance and etc 
import numpy as np 
arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr,axis = 1))
print(np.min(arr))
print(np.std(arr))
# np.var(): Computes the variance, which is the square of the standard deviation.
print(np.var(arr))  # μ=1/n ∑^n/i=1  xi



