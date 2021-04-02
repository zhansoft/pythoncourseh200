#imports
import math 

######################################
#
# DATA 
#
#All values $/ounce abbreviated $/Oz
Gold = 1503.35        #up 11.00
Silver = 17.91          #up 0.47
Platinum = 950.60    #down 2.50
Palladium = 1468.82 #down 10.48

Au, Ag, Pl, Pa = "Au", "Ag", "Pl", "Pa" # to make use of symbols easier

account = 100000  # $100,000 cash assets
Au_amt, Ag_amt, Pl_amt, Pa_amt = 0,0,0,0

#######################################
#INPUT NOTHING
#RETURN amount of money you have
#and amount of precious metals
def holdings():
    print("Your current holdings")
    print("Account   = {0:.2f}".format(account))
    print("Gold      = ",Au_amt)
    print("Silver    = ",Ag_amt)
    print("Platinum  = ",Pl_amt)
    print("Palladium = ",Au_amt)
    print()
    

#INPUT metal and amount in ounces you want to purchase
#RETURN the cost of the amount of metal you're purchasing
def preciousMetalToDollars(metal, amt):
#TO DO: IMPLEMENT FUNCTION
    price = 0
    if metal == Au:
        price = amt * 1503.35
    elif metal == Ag:
        price = amt * 17.91
    elif metal == Pl:
        price = amt * 950.60
    elif metal == Pa:
        price = amt * 1468.82
    return price

#INPUT metal and amt you want to purchase
#RETURN IF you have sufficient funds, purchase that amount in 
#oz. and add to x_amt and subtract that from account
#If you don't have sufficient funds, output message that you 
#can't purchase that amount
def purchase(metal, amt):
    global account
    global Au_amt
    global Ag_amt
    global Pl_amt
    global Pa_amt

    def metalPrice(metal):
        price = 0
        if(metal == Au):
            price = 1503.35
        elif (metal == Ag):
            price = 17.91
        elif (metal == Pl):
            price = 950.60
        elif(metal == Pa):
            price = 1468.82
        return price

    if (account < preciousMetalToDollars(metal, amt)):
        statement = "You can't buy that.  Ya poor."
        print(statement)
    else:
        account -= preciousMetalToDollars(metal, amt)
        if(metal == Au):
            Au_amt += amt
        elif (metal == Ag):
            Ag_amt += amt
        elif (metal == Pl):
            Pl_amt += amt
        elif(metal == Pa):
            Pa_amt += amt
        print("You have purchased", amt, "oz. of {0: .2f}".format(metalPrice(metal)), "for {0: .2f}".format(preciousMetalToDollars(metal, amt)), "\nYou have {0: .2f}".format(account), "remaining in your account.")



#COMPLETE IMPLEMENTATION OF FUNCTION
#LEAVE GLOBAL variables



######MAIN######

holdings()

print("{:0.2f}".format(preciousMetalToDollars(Au,4)))
print("{:0.2f}".format(preciousMetalToDollars(Ag,100)))
print("{:0.2f}".format(preciousMetalToDollars(Pa,23)))
print("{:0.2f}".format(preciousMetalToDollars(Pl,17)))

print()
purchase(Au,4)
purchase(Ag,100)
purchase(Pa,23)
purchase(Pl,17)
print()

holdings()

purchase(Pl,100000)
if __name__=="__main__":
    pass