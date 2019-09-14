
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: num2eng2.py
# [H5-5] (num2eng2.py) Define a function teens_to_english(N), which returns a string (str) that is the English
# equivalent of N, for 10 <= N < 20. This is similar to the previous problem, but handles a different range of inputs.
# If N is not in this range, return 'Invalid'. You may assume N is a valid int. Then write a program whose main() method
#  reads int num from the user, then prints out teens_to_english(num).
# ----------------------------------------------------------------------------------------------------------------------


def teens_to_english(n):
    """Function which prints number to english for n is between 10 and 20"""
    if n < 10 or n >= 20:
        return 'Invalid'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'


def main():
    num = int(input("Enter any integer from 10 to 19: "))
    print(teens_to_english(num))


if __name__ == "__main__":
    main()