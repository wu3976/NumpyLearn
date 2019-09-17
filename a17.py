import numpy.matlib
# this library have modules to return matrix instead of ndarray objects
# matrix is always 2 dimensional, while ndarray can be any dimensional
import numpy as np

# np.matlib.empty() return matrix w/o initialized values
arr=np.matlib.empty([3, 3], dtype=int, order="C")
print (arr) # because not empty, just print meaningless numbers
# numpy.matlib.zeros() returns zeros
arr2=np.matlib.zeros([2, 3], dtype=float, order="C")
print(arr2)
# numpy.matlib.ones() returns ones
arr3=np.matlib.ones([4, 3], dtype=int)
print(arr3)
# numpy.matlib.eye() returns a matrix with 1 along the diagonal elements and the zeros elsewhere
# specify rows: n, columns: M, axis: k
# k=0 is the main axis, -1 is left of main axis, 1 is right of main axis
arr4=np.matlib.eye(n=3, M=5, dtype=int, k=-1)
print(arr4)
# numpy.matlib.identity() return an identity matrix
arr5=np.matlib.identity(5, dtype=int)
print (arr5)
# numpy.matlib.rand() return matrix full of random values from 0 to (exclusively) 1
arr6=np.matlib.rand(3, 3)
print(arr6)
# matrix and array are interconvertible
arr7=np.array([[1, 2], [3, 4]], dtype=int)
mat=np.asmatrix(arr7)
print(mat)
arr8=np.asarray(mat)
print(arr8)