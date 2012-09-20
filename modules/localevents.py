#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# title: localevents
# file: localevents.py
# description: Local Events
# language: python
# 
# authors: Andrew Hyder
# date: 9/20/2012
# version: 1.0.0
# notes: local events
#
# keywords: events
#
# # # # # # # # # # # # # # # # # # # # # #
import sys, urllib, simplejson, datetime
from xml.dom.minidom import parseString
#phoneNum = sys.argv[1]
lat = sys.argv[2]
lon = sys.argv[3]
#message = sys.argv[4]
eb_api = 'http://api.everyblock.com/0.1/newsitems/?api_key=ifxni5AtKmG6cPI&metro=sf&schemas=34'
response = urllib.urlopen(eb_api)
xml_response = ''
for line in response:
	xml_response = xml_response+line

xml = parseString(xml_response)
newsitems_node = xml.getElementsByTagName('newsitems')
newsitems = newsitems_node[0].childNodes
for newsitem in newsitems:
	print newsitem.nodeType

# newsitems = events[0].getElementsByTagName('newsitem')[0]
# print newsitems.getAttribute('title')