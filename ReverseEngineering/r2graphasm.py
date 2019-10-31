#!/usr/bin/env python3 

import r2pipe
import sys
import os

try:
  binary=sys.argv[1]
except:
  print ("Usage : %s <binary>" %(sys.argv[0]))
  sys.exit(2)

try: 
  out=os.popen("radare2 -v").read()
  if ("radare2 2." in out): version=2
  if ("radare2 3." in out): version=3
except: 
  print ("No radare2 installed ???")
  sys.exit(0)

filename=os.path.basename(binary)

r = r2pipe.open(binary)
r.cmd("aaa")

if (version==2): 
  r.cmd('ag main > main.dot')

if (version==3): 
  r.cmd("s main")
  r.cmd('agfd > main.dot')

os.system ("dot -Tjpg -o "+filename+".jpg main.dot")
os.remove ("main.dot")

