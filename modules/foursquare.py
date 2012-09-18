#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# title: foursquare
# file: foursquare.py
# description: Local Places
# language: python
# 
# authors: Andrew Hyder
# date: 9/18/2012
# version: 1.0.0
# notes: local shit
#
# keywords: places, food, drink, art
#
# # # # # # # # # # # # # # # # # # # # # #
import sys, urllib, simplejson, datetime
phoneNum = sys.argv[1]
lat = sys.argv[2]
lon = sys.argv[3]
message = sys.argv[4]
fq_api = 'https://api.foursquare.com/v2/venues/search'
location = '?ll='+str(lat)+','+str(lon)
limit = '&limit=1'
radius = '&radius=300'
query = '&query='+message
oauth_key ='&oauth_token=EIIMHUKS2TFQALQMUBRGUZQ4QVLUEUTDR4MG0U2UZ1DLND5E&v=20120917'
response = urllib.urlopen(fq_api+location+limit+query+radius+oauth_key)

for line in response:
	response_dict = simplejson.loads(line)

	for venue in response_dict['response']['venues']:
		print venue['name']
		print str(venue['location']['lat'])+','+str(venue['location']['lng'])