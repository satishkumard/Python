
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: unidump.py
# [[H7-2] (unidump.py) Write a program that reads an integer N, then prints out the Unicode characters from chr(32)
# through chr(N-1); that is, print the first N-32 Unicode characters.  Print 32 characters per line, formatted as
# described below. Note we are skipping the first 32 characters chr(0) through chr(31); these are the ASCII control
# characters, which do strange things when printed to the console. (As you will see when you run your code, other later
# Unicode characters will also result in odd output...)
# The Unicode number ord(c) of the first character c of each line should preface the line, right-justified in a field of
# width 6 followed by a colon and a blank, as shown below. The H7 Help Video shows how to do this using the % operator
# in class.
# Use Python's built-in chr(N) which returns the Nth Unicode character. For example, the output for N == 256 should look
# something like this:
# 0032:  !"#$%&'()*+,-./0123456789:;<=>?
# 0064: @ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
# 0096: `abcdefghijklmnopqrstuvwxyz{|}~
# 0128: 
# 0160:  ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿
# 0192: ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß
# 0224: àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
# Keep in mind that the Python console may not display all Unicode characters correctly, and your particular operating
# system may affect which Unicode characters are displayed. Example: in the above output on MacOS X, many of the
# characters in the range chr(127)- chr(150) don't display correctly (and will likely appear differently in your console
# than in the above example).  And… you'll see even stranger output for larger N. Very large N may result in runtime
# errors: don't worry about this.
# ----------------------------------------------------------------------------------------------------------------------


def unicode(N):
    """Function to prints out the Unicode characters from chr(32) through chr(N-1)"""
    unicode = ''
    for value in range(32, N):
        unicode = unicode + chr(value)
    for len in range(32, N, 32):
        lineNumber = str(ord(chr(len))).zfill(4) + ": "         # Formatting the output
        if len == 32:
            print(lineNumber + unicode[:len])                   # Slicing it appropriately and printing the output
        else:
            print(lineNumber + unicode[len-32:len])             # Slicing it appropriately and printing the output


def main():
    N = int(input("Enter integer N: "))
    unicode(N)


if __name__ == "__main__":
    main()

