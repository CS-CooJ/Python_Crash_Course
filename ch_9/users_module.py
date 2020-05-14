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

cody = Admin('cody', 'schindel', 'cjschindel@gmail.com', 'kansas city, ks', 'cjschindel')
cody.privileges.privileges = []
