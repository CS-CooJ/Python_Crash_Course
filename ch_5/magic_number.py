answer = 17

if answer != 42:
	print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) #false
age_1 = 22
print(age_0 >= 21 and age_1 >= 21) #true
#can also be written as (cleaner):
(age_0 >= 21) and (age_1 >= 21)

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21 #True
age_0 = 18
age_0 >= 21 or age_1 >= 21 #False

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings #True
'pepperoni' in requested_toppings #False
