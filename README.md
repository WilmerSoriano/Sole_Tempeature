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

### Create & activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Set up API key
Create a `.env` file:
```text
OPEN_API_KEY=your_openweathermap_api_key
```

### Run the app
```bash
python main.py
```

---

## 📌 Notes

- Designed the GUI in **Qt Designer** and loaded `.ui` file with PyQt5.
- Background image (`bg.jpg`) and fonts/colors can be customized.
- API key is hidden using `.env` for security.

---

## 🔗 References

- OpenWeatherMap API: [https://openweathermap.org/api](https://openweathermap.org/api)
- PyQt5 Documentation: [https://www.riverbankcomputing.com/static/Docs/PyQt5/](https://www.riverbankcomputing.com/static/Docs/PyQt5/)

---

## Instructions for use
1. Replace `<your-repo-url>` with your actual repository URL
2. Replace `<your-repo-folder>` with your actual repository folder name
3. Replace `your_openweathermap_api_key` with your actual API key
4. Add your actual screenshot as `screenshot.png` in the root directory
5. Update the Python version in badges if needed (currently shows 3.11)
6. Save this content as `README.md` in your project root
