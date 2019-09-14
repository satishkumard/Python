
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: strip_comments.py
# [H7-4] (strip_comments.py) Write a program that reads a string fname from the user, then opens the file fname.py
# (Python source) with that name.  Copy each of its lines into a new file named 'strip_' + fname.py, deleting all Python
# comments as you go. Recall these begin with a # anywhere on a line and continue to the end of the line. Your
# output .py file should still be a valid program.
# ----------------------------------------------------------------------------------------------------------------------

# strip_comments.py:
#
#   Starting code H7-4
#

# read string fname from user

# open Python source file named fname.py for reading

# create new file 'strip_' + fname.py for writing

# for each line in fname file:

# read line remove comments: starting at # and going to end of line

# write modified line to output file

# close both files


def removeComment(fileName):
    """Funtion to remove the comments from the given .py file"""
    file = open(fileName, 'r')
    new_file = open('strip_' + fileName, 'w')
    for var in file.readlines():
        if '#' in var:              # Checking the # value in the line
            var.index('#')
            new_file.write(var[:var.index('#')] + '\n')
        else:
            new_file.write(var)
    file.close()
    new_file.close()


def main():
    fileName = input("Enter the .py filename to remove the comments:")
    removeComment(fileName)


if __name__ == "__main__":
    main()