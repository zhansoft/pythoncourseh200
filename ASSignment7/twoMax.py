import random as rn

def twoMax(xlst):
    def mymax(x, y):
        if x > y:
            return x
        else:
            return y
    # to do: finish the function
    if not xlst:
        return []
    elif (len(xlst[0]) == 1):
        return xlst[0]
    else:
        return [mymax(xlst[0][0], xlst[0][1])] + twoMax(xlst[1:])


# TO DO: Implement Recursive Function
if __name__ == "__main__":
    testlst = rn.randint(0, 10)
    lst = []
    while testlst:
        lst.append([rn.randint(0, 20), rn.randint(0, 20)])
        testlst -= 1
    print(lst)
    answer = twoMax(lst)
    print(answer)