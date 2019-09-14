
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: mileage.py
# [H2-4] (mileage.py) Do Exercise 10 at the end of HTT2. Write a program that will compute MPG for a car. Prompt the
# user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.
# ----------------------------------------------------------------------------------------------------------------------


def mileage(miles, gallons):            # Function for calculating user MPG
    mpg = miles/gallons                 # Miles per gallon calculation
    print("Hi! the miles per gallon for this travel is: ", mpg)  # printing with a message


miles = float(input("Enter number of miles travelled to calculate the MPG: "))
gallons = float(input("Enter number of gallons used during this travel to calculate the MPG: "))

mileage(miles, gallons)         # Calling the function using user inputs
