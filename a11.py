import numpy as np

#numpy.str class
str=np.str("Hahaha dick!")
print (str)

# numpy.char.add
arr=np.array(["Jack", "dick"], dtype=np.str, order='C')
# print(arr)
arr2=np.array(["Hello, ", "Hi, "], dtype=np.str)
# print(arr2)
arr_all=np.char.add(arr2, arr)
print(arr_all)

#numpy.char.multiply
arr3=["aa ", "bb "]
arr_all2=np.char.multiply(arr3, 3)
print(arr_all2)