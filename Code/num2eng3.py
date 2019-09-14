
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: num2eng3.py
# [H5-6] (num2eng3.py) Define a function tens_to_english(N), which returns a string (str) that is the English equivalent
#  of N*10, for 2 <= N < 10. For example, tens_to_english(2) should return 'twenty', etc., up to tens_to_english(9)
# returning 'ninety'.
# If N is not in this range, return 'Invalid'. You may assume N is a valid int. Then write a program whose main() method
#  reads int num from the user, then prints out tens_to_english(num).
# ----------------------------------------------------------------------------------------------------------------------


def tens_to_english(n):
    """Function which prints integer to tens * number in english for n is between 2 and 10"""
    if n < 2 or n >= 10:
        return 'Invalid'
    elif n == 2:
        return 'twenty'
    elif n == 3:
        return 'thirty'
    elif n == 4:
        return 'forty'
    elif n == 5:
        return 'fifty'
    elif n == 6:
        return 'sixty'
    elif n == 7:
        return 'seventy'
    elif n == 8:
        return 'eighty'
    elif n == 9:
        return 'ninety'


def main():
    num = int(input("Enter any integer from 2 to 9: "))
    print(tens_to_english(num))


if __name__ == "__main__":
    main()