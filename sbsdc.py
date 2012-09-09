# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# file: sbsdc.py
# description: core program for SBSDC
# language: python
# 
# authors: Anders Finn (anders@visiblethinking.com)
# date: 9/8/2012
# version: 1.0.5
# notes: for now does not do geolocation, just uses San Francisco
#
# # # # # # # # # # # # # # # # # # # # # # 
import socket
import sys
import datetime
import os
   
def get_location(location):
    geo_lat="37.7750 N"
    geo_long = "122.4183 W"  
    return(geo_lat,geo_long)

module_name = []
module_lang = {}
module_keys = {}
for module in os.listdir("%s/modules" % os.getcwd()):
   x = ''
   f = open("modules/%s" % module, 'r')
   for line in f.readlines():
      if "Title" in line:
         module_name.append(line.split("Title: ")[1])
         x = line.split("Title: ")[1][:-1]
      if "# Language:" in line:
         module_lang[x] = line.split("Language: ")[1][:-1]
         lang = ''
      if "# Keywords:" in line:
         module_keys[x] = line.split("Keywords: ")[1][:-1]
   print "\nOpening file modules/%s. written in %s with keywords: %s." % (module, module_lang[x], module_keys[x])
   if oct(os.stat("modules/%s" % module)[0]) != oct(33277):
      print "Module %s has file permissions %s, fixing. . . " % (module, oct(os.stat("modules/%s" % module)[0]))
      os.system("chmod 775 modules/%s" % module)
   
HOST = 'visiblethinking.com'                 # Symbolic name meaning the local host
PORT = 13208               # Arbitrary non-privileged port
s = None
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
    geo = message.split("+")[0]
    geo = get_location(message.split(" ")[0])
    message = " ".join(message.split("+")[1:])
    open("sbsdc.log", "w").write("%s: %s | %s\n" % (datetime.datetime.now(), sender, message))
conn.close()