"""
    Author: Zachary White
    Instructor: Darrell Payne
    Date: 05/01/2026
    Assignment: Module 7 - City Functions
    Description: Function that accepts city, country, optional population,
                 and optional language and returns a formatted string.
"""

def city_country(city, country, population=None, language=None):
    """Return a formatted string of city, country with optional population and language."""
    result = "{}, {}".format(city.title(), country.title())

    if population:
        result += " - population {}".format(population)

    if language:
        result += ", {}".format(language.title())

    return result


# -- Call the function three times --

# Call 1: City and Country only
print(city_country("santiago", "chile"))

# Call 2: City, Country, and Population
print(city_country("tokyo", "japan", population=13960000))

# Call 3: City, Country, Population, and Language
print(city_country("paris", "france", population=2161000, language="french"))
