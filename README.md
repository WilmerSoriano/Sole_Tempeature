# Sole_Temperature 🌤️

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15-brightgreen)
![API](https://img.shields.io/badge/OpenWeatherMap-API-orange)

A simple **desktop weather application** built using **PyQt** for the GUI and the **OpenWeatherMap API** to fetch live weather data.

![Weather App Screenshot](screenshot.png)  

---

## ✨ Features
- Display current temperature, high and low temperatures for a city.
- Modern GUI with custom background image.
- City name displayed prominently.
- API key is securely hidden in a `.env` file.

---

## 🛠️ Tech Stack
- **Python 3**
- **PyQt5** – GUI design
- **Requests** – HTTP calls to API
- **python-dotenv** – Environment variable handling
- **OpenWeatherMap API** – Weather data

---

## ⚡ Setup Instructions

### 1st. Set up API key
Create a `.env` file:
```text
OPEN_API_KEY=your_open_weather_map_api_key_here
```
---

### 🏗 2nd. Build the image
```text
docker build -t sole_temperature .
```

### ▶ 3rd.Run the app
```
docker-compose up
```

---

## 📌 Notes

- Designed the GUI in **Qt Designer** and loaded `.ui` file with PyQt5.
- API key is hidden using `.env` for security.

---

## 🔗 References

- OpenWeatherMap API: [https://openweathermap.org/api](https://openweathermap.org/api)
- PyQt5 Documentation: [https://www.riverbankcomputing.com/static/Docs/PyQt5/](https://www.riverbankcomputing.com/static/Docs/PyQt5/)

---

## Instructions for use
1. Replace `your_openweathermap_api_key` with your actual API key inside .env file.
2. No other dependencies are required outside of those specified in the Dockerfile.
3. Enjoy checking the weather with Sole_Temperature! 🌤️
