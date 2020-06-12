import time, random

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
print('your time was '+str(timeSpent) + ' seconds')
