
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: bjackodds.py
# [H9-2] (bjackodds.py) Use the Card and Deck classes of Lab 9, here provided in separate files card.py and deck.py.
# Use them to write a program which simulates the repeated shuffling of a full deck, then drawing its top two cards and
# checking them for blackjack. "Blackjack" occurs when one card is an Ace, and the other is one of 10, Jack, Queen, or
# King. Your program should calculate the percentage of the time that "blackjack" occurs.
# Run your program multiple times. Do your results agree with theoretical probabilities? Add a comment at the top of
# your submitted file that addresses this question.
# ----------------------------------------------------------------------------------------------------------------------


import deck as d

TRIALS = 10000


def main():
    """
    Repeat the following of TRIALS
    """
    blackjackCount = 0

    for count in range(TRIALS):
        deck = d.Deck()
        deck.shuffle()
        card1 = deck.dealCard()
        card2 = deck.dealCard()
        if card1._rank == 1 and (card2._rank in [10, 11, 12, 13]):
            blackjackCount = blackjackCount + 1
        elif card2._rank == 1 and (card1._rank in [10, 11, 12, 13]):
            blackjackCount = blackjackCount + 1

    print("Percentage of blackjacks is %.2f" % (100 * blackjackCount / TRIALS))


if __name__ == "__main__":
    main()