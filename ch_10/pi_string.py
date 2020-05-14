filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
	
print(pi_string)
print(len(pi_string))


"""if we had 1 million digits of pi and only wanted to print the first 50:"""

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.strip()
	
print(pi_string[:52] + "...")
print (len(pi_string))
