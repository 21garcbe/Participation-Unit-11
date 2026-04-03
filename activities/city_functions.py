""" 
city_functions.py 
A module containing a function that formats two inputs, a city name (string), country name (string)
and population (integer) into a single string in the format "City, Country".

"""

def format_city_country(city, country, population):
    """Takes a city name, country name and optional population formats it as 'City, Country'."""
    if population is not None:
        formatted_location = f"{city}, {country} - Population: {population}"
    else:
        formatted_location = f"{city}, {country}"
    return formatted_location

def main():
    city = input("Enter the name of a city: ")
    country = input("Enter the name of a country: ")
    population = input("Enter the population (optional): ")

    

    print(format_city_country(city, country, population))

if __name__ == "__main__":
    main()