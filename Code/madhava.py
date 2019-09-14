
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: madhava.py
# [H4-6] (madhava.py) Madhava of Sangamagrama was an Indian mathematician whose work in infinite series predated similar
# European results by several centuries. In particular, he gave a series for pi which converges more rapidly than the
# Madhava-Leibniz series you worked with in H3:
# Write a Python program which reads an int numTerms, then computes the above approximation to pi using numTerms of the
# above series. As in H3-3, print out the computing estimate and the abs() of its difference from math.pi.
# ----------------------------------------------------------------------------------------------------------------------


import math


def madhavaEstimate(numTerms):
    mul = 3
    summ = 3
    piEstimate = 0
    for i in range(numTerms):            # For loop iteration for pi estimate using Leibniz formula
        if i == 0 or i % 2 == 0:         # assigning the sign value +ve or -ve for the formula
            sign = 1
        else:
            sign = -1
        if i == 0:                      # Assigning summ and mul for i == 0 and i == 1
            summ = 1
            mul = 1
        elif i == 1:
            summ = 3
            mul = 3
        elif i > 1:
            for j in range(i - 1):
                mul = mul * 3
                summ = summ + 2
        piEstimate += sign * (1 / (mul * summ))
    return math.sqrt(12) * piEstimate


def main():
    numTerms = int(input("Enter integer for no. of terms: "))  # User input for numTerms
    finalPiEstimate = madhavaEstimate(numTerms)
    print("Math pi value: ", math.pi)                          # printing the calculated value and the error
    print("Madhava formula estimate is: ", finalPiEstimate)
    print("Error is: ", abs(math.pi - finalPiEstimate))


if __name__ == "__main__":
    main()
