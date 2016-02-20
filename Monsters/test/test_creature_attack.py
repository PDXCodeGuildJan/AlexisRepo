__author__ = "Aexis Bird"

import unittest # built in Python function for testing purposes
from creature import Creature, Weapon # importing Creature Class 
#(where the function is we're testing) from creature.py file


# Make a new TestCase, CreatureAttackTest that inherits from unittest.TestCase
class CreatureAttackTest(unittest.TestCase):

	def setUp(self):
		# built in Python setUp function 
		"""Create an instance of the Creature class so that we can leverage its functions in our tests.
		"""
		self.creature = Creature()

	def tearDown(self):
		# undoes everything that your setUp function did
		# built in Python tearDown function
		"""Delete the Creature instance we made in the setUp.
		"""
		del self.creature

	def test_attack_return_int(self):
		# begin every test function name with test_
		"""Ensure that when attack is called, an int is returned.
		"""
		# Call the attack  function of our creature and return an integer
		value = self.creature.attack()

		self.assertIsInstance(value, int, "Returned Attack value is not an int") #wrote comment here to personalize error message

	def test_no_weapon_return_base_damage(self):
		"""Ensure that with no weapon equipped, the creature does its base damage.
		"""
		# Manually set the base damage to something we know (in this case: 3)
		self.creature.attack_points = 2

		# Get the creature's attack value
		value = self.creature.attack()

		self.assertEqual(value, 2, "Expected base attack value not given.")

	def test_with_weapon_return_damage(self):
		"""Ensure that with a weapon, the creature does base damage + Weapon damage.
		"""
		# Make a weapon to give creature
		weapon = Weapon(3)

		# Give the weapon to the creature
		self.creature.weapon = weapon

		# Set creature's base attack value
		self.creature.attack_points = 2

		# Get the creature's total attack value
		value = self.creature.attack()

		# Assert the attack value is the base + weapon damage
		self.assertEqual(value, 5, "Computed attack value is not correct.")
