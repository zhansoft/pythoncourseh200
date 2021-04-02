#input temperature in fahrenheit T, wind speed in mph V
#return wind chill temperature

def windChill(T, V):
    wChill = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)
    return wChill

print(windChill(25, 5))

#this is the one i want you to look at
#please work
#why won't you push
#please