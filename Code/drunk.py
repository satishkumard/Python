
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: drunk.py
# [H2-7] (drunk.py) Modify the code given in HTT4.11 Exercise 7 as follows. Read the number of steps from the user as an
#  int numSteps. Don't move the turtle from its initial home location of (0,0), before you start the loop. In each loop
# iteration, set the turtle's heading to a random value from 0..359, then move the pirate turtle forward 5 units per
# step. (See the PyDoc for the method to set the heading of a turtle.) Thus, the turtle will change its heading to a
# different random direction before making the next step. After the loop terminates, print out the distance from the
# turtle's final position to the origin (0,0). Hint: there's a method to calculate this. To speed up the animation,
# (a) hide the turtle, and (b) set the turtle's speed to 0.  Look up the Turtle API in PyDoc for details.
# ----------------------------------------------------------------------------------------------------------------------

import turtle                           # Importing required modules
import random

wn = turtle.Screen()                    # Initial screen setup, initialize turtle, speed and hide turtle
drunk = turtle.Turtle()
drunk.speed(0)
drunk.hideturtle()

numSteps = int(input("Enter number of steps: "))        # User input for number of steps

for i in range(numSteps):                       # Looping on the steps with random angle with each iteration
    angle = random.randint(0, 359)              # Setting random angle
    drunk.setheading(angle)
    drunk.forward(5)

# the .heading() method gives us the turtle's current heading in degrees
print("The distance from the turtle's final position to the origin(0,0): ", drunk.distance(0, 0))

wn.exitonclick()                                # Closing the screen window on click
