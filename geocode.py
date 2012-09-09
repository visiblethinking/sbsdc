#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# file: geocode.py
# description: Geolocation functions for SBSDC
# language: python
# 
# authors: Anders Finn (anders@visiblethinking.com)
# date: 9/9/2012
# version: 1.0.1
# notes: for now does not do geolocation, just uses San Francisco
#
# # # # # # # # # # # # # # # # # # # # # # 


# sub that does lookup of geolocation and retuns lat, long
def get_location(location):
    geo_lat="37.7750 N"
    geo_long = "122.4183 W"  
    return(geo_lat,geo_long)
   