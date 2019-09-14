
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: leap.py
# [H5-9] (leap.py) Write a bool function isLeap(year) which returns True if year is a leap year, and False otherwise.
# The year y is a leap year if and only if if y is evenly divisible by 4, but not by 100 - or if y is evenly divisible
# by 400.
# ----------------------------------------------------------------------------------------------------------------------


def isLeap(year):
    """Check if the year is leap year"""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def main():
    year = int(input("Enter year to check if it is a leap year: "))
    print(isLeap(year))


if __name__ == "__main__":
    main()


# test: not leap year - 1900, 2100, 2200, 2300, 2500
#       leap year - 2000, 1996, 1992


