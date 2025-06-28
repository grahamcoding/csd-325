# Daniel Graham
# Date: 6/28/25
# Module 7.2 Assignment: Test Cases

def format_city_country(city, country, population=None, language=None):
    result = f"{city}, {country}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language}"
    return result.title()

# Call the function at least three times
print("Welcome to the Module 7.2 Assignment by Daniel Graham!")
print("Let's Test City and Country Formatting:")

# Only city and country
print("\tNeatly formatted name:", format_city_country("santiago", "chile"))

# City, country, and population
print("\tNeatly formatted name:", format_city_country("tokyo", "japan", 40000000))

# City, country, population, and language
print("\tNeatly formatted name:", format_city_country("minneapolis", "united states", 425115, "english"))
