
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: num2eng4.py
# [H5-7] (num2eng4.py) Now define a function num_to_english(N), which returns a string (str) that is the English
# equivalent of N, for 0 <= N <= 100.  If N is outside the legal range, return 'Invalid'.
# Do this any way you can, but try using the functions of the previous three problems.  Write a program whose main()
# method reads int num from the user, then prints out num_to_english(num).
# Examples:
# num_to_english(0) => 'zero'
# num_to_english(3) => 'three'
# num_to_english(12) => 'twelve'
# num_to_english(47) => 'forty seven'
# num_to_english(60) => 'sixty'
# num_to_english(99) => 'ninety nine'
# num_to_english(-1) => 'Invalid'
# Hint: check input num for an invalid range, returning 'Invalid' if so.  Otherwise, break num into tens and ones, where
#  tens is the tens digit of num and ones is the ones digit. For example, if num == 47, tens == 4 and ones == 7.
# Use % and //.
# Then write selection (if-else or if-elif-else) statements that build and the correct str value to return, by calling
# one or more of your previously-defined functions xxx_to_english().
# ----------------------------------------------------------------------------------------------------------------------

import num2eng1
import num2eng2
import num2eng3


def num_to_english(n):
    """Function which prints number to english for n is between 0 and 100"""
    if n < 0 or n >= 100:
        return 'Invalid'
    elif len(str(n)) == 1:
        return num2eng1.digit_to_english(n)
    elif len(str(n)) == 2 and n >= 10 and n < 19:
        return num2eng2.teens_to_english(n)
    elif len(str(n)) == 2 and n >= 20 and int(str(n)[1]) == 0:
        tens = int(str(n)[0])
        return num2eng3.tens_to_english(tens)
    elif len(str(n)) == 2 and n >= 20 and int(str(n)[1]) != 0:
        tens = int(str(n)[0])
        ones = int(str(n)[1])
        return num2eng3.tens_to_english(tens) + ' ' + num2eng1.digit_to_english(ones)


def main():
    num = int(input("Enter an integer between 0 and 100: "))
    print(num_to_english(num))


if __name__ == "__main__":
    main()
