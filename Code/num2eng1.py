
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: num2eng1.py
# [H5-4] (num2eng1.py) Define a function digit_to_english(N), which returns a string (str) that is the English
# equivalent of N, for 0 <= N < 10.
# If N is not in this range, return 'Invalid'. You may assume N is a valid int.
# Then write a program whose main() method reads int num from the user, then prints out digit_to_english(num).
# Here are some sample calls and the strings they should return:
# digit_to_english(0) => 'zero'
# digit_to_english(3) => 'three'
# digit_to_english(9) => 'nine'
# digit_to_english(-1) => 'Invalid'
# digit_to_english(10) => 'Invalid'
# Hint: use multiple alternative decisions => if..elif..elif..else
# ----------------------------------------------------------------------------------------------------------------------


def digit_to_english(n):
    """Function which prints number to english for n is between 0 and 10"""
    if n < 0 or n >= 10:
        return 'Invalid'
    elif n == 0:
        return 'zero'
    elif n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'


def main():
    num = int(input("Enter any integer from 0 to 9: "))
    print(digit_to_english(num))


if __name__ == "__main__":
    main()


