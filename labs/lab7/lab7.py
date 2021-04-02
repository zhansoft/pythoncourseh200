# Recursion == unbounded
# tail end recursion: faster
# yield --> function into a generator function (does one computation and then returns that)

# # generator example
# def f():
#     i = 0
#     while True:
#         yield i
#         i += 1

# *kwargs (dctionary?)
def su(*args):
    total = 0
    for i in args:
        total += i
    return total # args takes in multiple arguments (unbounded) but not generators or dictionaries

a = su(1,2,3,4, 5)
b = su(*[1,2,3,4,5]) # when you have a list as input you can unpack the list with a star *
# print(a)
# print(b)

# generator; does not create it all at once
s = sum(x * 3 for x in range(3))
# print(s)

# list comprehension; creates it all as one because it builds that entire list and then passes it as one
l = sum([x * 3 for x in range(18) if x % 2 == 1])
# print(l)

# dir() = shows all attributes of object given like within a list
# __iter__: only iterable objects have this

def length(cont):
    """
    Recursively returns the length of the cont
    """
    if not cont:
        return 0
    else:
        return 1 + length(cont[1:])

print(length("abcd"))

def removePos(x, cont):
    """
    Recursively removes an item from the list "cont" that is at "x".
    Returns a list of all items from "cont" that are not were not at the "x" position

    Example: removePos(1, ['a', 'b', 'c']) ---> ['a', 'c']
    """
    if not cont:
        return []
    else:
        if x:
            return [cont[0]] + removePos(x-1, cont[1:])
        else:
            return [] + removePos(x-1, cont[1:])

print(removePos(1, ['a', 'b', 'c', 'd']))

def sum20list(mat):
    """
    Recursively go through and sum all the valeus from each row and 
    add the result of each row together to get a final value
    """
    if not mat:
        return 0
    else:
        total = 0
        for i in range(len(mat[0])):
            total += mat[0][i]
        return total + sum20list(mat[1:])

x = [[1,2,3], [4,5,6], [7, 8, 9]]
print(sum20list(x))
            

