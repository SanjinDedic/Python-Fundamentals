import random,time

#get a sequence length from the user
digits = input('How many digits do you want to guess: ')
digits = int(digits) 

#create a random sequence
sequence = []
for i in range(0,digits):
    sequence.append(random.randint(0,9))
print(sequence)
    
#show it for 5 seconds
time.sleep(5)
# hide the sequence
for i in range(0,50):
    print('')


#check if the user can recall the sequence

for i in range(0,digits):
    print('enter number at index ' +str(i))
    num = int(input())
    if num == sequence[i]:
        print('correct')
    else:
        print('WRONG')
        break

print(sequence)
