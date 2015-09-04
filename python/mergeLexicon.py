__author__ = 'sjai013'

import sys
import os.path

# Parse lexicon file.
# Lexicon should be of format [WORD]\t[SPACE-DELIMITED PHONES]
# Space-delimited phones may also contain special characters.
# ' is used to denote a stress
# - is used to denote a syllable break
# The output is a dictionary of the format (each key is associated with a 4-length list):
#   WORD - [pronunciation, pronunciation without stress,
#           pronunciation without syllables, pronunciation without stress OR syllables]
def parseLex(file):
    lex = dict()
    for line in open(file).readlines():
        line = line.translate(None,'\n').split('\t')
        elements = list()
        elements.insert(0,line[1])
        elements.insert(1,elements[0].replace("' ",""))

        elements.insert(2,elements[0].replace("- ",""))
        elements.insert(3,elements[0].replace("' ","").replace("- ",""))
        lex[line[0]] = elements

    return lex


def matchPronunciation(primaryLex, secondaryLex):
    for word in primaryLex:
        if word in secondaryLex:
            if primaryLex[word][3] == secondaryLex[word][3]:
                print word


if len(sys.argv) < 5:
    print "Merges SECONDARY LEXICON into PRIMARY LEXICON by modifying elements" \
          " of all words in PRIMARY LEXICON to match those in SECONDARY LEXICON " \
          "(obviously, only if words exist in both dictionaries), and creates a new lexicon, NEW LEXICON."
    print "ELEMENTS TO MODIFY may be any combinations of:"
    print "\tp - pronunciation"
    print "\ts - syllable markers"
    print "\tt - stress markers"
    print "The pronunciation (p) option looks for all words present in SECONDARY LEXICON and PRIMARY LEXICON " \
          "and modifies the pronunciation of the PRIMARY LEXICON to match the SECONDARY LEXICON."
    print "The syllable markers (s) option adds syllable markers to PRIMARY LEXICON, if the pronunciations " \
          "of the SECONDARY LEXICON and PRIMARY LEXICON match (matching is independent of stress/syllable markers)."
    print "The stress markers (t) option adds syllable markers to PRIMARY LEXICON, if the pronunciations " \
          "of the SECONDARY LEXICON and PRIMARY LEXICON match (matching is independent of stress/syllable markers)."
    print "They are done in the same order as input into the command line"
    print "USAGE: ", sys.argv[0], " [PRIMARY LEXICON] [SECONDARY LEXICON] [NEW LEXICON] [ELEMENTS TO MODIFY]"
    print "EXAMPLE: ", sys.argv[0], " main.lex secondary.lex new.lex st"
    sys.exit()

primaryLexFilename = sys.argv[1]
secondaryLexFilename = sys.argv[2]
newLexicon = sys.argv[3]
options = sys.argv[4]

if not os.path.exists(primaryLexFilename) or not os.path.exists(secondaryLexFilename):
    print "Unable to read one of the input files"
    sys.exit()


# Read both lexicon into memory.
primaryLex = parseLex(primaryLexFilename)
secondaryLex = parseLex(secondaryLexFilename)


matchPronunciation(primaryLex, secondaryLex)