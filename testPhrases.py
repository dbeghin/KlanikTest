import os
import csv

os.system("python3 findPhrases.py numbertest.txt")

print("The most common phrase is supposed to be 'one two three' appearing 2 times")

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
