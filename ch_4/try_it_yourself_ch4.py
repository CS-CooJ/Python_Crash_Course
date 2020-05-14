#4-1
pizza = ['pepperoni', 'sausage', 'meat lovers']
for type in pizza:
	print(type)
	print("\nI really like pizza, one topping I like on my pizza is " + 
	type + '.\n')
print('I could eat pizza everyday!\n')

#4-2
animals = ['cheetah', 'elephant', 'dolphin']
for animal in animals:
	print(animal.upper())
	print('\nA ' + animal + ' would not make a good pet\n')
pop_animal = animals.pop(1)
print(pop_animal + '\n')
animals.append('giraffe')
print(animals)
animals.insert(0, 'antelope')
print(animals)
animals.sort(reverse=True)
print(animals)

#4-3
digit = range(1,21)
for sequence in digit:
	print(sequence)

#4-4
tenoooo = range(1,10)#took away zeroes because.... yea...
for rundown in tenoooo:
	print(rundown)

#4-5
million = range(1,1000001)
print(min(million))
print(max(million))
print(sum(million))

#4-6
odds = range(1,21,2)
for digits in odds:
	print(digits)
	
#4-7
odds = []
for digits in range(3,28):
	mult = digits+3
	odds.append(mult)
print(odds)
#or
odds = range(3,31,3)
for digits in odds:
	print(digits)
#or
odds = [value+3 for value in range(0,28)]
print(odds)

#4-8
cubes = range(1,11)
for digits in cubes:
	end = digits**3
	print(end)

#4-9
cubes = [value**3 for value in range(1,11)]
print(cubes)

#4-10
balls = ['baseball', 'football', 'futbol', 'hockey ball', 'golf ball']
print("The first three items in the list are:")
for f3 in balls[:3]:
	print(f3)
print("The middle three items in the list are:")
for m3 in balls[1:4]:
	print(m3)
print("The last three items in the list are:")
for l3 in balls[2:]:
	print(l3)

#4-11
pizza = ['pepperoni', 'meat lovers', 'sausage', 'chicken alfredo']
friend_pizzas = pizza[:]
pizza.append('three cheese')
friend_pizzas.append('hawaiin')
print("My favorite pizzas are:")
for mine in pizza[:]:
	print(mine)
	
print("My friend's favorite pizzas are:")
for theirs in friend_pizzas:
	print(theirs)

print(pizza)
print(friend_pizzas)

#4-13
food = ('burgers', 'hotdogs', 'fries', 'mac and cheese', 'coca cola')
for item in food:
	print(item)

food = ('burgers', 'hotdogs', 'fries', 'mac and cheese', 'coca cola', 
'mt dew')
for item in food:
	print(item)


