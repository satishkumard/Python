
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: fib.py
# [H4-3] (fib.py) Define a function def fib(N) that computes the Nth Fibonacci number F(N) for N >= 0. This is defined
# for n>=0 by the recurrence relation: F(0)==0,F(1)==1, F(n)= F(n-1) + F(n-2) for n>1.
# Do this using a for-loop as follows. Initialize fn_1 and fn_2, then loop a number of times that's related to N. In
# your loop body, calculate fn=fn_1+fn_2 then update fn_1 and fn_2 to the previous values of fn and fn_1, respectively.
#  When the loop ends, fn==F(N) is calculated.
# This can be tricky to get correct for N==0 and N==1. Try initializing fn=1, fn_1=1, fn_2=0 then find the right number
# of times related to N to loop over the calculation so that fn==F(N) is correct for all N...)
# ----------------------------------------------------------------------------------------------------------------------


def fibonacci(n):
    """Function for fibonacci for value n"""
    fn = 0
    fn_1, fn_2 = 1, 1
    if n == 1 or n == 2:            # checking if n is 1 or 2 then fibonacci value is 1
        return fn_1
    else:
        for i in range(n - 2):
            fn = fn_1 + fn_2
            fn_2, fn_1 = fn_1, fn
        return fn


def main():
    while True:
        n = int(input("Enter a integer greater than or equal to zero: "))
        if n < 0:
            print("Number is not valid ")
        else:
            fibo = fibonacci(n)
            print("The", n, "Fibonacci number is", fibo)


if __name__ == "__main__":
    main()



# Input:            0 1 2 3 4 5 6 7  8  9
# Fibonacci Number: 0 1 1 2 3 5 8 13 21 34



