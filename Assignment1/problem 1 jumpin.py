#problem 1
x == 3
#x is not defined hahahahha does not output because == is not an assignment operator

#problem 2
_x = 10000
#no problem here yay

#problem 3
3x = 10
print(3x)
#syntax error: will not print because you can't have vars start with number

# #problem 4
    xxx = 200
#won't print because of an INDENTATION ERROR

#problem 5
_kitty = 20
_catty      =     40 + _kitty
_kitty = _catty + _kitty
print(_kitty + _catty)
#no problem here it prints out 140 because _kitty = 80 and _catty is 60 (does not rewrite function)

#problem 6 
_x = 10000
x = x + _x
#won't print because 'x' is not defined prior to line 27

#problem 7
Happy = 23
Sad = happy + 30
#won't print because 'happy' is lowercase

#problem 8
def funhouse(x):
    return x + x + x + xxx

x = 10
print(x)
x = funhouse(x + x)
print(x)
#won't print because 'xxx' isn't fucking acceptable

#problem 9
def RickandMorty(x, a, b):
    x = a + b
    return a

y = rickandmorty(1,2,3)
won't print because 'rickandmorty' isn't a function that's defined AND what teh fuck is the body of the actual function

#problem 10
def x(a):
    return b = 2*a + 1
def y(a):
    return b = 3*a + 2

a = 1
print(a)
a = x(a) + y(a) + x(y(a))
print (a)
#you have to write the local variable out first before printing it so dumb

#problem 11
def foo(x):
    x + 1

print(foo (1) + foo(2))
#won't print shit out because no return statement so stupid
