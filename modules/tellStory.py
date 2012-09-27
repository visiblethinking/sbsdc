#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# title: tellStory
# file: tellStory.py
# description: Local stories for SBSDC
# language: python
# 
# authors: Andrew Hyder
# date: 9/26/2012
# version: 1.0.0
# notes: Tell a story about the bus stop
#
# keywords: overheard, story
#
# # # # # # # # # # # # # # # # # # # # # #
import sys
phoneNum = sys.argv[1]
lat = sys.argv[2]
lon = sys.argv[3]
message = sys.argv[4]

w = open('localstories.txt','a')
w.write(message)
w.write('||')
w.close()