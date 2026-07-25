import numpy as np
arr = np.array([44,2,42,43,2])
#print(arr.dtype)
arr_01 = np.array(['apple' , 'banana' , 'cat' , 'dog'])
#print(arr_01.dtype)  # u : unsigned interger

arr_02 = np.array([3,452,2,1,2] , dtype= 'S')
#print(arr_02)
#print(arr_02.dtype)  # datatype as a string

arr_03 = np.array(['4','2','3' ,'3'] , dtype='i')
#print(arr_03.dtype)

#  best way to change type of an array
arr_04 = np.array([0,1,0,1,2,4])
new_arr = arr_04.astype(bool)
print(new_arr)