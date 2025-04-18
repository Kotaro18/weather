import requests

API_KEY = 'your_api_key_here'  # Replace with your actual API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_by_city(city_name):
    """Fetch weather data for a given city name."""
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def get_weather_by_coordinates(lat, lon):
    """Fetch weather data for given latitude and longitude."""
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()