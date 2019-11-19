#!/usr/bin/python3 -u

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

if ("://" not in url):
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
         'script':{'src'},
         'applet':{'code'}}

glob=[url]

for ank in anchors:
  for line in soup.find_all(ank):
    for key in anchors[ank]:

      if line.get(key):
        link=line.get(key).lstrip().rstrip()


        if not '://' in link:
          link=url.rstrip("/")+"/"+link.lstrip("./")
        link=link.split("?")[0].split("#")[0]

        if link not in glob:
          glob.append(link)

for link in glob:
  print ("Will probe for old version of",link)

print ("")

busterer={'/index.html.old','/index.html.bak','/index.html.back','/index.html~',
          '/index.htm.old','/index.htm.bak','/index.htm.back','/index.htm~',
          '/index.php.old','/index.php.bak','/index.php.back','/index.php~',
          '.old','.back','.bak','~'}

for link in sorted(glob):
   if  (not url in link): continue
   for buster in busterer:
      treasure=link.rstrip("/")+buster
      #Uncomment next print to see progress 
      #print ("-- trying", treasure)
      status, response = http.request(treasure, headers=user_agent)
      if (status['status']=="200"):
        print ("++ ",treasure)
