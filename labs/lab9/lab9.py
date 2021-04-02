### This lab assignment will be done in "Labs/Lab9/lab9.py"
### Generators
import random as rn
            
def diceRolls(diceList):
    """
    Given a list of tuples, where each tuple is structured as:
    (size of dice, number of rolls)
    Where the "size of the dice" is rolled that many times in a row. 
    Each call to the generator produces a single value. 
    You will need to use a certain function from the 
    `random` module. 
    ---------------------------------------------------------------------------
    Example:
    >>> tuples = [(20, 4), (6, 3)]
    >>> print([i for i in diceRolls(tuples)])
    [13, 17, 18, 17, 5, 6, 1] 
    # Note that this will be a different list because of random
    """

    def roll_gen(x):
        while True:
            x1 = rn.randint(1, x + 1)
            yield x1
        
    rolled_lst = []
    for i in diceList:
        x2 = roll_gen(i[0])
        for x in range(i[1]):
            rolled_lst += [next(x2)]
    return rolled_lst
### List Comprehension

"""
All list comprehensions must be written as one expression. 
While coding them, it is alright to test with multiple lines, 
but when finalizing your solution for a problem, condense it 
into one expression.
"""
def splitCharacters(word):
    """
    Given a single word, split up each character into it's own element within a list. 
    Extra challege, you cannot keep spaces (' ' (ignore quotes)).
    """
    return [c for c in word if ord(c) != 32 ]

def oddNumbers():
    """
    Return a list of all odd numbers less than 50
    """
    return [i for i in range(50) if i %2 == 1]

def dictionaryProblem(d):
    """
    Given a dictionary, where each key is a string and a value is a number, 
    create a dictionary with all keys and their associated value that have a 
    value over 1
    """
    return {char: int(val) for char, val in zip(d.keys(), d.values()) if val > 1}
### Memoized
def fibMemo(n):
    """
    Given the nth fibonacci number, calculate the value. 
    Do this with memoization (determine where to put the dictionary)
    Fib(0) = 0
    Fib(1) = 1
    Fib(2) = 1
    Fib(3) = 2
    ...
    Fib(11) = 89
    
    F(n) = F(n-1) + F(n - 2)
    """
    d= {0: 0, 1: 1}
    if n in d.keys():
        return d[n]
    else:
        for i in range(2, n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]
### Test code
if __name__ == "__main__":
    # test diceRolls
    tuple_d = [(10, 2), (3, 3), (15, 2)]
    print([i for i in diceRolls(tuple_d)])

    # test splitCharacters
    print(splitCharacters("hello darkness my old friend"))

    # test oddNumbers
    print(oddNumbers())

    # test dictionaryProblem
    d = {"i": 2, "am": 3, "so": 1, "very": 0, "tired": 10000}
    print(dictionaryProblem(d))

    # test fib
    print([fibMemo(i) for i in range(12)])

    pass