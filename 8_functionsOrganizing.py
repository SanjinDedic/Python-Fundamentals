
def main():
    print('please make your selection by entering a number:')
    print('press 1 for computer greeting')
    print('press 2 for times table')
    print('press 3 for factorisation')
    choice = input('your selection: ')
    if choice == '1':
        computerGreeting()
    if choice == '2':
        timesTable()
    if choice == '3':
        factorisation()
    


def computerGreeting():
    print('Hello human what is your name?')
    name = input()
    if(name == 'Sanjin'):
        print('aaah, its you again Sanjin')
    elif(name =='Bob'):
        print('Heey Boob, hows it been')
    elif(name =='Alice'):
        print('Alice you are the best ever of all time')
    else:
        print('I dont know you ' + name + ' go away')
    print('the end')


def timesTable():
    num = input('enter a number: ')
    num = int(num)
    print('here is your times table') 
    for i in range(1,101):
        print(num*i)


def factorisation():
    num = input('enter a number you wish to factorise: ')
    num = int(num)
    counter = 0
    for i in range(1,num+1):
        if(num%i ==0):
            print(str(i) + ' is a factor')
            counter = counter + 1
    if(counter == 2):
       print(str(num) + ' is a prime number')
       
main()



