# Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Assignment 10
# Description: This program allows the user to naviguate a menu, add/delete items, change the price, and view prices

def displayChoices():
    print("Manage the Menu\na) Add a menu item\nb) Update the price\nc) Show the price\nd) Delete a menu item\ne) Show the menu\nx) Exit)")


def isFloat(numStr):
    numStr = numStr.replace(".", "", 1) # replace one decimal point with nothing
    if numStr.isdigit(): # see if that replacement made the whole thing a number
        return True
    else:
        return False


def updatePrice(menuDict):
    itemToUpdate = input("Enter a food item to update: ").strip().title()
    if itemToUpdate in menuDict.keys():
        print(itemToUpdate, "costs $" + str(menuDict[itemToUpdate]))
        newPrice = "flhdsfg" # initial value to enter the loop
        while not isFloat(newPrice): # keep asking until a valid float is entered
            newPrice = input("Enter the price: ")
        newPrice = float(newPrice) # convert to float
        menuDict[itemToUpdate] = newPrice # add entry
        print(itemToUpdate, "now costs $" + str(newPrice)) # print confirmation
    else:
        print(itemToUpdate, "is not on the menu.")


def addItem(menuDict):
    newItem = input("Enter a food item to add: ").strip().title()
    if newItem in menuDict.keys():
        print(newItem, "is already on the menu.")
    else:
        newPrice = "flhdsfg" # new value to enter loop
        while not isFloat(newPrice): # until value entered is a float
            newPrice = input("Enter the price: ")
        newPrice = float(newPrice) # convert to float
        menuDict[newItem] = newPrice # add entry
        print(newItem, "has been added to the menu.") # confirmation


def showPrice(menuDict):
    item = input("Enter a food item to find: ").strip().title() # format
    if item in menuDict.keys():
        print(item, "costs $" + str(menuDict[item])) # print price
    else:
        print(item, "is not on the menu.")


def deleteItem(menuDict):
    item = input("Enter a food item to find: ").strip().title() # format
    if item in menuDict.keys():
        menuDict.pop(item) # remove it
        print(item, "was deleted from the menu.")
    else:
        print(item, "is not on the menu.")


def showMenu(menuDict):
    for item in menuDict: # loop through every item
        print(item, "costs $" + str(menuDict[item]))


def main():
    menuDict = {"Pizza" : 4.99, "Salad": 7.99, "Sandwich" : 10.99}
    displayChoices()
    userChoice = "m" # enter loop
    while userChoice.lower() != "x":
        userChoice = input("Choice: ").lower()
        if userChoice=="a":
            addItem(menuDict)
        elif userChoice=="b":
            updatePrice(menuDict)
        elif userChoice=="c":
            showPrice(menuDict)
        elif userChoice=="d":
            deleteItem(menuDict)
        elif userChoice=="e":
            showMenu(menuDict)
        elif userChoice=="x":
            print("Thank you!")
        else:
            print("Invalid input")

main()