def count_words(filename):
	"""Count the approximate number of words in a file"""
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError as e:
		pass #tells the program to fail silently
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'moby_dick.txt', 'siddhartha.txt']
for obj_file in filenames:
	count_words(obj_file)
