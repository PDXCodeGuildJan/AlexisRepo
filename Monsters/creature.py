"""Defines the Creature class, the base class of all living things in our game."""

class Weapon:
	"""Weapon objects that equip creatures.
	"""

	def __init__(self, atk_value):
		self.base_damage = atk_value

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
		"""Return the attack value of the creature, given its base attack 
		value, Weapon attack value, and state.
		"""
		# Set the attack value to the base attack amount
		atk_value = self.attack_points
		# if we have a weapon, add the weapon's damage to atk_value
		if self.weapon:
			atk_value += self.weapon.base_damage

		# return the total calculated damage
		return atk_value

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
