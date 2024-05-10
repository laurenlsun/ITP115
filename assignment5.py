# Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Assignment 5
# Description: This program counts the occurances of each letter of the alphabet in a given string
loopTimes = int(input("Character Distribution\nEnter the number of times to run: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"
for loopVar in range(0, loopTimes, 1):
    userInput = input("Enter a sentence: ")
    specialCharCounter = 0
    for char in userInput:
        if char.lower() not in alphabet and char != " ":
            specialCharCounter +=1
    print("special characters:", specialCharCounter*"*")

    for letter in alphabet:
        print(letter + ":", end="")
        counter = 0
        for char in userInput:
            if char.lower()==letter:
                counter += 1
        if counter > 0:
            print(counter * "*")
        elif counter==0:
            print("NONE")
