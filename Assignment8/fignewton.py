f = lambda x: x**6 - x - 1
fp = lambda x: 6*(x**5)-1

def f_eval(f):
    f_lambda = "lambda x: "
    actual_f = eval(f_lambda + f)
    return actual_f

def fpa(f):
    h = .000001
    return lambda x: (f(x+h)-f(x-h))/(2*h)

def newton(f, fp, x, tau, iterations):
    def n(x, i):
        while f(x) > tau:
            print("{0} {1:.5f} {2:.5f}".format(i, x, f(x)))
            x = x - f(x)/fp(x)
            i += 1
            if i > iterations-1:
                print("number of iterations exceeded...")
                break
        return x
    n(x, 0)

newton(f, fp, 1.5, .0001, 20)
print(" ")
newton(f, fpa(f), 1.5, .0001, 5)

if __name__ == "__main__":
    while True:
        f_input = input("Function: ")
        f1 = f_eval(f_input)
        f_derivative = fpa(f1)
        threshold = float(input("tau: "))
        x0 = float(input("x0: "))
        iterations = int(input("iterations: "))
        newton(f1, f_derivative, x0, threshold, iterations)
        cont = input("Press any key to continue: ")
        print(" ")

    pass