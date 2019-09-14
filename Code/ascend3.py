
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: ascend3.py
# [H8-1] (ascend3.py) Find and print all three digit integers abc where a < b < c, a,b,c in '0123456789'. Your integer
# may have leading zeroes, as in 007. Hint: use a triply-nested for-loop, each of the form for d1 in range(10):
# ----------------------------------------------------------------------------------------------------------------------


def main():
    """ Printing all the numbers with range 10 with triple for loop"""
    for hundreds in range(10):
        for tens in range(10):
            for ones in range(10):
                if hundreds < tens and tens < ones:
                    print(hundreds, tens, ones, sep='')


if __name__ == "__main__":
    main()
