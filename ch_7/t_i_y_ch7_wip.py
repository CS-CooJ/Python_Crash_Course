#to work on the try it yourself in ch 7 so don't have to continue 
#running through other programs with inputs

#7-9 extra credit
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
