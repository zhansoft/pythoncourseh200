# while loops do not terminate if the boolean condition is false until it loops completely

# going over elements in container

container = ["a", "b", "c"]

for i in container:
    print(i)

# going over a number
for i in range(0,1):
    print(i)

# for while loops you need to define it yourself in order to stop/start/step
start = 0
stop = 5
step = 1
i = start
while i < stop:
    print(i)
    i += step


container = ["d", "e", "f"]
for i in container:
    print(i)
# use a fucking while loop instead.

while container: # filled so true; false if empty
    print(container)
    print(container[0])
    container = container[1:] # this removes the first and the last

container = container[::-1] # so it'll make a copy from start to stop and it'll reverse it
print(container)

# keys must be hashable thus if put in a hash function, it should give you the same result

# dictionaries and lists
d = {}
d = {"a": [5,2,6,1], "b": [24,3,5,1]}
d["a"] = 3 # modify a value
d["c"] = "d" # add a key/value
d[4] = 1
d[4] += d["a"]


for i in d: # loops over values and not keys because it'll give you keys if not the d[i] thingy
    print(d[i]) # prints values
    print(i, d[i]) # prints both key and value

for i in d.values(): # again loops over the values
    print(i)

for k, v in d.items():
    print(k, v)

# something about dictionary.pop() which returns the deleted value and del but do not use this...
print(d)
print(d.pop(4))
print(d)