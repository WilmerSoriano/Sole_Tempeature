import os
import requests
from dotenv import load_dotenv

def fetch_data():
    # Load variables from .env into environment
    load_dotenv()

    # Location: Dallas, Texas, US
    CityName = "Dallas"

    # Keeping API Key a Secret
    API_KEY = os.getenv("OPEN_API_KEY")

    URL = "https://api.openweathermap.org/data/2.5/weather"

    CALL = f"{URL}?q={CityName}&appid={API_KEY}&units=imperial"

    response = requests.get(CALL)

    if response.status_code == 200:
        data = response.json()

        temp = float(data["main"]["temp"])
        h_temp = int(data["main"]["temp_max"]) 
        l_temp =  int(data["main"]["temp_min"])
        
        return temp, h_temp, l_temp
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    temp, h_temp, l_temp = fetch_data()
    print(temp, h_temp, l_temp)