import requests
from urllib import parse


def get_forecast(city):
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = parse.urlencode({
          "q": city,
          "appid": "895ef06c0d93fd43f9c290e033d5fd3b",
          "units": "metric"
        })
        url = "".join((url, "?", params))
        res_weather = requests.get(url)
        res_weather.status_code
        response_json = res_weather.json()
        print(f"Temperature: {response_json['main']['temp']}, Pressure: {response_json ['main']['pressure']}, Humidity: {response_json ['main']['humidity']}")
    except:
        print('Error')
