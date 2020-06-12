import string
text = open('HarryPotter.txt')
text = text.read()

#1. strip punctuation
clearingSymbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~’‘'
for c in text:
    if c in clearingSymbols:
        text.replace(c,'')
        
#2. convert text to a list of lowercase words
text = text.lower()
allWords = text.split()
nonRepeatWords = []
dictionary = {}

#3. create a non repeating list of words

for word in allWords:
    if word not in nonRepeatWords:
        nonRepeatWords.append(word)

#4 Create a dictionary where every non repeating word is a key
# and count of how many times word appears in text is a value
for word in nonRepeatWords:
    dictionary[word] = allWords.count(word)


#5 Use sorted function to print the ranked value of this dictionary
rankedList =sorted(dictionary, key=dictionary.get, reverse = True)

for i in range(0,100):
    key = rankedList[i]
    value = dictionary[key]
    print(key+' repeats '+str(value) +' times')
    
'''
EXTENSION QUESTIONS
1. Create a function for punctuation free word list
2. Create a function for a frequency dictionary
3. Create a function for printing X members of a ranked dictionary
4. Create a mechanism for ranking capitalised words
5. Create a menu chosing to rank all words or capitalised words only
'''

