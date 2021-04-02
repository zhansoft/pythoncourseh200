import numpy as np
import matplotlib.pyplot as mpl

# a = np.array([1, 2,3,])
# print(a)
# print(type(a))

# b = np.zeros((3,2))
# print(b)

# c = np.full((2,3), 7)
# print(c)


#mpl.plot([x][y][])
mpl.plot([0,15,20,100], [-9,20,100,-15], 'ro')
#mpl.plot(xmin, xmax, ymin, ymax)
mpl.axis([-100, 100, -100, 100])
#to generate it mpl.show()
mpl.show()