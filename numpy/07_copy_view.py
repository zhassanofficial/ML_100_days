import numpy as np
 # copying an array

arr = np.array([22,3,42,1])
new_arr = arr.copy()
arr[0] = 4  # any changes in original copy cannot be affected
#print(arr)
#print(new_arr)

# view

arr_01= np.array([3,2,1,4,])
arr_view = arr_01.view()
arr_view[0] = 5
arr_01[1] = 3
print(arr_01)
print(arr_view)




