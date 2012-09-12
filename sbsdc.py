#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# file: sbsdc.py
# description: core program for SBSDC
# language: python
# 
# authors: Anders Finn (anders@visiblethinking.com)
# date: 9/8/2012
# version: 1.1.2
# notes: for now does not do geolocation, just uses San Francisco
#
# # # # # # # # # # # # # # # # # # # # # # 
import socket
import sys
import datetime
import os
sys.path.append("/var/www/smartbusstop.com/sbsdc")


# open port and recieve incomming connections   
HOST = 'visiblethinking.com'                 # Symbolic name meaning the local host
PORT = 13208               # Arbitrary non-privileged port
s = None
open("/var/www/smartbusstop.com/logs/sbsdc.log", "a").write("\n-----------------------------------------------------\n%s: Startup, checking core and scanning modules.\n" % datetime.datetime.now())
from modules import *
from geocode import *
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
	s = socket.socket(af, socktype, proto)
    except socket.error, msg:
	s = None
	continue
    try:
	s.bind(sa)
	s.listen(1)
    except socket.error, msg:
	s.close()
	s = None
	continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)
conn, addr = s.accept()
# we should fork here??

while 1:
    data = conn.recv(1024)
    if not data: break
    references = data.split('&')
    message = ""
    sender = ""
    for x in references:
	if "body=" in x.lower():
	    message = x[5:]
	if "from=" in x.lower():
	    sender = x[8:]
    module = message.split("+")[1]
    geo = get_location(message.split("+")[0])
    message = " ".join(message.split("+")[2:])
    open("/var/www/smartbusstop.com/logs/sbsdc.log", "a").write("%s: %s | %s | %s\n" % (datetime.datetime.now(), sender, module, message))
    newpid = os.fork()
    if newpid == 0:
         run_module(module, geo , message, sender)
    else:
         pids = (os.getpid(), newpid)
    if raw_input( ) == 'q': break
conn.close()