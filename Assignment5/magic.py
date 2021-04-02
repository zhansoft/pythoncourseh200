# Input value: some number
# Output value: the result of the magical encantation
def magic(x):
    # TO DO:
    magicNum = ((((x + 15) * 3) - 9) / 3) - 12
    return magicNum

if __name__ == "__main__":
    # get input
    x = input("Pick any positive whole number: ")
    
    # change from string to integer
    x = int(x)

    print("Your number was", magic(x))