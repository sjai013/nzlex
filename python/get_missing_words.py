__author__ = 'sjai013'

# Get list of all words in the NZ dictionary
f = open("nz_dict/compiled/all_modified_words.txt", 'r')
all_modified_words_temp = f.readlines()
f.close()

all_modified_words = dict()

for word in all_modified_words_temp:
    word = word.split('\t')
    word[0] = word[0].translate(None,"(\")")
    all_modified_words[word[0]] = word[2:]

del f, all_modified_words_temp

# Get a list of all words in the alveo MAUS dictionary
f = open("complete.txt")
alveo_temp = f.readlines()
f.close()

alveo = dict()
for word in alveo_temp:
    line = word.split('\t')
    alveo[line[0]] = line[1].strip()

del f, alveo_temp


# Get list of all unique words
f = open("all_unique_words.txt",'r')
unique_words_temp = f.readlines()
f.close()

unique_words = dict()

for word in unique_words_temp:
    word = word.split('\t')
    unique_words[word[0]] = word[1].strip()

del f, unique_words_temp
# Compare unique words and NZ dictionary, and get all unique words NOT in the NZ or MAUS dictionary
nz_maus_words = list(set(all_modified_words) | set(alveo))
missing_corpus_words_temp = list(set(unique_words) - set(nz_maus_words))
missing_corpus_words = dict()

for word in missing_corpus_words_temp:
    words = word.split("-")
    for word in words:
        missing_corpus_words[word] = ""


# Get all words in the NZ/MAUS lexicon, that aren't in the 5000 most common word list
f = open("nz_dict/5000_most_common.txt")
most_common_words_temp = f.readlines();
f.close()

most_common_words = dict()
for line in most_common_words_temp:
    word = line.split()[1]
    most_common_words[word] = ""


missing_common_words_temp = list(set(most_common_words) - set(nz_maus_words))
missing_common_words = dict()

for item in missing_common_words_temp:
    # For hyphenated words, only put in the words that are not already in the lexicon, or missing words list
    words = item.split("-")
    for word in words:
        if (word not in missing_common_words) | (word not in nz_maus_words):
            missing_common_words[word] = ""




f = open("nz_dict/compiled/words_to_add.txt", "w")
for word in sorted(missing_common_words):
        f.write(word + '\n')

f.close()


# Recreate list of missing corpus words by removing all common words, and breaking hyphenated words into separate words
missing_corpus_words = list(set(missing_corpus_words) - set(missing_common_words))


# Print all words that are in the corpus, but are not included in the missing_common_words list
f = open("nz_dict/compiled/missing_corpus_words.txt", "w")
for word in sorted(missing_corpus_words):
    f.write(word + '\n')

f.close()
del f
