#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# title: weather
# file: weather.py
# description: Weather modulefor SBSDC
# language: python
# 
# authors: Andrew Hyder
# date: 9/9/2012
# version: 1.0.0
# notes: fetches and sends latest weather forecast
#
# keywords: weather, forecast
#
# # # # # # # # # # # # # # # # # # # # # #
import sys, urllib2
args = sys.argv

print 'Fuck You.'

# # An easy way to do it
# r = urllib2.openurl('http://free.worldweatheronline.com/feed/weather.ashx?q=37.78,122.42&format=json&num_of_days=5&key=4e11214676001957120909')

# # Or using json module
# import json

# weather_text = r.text
# weather_json = json.loads(weather_text)

# for day in weather_json['data']['weather']:
# 	print day['date'] + ' ' + day['tempMaxF']
# 	print day['weatherDesc'][0]['value']




