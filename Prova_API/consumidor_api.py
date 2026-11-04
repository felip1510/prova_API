import requests

url = 'https://api.open-meteo.com/v1/forecast'
params={
    "latitude": -26.4861,
    "longitude": -49.0667,
    "hourly": ["temperature_2m", "precipitation", "wind_speed_10m", "apparent_temperature"],
    "current": ["temperature_2m", "relative_humidity_2m"],}

resposta = requests.get(url, params=params)

dados = resposta.json()