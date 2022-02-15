#### TRY IT YOURSELF - Population - Chapter 11 - Page 216
import unittest
from _2city_country_functions_11_1 import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_country_functtions."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        formatted_location = city_country('london', 'united kingdom')
        self.assertEqual(formatted_location, 'London, United Kingdom')

    def test_city_country_population(self):
        """Does the function accepts the optional paramater 'population'."""
        formatted_location = city_country('santigo', 'chile', '5000000')
        self.assertEqual(formatted_location, 'Santigo, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()