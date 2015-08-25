__author__ = 'sjai013'

f = open("mansfield_corpus.txt","r")
lines = f.readlines();
f.close()

unique_mansfield_words = dict()
for line in lines:
    line = line.translate(None,'\r\n.,?').lower().strip()
    wordsInLine = line.split(' ')
    for word in wordsInLine:
        word = word.strip("'")
        if (word not in unique_mansfield_words):
            unique_mansfield_words[word] = 1
        else:
            unique_mansfield_words[word] = unique_mansfield_words[word] + 1


f = open("unique_mansfield_words.txt", "w")

for word in sorted(unique_mansfield_words):
    f.write(word + '\t' + str(unique_mansfield_words[word]) + '\n')

f.close()

f = open("all_transcripts.txt")
lines = f.readlines();
f.close()

unique_transcript_words = dict()
for line in lines:
    line = line.translate(None,'\r\n.,?`').lower().strip()
    wordsInLine = line.split(' ')
    for word in wordsInLine:
        word = word.strip("'")

        if (word.isdigit()):
            continue

        if word == "":
            continue

        if word not in unique_transcript_words:
            unique_transcript_words[word] = 1
        else:
            unique_transcript_words[word] += 1


f = open("unique_transcript_words.txt", "w")

for word in sorted(unique_transcript_words):
    f.write(word + '\t' + str(unique_transcript_words[word]) + '\n')

f.close()

all_unique_words_temp = list(set(unique_mansfield_words) | set(unique_transcript_words))
all_unique_words = dict()

f = open("all_unique_words.txt","w")

for word in sorted(all_unique_words_temp):
    numberOccurences = 0
    if word in unique_mansfield_words:
        numberOccurences += unique_mansfield_words[word]

    if word in unique_transcript_words:
        numberOccurences += unique_transcript_words[word]

    all_unique_words[word] = numberOccurences
    f.write(word + '\t' + str(all_unique_words[word]) + '\n')

f.close()
