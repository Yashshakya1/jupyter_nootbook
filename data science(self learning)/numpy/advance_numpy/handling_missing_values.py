import numpy as np  
# 1.
# isnan method is used for detect the missing values 
arr = np.array([1,np.nan,2,np.nan,3]) 
print(np.isnan(arr))
print(np.nansum(arr))
# interview question 
# print(np.nan == np.nan)
# we cannot compair the nan values

# 2.
# is nan_to_num(arr_name, nan = values)
# this method is used for replace the nan value in spacfic number 
# default value zero in this method 
print(np.nan_to_num(arr, nan = 5))

# 3.
# np.isinf is used for detect the infinite values in the array 
array = np.array([1,2,np.inf,5,np.inf,48,np.inf])
print(np.isinf(array))
