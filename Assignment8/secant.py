f = lambda x: x**6-x-1

def secant(f, x0, x1, tau):
    x2 = x1 - f(x1) * (x1 - x0)/(f(x1)-f(x0))
    print("{0:.5f} {1:.5f} {2:.5f} {3:.5f}".format(x0, f(x0), f(x1), (x0-x1)))
    if abs(f(x2)) < tau:
        return x2
    else:
        return secant(f, x1, x2, tau)
    
    

secant(f, 2.0, 1.0, .0001)