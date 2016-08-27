#!/usr/bin/python

import string, argparse
from itertools import cycle

argsParser = argparse.ArgumentParser(description="Vigenere Encrypt/Decrypt")
argsParser.add_argument("file", metavar="text file", nargs="?")
argsParser.add_argument("key", metavar="key", nargs="?")
args = argsParser.parse_args()


def encrypt(key, plaintext):
    """
    Encrypt the string and return the ciphertext
    http://programeveryday.com/post/implementing-a-basic-vigenere-cipher-in-python/
    """
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: string.uppercase.index(x) + string.uppercase.index(y), pair)
        result += string.uppercase[total % 26]

    return result


def decrypt(key, ciphertext):
    """
    Decrypt the string and return the plaintext
    http://programeveryday.com/post/implementing-a-basic-vigenere-cipher-in-python/
    """
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: string.uppercase.index(x) - string.uppercase.index(y), pair)
        result += string.uppercase[total % 26]

    return result


with open(args.file, "r") as f:
	txt = f.read().strip().replace(" ","").replace("\n", "").upper()

print 'Key: %s' % args.key
print 'Plaintext: %s' % txt
print 'Encrypted: %s' % encrypt(args.key, txt)
print 'Decrypted: %s' % decrypt(args.key, txt)