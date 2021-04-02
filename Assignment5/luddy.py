import numpy as np

def area(x, y):
    # TO DO:
    return x * y == 75 # returns a bool?


def f(x, y):
    # TO DO:
    price =  (10 * x * 2) + (10 * y) + (y * 5)
    return price # in dollars/ft


# MARVELOUS BRUTE FORCE EW
minimum = 100000
for x in np.arange(0, 100, .25):
    for y in np.arange(0, 100, .25):
        if (f(x,y) < minimum and area(x,y)):
            minimum = f(x,y)
            ax = x
            by = y 

print(ax, by, f(ax, by)) 