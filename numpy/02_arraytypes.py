import numpy as np
arr_0d = np.array([44])
arr_1d = np.array([33,22,44,56,55,44])
arr_2d = np.array([[33,22,44,22] ,[44,22,44,22],[22,9,66,0]])
arr_3d = np.array([[[34,34,12],[34,42,66]], [[32,44,11],[6,42,32]]])
print(arr_3d)

print(arr_3d.ndim)    #checking dimension
print(arr_3d.shape)
print(arr_3d.size)