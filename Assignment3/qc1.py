import numpy as np
import math
import matplotlib.pyplot as plt
# # Example Provided
# def f(x):
#     return 3 * (x ** 2) + 4 * x + 2

# x = -2/3 + math.sqrt(2)/3j
# y = -2/3 - math.sqrt(2)/3j

# print(f(x)) #0j
# print(f(y)) #0j

# INPUT ax**2 + bx + c = 0 coefficients to quadratic
# RETURN tuple(x, y) that are solutions
def q(a, b, c):
    discriminant = ((b**2) - 4*a*c)
    if discriminant < 0:
        print("Complex")
        x = complex((-b/(2*a)), - math.sqrt(-discriminant)/(2*a))
        y = complex((-b/(2*a)),+ math.sqrt(-discriminant)/(2*a))
        #also you can do it w/o complex by
        # x = (-b/(2*a)) - math.sqrt(-discriminant)/(2j*a)
        # y = (-b/(2*a)) + math.sqrt(-discriminant)/(2j*a)
    else:
        print("Not Complex")
        x = (-b - math.sqrt(discriminant)) / (2 * a)
        y = (-b + math.sqrt(discriminant)) / (2 * a)
    return (x, y)

print(q(1, 3, -4))
print(q(2, -4, -3))
print(q(9, 12, 4))
print(q(3, 4, 2))

# Test & fun stuff!
#assigns the two values into x and y
#because this returns a tuple (firstvalue, secondvalue)
x1, y1 = q(1, -2, -4) # x ** 2 - 2 *x - 4 = 0
print(x1, y1)
#creates an anonymous function
#this is the function described above
#You should be intrigued by this assignment
#What is it doing?
f = lambda x: x**2 - 2*x - 4
#the output should be zero
#print(x1 ** 2 - 2*x1 - 4)
print(f(x1), f(y1))

# Plotting Porition
# evenly sampled time at 200ms intervals
x = np.arange(-4.0, 5.0, 0.2)
# Green dashes for line
plt.plot(x, x**2 - 2*x - 4, 'g--')
# Blue dashes fo rline
plt.plot(x, 3*x**2 + 4*x +2, 'b--')
# Draw horizontal line
plt.plot([-4,4], [0,0], color = 'k', linestyle = '-', linewidth=2)
# Plot red dots as solution
plt.plot([x1, y1], [0,0], 'ro')

#if __name__ == "__main__":
    #plt.show()

#Explain (-2 **2) = -4 and (-2)**2 = 4
#Essentially, the power of 2 in the first problem is only being applied to the
#positive two and then the negative is being applied after it's finished computing 4.
#The second problem incorporates the negative value in the exponential thus the output
#is positive.