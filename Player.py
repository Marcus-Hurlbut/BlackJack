#from Deck import Deck
from pprint import pprint

class Player:
	def __init__(self):
		self.hand = []
		self.bust = False
		self.money = 0
		self.hand_value = 0

	def turn(self):
		user_turn = 0
		user_turn = int(input('\n\t[*] Enter `0` to Stand or `1` to Hit: '))
		user_turn = int(user_turn)

		while(user_turn < 0 or user_turn > 1):
			print('\n\t[!] Please a correct key - Enter `0` to Stand or `1` to Hit.')
			user_turn = int(input('\t[*] Enter `0` to Stand or `1` to Hit: '))

		self.move = user_turn

		return self.move

	def printHand(self):
		print('\n\t--- Your Hand --- ')
		for card in self.hand:
			print('\t', card.getSuite(), end = ': ')
			print('\t', card.getValue())


	def totalHandValue(self):
		self.hand_value = 0
		for card in self.hand:
			self.hand_value += card.getValue()


	def checkBust(self):
		total_value = 0

		for card in self.hand:
			total_value += card.getValue()

		while(total_value > 21):
			for card in self.hand:
				if card.getValue() == 11:
					card.revertAceValue()
					total_value -= 10
					if (total_value < 22):
						break
			break	

		self.hand_value = total_value		

		if(total_value > 21):
			self.bust = True
			return True
		else:
			return False

