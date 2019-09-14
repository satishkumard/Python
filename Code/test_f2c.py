
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: test_f2c.py
# [H4-2] (test_f2c.py) Write PyTest unit tests for your f2c() function of the previous problem.  You should test
# your function with at least ten (10) different unit test functions (name them test_...), with asserts within each that
#  test for 10 different input values.
# ----------------------------------------------------------------------------------------------------------------------

import pytest
import f2c


def test_f2c_1():                           # Test case 1
    assert f2c.f_to_c(32) == '0.00'


def test_f2c_2():                           # Test case 2
    assert f2c.f_to_c(-40) == '-40.00'


def test_f2c_3():                           # Test case 3
    assert f2c.f_to_c(110) == '43.33'


def test_f2c_4():                           # Test case 4
    assert f2c.f_to_c(100) == '37.78'


def test_f2c_5():                           # Test case 5
    assert f2c.f_to_c(-25) == '-31.67'


def test_f2c_6():                           # Test case 6
    assert f2c.f_to_c(0) == '-17.78'


def test_f2c_7():                           # Test case 7
    assert f2c.f_to_c(78) == '25.56'


def test_f2c_8():                           # Test case 8
    assert f2c.f_to_c(18) == '-7.78'


def test_f2c_9():                           # Test case 9
    assert f2c.f_to_c(-18) == '-27.78'


def test_f2c_10():                          # Test case 10
    assert f2c.f_to_c(72) == '22.22'



