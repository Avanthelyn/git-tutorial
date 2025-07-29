API_KEY = "912c622485ebcccfe6e75ebb3dc2de10"
CITY = "Lisbon"

def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

    try:
        response = requests.get(URL)
        data = response.json()
        return data
    except:
        print("Błąd")

def f_to_c(f):
    return (f - 32) * 5/9

result = fetch_weather()
print(result)

temp_min = result.get("main").get("temp_min")
pressure = result.get("main").get("pressure")
feels_like = result.get("main").get("feels_like")
wind_speed = result.get("wind").get("speed")
description = result.get("weather",)[0].get("description", "Brak danych")
longitude = result.get("coord").get("lon")
name = result.get("name")

print(f"Minimalna temperatura: {temp_min}°F")
print(f"Ciśnienie atmosferyczne: {pressure} hPa")
print(f"Temp odczuwalna):{feels_like}°F")
print(f"Wiatr):{wind_speed}km/h")
print(f"description: {description}")
print(f"Longitude: {longitude}")
print(f"Name: {name}")


import requests

API_KEY = "912c622485ebcccfe6e75ebb3dc2de10"
CITY = "Lisbon"

def convert_speed(value, units="km/h"):
    match units:
        case "km/h":
            return round(value * 3.6, 2)  # m/s → km/h
        case "m/s":
            return round(value / 3.6, 2)  # km/h → m/s
        case _:
            return value  # fallback

def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(URL)
        data = response.json()
        return data
    except:
        print("Błąd")

result = fetch_weather()

wind_speed = result.get("wind", {}).get("speed", 0)

wind_kmh = convert_speed(wind_speed, "km/h")

print(f"Prędkość wiatru: {wind_speed} m/s")
print(f"Prędkość wiatru: {wind_kmh} km/h")