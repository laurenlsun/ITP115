# Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Final Project
# extra_credit.py
# Description: this program provides additional functions to give the user more info on roller coasters
import helper
import user_interface

def getLongestCoaster(coastersList):
    longestCoaster = coastersList[0] # initialize the value
    greatestLength = 0 # initialize the value
    for coaster in coastersList:
        if "length" in coaster.keys():
            if coaster["length"] != "": # validity check
                if int(coaster["length"]) > greatestLength:
                    greatestLength = int(coaster["length"]) # set new greatest length
                    longestCoaster = coaster # set new longest coaster
    return longestCoaster


def displayLongestCoaster(coastersList):
    user_interface.displayCoaster(getLongestCoaster(coastersList))


def getParkMostCoasters(coastersList):
    parkMostCoasters = coastersList[0]["park"] # initialize the value
    highestCount = 0 # initialize the value
    parkList = helper.getParksList(coastersList)
    for park in parkList:
        count = 0  # indiv count for each coaster
        for coaster in coastersList: # go through coasters and find coasters in this park
            if "park" in coaster.keys():
                  if coaster["park"] == park and coaster["park"] != "": # validity check
                       count += 1
        if count > highestCount:
            highestCount = count # set new highest count
            parkMostCoasters = park # set new park with the most coasters
    return parkMostCoasters


def displayParkMostCoasters(coastersList):
    park = getParkMostCoasters(coastersList) # get the park with most coasters
    count = 0
    for coaster in coastersList:
        if "park" in coaster.keys(): # validity check
            if coaster["park"] == park:
                user_interface.displayCoaster(coaster) # display this coaster if it's in the park
                count += 1
    print(park, "has", count, "coasters.")