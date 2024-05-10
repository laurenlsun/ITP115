#Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Assignment 2
# This program creates a Mad Libs story.
# It gets input from the user and prints output.

# string inputs
noun = input("Enter a singular noun (ex. \"car\"): ")
verb = input("Enter a verb (ex. \"eat\"): ")
adj = input("Enter an adjective (ex. \"shy\"): ")
prep = input("Enter a preposition (ex. \"in\"): ")
adverb = input("Enter an adverb (ex. \"quickly\"): ")

# numerical inputs
num1 = int(input("Enter an integer number from 1 to 100: "))
num2 = int(input("Enter another integer number: "))
num3 = int(input("Enter another integer number: "))
num4 = float(input("Enter a decimal number between 0 and 10: "))

# create output
print("The other night, I had to \"" + verb + "\" really \"" + adverb + "\" because I wanted to make it \"" + prep + "\" the birthday party.")
print("They wanted me to bring \"" + str(num1) + "\" chairs, and it turns out they had \"" + str(num2) + "\" stools, so we ended up with \"" + str(num1+num2) + "\" seats.")
print("It went on for \"" + str(num3) + "\" hours, so I'd rate that a \"" + str(num4) + "\" out of 10.")