import xml.etree.ElementTree as ET
import csv

def parse_weather_xml(xml_file):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    weather_data = []

    for day in root.findall('day'):
        date = day.find('date').text
        temperature = day.find('temperature').text
        humidity = day.find('humidity').text
        precipitation = day.find('precipitation').text

        weather_data.append({
            'Date': date,
            'Temperature': temperature,
            'Humidity': humidity,
            'Precipitation': precipitation
        })

    return weather_data

def save_to_csv(data, filename="parsed_weather_data.csv"):

    headers = ['Date', 'Temperature', 'Humidity', 'Precipitation']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

xml_file = 'weather_data.xml'
parsed_data = parse_weather_xml(xml_file)

save_to_csv(parsed_data, 'parsed_weather_data.csv')
print("Weather data has been successfully exported to 'parsed_weather_data.csv'.")
