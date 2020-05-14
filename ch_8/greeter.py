prompt = "Please enter your username: "
username = input(prompt)

def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")
	
greet_user(username)

def get_formatted_name2(first_name2, last_name2):
	"""Return a full name, neatly formatted"""
	full_name2 = first_name2 + " " + last_name2
	return full_name2.title()
	
while True:
	print("\nPlease tell me your name:")
	print(" (enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	
	formatted_name2 = get_formatted_name2(f_name, l_name)
	print("\nHello, " + formatted_name2 + "!")
