#!/usr/bin/env python3 
# coding: utf-8

import r2pipe
import sys
import os

try:
  binary=sys.argv[1]
except:
  print ("Usage : %s <binary>" %(sys.argv[0]))
  sys.exit(2)

filename=os.path.basename(binary)

r = r2pipe.open(binary)
r.cmd("aaa")
r.cmd('ag main > main.dot')
os.system ("dot -Tjpg -o "+filename+".jpg main.dot")
os.remove ("main.dot")

