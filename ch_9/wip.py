from random import randint

while True:
	message = input("Do you want to roll? (Y/N) ")
	if message.upper() != 'Y':
		break
	
	else:
		dice_type = input("How many sides to your die? ('q' to quit) ")
		num_rolls = input("How many times will you roll the dice? ('q' to quit) ")
		for num_rolls in range(int(num_rolls)):
			results = []
			result = randint(1, int(dice_type))
			results.append(result)
			print(results)
