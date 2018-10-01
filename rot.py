#!/usr/bin/python3

import sys, string

if len(sys.argv) < 2:
	sys.exit('Usage: rot.py message')

cipher = sys.argv[1]

for rot in range(1, 27):
	charset_lowercase = string.ascii_lowercase[rot:] + string.ascii_lowercase[:rot]
	charset_uppercase = string.ascii_uppercase[rot:] + string.ascii_uppercase[:rot]
	roted = ''

	for ch in cipher:
		if ch in string.ascii_lowercase:
			roted += charset_lowercase[string.ascii_lowercase.index(ch)]
		elif ch in string.ascii_uppercase:
			roted += charset_uppercase[string.ascii_uppercase.index(ch)]
		else:
			roted += ch

	print('[%02d] %s' % (rot, roted))
