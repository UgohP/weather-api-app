import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_data(city_name, api_key=None):
    api_key = api_key or os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        raise ValueError("No OpenWeather API key provided.")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
