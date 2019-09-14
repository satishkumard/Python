
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: valid.py
# [H5-14] (valid.py) For 1 point, write a program that reads a date month, day, year from the user, then outputs whether
# or not the input date is valid. Examples: 1/47/2018 is not a valid date, nor is 2/29/2018. However, 2/29/2016 is a
# valid date, since 2016 was a leap year.
# Do this by writing a bool function is_valid(month,day,year).  It should return True if the passed date is valid, False
# otherwise. Write a main() program that reads an input date as three separate int values month, day, and year, one at
# a time, then prints out the value returned by your function call.
# Finally, write PyTest unit tests that together test your function's correctness for 15 different dates. Put your
# function in the same .py file as the PyTest unit tests. You should be able to run your valid.py file as either a
# program or as a PyTest test. (test_valid.py is in separate file)
# ----------------------------------------------------------------------------------------------------------------------


def is_valid(month, day, year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and month == 2 and day <= 29:
        return True
    elif month in (4, 6, 9, 11) and day <= 30:
        return True
    elif month in (1, 3, 5, 7, 8, 10, 12) and day <= 31:
        return True
    elif year % 4 != 0 and month == 2 and day <= 28:
        return True
    else:
        return False


def main():
    dateInput = str(input("Enter the date in mm/dd/yyyy format: "))
    month = int(dateInput[0:2])
    day = int(dateInput[3:5])
    year = int(dateInput[6:])
    print(is_valid(month, day, year))


if __name__ == "__main__":
    main()
