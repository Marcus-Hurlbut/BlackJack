

class Card:
	def __init__(self, suite, value):
		self.suite = suite
		self.value = value

	def getValue(self):
		return self.value

	def setValue(self, val):
		self.value = val 

	def getSuite(self):
		return self.suite

	def setSuite(self, suite):
		self.suite = suite

	def revertAceValue(self):
		if (self.value == 11):
			self.value = 1
		else:
			print("ERROR IN REVERTING ACE VALUE")


