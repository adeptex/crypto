#!/usr/bin/python

import argparse, os

argsParser = argparse.ArgumentParser(description='XOR by t3h XRUST')
group = argsParser.add_mutually_exclusive_group(required=True)
group.add_argument("--key", "-k", help="Key (text)")
group.add_argument("--keyfile", "-f", help="Key (file)")
argsParser.add_argument("file", metavar='FILE', help='File with data to XOR')
args = argsParser.parse_args()

if args.key:
	key = args.key
elif args.keyfile:
	if not os.path.isfile(args.keyfile):
		sys.exit("Keyfile not found.")
	with open(args.keyfile, "rb") as f:
		key = f.read()

if not len(key): sys.exit("Key missing.")
if not os.path.isfile(args.file): sys.exit("File not found.")

with open(args.file, "rb") as f: 
	data = f.read()
xor = ""
for i in xrange(len(data)):
	xor += chr(ord(data[i]) ^ ord(key[i%len(key)]))
print xor
