
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: rand10.py
# [H3-1] (rand10.py) Write a program that prints out 10 random integers, each in the range 1 through 6.
# ----------------------------------------------------------------------------------------------------------------------

import random                               # importing the random module

for integer in range(10):                   # for loop iteration with range 10
    randInteger = random.randrange(1, 6)    # use randint function from random module to choose integer  range 1 and 6
    print(randInteger)
