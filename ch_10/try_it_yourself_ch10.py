#10-1
filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
	for line in lines:
		print(line.rstrip())
		
learnt = ''
for line in lines:
	learnt = line.rstrip()
	
search = input("What word do you want to look for? ")
if search in learnt:
	print("That is in there.")
else:
	print("Sorry, no find-o that.")	
	
#10-2
with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	line = line.strip()
	print(line.replace('python', 'JavaScript'))

#10-3
filename = 'guest.txt'

with open(filename, 'w') as file_object:
	name = input("What is your name? ")
	file_object.write(name.title())
	
#10-4
filename = 'guest_book.txt'

while True:
	new_guest = input("Please enter your full name: ")
	if new_guest == 'quit':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write("\n" + new_guest.strip().title())
			print("Hi " + new_guest + ", you have been entered.")
			
#10-5
filename = 'reason.txt'

while True:
	reason = input("Why do you like programming? ('q' to quit) ")
	
	if reason == 'q':
		break
	else:
		with open(filename, 'a') as f:
			f.write(reason.strip() + "\n")
		print("Reason added, thank you.\n")
		
#10-6
print("I will add for you, if you provide the numbers.")

while True:
	num_1 = input("What is the first number you wish to add? ")
	num_2 = input("What is the second number you wish to add? ")

	try:
		sum_1_2 = int(num_1) + int(num_2)
		print(str(sum_1_2))
	
	except ValueError:
		print("Sorry, your input is unable to be added.")

#10-8
filenames = ['cats.txt', 'dogs.txt']

def read_animal():
	for filename in filenames:
		try:
			with open(filename) as file_obj:
				file_obj = file_obj.read()
				
		except FileNotFoundError:
			print("A friendly message to say: File was unable to be found.")
			
		else:
			print(file_obj)
		
read_animal()

#10-9
filenames = ['cats.txt', 'dogs.txt', 'monkeys.txt']

def read_animal():
	for filename in filenames:
		try:
			with open(filename) as file_obj:
				file_obj = file_obj.read()
		except FileNotFoundError:
			pass			
		else:
			print(file_obj)
		
read_animal()

#10-10
filename = ['moby_dick.txt']

def count_occurences(filename, word):
	"""Count the number of times a line occurs in a text"""
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		word_count = contents.lower().count(word)
		
		msg = f"'{word}' appears in {filename} about {word_count} times."
		print(msg)
		
filename = 'alice.txt'
count_occurences(filename, 'the')

filename = 'moby_dick.txt'
count_occurences(filename, 'the')

#10-11, 12
import json

def get_fav_num():
	"""Retrieves a user's favorite number."""
	filename = 'fav_num.py'
	try: 
		with open(filename) as f_obj:
			number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return number
		
def get_new_fav():
	"""Prompt for a new favorite number from user."""
	number = input(f"What is your favorite number? ")
	filename = 'fav_num.py'
	with open(filename, 'w') as f_obj:
		number = json.dump(number, f_obj)
	return number
	
def show_fav_num():
	"""Display the user's favorite number."""
	number = get_fav_num()
	if number:
		print(f"Your favorite number is {number}!")
	else:
		number = get_new_fav()
		print(f"Thank you, we will remember your favorite number.")
		
show_fav_num()

#10-13
import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def get_new_username():
	"""PRompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""Greet a user by name."""
	username = get_stored_username()
	if username:
		correct = input(f"Are you {username}? (Y/N)")
		if correct.lower() == 'y':
			print(f"Welcome back, {username}!")
		else:
			username = get_new_username()
			print(f"We'll remember you when you come back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")

greet_user()
