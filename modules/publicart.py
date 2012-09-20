#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# title: publicart
# file: publicart.py
# description: Public Art
# language: python
# 
# authors: Andrew Hyder
# date: 9/20/2012
# version: 1.0.0
# notes: public art
#
# keywords: art
#
# # # # # # # # # # # # # # # # # # # # # #
import sys, urllib, simplejson
lat = sys.argv[2]
lng = sys.argv[3]
carto_query = 'http://ondrae.cartodb.com/api/v2/sql?q='
carto_query = carto_query + 'SELECT%20title,location_description%20FROM%20sf_civic_art_collect%20WHERE%20ST_DISTANCE(the_geom,SetSRID(ST_POINT('+str(lng)+','+str(lat)+'),4326))<0.003'
response = urllib.urlopen(carto_query)
for line in response:
	response_dict = simplejson.loads(line)

	for art in response_dict['rows']:
		print 'Title: ' + art['title']
		print 'Location: ' + art['location_description']
