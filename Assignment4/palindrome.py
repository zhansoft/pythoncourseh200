# Input Parameter: a string x
# Return Value: True if x is a palindrome, False otherwise.

def palindrome(x):
    # Do this shiz
    hp = int(len(x) / 2)
    if len(x) == 1:
        return True
    elif len(x) % 2 == 0:
        reversal = x[:hp-1:-1]
        if x[0:hp] == reversal:
            return True
        else:
            return False
    elif len(x) % 2 == 1:
        reversal = x[:hp:-1]
        if x[0:hp] == reversal:
            return True
        else:
            return False


print(palindrome("aba"))
print(palindrome("a"))
print(palindrome("abba"))
print(palindrome("amanaplanacanalpanama"))
print(palindrome("abca"))
print(palindrome("ac"))
print(palindrome("adabbba"))
print(palindrome("amandaplanacanalpanama"))
