from random import sample

f = open("labs/lab5/storage.txt", "w")
randList = sample(range(0, 100), 10)
for i in randList:
    f.write(str(i) + "\n")
f.close()
print("*" * 30)

z = open("labs/lab5/storage.txt", "r")
print("old tings")
print(z.read())
z.close()

a = open("labs/lab5/storage.txt", "r")
b = a.read().split("\n")
totalScore = 0
for i in b:
    if i:
        totalScore += int(i)
a.close()
# if you read before then you can't do it because it'll go to the end it's line by line you were right earlier

x = open("labs/lab5/storage.txt", "a")
x.write(str(totalScore))
x.close()

y = open("labs/lab5/storage.txt", "r")
print("new tingz")
print(y.read())
y.close()

