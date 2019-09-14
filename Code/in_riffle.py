
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: in_riffle.py
# [H9-5] (in_riffle.py) Same as L10-4 but implement a perfect in riffle shuffle by adding to Deck the instance method
# inRiffle(self).  This is similar to the out riffle-shuffle of the Lab.  Here the top card before shuffling becomes the
# second card after interleaving the two deck halves, with the top card of the shuffled deck as the second card of the
# last half of the Deck before shuffling.
# Then write a main() method that experimentally determines the smallest number of perfect in riffle-shuffles needed to
# bring the deck back to its original order.  You'll find it's different than the minimum number of perfect out riffle-
# shuffles to do the same thing. Hint: modify your outRiffle() method and supporting code from L10-4
# ----------------------------------------------------------------------------------------------------------------------


import card as c
import deck as d


def main():
    deck = d.Deck()
    deck.shuffle()
    original_order = str(deck)
    riffleCount = 0
    while True:
        deck.inRiffle()
        riffleCount += 1
        if str(deck) == original_order:
            print("It took %d in riffle-shuffles" % riffleCount)
            break


if __name__ == "__main__":
    main()
