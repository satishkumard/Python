
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: triangles.py
# [H2-5] (triangles.py) Create a Python program using turtle graphics that draws the picture shown at the right. The
# inner equilateral triangle is nested inside the outer equilateral triangle, with the outer having a side of length
# 200. Each vertex of the inner triangle touches the midpoints of sides of the outer square. You can draw your triangles
# anywhere within the screen, but you'll earn 0.5 Extra Credit if both triangles are centered at the origin (0,0).
# ----------------------------------------------------------------------------------------------------------------------

import turtle                   # Importing turtle module

wn = turtle.Screen()            # Initializing screen
wn.bgcolor("White")             # Adding background color
triangle = turtle.Turtle()      # Initializing the turtle
triangle.color("Blue")

triangle.penup()                # Setup to draw outer equilateral triangle
triangle.goto(0, 100)
triangle.pendown()
triangle.right(60)

for i in range(3):              # Outer equilateral triangle
    triangle.forward(200)
    triangle.right(120)

triangle.penup()                # Setup to draw inner equilateral triangle
triangle.right(60)
triangle.goto(0, 100)
triangle.forward(100)
triangle.left(120)
triangle.pendown()
triangle.forward(100)

for i in range(2):              # Inner equilateral triangle
    triangle.right(120)
    triangle.forward(100)

wn.exitonclick()

