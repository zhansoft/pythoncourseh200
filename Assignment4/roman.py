# Hint Code
# def roman(number):
#     one = "1"
#     five = "V"
#     romanNumber = (number <= 3)*number*one + (number == 4)*(one + five) + (number == 5)*five
#     print("{0:<4} {1: <4}".format(number, romanNumber))

# Input Paramter: a decimal value n
# Return Value: a string containing the Roman numeral representation of n

def roman(n):
    # TO DO: Implement this function
    multiples_10 = {1: "1", 5: "V", 10: "X", 50: "L", 100: "C"}

    def roman1_6(n):
        one = "1"
        five = "V"
        romanNumber = (n%10 <= 3)*one*(n%10) + (n%10 == 4)*(one+five) + (n%10 == 5)*five
        return romanNumber
    
    def roman6_10(n):
        one = "1"
        five = "V"
        rN = (n%10 >= 6 and n%10 <= 8)*five + (n%10 >= 6 and n%10 <= 8)*one*(n%10-5) + (n%10 ==9)*(one+multiples_10[10])
        # rN = ""
        # if (n%10 >= 6 and n%10 <= 8):
        #     one = one * (n%10 - 5)
        #     rN = five + one
        # elif (n%10 == 9):
        #     rN = one + multiples_10[10]
        #romanNumber = (n < 9)*five + (n <= 8)*one*(n) + (n == 9)(one + multiples_10[10])
        return rN

    def roman10multiples(n):
        #return = (n//10 >= 1 or n//10 <= 3)*(n//10)*(multiples_10[10]) + (n//10 == 4)*(multiples_10[10] + multiples_10[50]) + (n//10 >= 5 or n//10 <= 8)*(multiples_10[50] + (multiples_10[10] * (n//10))) + (n//10 == 9)*(multiples_10[10]+multiples_10[100]) + (n // 100 == 1)*multiples_10[100]
        #rN = (n//10 >= 1 and n//10 <= 3)*multiples_10[10]*(n//10) + (n//10 == 4)*(multiples_10[10] + multiples_10[50]) + (n//10 >= 5 and n//10 <= 8)*multiples_10[50] + (n//10 >= 5 and n//10 <= 8)*multiples_10[10]*(n//10) + (n//10 == 9)*(multiples_10[10] + multiples_10[100]) + (n//10 == 10)(multiples_10[100])
        rN = ""
        if (n//10 >= 1 and n//10 <= 3):
            rN += multiples_10[10] * (n//10)
        elif (n//10 == 4):
            rN += (multiples_10[10] + multiples_10[50])
        elif (n//10 >= 5 and n//10 <= 8):
            rN += (multiples_10[50] + multiples_10[10]*(n//10 - 5))
        elif(n//10 == 9):
            rN += (multiples_10[10] + multiples_10[100])
        elif (n//10 == 10):
            rN += multiples_10[100]
        return rN


    
    return roman10multiples(n) + roman1_6(n) + roman6_10(n)


for i in range(1, 101):
    if i % 5 == 0:
        print()
    print(i, roman(i), ", ", end ="")
