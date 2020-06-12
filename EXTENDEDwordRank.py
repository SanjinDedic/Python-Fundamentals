import string
text = open('HarryPotter.txt')
text = text.read()

def menu():
    tot = int(input('how many ranked words do you want to print: '))
    print('type 1 for ranking all words and ignoring case')
    print('type 2 for ranking all words and maintaining case')
    print('type 3 for ranking only capitalised words')
    case = input()
    allWords = cleanWordList(text,case)
    freqDictionary = frequencyDictionary(allWords,case)
    printRankedDictionary(freqDictionary,tot)
    
def cleanWordList(text,style):
    clearingSymbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~’‘'
    for c in text:
        if c in clearingSymbols:
            text.replace(c,'')
    if style == '1':
        text = text.lower()
    return text.split()

def frequencyDictionary(wordList,style):
    nonRepeatWords = []
    dictionary = {}
    print(style)
    if style == '3':
        capList = []
        for word in wordList:
            if word.istitle():
                capList.append(word)
        print(capList)
        wordList = capList


    for word in wordList:
        if word not in nonRepeatWords:
            nonRepeatWords.append(word)
    for word in nonRepeatWords:
        dictionary[word] = wordList.count(word)
    return dictionary

def printRankedDictionary(dct,total):
    rankedList =sorted(dct, key=dct.get, reverse = True)
    for i in range(0,total):
        key = rankedList[i]
        value = dct[key]
        print(key+' repeats '+str(value) +' times')

menu()
    
'''
EXTENSION QUESTIONS
1. Create a function for punctuation free word list
2. Create a function for a frequency dictionary
3. Create a function for printing X members of a ranked dictionary
4. Create a mechanism for ranking capitalised words
5. Create a menu chosing to rank all words or capitalised words only
'''
