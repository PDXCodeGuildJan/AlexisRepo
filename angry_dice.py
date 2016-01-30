""" Angry Dice Game - a single player game in which the player rolls two 6-sided dice
	to match the specified criteria through 3 different stages, winning once
	completing the third stage. Stage 1 requires rolling a 1 and 2, Stage 2 rolling 
	an Angry Face (which replaces the 3) and a 4, and Stage 3 rolling a 5 and 6. The
	player has the option of holding a die if the value matches one of the required
	dice values with any value except 6.
	Rolling a pair of Angry Dice at any point will make you start
	over at Stage 1. """ 

__author__ = "Alexis Bird"

from random import randint



def main():
	""" The driving function that utilizes the smaller functions to create the Angry Dice game. """

	pass

def start():
	""" Welcomes the player and explains the rules of the game, as well as a quit option. """
	print("Welcome to ANGRY DICE - the game where your dice get angry!")
	# create an option to print instructions ("I") and a quit option ("Q")
	# or maybe just print instructions automatically with welcome statement?

	pass


def die_hold(valid, invalid):
	""" Asks if player would like to hold a die, then
		determines whether selected die can be held or not and stores die """

	#hold_choice = input("Would you like to hold one of your dice? ")
	#if hold_choice == "y".lower():
		# ask player to enter value of die he/she would like to hold
		# is there a way to do this so that the two current values of the dice would appear for
		# player to choose from?
		# determine whether selected dice can be held or not - must also confirm that one of the player's
		# current dice values matches what they're trying to hold

	pass

def evaluate_roll(angry, full_match, no_match, one_match):
	""" Evaluates the dice roll to determine which option it matches and how to proceed. """
	pass

def winner(winning, rounds):
	""" In the event of a win, determines which round to switch to or if the game is over. """
	pass


class Die:
	""" A class that defines the dice used to play the game. """

	def __init__(self):
		""" Creates/defines the class objects (dice). """
		self.value = 1
		is_locked = False # Does this need a self?
		self.possible_values = {
		1: """
+-------+
|       |
|   o   |
|       |
+-------+""",
2: """
+-------+
|     o |
|       |
| o     |
+-------+""",
3: """
+-------+
| \   / |
| ^   ^ |
| ----- |
+-------+""",
4: """
+-------+
| o   o |
|       |
| o   o |
+-------+""",
5: """
+-------+
| o   o |
|   o   |
| o   o |
+-------+""",
6: """
+-------+
| o   o |
| o   o |
| o   o |
+-------+"""

}


	def roll(self):
		""" Randomly rolls the die/dice. """
		self.value = randint(1,6)


	def __str__(self):
		""" Returns the rolled and held dice in a pretty manner, as a string. """
		return self.possible_values[self.value]

# globals
die_1 = Die()
die_2 = Die()
current_round = 0 # you may have to change this to 1 in the future, but I don't know yet
	

if __name__ == "__main__":
	die_1 = Die()
	print(die_1)
	for x in range(200000):
		die_1.roll()
		print(die_1)





