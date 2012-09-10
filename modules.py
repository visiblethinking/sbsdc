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

module_name = []
module_lang = {}
module_keys = {}
for module in os.listdir("%s/modules" % os.getcwd()):
   x = ''
   f = open("modules/%s" % module, 'r')
   for line in f.readlines():
      if "Title" in line:
         y = line.split("Title: ")[1][:-1]
         module_name.append(y.lower())
         x = line.split("Title: ")[1][:-1].lower()
      if "# Language:" in line:
         y = line.split("Language: ")[1][:-1]
         module_lang[x] = y.lower()
         lang = ''
      if "# Keywords:" in line:
         y = line.split("Keywords: ")[1][:-1]
         module_keys[x] = y.lower()
   print "\nOpening file modules/%s. written in %s with keywords: %s." % (module, module_lang[x], module_keys[x])
   if oct(os.stat("modules/%s" % module)[0]) != oct(33277):
      print "Module %s has file permissions %s, fixing. . . " % (module, oct(os.stat("modules/%s" % module)[0]))
      os.system("chmod 775 modules/%s" % module)

# sub that forks off a call to external module
def run_module(name, location, message):
    language_map = { 'python' : 'python|py' , 'perl' : 'perl|pl' , 'php' : 'php|php'}
    PIPE = subprocess.PIPE
    x = language_map[module_lang[name.lower()]]
    lang = x.split("|")[1]
    prog = x.split("|")[0]
    process = subprocess.Popen(["%s" % prog,"/var/www/smartbusstop.com/sbsdc/modules/%s.%s" % (name.lower(), lang)], stdin=PIPE, stdout=PIPE, shell=False)
    output = ''
    while True:
      out = process.stdout.read(1)
      output += out
      if out == '' and process.poll() != None:
          break
      if out != '':
          #sys.stdout.write(out)
          sys.stdout.flush()
    for x in output.split("\n"):
      print x
    os._exit(0)