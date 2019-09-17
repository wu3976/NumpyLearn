from matplotlib import pyplot as pl
import numpy as np
from numpy import matlib

# plot a bar graph
x=np.array([1, 3, 4])
y=np.array([2, 5, 9])

x2=np.array([2, 5, 6])
y2=np.array([5, 2, 6])
y2=np.asarray(y2)

pl.title("Bar graph")
pl.xlabel("x")
pl.ylabel("y")
pl.bar(x, y, color='g', align='center')
pl.bar(x2, y2, color='k', align='center')
pl.show()