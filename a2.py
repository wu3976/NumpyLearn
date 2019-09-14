import numpy as np

# asarray: can convert anything to array, including tuples, tuple of tuples, ...
arr=np.asarray(((1, 2), (3, 4)), dtype=int)
print ("arr="+str(arr))

# in this situation, the tuple would not be dissolved:
arr2=np.asarray([(1, 2, 3), (4, 6)])
print ("arr2="+str(arr2))

#arr3=np.frombuffer("Hello, world!", dtype='S1')
#print("arr3 = "+str(arr3))

list=range(5)
it=iter(list) # create an iterable object

# fromiter: create the np array list from iterable object
arr4=np.fromiter(it, dtype='f', count=-1)
print("arr4="+str(arr4))