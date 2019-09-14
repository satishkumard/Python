
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: dec2bin.py
# [H5-13] (dec2bin.py) For 1 point, write a function dec_2_bin(dec) which returns the binary equivalent of decimal
# number dec, dec >= 0, as a string (str).  Do so any way you wish - but the following suggests an approach.
# The posted file dec_2_bin.py contains a while loop that creates and prints the reversed binary equivalent of input num
#  as a string (str).  It also contains a function reverse(s) which returns the reversed str argument s. Create your
# function by combining these two into a single while loop that calculates and returns the binary equivalent of dec,
# in the correct order. If dec is negative, return "Invalid".
# Then create 15 PyTest test functions within a separate file test_dec2bin.py. Each should test a different decimal
# number for its correct conversion to binary.
# ----------------------------------------------------------------------------------------------------------------------


# def dec_2_bin(dec):   # Using the While and For loop
#     """Conversion of Decimal Integer to Binary"""

#     bit_str = ''
#     while dec > 0:
#         bit = dec % 2
#         bit_str = bit_str + str(bit)
#         dec = dec // 2
#     binary = ''
#     for i in bit_str:
#         binary = i + binary
#     return binary


def dec_2_bin(dec):  # Just using the While loop
    """Conversion of Decimal Integer to Binary"""
    bit_str = ''
    binary = ''
    while dec > 0:
        bit = dec % 2
        bit_str = bit_str + str(bit)
        dec = dec // 2
        binary = str(bit) + binary
    return binary


def main():
    dec = int(input("Enter a decimal for binary conversion: "))
    print(dec_2_bin(dec))


if __name__ == "__main__":
    main()