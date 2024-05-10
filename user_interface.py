# Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Final Project
# user_interface.py
# Description: this program contains various functions that allows the user to retrieve information about various roller coasters

import helper

def displayMenu(menuDict):
    # create a list from the keys
    listOfKeys = []
    for key in menuDict.keys():
        listOfKeys.append(key)
    listOfKeys.sort()
    # Loop through the sorted keys and print the key, "->", and description.
    for key in listOfKeys:
        print(key, "->", menuDict[key])


def getUserChoice(menuDict):
    # Use the appropriate loop to continue to ask the user for input until they enter valid input.
    userChoice = "gfjhldskfj" # initial value not in menudict keys
    while userChoice not in menuDict.keys(): # allow for lowercase + extra spaces. compare with valid format menudict keys
        userChoice = input("Choice: ").strip().upper()
    return userChoice


def displayNumCoasters(coastersList):
    print('The total number of coasters is', len(coastersList)) # use length of coasterlist


def displayNumOperatingCoasters(coastersList):
    count = 0
    for coaster in coastersList:
        if coaster["status"] == "operating": # if operating
            count += 1 # increase count
    print("The total number of operating coasters is", count)


def displayCoaster(coasterDict):
    print(coasterDict["name"] + " [" + coasterDict["park"] + "]") # coaster name and park
    if "speed" in coasterDict.keys(): # check if coaster has a listed speed
        if coasterDict["speed"] != "": # check if that speed isn't blank
            print("\tSpeed =", coasterDict["speed"], "mph")
    if "height" in coasterDict.keys(): # check if coaster has a listed height
        if coasterDict["height"] != "": # check if that height isn't blank
            print("\tHeight =", coasterDict["height"], "ft")
    if "length" in coasterDict.keys(): # check if coaster has a listed length
        if coasterDict["length"] != "": # check if that length isn't blank
            print("\tLength =", coasterDict["length"], "ft")
    print("\tStatus is", coasterDict["status"])


def displayFastestCoaster(coastersList):
    displayCoaster(helper.getFastestCoaster(coastersList)) # get the fastest coaster, send it to display function


def displayAllParks(coastersList):
    listOfNames = helper.getParksList(coastersList) # create list of parks
    count = 0
    print("Amusement parks in alphabetical order:")
    for name in listOfNames: # print each
        print(name)
        count += 1
    print("There are", count, "unique parks.")


def displayCoastersInPark(coastersList):
    park = input("Enter a park: ").strip().lower()
    lowercaseParksList = [] # make a temporary list in all lowercase to compare with whatever format user enters
    for item in helper.getParksList(coastersList): # loop through each park
        lowercaseParksList.append(item.lower()) # add it to lowercase list
    searchResult = False # whether or not there were matches found
    for parkName in lowercaseParksList:
        if park in parkName: # if there's a search match
            count = 0 # start counting coasters in park
            coastersInPark = [] # create list of coasters in park
            for coaster in coastersList:
                if "park" in coaster.keys(): # check if coaster has a park listed
                    if park in coaster["park"].lower(): # if the coaster is in the park entered by user
                        displayCoaster(coaster)
                        count += 1
            print(park.capitalize(), "has", count, "coasters.")
            searchResult = True # found a search result
    if not searchResult:
        print("No coasters in", park.capitalize())


def findCoasters(coastersList):
    search = input("Enter a search phrase: ").strip().lower()
    count = 0
    for coaster in coastersList: # go through coasters
        if search in coaster["name"].lower(): # if search query in coaster name
            displayCoaster(coaster) # display it
            count += 1 # increase count
    if count == 0:
        print("No coasters contain \"" + search + "\"")
    else:
        print("Found", count, "coasters that contain \"" + search + "\"")