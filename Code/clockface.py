
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: clockface.py
# [H2-6] Write a program to draw a face of a clock
# ----------------------------------------------------------------------------------------------------------------------

import turtle  # Importing turtle module

wn = turtle.Screen()        # Initializing screen
wn.bgcolor("Light Green")   # Adding background color
rob = turtle.Turtle()       # Initializing the turtle - shape, color
rob.shape("turtle")
rob.color("Blue")
rob.penup()

for i in range(12):  # Looping 12 times for the shape of the clock
    rob.left(30)
    rob.forward(80)
    rob.pendown()
    rob.forward(10)
    rob.penup()
    rob.forward(10)
    rob.stamp()
    rob.forward(-100)

wn.exitonclick()            # Closing the window on user click

