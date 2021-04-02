import math
import time
# limit of recursion on s(): 999 loops oof
# p(30) takes so damn long. it took 293.017481 seconds apparently wow
 # the answer is... literally n - 1. it's the fibonacci sequence


def s(n):
    if n == 0:
        return 0
    else:
        return n + s(n-1)
def s1(n):
    return (n*(n+1))/2

def p(n):
    if n == 0:
        return 10000
    else:
        return p(n-1) + 0.02*p(n-1)

def p1(n):
    return math.pow(1.02, n) * 10000


def b(n):
    if n == 0:
        return 1
    elif (n == 1):
        return 2
    elif (n == 2):
        return 3
    else:
        return b(n-1) + b(n-2)


def c(n):
    if n == 0:
        return 1
    else:
        return 9 * c(n-1) + math.pow(10, n-1) - c(n-1)

def d(n):
    if n == 0:
        return 1
    else:
        return 3*d(n-1) + 1
def d1(n):
    return (math.pow(3, n+1)-1)/2

def B(n):
    if n == 0:
        return 1
    else:
        return (-1/(1+n)*(c18(B(n-1),0)))

def c18(n, k):
    if (n == 1 or k == 0):
        return 1
    elif (n == k):
        return 1
    else:
        return c18(n-1, k) + c18(n-1, k-1)

if __name__ == "__main__":
    
    #test for s(n)/s1(n)
    for i in range(11):
        print("s(n) ", s(i))
        print("s1(n) ", s1(i))
    print(" ")
    # I hit the limit at 999 loop throughs.

    for i in range(11):
        print("p(n) ", p(i), i)
        print("p1(n) ", p1(i), i)
    print(" ") #i tried to do p(30) but it didn't finish i guess idk...

    for i in range(11):
        print("b(n) ", b(i))
    print(" ") # the answer is... literally n - 1.

    for i in range(11):
        print("c(n) ", c(i))
    print(" ")

    for i in range(11):
        print("d(n) ", d(i))
        print("d1(n) ", d1(i))
    print(" ")

    for i in range(1, 10):
        for x in range(1, 5):
            print("c18(n, k)", c18(i,x), i, x)

    for i in range(11):
        print("B(n) ", B(i))

    # time_start = time.clock()
    # p(30)
    # time_elapsed = (time.clock() - time_start)
    # print(time_elapsed)

    pass