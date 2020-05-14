filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.")
	file_object.write("\nAnd this is how you write on a new line. (with \n)")
	
with open(filename, 'a') as file_object:
	file_object.write("\nI also love finding meaning in large datasets.")
	file_object.wirte("\nI love creating apps that can run in a browser.")
	#Using 'a' will append everything at the end of the file, or create a new file if it doesn't exist
	
