"""
Weather Lookup Tool (Open-Meteo API)
"""

import requests

def get_weather(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&daily=temperature_2m_max&timezone=auto"
    )

    response = requests.get(url)
    data = response.json()

    return data["daily"]["temperature_2m_max"][:3]
