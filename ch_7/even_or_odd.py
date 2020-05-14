#modulo operator: divides 1 number by another and returns the remainder
print(4 % 3) #will display remainder of 1

number = input("Enter a number, and I'll tell you if its even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + "is even.")
else:
	print("\nThe number " + str(number) + "is odd.") 
