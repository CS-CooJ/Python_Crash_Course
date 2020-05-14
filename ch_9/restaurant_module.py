class Restaurant():
	"""Model of restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type
	
	def describe_restaurant(self):
		print("The restaurant's name is " + self.name.title() + ".\n")
		print("The restaurant serves " + self.cuisine + " cuisine.")
		
	def open_restaurant(self):
		print(self.name.title() + " is now open.")
