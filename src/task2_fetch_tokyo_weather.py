import requests
import json
from datetime import datetime


def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&daily=temperature_2m_max&timezone=Asia/Tokyo"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_date = data['daily']['time'][0]
        max_temperature = data['daily']['temperature_2m_max'][0]
        return {
            "date": forecast_date,
            "max_temperature": max_temperature
        }
    else:
        print("Помилка при отриманні даних з Open-Meteo API.")
        return None


def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


weather_data = fetch_weather_data()

if weather_data:
    save_to_json(weather_data, 'tokyo_weather.json')
    print("Дані погоди збережено в 'tokyo_weather.json'")
else:
    print("Не вдалося отримати дані погоди.")
