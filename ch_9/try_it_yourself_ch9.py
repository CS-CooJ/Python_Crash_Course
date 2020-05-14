#9-1
class Restaurant():
	"""Model of restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type
	
	def describe_restaurant(self):
		print("The restaurant's name is " + self.name.title() + ".\n")
		print("The restaurant serves " + self.cuisine + " cuisine.")
		
	def open_restaurant(self):
		print(self.name.title() + " is now open.")
		
my_restaurant = Restaurant("fazoli's", "fine italian")
whitecastle = Restaurant('white castle', 'fast food burger')
applebees = Restaurant('Applebees','American')

print("Name: " + my_restaurant.name.title() + "\nCuisine: " + 
	  my_restaurant.cuisine.title() + "\n")

my_restaurant.describe_restaurant()
print('\n')
my_restaurant.open_restaurant()
whitecastle.describe_restaurant()
applebees.describe_restaurant()

#9-3
class User():
	
	def __init__(self, first_name, last_name, email, location, username):
		self.fname = first_name
		self.lname = last_name
		self.email = email
		self.location = location
		self.username = username
	
	def describe_user(self):
		print("Username: " + self.username + "\nFirst Name: " + 
		self.fname.title() + "\nLast Name: " + self.lname.title() + 
		"\nEmail: " + self.email + "\nLocation: " + 
		self.location.title())
		
	def greet_user(self):
		print("Hello, " + self.fname.title() + "! Coming at us from " +
		self.location.title() + "!")
		
user_1 = User('albert', 'camus', 'a_camel@aol.com', 'potato, idaho', 
			  'a_camel')
user_2 = User('walter', 'disney', 'mickey@disney.com',
			  'little rock, arkansas', 'mickey_dad')
user_3 = User('bill', 'gates', 'microsoft@microsoft.com',
			  'austin, texas', 'richest_guy')
			  
user_1.describe_user()
user_1.greet_user()
user_2.greet_user()
user_3.greet_user()

#9-4
class Restaurant():
	"""Model of restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print("The restaurant's name is " + self.name.title() + ".\n")
		print("The restaurant serves " + self.cuisine + " cuisine.")
		
	def open_restaurant(self):
		print(self.name.title() + " is now open.")
	
	def display_number_served(self):
		print("Total customers served: " + str(self.number_served))
		
	def set_number_served(self, total):
		if total >= self.number_served:
			self.number_served = total
		else:
			print("Total served cannot be reduced, sorry.")
			
	def increment_number_served(self, served):
		self.number_served += served
		
my_restaurant = Restaurant("fazoli's", "fine italian")

print("Name: " + my_restaurant.name.title() + "\nCuisine: " + 
	  my_restaurant.cuisine.title() + "\n")

my_restaurant.describe_restaurant()
my_restaurant.display_number_served()

print('\n')
my_restaurant.set_number_served(100)
my_restaurant.display_number_served()

print("\n")
my_restaurant.increment_number_served(10)
my_restaurant.display_number_served()

#9-5
class User():
	
	def __init__(self, first_name, last_name, email, location, username):
		self.fname = first_name
		self.lname = last_name
		self.email = email
		self.location = location
		self.username = username
		self.login_attempts = 0
	
	def describe_user(self):
		print("Username: " + self.username + "\nFirst Name: " + 
		self.fname.title() + "\nLast Name: " + self.lname.title() + 
		"\nEmail: " + self.email + "\nLocation: " + 
		self.location.title())
		
	def greet_user(self):
		print("Hello, " + self.fname.title() + "! Coming at us from " +
		self.location.title() + "!")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
user_1 = User('albert', 'camus', 'a_camel@aol.com', 'potato, idaho', 
			  'a_camel')
user_2 = User('walter', 'disney', 'mickey@disney.com',
			  'little rock, arkansas', 'mickey_dad')
user_3 = User('bill', 'gates', 'microsoft@microsoft.com',
			  'austin, texas', 'richest_guy')
			  
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("Login attempts: " + str(user_1.login_attempts) + "\n")

user_1.reset_login_attempts()
print("Login attempts: " + str(user_1.login_attempts) + "\n")

#9-6
class Restaurant():
	"""Model of restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine = cuisine_type
	
	def describe_restaurant(self):
		print("The restaurant's name is " + self.name.title() + ".\n")
		print("The restaurant serves " + self.cuisine + " cuisine.")
		
	def open_restaurant(self):
		print(self.name.title() + " is now open.")
		
class IceCreamStand(Restaurant):
	"""Model of an Ice Cream Stand"""
	def __init__(self, restaurant_name, cuisine_type="ice cream"):
		"""Initialize parent class, then initialize subclass"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []
		
	def display_flavors(self):
		"""Display flavors available."""
		print("The flavors available include: ")
		for flavor in self.flavors:
			print("\t- " + flavor.title())

icream = IceCreamStand("Sheridan's")
icream.flavors = ['vanilla', 'chocolate', 'strawberry', 'neopolitan']

icream.describe_restaurant()
icream.display_flavors()

#9-7
class User():
	
	def __init__(self, first_name, last_name, email, location, username):
		self.fname = first_name
		self.lname = last_name
		self.email = email
		self.location = location
		self.username = username
		self.login_attempts = 0
	
	def describe_user(self):
		print("Username: " + self.username + "\nFirst Name: " + 
		self.fname.title() + "\nLast Name: " + self.lname.title() + 
		"\nEmail: " + self.email + "\nLocation: " + 
		self.location.title())
		
	def greet_user(self):
		print("Hello, " + self.fname.title() + "! Coming at us from " +
		self.location.title() + "!")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
user_1 = User('albert', 'camus', 'a_camel@aol.com', 'potato, idaho', 
			  'a_camel')

class Admin(User):
	"""Define an administrator user."""
	def __init__(self, first_name, last_name, email, location, username):
		"""Initialize and add attributes"""
		super().__init__(first_name, last_name, email, location, username)
		self.privileges = []

	def show_privileges(self):
		"""Show privileges of a user."""
		print("Your admin privileges include: ")
		for privilege in self.privileges:
			print("\t- " + privilege)

cody = Admin('cody', 'jinlin', 'del@gmail.com', 'kansas city, ks', 'jinl')
cody.privileges = ['can add post', 'can delete post', 'can ban users']

cody.describe_user()
cody.show_privileges()

#9-8
class User():
	
	def __init__(self, first_name, last_name, email, location, username):
		self.fname = first_name
		self.lname = last_name
		self.email = email
		self.location = location
		self.username = username
		self.login_attempts = 0
	
	def describe_user(self):
		print("Username: " + self.username + "\nFirst Name: " + 
		self.fname.title() + "\nLast Name: " + self.lname.title() + 
		"\nEmail: " + self.email + "\nLocation: " + 
		self.location.title())
		
	def greet_user(self):
		print("Hello, " + self.fname.title() + "! Coming at us from " +
		self.location.title() + "!")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
user_1 = User('albert', 'camus', 'a_camel@aol.com', 'potato, idaho', 
			  'a_camel')

class Admin(User):
	"""Define an administrator user."""
	def __init__(self, first_name, last_name, email, location, username):
		"""Initialize and add attributes"""
		super().__init__(first_name, last_name, email, location, username)
		self.privileges = Privileges()

class Privileges():
	"""Define different privileges to give accounts"""
	def __init__(self, privileges=[]):
		self.privileges = privileges
		
	def show_privileges(self):
		"""Show privileges of a user."""
		print("Your admin privileges include: ")
		if self.privileges:
			for privilege in self.privileges:
				print("\t- " + privilege)
		else:
			print("\t- NONE")
			
joanna = Admin('joanna', 'schindel', 'jgschindel@gmail.com', 'kansas city', 'numka')
joanna.privileges.privileges = ['can ban users', 'can edit posts']

joanna.privileges.show_privileges()

cody = Admin('cody', 'schindel', 'cjschindel@gmail.com', 'kansas city, ks', 'cjschindel')
cody.privileges.privileges = []

cody.privileges.show_privileges()

#9-9
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles
		
	def fill_gas_tank(): #Just here to be overwritten by ElectricCar
		print("Your gas tank is filled.") 

class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles"""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class (@ super).
		Then initialize attributes specific to an electric car."""
		super().__init__(make, model, year)
		self.battery = Battery()
		
	#def describe_battery(self):
		#"""Print a statement describing the battery size."""
		#print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")
		
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	
	def __init__(self, battery_size=60):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 60:
			range = 140
		elif self.battery_size == 85:
			range = 185
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
		
	def upgrade_battery(self):
		if self.battery_size == 60:
			self.battery_size == 85
			print("Your battery has been upgraded!")
		else:
			print("Unable to upgrade battery at this time.")
		
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#9-10
from restaurant_module import Restaurant

ihop = Restaurant('IHOP', 'breakfast')

ihop.describe_restaurant()

#9-11
from users_module import Admin

uberhaxor = Admin('gerald', 'fjorgendontenson', 'uberhaxor@yahoo.com', 
				  'chillicothe, mo', 'uberhaxor')
uberhaxor.privileges.privileges = ['total control']
uberhaxor.privileges.show_privileges()
