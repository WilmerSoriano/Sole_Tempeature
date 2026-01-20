import requests

API_KEY = ""

URL = "http://api.openweathermap.org/data/2.5/forecast?"

CALL = f"{URL}id={ID}&appid{API_KEY}" 

response = requests.get(CALL)

if response.status_code == 200:
    print()
else:
    print(f"Error: {response.status_code}")