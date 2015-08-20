__author__ = 'sjai013'

f = open("../ald/lexicon.txt");
a = f.readlines();

ald = dict()
for line in a:
    ald[line.split()[0]] = line.split()[1]


f = open("../alveo/all.txt")
a = f.readlines();

alveo = dict()
for line in a:
    alveo[line.split(",")[0]] = line.split(",")[1].replace("\n","")

