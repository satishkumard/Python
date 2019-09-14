
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: count_alice3.py
# [H8-2] (count_alice3.py) Continue with refining your H7-1 count_alice2.py code, which reads and analyzes alice.txt and
# prints out all lower-cased words in the text file without words including unnecessary punctuation. Extend it by using
# a dictionary to count the frequency of each word, as described in HTT12 Exercise 17.
# ----------------------------------------------------------------------------------------------------------------------


import string


def main():
    FILENAME = 'alice.txt'
    fvar = open(FILENAME, 'r')  # open file for reading

    stripwords = []                                 # accumulate the stripped words in this list

    for aline in fvar:                              # Looping through each line in the file
        line = aline.lower()
        line = line.replace('--', '')
        line = line.replace(')', '')
        words = line.split()                        # splits the line on whitespace (blanks, '\n', '\t')
        for word in words:                          # Looping through each in the line
            while word[0] in string.punctuation:    # Checking the special character at the starting of the word
                word = word.strip(word[0])
            while word[-1] in string.punctuation:   # Checking the special character towards the end of the word
                word = word.strip(word[-1])
            stripwords.append(word)

    stripwords = list(stripwords)
    stripwords.sort()
    counts = {}  # initialize dictionary counts to empty
    for word in stripwords:
        counts[word] = counts.get(word, 0) + 1

    for key, value in counts.items():       # print the output as required format
        print("%s - %d" % (key, value))

    fvar.close()                            # Closing the file


if __name__ == '__main__':
    main()
