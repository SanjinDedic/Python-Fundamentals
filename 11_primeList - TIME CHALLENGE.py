import time
limit = 2000
primes =[]
tic = time.clock()

for num in range(2,limit+1):
    counter = 0
    for i in range(1,num+1):
        if(num%i ==0):
            counter = counter + 1
    if(counter == 2):
        primes.append(num)
        
toc = time.clock()
print(toc-tic)
print(len(primes))

