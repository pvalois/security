#!/usr/bin/env python3 
#-*- coding: utf-8 -*-

'''
Script pour extraire d'une capture pcap d'un réseaux wifi, les AP trouvées et afficher leur adresse mac et ssid
C'est un prérequis de filtrage d'information, nécessaire au cassage de clef avec aircrack-ng
'''

from scapy.all import *
from dumper import dump

try: 
  pcap=rdpcap(sys.argv[1])
except:
  print ("usage : %s <file.pcap>" %(sys.argv[0]))
  sys.exit(0)


ap_list=[]

for packet in pcap:
  if packet.haslayer(Dot11) :
     if packet.type == 0 and packet.subtype == 8:
        if packet.addr2 not in ap_list:
           ap_list.append(packet.addr2)
           print("Access Point found ... MAC [%s] and SSID [%s] " %(packet.addr2.upper(), packet.info.decode()))

