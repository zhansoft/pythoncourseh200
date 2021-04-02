def sumListFor(aList):
    sum = 0
    for i in aList:
        sum = sum + i
    return sum

a = [1,2,3,4]

def neverGonna(listofWrongDoings):
    # print out "never gonna" + ...
    for doing in listofWrongDoings:
        print("never gonna", doing)

def multiplyListFor(aListing):
    """
    Multiply the numbers in a list together using a for
    """
    product = 1
    for num in aListing:
        product *= num
    return product