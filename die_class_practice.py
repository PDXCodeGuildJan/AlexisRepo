
from random import randint

class Die:
	""" A class of Die that allows users to pass a list of values that serve as the Die's sides """

	def __init__(self, possible_values):

		self.current_index = 0
		self.possible_values = possible_values

	def roll(self):

		self.current_index = randint(0, len(self.possible_values)-1)


		


	def __str__(self):

		return str(self.possible_values[self.current_index])

