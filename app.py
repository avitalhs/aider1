import requests
import sys

def get_weather(city_name):
    url = f"https://api.open-meteo.com/v1/forecast?latitude=32.0853&longitude=34.7818&current_weather=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"HTTP Error: {response.status_code} Client Error for url: {url}")
        return None

if __name__ == '__main__':
    import os
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    
    # Reconfigure sys.stdout and sys.stdin to use UTF-8 encoding
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    
    print("Hello Avital ..")
    city_name = input("Enter the city name (Hebrew or English): ")
    weather_data = get_weather(city_name)
    
    if weather_data:
        current_weather = weather_data['current_weather']
        temperature = f"{current_weather['temperature']}°C"
        wind_speed = f"{current_weather['windspeed']} km/h"
        wind_direction = f"{current_weather['winddirection']}°"
        is_day = 'Yes' if current_weather['is_day'] else 'No'
        weather_code = current_weather['weathercode']
        
        print(f"Current temperature in {city_name}: {temperature}")
        print(f"Wind speed: {wind_speed}")
        print(f"Wind direction: {wind_direction}")
        print(f"Is day: {is_day}")
        print(f"Weather code: {weather_code}")
