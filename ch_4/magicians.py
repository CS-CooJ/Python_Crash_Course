magicians = ['merlin', 'harry potter', 'dumbledore', 'newt scamander']
for magician in magicians: #produces a temporary variable "magician" to used, then will do the process for each variable in the list.
	print(magician + '\n')
	print(magician.title() + ', that was a great trick!\n')
	print("I can't wait for your next trick " + magician.upper() + '.\n')

print('Thank you all, that was a great show!')
print("I can't wait to see your next trick " + magician.title()) #the final value of 'magician' will be the last in the list

languages = ['python', 'c', 'java script']
print('The programming languages I know are:\n')
for language in languages:
	print(language.title())

