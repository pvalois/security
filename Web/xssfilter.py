#!/usr/bin/env python3

from mechanize import *
import sys

try: 
  url=sys.argv[1]
except:
  url = input("Enter the full url : ")

try: 
  vectors=sys.argv[2]
except:
  vectors="vectors_XSS.txt"

attack_no = 1
browser=Browser()
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

with open (vectors) as x:

  for line in x:
    print (attack_no)
    browser.open(url)
    browser.select_form(nr = 0)
    browser["message"] = line
    res = browser.submit()
    content = res.read()
    print (content)

    if line in str(content):
       print("Possible XSS")
       output = open("response-" + str(attack_no) + ".txt", "w")
       output.write(content)
       output.close()

    attack_no += 1
