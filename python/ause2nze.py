__author__ = 'sjai013'

import sys
import os.path

if len(sys.argv) < 2:
    print "USAGE: ", sys.argv[0], " [AUSE LEXICON]"
    sys.exit()

readFile = sys.argv[1]

if not os.path.exists(readFile):
    sys.exit("Input file not readable")

lines = open(readFile).readlines()

words = dict()

for line in lines:
    line = line.split(",")
    words[line[0]] = line[1].strip()


lettersToCheck = dict()
lettersToCheck["{ns"] = ["ance","ans"]
lettersToCheck["{ntS"] = ["anch"]
lettersToCheck["{nS"] = ["anch"]
lettersToCheck["{nt"] = ["ant"]
lettersToCheck["{f"] = ["aph"]

i = 0
for word in sorted(words):
    for phone in lettersToCheck:
        for item in lettersToCheck[phone]:
            if (item in word) & (phone in words[word]):
                i += 1
                print str(i) + '\t' + word + '\t' + words[word]