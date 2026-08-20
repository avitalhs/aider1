import requests

def get_weather(city_name):
    url = f"https://api.open-meteo.com/v1/forecast?latitude=32.0853&longitude=34.7818&current_weather=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"HTTP Error: {response.status_code} Client Error for url: {url}")
        return None

if __name__ == '__main__':
    city_name = input("Enter the city name: ")
    weather_data = get_weather(city_name)
    
    if weather_data:
        current_weather = weather_data['current_weather']
        print(f"Current temperature in {city_name}: {current_weather['temperature']}°C")
        print(f"Wind speed: {current_weather['windspeed']} km/h")
        print(f"Wind direction: {current_weather['winddirection']}°")
        print(f"Is day: {'Yes' if current_weather['is_day'] else 'No'}")
        print(f"Weather code: {current_weather['weathercode']}")
