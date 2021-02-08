import re

from optparse import OptionParser
parser=OptionParser()
opts, args = parser.parse_args()

nameIn = str(args[0])

fileIn = open(nameIn, "r")
fileOut = open("wordCounts.csv", "w")

wordOcurrencesDic = {}

for line in fileIn.readlines():
    wordsInLine = re.findall(r'\w+', line)
    for word in wordsInLine:
        word = word.lstrip("_")
        word = word.lower()

        if not word in wordOcurrencesDic.keys():
            wordOcurrencesDic[word] = 1
        else:
            wordOcurrencesDic[word] += 1

fileIn.close()

fileOut.write("Word, Number of occurences\n")
for word in wordOcurrencesDic.keys():
    fileOut.write("%s, %s\n"%(word, str(wordOcurrencesDic[word])))

fileOut.close()
