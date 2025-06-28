# Daniel Graham
# Date: 6/28/25
# Module 7.2 Assignment: Test Cases

# test_cities.py
import unittest
from city_functions import format_city_country

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_name = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()