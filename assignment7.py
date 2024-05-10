# Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Assignment 7
# Description: rock paper scissor game against the computer until someone wins twice
import random


def displayRules(): # print the rules
    print("Let's play Rock Paper Scissors.\nThe rules of the game are:\nROCK smashes SCISSORS\nSCISSORS cut PAPER PAPER covers ROCK\n(If both the hands are the same, it's a tie)")


def userPlays(optionsList):
    userChoice = "" # just initialize it to something not in options list
    while userChoice not in optionsList: # keep asking until input is valid
        userChoice = (input("Enter ROCK, PAPER, or SCISSORS: ").strip()).upper() # strip/uppercase text
    print("User plays", userChoice)
    return userChoice


def computerPlays(optionsList):
    computerPlay = random.choice(optionsList) # randomly pick one from the r,p,s list
    print("Computer plays", computerPlay)
    return computerPlay


def gameOutcome(computerStr, userStr):
    if computerStr == userStr: # tie
        print("You and the computer tied.")
        return 0
    # 3 cases where comp wins
    elif computerStr == "SCISSORS" and userStr == "PAPER":
        print("Computer wins.")
        return -1
    elif computerStr == "ROCK" and userStr == "SCISSORS":
        print("Computer wins.")
        return -1
    elif computerStr == "PAPER" and userStr == "ROCK":
        print("Computer wins.")
        return -1
    else: # if not tie and not comp win, user wins
        print("You win!")
        return 1


def main():
    # initialize counters
    userW = 0
    compW = 0
    handsOptions = ["ROCK", "PAPER", "SCISSORS"] # option list
    displayRules() # intro
    while compW < 2 and userW < 2: # keep playing until one of them hits 2 wins
        userPlay = userPlays(handsOptions) # store user choice in a variable
        compPlay = computerPlays(handsOptions) # store comp choice in a variable
        result = gameOutcome(compPlay, userPlay) # evaluate outcome
        if result==-1: # comp wins
            compW += 1
        elif result==1: # user wins
            userW += 1
    # display results
    if compW==2:
        print("Computer won twice.")
    elif userW==2:
        print("You won twice!")

main()