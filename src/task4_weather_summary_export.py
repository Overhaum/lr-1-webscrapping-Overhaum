import json
import csv


def load_json(filename):

    with open(filename, 'r') as file:
        return json.load(file)


def summarize_weather_data(data):

    total_max_temp = 0
    total_min_temp = 0
    total_precipitation = 0
    total_wind_speed = 0
    total_humidity = 0
    hot_days = 0
    windy_days = 0
    rainy_days = 0
    days_count = len(data)

    for day in data:
        total_max_temp += day['max_temperature']
        total_min_temp += day['min_temperature']
        total_precipitation += day['precipitation']
        total_wind_speed += day['wind_speed']
        total_humidity += day['humidity']

        if day['max_temperature'] > 30:
            hot_days += 1
        if day['wind_speed'] > 15:
            windy_days += 1
        if day['precipitation'] > 0:
            rainy_days += 1

    # Підсумкові метрики
    summary = {
        'average_max_temp': total_max_temp / days_count,
        'average_min_temp': total_min_temp / days_count,
        'total_precipitation': total_precipitation,
        'average_wind_speed': total_wind_speed / days_count,
        'average_humidity': total_humidity / days_count,
        'hot_days_count': hot_days,
        'windy_days_count': windy_days,
        'rainy_days_count': rainy_days
    }

    return summary


def export_to_csv(data, file):

    headers = [
        'Date', 'Max Temperature', 'Min Temperature', 'Precipitation',
        'Wind Speed', 'Humidity', 'Weather Description', 'Is Hot Day',
        'Is Windy Day', 'Is Rainy Day'
    ]

    with open(file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for day in data:
            writer.writerow({
                'Date': day['date'],
                'Max Temperature': day['max_temperature'],
                'Min Temperature': day['min_temperature'],
                'Precipitation': day['precipitation'],
                'Wind Speed': day['wind_speed'],
                'Humidity': day['humidity'],
                'Weather Description': day['weather_description'],
                'Is Hot Day': day['max_temperature'] > 30,
                'Is Windy Day': day['wind_speed'] > 15,
                'Is Rainy Day': day['precipitation'] > 0
            })


data = load_json(
    'C:/Users/Overhaum/Documents/GitHub/lr-1-webscrapping-Overhaum/src/tokyo_weather_complex.json')

summary = summarize_weather_data(data['daily'])

print("Weather Summary:")
for key, value in summary.items():
    print(f"{key}: {value}")

export_to_csv(data['daily'], 'tokyo_weather_summary.csv')
print("Weather data has been exported to 'tokyo_weather_summary.csv'.")
