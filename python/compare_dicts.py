__author__ = 'sjai013'

def replacePhone(phoneset, old, new):
    for phones in phoneset:
        phoneset[phones] = phoneset[phones].replace(old, new)

import random;

# Read ALD lexicon (in a transformed SAMPA format)

f = open("../ald/lexicon.txt");
temp = f.readlines();

ald = dict()
for line in temp:
    ald[line.split("\t")[0]] = line.split("\t")[1].replace("\n","").split(",")[0]

# Read MAUS dictionary (in SAMPA format)

f = open("../alveo/all.txt")
temp = f.readlines();

alveo = dict()
for line in temp:
    alveo[line.split(",")[0]] = line.split(",")[1].replace("\n","")


# Transform the ALD pronunciation to SAMPA - need to define a 1:1 transformation
# Not all phones are one character long - some are two.  So, need to begin search with two-character long phones

#####################################################################
###################### Transform ALD to SAMPA #######################
#####################################################################
# Now we can compare the two dictionaries, and find:
# (1) words that are unique to each dictionary,
# (2) words that have differing pronunciations in the dictionary


#####################################################################
##### (1) Find unique words (i.e. words only in one dictionary) #####
#####################################################################
unique_words = list(set(ald.keys()) ^ set(alveo.keys()))

# Also find words that are in both dictionaries (so we can compute the
# Modified SAMPA --> SAMPA rules)
common_words = list(set(ald.keys()) & set(alveo.keys()))

#####################################################################
########### (2) Find words with differing pronunciations ############
#####################################################################

# Perform replace in the ALD dictionary so they match the SAMPA phones in the MAUS dictionary
replacePhone(ald,"a:","6:")
replacePhone(ald,"A","{")
replacePhone(ald,"EI","{I")
replacePhone(ald,"V","6")
replacePhone(ald,"r","r\\")
replacePhone(ald,"u:","}:")
replacePhone(ald,"E","e")
replacePhone(ald,"@U","@}")
replacePhone(ald,"6:U","{O")
replacePhone(ald,"6:I","Ae")

#Not sure about these
#replacePhone(ald,"@:","3:")
#replacePhone(ald,"3:","o:")


replacePhone(ald,"`","")
replacePhone(ald," ","")


replacePhone(alveo,"`","")



# Print some random words common to both, so we can compare the symbols
random.seed()

f = open("common_words.txt", mode="w")

for i in range(1,100):
    word = random.choice(common_words)
    f.write(word + '\t' + ald[word] + '\t' + alveo[word]+'\n')

f.close()

f = open("differences.txt", mode="w")

for word in common_words:
    if (ald[word] != alveo[word]):
        f.write(word + '\t' + ald[word] + '\t' + alveo[word] + '\n')