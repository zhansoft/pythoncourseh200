def lr(xlst):
    # TO DO: IMPLEMENT
    longest = 0
    tmpcount = 0
    while xlst:
        if xlst[0] == 1:
            tmpcount += 1
            if tmpcount > longest:
                longest = tmpcount
        elif xlst[0] == 0:
            if tmpcount > longest:
                longest = tmpcount
            tmpcount = 0
        xlst = xlst[1:]
    return longest

x = [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0]
print(lr(x))

a = [1,1,1,1,1,1,1,1,1]
print(lr(a))

b = [0]
print(lr(b))