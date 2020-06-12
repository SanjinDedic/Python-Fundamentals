username = 'Bobo'
password = 'Abc123'
username2 = 'Sanjin'
password2 = 'passwordy'

inName = input('please enter your username: ')
if inName == username or inName == username2:
    inPassword = input('please enter your password: ')
    if inName == username and inPassword == password:
        print('ACCESS GRANTED')
    elif inName == username2 and inPassword == password2:
        print('ACCESS GRANTED')
    else: # say invalid password
        print('that is not a valid password')
else: # say user name is invalid
    print('that is not a valid user name')
