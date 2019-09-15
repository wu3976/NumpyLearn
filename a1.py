import numpy as np


#ndmin: indicates the minimum dimention of array. e.g. if you input ndmin=2, and you input a
#1-row array, it will automatically consider it to be a 2-row one, and print it like the style
# [[a, c, d]]

#dtype: the data typr of array. dtype=complex indicates complex number
#order: C is row based, F is column-based.
arr=np.array([1, 2, 3, 4], ndmin=1, dtype=complex, order='C')
print(arr)

#when express complex number j, use 1j
dt=np.dtype(complex)
arr2=np.array([1j, 2j, 3j, 1+3j], dtype=dt, ndmin=2)
print(arr2)

#arange: generate an nparray in [0, 24), step 0.5
arr3=np.arange(0, 24, 0.5)
print (arr3)

#print some flags of arr3
print(arr3.flags)

# zeros: return an array filled with zero, in size, data type, order specified.
arr4=np.zeros([4, 3], dtype=float, order='C')
print(arr4)

# empty: return an specified size, data type uninitialized array
arr5=np.empty([4, 3], dtype=float, order='C')
print(arr5)

# one: filled with ones
arr6=np.ones([4, 3], dtype=int, order='F')
print (arr6)

