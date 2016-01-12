my_string = "Portland" # make a string

#print(my_string) # = print string

#print(my_string[1]) # = print out string's 2nd character

#print(my_string[-3]) # = print out string's 3rd to last character

#print(my_string[2:5]) # = print out string's middle 3 characters as a substring

MyStringLength = len(my_string) # to determine length of string


def middle_characters(my_string):
	# determine the middle 3 characters of the string and print them
	# round up or down for even number of characters
	print(my_string)

	string_length = len(my_string) # establish length of the string as a variable

	move_number = ((string_length - 3) // 2) # number of spaces to move over becomes the first variable for slicing since
	# it's a number

	move_number2 = move_number + 3 # the second part of the slice comes from the original move number plus 3 rather
	# than 2 since the last character won't appear in a slice

	middle = my_string[move_number:move_number2] #slice the string

	 
	print(middle)




# write a function that:
	# - expects an input of a sequence
	# - prints the sequence
	# - loops through the sequence, and prints each element


new_string = "serpentine"
def sequence_loop(new_string):

	print(new_string) #prints the string

	for x in new_string: #prints the string out, letter by letter on individual lines via for loop
		print(x)



def main(): # the main function to be called, uses the other functions inside of itself
	#user_input = input("Please enter a word: ") # = new variable created through prompting user to type 
	# in a word and then using whatever the user types as the variable
	my_list = ["happy", "gorilla", "orange", "essential", "window", "munchkin"]
	#middle_characters(user_input) # = calls middle_characters function with whatever the user types in
	#sequence_loop(user_input) # = calls the sequence_loop function with whatever the user types in

	sequence_loop(my_list)

main()

# Make a list of random words and print it using your looping print function


