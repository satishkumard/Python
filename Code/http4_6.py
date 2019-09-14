
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: http4_6.py
# [H3-4] (http4_6.py) Do Exercise 6 at the end of Chapter 4 in your HTT online book.  Hint: you can draw a polygon with
# n sides by repeating the following n times: move forward the length of a side, then turn left 360/n. Study the chapter
# examples to see how to set the color of each side, as well as how to fill your polygon with a given color. You can
# find all legal colors for setting on the Turtle Colors link next to this handout on Canvas, as well as
# here: https://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm.
# Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of
# a regular polygon. The program should draw the polygon and then fill it in.
# ----------------------------------------------------------------------------------------------------------------------

import turtle                       # importing the turtle module


def drawpoly(side, length, color):  # Defining function drawpoly
    wn = turtle.Screen()            # Initializing the screen, turtle and the color
    poly = turtle.Turtle()
    poly.color(color)
    poly.begin_fill()

    for n in range(side):           # Drawing the polygon based on the user input sides and length
        poly.forward(length)
        poly.left(360/side)

    poly.end_fill()

    wn.exitonclick()                # Close the window on click


# Getting user inputs on number of sides, length of side and color to filled for the poylgon
side = int(input("Enter an integer for the number of sides to draw a polygon: "))
length = int(input("Enter an integer for the length of the side: "))
color = input("Enter name of the color to fill the polygon: ")

drawpoly(side, length, color)       # Calling the function drawpoly with user inputs




