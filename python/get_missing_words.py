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

# Get list of all unique words
f = open("all_unique_words.txt",'r')
unique_words_temp = f.readlines()
f.close()

unique_words = dict()

for word in unique_words_temp:
    word = word.split('\t')
    unique_words[word[0]] = word[1].strip()

del f, unique_words_temp
# Compare unique words and NZ dictionary, and get all unique words NOT in the NZ dictionary
missing_words = list(set(unique_words) - set(all_modified_words))

f = open("missing_words.txt", "w")
for word in sorted(missing_words):
    f.write(word + '\t' + unique_words[word] + '\n')

f.close()
del f