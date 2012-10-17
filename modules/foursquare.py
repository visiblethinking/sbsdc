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
import sys, urllib, simplejson, datetime, random
phoneNum = sys.argv[1]
bus_stop_lat = sys.argv[2]
bus_stop_lng = sys.argv[3]
message = sys.argv[4]
fq_api = 'https://api.foursquare.com/v2/venues/search'
location = '?ll='+str(bus_stop_lat)+','+str(bus_stop_lng)
limit = '&limit=5'
radius = '&radius=1000'
query = '&query='+message
oauth_key ='&oauth_token=EIIMHUKS2TFQALQMUBRGUZQ4QVLUEUTDR4MG0U2UZ1DLND5E&v=20120917'
response = urllib.urlopen(fq_api+location+limit+query+radius+oauth_key)

def get_walking_directions(bus_stop_lat, bus_stop_lng, dest_lat, dest_lng):
	mq_api = 'http://open.mapquestapi.com/directions/v1/route?outFormat=json&routeType=pedestrian&timeType=1'
	from_bus_stop = '&from=' + str(bus_stop_lat) + ',' + str(bus_stop_lng)
	to_dest = '&to=' + str(dest_lat) + ',' + str(dest_lng)
	response = urllib.urlopen(mq_api+from_bus_stop+to_dest)
	for line in response:
	    response_dict = simplejson.loads(line)
	legs_list = response_dict['route']['legs']
	legs_dict = legs_list[0]
	for v in legs_dict['maneuvers']:
	    print v['narrative']

for line in response:
	response_dict = simplejson.loads(line)	
	venue_count=0
	random_number=0
	
	for venue in response_dict['response']['venues']:
		venue_count+=1
		random_number=random.randint(0,venue_count-1)
	
	try:
		venue_name = response_dict['response']['venues'][random_number]['name']
		venue_lat = response_dict['response']['venues'][random_number]['location']['lat']
		venue_lng = response_dict['response']['venues'][random_number]['location']['lng']
		venue_address = response_dict['response']['venues'][random_number]['location']['address']
	except IndexError:
		sys.exit('No results.  Best ask someone else!')
	
	print '%s: %s' % (venue_name, venue_address)
	
	walking_directions=get_walking_directions(bus_stop_lat, bus_stop_lng, venue_lat, venue_lng)

	
