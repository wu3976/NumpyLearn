import numpy as np
# slicing and indexing operations

# slice object: slice (start, stop, step): a kind of index slicing out the array
# from index start to stop, interval of index is 2
arr1=np.arange(0, 5)
slc=slice(0, 6, 2)
print("arr1 sliced="+str(arr1[slc]))

#can also use column
b=arr1[0:6:2]
print("b="+str(b))
b2=arr1[2: ]
print("b2="+str(b2))
b3=arr1[2:4]
print("b3="+str(b3)) # the element at index 4 is not included!

#for multidimensional array
arr2=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=int)
print ("The second and third row of arr2 is: "+str(arr2[1:]))

# print column
print ("The second column of arr2 is "+str(arr2[..., 1]))
# when indexing multiple columns, it would come out with an actual form of matrix
print ("The last two column of arr2 is "+str(arr2[..., 1:]))
