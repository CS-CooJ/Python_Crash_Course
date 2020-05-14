cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() #sorts alphabetically
print(cars)
cars.sort(reverse=True) #sorts reverse alphabetical
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the list in reverse:")
cars.reverse() #this is permanent
print(cars)
print("\nAnd back to normal:")
cars.reverse()
print(cars)
print("\nThis is the # of cars in the list:")
print(len(cars))

