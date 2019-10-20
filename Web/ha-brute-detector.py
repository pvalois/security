#!/usr/bin/env python3 
# coding: utf8

import sys 
import re
import shlex
import getopt
import os.path
import collections
from ipwhois import IPWhois
from dumper import dump

''' 
Oct 20 01:01:49 teknomage haproxy[17010]: 103.60.221.239:58703 [20/Oct/2019:01:01:49.151] http-in teknomage/localhost 0/0/0/0/0 404 751 - - ---- 3/3/0/1/0 0/0 "GET /mysql/sqlmanager/index.php HTTP/1.1"
'''

logfile="/var/log/haproxy.log"

try:
  options, remain = getopt.getopt(sys.argv[1:], "f:", ["file:"])
except getopt.GetoptError as err:
  print (err)
  sys.exit(1)

for opt, optarg in options:
  if opt in ("-f","--file"): logfile=optarg

print ("Parsing file", logfile)

if (not os.path.isfile(logfile)):
  print ("file non existent")
  sys.exit(0)

log404=[]

cpt=0
with open(logfile, "r") as logfp: 
  for line in logfp:

    cpt=cpt+1
    try:
      month,day,time,host,pid,ip_port,timestamp,frontend,backend,_,error_code,content_soze,_,_,_,_,_,action=shlex.split(line,17)
    except:
      #print ("non parsable line @"+str(cpt))
      continue

    ip,port=ip_port.split(":")

    if (error_code=="404"):
      log404.append(ip)

freq = collections.Counter(log404)

print ("")
print ("Top 404") 
print ("-------------------------------------------------")

for candidat in freq:
   who = IPWhois(candidat)
   results = who.lookup_whois() 
   country=results['nets'][0]['country']

   print ("%15s | %5d | %s"  %(candidat,freq[candidat],country))
