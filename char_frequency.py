#!/usr/bin/python

import sys, operator

cipher_file = sys.argv[1]

with open(cipher_file, "r") as f:
	cipher = f.read().strip()

freq = {}

for c in cipher:
	if c in freq:
		freq[c] += 1
	else:
		freq[c] = 1

for c, f in sorted(freq.items(), key=operator.itemgetter(1))[::-1]:
	print "[%s] %d" % (c, f)
