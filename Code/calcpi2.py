
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: calcpi2.py
# [H3-3] (calcpi2.py) Here's another way of approximating Pi, using Leibniz' formula: Pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
# Notice how the signs alternate between + and - for each term of this series. Write a program which reads an int
# numTerms, then computes the above approximation of Pi by summing the first numTerms of this series.  Then print out
# the calculated value of Pi as well the error: the absolute value of its difference with math.pi.
# Hint: use a loop for count in range(numTerms):, with a loop body that does sign = -sign, and
# term = 1.0 / (2*count + 1) for count=0,1,2... Accumulate the sum of these terms, using the accumulator pattern, then
# calculate its error.
# ----------------------------------------------------------------------------------------------------------------------

import math                                                 # Importing Math module

numTerms = int(input("Enter integer for no. of terms: "))   # User input for numTerms
piEstimate = 0

for count in range(numTerms):                               # For loop iteration for pi estimate using Leibniz formula
    if count == 0 or count % 2 == 0:                        # assigning the sign value +ve or -ve for the formula
        sign = 1
    else:
        sign = -1
    piEstimate += sign * (1.0/(2 * count + 1))

finalPiEstimate = 4 * piEstimate

print("Math pi value: ", math.pi)                           # printing the calculated value and the error
print("Leibniz formula estimate is: ", finalPiEstimate)
print("Error is: ", abs(math.pi - finalPiEstimate))

