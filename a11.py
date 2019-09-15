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

# np.char.center(arr, width,fillchar)
arr4=np.array(["Hello", "Selina"], dtype=np.str)
b=np.char.center(arr4, 20, fillchar="*")
print(b)

# np.char.split(np.str, sep)
str=np.array(["Dame you!", "Hell no"], dtype=np.str)
sp_str=np.char.split(str, sep=" " )
print(sp_str)

# np.char.encode & np.char.decode
str_enc=np.char.encode(str, 'cp500')
print(str_enc)
str_dec=np.char.decode(str_enc, 'cp500')
print(str_dec)