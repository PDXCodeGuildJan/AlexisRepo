""" Angry Dice Game - a single player game in which the player rolls two 6-sided dice
	to match the specified criteria through 3 different stages, winning once
	completing the third stage. Stage 1 requires rolling a 1 and 2, Stage 2 rolling 
	an Angry Face (which replaces the 3) and a 4, and Stage 3 rolling a 5 and 6. The
	player has the option of locking a die if the value matches one of the required
	dice values with any value except 6.
	Rolling a pair of Angry Dice at any point will make you start
	over at Stage 1. """ 

__author__ = "Alexis Bird"

from random import randint



def main():
	""" The driving function that utilizes the smaller functions to create the Angry Dice game. """

	start()

	while True:

		# roll dice
		roll_dice()
		# evaluate dice

		# double angry
		angry = double_angry()

		if not angry:
			# check if advance stage
			new_stage = advance_stage()

			if not new_stage:
				die_lock()
			else:
				input("Hit return to roll again!")


def start():
	""" Welcomes the player and explains the rules of the game, as well as a quit option. """

	print("Welcome to ANGRY DICE - the game where your dice get angry! Enter 'q' to quit. \n")
	instruction_prompt = input("If you're new to the game, enter 'i' to view instructions. Otherwise hit return to start playing. ")

	if instruction_prompt.lower() == "i":
		print("Angry Dice is a single player game in which the player rolls two 6-sided dice to match the specified criteria through 3 different stages, winning once completing the third stage. Stage 1 requires rolling a 1 and 2, Stage 2 rolling an Angry Face (which replaces the 3) and a 4, and Stage 3 rolling a 5 and 6. The player has the option of locking a die if the value matches one of the required dice values with any value except 6. Rolling a pair of Angry Dice at any point will make you start over at Stage 1.")
	elif instruction_prompt.lower() == "q":
		exit()


def roll_dice():
	"""Rolls any die that is not locked."""
	if not die_1.is_locked:
		die_1.roll()
		print("Rolling Die 1...")

	# Print Die 1
	print(die_1)

	if not die_2.is_locked:
		die_2.roll()
		print("Rolling Die 2...")

	# Print Die 2
	print(die_2)


def die_lock():
	""" Asks if player would like to lock a die, then
		determines whether selected die can be held or not and stores die """

	global current_stage
	goal = goal_dict[current_stage]
	

	lock_choice = input("Would you like to lock one of your dice? Please answer yes or no. ")
	if lock_choice.lower() == "yes":
		lock_choice = input("What is the value of the die you would like to lock? ")
		if lock_choice.isdigit():
			lock_choice = int(lock_choice)

			if lock_choice <= 5:

				if lock_choice == die_1.value and lock_choice in goal:
					die_1.is_locked = True

				elif lock_choice == die_2.value and lock_choice in goal:
					die_2.is_locked = True

				else:
					print("Sorry, you can't lock that value!")

		else:
			print("Sorry, you can't lock that value!")
			# make sure only die_2 is now rolled, but keep locked_die for match comparison purposes
			# locked_die must unlock once match has been met and moving onto new stage

	elif lock_choice.lower() == "no":
		print("Okay, let's roll the dice again!")

	elif lock_choice.lower() == "q":
		exit()

	else:
		input("I'm sorry, I didn't understand that. Yes or no? ")

		# ask player to enter value of die he/she would like to hold
		# is there a way to do this so that the two current values of the dice would appear for
		# player to choose from?
		# determine whether selected dice can be held or not - must also confirm that one of the player's
		# current dice values matches what they're trying to hold



def double_angry():
	""" What happens in the event of two angry dice appearing. """

		# stage_1 - let user know they are at Stage 1, establish parameters: if roll is 1 and 2, proceed
	# to Stage 2 (keep in mind to establish that one dice cannot equal the same as the other, if that
		# even remotely makes sense, no loophole), if 
	# stage_2 - print "Stage 2", establish parameters: 
	# stage_3

	# to establish goal value for each individual stage, could I do an initial goal of 1 and 2, then
		# loop through to incrimentally add until reaching 6/winning match?

	# if angry - if both die_1 and die_2 = 3, then go back to stage 1, print statement about going back
	#to stage 1

	global current_stage

	if die_1.value == 3 and die_2.value == 3:
		# return to stage_1
		print("You got ANGRY! Time to calm down and go back to Stage 1. ")
		input("Hit return to roll again!")
		current_stage = 1
		return True
	else:
		return False


def advance_stage():
	
	global current_stage
	goal = goal_dict[current_stage]

	if die_1.value in goal and die_2.value in goal and die_1.value != die_2.value:
		current_stage += 1
		# Unlock Everything
		die_1.is_locked = False
		die_2.is_locked = False
		if current_stage <= 3:
			print("Congratulations! You've reached Stage", current_stage)
			return True 
		else:
			winner()

	return False

def winner():
	""" In the event of a win, determines which round to switch to or if the game is over. """

	print("Yay, you win!!! ")
	play_again = input("Would you like to play again? Please answer yes or no. ")
	if play_again.lower() == "yes":
		main()
	elif play_again.lower() == "no":
		print("Thank you for playing Angry Dice! Goodbye!")
		exit()
	else:
		print("I'm sorry, I didn't understand that. ")

class Die:
	""" A class that defines the dice used to play the game. """

	def __init__(self): # initializes the object, its properties, self
		""" Creates/defines the class objects (dice). """
		self.value = 1 # self defines object, needs to be mentioned to know object is being modified
		self.is_locked = False
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


	def __str__(self): # double underscores indicate built-in python function - says to python "ignore
	# whatever you were going to do for your string function and override it with this" 
	# __str__ good for returning, must be a string
	# don't print inside this function unless it is for debugging purposes
		""" Returns the rolled and held dice in a pretty manner, as a string. """
		return self.possible_values[self.value]

# globals
die_1 = Die()
die_2 = Die()
current_stage = 1
goal_dict = {1: [1, 2], 2: [3, 4], 3: [5, 6]}





if __name__ == "__main__":
	main()



