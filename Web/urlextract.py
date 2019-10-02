#!/usr/bin/python3 

import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import sys


try:
  url=sys.argv[1]
except:
  print ("Usage : "+sys.argv[0]+" <url>")
  sys.exit(0)

http = httplib2.Http()
user_agent = {'User-agent': 'Mozilla/5.0'}

if ("http" not in url):
  url="http://"+url

status, response = http.request(url, headers=user_agent)

soup = BeautifulSoup(response,"html.parser")

anchors={'a':{'href'},
         'area':{'href'},
         'base':{'href'},
         'img':{'src','href'},
         'body':{'background'},
         'frame':{'src'},
         'iframe':{'src'},
         'overlay':{'src'},
         'scrpts':{'src'},
         'embed':{'src'},
         'bgsound':{'src'},
         'applet':{'code'}}

glob=[]

for ank in anchors:
  for line in soup.find_all(ank):
    for key in anchors[ank]:
      if line.get(key):
        if (line.get(key) not in glob):
          glob.append(line.get(key))

for link in sorted(glob):
    if link[0] == '/':
       link=url+link
    print (link)
