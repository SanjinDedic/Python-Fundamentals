num = input('enter a number you wish to factorise: ')
num = int(num)

for i in range(1,num+1):
    if(num%i ==0):
        print(str(i) + ' is a factor')
