"""Module with unit tests for city_functions.py"""
from city_functions import format_city_country

def test_format_city_country():
    """Test for the format_city_country function."""
    formatted_location = format_city_country("Santiago", "Chile")
    assert formatted_location == "Santiago, Chile"
    formatted_location = format_city_country("Paris", "France")
    assert formatted_location == "Paris, France"

def test_city_country_population():
    """Test for the format_city_country function with population."""
    formatted_location = format_city_country("santiago", "chile", 5000000)
    assert formatted_location == "santiago, chile - Population: 5000000"