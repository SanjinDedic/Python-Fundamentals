print('Hello human what is your name?')
name = input()
print('Hello ' + name)

if name[-1] not in 'aeiouy':
    nickname = 'Captain ' + name + 'y'
else:
    nickname = 'Captain ' + name + name[-1]
    
print('I will call you ' + nickname.upper())



'''
EXTENSION QUESTIONS
1. Create your own nickname variation
2. Use nickname.upper() to create an upper case nickname
3. name[0] is the first letter of the name and name[-1]
is the last letter. Use one of these to create a nickname
'''
