from decimal import *

getcontext().prec = 2

change = Decimal("0.1")
print(" new change before 1p %s" % (change))

if change > Decimal("0.01"):
    print("The number of one pences is 1 ")
    change = change - Decimal("0.01")

print(" new change at end %s" % (change))