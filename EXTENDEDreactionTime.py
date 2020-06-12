import time, random

rounds = int(input('How many rounds do you want to play?'))
times = []

for i in range(0,rounds):
    print('when I say __GO__ you hit ENTER!. got it?')
    time.sleep(1)
    print('ready')
    time.sleep(1)
    print('steady')
    time.sleep(random.randint(2,5))
    print('#####__GO__######')
    tic = time.clock()
    a = input()
    toc = time.clock()
    timeSpent = toc-tic
    times.append(timeSpent)
    print('your time was '+str(timeSpent) + ' seconds')


print('fastest time was ' + str(min(times)))
print('slowest time was ' + str(max(times)))
average = sum(times)/len(times) 
print('the average time was ' + str(average))

'''
EXTENSION QUESTIONS:

1. Ask the user how many rounds they want to play 
2. Save the users reaction times in a list 
3. At the end of the game print the following 
    fastest time 
    slowest time
    average time

'''
