
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: refactor_trace_me.py
# H3-5: run the following in the PyCharm debugger and print
# the following requested info...
# The program is to find the Minimum, Maximum and Average values from the user float inputs
# ----------------------------------------------------------------------------------------------------------------------

nums = int(input("Enter number of floats for Min, Max and Avg: "))  # Request user for the number of floats to compare

maximumFloat = 0.0          # setting the initial values for max, min and avg
minimumFloat = 0.0
averageFloat = 0.0

for num in range(nums):
    compareFloat = float(input("Enter the float to compare: "))     # User inputs for the floats
    if num == 0 and compareFloat < maximumFloat:  # This program will not work for negative and positive integers for
        maximumFloat = compareFloat - 1           # calculating the max and min when the first user value is less or
    if num == 0 and compareFloat > minimumFloat:  # greater than zero for the first iteration. Adding If statement to
        minimumFloat = compareFloat + 1           # set the right values for comparing.
    maximumFloat = max(maximumFloat, compareFloat)
    minimumFloat = min(minimumFloat, compareFloat)
    averageFloat = averageFloat + compareFloat

averageFloat = averageFloat / nums                          # Calculating the average
print("The Maximum among the floats is: ", maximumFloat)    # Printing the Max, Min and Average values to the user
print("The Minimum among the floats is: ", minimumFloat)
print("The Average among the floats is: ", averageFloat)




