def div_9(n):
    # TO DO

    def listOfN(n):
        n = str(n)
        lst = []
        for i in n:
            lst += i
        return lst
    
    tmpList = listOfN(n)
    sumNine = 0
    for i in tmpList:
        sumNine += int(i)
        if sumNine > 9:
            sumNine -= 9
    return sumNine == 9 or sumNine == 0
    

x = [99, 0, 18273645, 22]
for i in x:
    print(div_9(i))

y = 10
print(div_9(y))