#!/usr/bin/python

import sys, string

cipher = sys.argv[1].upper()

for rot in range(1, 27):
	plain = ""
	for c in cipher:
		try:
			i = string.uppercase.index(c)
			i = (i + rot) % len(string.uppercase)
			plain += string.uppercase[i]
		except:
			plain += c

	print "[%02d] %s" % (rot, plain)
