# integer indexing
import numpy as np
arr= np.array([[1, 2], [3, 4], [5, 6]], dtype=int)
arr2= arr[[0, 1, 2], [0, 1, 0]] # get elements at 3 points: (0, 0), (1, 1) and (2, 0)
print(arr2)

# this one returns a 2x2 array, whose element is in the rows [[0, 0], [3, 3]],
# column [[0, 2], [0, 2]] of x
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print (x)
print('The corner elements of this array are:')
print(y)

# can mix use of basic and advanced indexing
c=x[1:, [1, 2]] # don't add [] for basic indexing
print("c="+str(c))

# boolean indexing
d=x[x>5] # return flatted array contains all elements larger than 5
print("d="+str(d))

#isnan method return true if the value is np.nan
arr3=np.array([np.nan, 1, 2, 3, np.nan, 4, 5])
e=arr3[np.isnan(arr3)]
f=arr3[~np.isnan(arr3)] # ~ is "not"
print("e: "+str(e)+" f: "+str(f))

#iscomplex method return true if the value is complex number
arr4=np.array([1, 2+1j, 3+2j, 4], dtype=complex)
g=arr4[np.iscomplex(arr4)]
print("g: "+str(g))
