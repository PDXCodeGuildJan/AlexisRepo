from creature import Creature
from monster import Monster

class Hero(Creature): # Creating a new class Hero that is inheriting all the features from Creature class

	def __init__(self):
		super(Hero, self).__init__() # can only use super for single object inheritance, not multiple

		self.level = 1

class MonsterHero(Monster, Hero): # Multiple Object Inheritance - creating class MonsterHero which will
#inherit everything from both Monster class and Hero class

	def __init__(self):
		Monster.__init__(self) # we don't use super here because weird things will happen and overlap with multiple
		#inheritance
		Hero.__init__(self) # instead of super, we must specificy each parent class from which MonsterHero
		#is inheriting

		self.second_weapon = None # staying consistent with weapon variable



