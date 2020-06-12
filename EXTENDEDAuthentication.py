import time

userPasswords = {'Sanjin':'Abc123', 'Bob':'aaa','Alice':'Yolo','Ana':'Block',
                 'Dozer':'Zion',}

accessGranted = False

while accessGranted == False:
    inName = input('please enter your username: ')
    if inName in userPasswords:
        goodPassword = False
        while goodPassword == False: 
            inPassword = input('please enter your password: ')   
            if inPassword == userPasswords[inName]:
                goodPassword = True
                accessGranted = True
                print('waiting .')
                time.sleep(1)
                print('waiting ..')
                time.sleep(1)
                print('waiting ...')
                time.sleep(1)
            else: # say invalid password
                print('waiting .')
                time.sleep(1)
                print('waiting ..')
                time.sleep(1)
                print('waiting ...')
                time.sleep(1)
                print('that is not a valid password')
    else: # say user name is invalid
        print('that is not a valid user name')

print('ACCESS GRANTED')
