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
getcontext().prec = 10

#create array for notes and coin values
notesandcoins = [["£20",20], ["£10", 10], ["£5", 5], ["£2",2], ["£1",1], ["50p",.5], ["20p",.2],["10p",.1],["5p",.05],["2p",.02],["1p",.01]]

#initialise cost
cost = Decimal(0.00)

#initialise total
totalcost = Decimal(0.00)

##############################################################
#function to calculate how many £20, £10, £5 notes and how many £2, £1, 50p, 20p, 10p, 5p, 2p and 1p
#coins should be given as change

def calculatenotesandcoins(change):

    print ("Starting change is £%s" % (change))
    for noteorcoin in notesandcoins:
        change = subtract_coin_or_note(Decimal(change), noteorcoin[0], noteorcoin[1])


################################################
def subtract_coin_or_note(change, faceValue, noteOrCoinValue):

    note = Decimal(noteOrCoinValue)
    print("Note or coin value " + str(noteOrCoinValue))
    if Decimal(change) >= Decimal(note):

        numofnotes = Decimal((Decimal(change)//Decimal(note)))
        print ("%s needed is %s "% (faceValue, numofnotes))
        change = Decimal(Decimal(change) - Decimal(numofnotes)*Decimal(note))
        print ("change after %s is £%s" % (faceValue,change))

    return change


###############################################
#Ask the user to enter how many items there are
#numofitems = int(input("How many items are there? "))

#for each item get the price and keep a running total
#for count in range(0,numofitems):
#   cost = Decimal((input("Please enter the price of the item: £")))
#  totalcost = totalcost + cost
# print ("Total so far £{0:.2f}".format(totalcost))

#get amount paid from user
#paid = Decimal((input("How much have you paid so far? £")))

# if more has been paid than the total cost then calculate the change due
#if paid > totalcost:
#   change = paid-totalcost
#  print("Your change is £{0:.2f}".format(change))
# print("You will receive the following amounts")
# work out optimal way to return change
calculatenotesandcoins(463.11)
#calculatenotesandcoins(345345.45)

# if more is still owed then calculate the amount owing
#elif paid < totalcost:
#   owed = totalcost-paid
#  print("You still owe £{0:.2f}".format(owed))
# print("Please pay the following amounts ")
#calculatenotesandcoins(58.99)

# if amount paid is exactly the amount owed then thank the user
#else :
#   print("Thankyou thats perfect - Enjoy your day")