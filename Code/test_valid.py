
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: test_valid.py
# [H5-14] (test_valid.py) For 1 point, write a program that reads a date month, day, year from the user, then outputs
# whether or not the input date is valid. Examples: 1/47/2018 is not a valid date, nor is 2/29/2018. However, 2/29/2016
# is a valid date, since 2016 was a leap year.
# Do this by writing a bool function is_valid(month,day,year).  It should return True if the passed date is valid, False
# otherwise. Write a main() program that reads an input date as three separate int values month, day, and year, one at
# a time, then prints out the value returned by your function call.
# Finally, write PyTest unit tests that together test your function's correctness for 15 different dates. Put your
# function in the same .py file as the PyTest unit tests. You should be able to run your valid.py file as either a
# program or as a PyTest test. (test_valid.py is in separate file)
# ----------------------------------------------------------------------------------------------------------------------

import pytest
import valid


def test_valid_1():
    assert valid.is_valid(2, 29, 2018) == False


def test_valid_2():
    assert valid.is_valid(2, 29, 2016) == True


def test_valid_3():
    assert valid.is_valid(4, 29, 2007) == True


def test_valid_4():
    assert valid.is_valid(1, 47, 2018) == False


def test_valid_5():
    assert valid.is_valid(3, 20, 2009) == True


def test_valid_6():
    assert valid.is_valid(4, 31, 2010) == False


def test_valid_7():
    assert valid.is_valid(5, 30, 2011) == True


def test_valid_8():
    assert valid.is_valid(6, 31, 2012) == False


def test_valid_9():
    assert valid.is_valid(7, 15, 2013) == True


def test_valid_10():
    assert valid.is_valid(8, 20, 2014) == True


def test_valid_11():
    assert valid.is_valid(2, 29, 2005) == False


def test_valid_12():
    assert valid.is_valid(9, 26, 2004) == True


def test_valid_13():
    assert valid.is_valid(10, 29, 2015) == True


def test_valid_14():
    assert valid.is_valid(11, 31, 2015) == False


def test_valid_15():
    assert valid.is_valid(12, 25, 2017) == True

