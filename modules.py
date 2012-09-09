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
import subprocess
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

module_name = []
module_lang = {}
module_keys = {}
for module in os.listdir("%s/modules" % os.getcwd()):
   x = ''
   f = open("modules/%s" % module, 'r')
   for line in f.readlines():
      if "Title" in line:
         module_name.append(line.split("Title: ")[1][:-1])
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

# sub that forks off a call to external module
def run_module(name, location, message):
    language_map = { 'python' : 'python|py' , 'perl' : 'perl|pl' , 'php' : 'php|php'}
    PIPE = subprocess.PIPE
    p = subprocess.Popen(["python","/var/www/smartbusstop.com/sbsdc/modules/weather.py"], stdin=PIPE, stdout=PIPE, shell=False)
    p.stdin.write("10")
    p.stdin.flush()
    print p.stdout.read() 
    os._exit(0)