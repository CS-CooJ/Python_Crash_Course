"""Produce random rolls based upon # of sides on dice"""
from random import randint

class Die():
	"""Define types of dice."""	
	def __init__(self, sides=6):
		"""Initialize the die."""
		self.sides = sides
		self.rolls = 1
		
	def roll(self):
		"""Return a random number for a dice roll"""
		return randint(1, self.sides)
		
d6 = Die()
d8 = Die(sides=8)
d10 = Die(sides=10)
d12 = Die(sides=12)
d20 = Die(sides=20)
d100 = Die(sides=100)

dice_type = input("How many sides to your die? ('q' to quit) ")
num_rolls = input("How many times will you roll the dice? ('q' to quit) ")
	
results = []
