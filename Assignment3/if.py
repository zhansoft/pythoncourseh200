x = True
y = False
z = 12
a = 10
b = not (x or not (x or y)) and True #False

#1###################
if (x and y):
    print("Happy")
elif b or x:
    print("Valentines")
else:
    print("day!")
#1###################


#2###################
if (z > a) or (2 * a > z):
    print("C200")
if not (z > a) and not (2 * a > z):
    print("is bliss")
#2###################


#3###################
#if not (not (x and y) or not x):
if x and y:
    print(a)
#3###################


#4###################
if (2 < z) or x:
    print("1")
if 2 == 1:
    print("2")
if (not(2 < z) and not x) and (y and not x):
    print("3")
if not((2 < z) or x) and (not y or x):
    print("4")
#4###################


#5###################
def f(x):
    if (x == 4):
        return 100
    elif (x == 3):
        return 10
    elif (x == 2):
        return 1000
    else:
        return 100000

print(f(4))
print(f(3))
print(f(2))
print(f(1))
#5###################
if __name__ == "__main__":
    pass
