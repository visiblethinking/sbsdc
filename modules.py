#!/usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # 
#
# project: Smart Bus Stops Done Dirt Cheap
# file: module.py
# description: module loader and loader program for SBSDC
# language: python
# 
# authors: Anders Finn (anders@visiblethinking.com)
# date: 9/9/2012
# version: 1.0.1
# notes: still working on getting return input
#
# # # # # # # # # # # # # # # # # # # # # # 

# search modules/ directory and determine name, language and keywords to available mods

import os
import sys
import subprocess
import httplib
import base64
import urllib

module_name = []
module_lang = {}
module_keys = {}
for module in os.listdir("%s/modules" % os.getcwd()):
   x = ''
   f = open("modules/%s" % module, 'r')
   for line in f.readlines():
      if "title" in line:
         y = line.split("title: ")[1][:-1]
         module_name.append(y.lower())
         x = line.split("title: ")[1][:-1].lower()
      if "# language:" in line:
         y = line.split("language: ")[1][:-1]
         module_lang[x] = y.lower()
         lang = ''
      if "# keywords:" in line:
         y = line.split("keywords: ")[1][:-1]
         module_keys[x] = y.lower()
   open("../logs/sbsdc.log", "a").write("Opening file modules/%s. written in %s with keywords: %s.\n" % (module, module_lang[x], module_keys[x]))
   if oct(os.stat("modules/%s" % module)[0]) != oct(33277):
      open("../logs/sbsdc.log", "a").write("Module %s has file permissions %s, fixing. . . \n" % (module, oct(os.stat("modules/%s" % module)[0])))
      os.system("chmod 775 modules/%s" % module)

# sub that forks off a call to external module
def run_module(name, location, message, sms):
    language_map = { 'python' : 'python|py' , 'perl' : 'perl|pl' , 'php' : 'php|php'}
    PIPE = subprocess.PIPE
    x = language_map[module_lang[name.lower()]]
    lang = x.split("|")[1]
    prog = x.split("|")[0]
    print "%s" % prog,"%s/modules/%s.%s" % (os.getcwd(), name.lower(), lang), message
    process = subprocess.Popen(["%s" % prog,"%s/modules/%s.%s" % (os.getcwd(), name.lower(), lang), location[0], location[1], message], stdin=PIPE, stdout=PIPE, shell=False)
    output = ''
    while True:
      out = process.stdout.read(1)
      output += out
      if out == '' and process.poll() != None:
          break
      if out != '':
          #sys.stdout.write(out)
          sys.stdout.flush()
    y=""
    for x in output.split("\n"):
       y+=x 

    
    username = "AC47761615be8d2db6fcf6512360fb7815"
    password = "89a918aa03f5c16d5f8dac2bb69c0431"
    params = {'From' : '14154187890', 'To' : sms, 'Body' : y}
    params = urllib.urlencode(params)
    auth = base64.encodestring("%s:%s" % (username, password)).replace('\n', '')
    headers = {"Authorization" : "Basic %s" % auth, 'Content-Type': 'application/x-www-form-urlencoded'}
    
    conn = httplib.HTTPSConnection("api.twilio.com")
    conn.request("POST", "/2010-04-01/Accounts/AC47761615be8d2db6fcf6512360fb7815/SMS/Messages.xml", params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    
    if data:
        1;
    else:
        print "Error updating..."
        os._exit(0) 