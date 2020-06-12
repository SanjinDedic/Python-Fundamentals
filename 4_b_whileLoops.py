num = input('enter a number: ')
num = int(num)

print('here is your times table') 


counter = 1

while counter <= 10:
    print(counter * num)
    counter = counter + 1


num = input('enter a number: ')
num = int(num)

print('Here are all multiples of', num, 'under 100')

counter = 1

while num * counter < 100:
    print(num * counter)
    counter = counter + 1
