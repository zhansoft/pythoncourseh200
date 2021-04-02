#lab 3
# for lists just use the + operator to combine two do NOTTTTTT append
# also len() returns the length of a list
# float division = /
# integer division = //

#Function 1
def factorial(n):
    #3! = 3 * 2 * 1
    answer = 1
    for i in range(n):
        answer = (i + 1) * answer
    return answer


#Function 2
def numberOfA(s):
    count = 0
    for i in s:
        if i == 'a' or i == 'A':
            count += 1
    return count

# Function 3
def mul(a, b):
    # a = first number & b = second number
    answer = 0
    for i in range(b):
        answer = answer + a
    return answer

# Function 5
def mod(a, b):
    remainder = a
    for i in range(div(a,b)):
        remainder = remainder - b
        if remainder < b:
            return remainder

# Function 4
def div(a, b):
    # a = first number & b = second number
    counter = 0
    answer = a
    for i in range(a):
        answer = answer - b
        if answer > 0:
            counter += 1
        elif answer == 0:
            counter += 1
            break
    return counter

