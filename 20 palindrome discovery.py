#1 convert file to string
text = open('allWords.txt')
text = text.read()

def main():
    global text 
    text = stripPunctuation(text)
    words = lowercaseList(text)
    print(checkPalindrome(words))


#2 strip punctuation
def stripPunctuation(st):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~’“”'
    for c in punctuation:
        st = st.replace(c,'')
    return st

#3 lowercase everything then convert to list
def lowercaseList(st):
    st = st.lower()
    st = st.split()
    return st

#4 reverse a string 
def reverse(string):
    answer = ''
    for i in range(len(string)-1,-1,-1):
        letter = string[i]
        answer = answer +letter
    return answer


#5 check it word == reverse word if so add to palindromes
def checkPalindrome(wordList):
    palindromes = []
    for word in wordList:
        if len(word) > 1:
            if word == reverse(word):
                palindromes.append(word)
    return palindromes 
                

main()
