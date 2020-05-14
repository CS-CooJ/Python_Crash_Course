pets = ['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
	pets.remove('cat')
	
for pet in pets:
	print(pet.title())
