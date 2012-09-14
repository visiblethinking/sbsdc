#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# title: neighborhood
# file: neighborhood.py
# description: Neighborhood module for SBSDC
# language: python
# 
# authors: Andrew Hyder
# date: 9/11/2012
# version: 1.0.0
# notes: fetches and sends latest weather forecast
#
# keywords: weather, forecast
#
# # # # # # # # # # # # # # # # # # # # # #
import sys, urllib, simplejson, datetime
lat = sys.argv[2]
lon = sys.argv[3]

get_hood_url = 'http://query.mapfluence.com/2.0/faa2473800838e5a0b407b40b3ab93ed/spatialquery.json?from=umi.neighborhoods.geometry&select=name'
get_hood_url = get_hood_url + '&where=intersects({%22type%22:%22Point%22,%22coordinates%22:['+str(lat)+','+str(lon)+']})'

response = urllib.urlopen(get_hood_url)
for line in response:
	response_dict = simplejson.loads(line)

for feature in response_dict['features']:
	print feature['properties']['name']
