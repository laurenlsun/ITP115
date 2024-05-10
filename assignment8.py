# Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Assignment 8
# Description:
# Lets the user guess a 3 digit secret code

import random

def isSingleDigit(userStr):
    if userStr.isdigit() and len(userStr) == 1: # contains a single digit
        return True
    else:
        return False


def generateCodeList(size):
    list = []
    for i in range (size):
        list.append(random.randrange(0, 10)) # add a random integer 0-9 until list is filled
    return list


def getUserList(size):
    list = []
    for i in range(size):
        newNum = "-1" # to initiate while loop
        while not isSingleDigit(newNum): # keep asking until user enters a single digit
            newNum = input("Enter a digit at index " + str(i) + ": ")
        list.append(int(newNum)) # add to guess list
    print("Your guess is", list)
    return list


def printHints(codeList, userList):
    print("Generating hints...")
    count = 0 # number of guessed digits that are in the answer
    hintedNums = [] # keep track of previously hinted numbers so the same hint isn't given twice
    for i in range(len(userList)): # will iterate for each item in user guess
        if codeList.count(userList[i]) > 0 and userList[i] not in hintedNums: # if present in answer and if not already hinted before
            print(userList[i], "occurs", codeList.count(userList[i]), "time(s).")
            count += 1
            hintedNums.append(userList[i]) # add hinted number to list
    if count == 0:
        print("No correct digits")
    for i in range(len(codeList)):
        if codeList[i] == userList[i]: # if the digits at matching indexes are correct
            print(userList[i], "is in the correct position.")


def main():
    numDigits = 3
    answer = generateCodeList(numDigits)
    print("The number of digits in the code is", numDigits)
    userGuess = []
    numGuesses = 0
    while userGuess != answer:
        userGuess = getUserList(numDigits)
        if userGuess != answer:
            printHints(answer, userGuess)
        numGuesses += 1
    print("You guessed it! It took you", numGuesses, "guess(es).")

main()