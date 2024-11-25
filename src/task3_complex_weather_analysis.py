import json

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def analyze_daily_weather(day, temp_threshold=30, wind_threshold=15, humidity_threshold=70):
    date = day['date']
    max_temp = day['max_temperature']
    min_temp = day['min_temperature']
    wind_speed = day['wind_speed']
    humidity = day['humidity']
    precipitation = day['precipitation']
    weather_description = day['weather_description']

    analysis = {
        'date': date,
        'max_temperature': max_temp,
        'min_temperature': min_temp,
        'wind_speed': wind_speed,
        'humidity': humidity,
        'precipitation': precipitation,
        'weather_description': weather_description,
        'hot_day': max_temp > temp_threshold,
        'temp_swing': max_temp - min_temp > 10,
        'windy_day': wind_speed > wind_threshold,
        'uncomfortable_humidity': humidity > humidity_threshold,
        'rainy_day': precipitation > 0,
        'precipitation_level': 'легкий' if 0 < precipitation <= 10 else 'помірний' if 10 < precipitation <= 20 else 'сильний' if precipitation > 20 else 'відсутній'
    }

    return analysis

def generate_daily_report(analysis):
    report = f"Дата: {analysis['date']}\n"
    report += f"Погода: {analysis['weather_description']}\n"
    report += f"Температура: Макс. {analysis['max_temperature']}°C, Мін. {analysis['min_temperature']}°C\n"

    if analysis['hot_day']:
        report += "Це був спекотний день.\n"
    if analysis['temp_swing']:
        report += "Були значні температурні коливання.\n"
    if analysis['windy_day']:
        report += "Це був вітряний день.\n"
    if analysis['uncomfortable_humidity']:
        report += "Вологість зробила цей день некомфортним.\n"
    if analysis['rainy_day']:
        report += f"Це був дощовий день з {analysis['precipitation_level']} опадами.\n"
    else:
        report += "Опадів не було.\n"

    return report

def summarize_weather_analysis(analyses):
    hottest_day = max(analyses, key=lambda x: x['max_temperature'])
    windiest_day = max(analyses, key=lambda x: x['wind_speed'])
    most_humid_day = max(analyses, key=lambda x: x['humidity'])
    rainiest_day = max(analyses, key=lambda x: x['precipitation'])

    summary = f"Підсумковий звіт:\n"
    summary += f"Найспекотніший день: {hottest_day['date']} з максимальною температурою {hottest_day['max_temperature']}°C\n"
    summary += f"Найвітряніший день: {windiest_day['date']} зі швидкістю вітру {windiest_day['wind_speed']} км/год\n"
    summary += f"Найбільш вологий день: {most_humid_day['date']} з рівнем вологості {most_humid_day['humidity']}%\n"
    summary += f"Найбільш дощовий день: {rainiest_day['date']} з {rainiest_day['precipitation']} мм опадів\n"

    return summary

data = load_json('C:/Users/Overhaum/Documents/GitHub/lr-1-webscrapping-Overhaum/src/tokyo_weather_complex.json')


analyses = []
for day in data['daily']:
    analysis = analyze_daily_weather(day)
    analyses.append(analysis)
    print(generate_daily_report(analysis))

print(summarize_weather_analysis(analyses))
