# Lauren, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Assignment 6
# Description: This program jumbles words and makes the user guess what it is. It gives a hint if the user wants one.

import random

# word lists
words = ["python", "bottle", "apple", "professor", "purse", "penguin", "programming"]
hints = ["coding", "container", "fruit", "person", "accessory", "animal", "class"]

randomWord = random.choice(words) # create random generator
randomWordList = list(randomWord)
n = len(randomWordList) # find number of letters
jumbledWord = [] # create empty list to add jumbled letters

for i in range (n):
    randomIndex = random.randrange(len(randomWordList)) # returns a random index within the number of letters
    jumbledWord.append(randomWordList.pop(randomIndex)) # adds letter of the random index to the jumbled word list
print("Your jumbled word is", ''.join(jumbledWord) + ".") # converts to string and prints
guess = ""
count = 0
while guess != randomWord:
    count += 1
    guess = input("Enter your guess: ").lower()
    if guess == randomWord:
        print("You got it! It took you", str(count), "guesses.")
    else:
        print("That is not correct.")
        hintYN = input("Do you want a hint? (y or n)")
        if hintYN.lower() == "y":
            hintIndex = words.index(randomWord)
            print("The hint is \"" + hints[hintIndex] + "\"")
