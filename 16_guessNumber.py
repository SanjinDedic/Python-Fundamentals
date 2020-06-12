import random

xNum = random.randint(1,100)
found = False
counter = 0

while found  == False:
    yourNum = int(input('please guess a number 1-100: '))
    counter = counter +1
    # too big
    if yourNum > xNum:
        print('too big')
    # too small
    elif yourNum < xNum:
        print('too small')
    # correct
    else:
        print('well done you guessed the number')
        print('it took you ' + str(counter) + ' tries')
        found = True
        
#Extension Questions
#1 Can you tell the user if they are close when the number is off by 10 or less

#2 Can you have a custom response to a number that is above 100 or below 1

#3 Can you create a custom response for a non numeric input
