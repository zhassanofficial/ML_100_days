import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#new_arr = arr.reshape(3,4) # reshape 1D array into 2D
#print(new_arr)

arr_3d = arr.reshape(2,3,2) # converting int 3D
#print(arr_3d.base)


# converting multi-dimensional array into 1D

arr_00 = np.array([[2,1,3,1] , [5,6,2,4] , [7,4,2,6]])
new_arr = arr_00.reshape(12)
print(new_arr)
print(new_arr.ndim)