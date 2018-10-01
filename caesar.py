#!/usr/bin/python3

import sys, string

cipher = sys.argv[1].upper()

charset = string.ascii_uppercase

for shift in range(27):
	plain = [charset[(charset.index(c) + shift) % len(charset)] for c in cipher]
	plain = ''.join(plain)
	print('[%02d] %s\t%s' % (shift, plain, plain.lower()))
