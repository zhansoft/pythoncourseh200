import math

def min(x, y):
    return x*(x<y) + y*(y<=x)

# recursively
def MIN(lst):
    def max(x, y):
        return x*(x>y) + y*(y>= x)
    if len(lst) == 1:
        return min(lst[0], lst[0])
    elif len(lst) == 2:
        return min(lst[0], lst[1])
    else:
        lst.remove(max(lst[0], lst[1]))
        return MIN(lst)

# for-loop and index into list
def min1(x):
    smallnum = x[0]
    for i in range(1, len(x)):
        if smallnum > x[i]:
            smallnum = x[i]
    return smallnum

# for-loop and container
def min2(x):
    smallnum = x[0]
    for i in x:
        if i < smallnum:
            smallnum = i
    return smallnum


# while-loop and index into list
def min3(x):
    index = 0
    smallnum = 100000000000000000000
    while index < len(x):
        if x[index] < smallnum:
            smallnum = x[index]
        index += 1
    return smallnum


# while-loop and container
def min4(x):
    smallnum = 100000000000000000000
    while x:
        for i in range(len(x)-1, -1, -1):
            if smallnum > x[i]:
                smallnum = x[i]
        x = x[1:]
    # for loop reverse index
    return smallnum

def min5(x):
    small = x[-1]
    for i in range(len(x)-1, -1, -1):
        if x[i] < small:
            small = x[i]
    return small

if __name__ == "__main__":
    x = [1, 42, -1, 22, 0, 12]
    # mf = [MIN, min1, min2, min3, min4, min5]
    mf = [MIN, min1, min2, min3, min4, min5]

    for f in mf:
        print("{0}({1}) = {2}".format(f.__name__,x,f(x)))