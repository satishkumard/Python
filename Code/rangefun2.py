
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: rangefun2.py
# [H2-2] (rangefun2.py) Write a program that uses loops of the form:
# to print out each of the sequences below.
# You MUST use a for loop like the above, with range(x,y,z) for some int values of x, y, z for each.
# 1 2 3 4 5 6 7 8 9 10
# 1 3 5 7 9
# 47 1
# 10 9 8 7 6 5 4 3 2 1
# 10 7 4 1
# 1 5 9 13 17 21
# ----------------------------------------------------------------------------------------------------------------------


def rangefun(start, stop, step):             # Function for printing the sequence provided start, stop and step
    for i in range(start, stop, step):
        print(i, end=' ')
    print()                                 # new line


rangefun(1, 11, 1)       # printing sequence 1 2 3 4 5 6 7 8 9 10

rangefun(1, 11, 2)       # printing sequence 1 3 5 7 9

rangefun(47, 0, -46)     # printing sequence 47 1

rangefun(10, 0, -1)      # printing sequence 10 9 8 7 6 5 4 3 2 1

rangefun(10, 0, -3)      # printing sequence 10 7 4 1

rangefun(1, 22, 4)       # printing sequence 1 5 9 13 17 21
