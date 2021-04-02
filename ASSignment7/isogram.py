def is_isogram(xword):
    dict_char = {}
    for i in xword:
        if i not in dict_char.keys():
            dict_char[i] = 0

    for x in dict_char.keys():
        for y in xword:
            if y == x:
                dict_char[x] += 1
    
    boolExp = True
    for z in dict_char.values():
        if z > 1:
            boolExp = False
    
    return boolExp
    




if __name__ == "__main__":
    word = ["dermatoglyphics", "palindrome", "anagram"]

    for w in word:
        print(is_isogram(w))