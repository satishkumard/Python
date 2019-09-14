
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: test_pokerodds2.py
# [H8-3] (test_pokerodds2.py,test_poker_odds2.py) Continue with Lab 9's L9-4 code, implementing the functions for
# checking if a hand has exactly one pair, two pairs, three of a kind, four of a kind, and full house.  Also implement
# at least 3 py.test tests for each of these kinds of poker hands, putting your tests in the separate file
# test_poker_odds2.py.
# ----------------------------------------------------------------------------------------------------------------------

import pytest
import pokerodds2 as p


def test_hasOnePair_1():
    testhand = [p.Card(2, 3), p.Card(1, 2),	p.Card(3, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert p.hasOnePair(dict)


def test_hasOnePair_2():
    testhand = [p.Card(2, 3), p.Card(1, 2),p.Card(3, 1), p.Card(13, 2), p.Card(4, 0)]
    dict = p.buildDict(testhand)
    assert not p.hasOnePair(dict)


def test_hasOnePair_3():
    testhand = [p.Card(2, 3), p.Card(1, 2),	p.Card(13, 1), p.Card(13, 2),p.Card(12, 0)]
    dict = p.buildDict(testhand)
    assert p.hasOnePair(dict)


def test_hasTwoPairs_1():
    testhand = [p.Card(2, 3), p.Card(1, 2),p.Card(3, 1), p.Card(13, 2),	p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert not p.hasTwoPairs(dict)


def test_hasTwoPairs_2():
    testhand = [p.Card(2, 3), p.Card(1, 2),p.Card(1, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert p.hasTwoPairs(dict)


def test_hasTwoPairs_3():
    testhand = [p.Card(2, 3), p.Card(1, 2),	p.Card(3, 1), p.Card(3, 2),	p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert p.hasTwoPairs(dict)


def test_hasThreeOfAKind_1():
    testhand = [p.Card(2, 3), p.Card(1, 2),	p.Card(3, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert not p.hasThreeOfAKind(dict)


def test_hasThreeOfAKind_2():
    testhand = [p.Card(2, 3), p.Card(1, 2),	p.Card(2, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert p.hasThreeOfAKind(dict)


def test_hasThreeOfAKind_3():
    testhand = [p.Card(2, 3), p.Card(1, 2),	p.Card(13, 1), p.Card(13, 2),p.Card(13, 0)]
    dict = p.buildDict(testhand)
    assert p.hasThreeOfAKind(dict)


def test_hasFourOfAKind_1():
    testhand = [p.Card(2, 3), p.Card(1, 2),p.Card(3, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert not p.hasFourOfAKind(dict)


def test_hasFourOfAKind_2():
    testhand = [p.Card(2, 3), p.Card(2, 2),	p.Card(2, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert p.hasFourOfAKind(dict)


def test_hasFourOfAKind_3():
    testhand = [p.Card(8, 3), p.Card(1, 2),	p.Card(8, 1), p.Card(8, 2),p.Card(8, 0)]
    dict = p.buildDict(testhand)
    assert p.hasFourOfAKind(dict)


def test_hasFullHouse_1():
    testhand = [p.Card(2, 3), p.Card(1, 2),p.Card(3, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert not p.hasFullHouse(dict)


def test_hasFullHouse_2():
    testhand = [p.Card(2, 3), p.Card(2, 2),	p.Card(13, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert p.hasFullHouse(dict)


def test_hasFullHouse_3():
    testhand = [p.Card(8, 3), p.Card(8, 2),	p.Card(8, 1), p.Card(6, 2),	p.Card(6, 0)]
    dict = p.buildDict(testhand)
    assert p.hasFullHouse(dict)


def test_hasStraight_1():
    testhand = [p.Card(2, 3), p.Card(1, 2),	p.Card(3, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict(testhand)
    assert not p.hasStraight(dict)


def test_hasStraight_2():
    testhand = [p.Card(2, 3), p.Card(1, 2),p.Card(3, 1), p.Card(4, 2),p.Card(5, 0)]
    dict = p.buildDict(testhand)
    assert p.hasStraight(dict)


def test_hasStraight_3():
    testhand = [p.Card(9, 3), p.Card(10, 2),p.Card(11, 1), p.Card(13, 2),p.Card(12, 0)]
    dict = p.buildDict(testhand)
    assert p.hasStraight(dict)


def test_hasFlush_1():
    testhand = [p.Card(2, 3), p.Card(1, 2),	p.Card(3, 1), p.Card(13, 2),p.Card(2, 0)]
    dict = p.buildDict2(testhand)
    assert not p.hasFlush(dict)


def test_hasFlush_2():
    testhand = [p.Card(2, 2), p.Card(1, 2),	p.Card(3, 2), p.Card(13, 2),p.Card(8, 2)]
    dict = p.buildDict2(testhand)
    assert p.hasFlush(dict)


def test_hasFlush_3():
    testhand = [p.Card(2, 0), p.Card(1, 0),	p.Card(8, 0), p.Card(13, 0),p.Card(6, 0)]
    dict = p.buildDict2(testhand)
    assert p.hasFlush(dict)


