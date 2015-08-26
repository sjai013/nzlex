__author__ = 'sjai013'

from xml.dom import minidom
xmldoc = minidom.parse("nz_dict/compiled/missing_common_words_lts.txt")

items = xmldoc.getElementsByTagName('t')

f = open("nz_dict/compiled/missing_word_pronunciations.txt","w")
for item in items:
    if 'ph' in item.attributes.keys():
        f.write(item.attributes['ph'].value + '\n')


f.close()



from xml.dom import minidom
xmldoc = minidom.parse("nz_dict/compiled/missing_corpus_words_lts.txt")

items = xmldoc.getElementsByTagName('t')

f = open("nz_dict/compiled/missing_corpus_pronunciations.txt","w")
for item in items:
    if 'ph' in item.attributes.keys():
        f.write(item.attributes['ph'].value + '\n')


f.close()

