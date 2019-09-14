
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: f2c.py
# [H4-1] (f2c.py) Write a program that reads a temperature in degrees Fahrenheit fahr, then converts it to the
# equivalent degrees Celsius and prints the results like this: 32.0 degrees F is equivalent to 0.0 degrees C. Don't
# worry about the number of decimals in your output, but... EC print two dec digits.
# ----------------------------------------------------------------------------------------------------------------------


def f_to_c(fahr):
    """Convert the fahrenheit degrees to Celsius."""
    celsius = (fahr - 32) * (5/9)               # Formula for calculating the fahrenheit to Celsius
    return "{:.2f}".format(celsius)


def main():                                         # Defining the main function
    fahr = float(input("Enter a Fahrenheit value to convert to Celsius: "))   # user input for fahrenheit value
    c = f_to_c(fahr)
    print(fahr, "Fahrenheit degrees is equivalent to", c, "Celsius degrees.")  # Printing the Celsius


if __name__ == "__main__":
    main()                  # calling the main function

