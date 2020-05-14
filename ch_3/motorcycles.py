motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #switches the first item in list with ducati
print(motorcycles)

motorcycles.append('honda') #append adds an item to the list
print(motorcycles)

motorcycles.insert(0, 'indian') #inserts at identified placing
print(motorcycles)

del motorcycles[-1] #deletes identified item
print(motorcycles)

popped_motorcycle = motorcycles.pop() #gets rid of the [-1] item and redefines new list
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop() #separates last and redefines into new variable
first_owned = motorcycles.pop(0) #separates first and redefines into new variable
print(last_owned)
print(first_owned)

message_first = "The first motorcycle I owned was an " + first_owned + " and I had it for 10 years."
message_last = "The last motorcycle I owned was a " + last_owned + " and I sold it last week."
print(message_first)
print(message_last)
print(motorcycles)

motorcycles = ['honda', 'suzuki', 'yamaha', 'indian', 'harley', 'ducati']
print(motorcycles)
motorcycles.remove('ducati') #to remove item by name
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
