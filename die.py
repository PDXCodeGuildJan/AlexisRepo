# create a die function that returns a random number, as if the user rolled a die.

from random import randint

def die():
	roll = randint(1, 6)
	print(roll)


# Make a function called custom_die that takes a range and prints a random number in that range

def custom_die(low, high): # make function accept two inputs
	roll = randint(low, high) # make sure to have two inputs in the randint() function
	print(roll)

# how big is the die?
# how many dice?

def main():
	# ask user how many dice to roll
	total_rolls = input("How many dice would you like to roll? ")
	total_rolls = int(total_rolls)

	#find out how big the dice are
	max_num = input("How many sides are on the dice? ")
	max_num = int(max_num)
	# you can also "nest": max_num = int(input("How many sides are on the dice?"))


	# roll that many dice

	for number in range(0, total_rolls):
		custom_die(0, max_num)

main()


