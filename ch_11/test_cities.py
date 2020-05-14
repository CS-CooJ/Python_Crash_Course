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
