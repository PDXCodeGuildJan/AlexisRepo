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

	goal = goal_dict[current_stage]

	advance_stage(goal)


def start():
	""" Welcomes the player and explains the rules of the game, as well as a quit option. """
	print("Welcome to ANGRY DICE - the game where your dice get angry!")
	# create an option to print instructions ("I") and a quit option ("Q")
	# or maybe just print instructions automatically with welcome statement?

	pass


def die_hold():
	""" Asks if player would like to hold a die, then
		determines whether selected die can be held or not and stores die """

	hold_choice = input("Would you like to hold one of your dice? Please answer yes or no. ")
	if hold_choice == "yes".lower():
		hold_choice = input("What is the value of the die you would like to hold? ")
		# return evaluate hold function?
		if hold_choice == die_1.value or hold_choice == die_2.value:
			# maintain the die value
			die_1.value = hold_choice
			hold_choice = locked_die
			locked_die = die_1.value
			# make sure only die_2 is now rolled, but keep locked_die for match comparison purposes
			# locked_die must unlock once match has been met and moving onto new stage

	elif hold_choice == "no".lower():
		print("Okay, let's roll the dice again! ")
		# return roll function?
	else:
		input("I'm sorry, I didn't understand that. Yes or no? ")

		# ask player to enter value of die he/she would like to hold
		# is there a way to do this so that the two current values of the dice would appear for
		# player to choose from?
		# determine whether selected dice can be held or not - must also confirm that one of the player's
		# current dice values matches what they're trying to hold




def double_angry(goal):	#value instead of goal?
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
		current_stage = 1
		return True # maybe?? go back to stage 1
	else:
		return False # I don't know what I'm doing here

	# Check stage goals, modify to catch stage 3 (winner) match??

def advance_stage(goal): # value instead of goal?
	
	global current_stage


	if die_1.value in goal and die_2.value in goal and die_1.value != die_2.value:
		current_stage += 1
		print("Congratulations! You've reached Stage ", current_stage, ". ") # problem in that it
		# might print Stage 4 if you win

	elif die_1.value in goal or die_2.value in goal: # may have to change to exclude value 6
		die_hold()

	else:
		print("No goal matches here. Keep rolling!")
		




def winner():
	""" In the event of a win, determines which round to switch to or if the game is over. """
	# is this all super sloppy coding??
	if die_1.value in goal and die_2.value in goal and current_round == 3:
		print("Yay, you win!!! ")
		play_again = input("Would you like to play again? Please answer yes or no. ")
		if play_again == "yes".lower():
			start()
		elif play_again == "no".lower():
			print("Thank you for playing Angry Dice! Goodbye!")
			exit()
		else:
			print("I'm sorry, I didn't understand that. ", play_again)

	else:
		roll()



class Die:
	""" A class that defines the dice used to play the game. """

	def __init__(self): # initializes the object, its properties, self
		""" Creates/defines the class objects (dice). """
		self.value = 1 # self defines object, needs to be mentioned to know object is being modified
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
	# for x in range(200000):
	# 	die_1.roll()
	# 	print(die_1)





