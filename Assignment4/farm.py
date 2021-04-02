def f(x, y, z):
    # TO DO: IMPLEMENT FUNCTION
    return 11*x*y + 14*y*z + 15*x*z

def vol(x, y, z):
    return x * y * z == 147840

# some arbitrary starting point
a, b, c = 2, 2, 36960

# TO DO: LOOPS SEARCHING THROUGH POSSIBLE
# VALUES
minValues = []
currMin = 1000000
for a in range(0, 101):
    for b in range(0, 101):
        for c in range (0, 101):
            if f(a,b,c) < currMin and vol(a,b,c):
                minValues += [[a, b, c, f(a,b,c)]]
                currMin = f(a,b,c)
a = minValues[len(minValues)-1][0]
b= minValues[len(minValues)-1][1]
c = minValues[len(minValues)-1][2]

print("H  W  L  Value")
print(a, b, c, f(a,b,c))




if __name__ == "main":
    pass