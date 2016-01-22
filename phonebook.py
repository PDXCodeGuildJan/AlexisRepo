"""Implements a very simple Phonebook using a Dictionary."""

__author__ = "Alexis Bird" # hidden variable

import re

# Initialize our dictionary, which will store our phone numbers
phonebook = {}

def main():
	"""The driving force function of our Phonebook, where everything comes together."""

	print("Welcome to the BEST Phonebook ever!")
	option = ""
	

	while option != "E":
		option = input("You can:\n\t(A)dd a contact\n\t(D)elete a contact\n\t(S)earch with Name\n\t(N)umber Search\n\t(P)rint phonebook\n\t(E)xit\nWhich would you like to do? ")

		if option.upper() == "A":
			name = input("What is your new contact's name? ")
			number = input("What is " + name + "'s number? ")
			add_contact(name, number)
		elif option.upper() == "D":
			name = input("Which contact are you removing?")
			delete_contact(name)
		elif option.upper() == "E":
			print("Goodbye!")
			exit()
		elif option.upper() == "P":
			print_phonebook()
		elif option.upper() == "S":
			name = input("Which contact would you like to search? ")
			search(name)
		elif option.upper() == "N":
			number = input("Which number would you like to search? ")
			search_by_number(number)
		else:
			print("I'm sorry, I did not understand that.")
	

def add_contact(name, phonenumber):
	"""Adds to the Phonebook with the given contact info."""

	# Remove any lingering whitespace that might have been added
	regex = "\s+\Z"
	thing_you_replace_with = ""
	scrubbed_name = re.sub(regex, thing_you_replace_with, name)
	print(scrubbed_name)


	# Scrub and reformat the phone number to follow (xxx) xxx-xxxx pattern
	# Remove all but the numbers
	regex = "[0-9]+"
	nums = re.findall(regex, phonenumber)
	new_num = ""
	for every_num in nums:
		new_num += every_num

	# Introdue the correct formatting
	formatted_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]
	


	phonebook[scrubbed_name] = formatted_num
	print("New Contact:", name, " was added with number", formatted_num, "\n")

def delete_contact(name):
	"""Removes the given contact from the Phonebook."""




	if name in phonebook:	
		del phonebook[name]
		print(name, "was removed from the Phonebook.\n")

	else:
		print("That contact already does not exist.\n")

def search(name):
	"""Find a contact's number."""
	if name in phonebook:
		number = phonebook[name]
		print(name, "'s number is", number, "\n")
	else:
		print("Sorry, no contact exists with that name.\n")

def search_by_number(search_number):
	"""Find who a certain number is associated with."""
	result = ""
	for name, number in phonebook.items():
		if search_number == number:
			print(name, "'s number is", number, "\n")
			result = name
		
	if result == "":
		print("Sorry, no contact has that number.")


def print_phonebook():
	"""Prints every contact in the Phonebook in a pretty way"""

	print("Contacts:")
	print("---------------------------")
	for name in phonebook:
		print(name, ":\t", phonebook[name], "\n")

if __name__ == "__main__":
	main()

