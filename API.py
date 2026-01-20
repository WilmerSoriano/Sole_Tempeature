import os
import requests
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

CityName = "Dallas"

# Keeping API Key a Secret
API_KEY = os.getenv("OPEN_API_KEY")

URL = "https://api.openweathermap.org/data/2.5/weather"

CALL = f"{URL}?q={CityName}&appid={API_KEY}&units=imperial"

response = requests.get(CALL)

if response.status_code == 200:
    data = response.json()
    print(f"Dallas {data["main"]["temp"]}F")
    print("Feels Like:", data["main"]["feels_like"])
    print("H:", data["main"]["temp_max"])
    print("L:", data["main"]["temp_min"])
else:
    print("Error:", response.status_code)