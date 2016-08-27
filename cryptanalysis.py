#!/usr/bin/python
import sys, os
if len(sys.argv) < 2: sys.exit("Usage: cryptanalysis.py encrypted.raw")
if not os.path.isfile(sys.argv[1]): sys.exit("File not found")
with open(sys.argv[1], "rb") as f: cipher = f.read()
print '''
[+]----------[ Cryptanalysis by t3h XRUST ]----------------------------------[+]
 |
 + Common Structures:
 |	* Fixed-length data
 |	* Variable-length data with separator chars
 |	* Variable-length data with length fields
 |
 + Common Mistakes:
 |	* Home-grown encryption
 |	* Insecure cipher mode (ECB, CBC, OFB, ...)
 |	* Poor key selection / Insufficient key length / Key reuse
 |	* Insecure random number generator
 |
'''
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
