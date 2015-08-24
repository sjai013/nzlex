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

unique_alveo = list(set(alveo.keys()) - set(common_words))



#####################################################################
########### (2) Find words with differing pronunciations ############
#####################################################################

# Perform replace in the ALD dictionary so they match the SAMPA phones in the MAUS dictionary
replacePhone(ald, "A", "{")
replacePhone(ald, "EI", "{I")
replacePhone(ald, "a:U", "{O")
replacePhone(ald, "a:I", "Ae")
replacePhone(ald, "a:", "6:")
replacePhone(ald, "V", "6")
replacePhone(ald, "r", "r\\")
replacePhone(ald, "u:", "}:")
replacePhone(ald, "E", "e")
replacePhone(ald, "@U", "@}")






# Print words common to both, but with differing pronunciations, to a file, so we can compare the symbols

f = open("differences.txt", mode="w")

for word in common_words:
    if ald[word] != alveo[word]:
        f.write(word + '\t' + ald[word] + '\t' + alveo[word] + '\n')


# Print final dictionary - merge ALD into MAUS


# ALD has two-word entries, so see which of the single words are not in the alveo dictionary
unique_ald_temp = list(set(ald.keys()) - set(common_words))
unique_ald = dict()
for words in unique_ald_temp:
    split_words = words.split(" ");
    for i in range(0,len(split_words)):
        if split_words[i] not in alveo:
            unique_ald[split_words[i]] = ald[words].split(" ")[i]



f = open("complete.txt", mode="w")
all_word_list = sorted(list(alveo.keys() + unique_ald.keys()))

for word in all_word_list:
    if word in alveo:
        f.write(word.lower() + '\t' + alveo[word] + "\tMAUS" + '\n')
    else:
        f.write(word.lower() + '\t' + unique_ald[word] + "\tALD" + '\n')


f.close()


