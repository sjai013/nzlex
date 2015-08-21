__author__ = 'sjai013'

# Read ALD lexicon (in a transformed SAMPA format)

f = open("../ald/lexicon.txt");
temp = f.readlines();

ald = dict()
for line in temp:
    ald[line.split("\t")[0]] = line.split("\t")[1].replace("\n","")

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
