
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: htt9_ex12.py
# [H6-5] (htt9_ex12.py) Do Exercise 12 at the end of HTT9.  Name your function remove_all(substr,theStr) and declare a
# main() method which prompts the user to enter a string s, followed by a substring sub to remove, then call and print
# the result of calling remove_all(sub,s).
# ----------------------------------------------------------------------------------------------------------------------


def remove_all(substr, theStr):
    """Find substring in the given string and remove it"""
    newStr = theStr[:]
    index = theStr.find(substr)
    while index >= 0:
        newStr = newStr[:index] + newStr[index+len(substr):]
        index = newStr.find(substr)
    return newStr


def main():
    str = input("Enter the string: ")
    sub = input("Enter the substring which needs to be removed: ")
    print(remove_all(sub, str))
    print(str.replace(sub, ''))  # Using built in replace function


if __name__ == "__main__":
    main()