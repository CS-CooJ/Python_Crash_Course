def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

def describe_pet2(pet_name2, animal_type2 = 'dog'):
	"""Display information about a pet."""
	print("\nI have a " + animal_type2 + ".")
	print("My " + animal_type2 + "'s name is " + pet_name2.title() + ".")

describe_pet2('willie')

#A dog named Willie (both below work)
describe_pet2('willie')
describe_pet2(pet_name2='willie')

#A hamster named Harry
describe_pet2('harry', 'hamster')
describe_pet2(pet_name2='harry', animal_type2='hamster')
describe_pet2(animal_type2='hamster', pet_name2='harry')
