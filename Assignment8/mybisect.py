f= lambda x: x**6 - x -1

def sign(x):
    # TO DO: Implement this function
    if x > 0:
        return 1
    else:
        return -1

def bisect(f, a, b, tau):
    c = (a+b)/2
    print("{0:.5f} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(a, b, c, b-c, f(c)))
    if (b-c) <= tau:
        return c
    elif sign(f(b)) * sign(f(c)) <= 0:
        return bisect(f, c, b, tau)
    else:
        return bisect(f, a, c, tau)
    # TO DO: IMPLEMENT THIS FUNCTION
    # USE THE FOLLOWING PRINT STATEMENT TO DISPLAY THE DATA NICELY

bisect(f, 1.0, 2.0, .001)