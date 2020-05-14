with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents) 
	
with open('find_me/find_me.txt') as file_object:
	contents = file_object.read()
	print (contents.rstrip()) # .rstrip() gets rid of line after .txt file

file_path = r'C:\Users\Cody\Desktop\Python\python_work\Python Crash Course\ch_1\find_me_again.txt'
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents)
	
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.strip())

with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	print(line.strip())
