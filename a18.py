import numpy.linalg
# a module contains linear algebra functions
import numpy as np
 # some linear algebra functions
a=np.array([[1, 2], [3, 4]])
b=np.array([[2, 1], [5, 2]])
#np.inner element-wise products cannot be broadcasted
print(np.inner(a, b))

 # np.vdot
arr=np.array([[1, 2, 3], [4, 5, 6]])
arr2=np.array([[2, 4], [6, 8], [10, 12]])
print(np.vdot(arr, arr2))

# np.dot dot product of matrix, for vector, it is the inner product
print(np.dot(arr,arr2))
print(np.dot([1, 2, 1], [3.2, 4.5, 12]))

# np.matmul matrix product
print (np.matmul(arr, arr2))

#np.linalg.determinant
arr3=np.array([[1, 3, 4], [2, 4, 1], [2.5, 4.2, 1]])
print(np.linalg.det(arr3))

#np.linalg.solve
coefficient_arr=np.array([[1, 2, 3], [4, 0, 1], [3, 4, 6]]) # coeff matrix must be square
b_vector=np.array([9, 8, 6])
print(np.linalg.solve(coefficient_arr, b_vector))

# np.linalg.inv() find inverse of matrix
a=np.array([[1, 2], [3, 4]], dtype=int)
print (np.linalg.inv(a))
print (np.matmul(np.linalg.inv(a), a)) # the result is almost[[1, 0], [0, 1]]