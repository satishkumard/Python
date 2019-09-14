
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: hand.py
# [H9-3] (hand.py) Create a new class Hand, whose objects represent a poker hand of Card instances drawn from a Deck.
# Its constructor should create an empty hand, its instance method addCard(self,card)should add card to the hand, and
# its  __str__(self) method should return a string which lists all the cards currently within the Hand.  Note there may
# be any number of cards within a Hand instance.
# Also define a main() method that does the following: create a new Deck, shuffle it, then create a Hand and add the top
# five cards of the shuffled Deck to it.  Finally, print out the string equivalent of the Hand.
# ----------------------------------------------------------------------------------------------------------------------

import deck as d


class Hand():
    """Collection of Cards dealt from Deck"""

    def __init__(self):
        """Initialzes new Hand by adding empty _cards list"""
        self._hand = []

    def addCard(self,cardToAdd):
        """Adds cardToAdd to this Hand: param cardToAdd:"""
        deck = d.Deck()
        deck.shuffle()
        for card in range(cardToAdd):
            self._hand.append(deck.dealCard())


    def __str__(self):
        """Return string describing all cards in hand"""
        result = ''
        for card in self._hand:
            temp = str(card)
            result = result + temp + '\n'
        return result


def main():
    """Create new Deck, shuffle it, create new Hand, deal top 5 Cards of Deck into it, then print "stringified" Hand"""
    h = Hand()
    h.addCard(5)
    print(h)


if __name__ == "__main__":
    main()

