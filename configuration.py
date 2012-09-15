#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# file: configuration.py
# description: settings core program for SBSDC
# language: python
# 
# authors: Anders Finn (anders@visiblethinking.com)
# date: 9/12/2012
# version: 1.0.0
# notes: all known configuation vars
#
# # # # # # # # # # # # # # # # # # # # # #

# TCP/IP hostname and port server listens for incomming Twilio sms messages on
global hostname
hostname = "visiblethinking.com"
global port
port = 13208

# Logging file
global logfile
logfile = "/var/www/smartbusstop.com/logs/sbsdc.log"

