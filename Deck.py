import random

from Card import Card

ACE = 11

class Deck:
	def __init__(self):
		self.deck = []
		self.shuffle()


	# Shuffles new deck
	def shuffle(self):
		# Initialize Card values
		suites = ['heart', 'diamond', 'club', 'spade']
		deck = []

		# Create New Cards for Deck
		for suite in suites:
			for val in range(1, 14):
				# Account for Ace Cards - Change to 1 later if needed
				if(val == 1):
					val = ACE

				# Account for Face Cards (11: Jack, 12: Queen, 13: King  -  All are worth value `10`)
				elif (val > 10):
					val = 10

				# Create a new Card Object
				card = Card(suite, val)
				self.deck.append(card)

		# Shuffle Deck of Card Objects - shuffle multiple times to simulate multiple card shuffles when playing game in real life
		for i in range(1,10):
			random.shuffle(self.deck)

		# Dealer sometimes 'burns' the top card of the deck - this simulates that
		burnt_card = self.deck.pop()




