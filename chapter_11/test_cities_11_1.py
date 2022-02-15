#### TRY IT YOURSELF - City, Country - Chapter 11 - Page 215
import unittest
from city_country_functions_11_1 import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_country_functtions"""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        formatted_location = city_country('london', 'united kingdom')
        self.assertEqual(formatted_location, 'London, United Kingdom')

if __name__ == '__main__':
    unittest.main()