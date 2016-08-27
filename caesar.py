#!/usr/bin/python

import sys, string

cipher = sys.argv[1].upper()

charset = string.uppercase

for shift in range(27):
	plain = [charset[(string.uppercase.index(c) + shift) % len(charset)] for c in cipher]
	print "[%02d] %s" % (shift, "".join(plain))