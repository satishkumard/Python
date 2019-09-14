
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: test_num2eng.py
# [H5-8] (test_num2eng.py) Write at least 20 different PyTest methods (def test_xxx()) to test your num_to_english(N)
# function of the previous problem. Each method should contain one assert, something like this: assert num_to_
# english(47) == 'forty seven'
# ----------------------------------------------------------------------------------------------------------------------

import pytest
import num2eng4


def test_num2eng1():
    assert num2eng4.num_to_english(47) == 'forty seven'


def test_num2eng_2():
    assert num2eng4.num_to_english(-1) == 'Invalid'


def test_num2eng_3():
    assert num2eng4.num_to_english(100) == 'Invalid'


def test_num2eng_4():
    assert num2eng4.num_to_english(11) == 'eleven'


def test_num2eng_5():
    assert num2eng4.num_to_english(20) == 'twenty'


def test_num2eng_6():
    assert num2eng4.num_to_english(88) == 'eighty eight'


def test_num2eng_7():
    assert num2eng4.num_to_english(17) == 'seventeen'


def test_num2eng_8():
    assert num2eng4.num_to_english(62) == 'sixty two'


def test_num2eng_9():
    assert num2eng4.num_to_english(55) == 'fifty five'


def test_num2eng_10():
    assert num2eng4.num_to_english(32) == 'thirty two'


def test_num2eng_11():
    assert num2eng4.num_to_english(26) == 'twenty six'


def test_num2eng_12():
    assert num2eng4.num_to_english(4) == 'four'


def test_num2eng_13():
    assert num2eng4.num_to_english(95) == 'ninety five'


def test_num2eng_14():
    assert num2eng4.num_to_english(30) == 'thirty'


def test_num2eng_15():
    assert num2eng4.num_to_english(66) == 'sixty six'


def test_num2eng_16():
    assert num2eng4.num_to_english(52) == 'fifty two'


def test_num2eng_17():
    assert num2eng4.num_to_english(77) == 'seventy seven'


def test_num2eng_18():
    assert num2eng4.num_to_english(38) == 'thirty eight'


def test_num2eng_19():
    assert num2eng4.num_to_english(9) == 'nine'


def test_num2eng_20():
    assert num2eng4.num_to_english(29) == 'twenty nine'

