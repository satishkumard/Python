
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: patterns2.py
# [H6-2] (patterns2.py) (2 points each) Write a program that reads an int N >= 0, then prints out each of the following
# patterns of *. However, you CANNOT use the string repetition operator *!   Also, each pattern must be output via a
# single function call to the given named function with single parameter N. Examples for N==4 follow, with explanations
# of how the displayed diagram reflects this value of N:
# (a) def triangle(N) => N lines, all right justified: first with N stars, second with N-1, ... Nth with 1 star):
# ****
#  ***
#   **
#    *
# (b) def hollow_box(N) => N lines, first and last with N stars, others with star in first and Nth column:
# ****
# *  *
# *  *
# ****
# (c) def solid_diamond(N) => 2*N+1 lines, first with 1 star, second with 3 stars, ..., N+1 line with 2*N-1 stars, then
# subsequent lines repeating the pattern, reversed; each line's stars are centered between first and Nth columns:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# (d) def hollow_diamond(N) => same as above, but with no interior stars (no 2 stars adjacent on same line):
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
# ----------------------------------------------------------------------------------------------------------------------


def triangle(n):
    """N lines, all right justified: first with N stars, second with N-1, ... Nth with 1 star"""
    totalStars = ''
    for row in range(n, 0, -1):
        stars = ''
        for column in range(row):
            stars = "*" + stars
        if row != n:
            for k in (range(n - row)):
                stars = ' ' + stars
        totalStars = totalStars + "\n" + stars
    return totalStars


def hollow_box(n):
    """first and last with N stars, others with star in first and Nth column"""
    stars = ''
    for i in range(n):
        stars = stars + '*'
        for j in range(n):
            if i == 0 or i == n-1 or j == n-1:
                stars = stars + '*'
            else:
                stars = stars + ' '
        stars = stars + "\n"
    return stars


def solid_diamond(n):
    """2*N+1 lines, first with 1 star, second with 3 stars, N+1 line with 2*N-1 stars"""
    for seq in range(n):            # First half of the solid diamond
        spaces = (n - seq) * ' '
        stars = (2 * seq + 1) * '*'
        print(spaces + stars)
    for seq in range(n, -1, -1):    # Second half of the solid diamond
        spaces = (n - seq) * ' '
        stars = (2 * seq + 1) * '*'
        print(spaces + stars)


def hollow_diamond(n):
    """Hollow Diamond no interior stars (no 2 stars adjacent on same line)"""
    for seq in range(n):            # First half of the hollow diamond
        if seq == 0:
            spaces = (n - seq) * ' '
            stars = '*'
            print(spaces + stars)
        else:
            spaces = (n - seq) * ' '
            stars = '*'
            spaces2 = (2 * seq - 1) * ' '
            stars2 = '*'
            print(spaces + stars + spaces2 + stars2)
    for seq in range(n, -1, -1):    # Second half of the hollow diamond
        if seq == 0:
            spaces = (n - seq) * ' '
            stars = '*'
            print(spaces + stars)
        else:
            spaces = (n - seq) * ' '
            stars = '*'
            spaces2 = (2 * seq - 1) * ' '
            stars2 = '*'
            print(spaces + stars + spaces2 + stars2)


def main():
    n = int(input("Enter a value for n: "))
    print(triangle(n))
    print()
    print(hollow_box(n))
    solid_diamond(n)
    print()
    hollow_diamond(n)


if __name__ == "__main__":
    main()
