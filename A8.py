import numpy as np
# iterator can functions on mutual broadcasting matrices.

arr=np.arange(0, 60, 5)
arr=arr.reshape(3, 4)

b=np.array([1, 2, 3, 4], dtype=int)

print("First array is: "+str(arr))
print("Second array is: "+str(b))

for x, y in np.nditer([arr, b]):
    print(str(x)+":"+str(y), end=" ")


