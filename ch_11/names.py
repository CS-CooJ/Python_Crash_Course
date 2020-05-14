from name_function import get_formatted_name

print(f"Enter 'q' at any time to quit.")
while True:
	first = input(f"\nPlease give me a first name: ")
	if first.lower() == 'q':
		break
	last = input(f"\nPlease give me a last name: ")
	if last.lower() == 'q':
		break
		
	formatted_name = get_formatted_name(first, last)
	print(f"\tNeatly formatted name: {formatted_name}.")
