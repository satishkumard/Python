
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: dec2bin.py
# [H5-13] (test_dec2bin.py) Tests for dec2bin.py
# ----------------------------------------------------------------------------------------------------------------------


import pytest
import dec2bin


def test_dec2bin_1():
    assert dec2bin.dec_2_bin(10) == '1010'

def test_dec2bin_2():
    assert dec2bin.dec_2_bin(100) == '1100100'


def test_dec2bin_3():
    assert dec2bin.dec_2_bin(20) == '10100'


def test_dec2bin_4():
    assert dec2bin.dec_2_bin(5) == '101'


def test_dec2bin_5():
    assert dec2bin.dec_2_bin(9) == '1001'


def test_dec2bin_6():
    assert dec2bin.dec_2_bin(50) == '110010'


def test_dec2bin_7():
    assert dec2bin.dec_2_bin(1000) == '1111101000'


def test_dec2bin_8():
    assert dec2bin.dec_2_bin(235) == '11101011'


def test_dec2bin_9():
    assert dec2bin.dec_2_bin(400) == '110010000'


def test_dec2bin_10():
    assert dec2bin.dec_2_bin(88) == '1011000'


def test_dec2bin_11():
    assert dec2bin.dec_2_bin(666) == '1010011010'


def test_dec2bin_12():
    assert dec2bin.dec_2_bin(10000) == '10011100010000'


def test_dec2bin_13():
    assert dec2bin.dec_2_bin(3455) == '110101111111'


def test_dec2bin_14():
    assert dec2bin.dec_2_bin(5648) == '1011000010000'


def test_dec2bin_15():
    assert dec2bin.dec_2_bin(1) == '1'

