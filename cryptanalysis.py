#!/usr/bin/python
import sys, os
if len(sys.argv) < 2: sys.exit("Usage: cryptanalysis.py encrypted.raw")
if not os.path.isfile(sys.argv[1]): sys.exit("File not found")
with open(sys.argv[1], "rb") as f: cipher = f.read()
print "\n+----------[ Cryptanalysis by t3h XRUST ]+++\n|"
print "+ Common Structures:"
print "|--- Fixed-length data"
print "|--- Variable-length data with separator chars"
print "|--- Variable-length data with length fields"
print "+ Common Mistakes:"
print "|--- Home-grown encryption"
print "|--- Insecure cipher mode (ECB, CBC, OFB, ...)"
print "|--- Poor key selection / Insufficient key length / Key reuse"
print "|--- Insecure random number generator"
print "|"
import entropy
print "+ Entropy:           %s" % entropy.shannon_entropy(cipher)
import collections
freq = collections.Counter(cipher)
print "+ Common Characters: %s" % freq.most_common(5)
length = len(cipher)
print "+ Ciphertext Length: %d bytes" % length
print "|---  8 byte blocks: %d (remainder: %d bytes)" % (length/8, length%8)
print "|--- 16 byte blocks: %d (remainder: %d bytes)" % (length/16, length%16)
print "|\n+" + "-"*40 + "+++"
