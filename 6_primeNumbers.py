num = input('enter a number you wish to factorise: ')
num = int(num)

counter = 0

for i in range(1,num+1):
    if(num%i ==0):
        print(str(i) + ' is a factor')
        counter = counter + 1

if(counter == 2):
   print(str(num) + ' is a prime number') 

        
