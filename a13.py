import numpy as np

# element-wise arithmetic functions:
# add, subtract, multiply, divide

arr=np.arange(0, 9, 1, dtype='f').reshape(3, 3)
print ("First array:\n"+str(arr))
arr2=np.array([10, 10, 10], dtype=int)
print("Second array:\n"+str(arr2))
#broadcasting
divided=np.divide(arr, arr2)
print(divided)

# np.reciprocal()
arr_rec=np.reciprocal(arr) # for element[0, 0], 1/0=inf, an error
print(arr_rec)

#np.power np.mod