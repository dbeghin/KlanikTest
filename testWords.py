import os
import csv

from optparse import OptionParser
parser=OptionParser()
opts, args = parser.parse_args()

textIn = str(args[0])
expectedCountsIn = str(args[1])

os.system("python3 countWords.py "+textIn)

print("Expected counts in test file:")
fileRefCSV = open(expectedCountsIn, 'r')
readerRef=csv.reader(fileRefCSV, delimiter=",")
for row in readerRef:
    if ("Word" in row[0]) or ("word" in row[0]):
        continue
    else:
        print("%s: %s"%(row[0], row[1]))


print("\n\nFound counts:")
fileCSV = open("wordCounts.csv", 'r')
reader=csv.reader(fileCSV, delimiter=",")
phrase = ""
times = 0
for row in reader:
    if "Word" in row[0]:
        continue
    else:
        print("%s: %s"%(row[0], row[1]))

fileCSV.close()
