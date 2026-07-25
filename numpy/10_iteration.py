import numpy as np

arr_1d = np.array([3,1,4,2,4])
#for x in arr_1d:
#    print(x)

arr_2d = np.array([[2,1,4,2] , [4,5,2,3]])
#for x in arr_2d:    #for each row
#    print(x)

#for x in arr_2d:    # for each element
#    for y in x:
#       print(y)


arr_3d = np.array([[[2,3,1,4] ,[31,31,43,42]], [[3,3,4,2] ,[4,44,22,6]]])
#for x in arr_3d:
#    for y in x:
#        for z in y:
#            print(z)


for x in np.nditer(arr_3d):  # for accessing each element use nditer() function
    print(x)
for x in arr_3d.flat:    # for accessing each element use .flat function
    print(x)
