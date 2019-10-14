#!/usr/bin/env python3
# coding: utf-8

''' 
pour un domaine, hote ou ip nous scannons sir les ports sont ouvert. si oui, nous faisons des requetes http et https et sortons les informations  
pertinentes
''' 

import socket
import sys
import requests
import urllib3
from bs4 import BeautifulSoup as bs
from getopt import *


ports={80,443,8080}
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
    # as the algorithm is stupid, it can request http on https andreverse, and get a 400 error code doing so, so we ignore
    response = requests.get(url, verify=False, allow_redirects=False)
    if (response.status_code == 400): return
  except:
    return

  print ("Url        : "+url)

  if ('server' in response.headers):
    print ("Server     : "+response.headers['server'])

  if ('Location' in response.headers):
    print ("Redirected : "+response.headers['Location'])
  else:
    soup = bs(response.content, 'lxml')
    if (soup.find('title')):
      print("Page title : "+soup.select_one('title').text)

  print ("")

################################## MAIN ######
 
try:
  opts, args = getopt(sys.argv[1:], "p:")
except GetoptError as err:
  print(err) # will print something like "option -a not recognized"
  print ("usage : "+sys.argv[0]+" <-p port,port,port,...>")
  print ("   default ports are : 80,443,8080")
  sys.exit(2)
    
for opt, arg in opts:
  if opt == "-p":
    ports={int(x) for x in list(arg.split(","))}
 
for target in args:
  for port in ports:
    if scan(target,port):
      getinfo("http://"+target+":"+str(port)+"/")
      getinfo("https://"+target+":"+str(port)+"/") 
