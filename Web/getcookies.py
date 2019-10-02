#!/usr/bin/env python3 

import requests
import sys
from dumper import dump

try:
  r = requests.get(sys.argv[1])
except: 
  print ("impossible to get cookies")
  sys.exit(0)

cookies=r.cookies
for cookie in cookies:
  print(cookie.name+"="+cookie.value, end="; ")
