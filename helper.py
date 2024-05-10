# Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Final Project
# helper.py
# Description: this program has functions to create/access information from a roller coaster csv file

def createCoastersFromFile(filenameStr = "roller_coasters.csv"): # works
    fileIn = open(filenameStr, 'r', encoding='utf8') # Open a file for reading, which creates a file variable
    keys = fileIn.readline().strip().split(",") # Read the keys in the first line.
    coastersList = [] # Create a variable to hold a list of coasters.
    for line in fileIn: # outer loop to create a dictionary and get the data
        lineAsList = line.split(",") # turn line into list
        dictionary = {} # empty dictionary to be filled for every iteration, every reading of a row
        for feature in lineAsList: # loop through the row's cell value in each column
            if keys[lineAsList.index(feature)] == "status": # if the column is status
                dictionary[keys[lineAsList.index(feature)]] = feature.strip()[7:] # start "reading" the status from after "status."
            else:
                dictionary[keys[lineAsList.index(feature)]] = feature # dictionary[key] = value for that key
        coastersList.append(dictionary)
    fileIn.close()
    return coastersList


def getParksList(coastersList):
    parkNamesList = [] # Create a variable to hold a list of park names.
    for coaster in coastersList: # Loop through the list of coasters.
        if "park" in coaster.keys(): # if a park is specified
            if coaster["park"].strip() not in parkNamesList:
                parkNamesList.append(coaster["park"].strip())
                # Get the park name from the dictionary and add it to the list if it is not already in the list.
    parkNamesList.sort() # sort the list
    return parkNamesList


def getFastestCoaster(coastersList): # works
    # Create variables to hold the fastest speed and a dictionary.
    fastestSpeed = 0
    fastestCoaster = {}
    for coaster in coastersList: # Loop through the list of coasters.
        # Get the speed of the coaster
        speed = coaster["speed"].strip()
        if speed != "": # in case it's blank
            speed = int(speed) # convert to number
            if speed > fastestSpeed: # compare it to fastest speed, see if it's a new fastest speed
                fastestSpeed = speed # Reset the variables accordingly.
                fastestCoaster = coaster
    return fastestCoaster
