
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: threelines.py
# [H2-1] (threelines.py) Write a program draws the picture to the right:
# Each line is of length 200 and separated from the next line by 30 units. The bottom end of the leftmost line is at
# (0,0) (the turtle's home location), and all lines are of width 3. (HTT4 has a code example that shows how to set the
# pen width for a turtle.)
# ----------------------------------------------------------------------------------------------------------------------

import turtle  # Importing turtle module

wn = turtle.Screen()        # Initializing screen
wn.bgcolor("White")         # Adding background color
lines = turtle.Turtle()     # Initializing the turtle
lines.pensize(3)            # Setting line width
lines.right(90)


for i in (60, 30, 0):
    lines.penup()
    lines.goto(i, 200)      # Moving to the co-ordinates x, y
    lines.pendown()
    lines.forward(200)      # Drawing the line

wn.exitonclick()            # Closing the window on user click

