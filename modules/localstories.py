#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# title: localStories
# file: localStories.py
# description: Local stories for SBSDC
# language: python
# 
# authors: Andrew Hyder
# date: 9/26/2012
# version: 1.0.0
# notes: Hear a story about the bus stop
#
# keywords: overheard, local stories
#
# # # # # # # # # # # # # # # # # # # # # #
import sys, random
phoneNum = sys.argv[1]
lat = sys.argv[2]
lon = sys.argv[3]
try:
	message = sys.argv[4]

	# Write a message
	w = open('localstories.txt','a')
	w.write(message)
	w.write('||')
	w.close()
	print 'Got it. We\'ll tell others your story when they ask.'

except IndexError:
	r = open('localstories.txt','r')
	r_raw = r.read()
	stories = r_raw.split('||')
	i = random.randint(0,len(stories)-2)
	print stories[i]