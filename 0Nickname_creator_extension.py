print('Hello human what is your name?')
name = input()
print('Hello ' + name)
if name[-1] not in 'aeiou':
    nickname = name + name[-1] + 'y'
else:
    nickname = name + name[-1]

print('I will call you ' + nickname)



'''
EXTENSION QUESTIONS
1. Create your own nickname variation
2. Use nickname.upper() to create an upper case nickname
3. name[0] is the first letter of the name and name[-1]
is the last letter. Use one of these to create a nickname
'''
