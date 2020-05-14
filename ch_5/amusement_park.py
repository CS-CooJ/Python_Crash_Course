age = 12
print('Your admission cost is:')
if age < 4:
	print('$0')
elif age < 18:
	print('$5')
else:
	print('$10')

age = 12

if age < 4:
	price = 0
elif age < 18:
	price =5
else: 
	price = 10
print('Your admission cost is $' + str(price) + '.')

age = 12

if age < 4:
	price = 0
elif age < 65:
	price =10
elif age >= 65:
	price = 5
print('Your admission cost is $' + str(price) + '.')

age = 66
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age >= 18 and age < 65:
	price = 10
elif age >= 65:
	price = 5
print('Your admission cost is $' +str(price) + '.')
