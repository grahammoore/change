#Task 2: GCSE style question
#Write a program that will add up the cost of several items.

#The program should ask the user to enter how many items there are,
#and then ask for the price of each item with the prompt message in the form
#“Please enter the price of the item: £”.

#The user enters the price of each item as a number without a currency symbol.

#The program should add the prices together and then display the total cost
#with a user-friendly message, including the currency symbol, £.

#Challenge: Develop your program further so that the user enters the amount
#that they have paid (e.g. 20.00 without the £ symbol) and the program displays
#how many £20, £10, £5 notes and how many £2, £1, 50p, 20p, 10p, 5p, 2p and 1p
#coins should be given as change, or how much more money is needed.
#For the above challenge, the // operator (floor division, or integer division)
#and % modulo operator (gives the positive remainder from integer division)
#are helpful.
#e.g.
#5 // 2 = 2             (the integer part of the division calculation)
#5 % 2 = 1             (the remainder from integer division)

from decimal import *
# getcontext().prec = 10


#initialise cost
cost = Decimal("0.00")

#initialise total
totalcost = Decimal("0.00")

#function to calculate how many £20, £10, £5 notes and how many £2, £1, 50p, 20p, 10p, 5p, 2p and 1p
#coins should be given as change
def calculatechangeformat(change):

    print ("Stating change is £%s" % (change))

    change = subtract_coin_or_note(change, "£20", "20")
    change = subtract_coin_or_note(change, "£10", "10")
    change = subtract_coin_or_note(change, "£5", "5")
    change = subtract_coin_or_note(change, "£2", "2")
    change = subtract_coin_or_note(change, "£1", "1")
    change = subtract_coin_or_note(change, "50p", "0.5")
    change = subtract_coin_or_note(change, "20p", "0.2")
    change = subtract_coin_or_note(change, "10p", "0.1")
    change = subtract_coin_or_note(change, "5p", "0.05")
    change = subtract_coin_or_note(change, "2p", "0.02")
    change = subtract_coin_or_note(change, "1p", "0.01")

    print(" new change at end %s" % (change))


def subtract_coin_or_note(change, faceValue, noteOrCoinValue):
    print(" new change before %s is %s" % (faceValue, change))

    note = Decimal(noteOrCoinValue)
    if change >= note:
        print ("The number of %s notes needed is 1" % faceValue)
        change = Decimal(change) - note

    return change



#Ask the user to enter how many items there are
#numofitems = int(input("How many items are there? "))

#for each item get the price
#for count in range(0,numofitems):
#   cost = float(input("Please enter the price of the item: £"))
#  totalcost = totalcost + cost
# print ("Total so far £{0:.2f}".format(totalcost))

#get amount paid from user
#paid = float(input("How much have you paid so far? £"))
#if paid > totalcost:
#    change = paid-totalcost
#    print("Your change is £{0:.2f}".format(change))
calculatechangeformat(Decimal("38.86"))
#elif paid < totalcost:
#   owed = totalcost-paid
#  print("You still owe £{0:.2f}".format(owed))
#else :
#   print("Thankyou thats perfect - Enjoy your day")