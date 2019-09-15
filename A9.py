import numpy as np

# some actions on matrices.
arr=np.arange(0, 60, 5, dtype='i')
# reshape array into [m, n] dimension
arr=arr.reshape(3, 4, order='F') # Fortran order: put by columns
print(arr)
# flatten: return the copy of value
arr2=arr.flatten()
print(arr2)

