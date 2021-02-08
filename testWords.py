import os
import csv

os.system("python3 countWords.py numbertest.txt")

print("Counts in test file:")
print("zero: 2")
print("one: 13")
print("two: 3")
print("three: 3")
print("four: 2")
print("five: 2")
print("six: 2")
print("seven: 2")
print("eight: 2")
print("nine: 2")

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
