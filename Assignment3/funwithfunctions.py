import math


#1 
def y(d,r,t):
#TO DO: IMPLEMENT FUNCTION
    final = d * math.exp(r * t)
    return final

#2
def N(n_0, m, t):
#TO DO: IMPLEMENT FUNCTION
    size = n_0 * math.exp(m*t)
    return size

#3
def N_t(t):
#TO DO: IMPLEMENT FUNCTION
    numberTeeth = 71.8 * math.exp(-8.96*math.exp(-0.0685*t))
    return numberTeeth

#4
def K(t):
#TO DO: IMPLEMENT FUNCTION
    concentration = (9*t/2.6)/(2*(t**2) + 3)
    return concentration

#5
def r(t):
#TO DO: IMPLEMENT FUNCTION
    rent = 1.5207*t**4 - 19.166*t**3 + 62.91*t**2 + 6.0726*t + 1026
    return rent

#6
def p(x):
#TO DO: IMPLEMENT FUNCTION
    profit = 4*x**2 - 100*x -1000
    return profit

#7
def W(P_i,P_f):
#TO DO: IMPLEMENT FUNCTION
    work = 8.314*(300)*math.log(P_i/P_f, math.e)
    return work

#8
def depreciate(c,s,life):
#TO DO: IMPLEMENT FUNCTION
    deductedCost = (c - s)/life
    return deductedCost

#9
def L(k,V,A,C):
#TO DO: IMPLEMENT FUNCTION
    lift = k * (V ** 2) * A * C
    return lift


if __name__=="__main__":
    print(y(1000,.02,10))
    print(N(500,100,4))
    print(math.floor(N_t(1000)))
    print(K(1))
    print(r(4))
    print(p(10))
    print(W(10,1))
    print(depreciate(20000,1000,5))
    print(L(0.0033,33.8,512,0.515))