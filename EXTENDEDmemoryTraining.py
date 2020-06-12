import random,time
text = open('1000EnglishWords.txt')
text = text.read()

def menu():
    items = input('How many items do you want to guess: ')
    items = int(items)
    print('type 1 to guess numbers')
    print('type 2 to guess words')
    choice = input()
    if choice == '1':
        memoryList = numberSequence(items)
    if choice == '2':
        memoryList = wordSequence(text,items)
    print(memoryList)
    time.sleep(5)
    hide()
    check(memoryList,items)

def numberSequence(items):
    sequence = []
    for i in range(0,items):
        sequence.append(str(random.randint(0,9)))
    return sequence

def wordSequence(textInput,items):
    wordList = textInput.split()
    sequence = []
    for i in range(0,items):
        sequence.append(random.choice(wordList))
    return sequence

def check(memoryList,items):
    for i in range(0,items):
        print('enter number at index ' +str(i))
        num = input()
        if num == memoryList[i]:
            print('correct')
        else:
            print('WRONG')
            break
    print('WELL DONE YOU WIN')

def hide():   
    for i in range(0,50):
        print('')

menu()



'''
EXTENSION QUESTIONS:
1. Create a menu to chose if you want to memorise words or numbers
2. Create a function to generate random sequences of numbers 
3. Create a function to generate random sequences of words
'''
