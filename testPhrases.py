import os
import csv

from optparse import OptionParser
parser=OptionParser()
opts, args = parser.parse_args()

textIn = str(args[0])
expectedPhraseIn = str(args[1])

fileRefCSV = open(expectedPhraseIn, 'r')
readerRef=csv.reader(fileRefCSV, delimiter=";")

phrase = ""
times = 0
for row in readerRef:
    if ("Phrase" in row[0]) or ("phrase" in row[0]):
        continue
    else:
        phrase = row[0]
        times = row[1]
        break

print("The most common phrase is supposed to be '%s' appearing %s time(s)"%(phrase, times))
fileRefCSV.close()

os.system("python3 findPhrases.py "+textIn)

fileCSV = open("phraseCounts.csv", 'r')
reader=csv.reader(fileCSV, delimiter=";")
phrase = ""
times = 0
for row in reader:
    if "Phrase" in row[0]:
        continue
    else:
        phrase = row[0]
        times = row[1]
        break

print("It is '%s' appearing %s time(s)"%(phrase, times))

fileCSV.close()
