import re

def findPunctuation(string, start):
    string = str(string)
    string = string[start:]
    #iAux = re.search('[.?!;]|\n\n', string)
    iAux = re.search('[?!;]|\n\n', string)
    try:
        iPunct = int(iAux.start()) + start
    except:
        iPunct = 1000+start
    return iPunct


def findWord(string, start):
    string = str(string)
    string = string[start:]
    iAux = re.search("[\w,.]+", string)  #we accept commas inside the phrases
    try:
        iWord = [int(iAux.start())+start, int(iAux.end())+start]
    except:
        iWord = [1000+start, 1000+start]
    return iWord


def sortDic(dic):
    sortedDic = []
    auxList = []
    for key in dic.keys():
        auxList.append([key, dic[key]])

    restList=[]
    while len(auxList)>0:
        mmax = 0
        mmax_key = ""
        mmax_index = -1
        for iList in range(0,len(auxList)):
            if auxList[iList][1] > mmax:
                mmax = auxList[iList][1]
                mmax_key = auxList[iList][0]
                mmax_index = iList
        sortedDic.append([mmax_key, mmax])
        auxList.pop(mmax_index)

    return sortedDic


from optparse import OptionParser
parser=OptionParser()
opts, args = parser.parse_args()

nameIn = str(args[0])

fileIn = open(nameIn, "r")
fileOut = open("phraseCounts.csv", "w")

text = fileIn.read();

iRead = 0
phraseOccurDic = {}
lastTenWords = []
while iRead < len(text):
    nextPunct = findPunctuation(text, iRead)
    nextWord = findWord(text, iRead)
    
    if nextPunct < nextWord[0]:
        if len(lastTenWords)>0: lastTenWords.clear()
        iRead = nextPunct+1
    else:
        iRead = nextWord[1]
        if len(lastTenWords)>= 10: lastTenWords.pop(0)
        lastWord = text[nextWord[0]:nextWord[1]]
        lastWord = lastWord.lstrip("_")
        lastWord = lastWord.rstrip("_")
        lastWord = lastWord.lower()
        lastTenWords.append(lastWord)

        #new phrases are only those that include the last word
        for iPhraseLength in range(3,len(lastTenWords)+1):
            newPhrase = ""
            for iNum in range(0,iPhraseLength):
                newPhrase += lastTenWords[-iPhraseLength+iNum]
                if iNum < iPhraseLength-1: newPhrase += " "

            newPhrase = newPhrase.rstrip(",.")
            if newPhrase in phraseOccurDic.keys():
                phraseOccurDic[newPhrase] += 1
            else:
                phraseOccurDic[newPhrase] = 1


fileIn.close()

phraseOccurDicCopy = phraseOccurDic.copy()
for phrase in phraseOccurDicCopy.keys():
    if (phraseOccurDicCopy[phrase]<2): del phraseOccurDic[phrase]

sortedPhrases = sortDic(phraseOccurDic)

#remove phrases which are a subset of other phrases
#and remove gutenberg related 
toBeDeleted = []
for iSorted in range(0, len(sortedPhrases)):
    for iSorted2 in range(0, iSorted):
        if sortedPhrases[iSorted][0].find(sortedPhrases[iSorted2][0])>= 0 and sortedPhrases[iSorted][1] == sortedPhrases[iSorted2][1]:
            toBeDeleted.append(sortedPhrases[iSorted2])

for iDel in range(0,len(toBeDeleted)):
    try:
        sortedPhrases.remove(toBeDeleted[iDel])
    except:
        print("already removed")
fileOut.write("Phrase; Number of occurences\n")
for iSorted in range(0, len(sortedPhrases)):
    fileOut.write("%s; %s\n"%(sortedPhrases[iSorted][0], str(sortedPhrases[iSorted][1])))

fileOut.close()
