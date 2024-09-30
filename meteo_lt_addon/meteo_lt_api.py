import requests
import json
import time
import sys
import os

def get_weather_data(location):
    url = f"https://api.meteo.lt/v1/places/{location}/forecasts/long-term"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def process_weather_data(data):
    if data and 'forecastTimestamps' in data:
        current = data['forecastTimestamps'][0]
        return {
            "temperature": current['airTemperature'],
            "wind_speed": current['windSpeed'],
            "humidity": current['relativeHumidity'],
            "condition": current['conditionCode']
        }
    return None

def main(interval, location):
    while True:
        data = get_weather_data(location)
        processed_data = process_weather_data(data)
        if processed_data:
            with open('/data/meteo_lt_weather.json', 'w') as f:
                json.dump(processed_data, f)
            print(f"Weather data updated: {processed_data}")
        else:
            print("Failed to update weather data")
        time.sleep(int(interval) * 60)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 meteo_lt_api.py <interval> <location>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
