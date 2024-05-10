# Lauren, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Assignment 3
# This program creates a Harry Potter vending machine.
# User enters payment and the program determines the change.

# menu display for user
print("Please select an item from the vending machine:")
print("a) Assortment of Candy for 11 sickles and 7 knuts")
print("b) Butterbeer for 2 sickles")
print("c) Quill for 6 sickles")
print("d) Daily Prophet for 5 knuts")

# choice input
choice = input("Choice (ex. \"b\"): ")

# conditions
if choice == "a" or choice == "A":
    print("You purchased the Assortment of Candy.")
    item = "Assortment of Candy"
    costInKnuts = 7 + 29*11
elif choice == "b" or choice == "B":
    print("You purchased Butterbeer.")
    item = "Butterbeer"
    costInKnuts = 2*29
elif choice == "c" or choice == "C":
    print("You purchased the Quill.")
    item = "Quill"
    costInKnuts = 6*29
elif choice == "d" or choice == "D":
    print("You purchased the Daily Prophet.")
    item = "Daily Prophet"
    costInKnuts = 5
else:
    print("You entered an invalid input. The item selected was the Daily Prophet.")
    costInKnuts = 5

# payment process
# ask for user's payment
print("Cost: ", str(costInKnuts), "knuts.")
print("Please pay by entering the number of each coin")
galleons = int(input("Number of galleons: "))
sickles = int(input("Number of sickles: "))
knuts = int(input("Number of knuts: "))

# convert payment to knuts
paymentInKnuts = galleons*493 + sickles*29 + knuts
print("Payment: ", str(paymentInKnuts), "knuts.")

# not enough money
if paymentInKnuts < costInKnuts:
    print("You did not enter enough money. You will not receive the", item + ".")
# return change
else:
    changeInKnuts = paymentInKnuts - costInKnuts
    print("Your change is", str(changeInKnuts), "knuts.")
    galleons = changeInKnuts // 493 # number of whole galleons to return
    changeInKnuts %= 493 # number of knuts left over after removing galleons
    sickles = changeInKnuts // 29 # number of whole sickles to return
    changeInKnuts %= 29
    print("You will receive", str(galleons), "galleons,", str(sickles), "sickles, and", str(changeInKnuts), "knuts.")