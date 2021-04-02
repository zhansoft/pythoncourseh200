def unmarriedTax(income):
#TO DO: IMPLEMENT FUNCTION


# 2 Finish this function
# Calculates the taxes a married person owes for 2019
# Input Parameters: amount of income in USD income
# Return Value: amount taxes owed (USD)
def marriedTax(income):
#TO DO: IMPLMEMENT FUNCTION


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
