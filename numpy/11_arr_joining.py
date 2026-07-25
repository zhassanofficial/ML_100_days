import numpy as np

#arr_1 = np.array([3,4,5,6])
#arr_2 = np.array( [1,2,3,4])
#arr_join = np.concatenate((arr_1 , arr_2))
#print(arr_join)

arr_1 = np.array([[3,4,5,6] , [3,2,1,0]])
arr_2 = np.array( [[1,2,3,4] , [3,4,67,7]])
arr_join = np.concatenate((arr_1 , arr_2) , axis=1)
print(arr_join.ndim)
for x in arr_join:
    print(x)
    for y in x:
        print(y)