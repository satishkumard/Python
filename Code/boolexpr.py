
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: boolexpr.py
# [H5-1] (boolexpr.py) Write a Boolean (bool) function is_in_semester(month,day) that returns True when month/day falls
# within the dates of the current GPS Spring Semester, which started on January 29 and ends on May 12. If month/day
# falls outside this range (which includes both starting and ending dates), return False.
# Then write a main() function that reads integers month and day from the user, then calls is_in_semester(month,day)and
# prints out the returned result. Finally, call main() as the last statement in your .py file.
# For 1 point of Extra Credit, write your function WITHOUT using ANY if-elif-else NOR if-else statements, NOR ANY
# external modules! Your function can ONLY use the Boolean and, or, not operators and the comparison operators >, >=,
# <, <=, ==, !=, plus any needed parentheses. However, you can assume that month/day is a legal date: you don't have to
# validate it within your function.
# ----------------------------------------------------------------------------------------------------------------------


def is_in_semester(month, day):
    """Function to find if given month and day are within the limits"""
    if (month > 1 and month < 5) or (month == 1 and day >= 29) or (month == 5 and day <= 12):
        return True
    else:
        return False

def is_in_semester_bool(month, day):
    """Function to find if given month and day are within the limits just using boolean function"""
    return (month > 1 and month < 5) or (month == 1 and day >= 29) or (month == 5 and day <= 12)


def main():
    """User inputs and calling the function"""
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    print(is_in_semester(month, day))
    print(is_in_semester_bool(month, day))


if __name__ == "__main__":
    main()

