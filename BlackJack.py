from Player import Player
from Deck import Deck
from Dealer import Dealer
import time
from string import punctuation

class BlackJack:
	def __init__(self):
		self.deck = Deck() 						# Deck Object
		self.player = Player()  				# Player Object
		self.dealer = Dealer() 					# Dealer Object
		self.playAgain = 1						# Play Again Flag
		self.winner = 'None'					# Round winner
		self.score = {'Dealer':0, 'Player':0}	# Score Board
		self.roundNumber = 1


	def start(self):
		anotherRound = 1
		self.printWelcomeStatement()
		self.determineDifficulty()

		while(anotherRound == 1):
			self.player.bust = False
			self.dealer.bust = False
			self.winner = 'None'	
			anotherRound = self.gameHandler()
			if(anotherRound == True):
				self.printRoundStatement()


		print('[*] Thanks for playing BlackJack!')
		print('[!] Exiting...')
		return False


	def gameHandler(self):
		# Initial Bet
		self.initialBet()

		# Initial Deal
		self.initialDeal()

		# Player action
		self.playerAction()

		# Dealer action
		self.dealerAction()

		# Access Round Winner
		self.determineWinner()

		# Increment Score
		self.scoring()

		# Settle Bets
		self.settleBets()

		# Re-Shuffle Deck
		self.shuffleDeck()

		# Play Again?
		return self.keepPlaying()

	def determineDifficulty(self):
		self.player.money = int(input("[*] Enter your starting money amount: "))



	def initialBet(self):
		print("\n[*] Initial Bet...")
		print('\n\tYour total Money: ', self.player.money)
		self.player.bet_amount = int(input("\tEnter your initial Bet: "))
		pass


	def initialDeal(self):
		print("\n[*] Initial Deal...")

		# Player Hand
		self.player.hand = []
		self.player.hand.append(self.deck.deck.pop())
		self.player.hand.append(self.deck.deck.pop())

		# Dealer hand - 2 cards: one face up
		self.dealer.hand = []
		self.dealer.hand.append(self.deck.deck.pop())
		self.dealer.hand.append(self.deck.deck.pop())

		# Print Player's Hand & Dealer's Face Card
		self.player.printHand()
		self.dealer.printFaceCard()


	def playerAction(self):
		print("\n[*] Player Action...")

		# Get Player's move
		self.player.move = 1
		self.player.bust = False

		# Loop until Player 'Stands' or Player Busts
		while(self.player.move != 0 and self.player.bust == False):

			# Get player's move
			self.player.move = int(self.player.turn())

			# Player 'Hits'
			if(self.player.move == 1):
				self.player.hand.append(self.deck.deck.pop()) 	# Add Card to Hand
				self.player.checkBust()							# Determine Bust
				self.player.printHand()							# Print new Hand

				# Get Player's turn again if they did not bust
				if(self.player.bust == True):
					break
			# Player 'Stands'
			elif(self.player.move == 0):
				self.player.totalHandValue()
				break




	def dealerAction(self):
		# Dealer automatically wins if player busts
		if(self.player.bust == False):
			print("\n[*] Dealer Action...")

			# Print Dealer's entire hand - revealing face-down card
			self.dealer.printHand()

			# Soft 17 rule - Once every player has gone the dealer then hits until they reach at least 17
			while(self.dealer.softSeventeen()):
				# Used to better simulate real-life timing
				time.sleep(1.5) 	

				print("\n[*] Dealer Hits...")

				# Add card to Dealers hand
				self.dealer.hand.append(self.deck.deck.pop())


			# Determine Bust
			if not(self.dealer.checkBust()):
				time.sleep(1.5) 	# Used to better simulate real-life timing
				print("\n[*] Dealer Stands...")

			self.dealer.printHand()
			

	# Determine the winner from this round from calculations & Print Results
	def determineWinner(self):
		print("\n[*] Results of Round...")

		# Player Busts
		if(self.player.bust == True):
			self.winner = 'Dealer'
			print('\tSorry, You busted this round! Your Hand Value: ', self.player.hand_value)
			print_hand_val = self.player.hand_value

		# Dealer Busts
		elif(self.dealer.bust == True):
			self.winner = 'Player'
			print('\n\tThe Dealer busted this round! Dealer Hand Value: ', self.dealer.hand_value)
			print_hand_val = self.dealer.hand_value

		# Win by Highest Hand
		else:
			# Dealer has higher hand value
			if (self.dealer.hand_value > self.player.hand_value):
				self.winner = 'Dealer'
				print_hand_val = self.dealer.hand_value

			# Tie - Dealer automatically wins
			elif(self.dealer.hand_value == self.player.hand_value):
				self.winner = 'Dealer'
				print_hand_val = self.dealer.hand_value
				print('\n\tThis Round was a Tie, Dealer wins by defualt! Dealer Hand Value: ', self.dealer.hand_value)

			# Player has higher hand value
			else:
				self.winner = 'Player'
				print_hand_val = self.player.hand_value

		print('\n\t--- Round Scoring: ---\n\tPlayer: ', self.player.hand_value, '\n\tDealer: ', self.dealer.hand_value, '\n')
		print('\t', (self.winner), 'won this round with a higher score! Hand Value: ', print_hand_val)



	def scoring(self):
		self.score[self.winner] += 1
		print("\n\t--- Overall Score ---")
		print('\tPlayer Score: ', self.score['Player'])
		print('\tDealer Score: ', self.score['Dealer'])


	def settleBets(self):
		if(self.winner == 'Dealer'):
			self.player.money -= self.player.bet_amount
		else:
			self.player.money += self.player.bet_amount

		print('\n\tCurrent money amount: $', self.player.money)
		self.player.bet_amount = 0


	def keepPlaying(self):
		self.playAgain = int(input('\n[*] Would you like to play another round: [1 for `Yes` / 0 for `No`]: '))

		# Entry Handling
		while(self.playAgain > 1 or self.playAgain < 0):
			print('[!] Please enter a valid key. ')
			self.playAgain = int(input('\n[*] Would you like to play another round. [1 for `Yes` / 0 for `No`]'))

		# End game session
		return self.playAgain



	def shuffleDeck(self):
		self.deck = Deck() 	# Instantiates a New shuffled Deck (Makes more sense than to shuffle current deck object)





	# Text GUI Welcome Statement
	def printWelcomeStatement(self):
		message = [" "]
		set(punctuation)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
		print('                                                              @*                 ')
		print('        *%%%%%%%#,    .(#######*                            &@@@@@,              ')
		print('      %%%%%%%%%%%%%//%############                       ,@@@@@@@@@@#            ')
		print('     %%%%%%%%%%%%%%#%%#############                    /@@@@@@@@@@@@@@@.         ')
		print('    .%%%%%%%%%%%%%%%%%#############,                 %@@@@@@@@@@@@@@@@@@@,       ')
		print('   .%%%%%%%%%%%%%%%%%#############.              .@@@@@@@@@@@@@@@@@@@@@@@@*      ')
		print('    ,%%%%%%%%%%%%%%%%############*              %@@@@@@@@@@@@@@@@@@@@@@@@@@@.    ')
		print('      %%%%%%%%%%%%%%%###########.              #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.   ')
		print('        #%%%%%%%%%%%%#########.                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(   ')
		print('          /%%%%%%%%%%######(                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,   ')
		print('            ,%%%%%%%%####*                     .@@@@@@@@@@@@@@@@@@@@@@@@@@@@#    ')
		print('              .#%%%%%#%.                         /@@@@@@@@@@@@@@@@@@@@@@@@@.     ')
		print('                 /%%(                                 ..  &@@@@@@@, ..           ')
		print('                 ....                                   @@@@@@@@@@@@*            ')
		print('                                                                                 ')
		print('                             WELCOME TO BLACKJACK!                               ')
		print('              ./@@@@&,         ~ Marcus Hurlbut ~                                ')
		print('           .@@@@@@@@@@@@&                                    ##,                 ')
		print('          %@@@@@@@@@@@@@@@*                                #%%%#%,               ')
		print('         .@@@@@@@@@@@@@@@@@                              (%%%%%%###.             ')
		print('         .@@@@@@@@@@@@@@@@%                            *%%%%%%%%#####.           ')
		print('       ./%&@@@@@@@@@@@@@@@@@&*                       ,%%%%%%%%%%######(          ')
		print('    *@@@@@@@@@@@@@@@@@@@@@@@@@@@/                  ,%%%%%%%%%%%%########/        ')
		print('   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               .%%%%%%%%%%%%%%##########*      ')
		print('  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,               %%%%%%%%%%%%%%##########,      ')
		print('  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                .%%%%%%%%%%%%########*        ')
		print('   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                   .%%%%%%%%%%######/          ')
		print('     /@@@@@@@@@@&@@@%@@@@@@@@@(                        ,%%%%%%%%####(            ')
		print('               /@@@@@.                                   *%%%%%%###              ')
		print('            ,%@@@@@@@@@(.                                  /%%%#%.               ')
		print('           .////////////*                                    (%,                 ')
		print('               ......                                                            ')





	# Text GUI Round Start
	def printRoundStatement(self):
		self.roundNumber += 1
		set(punctuation)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
		print('                                                              @*                 ')
		print('        *%%%%%%%#,    .(#######*                            &@@@@@,              ')
		print('      %%%%%%%%%%%%%//%############                       ,@@@@@@@@@@#            ')
		print('     %%%%%%%%%%%%%%#%%#############                    /@@@@@@@@@@@@@@@.         ')
		print('    .%%%%%%%%%%%%%%%%%#############,                 %@@@@@@@@@@@@@@@@@@@,       ')
		print('   .%%%%%%%%%%%%%%%%%#############.              .@@@@@@@@@@@@@@@@@@@@@@@@*      ')
		print('    ,%%%%%%%%%%%%%%%%############*              %@@@@@@@@@@@@@@@@@@@@@@@@@@@.    ')
		print('      %%%%%%%%%%%%%%%###########.              #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.   ')
		print('        #%%%%%%%%%%%%#########.                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(   ')
		print('          /%%%%%%%%%%######(                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,   ')
		print('            ,%%%%%%%%####*                     .@@@@@@@@@@@@@@@@@@@@@@@@@@@@#    ')
		print('              .#%%%%%#%.                         /@@@@@@@@@@@@@@@@@@@@@@@@@.     ')
		print('                 /%%(                                 ..  &@@@@@@@, ..           ')
		print('                 ....                                   @@@@@@@@@@@@*            ')
		print('                                                                                 ')
		print('                             Another Round of BlackJack?                         ')
		print('               			   ~ Round ', self.roundNumber,' ~                                ')
		print('              ./@@@@&,            			                              		')
		print('           .@@@@@@@@@@@@&                                    ##,                 ')
		print('          %@@@@@@@@@@@@@@@*                                #%%%#%,               ')
		print('         .@@@@@@@@@@@@@@@@@                              (%%%%%%###.             ')
		print('         .@@@@@@@@@@@@@@@@%                            *%%%%%%%%#####.           ')
		print('       ./%&@@@@@@@@@@@@@@@@@&*                       ,%%%%%%%%%%######(          ')
		print('    *@@@@@@@@@@@@@@@@@@@@@@@@@@@/                  ,%%%%%%%%%%%%########/        ')
		print('   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               .%%%%%%%%%%%%%%##########*      ')
		print('  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,               %%%%%%%%%%%%%%##########,      ')
		print('  (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                .%%%%%%%%%%%%########*        ')
		print('   (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                   .%%%%%%%%%%######/          ')
		print('     /@@@@@@@@@@&@@@%@@@@@@@@@(                        ,%%%%%%%%####(            ')
		print('               /@@@@@.                                   *%%%%%%###              ')
		print('            ,%@@@@@@@@@(.                                  /%%%#%.               ')
		print('           .////////////*                                    (%,                 ')
		print('               ......                                                            ')








