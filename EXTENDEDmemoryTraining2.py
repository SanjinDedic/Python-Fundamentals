import random,time
text = open('1000EnglishWords.txt')
text = text.read()

#allows user to select num of items and numbers or words
def menu():
    items = input('How many items do you want to guess: ')
    items = int(items)
    print('type 1 for guessing numbers and 2 for guessing words')
    choice = input()
    if choice == '1':
        memoryList = numberSequence(items)
    if choice == '2':
        memoryList = wordSequence(items,text)
    print(memoryList)
    hide()
    check(items,memoryList)

#returns a sequence of random numbers of numItems length    
def numberSequence(numItems):
    sequence = []
    for i in range(0,numItems):
        sequence.append(str(random.randint(0,9)))
    return sequence

#returns a sequence of random words of numItems length 
def wordSequence(numItems,textInput):
    wordList =textInput.split()
    sequence = []
    for i in range(0,numItems):
        sequence.append(str(random.choice(wordList)))
    return sequence

#hides the sequence the user needs to memorise after 5 seconds
def hide():
    time.sleep(5)
    for i in range(0,50):
        print('')

#checks users answer to each member of the sequence
def check(numItems,memList):
    for i in range(0,numItems):
        print('enter number at index ' +str(i))
        ans = input()
        if ans == memList[i]:
            print('correct')
        else:
            print('WRONG')
            return None
    print('WELL DONE YOU GOT IT RIGHT!!')

menu()

'''
EXTENSION QUESTIONS:

1. Use a word list and then select and guess random words instead of
numbers
2. Create a menu at the start allowing the user to guess either words
or numbers
3. Simplify the code using functions 
'''
