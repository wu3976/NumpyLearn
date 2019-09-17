import numpy as np

# np.id returns the unique identification of an object
arr=np.arange(0, 10, 1, dtype=int)
arr2=arr
print (str(id(arr))+" "+str(id(arr2)))

#ndarray.view() shallow copy
print(arr)
arr3=arr.view()
print(id(arr), end=" ")
print(id(arr3)) # id is different
arr=np.reshape(arr, [5, 2])
print(str(arr)+" "+str(arr3)) # shape don't change
arr[0, 0]=100
print(str(arr)+" "+str(arr3)) # because it is shallow copy, the value in arr3 also changed

# ndarray.copy() deep copy
print("-----------------------------")
arr4=arr.copy()
arr=np.reshape(arr, [2, 5])
print (str(arr)+"\n"+str(arr4)) # shape don't change
arr[0, 1]=100
print (str(arr)+"\n"+str(arr4)) # value don't change