"""Defines the Creature class, the base class of all living things in our game."""

class Creature:

	# this is where you declare constant variables in a class
	# Write constant variable in all caps to signify it is a constant
	# Constants for the state of creatures
	NORMAL = "normal"
	ASLEEP = "asleep"
	UNCONS = "unconscious"
	POISONED = "poisoned"
	WEAKENED = "weakened"

	# Creature() signifies new object from that class
	# to access constants: name_of_class.variable_you_want because the constants are just defined
	# with the class template, not the objects themselves that the class will create

	def __init__(self):
		self.name = ""
		self.state = Creature.NORMAL # constant variable, signifies that it should never change
		self.health = 20
		self.max_health = 20 # group things together in logical order, e.g. health and max_health are by each other
		self.attack_points = 2
		self.weapon = None #Class
		self.special_abilities = {} # dictionary of classes?
		self.stats = {}
		

	def attack(self):

		pass

	def heal(self, amount):

		pass

	def defend(self, amount):

		pass

	def take_damage(self, damage):

		pass

	def change_weapon(self, new_weapon):

		pass

	def change_stage(self, new_state):
		pass
