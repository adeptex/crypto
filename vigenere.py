#!/usr/bin/python3

import sys, string
from itertools import cycle

if len(sys.argv) < 3:
	sys.exit('Usage: vigenere.py key message')

key = sys.argv[1].upper()
cipher = sys.argv[2].upper()
plain = ''
table = {}

for ch in string.ascii_uppercase:
    ch_idx = string.ascii_uppercase.index(ch)
    table[ch] = string.ascii_uppercase[ch_idx:] + string.ascii_uppercase[:ch_idx]

for pair in zip(cycle(key), cipher):
    k, c = pair
    c_idx = table[k].index(c)
    plain += string.ascii_uppercase[c_idx]

print('%s\n%s' % (plain, plain.lower()))
