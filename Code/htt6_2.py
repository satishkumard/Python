
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: htt6_2.py
# [H4-5] (htt6_2.py) Do Exercise 2 at the end of HTT Chapter 6, modified as follows.  Read the number N of nested
# squares to draw, then do so, starting with the innermost square of side 20. Each nested square should be centered at
# the origin (0,0).  Note this problem is *much* easier if you define a function that draws a centered square of some
# side length.
# Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is 20 units
# bigger, per side, than the one inside it.
# ----------------------------------------------------------------------------------------------------------------------


import turtle


def squares_gap(alex, iterator, distance):
    """Creating the gap between the squares"""
    alex.penup()
    alex.goto((distance/2) * iterator, -(distance/2) * iterator)
    alex.pendown()


def squares(alex, totalsquares, distance):
    """Drawing the number of squares based on n with distance d between them"""
    for iterator in range(1, totalsquares + 1):
        squares_gap(alex, iterator, distance)
        for j in range(4):
            alex.left(90)
            alex.forward(distance * iterator)


def main():
    wn = turtle.Screen()                                                # Initializing the Screen, color and turtle alex
    wn.bgcolor("Light Green")
    alex = turtle.Turtle()
    alex.pensize(3)
    alex.pencolor("Hot Pink")
    alex.speed(0)
    totalsquares = int(input("Enter number of squares: "))              # User inputs for No of squares and distance
    distance = int(input("Enter the distance between the squares: "))   # between them
    squares(alex, totalsquares, distance)
    wn.exitonclick()


if __name__ == "__main__":
    main()

