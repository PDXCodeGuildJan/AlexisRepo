""" A Phonebook program implemented with classes. """

__author__ = "Alexis Bird"

import re

def main():

	# Test the Contact and Address classes with Jim Everyperson
	jim = Contact("Jim", "Everyperson")
	jim.phone_num = "9873496567"
	jim.email = "jim@jimail.com"
	jim.update_address("Home", city="Portland")
	jim.update_address("Work", "1234 Awesome Lane", "Bldg G", "Vancouver", "BC", "8374", "CANADA")
	print(jim)

class Contact:
	""" Defines the Contact object to store information about people."""

	def __init__(self, f_name, l_name):
		# Assign passed arguments to their corresponding properties
		self.first_name = f_name
		self.last_name = l_name

		self.phone_num = ""
		self.addresses = {}
		self.email = ""

	def update_address(self, addy_key, street=None, 
						unit=None, city=None, state=None, 
						zip_code=None, country=None):
		""" Update the address at addy_key with the info passed. """

		if addy_key in self.addresses:
			temp_address = self.addresses[addy_key]

		else:
			# Make a new Address object
			temp_address = Address()

		# Set the new address' street to whatever was passed
		if street:
			temp_address.street = street
		if unit:    
			temp_address.unit = unit
		if city:
			temp_address.city = city
		if state:
			temp_address.state = state
		if zip_code:
			temp_address.zip_code = zip_code
		if country:
			temp_address.country = country

		self.addresses[addy_key] = temp_address


	def format_phone_num(self, phone_num):
		""" Format the phone nmber of the contact in a pretty way. """

		# Scrub and reformat the phone number to follow (xxx) xxx-xxxx pattern
		# Remove all but the numbers
		regex = "[0-9]+"
		nums = re.findall(regex, phone_num)

		new_num = ""
		for every_num in nums:
			new_num += every_num

		formatted_num = "(" + new_num[0:3] + ") " + new_num[3:6] + "-" + new_num[6:]

		self.phone_num = formatted_num

	def __str__(self):
		""" Print out the contact's info in a pretty way. """

		# Initialize formatted string
		formatted_str = "{0} {1}".format(self.first_name, self.last_name)

		# If there is a phone number
		if self.phone_num:
			# Format the phone number properly
			self.format_phone_num(self.phone_num)
			# Add the pretty phone number to the formatted_str
			formatted_str += "\nPhone: {0}".format(self.phone_num)

		# If there is an email address
		if self.email:
			formatted_str += "\nEmail: {0}".format(self.email)

		if self.addresses:
			formatted_str += "\nAddresses"
			formatted_str += "\n---------------------------"

			# Loop through all the addresses and print them
			for key, address in self.addresses.items():
				formatted_str += "\n{0}:".format(key)
				formatted_str += "\n{0}".format(address)
				formatted_str += "\n------------------------"

		return formatted_str



class Address:
	""" Defines the Address object to be used with Contact. """

	def __init__(self):
		self.street = ""
		self.unit = ""
		self.city = ""
		self.state = ""
		self.zip_code = ""
		self.country = ""

	def __str__(self):
		""" Print out the address in proper format as one string instead of separate print statements. """

		formatted_str = self.street
		if self.unit != "":
			formatted_str += "\n" + self.unit
			
		formatted_str += "\n" + self.city + " " + self.state
		formatted_str += " " + self.zip_code
		formatted_str += "\n" + self.country

		return formatted_str


if __name__ == "__main__":
	main()


