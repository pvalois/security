#!/usr/bin/env python3

''' 
pour un domaine, hote ou ip nous scannons sir les ports sont ouvert. si oui, nous faisons des requetes http et https et sortons les informations  
pertinentes
''' 

import socket
import sys
import requests
import urllib3
from bs4 import BeautifulSoup as bs

ports={80,443,8080,8443}
urllib3.disable_warnings()

def scan(target,port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    con = sock.connect((target,port))
    return True
  except:
    return False

def getinfo(url):
  try:
    response = requests.get(url, verify=False)
  except:
    return

  # as the algorithm is studip, it can request http on https andreverse, and get a 400 error code doing so, so we ignore
  if (response.status_code == 400):
    return

  print ("Url        : "+url)

  try:
    print ("Server     : "+response.headers['server'])
  except:
    print ("Server     : <Undisclosed>")

  print ("Page title : ", end="")

  soup = bs(response.content, 'lxml')
  try: 
    print(soup.select_one('title').text)
  except: 
    print ("NONE")

  print ("")
  
for target in sys.argv[1:]:
  for port in ports:
    if scan(target,port):
      getinfo("http://"+target+":"+str(port))
      getinfo("https://"+target+":"+str(port)) 
