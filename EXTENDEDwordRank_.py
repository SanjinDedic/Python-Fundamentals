import string
text = open('HarryPotter.txt')
text = text.read()

#allows user to select number of words and the type of word ranking
def menu():
    tot  = int(input('how many words do you want to rank? '))
    print('type 1 for ranking all words and ignoring case')
    print('type 2 for ranking all words and being case sensitive')
    print('type 3 for ranking only capitalised words')
    case = input()
    allWords  = cleanWordList(text,case)
    freqD = frequencyDictionary(allWords)
    printRankedDictionary(freqD,tot)


# generates a list of words with no punctuation
# takes in 3 options for style: 1 = all words ranked case ignored
# 2 = all words ranked and case maintained
# 3 = only capitalised words ranked
def cleanWordList(st,style):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for c in st:
        if c in punctuation:
            st = st.replace(c,'')
    if style == '1':
        st = st.lower()
        return st.split()
    if style == '2':
        return st.split()
    if style == '3':
        titleWords = []
        for word in st.split():
            if word.istitle():
                titleWords.append(word)
        return titleWords
    
# creates a dictionary where the key is a word in a list
# and the value is the number of times that a word repeats
def frequencyDictionary(wordList):
    nonRepeatWords = []
    for word in wordList:
        if word not in nonRepeatWords:
            nonRepeatWords.append(word)
    dictionary = {}
    for word in nonRepeatWords:
        dictionary[word] = wordList.count(word)
    return dictionary

# prints a ranked version of the frequency dictionary
# paramer total choses how many words get printed
def printRankedDictionary(dct,total):
    rankedList = sorted(dct, key=dct.get, reverse = True)
    for i in range(0,total):
        key = rankedList[i]
        value = dct[key]
        print(key + ' repeats ' + str(value) + ' times')

menu()



'''
EXTENSION QUESTIONS
1. Create a function for punctuation free word list
2. Create a function for a frequency dictionary
3. Create a function for printing X members of a ranked dictionary
4. Create a mechanism for ranking capitalised words
5. Create a menu chosing to rank all words or capitalised words only
'''
