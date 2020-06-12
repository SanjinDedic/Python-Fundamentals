import time, random

rounds = input('How many games do you want to play: ')
rounds = int(rounds)
print('when I say __GO__ you hit ENTER!. got it?')
times = []

for i in range(0,rounds):
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

average = sum(times) / rounds

print('fastest time was: ' + str(min(times)))
print('slowest time was: ' + str(max(times)))
print('the average time was: ' + str(average))


