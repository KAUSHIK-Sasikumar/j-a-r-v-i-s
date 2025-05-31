import requests
from config import WEATHER_API_KEY

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        data = requests.get(url).json()
        if data["cod"] != 200:
            return "City not found."
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city} is {desc} with {temp}°C."
    except:
        return "Unable to retrieve weather."
