def sq(n):
    # TO DO:
    if n <= 2:
        for i in range(n):
            str = ""
            for x in range(n):
                str += "*"
            print(str)
    elif n > 2:
        for i in range(n):
            str = ""
            for x in range(0, n):
                if (i == 0 or i == (n-1)):
                    str += "*"
                elif (i > 0 or i < (n-1)):
                    if (x == 0 or x == (n-1)):
                        str += "*"
                    elif (x > 0 or x < (n-1)):
                        str += " "
            print(str)


sq(1)
print()
sq(2)
print()
sq(5)
print()
sq(6)