import math

# INPUT FUNCTION fn, start is a, end is b,
# n is an even number of integrals

# RETURN approximate area under the curve
def simpson(fn, a, b, n):
    delta_x = (b-a)/n
    interval = lambda i: a + i*delta_x
    interval_values = []
    for i in range(n+1):
        if i == 0 or i == n:
            interval_values += [fn(interval(i))]
        elif i % 2 == 1:
            interval_values += [4*fn(interval(i))]
        elif i % 2 == 0:
            interval_values += [2*fn(interval(i))]
    def sumInterval(lst):
        sum = 0
        for i in interval_values:
            sum += i
        return sum
    area = sumInterval(interval_values)*(b-a)/(3*n)
    return area

def convert(x):
    if x.isnumeric():
        return float(x)
    else:
        return eval(x)

with open("Assignment8/integralfile.txt", "r") as xfile:
    xlines = [d.split(",") for d in xfile.read().split("\n")]

for i in xlines:
    body = i[0]
    fn = eval("lambda x: " + body)
    a = convert(i[1])
    b = convert(i[2])
    n = convert(i[3])
    answer = convert(i[4])
    integration = simpson(fn, a, b, n)
    error = abs((answer - integration)/answer)
    print("f(x) = {0} over [{1}, {2}] is {3:.3f}".format(body, a, b, integration))
    print("Actual answer is {0:.3f}".format(answer))
    print("error is {0:.3f}".format(error))
