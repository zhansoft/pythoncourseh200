#need mathematical constants
import math

#Get radius (it's a string)
#Input allows you to type information into  the computer -- it's always as a 
#string.
#so you must convert the type to integer if that's what you need
diameter = input("Enter the radius of the circle: ")

#change string type to integer type
radius = int(diameter)/2

#to print the value, we convert it back to string
print("The area of a circle is "+ str(4 * (radius ** 2) * math.pi))



