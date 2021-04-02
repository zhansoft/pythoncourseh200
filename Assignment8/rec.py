#TIMER FUNCTION -- deprecated in 3.8 FYI
#so you might get messages -- you can ignore them for now
import time

def ftimer(f,args):
    time_start = time.clock()
    f(args)
    time_elapsed2 = (time.clock()-time_start)
    return time_elapsed2

#1
def even(x):
     #TO DO: IMPLEMENT
     return x % 2 == 0

#2
def odd(x):
     #TO DO:IMPLEMENT
     return x % 2 == 1

#3
#Recursive
#INPUT n
#OUTPUT RE value
def b(n):
     #TO DO: IMPLEMENT
     if n == 1 or n == 2:
          return 0
     elif even(n):
          return n - 1 + b(n-1)
     else:
          return n**2 + 1 + b(n-1)

#4
#TAIL RECURSIVE FOR 3
def btr(n,s):
     #TO DO: IMPLEMENT
     if n == 1 or n == 2:
          return s
     elif even(n):
          return btr(n-1, s + n - 1)
     else:
          return btr(n-1, s + n ** 2 + 1)

     
#5 
#MEMOIZATION 
#USE THIS DICTIONARY
d = {2:0,1:0}
def bm(n):
     #TO DO: IMPLEMENT
     if n in d.keys():
          return d[n]
     else:
          for x in range(3, n+1):
               if even(x):
                    d[x] = x - 1 + d[x-1]
               else:
                    d[x] = x**2 +1 + d[x-1]
          return d[n]


for i in range(1,10): 
    print("f({0}) = {1}, {2}, {3}".format(i, b(i),btr(i,0),bm(i)))

fblist = [b, lambda i: btr(i,0), bm ]
tlist = [round(ftimer(f,700)*10**5,2) for f in fblist]
print(tlist)
print()
###################################################

#7
#RECURSIVE IMPLMENTATION
#INPUT N
#OUTPUT RE VALUE
def gg(n):
     #TO DO: IMPLEMENT
     if n == 0:
          return 1
     else:
          return 1 + 2*gg(n-1)

#8
#TAIL RECURSIVE
def gtr(n,s):
     #TO DO:IMPLEMENT
     if n == 0:
          return s + 1
     else:
          return gtr(n-1, 2**(n) + s)

#9
#MEMOIZATION DICTIONARY INSIDE
def gm(n):
     d = {0:1}
     if n in d.keys():
          return d[n]
     else:
          for x in range(1, n+1):
               d[x] = 1 + 2*d[x-1]
          return d[n]


fglist = [gg, lambda i: gtr(i,0),gm]

for i in range(0,10):
     print("f({0}) = {1}, {2}, {3}".format(i,gg(i),gtr(i,0),gm(i)))

tlist = [round(ftimer(f,700)*10**5,2) for f in fglist]
print(tlist)

