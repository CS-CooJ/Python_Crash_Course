#5-1
car = 'impala'
van = 'astro'
hatchback = 'crv'
print(car == 'astro')
print("Is car 'impala'? I predict True.")
print(car == 'impala')
print("\nIs van not 'crv'? I predict true.")
print(van != 'crv')
print("\nIs car 'astro'? I predict False.")
print(car == 'astro')

#5-2
sizes = ['xsmall', 'small', 'medium', 'large', 'xlarge']
colors = ['red', 'orange', 'yellow', 'GREEN', 'blue', 'indigo', 'violet']
age_dad = 59
age_mom = 57
if age_mom >= 50 and age_dad <= 65:
	print(True)
if age_mom >=60 or age_dad <= 50:
	print(True)
if age_mom >= 60 and age_dad >= 60:
	print(True)
if 'xsmall' in sizes:
	print('They have xsmall!')
if 'purple' not in colors:
	print("They call it violet.")
for color in colors:
	if color == "GREEN":
		print(color)
	else:
		print(color.upper())
		
#5-3
alien_color = 'green'

if alien_color is 'green':
	coins = 5
if alien_color is 'yellow':
	coins = 0
if alien_color is 'red':
	coins = -5
	
print("You killed a " + alien_color + ".\nYou've earned " + str(coins) + " points.")

#5-4
alien_color = 'red'
if alien_color is 'green':
	points = 5
else:
	points = 10
print("You've killed a " + alien_color + " alien and earned " + str(points) + " points.")

if alien_color is 'green':
	points = 5
if alien_color is 'yellow' or 'red':
	points = 10
print("You've killed a " + alien_color + " alien and earned " + str(points) + " points.")

#5-5
alien_color = 'red'

if alien_color is 'green':
	points = 5
elif alien_color is 'yellow': 
	points = 10
else:
	points = 15
print("You killed a " + alien_color + " alien and earned " + str(points) + " points.\n")

#5-6
age = 29

if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'toddler'
elif age < 13:
	stage = 'kid'
elif age < 20:
	stage = 'teenager'
elif age < 65:
	stage = 'adult'
else:
	stage = 'elder'

if age > 19:
	print("Your age is " + str(age) + ". You are considered an " + stage + ".\n")
else:
	print("Your age is " + str(age) + ". You are considered a " + stage + ".\n")
	
#5-7
fruits = ['apple', 'strawberry', 'grape', 'orange', 'mango', 'banana']
fav_fruits = ['mango', 'apple', 'grape']
fruits.append('avocado')

fruit = 'avocado'
if fruit in fav_fruits:
	print(fruit.title() + " is one of your favorite fruits. Yum!")
elif fruit in fruits:
	print(fruit.title() + " is not one of your favorites, but you still like them.\n")
else:
	print(fruit.title() + " is not one of your favorite fruits. You don't even like " + fruit + ".")

#5-8
approved_users = ['admin', 'john', 'jacob', 'jinglhinerschmidt', 'myname2']

for username in approved_users:
	if username != 'admin' in approved_users:	
		print("Greetings " + username.title() + "!")
	else:
		print("All hail " + username.upper() + "!")

#5-9
approved_users = []

if approved_users:
	for username in approved_users:
		if username != 'admin' in approved_users:	
			print("Greetings " + username.title() + "!")
		else:
			print("All hail " + username.upper() + "!")

else:
	print("\nWe need to find some users!")
	
#5-10
current_users = ['carissa', 'Davin', 'cody', 'mark', 'carol']
new_users = ['ricardo', 'joanna', 'eliana', 'CODY', 'hutch', 'TIqUe', 'davin']

lower_current = str(current_users).lower()

for nuser in new_users:
	if nuser.lower() in lower_current:
		print("Username " + nuser + " unavailable. Please select another username.")
	else:
		print("Username " + nuser + " available. Would you like to use " + nuser + " as your username?")		

#5-11
numbers = range(1,10)

for ordinal in numbers:
	if ordinal == 1:
		print(str(ordinal) + 'st')
	elif ordinal == 2:
		print(str(ordinal) + 'nd')
	elif ordinal == 3:
		print(str(ordinal) + 'rd')
	else:
		print(str(ordinal) + 'th')

numbers = range(1,10)
for ordinal in numbers:
	if ordinal == 1:
		end = 'st'
		print("This is the " + str(ordinal) + end + " number in the list.")
	elif ordinal == 2:
		end = 'nd'
		print("This is the " + str(ordinal) + end + " number in the list.")
	elif ordinal == 3:
		end = 'rd'
		print("This is the " + str(ordinal) + end + " number in the list.")
	else:
		end = 'th'
		print("This is the " + str(ordinal) + end + " number in the list.")

else:
	print("There are no more numbers in this list.")
	
