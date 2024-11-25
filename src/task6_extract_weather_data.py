import csv
import re

def clean_text(line):

    return re.sub(r'[^\x00-\x7F]+', '', line)

def extract_weather_data(text_file):

    pattern = r"Date:\s*(\d{4}-\d{2}-\d{2}),\s*Max\s*Temp:\s*([\d\.]+)°C,\s*Min\s*Temp:\s*([\d\.]+)°C,\s*Humidity:\s*(\d+)%,\s*Precipitation:\s*([\d\.]+)mm"

    weather_data = []

    with open(text_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Очищаємо кожен рядок перед обробкою
            line = clean_text(line)

            # Застосовуємо регулярний вираз
            match = re.search(pattern, line)
            if match:
                # Зберігаємо знайдені дані в словнику
                weather_data.append({
                    'Date': match.group(1),
                    'Max Temperature': match.group(2),
                    'Min Temperature': match.group(3),
                    'Humidity': match.group(4),
                    'Precipitation': match.group(5)
                })

    return weather_data

def save_to_csv(data, filename="extracted_weather_data.csv"):

    headers = ['Date', 'Max Temperature', 'Min Temperature', 'Humidity', 'Precipitation']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

text_file = 'weather_report.txt'
extracted_data = extract_weather_data(text_file)

save_to_csv(extracted_data, 'extracted_weather_data.csv')
print("Weather data has been successfully exported to 'extracted_weather_data.csv'.")
