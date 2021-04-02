import math

def hex_dec(hex):
    # To Do
    hex_alphabet = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    base_index = {}

    index_char = len(hex) - 1
    for i in range(len(hex)):
        base_index[hex[i]] = index_char
        index_char -= 1
    
    print(base_index)

    sum = 0
    for x in base_index.keys():
        print(x)
        sum += (hex_alphabet[x] *math.pow(16, base_index[x]))
    return sum

if __name__ == "__main__":
    hex = input("Hex: ")
    print(hex_dec(hex))