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

    
def accept_conn(data):
    try:
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
	#open(logfile, "a").write("%s: %s | %s | %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), sender, module, message))
	newpid = os.fork()
	if newpid == 0:
	    open(logfile, "a").write("%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "ERROR!!! Module run failed on PID\n")
	    os.exit()
	else:
	    pids = (os.getpid(), newpid)
	    open(logfile, "a").write("%s: Running module %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), module))
	    try:
		print "hi"
		if NL == 1:
		    print "yo"
		    nl_data = nl_process(data,logfile,module_keys)
		    run_module(nl_data[1], geo, nl_data[2], sender, logfile)    
		else:
		    run_module(module, geo , message, sender, logfile)
	    except:
		open(logfile, "a").write("%s: Failed in run_module.\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    except:
	open(logfile, "a").write("%s: Failed in accept_conn\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    import sys
    import datetime
    import os
    import time
    import socket
    import threading
    
    # Read config file and sset global standards
    global hostname
    global port
    global logfile
    global NL
    NL=0
    
    try:
	config = open('config','r').readlines()
    except:
	open(config, "a").write("%s: Unable to open configuration file.\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), sender, module, message))
	os.exit()
    for line in config:
	x = line.split("=")
	if x[0].lower() == "hostname":
	    hostname = x[1].rstrip()
	elif x[0].lower() == "port":
	    port = x[1].rstrip()
	elif x[0].lower() == "logfile":
	    logfile = x[1].rstrip()
	elif x[0].lower() == "natural language":
	    if x[1].lower() == "on":
		NL = 1
    
    # open port and recieve incomming connections   
    open(logfile, "w").write("\n-----------------------------------------------------\n%s: Startup, checking core and scanning modules.\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    from modules import *
    from geocode import *
    backlog = 5 
    size = 1024 
    while 1:
	try:
	    soc = None
	    open(logfile, "a").write("%s: Starting server at %s:%s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), hostname, port))
	    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    port = int(float(port))
	    soc.bind((hostname,port))
	    soc.listen(backlog)
	    print "Server is now running on %s:%s" % (hostname, port)
	    try:
		while 1:
		    client, address = soc.accept() 
		    data = client.recv(size) 
		    if data:
			accept_conn(data) 
		    client.close()
	    except:
		open(logfile, "a").write("%s: ERROR!!! Server failed to run module: %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), client.recv(size)))
	except:
	    print "%s: WARNING!!! Server failed to start.%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), soc)
	    soc = None
	time.sleep(1)