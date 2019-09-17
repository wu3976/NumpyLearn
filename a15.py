import numpy as np

# statistical functions
arr=np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]], dtype=int)
# amax, amin
max=np.amax(arr)
min=np.amin(arr)
print (str(max)+" "+str(min))
# np.percentile
perc=np.percentile(arr, 30)
print(perc)
# mp.median
median=np.median(arr)
print (median)
# more on documents