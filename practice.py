my_string = "Portland" # make a string

print(my_string) # print string

print(my_string[1]) # print out string's 2nd character

print(my_string[-3]) #print out string's 3rd to last character

print(my_string[2:5]) # print out string's middle 3 characters as a substring

MyStringLength = len(my_string) # to determine length of string
print(MyStringLength)

def middle_characters(my_string):
	# determine the middle 3 characters of the string and print them
	# round up or down for even number of characters

	string_length = len(my_string) # establish length of the string as a variable

	move_number = ((string_length - 3) // 2) # number of spaces to move over becomes the first variable for slicing since
	# it's a number

	move_number2 = move_number + 3 # the second part of the slice comes from the original move number plus 3 rather
	# than 2 since the last character won't appear in a slice

	middle = my_string[move_number:move_number2] #slice the string

	 
	print(middle)

middle_characters(my_string)

middle_characters("Chinese")