
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: fib_tiling.py
# [H5-11] (fibTiling.py) 1 points Extra Credit Draw this:
# ----------------------------------------------------------------------------------------------------------------------

import turtle
import random


# Was not able to figure out on how to get the number printed in the middle. Will fix this after talking to you.
# def printNumber(fn, alex):
#     """Print the number inside the square"""
#     if fn != 0:
#         alex.penup()
#         x = alex.xcor()
#         y = alex.ycor()
#         print(alex.xcor(), alex.ycor())
#         newx = x - (fn*10/2)
#         newy = y + (fn*10/2)
#         print(newx, newy)
#         alex.goto(newx, newy)
#         alex.pendown()
#         alex.write(str(fn), align="Center")
#         alex.penup()
#         alex.goto(x, y)
#         alex.pendown()


def drawSquare(fn_list, alex, colors):
    """Draw the squares for the given list"""
    for fn in fn_list:
        color = random.choice(colors)
        alex.color(color)
        alex.pencolor("black")
        alex.begin_fill()
        squares(fn, alex)
        #     printNumber(fn, alex)
        alex.end_fill()


def squares(fn, alex):
    """Function for drawing the squares with fibonacci numbers"""
    if fn == 1:
        for i in range(4):
            alex.forward(fn * 10)           # Multiplying fn with 10 to draw a bigger square
            alex.left(90)
        alex.forward(fn * 10)
    elif fn == 2:
        alex.left(90)
        alex.forward(1 * 10)
        for i in range(5):
            alex.forward(fn * 10)
            alex.left(90)
        alex.forward(fn * 10)
    elif fn != 0 and fn != 1 and fn != 2:
        for i in range(5):
            alex.forward(fn * 10)
            alex.left(90)
        alex.forward(fn * 10)


def fibonacciList(n):
    """Function to store all the fibonacci numbers in a list"""
    fibo_list = []   # Creating empty List to store each fibonacci number
    for n in range(n+1):
        fibo_list.append(fibonacci(n))
    return fibo_list


def fibonacci(n):
    """Function for fibonacci for value n"""
    fn = 0
    fn_1, fn_2 = 1, 1
    if n == 1 or n == 2:            # Checking if n is 1 or 2 then fibonacci value is 1
        return fn_1
    else:
        for i in range(n - 2):
            fn = fn_1 + fn_2
            fn_2, fn_1 = fn_1, fn
        return fn


def main():
    """ Initialization and calling other methods"""
    wn = turtle.Screen()
    alex = turtle.Turtle()
    alex.hideturtle()
    alex.pensize(1)
    colors = sorted(["red", "green", "blue", "orange", "purple", "Hot Pink", "yellow"]) # list of color to select
    n = int(input("Enter n:"))
    drawSquare(fibonacciList(n), alex, colors)
    wn.exitonclick()


if __name__ == "__main__":
    main()



# Input:            0 1 2 3 4 5 6 7  8  9
# Fibonacci Number: 0 1 1 2 3 5 8 13 21 34



