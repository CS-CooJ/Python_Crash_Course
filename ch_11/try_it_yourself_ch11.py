#11-1
#FUNCTION BEING TESTED (IN SEPARATE FILES)
def city_proper(city_name, state_name):
	"""Return proper city/state name structure."""
	return(city_name.title() + ', ' + state_name.title())
#FUNCTION TEST (IN SEPARATE FILES)
import unittest
from city_functions import city_proper

class CityNameTest(unittest.TestCase):
	"""Tests for name of location, like 'Kansas City, Missouri.'"""
	def test_city_state(self):	
		formatted_name = city_proper('topeka', 'kansas')
		self.assertEqual(formatted_name, 'Topeka, Kansas')
	
unittest.main()

#11-2
def city_proper(city_name, state_name, population=''):
	"""Return proper city/state name structure."""
	
	if population:
		return(city_name.title() + ', ' + state_name.title() + ' - population: '
			+ str(population))
	else:
		return(city_name.title() + ', ' + state_name.title())
#CLASS TEST FOR ABOVE FUNCTION
import unittest
from city_functions import city_proper

class CityNameTest(unittest.TestCase):
	
	def test_city_state(self):	
		"""Tests for name of location, like 'Kansas City, Missouri.'"""
		formatted_name = city_proper('topeka', 'kansas')
		self.assertEqual(formatted_name, 'Topeka, Kansas')
		
	def test_with_pop(self):
		"""Tests for name and population formatted correctly."""
		formatted_prop = city_proper('topeka', 'kansas', 125904)
		self.assertEqual(formatted_prop, 'Topeka, Kansas - population: 125904')
	
unittest.main()
