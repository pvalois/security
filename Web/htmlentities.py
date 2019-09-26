#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, urllib as ul;

try:
  print ul.unquote_plus(sys.argv[1])
except:
  print "Usage : %s <string_to_decode>" %(sys.argv[0])
