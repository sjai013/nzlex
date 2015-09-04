__author__ = 'sjai013'

mausFile = open("../alveo/all.txt").read().replace("`","'").split('\n')
mausFile.remove('')
phones = open("SAMPA_phones").read().split('\n')
phones_1ch = list()
phones_2ch = list()
phones.remove('')

for phone in phones:
    if len(phone) == 1:
        phones_1ch.append(phone)
        continue

    if len(phone) == 2:
        phones_2ch.append(phone)
        continue


mausLex = dict()
for line in mausFile:
    line = line.split('\t')
    word_phones = line[1].replace(" ","")
    word_phones_new = list()
    i = 0
    while i < len(word_phones):
        ch = word_phones[i]
        if i < len(word_phones) - 1:
            next_ch = word_phones[i+1]
        else:
            next_ch = ""

        phone_2ch = ch + next_ch

        if phone_2ch in phones_2ch:
            word_phones_new.append(phone_2ch)
            i += 2
        else:
            word_phones_new.append(ch)
            i += 1

    mausLex[line[0]] =  " ".join(word_phones_new)


f = open("../alveo/all_formatted.txt", "w")
for word in mausLex:
    f.write(word + '\t' + mausLex[word] + '\n')

f.close()