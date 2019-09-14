
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: andornot.py
# [H5-12] (andornot.py) For 1 point, write a program that prints out the "truth tables" for each of the Python bool
# operators and, or, and not.  You must use two variables A and B, setting them to True and False for each line, then
# printing each of A and B,  A or B, not A, not B, all with appropriate formatting. Your output should look something
# like this:
# |   A   |   B   | A and B | A or B | not A | not B |
# |--------------------------------------------------|
# | True  | True  |  True   |  True  | False | False |
# | True  | False |  False  |  True  | False | True  |
# | False | True  |  False  |  True  | True  | False |
# | False | False |  False  |  False | True  | True  |
# ----------------------------------------------------------------------------------------------------------------------


def main():
    A = [True, False]
    B = [True, False]
    for i in range(2):
        if i == 0:
            print('|', '{!s:^6}'.format('A'), '|', '{!s:^6}'.format('B'), '|', '{!s:^7}'.format('A and B'), '|',
                  '{!s:^6}'.format('A or B'), '|', '{!s:^6}'.format('not A'), '|', '{!s:^6}'.format('not B'), '|')
            print("|------------------------------------------------------|")
        for j in range(2):
            print('|', '{!s:<6}'.format(A[i]), '|', '{!s:<6}'.format(B[j]), '|', '{!s:<7}'.format(A[i] and B[j]), '|',
                  '{!s:<6}'.format(A[i] or B[j]), '|', '{!s:<6}'.format(not A[i]), '|', '{!s:<6}'.format(not B[j]), '|')


if __name__ == "__main__":
    main()

