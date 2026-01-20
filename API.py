import os
import requests
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

CityName = 'Dallas'

API_KEY = os.getenv('OPEN_API_KEY') # Keeping API Key a Secret

URL = "https://api.openweathermap.org/data/2.5/weather"

CALL = f"{URL}?q={CityName}&appid={API_KEY}&units=imperial"

response = requests.get(CALL)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")