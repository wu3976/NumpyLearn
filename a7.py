import numpy as np

# iterating over np array

# numpy.nditer iterator object
a=np.linspace(0, 60, 12, endpoint=False, dtype=int)
a=a.reshape(3, 4)

print("a="+str(a))
for ele in np.nditer(a):
    print (str(ele))
# the sequence of iteration match array object's layout in the memory.
print("-------------")
b=a.T
for ele in np.nditer(b):
    print(str(ele))

# iterator interates according to the storing order of array
print("-------------")
print("Original: ")
print(a)

c=np.copy(a, order='C')
f=np.copy(a, order='F')
print("-------------")
# iterate in C order
for ele in np.nditer(c):
    print(str(ele)+" ", end="")
print()
# iterate in Fortran order
for ele in np.nditer(f):
    print(str(ele)+" ", end="")
print()

# you can force nditer to iterate in specific order
for ele in np.nditer(c, order='F'):
    print(str(ele)+" ", end="")
print()

# op_flag parameter: 'read', 'write', 'readwrite'
for ele in np.nditer(c, op_flags=['readwrite']):
    print(str(ele)+" ", end="")
print()

# flags parameter: can have values: 'c_index', 'f_index', 'multi-index', 'external_loop'
for ele in np.nditer(c, flags=['external_loop'], order='F'):
    print(str(ele)+" ", end="") # there is a bracket in every jump of "memory interval". If the
    #array is stored in fortran-order, there would not have brackets in the middle
print()

for ele in np.nditer(f, flags=['external_loop'], order='F'):
    print(str(ele)+" ", end="")