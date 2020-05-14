#8-1
def display_message():
	"""Displays what I'm learning this chapter"""
	print("I am learning about functions, how to define and use them.")
	
display_message()

#8-2
def favorite_book(title):
	"""Display favorite book titles"""
	print("One of my favorite books is " + title.title() + ".")
	
favorite_book('Chronicles of Narnia')

#8-2.2
prompt = "What is your favorite book? "
title = input(prompt)

def favorite_book(title):
	"""Display favorite book titles"""
	print("One of my favorite books is " + title.title() + ".")
	
favorite_book(title)

#8-3
def make_shirt(size, text):
	print("The size of your shirt will be: " + size.title())
	print("\nThe text of your shirt will read: \n" + text)
	
make_shirt(size='small', text='I really like small shirts to show off my muscles!')

#8-4
def make_shirt(text, size='small'):
	print("The size of your shirt will be: " + size.title())
	print("\nThe text of your shirt will read: \n" + text)
	
make_shirt(text='I really like small shirts to show off my muscles!')

#8-5
def describe_city(name, country='austria'):
	print(name.title() + " is in " + country.title() + ".")
	
describe_city('vienna')
describe_city(name='graz')
describe_city('madrid', 'spain')
describe_city(name='frankfurt', country='germany')

#8-6
def city_country(city_name, country_name):
	"""To write the city and country."""
	location = city_name + ', ' + country_name
	return (location.title())

city = city_country('santiago', 'chile')
print(city)

#8-7
def make_album(artist, album, tracks=''):
	"""Return dictionary of album by artist"""
	cd = {'artist': artist.title(), 'album': album.title()}
	if tracks:
		cd ['tracks'] = tracks
	return(cd)
	
dictionary = make_album('red hot chili peppers', 'californication', 12)
print(dictionary)
dictionary = make_album('red hot chili peppers', 'stadium arcadium')
print(dictionary)
dictionary = make_album('red hot chili peppers', "i'm with you", 14)
print(dictionary)

#8-8
def make_album(artist, album, tracks=0):
	"""Return dictionary of album by artist"""
	cd = {'artist': artist.title(), 'album': album.title()}
	if tracks:
		cd ['tracks'] = tracks
	return(cd)
	
while True:
	print("Please give me all the information about the album. (q to quit)")
	singer = input("\nArtist/Band Name: ")
	if singer == 'q':
		break
	album2 = input("Album Name: ")
	if album2 == 'q':
		break
	tracks2 = input("# of tracks: ")
	if tracks2 == 'q':
		break
	make_albums = make_album(singer, album2, tracks2)
	print(make_albums)
	print('\n')

#8-9
magician_names = ['houdini', 'david blane', 'chris angel', 'micky mouse']

def show_magicians(magician_names):
	for magician in magician_names:
		print(magician.title())
		
show_magicians(magician_names)

#8-10
magicians = ['houdini', 'david blane', 'chris angel', 'micky mouse']

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician.title() + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

#8-11
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)
        
    return magicians
    
magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
print('\n')
show_magicians(magicians)

#8-12
def make_sandwich(*items):
	"""Add as many items identified into a sandwich"""
	print("\nYour sandwich will contain:")
	for item in items:
		print("\t- " + item.title())
		
make_sandwich('bologna', 'american cheese', 'mustard', 'lettuce')
make_sandwich('turkey', 'swiss cheese', 'mayonnaise')
make_sandwich('ham', 'cheddar cheese')

#8-13
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know abou ta user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')

user_profile2 = build_profile('cody', 'einstein',
							location='kansas city',
							field='poor social work',
							state='depressed')
print(user_profile)
print(user_profile2)

#8-14
def car_info(manufacturer, model, **other_info):
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model
	for key, value in other_info.items():
		car[key] = value
	return car
	
new_car = car_info('pontiac', 'g5',
			  color='red',
			  style='coupe',
			  shift='automatic')
					
print(new_car)
