""" This set of code reads in the original nzlex and adds a closed bracket at the end of every line """

outfile = open("compiled/nzlex.I.txt","w")

# this reads in each line from the original lexicon and strips the EOL character from it. 
#It stores it in a list
lines = [line.strip() for line in open("nzlex.txt")]
#this goes through each line and adds a bracket, and the EOL character, then writes it out to a new file.
for line in lines:
    outfile.write(line + ")" + '\n'	)

outfile.close()
del outfile

""" creating new file which has entries from the original lex, but only from the words of the rev lex"""

revlex = open("nzlex.revised.11.8.2014..out","r")
badlex = open("compiled/nzlex.I.txt","r")

# create lists from the data in the original and revised lexicon
rl_lines=revlex.readlines()
bl_lines=badlex.readlines()

# create lists of words from the two lexicons (first entry on the line)
# Modified by SJ
rl_word=dict()
for line in rl_lines:
    line = line.replace("\" nil (", "\"\tnil\t(")
    item=line.split("\t")
    if len(item) < 2:
        continue
    word = item[0].replace("(","").replace("\"","")
    rl_word[word] = item[2].replace("\"","")

bl_word=dict()
for line in bl_lines:
    line = line.replace("\" nil (", "\"\tnil\t(")
    item=line.split("\t")
    if len(item) < 2:
        continue
    word = item[0].replace("(","").replace("\"","")
    bl_word[word] = item[2].replace("\"","")


#######################################################################################################
###################### Find common words, and print pronunciation (SJ) ################################
#######################################################################################################

# Find words common to revised and original lexicon (SJ)
common_words = sorted(list(set(bl_word.keys()) & set(rl_word.keys())))


outfile = open("compiled/nzlex.II.txt","w")

common_words_dict = dict()
# Print the pronunciation of the common words as defined in the original lexicon (SJ)
for word in common_words:
    outfile.write("(\"" + word + "\"\tnil\t" + bl_word[word])
    common_words_dict[word] = bl_word[word]

outfile.close()
del outfile

#######################################################################################################
############### Find words unique to revised lex, and print pronunciation (SJ) ########################
#######################################################################################################

f = open("compiled/newwords.txt","w")
newWords = dict()
unique_revised_lex = sorted(list(set(rl_word.keys()) - set(common_words)))

for word in unique_revised_lex:
    newWords[word] = rl_word[word].strip()
    f.write("(\"" + word + "\"\tnil\t" + rl_word[word])


f.close()
del f


'''
#####################################################################################################
#################### Find all words that have a modified pronunciation ##############################
#####################################################################################################

# Find all words that differ in pronunciation between revised lexicon and original lexicon.  Remove all redundant
# characters, such as numbers, brackets, dashes, and spaces, before comparing.

outfile = open("modified_words.txt","w")

modified_words = dict()

for word in sorted(common_words_dict):
    revised_pronunciation = rl_word[word].translate(None,'123456789() ')
    orig_pronunciation = common_words_dict[word].translate(None,'123456789()- ')

    if (revised_pronunciation != orig_pronunciation):
        modified_words[word] = rl_word[word]
        outfile.write("(\"" + word + "\"\tnil\t" + modified_words[word])


del outfile
'''


#####################################################################################################
################# Parse Macaulay dictionary, and find oul, uul and drug words #######################
#####################################################################################################

mac_lex = open("nzlex.macaulay.v1.out","r")
mac_lines=mac_lex.readlines()
mac_lex.close()


mac_words=dict()
for line in mac_lines:
    line = line.replace("\" nil (", "\"\tnil\t(").replace("\r\n","").replace(" ;;","\t;;",1)
    item=line.split("\t")
    if len(item) < 2:
        continue
    word = item[0].replace("(","").replace("\"","")
    if len(item) > 2:
        mac_words[word] = item[2:]
        mac_words[word][0] = mac_words[word][0].replace("\"","")
        if len(mac_words[word]) > 1:
            mac_words[word][1] = mac_words[word][1].replace(" ","").replace(";;","",1).split(";;")


# The dict data structure now looks like this: [word/key] : [pronunciation] [list of comments (optional)]
# Write all words to file, which match a list of pre-defined tags

tagsToPrint = ["oul", "uul", "drug", "maori", "contraction"]
mac_words_modified = dict()
mac_lex_out = open("compiled/macaulay_mods.txt", "w")
for word in sorted(mac_words):
    if len(mac_words[word]) > 1:
        if len(set(mac_words[word][1]) & set(tagsToPrint)) > 0:
            mac_lex_out.write("(\"" + word + "\"\tnil\t" + mac_words[word][0] + "\t;;" + ','.join(mac_words[word][1]) + '\n')
            mac_words_modified[word] = mac_words[word]

mac_lex_out.close()

#####################################################################################################
################# Find all 'ing' words that have /i n/ and replace with /i ng/ ######################
#####################################################################################################

outfile = open("compiled/modified_words.ing.txt","w")

ing_words = dict()
for word in sorted(common_words_dict):
    if word.endswith("ing"):
        pronunciation_temp = common_words_dict[word].translate(None,'01() \n')
        if pronunciation_temp.endswith("in"):
            pronunciation = common_words_dict[word][::-1].replace("i n"[::-1],"i ng"[::-1],1)[::-1]
            ing_words[word] = pronunciation
            outfile.write("(\"" + word + "\"\tnil\t" + ing_words[word])


outfile.close()

del outfile


#####################################################################################################
################# Compile final list of all modified words (new, Mac, and ing) ######################
#####################################################################################################

all_new_words_temp = list(set(ing_words) | set(mac_words_modified) | set(newWords))
all_new_words = dict()

outfile = open("compiled/all_modified_words.txt","w")
for word in sorted(all_new_words_temp):
    # Order of priority is (most important to least important): new -> Macaulay -> ing modification
    if word in unique_revised_lex:
        all_new_words[word] = newWords[word].strip() + '\t' + ';; unique'

    elif word in mac_words_modified:
        all_new_words[word] = mac_words_modified[word][0] + '\t;; ' + ', '.join(mac_words_modified[word][1])
    elif word in ing_words:
        all_new_words[word] = ing_words[word].strip() + '\t' + ';; ing'
    else:
        print "Error with word: " + word

    outfile.write("(\"" + word + "\"\tnil\t" + all_new_words[word].strip() + '\n')

outfile.close()