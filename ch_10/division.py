try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero.")
	
print("\n\n\n")

print("Give me 2 numbers and I'll divide them ('q' to quit): ")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)
