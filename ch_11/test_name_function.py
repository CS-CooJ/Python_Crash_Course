import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_funciton.py'."""
	
	def test_first_last_name(self):
		"""Do names like 'John Cena' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, "Janis Joplin")
		
	def test_first_last_middle_name(self):
		"""Do names with 3 parts work, like 'Johnathon Taylor Thomas'?"""
		formatted_name = get_formatted_name(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
	
unittest.main()
