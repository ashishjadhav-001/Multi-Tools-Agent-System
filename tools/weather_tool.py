import os
import requests
from langchain.tools import tool

@tool
def get_weather(city: str) -> dict:
    """Get current weather information for a given city"""
    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }

    except Exception as e:
        return {"error": str(e)}