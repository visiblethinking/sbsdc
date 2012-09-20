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

# Usage: walkingDirections.py <phone#> <lat> <long> <message>
import sys
import urllib
import simplejson
import urllib2

progName = sys.argv[0]
argList = sys.argv[1:]
argCount = len(argList)
messageList=[]
containsStr=''
messageStr=''


for i in range(argCount):
    if i == 0:
        phoneNum = argList[i]
    elif i == 1:
        srcLat = argList    [i]
    elif i == 2:
        srcLon = argList[i]
    else:
        messageList.append(argList[i])
        


for item in messageList:
    containsStr += 'name__icontains:' + str(item) + ','
for item in messageList:
    messageStr += str(item) + ' '


mfURL = 'http://query.mapfluence.com/2.0/faa2473800838e5a0b407b40b3ab93ed/spatialquery.json?from=umi.business_listings.geometry&select=name,geometry&where=AND(' + containsStr + 'intersects(range(10mi,%20{%22type%22:%22Point%22,%22coordinates%22:[' + str(srcLon) + ',' + str(srcLat) + ']})))'
mfResponse = urllib.urlopen(mfURL)

for line in mfResponse:
    mfDict = simplejson.loads(line)

try:
    x = mfDict['features'][0]['geometry']['coordinates'][0]
except NameError:
    print 'No listing for: ' + messageStr + 'found'
    exit()
except IndexError:
    print 'No listing for: ' + messageStr + 'found'
    exit()

print mfDict['features'][0]['geometry']['coordinates']

destLon = mfDict['features'][0]['geometry']['coordinates'][0]
destLat = mfDict['features'][0]['geometry']['coordinates'][1]


URL = 'http://open.mapquestapi.com/directions/v1/route?outFormat=json&routeType=pedestrian&from=' + str(srcLat) + ',' + str(srcLon) + '&to=' + str(destLat) + ',' + str(destLon) #'&callback=renderNarrative'
response = urllib.urlopen(URL)

for line in response:
    response_dict = simplejson.loads(line)

legs_list = response_dict['route']['legs']

legs_dict = legs_list[0]

for v in legs_dict['maneuvers']:
    print v['narrative'] + ';'

