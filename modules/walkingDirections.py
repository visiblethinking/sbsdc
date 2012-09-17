#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# title: Walking Directions
# file: walkingDirections.py
# description: returns walking directions to a location.
# language: python
# 
# authors: Cameron Jeffries (camservo@gmail.com)
# date: 9/9/2012
# version: 1.0.0
# notes: .
#
# keywords: walking, walk, onfoot, walkingdir
#
# # # # # # # # # # # # # # # # # # # # # #
import sys
import urllib
import simplejson
from geopy import geocoders

progName = sys.argv[0]
argList = sys.argv[1:]
argCount = len(argList)
messageList=[]
messageStr=''

for i in range(argCount):
    if i == 0:
        phoneNum = argList[i]
    elif i == 1:
        srcLat = argList[i]
    elif i == 2:
        srcLon = argList[i]
    else:
        messageList.append(argList[i])
        

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
    
for item in messageList:
    messageStr += item + ' '

print messageStr

destLat = 37.5
destLon = -122.5

URL = 'http://open.mapquestapi.com/directions/v1/route?outFormat=json&routeType=pedestrian&from=' + str(srcLat) + ',' + str(srcLon) + '&to=' + str(destLat) + ',' + str(destLon) #'&callback=renderNarrative'

response = urllib.urlopen(URL)

for line in response:
    response_dict = simplejson.loads(line)

legs_list = response_dict['route']['legs']

legs_dict = legs_list[0]

for v in legs_dict['maneuvers']:
    print v['narrative'] + ';'
    


