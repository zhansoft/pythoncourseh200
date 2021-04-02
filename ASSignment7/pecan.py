appr = 355/113

def mypi():
    # to do: implement yield
    num = 0
    iterator = 1
    counter = 0
    while True:
        if counter % 2 == 0:
            counter += 1
            num += 4/iterator
        else:
            counter += 1
            num -= 4/iterator
        yield num
        iterator += 2

cnt = 0
x1 = mypi()
z = next(x1)
while abs(z-appr)/appr > 0.0001:
    z = next(x1)
    cnt += 1

print(cnt, z)