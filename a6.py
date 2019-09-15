import numpy as np

# pairwise multiplication
a=np.array([1, 2, 3, 4, 5], dtype=int)
b=np.array([2, 3, 4, 5, 6], dtype=int)
c=a*b
print("c="+str(c))

# broadcasting: for different size operations, automatically "stretch" the smaller size matrix
arr1=np.array([[0, 0, 0],
               [10, 10, 10],
               [20, 20, 20],
              [30, 30, 30]])
arr2=np.array([1, 2, 3])
d=arr1+arr2
print("d="+str(d))