# Lauren, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Assignment 4
# Description: This program continuously asks for numbers and finds the least, greatest, and average numbers
userChoiceToRepeat = True # ensure that it runs at least once
while userChoiceToRepeat == True:
    userInput = 0
    sum = 0
    count = 0
    maxNum = -float('inf') # sets initial max as lowest number possible
    minNum = float('inf') # sets initial min as highest number possible
    print("Enter an integer greater than or equal to 0 or -1 to quit:")
    # repeated segment that will continuously ask for number
    '''
    while userInput != -1:
        userInput = int(input("> "))
        if userInput != -1:
            sum += userInput # add to cumulative sum
            count += 1 # increase count of numbers entered
            if userInput > maxNum:
                maxNum = userInput
            if userInput < minNum:
                minNum = userInput
    '''
    userInput = int(input("> "))
    minNum = userInput
    maxNum = userInput
    while userInput != -1:
        sum +=userInput
        count += 1
        userInput = int(input("> "))
        if userInput > maxNum:
            maxNum = userInput
        if userInput < minNum:
            minNum = userInput

    # display results
    print("average:", str(sum/count))
    print("max number:", str(maxNum))
    print("min number:", str(minNum))

    # loop control to stay/leave
    userChoiceToRepeat = input("Would you like to continue? (enter y/n): ")
    if userChoiceToRepeat.lower() == "y":
        userChoiceToRepeat = True
    elif userChoiceToRepeat.lower() == "n": # exit
        userChoiceToRepeat = False
        print("Goodbye.")