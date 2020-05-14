def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print("\n")
	for topping in toppings:
		print(topping.title() + " added to your pizza.")
	
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print('\nMaking a ' + str(size) +
	"-inch pizza with the following toppings:")
	for topping in toppings:
		print("\t- " + topping)
		
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
