
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: randN.py
# [H3-2] (randN.py) Write a program that reads an int numRolls from the user, then generates numRolls random integers,
# each in the range 1 through 6. Use a for-loop to add together all rolls giving int sum, then compute the average
# (sum / numRolls).  Print out this average.  What do you expect for this average, as numRolls gets larger and larger?
# ----------------------------------------------------------------------------------------------------------------------

import random                                 # importing the random module


def randaverage(numRolls):                    # Function randaverage
    sum = 0
    for number in range(numRolls):            # for loop iteration with range user input numRolls
        randinteger = random.randint(1, 6)  # use randint function from random module to choose integer  range 1 and 6
#       print(randInteger)
        sum += randinteger

    average = sum/numRolls                    # calculating the average for the random numbers generate
    print("The average of random integers is: ", average)  # printing the average for the user


numRolls = int(input("Enter the integer: "))  # user input for the integer

randaverage(numRolls)                         # Calling function randaverage based on user input

# As the numRolls gets larger the average converges close to value 3.0 which is same as (1+2+3+4+5)/5
