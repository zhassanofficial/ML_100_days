import numpy as np

arr = np.array([1,2,3,4,5,3,6,7,8])
#new = np.where(arr == 3)
#print(new)
arr_new = np.where(arr%2 == 1)
print(arr_new)