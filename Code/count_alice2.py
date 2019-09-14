
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: count_alice2.py
# [H7-1] (count_alice2.py) Continue with refining your Lab 8 count_alice.py code, which reads and analyzes alice.txt.
# Your goal is to create a program that prints out a list of all lower-cased words in the text file without words
# including unnecessary punctuation. They should be printed in ascending alphabetic order, one per line.
# ----------------------------------------------------------------------------------------------------------------------

import string


def main():
    FILENAME = 'alice.txt'
    fvar = open(FILENAME, 'r')  # open file for reading

    stripwords = []                                 # accumulate the stripped words in this list

    for aline in fvar:                              # Looping through each line in the file
        line = aline.lower()
        line = line.replace('--', '')
        words = line.split()                        # splits the line on whitespace (blanks, '\n', '\t')
        for word in words:                          # Looping through each in the line
            while word[0] in string.punctuation:    # Checking the special character at the starting of the word
                word = word.strip(word[0])
            while word[-1] in string.punctuation:   # Checking the special character towards the end of the word
                word = word.strip(word[-1])
            stripwords.append(word)

    stripwords = list(set(stripwords))      # Making the list as distinct words by using set function
    stripwords.sort()
    for word in stripwords:                 # Print the words
        print(word)

    fvar.close()                            # Closing the file


if __name__ == '__main__':
    main()
