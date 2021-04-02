import math
# Task 1: Finish the following four functions

def maxThree(x, y, z):
    """
    Returns the maximum of the three parameters
    """
    # TODO implement this function
    #logically there can only be xyz xzy yxz yzx zxy zyx (greatest to least) or if two variables equal each other just return that
    # 1 2 3
    if x >= y and x >= z:
        return x
    elif y >= z and y >= x:
        return y
    else:
        return z
            

    
def minThree(p1, p2, p3):
    """
    Returns the minimum of the three parameters
    """
    # TODO implement this function
    if p1 <= p2 and p1 <= p3:
        return p1
    elif p2 <= p3 and p2 <= p1:
        return p2
    else:
        return p3

    
def maxTwoSum(tomato, potato, idaho):
    """
    Returns the sum of the largest two parameters
    """
    # TODO implement this function
    if tomato >= potato and tomato >= idaho:
        if potato >= idaho:
            return tomato + potato
        else:
            return tomato + idaho
    elif potato >= idaho and potato >= tomato:
        if idaho >= tomato:
            return potato + idaho
        else:
            return potato + tomato
    elif idaho >= potato and idaho >= tomato:
        if potato >= tomato:
            return idaho + potato
        else:
            return idaho + tomato



    

def minTwoSum(x, y, z):
    """
    Returns the sum of the smallest two values
    """
    # TODO implement this function
    if x <= y and x <= z:
        if y <= z:
            return x + y
        else:
            return x + z
    elif y <= x and y <= z:
        if x <= z:
            return y + x
        else:
            return y + z
    elif z <= x and z <= y:
        if x <= y:
            return z + x
        else:
            return z + y
    
    
    
# Task 2: Writing more functions

def circleArea(d):

    
    """
    Implement the code in the circle.py listing from Problem 2 of Assignment 1 
    as a function named circleArea that takes in the diameter of a circle and returns the area
    """
    # TODO implement this function
    radius = int(d)/2
    circleArea = math.pi * radius ** 2
    return circleArea
    
    
def areaDifference_rect(l1, w1, l2, w2):
    """
    This function takes in the lengths and widths of two different rectangles
    and returns the difference between their two areas
    """
    areaRectangle1 = l1 * w1
    areaRectangle2 = l2 * w2
    areaDifference = abs(areaRectangle1 - areaRectangle2)
    return areaDifference
    #I just made it absolute value so it'd be a positive number and pretty.
    # TODO implement this function
    
    
def areaDifference_circle(d1,d2):
    """
    This function takes in the diameters of two circles and returns    the difference
    between their two areas. Hint: this function can make use of the circleArea function
    """
    # TODO implement this function
    areaCircle1 = circleArea(d1)
    areaCircle2 = circleArea(d2)
    areaDifference = abs(areaCircle1 - areaCircle2)
    return areaDifference
    #I just made it absolute value so it'd be a positive number and pretty.


if __name__ == "__main__":
    pass
    #  TODO: Fill me in
    print(maxThree(1,2,3))
    print()
    print(minThree(2,3,1))
    print()
    print(maxTwoSum(3,3,9))
    print(maxTwoSum(3,2,9))
    print(maxTwoSum(0,0,0))
    print()
    print(minTwoSum(10,2,1))
    print(minTwoSum(2,3,1))
    print(minTwoSum(2,1,100))
    print(minTwoSum(2,1,1))
    print()
    print(circleArea(2))
    print()
    print(areaDifference_rect(2,2,3,3))
    print()
    print(areaDifference_circle(2,3))
    #we're gonna do this again
    