# sophia zhang
def unmarriedTax(income):
#TO DO: IMPLEMENT FUNCTION
    if (income >= 0 and income <= 9700):
        taxOwed = .10 * income
    elif (income >= 9701 and income <= 39475):
        taxOwed = .12 * income
    elif (income >= 39476 and income <= 84200):
        taxOwed = .22 * income
    elif (income >= 84201 and income <= 160725):
        taxOwed = .24 * income
    elif (income >= 160726 and income <= 204100):
        taxOwed = .32 * income
    elif (income >= 204101 and income <= 510300):
        taxOwed = .35 * income
    elif (income < 0):
        print("How you gonna get a negative income? Smh.")
    else:
        taxOwed = .37 * income
    return taxOwed



# 2 Finish this function
# Calculates the taxes a married person owes for 2019
# Input Parameters: amount of income in USD income
# Return Value: amount taxes owed (USD)
def marriedTax(income):
#TO DO: IMPLMEMENT FUNCTION
    if (income >= 0 and income <= 19400):
        taxOwed = .10 * income
    elif (income >= 19401 and income <= 78950):
        taxOwed = .12 * income
    elif (income >= 78951 and income <= 168400):
        taxOwed = .22 * income
    elif (income >= 168401 and income <= 321450):
        taxOwed = .24 * income
    elif (income >= 321451 and income <= 408200):
        taxOwed = .32 * income
    elif (income >= 408201 and income <= 612350):
        taxOwed = .35 * income
    elif (income < 0):
        print("How you gonna get a negative income? Smh.")
    else:
        taxOwed = .37 * income
    return taxOwed
    


# Calculates the taxes an individual owes for 2019
# Input Parameters: amount of income in USD income and marital status Boolean maritalStatus
# Return Value: amount taxes owed (USD)
def tax(income, maritalStatus):
	if(maritalStatus):
		return marriedTax(income)
	else:
		return unmarriedTax(income)
		
############################
#   DATA
############################
UrsalaIncome,UrsalaMarried = 160726, True
KaiserIncome, KaiserMarried = 501000, True
ShilahIncome, ShilahMarried = 20, True

############################
#   TESTS
############################
print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
print("Shilah owes ", tax(ShilahIncome, ShilahMarried))

print()
############################
#   DATA
############################
UrsalaIncome,UrsalaMarried = 204099, False
KaiserIncome, KaiserMarried = 510310, False
ShilahIncome, ShilahMarried = 9400, False

############################
#   TESTS
############################
print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
print("Shilah owes ", tax(ShilahIncome, ShilahMarried))

__name__ == "__main__"

# Tax brackets are so dumb in the fact that if you make even $1 over, then you have to pay a significant amount more
# than in the previous bracket.  ALso, if you're married then you really get screwed over because you have to pay
# even more than if you were single.  That's why, Dr. D brought this one up, Judge Judy is like "Why are you living
# together if you're not married huh?" Millenials won't get married just so that they owe less.  I also personally
# think that tax breaks for corporations is mega dumb.