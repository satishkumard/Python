
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: julian.py
# [H5-10] (julian.py) Here's a way of calculating the Julian date daynum of a year, which is the ordinal number of any
# date within the year. For example, January 1 is always Julian date 1, February 1 is Julian date 32, and December 31 is
# Julian date 365 in non-leap years and 366 in leap years. Use int arithmetic in these calculations:
# (1) daynum = 31*(month−1) + day
# (2) If the month is after February subtract (4*month + 23) // 10 from daynum
# (3) If it’s a leap year and after February 29, add 1 to daynum
# Using this algorithm, write a function julian(day,month,year) which returns the Julian date of its arguments. You may
# assume that year is not a leap year (skip step (3)).
# Define a main() function which reads the date from the user as three separate int values; you don't have to verify
# that it's valid.  Then call your function passing the input argument, and print the result. For 0.5 points of Extra
# Credit, add the leap year calculation in (3).
# ----------------------------------------------------------------------------------------------------------------------


def julianDate(day, month, year):
    """Calculate the julian date for given date"""
    daynum = 31 * (month - 1) + day
    if year % 4 != 0:           # Check if the year is not a leap year
        if month > 2:           # Check if the month is greater than Feb
            return daynum - (4 * month + 23)//10
        else:
            return daynum
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Check if the year is a leap year
        if month > 2:           # Check if the month is greater than Feb
            return (daynum - (4 * month + 23)//10) + 1
        else:
            return daynum


def main():
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    print(julianDate(day, month, year))


if __name__ == "__main__":
    main()

