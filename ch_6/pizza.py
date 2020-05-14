# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick', 
	'toppings': ['mushrooms', 'extra cheese'],
	}
#Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza, with the following toppings:")
for items in pizza['toppings']:
	print("\t" + items.title())
