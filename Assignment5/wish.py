def is_magic(ms):
    # TO DO:
    magicsquare = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    seemsMagic = True
    for x in range(len(ms)):
        for y in range(len(ms[x])):
            if magicsquare[x][y] == ms[x][y]:
                seemsMagic = True
            else:
                seemsMagic = False
                print("This is NOT a magic Square...hide")
                break
    if seemsMagic:
        print("This is a magic Square.")


ms = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

is_magic(ms)

ms = [[4, 9, 2], [3, 5, 7], [8, 2, 6]]

is_magic(ms)
