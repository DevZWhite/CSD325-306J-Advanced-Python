"""
    Author: Zachary White
    Instructor: Darrell Payne
    Date: 05/01/2026
    Assignment: Module 7 - Unit Tests for City Functions
    Description: Unit tests to verify the city_country function
                 works correctly for all parameter combinations.
"""

import unittest
from zwhite_assignment7 import city_country


class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        """Test city and country only."""
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        """Test city, country, and population."""
        result = city_country("tokyo", "japan", population=13960000)
        self.assertEqual(result, "Tokyo, Japan - population 13960000")

    def test_city_country_population_language(self):
        """Test city, country, population, and language."""
        result = city_country("paris", "france", population=2161000, language="french")
        self.assertEqual(result, "Paris, France - population 2161000, French")


if __name__ == "__main__":
    unittest.main()
