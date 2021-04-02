def occurencesWhile(lst, var):
    # Using a while loop, findt he number of occurences in the list
    # return count
    f = 0 # counter
    i = 0 # iteration number
    while i < len(lst):
        if lst[i] == var:
            f += 1
        i += 1
    return f

def occurencesWhileList(lst, var):
    item = 0
    while lst:
        if lst[0] == var:
            item += 1
        lst = lst[1:]
    return item

def operationList(opsList, opp):
    # Given a  list of lists, where each inner lsit has a size > 0
    # using the operation provide:
    # subtract: s
    # multiply: m
    # addition: a
    # Apply that to a whole list
    resultingList = []
    index1 = 0
    index2 = 0

    while index1 < len(opsList):
        currList = opsList[index1]
        index2 = 0

        if opp == "m":
            currResult = 1 # never will be undefined if defined in both branches
        else:
            currResult = 0

        while index2 < len(currList):
            if opp == "m":
                currResult *= currList[index2]
            elif opp == "a":
                currResult += currList[index2]
            elif opp == "s":
                currResult -= currList[index2]
            index2 += 1
        index1 += 1

        resultingList += [currResult]

    return resultingList

def evenCount2(dictionary):
    # Given a dictionary, count the number of even keys
    count = 0
    for key in dictionary:
        if key % 2 == 0:
            count += 1
    return count



