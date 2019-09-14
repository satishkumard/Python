
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: dedupe_list.py
# [H7-3] (dedupe_list.py) Write a program that reads a list directly from the user, then removes duplicate top-level
# elements in it and prints out the resulting list.  You may not use the Python set type to do this problem.
# Use eval(input("input list: ")) to read a list from the user. eval(s) is a built-in Python function which evaluates
# its str argument s, converting it to the proper Python type and returning this value.  (It's the Python interpreter
# as a built-in function.) The starting program contains such code.
# ----------------------------------------------------------------------------------------------------------------------


def dedupeList(myList):
    """Function for de-duping the list"""
    result = []
    for i in myList:            # looping through the items in the list
        if i not in result:     # De-duping the list by checking the item is in the new list if not insert into it.
            result.append(i)
    return result


def main():
    myList = eval(input("Enter a list in proper Python format:"))
    print(dedupeList(myList))


if __name__ == "__main__":
    main()


