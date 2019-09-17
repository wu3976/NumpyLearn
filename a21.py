import numpy as np
 # ndarray object can be stored and load in the disk files

#save in .npy format
a=np.array([1, 2, 3, 4, 5], dtype=int, order='C')
np.save("array_a", a)

#load .npy file
b=np.load("array_a.npy")
print(b)

# save and load in .txt format
a2=np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt("array_a.txt", a2)
c=np.loadtxt("array_a.txt")
print(c)