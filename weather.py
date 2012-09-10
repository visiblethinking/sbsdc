# An easy way to do it
import requests

r = requests.get('http://free.worldweatheronline.com/feed/weather.ashx?q=37.78,122.42&format=json&num_of_days=5&key=4e11214676001957120909')

weather_json = r.json

for day in weather_json['data']['weather']:
	print day['date'] + ' ' + day['tempMaxF']
	print day['weatherDesc'][0]['value']


# Or using json module
import json

weather_text = r.text
weather_json = json.loads(weather_text)

for day in weather_json['data']['weather']:
	print day['date'] + ' ' + day['tempMaxF']
	print day['weatherDesc'][0]['value']
