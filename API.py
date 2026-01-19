import request

API_KEY = "API key here!"

URL = f"Here"
reponse = request.get(URL)

print(response.status_code)