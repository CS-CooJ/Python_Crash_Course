#6-1
guy = {'f_name': 'joey', 'l_name': 'tribiani', 'm_name': 'allen',
	'b_month': 'february', 'b_day': 30, 'b_year': 1980, 'age': 40,
	'city': 'kansas city', 'state': 'kansas'}

print(guy['f_name'].title() + ' ' + guy['l_name'].title() + ' lives in ' +
	guy['city'].title() + ', ' + guy['state'].title() + '. ' + 
	'He was born on ' + guy['b_month'].title() + ' ' + str(guy['b_day']) + 
	', ' + str(guy['b_year']) + ' and he is currently ' 
	+ str(guy['age']) + ' years old. His middle name is ' 
	+ guy['m_name'].title() + '.')

#6-2
fav_numbers = {
	'joanna': 16,
	'cody': 24,
	'davin': 23,
	'james': 24,
	'daniel': 1000,
	}
print(fav_numbers)

#6-3
glossary = {
	'title': 'Turns string data to String Data',
	'del': 'Permanently removes and item/key/whatever',
	'pop.': 'Removes the last item in a list',
	'sort': 'Used to sort a list',
	'sorted': 'Like sort, but temporary',
	}
print('del:\t')
print(glossary['del'].title())
print('\ntitle:\t')
print(glossary['title'].title())

#6-4
for term in glossary.items():
	print(term)
glossary['upper'] = 'Makes all letters in value upper case'
glossary['lower'] = 'Makes all letter in value lower case'
glossary['append'] = 'Adds an item to the end of a list'
glossary['print'] = 'Used to print text/integers/lists/tuples'
	
for term2 in sorted(set(glossary.keys())):
	print(term2)

#6-5
rivers = {
	'nile': 'egypt',
	'missouri river': 'missouri',
	'takoma (not an actual river)': 'arizona',
	}
for river, location in rivers.items():
	print(river.title() + " is located in " + location.title() + '.')
for river in rivers.keys():
	print(river.title())
for location in rivers.values():
	print(location.title())

#6-6
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
should_take = ['jeremy', 'jen', 'eddy', 'phil', 'andrew']

for user in should_take:
	if user in favorite_languages.keys():
		print("Thank you " + user.title() + ", you have already completed this poll, move on.")
	else: 
		print(user.title() + " you have not taken this poll, please do so.")

#6-8
pets = []
pet = {
	'name': 'fleetwood',
	'type': 'dog',
	'age': 8,
	'owner': 'mark',
	}
pets.append(pet)
pet = {
	'name': 'baskin',
	'types': 'bird',
	'age': 32,
	'owner': 'carol',
	}
pets.append(pet)
pet = {
	'name': 'danny',
	'types': 'dog',
	'age': 15,
	'owner': 'carissa',
	}
pets.append(pet)
pet = {
	'name': 'magikarp',
	'types': 'fish',
	'age': 1,
	'owner': 'ash',
	}
pets.append(pet)

for info in pets:
	print("Here is what I know about " + info['name'].title() + ':')
	for key, value in pet.items():
		print('\t' + key.title() + ': ' + str(value).title())
		
#6-9
#make a dictionary called favorite_places
#think of 3 names to use as keys in the dictionary and store 1-3 
#favorite places for each person. 
favorite_places = {
	'joanna': ['park', 'store', 'zoo'],
	'cody': ['home', 'park', 'movie theater'],
	'eliana': ['park', 'movie theater', 'zoo'],
	}
#loop through the dictionary and print everyone's name and fav places.

for name, places in favorite_places.items():
	print('\n' + name.title() + "'s favorite places to visit are:")
	for place in places:
		print("\t -" + place)
		
#6-10
# Modify #6-2 so they have multiple fav numbers.
fav_numbers = {
	'joanna': [5, 16,],
	'cody': [2, 4, 24,],
	'davin': [23, 13, 97],
	'james': [69, 420, 1337],
	'daniel': [1000, 1],
	}
for name, numbers in fav_numbers.items():
	print('\n' + name.title() + " has " + str(len(numbers)) + 
	" favorite numbers, including:")
	for number in numbers:
		print("\t-" + str(number))

#6-11
cities = {
	'kansas city': {
		'country': 'united states',
		'population': 459787,
		'website': 'kcmo.gov',
		},
	'bangkok': {
		'country': 'thailand',
		'population': 8305218,
		'website': 'bangkok.go.th',
		},
	'vienna': {
		'country': 'austria',
		'population': 1888776,
		'website': 'wien.gv.at',
		},
	}
for city, info in cities.items():
	country = info['country'].title()
	population = info['population']
	website = info['website']
	print("\nFor the city of " + city.title() + ", we know the following:")
	print("\n\t- This city is located in " + country + 
	"\n\t- This city has a population of " + str(population) + 
	"\n\t- This city's website is " + website)

#6-12
users = {
	'enfermi': {
		'f_name': 'enrique',
		'l_name': 'fermi',
		'age': 45,
		'location_city': 'sydney',
		'location_country': 'australia',
		'fav_websites': ['gamestop.com', 'facebook.com', 'transformice.com']
		},
	'kodiak': {
		'f_name': 'danny',
		'l_name': 'trego',
		'age': 20,
		'location_city': 'kansas city',
		'location_country': 'kansas',
		'fav_websites': ['reddit.com', 'facebook.com', 'youtube.com']
		},
	'anonymoose': {
		'f_name': 'alex',
		'l_name': 'moose',
		'age': 17,
		'location_city': 'yakutsk',
		'location_country': 'russia',
		'fav_websites': ['haxorz.eu', 'ihacku.com', 'darkweb.com']
		},
	}

for username, info in users.items():
	f_name = info['f_name']
	l_name = info['l_name']
	age = info['age']
	location_city = info['location_city']
	location_country = info['location_country']
	websites = info['fav_websites']
	print("\nHere is the information we have on the user " + username + ':')
	print("Their actual name is " + f_name.title() + ' ' + l_name.title() +
	'. ' + "They are " + str(age) + " years old and live in " + 
	location_city.title() + ", " + location_country.title() + "." + 
	"The 3 websites they visit most are:")
	for site in websites:
		print("\t- " + site)
		
