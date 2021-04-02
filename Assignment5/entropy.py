import math

def makeProbability(xlst):
    # TO DO
    probList = []
    usedList = []
    for i in range(0, len(xlst)):
        count = 0
        for x in range(0, len(xlst)):
            if xlst[i] == xlst[x]:
                count += 1
        if xlst[i] not in usedList:
            probList += [count/len(xlst)]
        usedList += [xlst[i]]
    return probList

def entropy(xlst):
    # TO DO
    entropySum = 0
    for i in xlst:
        entropySum += (i * math.log2(i))
    return abs(entropySum)


s1 = ['a', 'b', 'a', 'b', 'a', 'b', 'b', 'b']
s2 = [(1), (2), (3), (4)]
s3 = [1]
s4 = [1,2]
xlst = [s1, s2, s3, s4]
for i in xlst:
    print(entropy(makeProbability(i)))