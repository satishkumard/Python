
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: poker_odds3.py
# [H9-4] (poker_odds3.py) Refactor your H8 program poker_odds2.py, rewriting it to use the Hand2 class, created as a
# modified version of the previous problem's Hand class.  Refactoring means to change the internal structure of a
# program without changing its external behavior. Thus, when you run your refactored program, it should generate exactly
# the same results as before.
# Part of your refactoring should alter Hand into Hand2 as follows: convert the function buildDict(hand) into a Hand2
# method buildDict(), which builds and returns the same dictionary as before. You should also move each of the five H8
# instance methods isOnePair(dict), ... from H8 into Hand2, modifying them so they have no arguments as methods within
# Hand2.  When called, each should first call the internal buildDict() method to create the necessary dictionary dict,
# then use it to determine what Boolean value to return.
# ----------------------------------------------------------------------------------------------------------------------


import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]


class Card():
    """
    Represents a single playing card,
        whose rank internally is int _rank: 1..13 => "Ace".."King"
        and whose suit internally is int _suit 0..3 => "Clubs".."Spades"
    """

    def __init__(self, rank=1, suit=3):
        '''
        Initialize card with given int suit and int rank
        :param rank:
        :param suit:
        :return:
        '''
        self._rank = rank
        self._suit = suit

    def __str__(self):
        '''
        Return the string name of this card:
        "Ace of Spades": translates int fields to strings
        :return:
        '''

        # "Ace of Spades" is string for self._rank==1, self._suit==3

        toreturn = RANKS[self._rank] + " of " + SUITS[self._suit]

        return toreturn


class Deck():
    """
    Represents a deck of 52 standard playing cards,
        as a list of Card refs
    """

    def __init__(self):
        '''
        Initialize deck: field _cards is list containing
            52 Card refs, initially
        :return: nothing
        '''

        self._cards = []
        for rank in range(1, 14):
            for suit in range(4):
                c = Card(rank, suit)
                self._cards.append(c)

    def __str__(self):
        '''
        "Stringified" deck: string of Card named,
        with \n for easier reading
        :return:
        '''
        toreturn = ''

        # for index in range(len(self._cards)):
        #     self._cards[index]

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            toreturn = toreturn + temp + "\n"  # note \n at end

        return toreturn

    def shuffle(self):
        random.shuffle(self._cards)  # note random function to do this

    def dealCard(self):
        toreturn = self._cards.pop(0)  # get and remove top card from deck
        return toreturn


class Hand2():
    '''
    Collection of Cards dealt from Deck
    '''

    def __init__(self):
        '''
        Initialzes new Hand by adding empty _cards list
        '''
        self._hand = []

    def addCard(self, cardToAdd):
        '''
        Adds cardToAdd to this Hand
        :param cardToAdd:
        '''
        deck = Deck()
        deck.shuffle()
        for card in range(cardToAdd):
            self._hand.append(deck.dealCard())

    def __str__(self):
        '''
        Return string describing all cards in hand
        '''
        result = ''
        for card in self._hand:
            temp = str(card)
            result = result + temp + '\n'
        return result

    def buildDict(self):
        self.dict = {}
        for card in self._hand:
            self.dict[card._rank] = self.dict.get(card._rank, 0) + 1
        return self.dict

    def buildDict2(self):
        self.dict = {}
        for card in self._hand:
            self.dict[card._suit] = self.dict.get(card._suit, 0) + 1
        return dict

    def hasOnePair(self):
        # Check for EXACTLY one value of 2 in dict
        # Note there might be 2 pairs; hence the counting of pairs

        # HOWEVER: there's a problem with this code, as it counts
        #   some hands as having 1 pair when they're not.
        # Hint: Bob Saget... (obscure TV trivia reference)

        twocount = 0
        threecount = 0
        for v in self.dict.values():
            if v == 2:
                twocount += 1
            elif v == 3:
                threecount += 1
        return twocount == 1 and threecount != 1

    def hasTwoPairs(self):
        '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''

        twocount = 0
        for v in self.dict.values():
            if v == 2:
                twocount += 1

        return twocount == 2

    def hasThreeOfAKind(self):
        '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''

        threecount = 0

        for v in self.dict.values():
            if v == 3:
                threecount += 1
        return threecount > 3

    def hasFullHouse(self):
        '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''
        twocount = 0
        threecount = 0
        for v in self.dict.values():
            if v == 3:
                threecount += 1
            elif v == 2:
                twocount += 1

        return twocount > 0 and threecount > 0

    def hasFourOfAKind(self):
        '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''
        fourcount = 0

        for v in self.dict.values():
            if v == 4:
                fourcount += 1
        return fourcount > 0

    def hasStraight(self):
        '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''

        straightcount = 0
        straightstep = 1
        rank_in_hand = list(dict.keys())
        rank_in_hand.sort()
        rank_in_hand_index = 1
        while True:
            if rank_in_hand_index >= len(rank_in_hand):
                break
            else:
                if rank_in_hand[rank_in_hand_index] == rank_in_hand[rank_in_hand_index - 1] + 1:
                    straightstep += 1
                else:
                    straightstep = 1

                if straightstep == 5:
                    straightcount += 1

                rank_in_hand_index += 1

        return straightcount > 0

    def hasFlush(self):
        '''
        Complete this!
        :param dict: dictionary with card ranks to check
        '''

        flushcount = 0
        for v in dict.values():
            if v >= 5:
                flushcount += 1

        return flushcount > 0


def main():
    # finish this...

    TRIALS = 10000  # int(input ("Input number of hands to test: "))

    hand = []  # list of Card in hand

    # accumulators for different counts

    onepairCount = 0
    twopairCount = 0
    threeCount = 0
    fourCount = 0
    fullHouseCount = 0

    # more if you wish...

    for num in range(TRIALS):

        hand = Hand2()
        hand.addCard(6)
        hand.buildDict()

        if hand.hasOnePair():
            onepairCount += 1
        elif hand.hasTwoPairs():
            twopairCount += 1
    ##        elif hasThreeOfAKind(dict):
    ##            threeCount += 1
    ##        elif hasFourOfAKind(dict):
    ##            fourCount += 1
    ##        elif hasFullHouse(dict):
    ##            fourCount += 1

    # add more if you wish...

    # print out results...

    print("Number of one pair hands is: ", onepairCount)

    print("% of hands: ", 100.0 * onepairCount / TRIALS)

    print("Number of two pair hands is: ", twopairCount)

    print("% of hands: ", 100.0 * twopairCount / TRIALS)


def test():
    ''' hardcoded hand, allowing test of hasXXX() methods
    '''

    testhand = [Card(2, 3), Card(1, 2), \
                Card(1, 1), Card(13, 2), \
                Card(2, 0)]

    # here's a hand that seems to have one pair; does it?

    # testhand = [Card(2, 3), Card(1, 2), \
    #             Card(1, 1), Card(1, 3), \
    #             Card(2, 0)]

    dict = buildDict(testhand)

    print("Does handtest contain exactly one pair? %s" % hasOnePair(dict))


def testCard():
    card1 = Card()  # Card(1,3)
    card2 = Card(12, 2)
    card1._newfield = 47

    print(card1.__str__())  # long-winded form
    print(str(card2))
    print(card1._newfield)
    print(card1._rank)
    print(card1._suit)


def testDeck():
    '''
    Test Deck: create, print then shuffle, print again
    Then deal first two cards and print, along with bottom card
    '''
    deck = Deck()
    print(str(deck))

    print("Now we shuffle:\n")

    deck.shuffle()
    print(str(deck))

    c = deck.dealCard()

    c2 = deck.dealCard()

    print("The first card dealt is", str(c), "and the second is", str(c2))
    print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!


if __name__ == "__main__":
    # testCard()  # uncomment to test creating & calling Card methods

    # testDeck()  # uncomment to test Deck: create, print, shuffle, print

    # test() # uncomment to test hand (list of 5 Card obj) for one pair

    main()  # uncomment to run general poker odds calculations
