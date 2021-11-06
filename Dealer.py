from pprint import pprint

class Dealer:
	def __init__(self):
		self.hand = []
		self.bust = False
		self.hand_value = 0

	# Print Dealers Face Card w/ formatting
	def printFaceCard(self):
		print('\n\t--- Dealers Face Card ---')
		for card in self.hand:
			print('\t', card.getSuite(), end = ': ')
			print('\t', card.getValue())
			break


	# Print Dealers hand w/ formatting
	def printHand(self):
		print('\n\t--- Dealers Hand ---')
		for card in self.hand:
			print('\t', card.getSuite(), end = ': ')
			print('\t', card.getValue())


	# Calculate Value in Dealer's Hand
	def totalHandValue(self):
		for card in self.hand:
			self.hand_value += card.getValue()



	# Soft17 rule logic
	def softSeventeen(self):
		total_value = 0
		for card in self.hand:
			total_value += card.getValue()

		if (total_value < 17):
			return True
		else:
			return False


	# Check if Dealer Busts & set Ace values to 1 when needed
	def checkBust(self):
		total_value = 0
		for card in self.hand:
			total_value += card.getValue()

		# Find Ace card and change to value 1
		while(total_value > 21):
			for card in self.hand:
				if card.getValue() == 11:
					card.setValue(1)
					total_value -= 10

					if (total_value < 22):
						break
			break		

		# Set Hand Value
		self.hand_value = total_value

		# Determine Bust
		if(total_value > 21):
			self.bust = True
			return True
		else:
			return False
