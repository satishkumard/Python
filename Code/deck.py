'''
Represents a standard deck of 52 playing cards,
requiring Card import
'''

#
# deck.py:
#
# 	Starting code for L10
#

import random
import card

class Deck():
	"""
	Represents a deck of 52 standard playing cards,
		as a list of Card refs
	"""

	def __init__(self):
		'''
		Initialize deck: field _cards is list containing
			52 Card refs, initially
		'''

		self._cards = []
		for rank in range(1, 14):
			for suit in range(4):
				c = card.Card(rank, suit)
				self._cards.append(c)

	def __str__(self):
		'''
		"Stringified" deck: string of each Card,
		concatenated with '\n' for easier reading
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

	## L10-1: add new method randomCard()

	def randomCard(self):
		rank = random.randint(1,13) # randrange(1,14)
		suit = random.randint(0,3) # randrange(0,4)

		c = card.Card(rank,suit)

		return c

	## L10-3: add new method dealHand()

	def dealHand(self):
		hand = []
		for count in range(5):
			try:
				c = self.dealCard()
			except IndexError:
				self.__init__()
				c = self.dealCard()

			hand.append(c)

		return hand

	## L10-4: add new method outRiffle()

	def outRiffle(self):
		top_half = []
		bottom_half = []

		# deal half of deck into top_half

		for count in range(len(self._cards)//2):
			c = self.dealCard()
			top_half.append(c)

		# deal remaining in self._cards into bottom_half

		for c in self._cards:
			bottom_half.append(c)

		# clear out current Deck's cards

		self._cards=[]

		for c in top_half:
			self._cards.append(c)
			bc = bottom_half.pop(0)
			self._cards.append(bc)

		for c in bottom_half:
			self._cards.append(c)

	# H9-4: add new method inRiffle()

	def inRiffle(self):
		odd_half = []
		even_half = []

		for count in range(len(self._cards)):
			if count % 2 == 0:
				odd_half.append(self._cards[count])
			else:
				even_half.append(self._cards[count])

		self._cards = []

		for card in even_half:
			self._cards.append(card)
			oc = odd_half.pop(0)
			self._cards.append(oc)

		for card in odd_half:
			self._cards.append(card)

def main():
	'''
	Create, print then shuffle, print again
	Then deal first two cards and print, along with bottom card
	'''

    # create and print new Deck

	deck = Deck()
	print(str(deck))

    # shuffle and print Deck

	print("Now we shuffle:\n")

	deck.shuffle()
	print(str(deck))

    # deal two cards from Deck, and report them

	c = deck.dealCard()
	c2 = deck.dealCard()

	print("The first card dealt is", str(c), "and the second is", str(c2))
	print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!

if __name__ == "__main__":
	main()
