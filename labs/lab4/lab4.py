# Lab 4
# Fall 2019 C200 / H200

"""
Below, finish the dictionary. Each key is a side of a die (1 - 6), and the 
value is the opposite side of the die. The opposite side of a 
dice always adds up to 7
"""

import random as r

dice_dict = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}


def twisted_die_roll():
    """
    Function that generates a random roll 1 - 6, and 
    uses previously defined dictionary to return the opposite side.
    If 1 was generated, return 6. 
    To understand Random, take a moment to read through the link to find what specific 
    function from the MODULE `random`.
    https://docs.python.org/3/library/random.html
    """
    randomroll = r.randint(1,6)
    returnvalue = dice_dict[randomroll]
    return returnvalue

def twisted_dice_rolls(n):
    """
    Function that uses a for loop to generate `n` twisted die rolls. 
    (You must use a previous function you made) and store them in a 
    list. Return the list
    """
    rlst = []
    for i in range(n):
        currRoll = [twisted_die_roll()]
        rlst += currRoll
    return rlst

def stats_twisted_rolls_list(n):
    """
    Generate `n` twisted die rolls (either a for loop or using a previous function) and 
    determine the roll statitics (how many times a 1, 2, ... 6 was rolled) in a list. 
    Print the list AND return the list. 
    Hint: how can we keep track of the statistics since we only have an ordered list and 
    what ever number we just rolled
    """
    nRolls = twisted_dice_rolls(n)
    nsRolls = nRolls[:]
    stats = [0,0,0,0,0,0]
    while nsRolls:
        num = nsRolls[0] 
        stats[num - 1] += 1
        nsRolls = nsRolls[1:]
    listOfStats = stats
    print("The List:", listOfStats)
    return listOfStats


def stats_twisted_rolls_dictionary(n):
    """
    Generate `n` twisted die rolls (either a for loop or using a previous function) and determine
    the roll statistics (how many times a 1, 2, ... 6 was rolled) in a DICTIONARY. 
    Print the dictionary AND return the dictionary. 
    You cannot call `stats_twisted_rolls_list` in this function. 
    """
    nRolls = twisted_dice_rolls(n)
    nsRolls = nRolls[:]
    oneStat, twoStat, threeStat, fourStat, fiveStat, sixStat = 0,0,0,0,0,0
    while nsRolls:
        if (nsRolls[0] == 1):
            oneStat +=1
        elif (nsRolls[0] == 2):
            twoStat += 1
        elif (nsRolls[0] == 3):
            threeStat += 1
        elif (nsRolls[0] == 4):
            fourStat += 1
        elif (nsRolls[0] == 5):
            fiveStat += 1
        elif (nsRolls[0] == 6):
            sixStat += 1
        nsRolls = nsRolls[1:]
    dictOfStats = {1: oneStat, 2:twoStat, 3: threeStat, 4: fourStat, 5: fiveStat, 6:sixStat}
    print("The Dictionary: ", dictOfStats)
    return dictOfStats


def sumOfOddNumbers(listOfNums):
    """
    Using a while loop, find the odd numbers and add them up.
    """
    sumOdd = 0
    while listOfNums:
        if (listOfNums[0] % 2 == 1):
            sumOdd += listOfNums[0]
        listOfNums = listOfNums[1:]
    return sumOdd

def getFirstHalfOfString(string):
    """
    Using a loop, get the characters from the first half of the string
    Note: You can't use slicing, you can use indexing
    """
    halfLength = int(len(string) / 2)
    newString = ""
    for i in range(halfLength):
        newString += string[i]
    return newString

def getSecondHalfOfString(string):
    """
    Get the second half of the string.
    You must only use slicing (plus a couple of other functions) to get the
    second half of the string
    """
    halfPoint = int(len(string)/2)
    secondHalf = string[halfPoint:]
    return secondHalf


def main():
    """
    TODO: Fill in tests for each of the above functions.
    """
    
    ### Fill in tests for dice roll
    print(twisted_die_roll())
    print(twisted_dice_rolls(3))
    print(stats_twisted_rolls_list(3))
    print(stats_twisted_rolls_dictionary(5))
    print(sumOfOddNumbers([0,2,3,4,5]))
    print(getFirstHalfOfString("tigerwoods"))
    print(getSecondHalfOfString("tigerwoods"))
    print(getSecondHalfOfString("cat"))


    ### Fill in tests for remaining functions
    # TODO




if __name__ == "__main__":
    main()