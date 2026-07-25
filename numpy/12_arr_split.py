import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
arr_split = np.array_split(arr , 2)
print(arr_split)
print(arr_split[0])
print(arr_split[1])
