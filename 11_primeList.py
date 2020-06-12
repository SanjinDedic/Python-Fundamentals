limit = input('enter a the upper limit: ')
limit = int(limit)
primes =[]

for num in range(2,limit+1):

    counter = 0
    for i in range(1,num+1):
        if(num%i ==0):
            counter = counter + 1
    if(counter == 2):
        primes.append(num)
 

print(primes)
