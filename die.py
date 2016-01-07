# create a die function that returns a rando number, as if the user rolled a die.

from random import randint

def die():
	roll = randint(1, 6)
	print(roll)

die()

# Make a function called custom_die that takes a range and prints a random number in that range

def custom_die(low, high): # make function accept two inputs
	roll = randint(low, high) # make sure to have two inputs in the randint() function
	print(roll)


# define range of numbers
custom_die(4, 10)
custom_die(3, 4398)
