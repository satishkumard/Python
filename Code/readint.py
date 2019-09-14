
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: readint.py
# [H8-4] (readint.py) Define a Boolean function read_int() that reads an int value from the user, then returns it as the
# result of the call.  Your function should defend against invalid entry by catching exceptions that occur when trying
# to convert a non-integer to int using int(), then handling them by printing an error message and prompting for
# reentry. Your function should not return until the user has entered a valid integer, with all your exception handling
# within the function body.
# ----------------------------------------------------------------------------------------------------------------------


def read_int():
    """Function to check if the usr input integer is valid if not handle it with exception until it is integer"""
    while True:
        try:
            user_input = input("Enter an integer: ")
            int(user_input)
            break
        except ValueError:
            print("Non-valid int entered. Try again...")
    return user_input


def main():
    return_value = read_int()
    print(return_value)


if __name__ == "__main__":
    main()






