import requests

SECRET_KEY = "0c73de498a1ab07cb6ac3ace571131d9"

parameters = {"lat": "47.498", "lon": "19.0399", "mode": "json", "exclude": "current,minutely,daily", "appid": SECRET_KEY}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
umbrella = False
for i in range(12):
    # print(weather_data["hourly"][i]["weather"][0]["description"])
    if weather_data["hourly"][i]["weather"][0]["id"] < 700: umbrella = True

if umbrella: print("Bring an umbrella")
else: print("You don't need an umbrella")
