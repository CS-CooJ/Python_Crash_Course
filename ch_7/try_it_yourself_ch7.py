#7-1
prompt = "Please enter the brand of the rental car you're currently looking for: "
rental = input(prompt)

print("Let me see if I can find you a " + rental.title() + '.')

#7-2
guests = input("Please input total amount of people dining in your group: ")
if int(guests) > 8:
	print("Please take a seat to wait for the next available table.")
else:
	print("A table is ready, please follower the next available server.")
	
#7-3
random = input("Please enter a number for me to determine if it is a multiple of 10: ")

if int(random) % 10 == 0:
	print(random + " is a multiple of 10.")
else:
	print(random + " is not a multiple of 10.")
	
#7-4
prompt = "Please enter what toppings you would like, one at a time."
prompt += "\nWhen you have done so, enter 'quit': "

current_toppings = []

while True:
	message = input(prompt)
	
	if message == 'quit':
		break
		
	else:
		print("Thank you! " + message.title() + " has been added to your pizza.")
		current_toppings.append(message)
		print("\nYour current toppings include " + str(current_toppings) + 
		". Enter 'quit' if you are finished entering toppings.\n")

#7-5
prompt = "Please enter your current age, enter 'quit' when you are done: "

while True:
	age = input(prompt)
	
	if str(age) != 'quit':
		if int(age) < 3:
			price = 'free'
		elif int(age) <= 12:
			price = '$10'
		elif int(age) > 12:
			price = '$15'
		print("\nThe ticket price for this individual is " + price + '.\n')
	else:
		break

#7-6
prompt = "Please enter what toppings you would like, one at a time."
prompt += "\nWhen you have done so, enter 'quit': "

current_toppings = []

while True:
	message = input(prompt)
	
	if len(current_toppings) = 5:
		print("You have reached your max topping amount, your order is being placed")
		break
	
	else:
		print("Thank you! " + message.title() + " has been added to your pizza.")
		current_toppings.append(message)
		print("\nYour current toppings include " + str(current_toppings) + 
		". Enter 'quit' if you are finished entering toppings.\n")

#7-8
sandwich_orders = ['original', 'little peppi', 'meat sausage', 'volcanic']
finished_sandwiches = []

while sandwich_orders:
	sending_order = sandwich_orders.pop()
	
	print("Your " + sending_order + " sandwich has been made, proceed to counter to pickup.")
	finished_sandwiches.append(sending_order)

print('\n')		
for finished in finished_sandwiches:
	print("We made a " + finished + ' sandwich.')

print("\nWe made a total of " + str(len(finished_sandwiches)) + ' sandwiches.')

#7-9
sandwich_orders = ['bologna', 'turkey', 'salami', 'turkey', 'tuna']
sandwich_orders += ['salami', 'veggie', 'bologna', 'salami', 'veggie']

print("We are currently out of salami.")

while 'salami' in sandwich_orders:
	sandwich_orders.remove('salami')
	
print("We can make the following orders: ")	
for item in sandwich_orders:
	print("\t- " + item)
	
#7-10
dream_vacation = []
prompt = "Where is your dream vacation spot?"
prompt += "\nEnter 'quit' when no more repsonses: "

while True:
	location = input(prompt)
	
	if location == 'quit':
		break
		
	else:
		print(location.title() + " has been added to your dream vacations.\n")
		dream_vacation.append(location)
		
print("\nYour dream vacation locations include:")
for location in dream_vacation:
	print("\t- " + location)
	
#7-9 EXTRA CREDIT
sandwich_orders = ['bologna', 'turkey', 'pastrami', 'turkey', 'tuna']
sandwich_orders += ['pastrami', 'veggie', 'bologna', 'pastrami', 'veggie']	

out_of_stock = []

prompt = "\nPlease enter the item which is out of stock (or 'quit' to end): "

while True:
	oos = input(prompt)
	
	if oos == 'quit':
		break
		
	else:
		print(oos.title() + " sandwiches have been removed from the menu and orders.")
		out_of_stock.append(oos)
		while oos in sandwich_orders:
			sandwich_orders.remove(oos)
	
print("\nWe are currently out of the following items: ")
for items1 in out_of_stock:
	print("\t- " + items1)

print("\nHere are the current orders we are processing: ")
for items2 in sandwich_orders:
	print("\t- " + items2)
