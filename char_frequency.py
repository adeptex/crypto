#!/usr/bin/python

import sys, operator, argparse, string

argsParser = argparse.ArgumentParser(description="Character Frequency Analysis")
argsParser.add_argument("file", metavar="cipher file", nargs="?")
argsParser.add_argument("combo", metavar="char combo", nargs="?")
argsParser.add_argument("fuzz", metavar="fuzz position", type=int, nargs="?")
argsParser.add_argument("--charset", nargs="?")
argsParser.add_argument("--length", nargs="?", type=int, default=4, help="Max length for most-common combo check")
args = argsParser.parse_args()


eng_freq = "etaoinshrdlucmwfygpbvkxjqz".upper()

with open(args.file, "r") as f:
	cipher = f.read().strip().replace(" ","").replace("\n", "").upper()


def findOccurrencesOf(combo):
	global cipher
	
	count = 0
	for i in range(len(cipher)-len(combo)+1):
		if cipher[i:i+len(combo)] == combo:
			count += 1

	return (combo, count)


def transformComboToPlain(combo, charset):
	plain = ""

	for c in combo:
		i = charset.index(c)
		plain += eng_freq[i]

	return plain



freq = {}

for c in cipher:
	if c in freq:
		freq[c] += 1
	else:
		freq[c] = 1

freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)

if args.fuzz:
	if args.fuzz > len(args.combo)+1: 
		sys.exit("Combo/fuzz mismatch")

	freq = []

	for c in string.uppercase:
		test_combo = bytearray(args.combo)
		test_combo[args.fuzz-1] = c
		freq.append(findOccurrencesOf(str(test_combo)))

	freq = sorted(freq, key=lambda x: x[1], reverse=True)

	for combo, count in freq:
		print "%s occurences of %s" % (count, combo)

	sys.exit()


if args.combo:
	freq = findOccurrencesOf(args.combo)
	print "%s occurences of %s" % (freq[1], freq[0])
	sys.exit()

else: 			# print char frequencies
	plain = cipher
	charset = ""

	if args.charset:		# use a custom charset
		charset = args.charset
		for c, p in zip(args.charset, eng_freq):
			plain = plain.replace(c, p.lower())

	else:					# use charset from frequency analysis
		for (c, f), p in zip(freq, eng_freq):
			print "[%s] \t%s --> %s" % (f,c,p)
			plain = plain.replace(c, p.lower())
			charset += c


		
		# freq2 = []
		# freq3 = []
		# freq4 = []
		for analysisLength in range(2, args.length):
			freq = []
			analysisHistory = []

			for i in range(len(cipher)-analysisLength):
				test_combo = cipher[i:i+analysisLength]
				if test_combo in analysisHistory:
					continue
				else:
					analysisHistory.append(test_combo)
					freq.append(findOccurrencesOf(test_combo))
			
			#freq = set(freq)
			freq = sorted(freq, key=lambda x: x[1], reverse=True)
			print "\nMost common %d-letter combos:" % analysisLength
			for combo, count in freq[:24]:
				plain = transformComboToPlain(combo, charset)
				print "[%s] %s --> %s" % (count, combo, plain)


		# for c1 in cipher:
		# 	for c2 in cipher:
		# 		test_combo = c1+c2
		# 		freq2.append(findOccurrencesOf(str(test_combo)))

		# 		for c3 in cipher:
		# 			test_combo = c1+c2+c3
		# 			freq3.append(findOccurrencesOf(str(test_combo)))

		# 			for c4 in cipher:
		# 				test_combo = c1+c2+c3+c4
		# 				freq4.append(findOccurrencesOf(str(test_combo)))


		# freq2 = sorted(freq2, key=lambda x: x[1], reverse=True)
		# print "\nMost common 2-letter combos:"
		# for combo, count in freq2[:24]:
		# 	plain = transformComboToPlain(combo, charset)
		# 	print "[%s] %s --> %s" % (count, combo, plain)

		# freq3 = sorted(freq3, key=lambda x: x[1], reverse=True)
		# print "\nMost common 3-letter combos:"
		# for combo, count in freq3[:24]:
		# 	plain = transformComboToPlain(combo, charset)
		# 	print "[%s] %s --> %s" % (count, combo, plain)

		# freq4 = sorted(freq4, key=lambda x: x[1], reverse=True)
		# print "\nMost common 4-letter combos:"
		# for combo, count in freq4[:24]:
		# 	plain = transformComboToPlain(combo, charset)
		# 	print "[%s] %s --> %s" % (count, combo, plain)


	print "\nCharset: %s\n" % charset
	print plain[:100]



"""

    Order Of Frequency Of Single Letters
        E T A O I N S H R D L U
    Order Of Frequency Of Digraphs
        th er on an re he in ed nd ha at en es of or nt ea ti to it st io le is ou ar as de rt ve
    Order Of Frequency Of Trigraphs
        the and tha ent ion tio for nde has nce edt tis oft sth men
    Order Of Frequency Of Most Common Doubles
        ss ee tt ff ll mm oo
    Order Of Frequency Of Initial Letters
        T O A W B C D S F M R H I Y E G L N P U J K
    Order Of Frequency Of Final Letters
        E S T D N R Y F L O G H A K M P U W
    One-Letter Words
        a, I
    Most Frequent Two-Letter Words
        of, to, in, it, is, be, as, at, so, we, he, by, or, on, do, if, me, my, up, an, go, no, us, am
    Most Frequent Three-Letter Words
        the, and, for, are, but, not, you, all, any, can, had, her, was, one, our, out, day, get, has, him, his, how, man, new, now, old, see, two, way, who, boy, did, its, let, put, say, she, too, use
    Most Frequent Four-Letter Words
        that, with, have, this, will, your, from, they, know, want, been, good, much, some, time

"""