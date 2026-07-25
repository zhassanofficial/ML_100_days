import numpy as np
arr = np.array([[3,3,4,2] , [3,4,2,3]])
#print(arr.shape) # output(2,4)--> 2 dimension array 1st
                  #  dimension = 2 elements 2nd dimension has  = 4 elements
arr_5d = np.array([1,2,3,4] , ndmin=5)
print(arr_5d)
print(arr_5d.shape)