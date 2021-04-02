import math as m

# Input Parameter: dollar amount x
# Return Value: list of quarters, dimes, nickels and pennies

def dollars(x):
    #ye
    q, d, n, p = .25, .1, .05, .01
    coinage = [0,0,0,0] #quarters dimes nickles pennies
    coinage[0] += m.trunc(x/q)
    x -= q*coinage[0]
    if (x /d) >= 0:
        coinage [1] += m.trunc(x/.1)
        x -= d * coinage[1]
    if (x / n) >= 0:
        coinage[2] += m.trunc(x/.05)
        x-= n*coinage[2]
    if (x/ p) >= 0:
        coinage[3] += m.trunc(x/.01)
        x -= p * coinage[3]
    return coinage


print(dollars(2.24))
print(dollars(1.19))
print(dollars(4.16)


if __name__ == "__main__":
    pass