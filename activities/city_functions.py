""" 
city_functions.py 
A module containing a function that formats two inputs, a city name (string), country name (string)
and population (integer) into a single string in the format "City, Country".

"""

def format_city_country(city, country):
    """Takes a city name and country name formats it as 'City, Country'."""
    return f"{city}, {country}"


city = input("Enter the name of a city: ")
country = input("Enter the name of a country: ")

print(format_city_country(city, country))
