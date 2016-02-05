from creature import Creature

class Monster(Creature): #Object Inheritance format - creates a class Monster that is inheriting the attributes
# and methods of the class Creature

	AGGRO = "aggressive"
	DEFENSE = "defensive"


	def __init__(self):
		super(Monster, self).__init__() # super is a built in variable in python that represents the class that 
		# it has inherited from the 'Parent', so in this case super represents creature

		self.personality = Monster.AGGRO


