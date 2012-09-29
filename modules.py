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
import datetime
import httplib
import base64
import urllib
   
module_name = []
module_lang = {}
global module_keys
module_keys = {}

# Read modules/ directory and determine their name, language and keywords
for module in os.listdir("%s/modules" % os.getcwd()):
   x = ''
   # open directory modules/
   f = open("modules/%s" % module, 'r')
   # Search each file found line by line for keywords
   for line in f.readlines():
      # If Title is found, save to memory cache and create a list for that module
      if "title" in line:
         y = line.split("title: ")[1][:-1]
         module_name.append(y.lower())
         x = line.split("title: ")[1][:-1].lower()
      # If Language found, save to memory cache
      if "# language:" in line:
         y = line.split("language: ")[1][:-1]
         module_lang[x] = y.lower()
         lang = ''
      # If Keywords found, save to memory cache 
      if "# keywords:" in line:
         y = line.split("keywords: ")[1][:-1]
         module_keys[x] = y.lower()
         # Write new module to logfile and check and repair permissions
   open("../logs/sbsdc.log", "a").write("%s: Opening file modules/%s. written in %s with keywords: %s.\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), module, module_lang[x], module_keys[x]))
   if oct(os.stat("modules/%s" % module)[0]) != oct(33277):
      open("../logs/sbsdc.log", "a").write("%s: Warning!! Module %s has file permissions %s, fixing. . . \n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), module, oct(os.stat("modules/%s" % module)[0])))
      os.system("chmod 775 modules/%s" % module)

open("../logs/sbsdc.log", "a").write("%s: Done loading modules. \n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# sub that forks off a call to external module
def run_module(name, location, message, tosms, logfile):
   try:
      prog = langs[module_lang[name.lower()]].split("|")[0]
      lang = langs[module_lang[name.lower()]].split("|")[1]
      myoutput = None
      PIPE = subprocess.PIPE
      open(logfile, "a").write("%s: %s%s %s %s %s %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name.lower(), lang, tosms, location[0], location[1], message))
      process = subprocess.Popen(["%s" % prog, "%s/modules/%s%s" % (os.getcwd(), name, lang), tosms, location[0], location[1], message], stdin=PIPE, stdout=PIPE, shell=False)
      myoutput = process.stdout.read()
      open(logfile, "a").write("%s: Running %s looking for %s.\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name.lower(), message))
   except:
      open(logfile, "a").write("%s: ERROR!!! Failed to run: %s%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name.lower(), lang), tosms, location[0], location[1], message)
      myoutput = "Sorry there was an error in your message."
   
   try:
      username = "AC47761615be8d2db6fcf6512360fb7815"
      password = "89a918aa03f5c16d5f8dac2bb69c0431"
      params = {'From' : '14154187890', 'To' : tosms, 'Body' : myoutput}
      params = urllib.urlencode(params)
      auth = base64.encodestring("%s:%s" % (username, password)).replace('\n', '')
      headers = {"Authorization" : "Basic %s" % auth, 'Content-Type': 'application/x-www-form-urlencoded'}
   except:
      open(logfile, "a").write("%s: Unable to load txt header.\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
   
   try:
      conn = httplib.HTTPSConnection("api.twilio.com")
      conn.request("POST", "/2010-04-01/Accounts/AC47761615be8d2db6fcf6512360fb7815/SMS/Messages.xml", params, headers)
      response = conn.getresponse()
      data = response.read()
      conn.close()
   except:
      open(logfile, "a").write("%s: Unable to load send text.\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
   
      
      
langs = {}
try:
   langfile = open('languages','r')
except:
   open(logfile, "a").write("%s: Unable to open languages file.\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), sender, module, message))
   os.exit()
for line in langfile:
   if not line[0] == "#":
      x=line.split("|")
      langs[x[0].rstrip()] = "%s|%s" % (x[1].rstrip(),x[2].rstrip())