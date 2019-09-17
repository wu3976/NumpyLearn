from matplotlib import pyplot as pl
import numpy as np

# matplotlib: plotting graph

# firstly, define a range of x and y
x=np.arange(9)
y=2*np.power(x, 2)+3
x2=np.arange(0, 4*np.pi, 0.01)
sinx2=np.sin(x2)
# then, first write title, xlabel, ..
pl.title("Matplotlib")
pl.xlabel("x")
pl.ylabel("y")

#plot!
pl.subplot(2, 1, 1) # like matlab
pl.plot(x, y, "o--b") # o: circle marker; --: dash line; b: blue
pl.subplot(2, 1, 2)
pl.plot(x2, sinx2, "r")
pl.show()
