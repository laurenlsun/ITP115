# Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Final Project
# main_sun_lauren.py
# Description: this program interacts with the user by calling other functions to provide info on rollercoasters

import user_interface
import extra_credit
import helper

def getMenuDict():
    dict = {"A": "Number of coasters",
            "B": "Number of operating coasters",
            "C": "Fastest coaster",
            "D": "Amusement parks",
            "E": "Coasters in a park",
            "F": "Find coasters",
            "G": "Longest coaster",
            "H": "Park with most coasters",
            "Q": "Quit"}
    return dict

def main():
    print("Roller Coasters")
    coastersList = helper.createCoastersFromFile() # list of roller coaster dictionaries
    menuDict = getMenuDict() # create menu
    userChoice = "" # initialize userChoice so it's not = to Q
    while userChoice != "Q":
        user_interface.displayMenu(menuDict)
        userChoice = user_interface.getUserChoice(menuDict)
        if userChoice == "A": # number of coasters
            user_interface.displayNumCoasters(coastersList)
        elif userChoice == "B": # operating ones
            user_interface.displayNumOperatingCoasters(coastersList)
        elif userChoice == "C": # fastest
            user_interface.displayFastestCoaster(coastersList)
        elif userChoice == "D": # print list of parks
            user_interface.displayAllParks(coastersList)
        elif userChoice == "E": # search, print coasters in searched park
            user_interface.displayCoastersInPark(coastersList)
        elif userChoice == "F": # search for coasters
            user_interface.findCoasters(coastersList)
        elif userChoice == "G": # longest
            extra_credit.displayLongestCoaster(coastersList)
        elif userChoice == "H": # park with most coasters
            extra_credit.displayParkMostCoasters(coastersList)

main()