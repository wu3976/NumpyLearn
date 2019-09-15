import numpy as np

#np.sort()
dt=np.dtype([('name', 'S10'), ('age', int)])
arr=np.array([("Jones", 25), ("Bill", 21), ("Andrew", 22)], dtype=dt)
print (np.sort(arr, order='name'))#sort according to alphabetical order of name

# np.argsort return the indices of sorted array's corresponding elements
indices=np.argsort(arr, order='name')
print(indices)
sorted_arr=arr[indices]
print(sorted_arr)

# np.argmax np.argmin return index of largest element
a=np.arange(0, 18, 2, dtype=int).reshape(3, 3)
a[1, 0]=20
print(a)
max_index=np.argmax(a) # in this situation, the index is in row-search form
print(max_index)


