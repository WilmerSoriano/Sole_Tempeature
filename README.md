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

### ✅ Requirements
- All OS devices: download Docker Desktop  
- Windows OS: enable WSL2 in settings (for Windows)
- Linux OS: run ```xhost +local:docker``` in terminal to allow GUI apps

### 1st. Set up API key
Create a `.env` file within repo folder and add the following line:
```
OPEN_API_KEY= use the link below to get your free API key.
```

### 2nd. Build the image (Linux user, use Sudo if needed)
```
docker build -t sole_temperature .
```

### 3rd. Run the app
```
docker-compose up
```

### 4th. Close container
```
docker-compose down
```

---

## 📌 Notes

- Designed the GUI in **Qt Designer** and loaded `.ui` file with PyQt5.
- API key is hidden using `.env` for security.

---

## 🔗 References

- OpenWeatherMap API: [https://openweathermap.org/api](https://openweathermap.org/api)
- PyQt5 Documentation: [https://www.riverbankcomputing.com/static/Docs/PyQt5/](https://www.riverbankcomputing.com/static/Docs/PyQt5/)

