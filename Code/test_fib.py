
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: test_fib.py
# [H4-4] (test_fib.py) Write PyTest unit tests for your fib() function of the previous problem.  You should test your
# function with at least ten (10) different unit test functions (name them test_...), with asserts within each that test
# for 10 different input values.
# ----------------------------------------------------------------------------------------------------------------------


import pytest                           # Import pytest module
import fib                              # Import fib module


def test_fib_2():                       # Test case 1 for value input 0
    assert fib.fibonacci(0) == 0


def test_fib_3():                       # Test case 2 for value input 1
    assert fib.fibonacci(1) == 1


def test_fib_1():                       # Test case 3 for value input 2
    assert fib.fibonacci(2) == 1


def test_fib_4():                       # Test case 4 for value input 5
    assert fib.fibonacci(5) == 5


def test_fib_5():                       # Test case 5 for value input 10
    assert fib.fibonacci(10) == 55


def test_fib_6():                       # Test case 6 for value input 14
    assert fib.fibonacci(14) == 377


def test_fib_7():                       # Test case 7 for value input 12
    assert fib.fibonacci(12) == 144


def test_fib_8():                       # Test case 8 for value input 100
    assert fib.fibonacci(100) == 354224848179261915075


def test_fib_9():                       # Test case 9 for value input 25
    assert fib.fibonacci(25) == 75025


def test_fib_10():                       # Test case 10 for value input 50
    assert fib.fibonacci(7) == 13

