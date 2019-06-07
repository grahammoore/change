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


#initialise cost
cost = Decimal(0.00)

#initialise total
totalcost = Decimal(0.00)



#function to calculate how many £20, £10, £5 notes and how many £2, £1
#coins should be given as change
def calculatepoundformat(change):

    # if the total change is over £20 then calculate how many £20s are required and
    # update the change
    if change >= 20:
        twenties = change//20
        print ("The quantity of £20 notes needed is " + str(twenties))
        # calculate the new change
        change = change - (twenties*20)

    # if the new value of change is greater than £10 there is one £10 required
    if change >= 10:
        print ("The quantity of £10 notes needed is 1")
        change = change-10

    # if the new value of change is greater than £5 there is one £5 required
    if change >= 5:
        print ("The quantity of £5 notes needed is  1")
        change = change - 5

    # if the new value of change is greater than £2 calculate how many are required
    if change >= 2:
        twopounds= change//2
        print ("The quantity of £2 coins is         " + str(twopounds))
        change = change% 2

    # if the new value of change is greater than £1 there is one £1 required
    if change >= 1:
        print ("The quantity of £1 coins is         1")
        change = change - 1



#function to calculate how many 50p, 20p, 10p, 5p, 2p and 1p
#coins should be given as change
def calculatepenceformat(change):

    # if the new value of change is greater than 50p there can only be one 50p required
    if change >= 50:
        print ("The quantity of 50p is              1")
        change = change - 50

    # if the new value of change is greater than 20p calc number of 20ps required
    if change >= 20:
        twentypence= int(change//20)
        print ("The quantity of 20p is              " + str(twentypence))
        change = change- ((twentypence) * 20)

    # if the new value of change is greater than 10p there can only be one 10p required
    if change >= 10:
        print ("The quantity of 10p is              1")
        change = change-10

    # if the new value of change is greater than 5p there can only be one 5p required
    if change >= 5:
        print ("The quantity of 5p is               1")
        change = change - 5

    # if the new value of change is greater than 2p calc number of 2ps required
    if change >= 2:
        twopence= change//2
        print ("The quantity of two pences is       " + str(twopence))
        change = change % 2

    # if the new value of change is 1p there can only be one 1p required
    if change >= 1:
        print ("The quantity of 1p is               1 " )
        change = change - 1


#----------------------------------------------------------#



#Ask the user to enter how many items there are
numofitems = int(input("How many items are there? "))

#for each item get the price
for count in range(0,numofitems):
    cost = input("Please enter the price of the item: £")
    totalcost = totalcost + Decimal(cost)

print ("Total spent £{0:.2f}".format(totalcost))

#get amount paid from user
paid = input("How much have you paid so far? £")

# if user has paid more than the costs then print the change requried.
if Decimal(paid) > totalcost:
    change = Decimal(paid)-totalcost
    print("Your change is £{0:.2f}".format(change))

    # split change into £s and pence
    pounds = change //1

    # convert pence to whole numbers
    pence = int((change % 1 )*100)
    calculatepoundformat(pounds)
    calculatepenceformat(pence)

# else if user has paid less than the total cost tell them how much more they
# need to pay
elif Decimal(paid) < totalcost:
    owed = totalcost-Decimal(paid)
    print("You still owe £{0:.2f}".format(owed))

# else if they have paid the exact amount, thank them
else :
    print("Thankyou thats perfect - Enjoy your day")