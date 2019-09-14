
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: speeding.py
# [H5-3] (score2grade.py) Write a Python program that reads an int number score from the user in the range from 0 to
# 100, inclusive. Then print out the equivalent letter grade, as per the following curve:
# 90 <= score <= 100 => A
# 80 <= score <= 89  => B
# 70 <= score <= 79  => C
# 60 <= score <= 69  => D
# 0  <= grade <= 59  => F
# You should also check that the entered score is >= 0 and <= 100; otherwise print "Bad input" and quit.
# Hint: use nested if statements. The outer should check the validity of score, with the second nested within the else
# of the first.
# ----------------------------------------------------------------------------------------------------------------------


def gradeCheck(score):
    """Check the score and return the grade"""
    if score < 0 or score > 100:
        message = "Bad Input."
    elif score >= 90 and score <= 100:
        message = "Grade is A."
    elif score >= 80 and score <= 89:
        message = "Grade is B."
    elif score >= 70 and score <= 79:
        message = "Grade is C."
    elif score >= 60 and score <= 69:
        message = "Grade is D."
    elif score >= 0 and score <= 59:
        message = "Grade is F."
    return message


def main():
    score = int(input("Enter the score to find the Grade: "))
    print(gradeCheck(score))


if __name__ == "__main__":
    main()