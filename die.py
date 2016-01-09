# create a die function that returns a random number, as if the user rolled a die.

from random import randint

def die():
	roll = randint(1, 6)
	print(roll)


# Make a function called custom_die that takes a range and prints a random number in that range

def custom_die(low, high): # make function accept two inputs
	roll = randint(low, high) # make sure to have two inputs in the randint() function
	if roll == low:
		print(roll, "Critical Fail!")
	elif low < roll < high:
		print(roll)
	else:
		print(roll, "Critical Hit!")
	

# how big is the die?
# how many dice?

def main():
	print("Welcome to Die Roller. Enter q to exit.")

	entree = ""

	while entree != "q":
	# ask user how many dice to roll
		entree = input("How many dice would you like to roll? ")
		if entree == "q":
			#Exit the program
			exit()
		total_rolls = int(entree)

	#find out how big the dice are
		entree = input("How many sides are on the dice? ")
		if entree == "q":
			exit()
		max_num = int(entree)
	# you can also "nest": max_num = int(input("How many sides are on the dice?"))


	# roll that many dice

		for number in range(0, total_rolls):
			custom_die(1, max_num)

	

main()

# long game: Let's modify our main so that it continues asking us what dice to roll until we exit the program.
# Wrap the core logic of the function in a while loop so that it keeps asking to roll until we exit.


