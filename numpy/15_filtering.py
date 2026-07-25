import numpy as np
arr = np.array([42,43,44,45])
filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)