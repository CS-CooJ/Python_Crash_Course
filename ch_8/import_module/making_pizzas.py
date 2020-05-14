#IMPORTING AN ENTIRE MODULE
import pizza #imports all modules to be used

pizza.make_pizza(16, 'pepperoni') 
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#IMPORT SPECIFIC FUNCTIONS
from pizza import make_pizza #imports the module, can import multiple by separation by a comma

make_pizza(16, 'pepperoni') #don't need to add the "pizza.>>>" when the module is imported
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#GIVING A FUNCTION AN ALIAS
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#GIVING A MODULE AN ALIAS
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#IMPORTING ALL FUNCTIONS IN A MODULE
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
