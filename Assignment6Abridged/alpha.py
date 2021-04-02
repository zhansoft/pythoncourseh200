d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
    'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
# marvelous code lmao

with open("/Users/sophiazhang/Documents/iu undergrad/freshman iu/sem i/csci h-200/H200-Assignments-zhanso/Assignment6Abridged/happy.txt", "r") as book:
    all_lines = book.read().splitlines()
#print(all_lines)

splitlst = []

for i in all_lines:
    splitlst += [i.split(" ")]
#print(splitlst)

# for k in d:
#     tmplst = splitlst[:]
#     while tmplst:
#         for word in tmplst[0]:
#             for char in word:
#                 if char == k:
#                     d[k] += 1
#         tmplst = tmplst[1:]
# this is stupidhead code right here.

tmplst = splitlst[:]

for k in d:
    for line in tmplst:
        for word in line:
            for char in word:
                if char == k:
                    d[k] += 1

print(d)


if __name__ == "__main__":
    pass
