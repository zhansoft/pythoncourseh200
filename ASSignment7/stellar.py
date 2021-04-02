import astronomy as astr
import math

def F(m):
    def lbToKg(pnds):
        return pnds/2.205 # lbs / (kg/lb)
    myWeight = lbToKg(m)
    print(myWeight)
    gravity = (astr.gravitationalConstant * myWeight * astr.earthMass)/math.pow(astr.earthDiameter/2,2) # [(m^3/kg*s)*(kg)*(kg)]/m^2
    return gravity # Newtons

if __name__ == "__main__":
    print("{0:.2f} Newtons.".format(F(143.3)))