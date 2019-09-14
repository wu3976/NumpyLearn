import numpy as np

# arange (start, stop, step, dtype): returns an ndarray object containing evenly spaced values within a given range.
arr1=np.arange(1, 6, 0.8, dtype=float)
print("arr1="+str(arr1))

# linspace(start, stop, num, endpoint, retstep, dtype) similar to arange, but num indicate the number of
# points, boolean value endpoint indicate whether to include endpoint for the array.
# retstep indicate whether display interval
arr2=np.linspace(0, 10, 6, dtype='i4', endpoint=True, retstep=True)
print("arr2="+str(arr2))

# logspace(start, stop, num, endpoint, base, dtype) return lograrithm spaced array.
arr3=np.logspace(2, 10, 4, endpoint=True, base=10, dtype='f')
print("arr3="+str(arr3))
arr4=np.logspace(1,10,num = 10, base = 2)
print ("arr4="+str(arr4))