
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: rangefun2.py
# [H2-3] (sumrange.py) Write a program that reads integers start and stop from the user, then calculates and prints the
# sum of each integer ranging from start to stop, inclusive. "Inclusive" means that both the values start and stop are
# included. For example, if you enter 2 and 4, your program should print 9 since 2+3+4==9.
# ----------------------------------------------------------------------------------------------------------------------


def sumrange(start, stop):              # function for summing numbers
    count = 0
    for i in range(start, stop + 1):    # loop to add the numbers
        count += i
    print("The summation between", start, "and", stop, "is:", count)


start = int(input("Enter the Start integer number for the summation: "))     # User input for start number
stop = int(input("Enter the Stop integer number for the summation: "))       # User input for stop number

sumrange(start, stop)               # Calling the function using user inputs
