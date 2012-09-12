#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# file: geocode.py
# description: Geolocation functions for SBSDC
# language: python
# 
# authors: Anders Finn (anders@visiblethinking.com), Andrew Hyder (hyd415@gmail.com)
# date: 9/9/2012
# version: 1.0.2
# notes:
#
# # # # # # # # # # # # # # # # # # # # # # 

import urllib2, json

# sub that does lookup of geolocation and retuns lat, long
def get_location(bus_stop_id):
	get_geo_url = 'http://ondrae.cartodb.com/api/v2/sql?q=SELECT latitude, longitude FROM sf_bus_stops WHERE stopid = ' + bus_stop_id
    response = urllib2.openurl('get_geo_url')
    for line in response:
    	json_response = json.loads(line)
    geo_lat = json_response['rows'][0]['latitude']
    geo_long = json_response['rows'][0]['longitude']
    return(geo_lat,geo_long)
   