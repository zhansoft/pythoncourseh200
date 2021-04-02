# DATA makes strings easier to type
Ap, Bp, Op, ABp = "A+", "B+", "O+", "AB+"
An, Bn, On, ABn = "A-", "B-", "O-", "AB-"

#sophia zhang

# INPUT Blood types x can receive from y
# OUTPUT Boolean
def receiveFrom(x, y):
    # TO DO: IMPLEMENT CODE
    if (x == Ap):
            return y == Ap or y == An or y == Op or y == On
    elif (x == Bp):
            return y == Bp or y == Bn or y == Op or y == On
    elif (x == ABp):
        return True
    elif (x == On):
        return y == On
    elif (x == Op):
        return y == Op or y == On
    elif (x == An):
        return y == An or y == On
    elif (x == Bn):
        return y == Bn or y == On
    elif (x == ABn):
        return y == ABn or y == An or y == Bn or y == On

# INPUT Blood types x can donate to y
# OUTPUT Boolean
def donateTo(x, y):
# TO DO: IMPLEMENT CODE
    if (x == Ap):
        return y == Ap or y == Bp
    elif (x == Bp):
        return y == Bp or y == ABp
    elif (x == ABp):
        return y == ABp
    elif (x == On):
        return True
    elif (x == Op):
        return y == Op or y == Ap or y == Bp or y == ABp
    elif (x == An):
        return y == An or y == Ap or y == ABn or y == ABp
    elif (x == Bn):
        return y == Bn or y == Bp or y == ABn or y == ABp
    elif (x == ABn):
        return y == ABn or y == ABp

x = [Ap, Bp, Op, ABp, An, Bn, On, ABn]

for i in x:
    print(i, " donate to ", end = "")
    for j in x:
        if donateTo(i, j):
            print(j, " ", end = "")
    print()

print()
for i in x:
    print(i, " receive from ", end = "")
    for j in x:
        if receiveFrom(i, j):
            print(j, " ", end = "")
    print()

__name__ == "__main__"

        