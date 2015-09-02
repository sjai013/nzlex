__author__ = 'sjai013'

import re
import sys
import os.path


def getFest2SAMPA():
    fest2sampa_phones = dict()
    fest2sampa_phones["i"] = "I"
    fest2sampa_phones["e"] = "e"
    fest2sampa_phones["a"] = "{"
    fest2sampa_phones["aa"] = "6:"
    fest2sampa_phones["o"] = "O"
    fest2sampa_phones["u"] = "U"
    fest2sampa_phones["uh"] = "6"
    fest2sampa_phones["ii"] = "i:"
    fest2sampa_phones["ei"] = "{I"
    fest2sampa_phones["oo"] = "o:"
    fest2sampa_phones["oul"] = "o"
    fest2sampa_phones["ou"] = "@}"
    fest2sampa_phones["uu"] = "}:"
    fest2sampa_phones["ai"] = "Ae"
    fest2sampa_phones["oi"] = "oI"
    fest2sampa_phones["ow"] = "{O"
    fest2sampa_phones["@@r"] = "3:"
    fest2sampa_phones["ir"] = "I@"
    fest2sampa_phones["@"] = "@"
    fest2sampa_phones["e+@"] = "e:"
    fest2sampa_phones["uw"] = "U\\"
    fest2sampa_phones["p"] = "p"
    fest2sampa_phones["t"] = "t"
    fest2sampa_phones["k"] = "k"
    fest2sampa_phones["b"] = "b"
    fest2sampa_phones["d"] = "d"
    fest2sampa_phones["g"] = "g"
    fest2sampa_phones["m"] = "m"
    fest2sampa_phones["n"] = "n"
    fest2sampa_phones["ng"] = "N"
    fest2sampa_phones["f"] = "f"
    fest2sampa_phones["th"] = "T"
    fest2sampa_phones["s"] = "s"
    fest2sampa_phones["sh"] = "S"
    fest2sampa_phones["v"] = "v"
    fest2sampa_phones["dh"] = "D"
    fest2sampa_phones["z"] = "z"
    fest2sampa_phones["ch"] = "tS"
    fest2sampa_phones["jh"] = "dZ"
    fest2sampa_phones["r"] = "r\\"
    fest2sampa_phones["y"] = "j"
    fest2sampa_phones["w"] = "w"
    fest2sampa_phones["l"] = "l"
    fest2sampa_phones["h"] = "h"
    fest2sampa_phones["t^"] = "4"
    fest2sampa_phones["l!"] = "l"
    fest2sampa_phones["n!"] = "n"
    fest2sampa_phones["m!"] = "m"
    fest2sampa_phones["zh"] = "Z"

    return fest2sampa_phones


if len(sys.argv) < 3:
    print "USAGE: ", sys.argv[0], " [FESTIVAL LEXICON] [SAMPA OUTPUT FILE]"
    sys.exit()

readFile = sys.argv[1]
writeFile = sys.argv[2]

if not os.path.exists(readFile):
    sys.exit("Input file not readable")


f = open(readFile).readlines()
words = dict()

for line in f:
    items = line.split('\t')
    word = items[0].replace("(\"","").replace("\"","")
    pronunciation = items[2]
    matches = re.findall(r"(\(\([A-Za-z0-9@^! ]*\)[0-9 ]+\))", pronunciation)
    words[word] = matches

sampa_words = dict()
for word in words:
    word_pronunciation = ""
    syllables = words[word]
    for syllable in syllables:
        m = re.match(r"\(+([A-Za-z0-9@^! ]+)\)([0-9 ]+)", syllable)
        syl_pronunciation = m.groups()[0].strip()
        stress = m.groups()[1].strip()
        if (stress == '1'):
            syl_pronunciation = "' " + syl_pronunciation

        word_pronunciation = word_pronunciation + " - " + syl_pronunciation

    word_pronunciation = word_pronunciation[3:] # Remove first instance of " - "
    sampa_words[word] = word_pronunciation




for word in sampa_words:
    pronunciation = sampa_words[word]
    phones = pronunciation.split(" ")
    fest2SAMPA = getFest2SAMPA()
    this_phone = ""

    for i in range(len(phones)):
        if phones[i] in fest2SAMPA:
            phones[i] = fest2SAMPA[phones[i]]

    phones = " ".join(phones)
    sampa_words[word] = phones


f = open(writeFile, "w")
for word in sorted(sampa_words):
    f.write(word + '\t' + sampa_words[word] + '\n')

f.close()